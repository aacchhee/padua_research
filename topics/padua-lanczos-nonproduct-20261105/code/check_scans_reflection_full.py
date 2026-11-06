#!/usr/bin/env python3
"""Independent high reflection replay and subsequent accepted-bundle/N2 checks.

Run mode actually executes ALT and PIVOT only. Validate mode verifies supplied
BJ/mirror artifacts but never labels them fresh high-degree independent reruns.
"""
import argparse,concurrent.futures,hashlib,itertools,json,platform,re,subprocess,sys,time
from fractions import Fraction as F
from pathlib import Path
from check_scans_review import log_bounds,extrema,decision,rounded
sys.set_int_max_str_digits(1000000)
TOP=Path(__file__).resolve().parents[1];ROOT=TOP.parents[1]
EVID=TOP/'evidence'
WORK=Path('/tmp/padua-lanczos-nonproduct-20261105/scan-review-reflection16')
INPUT=Path('/tmp/padua-lanczos-nonproduct-20261105/p6/full16-D36x9/input.txt')
SOURCE=TOP/'code/p6_reflection_scalar.cpp'
SOURCE_PIN='09d524f915076105b04fb196ee98c6c6cd4cecbc6b6e49bcfacb541ffc999088'
INPUT_PIN='48977eefea1c662c3ef23c8ed17d49e3cb0310a6d53321add8c51c91866313f6'
RULES=('bj','mirror','alt','pivot')
FIELDS=('Knode_squared','KHS_squared','Urow_squared','upper_squared')
def ident(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def checked(rec):
 p=Path(rec['path']);value=ident(p);assert value['bytes']==rec['bytes'] and value['sha256']==rec['sha256'];return p

def rowread(path,rule):
 data=[json.loads(s) for s in Path(path).read_text().splitlines()]
 assert [r['degree'] for r in data]==list(range(2,17))
 for r in data:
  s=r['degree'];n=(s+1)*(s+2)//2
  assert r['set']=='D36x9' and r['rule']==rule and r['point_count']==324 and r['basis_count']==n
  assert r['sources']=='all' and r['source_count']==n-1 and F(r['normal_trace_exact'])==324-n
  assert r['exact_gram_pairs_checked']==153*152//2
  vals=[F(r[f]['exact']) for f in FIELDS];assert 0<vals[0]<=vals[3]==min(vals[1:3])
  assert len(r['pivot_choices'])==n-1
 return data

def scientific(row):return {k:v for k,v in row.items() if k!='elapsed_seconds'}
def compare(a,b):assert [scientific(v) for v in a]==[scientific(v) for v in b]

def parse_guards(path,rule):
 text=Path(path).read_text();matches={}
 for name in ('reflection_orbits','reflection_guards'):
  found=re.findall('^'+name+r' (.+)$',text,re.M);assert len(found)==1;matches[name]=json.loads(found[0])
 assert matches['reflection_orbits']==dict(nodes=324,representatives=90,size1=0,size2=18,size4=72)
 exponents=[(t-j,j) for t in range(17) for j in range(t+1)]
 parents=slots=zeros=0
 for k,(a,b) in enumerate(exponents[1:],1):
  candidates=2 if rule=='pivot' and a>0 and b>0 else 1
  parents+=candidates;slots+=k*candidates
  zeros+=candidates*sum((u%2,v%2)!=(a%2,b%2) for u,v in exponents[:k])
 snapshots=324*sum((s+1)*(s+2)//2-1 for s in range(2,17))
 expected=dict(basis_parity_scalar_checks=2*324*153,parent_exponent_checks=parents,alpha_slots_checked=slots,cross_parity_zeros_checked=zeros,source_positions=152,expanded_node_source_snapshots=snapshots,expected_expanded_node_source_snapshots=snapshots)
 assert snapshots==307800 and matches['reflection_guards']==expected
 return matches

def run():
 WORK.mkdir(exist_ok=False)
 sourceid=ident(SOURCE);inputid=ident(INPUT);assert sourceid['sha256']==SOURCE_PIN and inputid['sha256']==INPUT_PIN
 bp=EVID/'p6-disk16-producer-bundle.json';bundle=json.loads(bp.read_text());assert bundle['family']=='D36x9' and bundle['max_degree']==16
 assert {r['rule'] for r in bundle['cases']}==set(RULES) and len(bundle['cases'])==4
 producers={r['rule']:r for r in bundle['cases']}
 for r in producers.values():assert r['status'].startswith('PASS');rowread(checked(r['output']),r['rule'])
 exe=WORK/'reflection';compilecmd=['g++','-O3','-std=c++17',str(SOURCE),'-lgmpxx','-lgmp','-o',str(exe)];subprocess.run(compilecmd,check=True)
 target=EVID/'check-scans-reflection-full-execution.json'
 record=dict(status='INCOMPLETE independent high ALT/PIVOT execution',command=[sys.executable,'-B',*sys.argv],harness=ident(__file__),source=sourceid,input=inputid,producer_bundle=ident(bp),compile_command=compilecmd,binary=ident(exe),head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],gmp=subprocess.check_output(['pkg-config','--modversion','gmp'],text=True).strip(),python=platform.python_version(),platform=platform.platform(),per_case_seconds=3600,max_concurrent_cases=2,rules_actually_launched=['alt','pivot'],rules_not_freshly_replayed=['bj','mirror'],runs=[])
 def save():target.write_text(json.dumps(record,indent=2)+'\n')
 save()
 def case(rule):
  out=WORK/(rule+'.jsonl');log=WORK/(rule+'.log');cmd=[str(exe),str(INPUT),'16',rule,'D36x9'];t=time.monotonic();result=dict(rule=rule,command=cmd,cap_seconds=3600)
  try:
   with out.open('w') as stdout,log.open('w') as stderr:subprocess.run(cmd,stdout=stdout,stderr=stderr,check=True,timeout=3600)
   data=rowread(out,rule);ref=producers[rule]['output'];compare(data,rowread(checked(ref),rule))
   guards=parse_guards(log,rule)
   assert ident(SOURCE)==sourceid and ident(INPUT)==inputid
   result.update(status='PASS fresh15rows all nonelapsed fields including Gram',exit_code=0,rows=15,producer_reference=ref,guard_records=guards)
  except Exception as exc:result.update(status='INCOMPLETE_OR_FAILED',error=repr(exc))
  result.update(wall_seconds=time.monotonic()-t,output=ident(out),log=ident(log));return result
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  futures=[pool.submit(case,rule) for rule in ('alt','pivot')]
  for future in concurrent.futures.as_completed(futures):
   result=future.result();record['runs'].append(result);save();print(json.dumps({k:result[k] for k in ('rule','status','wall_seconds')}),flush=True)
 if len(record['runs'])==2 and all(r['status'].startswith('PASS') for r in record['runs']):record.update(status='PASS independent high ALT/PIVOT execution',rows=30,scope='Fresh D36x9 ALT/PIVOT2..16 only; primary all-rule completion and N2 validation remain separate')
 save();return 0 if record['status'].startswith('PASS') else 1

def validate():
 primarypath=EVID/'p6-disk16-reflection-acceptance.json';primary=json.loads(primarypath.read_text())
 assert primary['status']=='PASS exact two-path weighted finite scan' and primary['exact_rows_compared']==60 and primary['max_degree']==16
 assert primary['input']['native_input_sha256']==INPUT_PIN
 assert len(primary['runs'])==8
 loaded={}
 for runrecord in primary['runs']:
  assert runrecord['status'].startswith('PASS');key=runrecord['backend'],runrecord['rule'];assert key not in loaded
  loaded[key]=rowread(checked(runrecord['output']),key[1])
 assert set(loaded)==set(itertools.product(('producer','checker'),RULES))
 for rule in RULES:compare(loaded['producer',rule],loaded['checker',rule])
 ownpath=EVID/'check-scans-reflection-full-execution.json';own=json.loads(ownpath.read_text());assert own['status']=='PASS independent high ALT/PIVOT execution'
 matched=[]
 for r in own['runs']:
  data=rowread(checked(r['output']),r['rule']);compare(data,loaded['checker',r['rule']]);matched.append(dict(rule=r['rule'],rows=15,own_output=r['output'],primary_output=next(v['output'] for v in primary['runs'] if (v['backend'],v['rule'])==('checker',r['rule']))))
 result=dict(status='PASS accepted all-rule artifacts and fresh ALT/PIVOT replay match',command=[sys.executable,'-B',*sys.argv],harness=ident(__file__),primary_receipt=ident(primarypath),fresh_execution_receipt=ident(ownpath),primary_producer_checker_rows_compared=60,fresh_to_primary_rows_compared=30,matches=matched,limit='BJ/mirror16 artifacts verified, not freshly executed by this checker')
 (EVID/'check-scans-reflection-full-comparison.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status']);return 0

def fits():
 primarypath=EVID/'p6-disk16-reflection-acceptance.json';primary=json.loads(primarypath.read_text());assert primary['status']=='PASS exact two-path weighted finite scan' and len(primary['runs'])==8
 target=EVID/'p6-n2-D36x9.json';data=json.loads(target.read_text());assert data['family']=='D36x9'
 checked(data['scan_receipt']);assert Path(data['scan_receipt']['path']).resolve()==primarypath.resolve()
 loaded={}
 for r in primary['runs']:
  assert r['status'].startswith('PASS');key=r['backend'],r['rule'];assert key not in loaded;loaded[key]=rowread(checked(r['output']),r['rule'])
 assert set(loaded)==set(itertools.product(('producer','checker'),RULES))
 for rule in RULES:compare(loaded['producer',rule],loaded['checker',rule])
 end={(rule,r['degree']):(F(r[FIELDS[0]]['exact']),F(r[FIELDS[-1]]['exact'])) for (backend,rule),rr in loaded.items() if backend=='producer' for r in rr}
 ratios={}
 for degree in range(8,17):
  low=end['bj',degree][0]/min(end[r,degree][1] for r in RULES);high=end['bj',degree][1]/min(end[r,degree][0] for r in RULES)
  a,b=log_bounds(low),log_bounds(high);claim=list(map(F,data['logratio_outward'][str(degree)]))
  assert claim[0]<=a[0]/2<=a[1]/2 and b[0]/2<=b[1]/2<=claim[1];ratios[degree]=(a[0]/2,b[1]/2)
 windows=[extrema(ratios,start) for start in (8,12)]
 for (lo,hi),w in zip(windows,data['windows']):
  assert F(w['lower_exact'])<=lo<=hi<=F(w['upper_exact'])
  assert F(w['checker_lower_exact'])<=lo<=hi<=F(w['checker_upper_exact'])
 assert decision(windows)==data['N2_verdict']
 result=dict(status='PASS independent D36x9 rational logs and signed OLS extrema',family='D36x9',command=[sys.executable,'-B',*sys.argv],harness=ident(__file__),arithmetic=ident(Path(__file__).with_name('check_scans_review.py')),primary_receipt=ident(primarypath),N2_receipt=ident(target),independent_log_bounds_contained=18,windows_outward=[rounded(v) for v in windows],N2_verdict=decision(windows),method='192-bit mantissa bounds;96-term rational atanh series;32 exact OLS corners per window',scope='Finite endpoint-interval screen, not exact capacity or an asymptotic rate')
 (EVID/'check-scans-reflection-full-n2.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return 0
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=('run','validate','fits'),required=True);args=ap.parse_args();sys.exit(dict(run=run,validate=validate,fits=fits)[args.mode]())
