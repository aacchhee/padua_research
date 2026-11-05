#!/usr/bin/env python3
"""One explicitly allocated BJ20 scheduling successor; frozen engine unchanged."""
import argparse,hashlib,json,os,pathlib,platform,signal,subprocess,sys,time
from fractions import Fraction
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(1000000)
ENGINE='49b45df9c2c28e3e63e9b886ff873a744ea0f0a44cd5f51fe2e3a345eec81552'
BENCH='646a6490433a4744199ee64f497826e245332ffef10f6af9e94ce8d011ea9e6f'
OVERLAP='8beb9707865479caac8c03323fb3e1c171c6b05be13422bb48cbc6c8694fb2ed'
OLD='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
OLD14='0ecedcd23e7fce677f204aeed326847ef18c095ee3dd0d63ecffd3c9778e6287'
NATIVE='0f7c1475a0484aa0905bcdfddf938b4ea2154f58322228e17bb7a91955ca3cf7'
FIELDS=('Knode_squared','KHS_squared','Urow_squared','upper_squared')
AUTH='Root explicit 2026-11-05 scheduling successor: one first-time fused BJ20, ceiling1800s; prior60sFAIL preserved.'

def ident(path):
 p=pathlib.Path(path);b=p.read_bytes();return {'path':str(p.resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def pin(path,digest):
 v=ident(path);assert v['sha256']==digest,(v['path'],'input hash mismatch');return v
def recorded(record):
 v=pin(record['path'],record['sha256']);assert v['bytes']==record['bytes'];return v
def save(path,value):pathlib.Path(path).write_text(json.dumps(value,indent=2)+'\n')
def checks(a):
 engine=pathlib.Path(__file__).with_name('g1_fast.py');pin(engine,ENGINE)
 bench=json.loads(pathlib.Path(a.benchmark14).read_text());pin(a.benchmark14,BENCH)
 assert bench['result']=='EXACT_CASE_COMPLETED' and bench['code_sha256']==ENGINE
 assert (bench['set'],bench['rule'],bench['max_degree'])==('rotated','bj',14)
 assert bench['complete_degrees']==list(range(2,15))
 assert bench['all_original_nodes']==625 and bench['all_source_columns']==119
 assert bench['controls']['fresh_scalar_basis_degrees']==[2,3,4]
 assert bench['controls']['every_new_column_exact_Gram_pairings']
 assert bench['additional_exact_comparison_degrees']==list(range(2,15))
 # Keep the old condition's actual failure explicit; no fabricated accepted guard.
 assert bench['timing']['wall_seconds']>60
 ep=recorded(bench['endpoint_file']);old14=recorded(bench['additional_exact_comparison']);assert old14['sha256']==OLD14
 rows=json.loads(pathlib.Path(ep['path']).read_text())['runs'];oldrows=json.loads(pathlib.Path(old14['path']).read_text())['runs']
 oldmap={r['degree']:r for r in oldrows};assert [r['degree'] for r in rows]==list(range(2,15))
 for r in rows:
  o=oldmap[r['degree']]
  assert (r['set'],r['rule'],r['sources'],r['point_count'])==('rotated','bj','all',625)
  assert r['source_count']==(r['degree']+1)*(r['degree']+2)//2-1
  assert all(Fraction(r[f]['exact'])==Fraction(o[f]['exact']) for f in FIELDS)
  assert r['pivot_choices']==o['pivot_choices'] and r['pivot_ties']==o['pivot_ties']
 overlap=json.loads(pathlib.Path(a.overlap).read_text());pin(a.overlap,OVERLAP)
 assert overlap['code_sha256']==ENGINE and overlap['all_88_old_endpoint_choice_tie_rows_match']
 assert overlap['eight_fresh_d4_cases_all_scalar_d2_d3_d4_prefix_controls']
 native=pin(a.native20,NATIVE);native_rows=[json.loads(s) for s in pathlib.Path(a.native20).read_text().splitlines()]
 assert [r['degree'] for r in native_rows]==list(range(2,21))
 assert all(r['set']=='rotated' and r['rule']=='bj' and r['point_count']==625 and r['sources']=='all' for r in native_rows)
 return {'engine':pin(engine,ENGINE),'benchmark14':pin(a.benchmark14,BENCH),'old14':old14,'benchmark_endpoint':ep,'overlap':pin(a.overlap,OVERLAP),'old_sweep':pin(a.old_sweep,OLD),'native20':native,'plan':ident(a.plan)}

def worker(a,inputs):
 import g1_fast as engine
 assert engine.sha(engine.__file__)==ENGINE
 out=pathlib.Path(a.output_dir);state={'basis_degree':0,'last_source':0,'completed_degrees':[]}
 start=time.monotonic();cpu=time.process_time()
 launch={'authorization':AUTH,'wrapper':ident(__file__),'inputs':inputs,'worker_command':[sys.executable,'-B',*sys.argv],
         'signal_cap_seconds':1795,'external_case_cap_seconds':1800,'pre_run_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
         'runtime':{'python':platform.python_version(),'python_flint':engine.flint.__version__,'PYTHONPATH':os.environ.get('PYTHONPATH')},
         'old60s_condition':'FAIL; not used or falsified by this separate authorized wrapper'}
 save(out/'pre-run.json',launch)
 args=argparse.Namespace(set='rotated',rule='bj',degree=20,old_sweep=a.old_sweep,compare=a.native20)
 def expire(*_):raise TimeoutError('New scheduling successor1795s signal cap within1800s ceiling')
 signal.signal(signal.SIGALRM,expire);signal.alarm(1795)
 try:result=engine.run(args,out,state)
 except Exception as error:
  result={'result':'INCOMPLETE_COST_CAP' if isinstance(error,TimeoutError) else 'FAILED_OR_REJECTED','set':'rotated','rule':'bj','max_degree':20,
          'code_sha256':ENGINE,'state':state,'wall_seconds':time.monotonic()-start,'process_cpu_seconds':time.process_time()-cpu,'error':repr(error),
          'limits':['No missing-source endpoint/completed-case claim. No automatic retry.']}
 finally:signal.alarm(0)
 result.update(scheduling_successor=launch,rules_head='9825d184517db81d0aad8542fbd6639f2164b803')
 save(a.receipt,result);return 0 if result['result']=='EXACT_CASE_COMPLETED' else 2

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for name in ('benchmark14','overlap','old-sweep','native20','plan','output-dir','receipt'):ap.add_argument('--'+name,required=True)
 ap.add_argument('--worker',action='store_true',help=argparse.SUPPRESS);a=ap.parse_args();inputs=checks(a)
 if a.worker:return worker(a,inputs)
 out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False)
 assert not pathlib.Path(a.receipt).exists()
 command=[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:],'--worker']
 save(out/'supervisor-launch.json',{'authorization':AUTH,'command':command,'wrapper':ident(__file__),'inputs':inputs,'external_timeout_seconds':1800,'pre_run_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})
 try:return subprocess.run(command,timeout=1800).returncode
 except subprocess.TimeoutExpired:
  save(a.receipt,{'result':'INCOMPLETE_EXTERNAL_COST_CAP','set':'rotated','rule':'bj','max_degree':20,'code_sha256':ENGINE,'authorization':AUTH,'external_case_cap_seconds':1800,'inputs':inputs,'wrapper':ident(__file__),'limits':['Worker killed at1800s; no completed-case claim, no automatic retry.']});return 2
if __name__=='__main__':sys.exit(main())
