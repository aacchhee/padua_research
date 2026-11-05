set -u
S=/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad
R=$S/L7G1/repo
P=$R/topics/padua-lanczos-frontier-20261105/code/g1_exact_prefix.py
O=$S/L7G1/g1/out
mkdir -p $O
rule=$1
start=$(date +%s.%N)
PYTHONPATH=$S/deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.13 -B $P --set triangle --rule $rule --max-degree 12 --old-sweep $S/L7G1/g1/inputs/e1-full-sweep.json --output-dir $O/ov-$rule --receipt $O/ov-$rule.json > $O/ov-$rule.log 2>&1; echo "ov $rule exit $?"
PYTHONPATH=$S/deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.13 -B $P --set triangle --rule $rule --max-degree 20 --old-sweep $S/L7G1/g1/inputs/e1-full-sweep.json --overlap-receipt $O/ov-$rule.json --output-dir $O/full-$rule --receipt $O/full-$rule.json > $O/full-$rule.log 2>&1; echo "full $rule exit $?"
end=$(date +%s.%N); echo "$rule elapsed $(echo "$end - $start" | bc)"
