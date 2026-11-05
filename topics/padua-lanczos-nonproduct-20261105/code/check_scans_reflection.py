#!/usr/bin/env python3
"""Fresh independently executed reflection-scalar pilot and rejection controls.

Compares every original JSON field except elapsed_seconds, including total Gram
count because the original reference and replay have the same degree cap.
"""
import argparse,hashlib,json,platform,re,subprocess,sys,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
TOP=Path(__file__).resolve().parents[1]
WORK=Path('/tmp/padua-lanczos-nonproduct-20261105/scan-review')
RULES=('bj','mirror','alt','pivot')
PIN='09d524f915076105b04fb196ee98c6c6cd4cecbc6b6e49bcfacb541ffc999088'
def ident(p):
 p=Path(p);raw=p.read_bytes();return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def scientific(row):return {k:v for k,v in row.items() if k!='elapsed_seconds'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--family',choices=('D36x9','D65x9'),required=True);args=ap.parse_args()
 wd=WORK/('reflection-'+args.family+'-d8');wd.mkdir(exist_ok=False)
 original=(WORK/'D36x9') if args.family=='D36x9' else Path('/tmp/padua-lanczos-nonproduct-20261105/p6/pilot8-D65x9')
 inp=original/'input.txt';source=TOP/'code/p6_reflection_scalar.cpp';startident=ident(source);assert startident['sha256']==PIN
 exe=wd/'checker';compilecmd=['g++','-O3','-std=c++17',str(source),'-lgmpxx','-lgmp','-o',str(exe)];subprocess.run(compilecmd,check=True)
 record=dict(status='INCOMPLETE fresh reflection replay',family=args.family,max_degree=8,command=[sys.executable,'-B',*sys.argv],head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),harness=ident(__file__),source=startident,compile_command=compilecmd,binary=ident(exe),input=ident(inp),python=platform.python_version(),compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],gmp=subprocess.check_output(['pkg-config','--modversion','gmp'],text=True).strip(),per_case_seconds=60,concurrency='one native process; coordinated after developer pilot slot release',runs=[],negative_controls=[])
 target=TOP/'evidence'/('check-scans-reflection-'+args.family+'.json')
 def save():target.write_text(json.dumps(record,indent=2)+'\n')
 # Original normalized data; malformed controls preserve positive weights,
 # full node count and normalization, isolating the new hypotheses.
 lines=inp.read_text().splitlines();points=[list(map(F,s.split())) for s in lines[1:]]
 assert len(points)==324 and sum(p[2] for p in points)==1
 controls=[]
 altered=[p[:] for p in points];altered[0][0]+=F(1,1000000);controls.append(('nonclosed nodes',altered,'missing exact reflected node'))
 altered=[p[:] for p in points];altered[0][2]+=F(1,648);altered[1][2]-=F(1,648);controls.append(('unequal reflected weights',altered,'unequal exact reflected weights'))
 for name,data,expected in controls:
  bad=wd/(name.replace(' ','-')+'.txt');bad.write_text('324\n'+''.join(' '.join(map(str,p))+'\n' for p in data))
  cmd=[str(exe),str(bad),'2','bj',args.family];p=subprocess.run(cmd,capture_output=True,text=True,timeout=10)
  assert p.returncode!=0 and expected in p.stderr
  record['negative_controls'].append(dict(control=name,command=cmd,input=ident(bad),returncode=p.returncode,diagnostic=p.stderr.strip()))
 control=subprocess.run([str(exe),'--guard-self-test'],text=True,capture_output=True,check=True,timeout=10)
 record['internal_guard_controls']=json.loads(control.stdout);save()
 for rule in RULES:
  out=wd/(rule+'.jsonl');log=wd/(rule+'.log');cmd=[str(exe),str(inp),'8',rule,args.family];t=time.monotonic()
  with out.open('w') as stdout,log.open('w') as stderr:
   try:
    result=subprocess.run(cmd,stdout=stdout,stderr=stderr,check=True,timeout=60);status='completed'
   except subprocess.TimeoutExpired:status='INCOMPLETE timeout60'
   except subprocess.CalledProcessError as exc:status='FAILED '+str(exc.returncode)
  run=dict(rule=rule,command=cmd,status=status,wall_seconds=time.monotonic()-t,output=ident(out),log=ident(log));record['runs'].append(run);save()
  if status!='completed':return 1
  rows=[json.loads(s) for s in out.read_text().splitlines()];assert [r['degree'] for r in rows]==list(range(2,9))
  refs=[]
  for backend in ('producer','checker'):
   ref=original/(backend+'-'+rule+'.jsonl');expected=[json.loads(s) for s in ref.read_text().splitlines()]
   assert [scientific(r) for r in rows]==[scientific(r) for r in expected]
   refs.append(ident(ref))
  text=log.read_text();orbit=json.loads(re.search(r'^reflection_orbits (.+)$',text,re.M).group(1));guards=json.loads(re.search(r'^reflection_guards (.+)$',text,re.M).group(1))
  assert orbit==dict(nodes=324,representatives=90,size1=0,size2=18,size4=72)
  assert guards['basis_parity_scalar_checks']==2*324*45
  assert guards['parent_exponent_checks']==(72 if rule=='pivot' else 44)
  assert guards['source_positions']==44
  expected_snapshots=324*sum((s+1)*(s+2)//2-1 for s in range(2,9))
  assert guards['expanded_node_source_snapshots']==guards['expected_expanded_node_source_snapshots']==expected_snapshots
  assert guards['cross_parity_zeros_checked']>0 and guards['alpha_slots_checked']>=990
  run.update(status='PASS all nonelapsed fields including Gram count',reference_outputs=refs,rows=7,reflection_orbits=orbit,reflection_guards=guards)
  save();print(json.dumps(dict(family=args.family,rule=rule,status=run['status'],wall_seconds=run['wall_seconds'])),flush=True)
 assert ident(source)==startident
 record.update(status='PASS fresh full-field reflection pilot',exact_rows_compared=28,reference_comparisons=56,scope='2..8 only; all original sources/nodes/fields retained; no degree16 or speed claim');save();return 0
if __name__=='__main__':sys.exit(main())
