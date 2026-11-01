set -x
cd "$(git rev-parse --show-toplevel)"
PY=${PY:-python3}
O=/tmp/lattice-claude
rm -rf $O; mkdir -p $O/c0
T=topics/lattice-unisolvence-20261031/directions
C=tracks/lattice-unisolvence/code
t(){ s=$(date +%s); "$@"; echo "EXIT $? $(( $(date +%s)-s ))s :: $*"; }
t $PY $C/c0_catalogue.py --output-dir $O/c0
t $PY $C/c3_rank.py $T/C0/catalogue.json --output $O/ranks.json
t $PY $C/c3_structure.py $T/C3/ranks.json --output $O/structure.json
t $PY $C/c3_obstructions.py $T/C3/ranks.json $T/C3/structure.json --output $O/obstructions.json
t $PY $C/c3_lowdegree.py $T/C3/ranks.json $T/C3/obstructions.json --output $O/lowdegree.json
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
t $PY $C/c3_lebesgue.py $T/C3/ranks.json $T/C0/catalogue.json --output $O/lebesgue.json
t $PY $C/c1_mod4.py --output $O/mod4.json
t $PY $C/c1_stability.py --output $O/stability.json
t $PY $C/c1_symbolic.py --output $O/symbolic.json
export OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2
t $PY $C/c1_gram.py --output $O/gram.json
t $PY $C/c1_extension.py --output $O/extension.json
t $PY $C/verify_artifacts.py topics/lattice-unisolvence-20261031/audit-targets.json
git diff --check; echo "DIFFCHECK $?"
echo ALLDONE
