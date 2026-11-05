#!/usr/bin/env python3
"""Bounded independent common-denominator validation, with explicit moderate gate."""
import argparse,concurrent.futures,hashlib,json,pathlib,subprocess,sys,time
sys.dont_write_bytecode=True
from g1_independent_run import equal,validate
sys.set_int_max_str_digits(1000000)
ROOT=pathlib.Path(__file__).resolve().parents[3]
def ident(p):
 p=pathlib.Path(p);data=p.read_bytes();return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--old',required=True);ap.add_argument('--receipt',required=True);ap.add_argument('--mode',choices=['tiny','benchmark14'],required=True);ap.add_argument('--tiny-receipt');ap.add_argument('--benchmark-endpoints');a=ap.parse_args()
 out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=False);src=pathlib.Path(__file__).with_name('g1_fast_independent.cpp');exe=out/'g1_fast_independent';compile_cmd=['g++','-O3','-std=c++17',str(src),'-lgmpxx','-lgmp','-o',str(exe)]
 subprocess.run(compile_cmd,check=True);oldpath=pathlib.Path(a.old);assert ident(oldpath)['sha256']=='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344';old={(r['set'],r['rule'],r['degree']):r for r in json.loads(oldpath.read_text())['runs']}
 receipt={'status':'INCOMPLETE','rules_sha':'bb67c1ee830d468fa33007e15008d5574d00ccf4','mode':a.mode,'native_source':ident(src),'harness':ident(__file__),'old_input':ident(oldpath),'compile_command':compile_cmd,'command':sys.argv,'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0],'GMP_package_version':'2:6.3.0+dfsg-3','nodes':'All original625/325 explicit; no symmetry reduction','runs':[]}
 if a.mode=='tiny':
  primitive_cmd=[str(exe),'--self-test'];p=subprocess.run(primitive_cmd,capture_output=True,text=True,check=True);receipt['native_primitive_controls']={'command':primitive_cmd,'result':json.loads(p.stdout)}
  cases=[('rotated',r,4,30) for r in ('bj','mirror','alt','pivot')]+[('triangle',r,4,30) for r in ('bj','pivot')]
 else:
  gate=json.loads(pathlib.Path(a.tiny_receipt).read_text());assert gate['status']=='PASS tiny exact backend controls' and gate['native_source']['sha256']==ident(src)['sha256'];assert a.benchmark_endpoints
  benchpath=pathlib.Path(a.benchmark_endpoints);bench={(r['set'],r['rule'],r['degree']):r for r in json.loads(benchpath.read_text())['runs']};receipt['reference_benchmark']=ident(benchpath);receipt['tiny_gate']=ident(a.tiny_receipt);cases=[('rotated','bj',14,300)]
 def run(case):
  grid,rule,degree,cap=case;path=out/f'{grid}-{rule}-d{degree}.jsonl';log=out/f'{grid}-{rule}-d{degree}.log';cmd=[str(exe),grid,str(degree),rule];start=time.monotonic();result={'set':grid,'rule':rule,'degree':degree,'cap_seconds':cap,'command':cmd}
  try:
   with path.open('w') as f,log.open('w') as e:p=subprocess.run(cmd,stdout=f,stderr=e,timeout=cap)
   assert p.returncode==0,('native exit',p.returncode);rows=[json.loads(x) for x in path.read_text().splitlines()];assert len(rows)==degree-1
   for r in rows:
    validate(r)
    if r['degree']<=12:equal(r,old[grid,rule,r['degree']])
    elif a.mode=='benchmark14':
     equal(r,bench[grid,rule,r['degree']]);assert r['pivot_ties']==bench[grid,rule,r['degree']]['pivot_ties']
   result.update(status='PASS exact independent endpoint identities',rows=len(rows))
  except Exception as e:result.update(status='INCOMPLETE_OR_REJECTED',error=repr(e))
  result.update(elapsed_seconds=time.monotonic()-start,endpoint_file=ident(path),progress_log=ident(log));return result
 if a.mode=='tiny':
  with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:receipt['runs']=list(pool.map(run,cases))
 else:receipt['runs']=[run(cases[0])]
 receipt['status']=('PASS tiny exact backend controls' if a.mode=='tiny' else 'PASS original rotated BJ13/14 benchmark independently matched') if all(r['status'].startswith('PASS') for r in receipt['runs']) else 'INCOMPLETE_OR_REJECTED bounded exact run'
 pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'runs':receipt['runs']},indent=2));return 0 if receipt['status'].startswith('PASS') else 1
if __name__=='__main__':sys.exit(main())
