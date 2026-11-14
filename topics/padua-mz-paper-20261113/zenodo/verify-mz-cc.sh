#!/usr/bin/env bash
# Re-run the computer-assisted and measured parts of MZ-CC from this archive and
# compare them with the committed receipts. Usage: bash verify.sh [OUTDIR]
# Needs Python 3.12 with requirements.txt installed (set PY to the interpreter).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$(mkdir -p "${1:-$HERE/verify-out}" && cd "${1:-$HERE/verify-out}" && pwd)"
PY="${PY:-python3}"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
CMP="$PY $HERE/tools/compare_receipts.py"
cd "$HERE/repository"
T=topics/padua-mz-sharp-constants-20261106
fail=0

echo "== Appendix C / Prop 5.3: certified Rayleigh quotient of the J=512 trial vector"
$PY $T/code/P4_rayleigh.py --trial $T/evidence/P4-trial-J512.json --output "$OUT/P4-rayleigh.json"
$CMP "$OUT/P4-rayleigh.json" $T/evidence/P4-rayleigh.json || fail=1
echo "== Appendix C: independent exact-rational grouped check"
$PY $T/code/P4_check_grouped.py --trial $T/evidence/P4-trial-J512.json --producer "$OUT/P4-rayleigh.json" --output "$OUT/P4-grouped-check.json"
$CMP "$OUT/P4-grouped-check.json" $T/evidence/P4-grouped-check.json || fail=1

echo "== Table 1 (MEASURED): float64 reproduction suite"
$PY tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output "$OUT/reproduction.json"
$CMP "$OUT/reproduction.json" "$HERE/data/table1/reproduction.json" || fail=1

if [ "$fail" = 0 ]; then echo "ALL CHECKS AGREE"; else echo "SOME CHECKS DIFFER (see above)"; exit 1; fi
