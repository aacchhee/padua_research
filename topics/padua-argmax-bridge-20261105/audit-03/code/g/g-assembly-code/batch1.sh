#!/bin/bash
cd /tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/g-assembly-code
run() { tag=$1; shift; { time PYTHONPATH=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/pylib python3 bern_indep.py "$@" > run_$tag.json ; } 2> run_$tag.time; echo "tag=$tag exit=$?"; }
run replay_n16 16 --cert /home/user/padua_research/topics/padua-argmax-bridge-20261105/code/small_degree_unification/certificates/n16.json.gz
run replay_n17 17 --cert /home/user/padua_research/topics/padua-argmax-effective-20261103/evidence/n17.json.gz
run own_n17 17
run own_n24 24
