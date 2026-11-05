"""Bounded subprocess staging and receipts for the unchanged natural suite."""
import argparse, hashlib, json, os, pathlib, platform, subprocess, sys, time
ROOT=pathlib.Path(__file__).resolve().parents[3]
TOP=pathlib.Path(__file__).resolve().parents[1]
RAW=pathlib.Path('/tmp/padua-lanczos-frontier-l7-suite')
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def manifest(directory):
 return [{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(directory.glob('*')) if p.is_file()]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--stage',choices=['pilot','remaining'],required=True);a=ap.parse_args()
 pairs=[('disk',2026110501)] if a.stage=='pilot' else [(d,s) for d in ['disk','lshape','triangle','sector'] for s in [2026110501,2026110502] if (d,s)!=('disk',2026110501)]
 stage=RAW/a.stage;stage.mkdir(parents=True,exist_ok=True)
 if (stage/'stage.json').exists():raise RuntimeError('refuse overwrite stage receipt')
 env=os.environ.copy();env.update(PYTHONPATH='/tmp/padua-lanczos-frontier-g0/deps',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
 meta={'input_head':'9825d184517db81d0aad8542fbd6639f2164b803','stage':a.stage,'python':platform.python_version(),'source_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [pathlib.Path(__file__),TOP/'code/l7_natural.py',TOP/'l7-preregistration.md',TOP/'l7-suite-methods.md',ROOT/'tracks/bivariate-lanczos/code/L2/l2_core.py',ROOT/'tracks/bivariate-lanczos/code/drift/e6_benchmark.py']},'environment':{k:env[k] for k in ['PYTHONPATH','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS']},'cases':[],'timeout_per_case_seconds':600}
 (stage/'pre-run.json').write_text(json.dumps(meta,indent=1)+'\n')
 for d,s in pairs:
  out=stage/f'{d}-{s}';out.mkdir()
  cmd=[sys.executable,str(TOP/'code/l7_natural.py'),'--external','/tmp/padua-lanczos-frontier-g0/polyrat','--output-dir',str(out),'--domains',d,'--seeds',str(s)]
  row={'domain':d,'seed':s,'command':cmd};t=time.time()
  with (out/'stdout.log').open('w') as stdout,(out/'stderr.log').open('w') as stderr:
   try:row['exit_code']=subprocess.run(cmd,cwd=ROOT,env=env,stdout=stdout,stderr=stderr,timeout=600).returncode
   except subprocess.TimeoutExpired:row['timeout']=True
  row['elapsed_seconds']=time.time()-t;row['artifacts']=manifest(out);meta['cases'].append(row)
  (stage/'stage.json').write_text(json.dumps(meta,indent=1)+'\n')
  print(json.dumps({k:v for k,v in row.items() if k!='artifacts'}),flush=True)
  if row.get('exit_code')!=0:break
 receipt=TOP/'evidence'/f'l7-suite-{a.stage}.json';receipt.write_text(json.dumps(meta,indent=1)+'\n')
if __name__=='__main__':main()
