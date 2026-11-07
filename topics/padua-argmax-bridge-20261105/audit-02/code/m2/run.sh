#!/bin/bash
# usage: run.sh script.py ; runs with -I, pylib on path, records CPU via bash times
A=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit2
S=$1
cd $A
python3 -I -c "import sys; sys.path.insert(0,'$A/pylib'); sys.argv=['$S']; exec(compile(open('$S').read(),'$S','exec'))" > ${S%.py}.out 2> ${S%.py}.err
rc=$?
echo "exit=$rc" >> ${S%.py}.out
times >> ${S%.py}.out
