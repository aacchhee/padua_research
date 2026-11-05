#!/usr/bin/env python3
"""One remaining-rule scheduling successor; unchanged exact numerical engine."""
import argparse,hashlib,json,os,pathlib,platform,signal,subprocess,sys,time
from fractions import Fraction
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(1000000)
ENGINE='49b45df9c2c28e3e63e9b886ff873a744ea0f0a44cd5f51fe2e3a345eec81552'
OVERLAP='8beb9707865479caac8c03323fb3e1c171c6b05be13422bb48cbc6c8694fb2ed'
OLD='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
NATIVE='b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc'
FIELDS=('Knode_squared','KHS_squared','Urow_squared','upper_squared')
AUTH='Root explicit2026-11-05 remaining rotated mirror/alt/pivot20: each1800s, max2producer workers, no numerical change; prior60sFAIL preserved.'

def ident(path):
 p=pathlib.Path(path);b=p.read_bytes();return {'path':str(p.resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def pin(path,digest):
 v=ident(path);assert v['sha256']==digest,(v['path'],'hash mismatch');return v
def recorded(record):
 v=pin(record['path'],record['sha256']);assert v['bytes']==record['bytes'];return v
def save(path,value):pathlib.Path(path).write_text(json.dumps(value,indent=2)+'\n')
def validate(r,rule,native=False):
 n=r['degree'];N=(n+1)*(n+2)//2;assert type(n)is int and 2<=n<=20
 assert (r['set'],r['rule'],r['sources'],r['point_count'],r['source_count'],r['basis_count'])==('rotated',rule,'all',625,N-1,N)
 assert len(r['pivot_choices'])==N-1 and set(r['pivot_choices'])<=set('XY')
 if rule=='pivot':
  ties=r['pivot_ties'];assert all(len(t)==2 and 2<=t[0]<=n and 0<t[1]<t[0] for t in ties)
  assert ties==[list(t) for t in sorted(set(tuple(t) for t in ties))]
  assert [t for t in ties if t[0]<=12]==[[2,1]]
 else:assert r['pivot_ties']==[]
 if native:assert r['exact_gram_pairs_checked']>=N*(N-1)//2
 assert Fraction(r['normal_trace_exact'])==625-N
 v=[Fraction(r[f]['exact']) for f in FIELDS];assert all(x>0 for x in v) and v[0]<=v[3]==min(v[1:3])
def equal(r,o):
 for f in ('set','rule','degree','sources','point_count','source_count','basis_count','pivot_choices'):assert r[f]==o[f],f
 ties=o.get('pivot_ties',[[2,1]] if o['set']=='rotated' and o['rule']=='pivot' and o['degree']<=12 else [])
 assert r['pivot_ties']==ties
 assert all(Fraction(r[f]['exact'])==Fraction(o[f]['exact']) for f in FIELDS)
def checks(a):
 engine=pin(pathlib.Path(__file__).with_name('g1_fast.py'),ENGINE);old=pin(a.old_sweep,OLD)
 oldrows={(r['set'],r['rule'],r['degree']):r for r in json.loads(pathlib.Path(a.old_sweep).read_text())['runs']}
 overlap_id=pin(a.overlap,OVERLAP);overlap=json.loads(pathlib.Path(a.overlap).read_text())
 assert overlap['code_sha256']==ENGINE and overlap['all_88_old_endpoint_choice_tie_rows_match']
 assert overlap['eight_fresh_d4_cases_all_scalar_d2_d3_d4_prefix_controls']
 case=next(c for c in overlap['cases'] if c['set']=='rotated' and c['rule']==a.rule)
 case_id=recorded(case['receipt']);receipt=json.loads(pathlib.Path(case_id['path']).read_text())
 assert receipt['result']=='EXACT_CASE_COMPLETED' and receipt['code_sha256']==ENGINE and receipt['max_degree']==12
 assert receipt['complete_degrees']==list(range(2,13)) and receipt['all_original_nodes']==625 and receipt['all_source_columns']==90
 assert receipt['controls']['fresh_scalar_basis_degrees']==[2,3,4] and receipt['controls']['every_new_column_exact_Gram_pairings']
 ep=recorded(receipt['endpoint_file']);rows=json.loads(pathlib.Path(ep['path']).read_text())['runs'];assert [r['degree'] for r in rows]==list(range(2,13))
 for r in rows:validate(r,a.rule);equal(r,oldrows['rotated',a.rule,r['degree']])
 native_id=ident(a.native_receipt);native=json.loads(pathlib.Path(a.native_receipt).read_text())
 assert native['status']=='PASS native exact remaining-rule20; fresh producer comparison pending'
 native_source=recorded(native['native_source']);assert native_source['sha256']==NATIVE
 assert native['completed_degrees']==list(range(2,21)) and native['node_count']==625 and native['source_count_at20']==230
 nep=recorded(native['endpoint_file']);nrows=[json.loads(line) for line in pathlib.Path(nep['path']).read_text().splitlines()]
 assert [r['degree'] for r in nrows]==list(range(2,21))
 for r in nrows:
  validate(r,a.rule,True)
  if r['degree']<=12:equal(r,oldrows['rotated',a.rule,r['degree']])
 return {'engine':engine,'old_sweep':old,'overlap_summary':overlap_id,'same_rule_overlap_receipt':case_id,'same_rule_overlap_endpoint':ep,
         'native_receipt':native_id,'native_source':native_source,'native_endpoint':nep,'plan':ident(a.plan)}
def worker(a,inputs):
 import g1_fast as engine
 assert engine.sha(engine.__file__)==ENGINE
 out=pathlib.Path(a.output_dir);state={'basis_degree':0,'last_source':0,'completed_degrees':[]};start=time.monotonic();cpu=time.process_time()
 launch={'authorization':AUTH,'rule':a.rule,'wrapper':ident(__file__),'inputs':inputs,'worker_command':[sys.executable,'-B',*sys.argv],
         'signal_cap_seconds':1795,'external_case_cap_seconds':1800,'pre_run_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
         'runtime':{'python':platform.python_version(),'python_flint':engine.flint.__version__,'PYTHONPATH':os.environ.get('PYTHONPATH')},
         'old60s_condition':'FAIL preserved; separate explicit scheduling successor'}
 save(out/'pre-run.json',launch)
 args=argparse.Namespace(set='rotated',rule=a.rule,degree=20,old_sweep=a.old_sweep,compare=inputs['native_endpoint']['path'])
 def expire(*_):raise TimeoutError('Remaining20 scheduling successor1795s signal cap inside1800s ceiling')
 signal.signal(signal.SIGALRM,expire);signal.alarm(1795)
 try:result=engine.run(args,out,state)
 except Exception as error:
  result={'result':'INCOMPLETE_COST_CAP' if isinstance(error,TimeoutError) else 'FAILED_OR_REJECTED','set':'rotated','rule':a.rule,'max_degree':20,
          'code_sha256':ENGINE,'state':state,'wall_seconds':time.monotonic()-start,'process_cpu_seconds':time.process_time()-cpu,'error':repr(error),
          'limits':['No missing-source endpoint or completed-case claim; no automatic retry.']}
 finally:signal.alarm(0)
 result.update(scheduling_successor=launch,rules_head='9825d184517db81d0aad8542fbd6639f2164b803');save(a.receipt,result)
 return 0 if result['result']=='EXACT_CASE_COMPLETED' else 2
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--rule',choices=['mirror','alt','pivot'],required=True)
 for name in ('overlap','old-sweep','native-receipt','plan','output-dir','receipt'):ap.add_argument('--'+name,required=True)
 ap.add_argument('--worker',action='store_true',help=argparse.SUPPRESS);a=ap.parse_args();inputs=checks(a)
 if a.worker:return worker(a,inputs)
 out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False);assert not pathlib.Path(a.receipt).exists()
 command=[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:],'--worker']
 save(out/'supervisor-launch.json',{'authorization':AUTH,'command':command,'wrapper':ident(__file__),'inputs':inputs,'external_timeout_seconds':1800,'pre_run_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})
 try:return subprocess.run(command,timeout=1800).returncode
 except subprocess.TimeoutExpired:
  save(a.receipt,{'result':'INCOMPLETE_EXTERNAL_COST_CAP','set':'rotated','rule':a.rule,'max_degree':20,'code_sha256':ENGINE,'authorization':AUTH,'external_case_cap_seconds':1800,'inputs':inputs,'wrapper':ident(__file__),'limits':['Worker killed at1800s; no completed-case claim or automatic retry.']});return 2
if __name__=='__main__':sys.exit(main())
