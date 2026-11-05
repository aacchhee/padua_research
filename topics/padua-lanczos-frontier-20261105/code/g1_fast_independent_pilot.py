#!/usr/bin/env python3
"""One authorized BJ20 exact native pilot; hard600-second cap, no other rules."""
import argparse,hashlib,json,pathlib,subprocess,sys,time
sys.dont_write_bytecode=True
from g1_independent_run import equal,validate
from g1_fast_independent_run import ident
sys.set_int_max_str_digits(1000000)
PIN='b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--old',required=True);ap.add_argument('--benchmark-receipt',required=True);ap.add_argument('--benchmark-endpoints',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args()
 out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=False);src=pathlib.Path(__file__).with_name('g1_fast_independent.cpp');assert ident(src)['sha256']==PIN
 gate=json.loads(pathlib.Path(a.benchmark_receipt).read_text());assert gate['status']=='PASS original rotated BJ13/14 benchmark independently matched' and gate['native_source']['sha256']==PIN
 oldpath=pathlib.Path(a.old);assert ident(oldpath)['sha256']=='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
 old={(r['set'],r['rule'],r['degree']):r for r in json.loads(oldpath.read_text())['runs']};benchpath=pathlib.Path(a.benchmark_endpoints);bench={(r['set'],r['rule'],r['degree']):r for r in json.loads(benchpath.read_text())['runs']}
 exe=out/'g1_fast_independent';compile_cmd=['g++','-O3','-std=c++17',str(src),'-lgmpxx','-lgmp','-o',str(exe)];subprocess.run(compile_cmd,check=True)
 cmd=[str(exe),'rotated','20','bj'];path=out/'rotated-bj-d20.jsonl';log=out/'rotated-bj-d20.log';start=time.monotonic();status='INCOMPLETE';error=None
 try:
  with path.open('w') as f,log.open('w') as e:p=subprocess.run(cmd,stdout=f,stderr=e,timeout=600)
  assert p.returncode==0,('native exit',p.returncode);status='NATIVE_COMPLETED'
 except Exception as e:error=repr(e)
 elapsed=time.monotonic()-start;rows=[json.loads(line) for line in path.read_text().splitlines()]
 for r in rows:
  validate(r);assert r['set']=='rotated' and r['rule']=='bj'
  if r['degree']<=12:equal(r,old['rotated','bj',r['degree']])
  elif r['degree']<=14:equal(r,bench['rotated','bj',r['degree']])
 assert [r['degree'] for r in rows]==list(range(2,2+len(rows)))
 if status=='NATIVE_COMPLETED':assert len(rows)==19
 receipt={'status':'PASS native exact BJ20 pilot; fresh producer comparison pending' if status=='NATIVE_COMPLETED' else 'INCOMPLETE bounded BJ20 pilot','rules_sha':'bb67c1ee830d468fa33007e15008d5574d00ccf4','native_source':ident(src),'launcher':ident(__file__),'validation_dependency':ident(pathlib.Path(__file__).with_name('g1_independent_run.py')),'benchmark_gate':ident(a.benchmark_receipt),'old_input':ident(oldpath),'benchmark_endpoints':ident(benchpath),'compile_command':compile_cmd,'command':cmd,'invocation':['python','-B',*sys.argv],'cap_seconds':600,'elapsed_seconds':elapsed,'completed_degrees':[r['degree'] for r in rows],'node_count':625,'source_count_at20':230,'endpoint_file':ident(path),'progress_log':ident(log),'last_event':log.read_text().splitlines()[-1] if log.stat().st_size else None,'error':error,'limits':'All sources and all625 nodes required; no fits or target status; fresh producer comparison mandatory.'}
 pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2));return 0 if status=='NATIVE_COMPLETED' else 1
if __name__=='__main__':sys.exit(main())
