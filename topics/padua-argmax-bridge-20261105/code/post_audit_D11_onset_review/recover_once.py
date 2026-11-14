"""One root-reviewed hash-only D11 recovery; preregistered in RECOVERY.md."""
import time
start_cpu=time.process_time()
import hashlib
import json
import resource
import subprocess
import sys
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(3,10))
p=Path(__file__).resolve()
base=p.parents[2]
out=base/'evidence/post_audit_D11_onset_review'
receipt=out/'recovery-receipt.json'
stdout=out/'recovery-stdout.txt'; stderr=out/'recovery-stderr.txt'
assert not any(x.exists() for x in (receipt,stdout,stderr,out/'scalars.json'))
source=p.with_name('check.py')
assert hashlib.sha256(source.read_bytes()).hexdigest()=='4816e2ee9109baad796aceb59580c120a5dae8c48a41eb4daf87054750a742d7'
r0=resource.getrusage(resource.RUSAGE_CHILDREN)
wall=time.monotonic()
with stdout.open('x') as so, stderr.open('x') as se:
 try:
  proc=subprocess.run([sys.executable,str(source)],stdout=so,stderr=se,timeout=2,check=False)
  code=proc.returncode
 except subprocess.TimeoutExpired:
  code='TIMEOUT'
elapsed=time.monotonic()-wall
r1=resource.getrusage(resource.RUSAGE_CHILDREN)
record={'returncode':code,'timeout_seconds':2,'recovery_wall_seconds':elapsed,'recovery_child_cpu_seconds':r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime,'wrapper_cpu_seconds':time.process_time()-start_cpu,'first_process_cpu_seconds':None,'first_observed_enclosing_tool_wall_seconds':0.3,'first_conservative_cpu_charge_seconds':1,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'wrapper_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'stdout_sha256':hashlib.sha256(stdout.read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256(stderr.read_bytes()).hexdigest()}
receipt.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
print(json.dumps(record,sort_keys=True))
assert code==0
