#!/bin/bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
cd /home/user/padua_research
run(){ name=$1; shift; s=$(date +%s.%N); "$@" > /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/$name.stdout 2> /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/$name.stderr; rc=$?; e=$(date +%s.%N); echo "$name rc=$rc wall=$(echo "$e - $s" | bc) cmd=$*" >> /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/runlog.txt; }
: > /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/runlog.txt
run manifest python topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks
run k0cc python topics/padua-mz-sharp-constants-20261106/code/S4_k0_replay.py --suite cc --output /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/k0-cc.json
run k0carrier python topics/padua-mz-sharp-constants-20261106/code/S4_k0_replay.py --suite carrier --output /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/k0-carrier.json
run k1 python topics/padua-mz-sharp-constants-20261106/code/S4_k1_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/k1.json
run k3 python topics/padua-mz-sharp-constants-20261106/code/S4_k3_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/k3.json
run s2 python topics/padua-mz-sharp-constants-20261106/code/S2_model.py --output /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/upper-model.json
run s3 python topics/padua-mz-sharp-constants-20261106/code/S3_corner_model.py --orders 128 192 --cuts 16 32 64 128 --output /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/corner-model.json
run padua python topics/padua-mz-sharp-constants-20261106/code/S4_padua_fit.py --essential topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-essential.json --output /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/padua-fits.json
echo DONE >> /tmp/claude-0/-home-user-padua-research/8d35f915-ba92-5bfd-81d7-431865a9781c/scratchpad/audit/num/runlog.txt
