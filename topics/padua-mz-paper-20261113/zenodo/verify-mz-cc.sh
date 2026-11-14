#!/usr/bin/env bash
# Re-run the computer-assisted and measured parts of MZ-CC from this archive and
# compare them with the committed receipts.
#   Usage: [PY=interpreter] bash verify.sh [OUTDIR]
# PY may be a command on PATH (default python3) or a path such as venv/bin/python;
# a relative path is taken relative to the directory you run the command from.
# Needs Python 3.12 with requirements.txt installed.
# Exit status: 0 if every check agrees, 1 otherwise. The last line says which.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTARG="${1:-$HERE/verify-out}"
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
T=topics/padua-mz-sharp-constants-20261106
fail=0
# run LOG CMD...: run a program with its output in LOG; a nonzero exit is a failed check.
run() { local log="$1"; shift; "$@" > "$log" 2>&1 || { echo "FAILED (exit $?; log $log): $*"; fail=1; return 1; }; }
# cmpr FRESH REFERENCE [--ignore REGEX ...]: field-by-field receipt comparison.
cmpr() { "$PY" "$HERE/tools/compare_receipts.py" "$@" || fail=1; }

echo "== Appendix C / Prop 5.3: certified Rayleigh quotient of the J=512 trial vector"
if run "$OUT/P4-rayleigh.log" "$PY" $T/code/P4_rayleigh.py --trial $T/evidence/P4-trial-J512.json --output "$OUT/P4-rayleigh.json"; then
  # The producer hashes the protocol file attempts/P4.md. The committed receipt hashed the
  # preregistered version (commit d03e74dc, archived in data/protocol-history/); the file
  # was later extended with results. Check that identity, then compare everything else.
  REFP=$("$PY" -c "import json,sys;print(json.load(open(sys.argv[1]))['protocol_sha256'])" $T/evidence/P4-rayleigh.json)
  if [ "$(sha256sum < "$HERE/data/protocol-history/attempts-P4-d03e74dc.md" | cut -d' ' -f1)" = "$REFP" ]; then
    echo "AGREE  preregistered protocol attempts/P4.md (d03e74dc) matches the receipt"
  else
    echo "DIFFER preregistered protocol hash"; fail=1
  fi
  cmpr "$OUT/P4-rayleigh.json" $T/evidence/P4-rayleigh.json --ignore '^protocol_sha256$'
  echo "== Appendix C: independent exact-rational grouped check"
  run "$OUT/P4-grouped-check.log" "$PY" $T/code/P4_check_grouped.py --trial $T/evidence/P4-trial-J512.json --producer "$OUT/P4-rayleigh.json" --output "$OUT/P4-grouped-check.json" \
    && cmpr "$OUT/P4-grouped-check.json" $T/evidence/P4-grouped-check.json
fi

echo "== Table 1 (MEASURED): float64 reproduction suite"
run "$OUT/reproduction.log" "$PY" tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output "$OUT/reproduction.json" \
  && cmpr "$OUT/reproduction.json" "$HERE/data/table1/reproduction.json"

echo "== Summary"
if [ "$fail" = 0 ]; then echo "ALL REQUIRED CHECKS AGREE"; exit 0; fi
echo "REQUIRED CHECKS FAILED (see DIFFER/FAILED lines above)"; exit 1
