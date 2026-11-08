#!/bin/bash
cd /tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/g-assembly-code
{ time timeout 1200 env PYTHONPATH=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/pylib python3 bern_indep.py 32 --cert /home/user/padua_research/topics/padua-argmax-effective-20261103/evidence/n32.json.gz > run_replay_n32.json ; } 2> run_replay_n32.time; echo "tag=replay_n32 exit=$?"
