#!/usr/bin/env python3
"""C12 one-shot bounded worker/build CPU supervisor."""
import json,os,pathlib,resource,signal,subprocess,sys,time
import build

def childcpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime

def groupcpu(pgid):
 ticks=0
 for p in pathlib.Path('/proc').iterdir():
  if not p.name.isdecimal():continue
  try:
   f=(p/'stat').read_text().rsplit(')',1)[1].split()
   if int(f[2])==pgid:ticks+=sum(int(f[i]) for i in (11,12,13,14))
  except (FileNotFoundError,ProcessLookupError):pass
 return ticks/os.sysconf('SC_CLK_TCK')

def main():
 build.OUT.mkdir(parents=True,exist_ok=True);target=build.OUT/'supervisor-v2.json';stdout=build.OUT/'stdout-v2.txt';stderr=build.OUT/'stderr-v2.txt'
 if target.exists() or stdout.exists() or stderr.exists():raise RuntimeError('refuse C12 supervisor overwrite')
 before=childcpu();own=time.process_time();wall=time.monotonic();stopped=False;peak=0.
 command=[sys.executable,str(build.HERE/'control_v2.py')]
 with stdout.open('x') as out,stderr.open('x') as err:
  process=subprocess.Popen(command,stdout=out,stderr=err,start_new_session=True)
  try:
   while process.poll() is None:
    cpu=groupcpu(process.pid)+time.process_time()-own;peak=max(peak,cpu)
    if cpu>=55 or time.monotonic()-wall>=90:os.killpg(process.pid,signal.SIGKILL);stopped=True;break
    time.sleep(.1)
   code=process.wait()
  except BaseException:
   try:os.killpg(process.pid,signal.SIGKILL)
   except ProcessLookupError:pass
   process.wait();raise
 report=dict(exit_status=code,watchdog_stopped=stopped,total_worker_build_cpu=childcpu()-before,supervisor_own_cpu=time.process_time()-own,wall=time.monotonic()-wall,peak_group_cpu=peak,command=command,supervisor_source=build.pinned.identity(pathlib.Path(__file__)),stdout=build.pinned.identity(stdout),stderr=build.pinned.identity(stderr),worker_receipt=build.pinned.identity(build.OUT/'controls-v2.json') if (build.OUT/'controls-v2.json').exists() else None)
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report));return code or int(stopped)
if __name__=='__main__':raise SystemExit(main())
