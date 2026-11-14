#!/usr/bin/env bash
# Re-run the computer-assisted and measured parts of MZ-SP from this archive and
# compare them with the committed receipts.
#   Usage: [PY=interpreter] bash verify.sh [OUTDIR] [--regenerate]   (arguments in any order)
# PY may be a command on PATH (default python3) or a path such as venv/bin/python;
# a relative path is taken relative to the directory you run the command from.
# Needs Python 3.12 with requirements.txt installed, a C compiler and GMP (libgmp-dev).
#
# Required checks (always run): replay of the archived certificates, compared with the
# committed receipts. Their outcome alone decides whether the archive verifies.
# Optional --regenerate (about 5 more minutes): rebuild the three Prop 8.2 witnesses from
# scratch (seeded eigensolver, then exact rounding) and compare them with the archive. The
# eigensolver is floating point, so its vectors may differ on other platforms; that is
# reported as a NOTE. A regenerated witness payload that differs from the archived one is
# reported as such. Neither affects the archived certificates, which are replayed exactly.
# Exit status: 0 = all required checks agree (and, with --regenerate, the archived payloads
# were reproduced); 1 = a required check failed; 2 = all required checks agree but the
# optional regeneration did not reproduce the archived payloads. The last lines say which.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTARG="$HERE/verify-out"; REGEN=""
for a in "$@"; do
  if [ "$a" = "--regenerate" ]; then REGEN="$a"; else OUTARG="$a"; fi
done
OUT="$(mkdir -p "$OUTARG" && cd "$OUTARG" && pwd)"
PY="${PY:-python3}"
# Resolve a path-like interpreter against the invocation directory *before* changing
# directory; a bare command name is looked up on PATH as usual.
case "$PY" in
  /*) ;;
  */*) PY="$(cd "$(dirname "$PY")" && pwd)/$(basename "$PY")" ;;
esac
command -v "$PY" >/dev/null 2>&1 || { echo "Python interpreter not found: $PY"; echo "REQUIRED CHECKS FAILED"; exit 1; }
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
cd "$HERE/repository" || exit 1
C=topics/padua-mz-cleanup-20261105
F=topics/padua-mz-2d-frontier-20261105
S=topics/padua-mz-sharp-constants-20261106
fail=0
# run LOG CMD...: run a program with its output in LOG; a nonzero exit is a failed required check.
run() { local log="$1"; shift; "$@" > "$log" 2>&1 || { echo "FAILED (exit $?; log $log): $*"; fail=1; return 1; }; }
# cmpr FRESH REFERENCE [--ignore REGEX ...]: field-by-field receipt comparison (required).
cmpr() { "$PY" "$HERE/tools/compare_receipts.py" "$@" || fail=1; }
payload() { gzip -dc "$1" | sha256sum | cut -d' ' -f1; }

echo "== Prop 8.2 (PD-T376): payload identities of the archived witnesses"
(cd "$HERE/data/witnesses" && for M in 1101 1240 1600; do
   printf '%s  cert-m%s/witness.json\n' "$(gzip -dc cert-m$M/witness.json.gz | sha256sum | cut -d' ' -f1)" "$M"
   printf '%s  cert-m%s/exact-norm.txt\n' "$(sha256sum < cert-m$M/exact-norm.txt | cut -d' ' -f1)" "$M"
 done) > "$OUT/payload-identities.txt"
if diff <(sort "$OUT/payload-identities.txt") <(sort "$HERE/data/witnesses/PAYLOAD-SHA256.txt") > /dev/null; then
  echo "AGREE  payload identities"
else
  echo "DIFFER payload identities"; fail=1
fi

for M in 1101 1240 1600; do
  W="$HERE/data/witnesses/cert-m$M/witness.json.gz"
  echo "== Prop 8.2, m=$M: exact producer replay of the archived witness"
  # A replay from the archived witness has no float source vector, so that one field is skipped.
  run "$OUT/producer-m$M.log" "$PY" $C/code/rigorous_witness.py --m $M --witness "$W" --scratch "$OUT/replay-m$M" --output "$OUT/producer-m$M.json" \
    && cmpr "$OUT/producer-m$M.json" $C/evidence/witness-producer-m$M.json --ignore 'witness\.source_vector_sha256$'
  echo "== Prop 8.2, m=$M: independent Arb/forward-error checker"
  run "$OUT/independent-m$M.log" "$PY" $C/code/independent_witness.py --witness "$W" --output "$OUT/independent-m$M.json" \
    && cmpr "$OUT/independent-m$M.json" $C/evidence/witness-independent-m$M.json
done

echo "== Prop 8.1: certified brackets m=10,20,30,40,60,80 (producer, then independent checker)"
if run "$OUT/brackets.log" "$PY" $F/code/cert_native.py --m 10 20 30 40 60 80 --scratch "$OUT/cert-native" --output-dir "$OUT/brackets"; then
  for M in 10 20 30 40 60 80; do
    cmpr "$OUT/brackets/cert-m$M.json" $F/evidence/cert-m$M.json
    run "$OUT/independent-cert-m$M.log" "$PY" $F/code/independent_cert.py --producer-receipt "$OUT/brackets/cert-m$M.json" --scratch "$OUT/independent-cert" --output "$OUT/brackets/independent-cert-m$M.json" \
      && cmpr "$OUT/brackets/independent-cert-m$M.json" $F/evidence/independent-cert-m$M.json
  done
fi

echo "== Props 6.8, 6.9: rectangle enclosure of ||B||"
# The program hashes ideas/P1-numeric-protocol.md and theory/P1-rectangle-certificate.md. The
# committed receipts hashed the versions at commit c1e6e59d (archived in data/protocol-history/);
# both files were later extended. Check those identities, then compare everything else.
for KEY in protocol_sha256:ideas-P1-numeric-protocol-c1e6e59d.md reduction_sha256:theory-P1-rectangle-certificate-c1e6e59d.md; do
  REF=$("$PY" -c "import json,sys;print(json.load(open(sys.argv[1]))[sys.argv[2]])" $S/evidence/P1-rectangle-N16.json "${KEY%%:*}")
  if [ "$(sha256sum < "$HERE/data/protocol-history/${KEY#*:}" | cut -d' ' -f1)" = "$REF" ]; then
    echo "AGREE  ${KEY#*:} matches ${KEY%%:*} of the receipt"
  else
    echo "DIFFER ${KEY#*:}"; fail=1
  fi
done
run "$OUT/P1-N16.log" "$PY" $S/code/P1_rectangle.py --N 16 --theta 256 --output "$OUT/P1-rectangle-N16.json" \
  && cmpr "$OUT/P1-rectangle-N16.json" $S/evidence/P1-rectangle-N16.json --ignore '^(protocol|reduction)_sha256$'
run "$OUT/P1-N8.log" "$PY" $S/code/P1_rectangle.py --N 8 --theta 64 --output "$OUT/P1-rectangle-N8.json" \
  && cmpr "$OUT/P1-rectangle-N8.json" $S/evidence/P1-rectangle-N8.json --ignore '^(protocol|reduction)_sha256$'

echo "== Section 8.3 (MEASURED): item (1) via the float64 reproduction suites (items (2)-(4): see README)"
for SUITE in padua marginal; do
  run "$OUT/reproduction-$SUITE.log" "$PY" tracks/mz-constants/code/reproduce.py --suite $SUITE --max-N 1280 --output "$OUT/reproduction-$SUITE.json" \
    && cmpr "$OUT/reproduction-$SUITE.json" "$HERE/data/measurements/reproduction-$SUITE.json"
done

regen=0; regen_fail=0; vec_notes=0
if [ "$REGEN" = "--regenerate" ]; then
  regen=1
  echo "== OPTIONAL: regenerate the Prop 8.2 witnesses from scratch (eigensolver, then exact rounding)"
  mkdir -p "$OUT/regen"
  if (cd $C/code && "$PY" g1_minimum.py --m 1101 1240 1600 --output "$OUT/regen/scan.json" --vector-dir "$OUT/regen/vectors") > "$OUT/regen/scan.log" 2>&1; then
    for M in 1101 1240 1600; do
      V="$OUT/regen/vectors/m$M-n$((M-1))-min.npy"
      if cmp -s "$V" "$HERE/data/source-vectors/m$M-n$((M-1))-min.npy"; then
        echo "AGREE  regenerated source vector m=$M"
      else
        echo "NOTE   regenerated source vector m=$M differs from the archived one (floating point, platform-dependent; not a premise of any certificate)"
        vec_notes=$((vec_notes+1))
      fi
      if "$PY" $C/code/rigorous_witness.py --m $M --vector "$V" --scratch "$OUT/regen/cert-m$M" --output "$OUT/regen/producer-m$M.json" > "$OUT/regen/producer-m$M.log" 2>&1; then
        SIGN=$("$PY" -c "import json,sys;print(json.load(open(sys.argv[1])).get('sign'))" "$OUT/regen/producer-m$M.json")
        echo "       regenerated witness m=$M: exact producer reports sign $SIGN"
        if [ "$(payload "$OUT/regen/cert-m$M/witness.json.gz")" = "$(payload "$HERE/data/witnesses/cert-m$M/witness.json.gz")" ] \
           && cmp -s "$OUT/regen/cert-m$M/exact-norm.txt" "$HERE/data/witnesses/cert-m$M/exact-norm.txt"; then
          echo "AGREE  regenerated witness payload and exact norm m=$M equal the archived ones"
        else
          echo "DIFFER regenerated witness payload or exact norm m=$M differs from the archived one"
          regen_fail=1
        fi
      else
        echo "FAILED (log $OUT/regen/producer-m$M.log): exact producer on the regenerated vector m=$M"
        regen_fail=1
      fi
    done
  else
    echo "FAILED (log $OUT/regen/scan.log): eigensolver for the regeneration"
    regen_fail=1
  fi
fi

echo "== Summary"
if [ "$fail" = 0 ]; then
  echo "ALL REQUIRED CHECKS AGREE"
else
  echo "REQUIRED CHECKS FAILED (see DIFFER/FAILED lines above)"
fi
if [ "$regen" = 1 ]; then
  if [ "$regen_fail" = 0 ]; then
    echo "OPTIONAL REGENERATION REPRODUCED THE ARCHIVED WITNESSES ($vec_notes source-vector difference(s) noted)"
  else
    echo "OPTIONAL REGENERATION DID NOT REPRODUCE THE ARCHIVED WITNESSES (see above; the archived certificates are unaffected)"
  fi
fi
[ "$fail" = 0 ] || exit 1
[ "$regen_fail" = 0 ] || exit 2
exit 0
