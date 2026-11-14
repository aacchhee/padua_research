#!/usr/bin/env python3
"""Prospective bounded public-adapter smoke; execute only after source checkpoint."""
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[4]
OUTPUT=ROOT/'local-output/argmax-bridge-20261105/zenodo-public-20261114'
PACKAGE=OUTPUT/'padua-reproducibility'

def main():
    if sys.argv[1:] != ['--execute']: raise SystemExit('requires --execute after source checkpoint')
    out=OUTPUT/'developer-smoke'; out.mkdir(exist_ok=False)
    command=[sys.executable,'-E','-B',str(PACKAGE/'verify.py'),'--degrees','41,511','--polynomial-degrees','2,17','--analytic']
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(300,300))
        resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
        resource.setrlimit(resource.RLIMIT_CORE,(0,0))
        os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    def interrupted(number, frame):
        raise RuntimeError('observer signal '+str(number))
    for number in (signal.SIGTERM,signal.SIGHUP,signal.SIGINT): signal.signal(number,interrupted)
    started=time.monotonic(); status=None; cleanup=False
    with (out/'stdout.txt').open('x') as stdout,(out/'stderr.txt').open('x') as stderr:
        child=subprocess.Popen(command,cwd=PACKAGE,stdout=stdout,stderr=stderr,start_new_session=True,preexec_fn=limits,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'})
        try:
            while True:
                pid,status,usage=os.wait4(child.pid,os.WNOHANG)
                if pid: break
                status=None
                if time.monotonic()-started>600: raise TimeoutError('wall cap')
                time.sleep(.1)
        finally:
            if status is None:
                for number in (signal.SIGTERM,signal.SIGHUP,signal.SIGINT): signal.signal(number,signal.SIG_IGN)
                cleanup=True
                try: os.killpg(child.pid,signal.SIGKILL)
                except ProcessLookupError: pass
                _,status,usage=os.wait4(child.pid,0)
            child.returncode=os.waitstatus_to_exitcode(status)
            receipt=dict(command=command,verify_sha256=hashlib.sha256((PACKAGE/'verify.py').read_bytes()).hexdigest(),CPU_limit_per_process=300,wall_limit_seconds=600,returncode=child.returncode,wait_status=status,CPU_seconds=usage.ru_utime+usage.ru_stime,wall_seconds=time.monotonic()-started,maximum_RSS_KiB=usage.ru_maxrss,cleanup=cleanup,scope='phase 41 and 511 both records; polynomial fresh build, 2 and 17; analytic gates and tables; no full rerun')
            (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
            print(json.dumps(receipt))
    if cleanup or child.returncode: raise SystemExit(1)
if __name__=='__main__': main()
