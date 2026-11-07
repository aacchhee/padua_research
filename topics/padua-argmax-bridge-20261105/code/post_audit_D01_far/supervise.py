#!/usr/bin/env python3
"""Single attempt; all descendants inherit task process group and CPU meter.
No retries or model changes. Run only once prospective gates are frozen.
"""
import hashlib,json,os,pathlib,resource,signal,subprocess,sys,time
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D01/far'
def cpu():
 return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime
            for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
RAW.mkdir(parents=True,exist_ok=True)
receipt=RAW/'supervisor.json'
if receipt.exists():raise FileExistsError('First attempt is immutable: '+str(receipt))
start=cpu();wall=time.monotonic();p=subprocess.Popen([sys.executable,str(HERE/'run.py')],start_new_session=True,stdout=open(RAW/'stdout.log','x'),stderr=open(RAW/'stderr.log','x'))
# Sum /proc task CPU over the whole group, plus reaped children in driver.
peak=0.; killed=False
while p.poll() is None:
 total=cpu()-start
 for path in pathlib.Path('/proc').glob('[0-9]*/stat'):
  try:
   data=path.read_text();fields=data[data.rfind(')')+2:].split()
   if int(fields[2])==p.pid:
    total+=(int(fields[11])+int(fields[12])+int(fields[13])+int(fields[14]))/os.sysconf('SC_CLK_TCK')
  except (OSError,ValueError,IndexError):pass
 peak=max(peak,total)
 if total>=590:
  os.killpg(p.pid,signal.SIGKILL);killed=True;break
 time.sleep(.1)
rc=p.wait();total=cpu()-start
record=dict(command=[sys.executable,str(HERE/'run.py')],returncode=rc,killed=killed,
 total_cpu_seconds=total,peak_group_cpu_seconds=peak,wall_seconds=time.monotonic()-wall,
 cap_cpu_seconds=600,result='CAP' if killed or total>600 else ('PASS' if rc==0 else 'FIRST_FAILURE'),
 supervisor_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
receipt.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
sys.exit(0 if rc==0 and not killed and total<600 else 1)
