#!/bin/bash
R=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/assembly-run
cd /home/user/padua_research
python3 - <<'PY' > $R/n37-wrapper.json 2> $R/n37-wrapper.err
import resource, subprocess, time, json
R='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/assembly-run'
cmd=['python3','topics/padua-argmax-effective-20261103/code/native_checker/check.py','topics/padua-argmax-bridge-20261105/evidence/n37.json.gz','--binary',R+'/kernel','--output',R+'/replay-n37.json']
r0=resource.getrusage(resource.RUSAGE_CHILDREN); t0=time.monotonic()
p=subprocess.run(cmd,capture_output=True,text=True)
r1=resource.getrusage(resource.RUSAGE_CHILDREN); t1=time.monotonic()
print(json.dumps(dict(cmd=cmd,exit=p.returncode,stdout=p.stdout,stderr=p.stderr,cpu_user=r1.ru_utime-r0.ru_utime,cpu_sys=r1.ru_stime-r0.ru_stime,wall=t1-t0),indent=1))
PY
echo "wrapper exit $?" >> $R/n37-wrapper.err
