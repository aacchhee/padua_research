#!/usr/bin/env python3
"""Capture complete worker+build CPU including receipt serialization."""
import json, pathlib, resource, subprocess, sys, time
import build

def main():
 build.OUT.mkdir(parents=True,exist_ok=True);target=build.OUT/'supervisor.json';stdout=build.OUT/'controls.stdout'
 if target.exists() or stdout.exists():raise RuntimeError('refuse supervisor overwrite')
 before=resource.getrusage(resource.RUSAGE_CHILDREN);own=time.process_time();wall=time.monotonic()
 command=[sys.executable,str(build.HERE/'controls.py')]
 with stdout.open('w') as f:result=subprocess.run(command,cwd=build.ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=90)
 after=resource.getrusage(resource.RUSAGE_CHILDREN)
 report=dict(command=command,exit_status=result.returncode,total_worker_and_build_cpu=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime),supervisor_own_cpu=time.process_time()-own,wall=time.monotonic()-wall,stdout=build.identity(stdout),worker_receipt=build.identity(build.OUT/'controls.json'),supervisor_source=build.identity(pathlib.Path(__file__)))
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report));return result.returncode
if __name__=='__main__':raise SystemExit(main())
