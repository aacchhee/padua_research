"""Bounded unchanged E6 G4 replay. No network or Git mutations."""
import argparse, hashlib, io, json, os, pathlib, platform, subprocess, sys, time
ROOT=pathlib.Path(__file__).resolve().parents[3]
TOP=ROOT/'topics/padua-lanczos-frontier-20261105'
DRIFT=ROOT/'tracks/bivariate-lanczos/code/drift'
PINS={
'arnoldi.py':'e51f356170dc5e1403f1065daf5bc331e7ce470cac1b9161f5ecb9efccf68d86',
'index.py':'84df400c73a2aacf922ff38c0a591b525c2ac1f9b7a9f958f4111d4ceb88d10d',
'basis.py':'9ce50feba7cfaa706db3bb94bbe2b34f065d9dbde28a18a3eee021d11e8ec478',
'version.py':'1d13b63cb7af46b37f80ac0d695be5f795c2db5ce6e66dea34143da4cb434439'}
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def diffs(a,b,p=''):
 if isinstance(a,dict):
  assert a.keys()==b.keys(),p
  return sum((diffs(a[k],b[k],p+'/'+k) for k in a),[])
 if isinstance(a,list):
  assert len(a)==len(b),p
  return sum((diffs(x,y,p+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))),[])
 if a==b:return []
 r={'path':p,'old':a,'new':b}
 if isinstance(a,(float,int)) and not isinstance(a,bool):r.update(abs_difference=abs(a-b),relative_difference=abs(a-b)/abs(a) if a else None)
 return [r]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--external',type=pathlib.Path,required=True);ap.add_argument('--deps',required=True);ap.add_argument('--output-dir',type=pathlib.Path,required=True);a=ap.parse_args();out=a.output_dir.resolve();assert ROOT not in out.parents;out.mkdir(parents=True,exist_ok=False)
 raw=subprocess.check_output(['git','show','2b52b432fe59c9a50aef9deebe5152c5d6874465:topics/padua-lanczos-drift-20261101/evidence/e6-benchmarks.json'],cwd=ROOT)
 assert len(raw)==239594 and hashlib.sha256(raw).hexdigest()=='e7a3f940c4bd79bbf84fbe4eeafca4186c9b969c92665fb972367becc23a3c58';(out/'historical.json').write_bytes(raw);old=json.loads(raw)
 upstream={k:sha(a.external/'polyrat'/k) for k in PINS};assert upstream==PINS
 prov=json.loads((ROOT/'topics/padua-lanczos-drift-20261101/evidence/e6-provenance.json').read_text());sources={}
 for item in prov['files']:
  if item['path'].endswith('.py'):
   assert sha(ROOT/item['path'])==item['sha256'];sources[item['path']]=item['sha256']
 env=dict(os.environ,PYTHONPATH=a.deps,OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1');env.pop('OPENBLAS_CORETYPE',None)
 probe="import numpy as np,scipy,json,platform,contextlib,io; s=io.StringIO();\nwith contextlib.redirect_stdout(s): np.show_config()\nprint(json.dumps({'python':platform.python_version(),'platform':platform.platform(),'numpy':np.__version__,'scipy':scipy.__version__,'blas':s.getvalue()}))"
 runtime=json.loads(subprocess.check_output([sys.executable,'-B','-c',probe],env=env));assert runtime['numpy']=='2.3.5' and runtime['scipy']=='1.17.0'
 write(out/'environment.json',runtime)
 result={'rules_head':'bb67c1ee830d468fa33007e15008d5574d00ccf4','status':'REPLAY_REQUIRES_REVIEW','code_sha256':sha(__file__),'source_sha256':sources,'upstream_sha256':upstream,'runtime':{k:v for k,v in runtime.items() if k!='blas'},'cases':[]}
 for name in ['rotpi4','triangle']:
  cmd=[sys.executable,'-B',str(DRIFT/'e6_benchmark.py'),'--external',str(a.external),'--sets',name,'--output',str(out/(name+'.json'))];start=time.time()
  with (out/(name+'.stdout')).open('w') as stdout,(out/(name+'.stderr')).open('w') as stderr:
   try:r=subprocess.run(cmd,cwd=ROOT,env=env,stdout=stdout,stderr=stderr,timeout=1800);exitcode=r.returncode
   except subprocess.TimeoutExpired:exitcode='TIMEOUT1800'
  receipt={'name':name,'command':cmd,'environment':{'PYTHONPATH':a.deps,'OPENBLAS_NUM_THREADS':'1','OPENBLAS_CORETYPE':None},'start_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(start)),'elapsed_seconds':time.time()-start,'exit_code':exitcode}
  assert exitcode==0,receipt
  path=out/(name+'.json');new=json.loads(path.read_text());oc=next(c for c in old['cases'] if c['name']==name);nc=new['cases'][0]
  delta=diffs(oc,nc);write(out/(name+'-differences.json'),delta)
  assert old['selection_check']==new['selection_check']
  for key in ['input_sha256','n','M','N']:assert oc[key]==nc[key],key
  for key in ['numerical_rank','full_rank','trusted']:assert oc['reference'][key]==nc['reference'][key],key
  checks={'reference_kappa_relative_difference':abs(nc['reference']['kappa']/oc['reference']['kappa']-1),'methods':{}}
  for label,m in nc['methods'].items():
   om=oc['methods'][label];d=abs(m['gap']-om['gap']);checks['methods'][label]={'old_gap':om['gap'],'new_gap':m['gap'],'gap_abs_difference':d,'gap_screen':d<=max(1e-10,1e-6*om['gap']),'orth_screen':m['orth_max']<1e-12,'old_orth_max':om['orth_max'],'new_orth_max':m['orth_max'],'old_fit_test':om.get('adversarial_test_relative_error'),'new_fit_test':m.get('adversarial_test_relative_error')}
  checks['reference_kappa_screen']=checks['reference_kappa_relative_difference']<=1e-8
  receipt.update(output={'path':str(path),'bytes':path.stat().st_size,'sha256':sha(path)},difference_count=len(delta),comparison={'path':str(out/(name+'-differences.json')),'sha256':sha(out/(name+'-differences.json'))},checks=checks,scalar_differences=[d for d in delta if not d['path'].startswith('/target/qr_coefficients/')])
  write(out/(name+'-receipt.json'),receipt);result['cases'].append(receipt);write(out/'summary.json',result);print(name,checks,flush=True)
 write(out/'summary.json',result)
if __name__=='__main__':main()
