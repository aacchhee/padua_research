#!/usr/bin/env python3
"""Fresh supplementary execution of the inspected basis-certificate/FLINT path."""
import argparse,hashlib,json,os,platform,subprocess,sys,time
from pathlib import Path
TOP=Path(__file__).resolve().parents[1]
WORK=Path('/tmp/padua-lanczos-nonproduct-20261105/scan-review')
def identity(p):
 b=Path(p).read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--family',choices=('D36x9','D65x9'),required=True);ap.add_argument('--degree',type=int,required=True);ap.add_argument('--rules',nargs='+',default=['alt','pivot']);ap.add_argument('--seconds',type=int,default=120);args=ap.parse_args()
 wd=WORK/f'flint-{args.family}-d{args.degree}';wd.mkdir(exist_ok=False)
 inputdir=Path('/tmp/padua-lanczos-nonproduct-20261105/p6')/('benchmark8-D36x9' if args.family=='D36x9' else 'pilot8-D65x9')
 source=TOP/'code/p6_basis_export.cpp';exe=wd/'exporter';compilecmd=['g++','-O3','-std=c++17',str(source),'-lgmpxx','-lgmp','-o',str(exe)]
 subprocess.run(compilecmd,check=True)
 checks=[]
 for rule in args.rules:
  stem=f'{args.family}-{rule}-d{args.degree}';basis=wd/(stem+'.basis.json');out=wd/(stem+'.jsonl');receipt=TOP/'evidence'/('check-scans-flint-'+stem+'.json')
  cmd=[str(exe),str(inputdir/'input.txt'),str(args.degree),rule,args.family];start=time.monotonic()
  with basis.open('w') as f,(wd/(stem+'.export.log')).open('w') as err:subprocess.run(cmd,stdout=f,stderr=err,check=True,timeout=args.seconds)
  exporttime=time.monotonic()-start
  flintcmd=[sys.executable,'-B',str(TOP/'code/flint_disk_check.py'),'--input',str(inputdir/'input.txt'),'--basis',str(basis),'--output',str(out),'--receipt',str(receipt),'--export-source',str(source),'--export-binary',str(exe)]
  if args.degree==8:
   for backend in ('producer','checker'):flintcmd+=['--reference',str(inputdir/(backend+'-'+rule+'.jsonl'))]
  env=os.environ.copy();env['PYTHONPATH']='/tmp/padua-lanczos-nonproduct-20261105/deps'
  with (wd/(stem+'.check.log')).open('w') as err: subprocess.run(flintcmd,stderr=err,check=True,timeout=args.seconds,env=env)
  checks.append(dict(export_command=cmd,export_seconds=exporttime,flint_command=flintcmd,receipt=identity(receipt)))
 report=dict(status='PASS fresh supplementary FLINT replay',command=[sys.executable,'-B',*sys.argv],code=identity(__file__),compile_command=compilecmd,exporter=identity(exe),input=identity(inputdir/'input.txt'),checks=checks,python=platform.python_version())
 (TOP/'evidence'/f'check-scans-flint-replay-{args.family}-d{args.degree}.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
