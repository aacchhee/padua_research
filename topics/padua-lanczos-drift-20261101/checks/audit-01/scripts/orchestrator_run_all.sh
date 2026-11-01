set -x
cd /home/claude/padua_research
export PYTHONPATH=/workspace/padua-drift-runs/python-deps
export OPENBLAS_NUM_THREADS=1
D=tracks/bivariate-lanczos/code/drift
( /usr/bin/time -v python3 $D/e1_check.py --evidence topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-e1-check.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/e1_check.log 2>&1
( python3 $D/e1_exact.py --set triangle --degree 12 --rule bj --sources all --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-T24-bj.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/T24-bj.log 2>&1
( python3 $D/e1_exact.py --set triangle --degree 12 --rule pivot --sources all --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-T24-pivot.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/T24-pivot.log 2>&1
( python3 $D/e1_exact.py --set rotated --degree 12 --rule bj --sources all --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-rotQ24-bj.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/rot-bj.log 2>&1
( python3 $D/e1_exact.py --set rotated --degree 12 --rule alt --sources all --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-rotQ24-alt.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/rot-alt.log 2>&1
wait
( python3 $D/e1_verify.py --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-e1-derivative-check.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/e1_verify.log 2>&1
( python3 $D/e1_reproduce.py --set rotated --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-scalar-rotated.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/repro-rot.log 2>&1
( python3 $D/e1_reproduce.py --set triangle --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-scalar-triangle.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/repro-tri.log 2>&1
( python3 -B $D/e5_exact_checks.py > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-e5.json ) 2> /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/e5.log
wait
( python3 $D/e6_benchmark.py --external /workspace/padua-drift-external/polyrat --sets rotpi4 triangle --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-e6.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/e6.log 2>&1
( python3 $D/e6_benchmark.py --external /workspace/padua-drift-external/polyrat --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-e6-full.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/e6full.log 2>&1
( python3 $D/e6_benchmark.py --external /workspace/padua-drift-external/polyrat --sets T24 Q24 --grid-degree 12 --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-e6-grids12.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/e6g12.log 2>&1
( python3 $D/e6_smooth.py --external /workspace/padua-drift-external/polyrat --output /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/audit-e6-smooth.json ) > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/e6smooth.log 2>&1
echo ALLDONE > /tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs/DONE
