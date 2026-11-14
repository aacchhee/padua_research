#!/usr/bin/env bash
# Re-run the computer-assisted and measured parts of MZ-SP from this archive and
# compare them with the committed receipts. Usage: bash verify.sh [OUTDIR] [--regenerate]
#   --regenerate  also rebuild the three witnesses from scratch (eigensolver +
#                 exact rounding, about 5 minutes); otherwise the archived
#                 witnesses are replayed (about 3 minutes).
# Needs Python 3.12 with requirements.txt installed (set PY to the interpreter),
# a C compiler and GMP (libgmp-dev) for the bracket certificates.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTARG="${1:-$HERE/verify-out}"; REGEN="${2:-}"
OUT="$(mkdir -p "$OUTARG" && cd "$OUTARG" && pwd)"
PY="${PY:-python3}"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
CMP="$PY $HERE/tools/compare_receipts.py"
cd "$HERE/repository"
C=topics/padua-mz-cleanup-20261105
F=topics/padua-mz-2d-frontier-20261105
S=topics/padua-mz-sharp-constants-20261106
fail=0

echo "== Prop 8.2 (PD-T376): payload identities of the archived witnesses"
(cd "$HERE/data/witnesses" && for M in 1101 1240 1600; do
   printf '%s  cert-m%s/witness.json\n' "$(gzip -dc cert-m$M/witness.json.gz | sha256sum | cut -d' ' -f1)" "$M"
   printf '%s  cert-m%s/exact-norm.txt\n' "$(sha256sum < cert-m$M/exact-norm.txt | cut -d' ' -f1)" "$M"
 done) > "$OUT/payload-identities.txt"
diff <(sort "$OUT/payload-identities.txt") <(sort "$HERE/data/witnesses/PAYLOAD-SHA256.txt") && echo "AGREE  payload identities" || { echo "DIFFER payload identities"; fail=1; }

for M in 1101 1240 1600; do
  W="$HERE/data/witnesses/cert-m$M/witness.json.gz"
  echo "== Prop 8.2, m=$M: exact producer replay of the archived witness"
  $PY $C/code/rigorous_witness.py --m $M --witness "$W" --scratch "$OUT/replay-m$M" --output "$OUT/producer-m$M.json" > "$OUT/producer-m$M.log"
  # A replay from the archived witness has no float source vector, so that one field is skipped.
  $CMP "$OUT/producer-m$M.json" $C/evidence/witness-producer-m$M.json --ignore 'witness\.source_vector_sha256$' || fail=1
  echo "== Prop 8.2, m=$M: independent Arb/forward-error checker"
  $PY $C/code/independent_witness.py --witness "$W" --output "$OUT/independent-m$M.json" > "$OUT/independent-m$M.log"
  $CMP "$OUT/independent-m$M.json" $C/evidence/witness-independent-m$M.json || fail=1
done

if [ "$REGEN" = "--regenerate" ]; then
  echo "== Prop 8.2: regenerate the witnesses from scratch (eigensolver, then exact rounding)"
  (cd $C/code && $PY g1_minimum.py --m 1101 1240 1600 --output "$OUT/regen/scan.json" --vector-dir "$OUT/regen/vectors" > "$OUT/regen-scan.log")
  for M in 1101 1240 1600; do
    cmp "$OUT/regen/vectors/m$M-n$((M-1))-min.npy" "$HERE/data/source-vectors/m$M-n$((M-1))-min.npy" && echo "AGREE  source vector m=$M" || { echo "DIFFER source vector m=$M (expected on other platforms; the replay above is the certificate)"; }
    $PY $C/code/rigorous_witness.py --m $M --vector "$OUT/regen/vectors/m$M-n$((M-1))-min.npy" --scratch "$OUT/regen/cert-m$M" --output "$OUT/regen/producer-m$M.json" > "$OUT/regen/producer-m$M.log"
    [ "$(gzip -dc "$OUT/regen/cert-m$M/witness.json.gz" | sha256sum | cut -d' ' -f1)" = "$(gzip -dc "$HERE/data/witnesses/cert-m$M/witness.json.gz" | sha256sum | cut -d' ' -f1)" ] && echo "AGREE  regenerated witness payload m=$M" || echo "DIFFER regenerated witness payload m=$M"
  done
fi

echo "== Prop 8.1: certified brackets m=10,20,30,40,60,80 (producer, then independent checker)"
$PY $F/code/cert_native.py --m 10 20 30 40 60 80 --scratch "$OUT/cert-native" --output-dir "$OUT/brackets" > "$OUT/brackets.log"
for M in 10 20 30 40 60 80; do
  $CMP "$OUT/brackets/cert-m$M.json" $F/evidence/cert-m$M.json || fail=1
  $PY $F/code/independent_cert.py --producer-receipt "$OUT/brackets/cert-m$M.json" --scratch "$OUT/independent-cert" --output "$OUT/brackets/independent-cert-m$M.json" > "$OUT/independent-cert-m$M.log"
  $CMP "$OUT/brackets/independent-cert-m$M.json" $F/evidence/independent-cert-m$M.json || fail=1
done

echo "== Props 6.8, 6.9: rectangle enclosure of ||B||"
$PY $S/code/P1_rectangle.py --N 16 --theta 256 --output "$OUT/P1-rectangle-N16.json" > "$OUT/P1-N16.log"
# The program hashes ideas/P1-numeric-protocol.md and theory/P1-rectangle-certificate.md. The
# committed receipts hashed the versions at commit c1e6e59d (archived in data/protocol-history/);
# both files were later extended. Check those identities, then compare everything else.
for KEY in protocol_sha256:ideas-P1-numeric-protocol-c1e6e59d.md reduction_sha256:theory-P1-rectangle-certificate-c1e6e59d.md; do
  REF=$($PY -c "import json,sys;print(json.load(open(sys.argv[1]))[sys.argv[2]])" $S/evidence/P1-rectangle-N16.json "${KEY%%:*}")
  [ "$(sha256sum < "$HERE/data/protocol-history/${KEY#*:}" | cut -d' ' -f1)" = "$REF" ] \
    && echo "AGREE  ${KEY#*:} matches ${KEY%%:*} of the receipt" || { echo "DIFFER ${KEY#*:}"; fail=1; }
done
$CMP "$OUT/P1-rectangle-N16.json" $S/evidence/P1-rectangle-N16.json --ignore '^(protocol|reduction)_sha256$' || fail=1
$PY $S/code/P1_rectangle.py --N 8 --theta 64 --output "$OUT/P1-rectangle-N8.json" > "$OUT/P1-N8.log"
$CMP "$OUT/P1-rectangle-N8.json" $S/evidence/P1-rectangle-N8.json --ignore '^(protocol|reduction)_sha256$' || fail=1

echo "== Section 8.3 (MEASURED): item (1) via the float64 reproduction suites"
for SUITE in padua marginal; do
  $PY tracks/mz-constants/code/reproduce.py --suite $SUITE --max-N 1280 --output "$OUT/reproduction-$SUITE.json" > "$OUT/reproduction-$SUITE.log" 2>&1
done
echo "   (compare with data/measurements/reproduction-*.json; items (2)-(4): see README)"
$CMP "$OUT/reproduction-padua.json" "$HERE/data/measurements/reproduction-padua.json" || fail=1
$CMP "$OUT/reproduction-marginal.json" "$HERE/data/measurements/reproduction-marginal.json" || fail=1

if [ "$fail" = 0 ]; then echo "ALL CHECKS AGREE"; else echo "SOME CHECKS DIFFER (see above)"; exit 1; fi
