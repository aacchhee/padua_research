#!/usr/bin/env python3
"""Executed bounded arithmetic/coverage controls, never a degree certificate."""
import copy,ctypes,gzip,hashlib,json,pathlib,time
from fractions import Fraction as F
import check as ck
BASE=ck.ROOT
SOURCE=BASE/'topics/padua-argmax-bridge-20261105/code/phase_checker'
OUT=BASE/'local-output/argmax-bridge-20261105/phase-checker'
SAMPLES=BASE/'local-output/argmax-bridge-20261105/N3/outward-calibration-v1'

def main():
 t=time.process_time();k=ck.Kernel();sample_reports=[]
 for suffix in ['far','nonlocal-defect','local']:
  p=SAMPLES/f'n17-sample-{suffix}.json';d=json.loads(p.read_text());r=ck.check(d,k)
  assert not r['accepted'] and not r['failed_leaves']
  sample_reports.append({'file':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'replay':r})
 d=json.loads((SAMPLES/'n17-sample-far.json').read_text())
 def mutation(name,mutate):
  x=copy.deepcopy(d);mutate(x)
  try:r=ck.check(x,k);rejected=not r['accepted'] and (bool(r.get('failed_leaves')) or bool(r.get('error')));reason='leaf predicate failed' if rejected else 'incomplete only'
  except ck.Invalid as e:rejected=True;reason=str(e)
  assert rejected,name
  return {'name':name,'rejected':rejected,'reason':reason}
 corrupt=[]
 corrupt.append(mutation('false complete',lambda x:x.update(complete=True)))
 corrupt.append(mutation('remove pending region',lambda x:x['pending'].pop()))
 corrupt.append(mutation('duplicate leaf',lambda x:x['leaves'].append(copy.deepcopy(x['leaves'][0]))))
 corrupt.append(mutation('ancestor overlap',lambda x:x['leaves'].append({'root':3,'path':'','kind':'far'})))
 corrupt.append(mutation('root omission',lambda x:x['roots'].pop()))
 corrupt.append(mutation('pi shrink',lambda x:x['constants'].__setitem__(1,3.14)))
 corrupt.append(mutation('inflated corner threshold',lambda x:x['constants'].__setitem__(2,100.)))
 corrupt.append(mutation('false outside',lambda x:x['leaves'][0].update(kind='outside')))
 corrupt.append(mutation('false local radius',lambda x:x['leaves'][0].update(kind='local-corner-plus-defect')))
 corrupt.append(mutation('unknown kind',lambda x:x['leaves'][0].update(kind='unproved-new-patch')))
 overlap=[]
 for n in [17,24,32]:
  p=BASE/f'topics/padua-argmax-effective-20261103/evidence/n{n}.json.gz'
  old=json.loads(gzip.decompress(p.read_bytes()));scale=old['scale'];q=old['threshold_interval']
  own=k.bounds(n,[0.,0.,0.,0.]);oldlo,oldhi=F(q[0],scale),F(q[1],scale)
  agree=F(own[3])<=oldhi and oldlo<=F(own[4]);assert agree
  overlap.append({'n':n,'inherited_certificate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
   'constant_intervals_overlap':agree,'independent_Lc':[own[3],own[4]],'note':'constant overlap only; no Bernstein leaf replay'})
 # Different finite formula: direct D_n triangular sum at 80-digit precision.
 import mpmath as mp
 mp.mp.dps=80
 fn=k.lib.phase_term;fn.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.POINTER(ctypes.c_double)];fn.restype=ctypes.c_int
 point_checks=[]
 for n,r,s,a,b in [(3,0,0,0.,0.),(3,3,4,0.,0.),(3,0,4,0.,0.),(17,5,8,.2,.3),(24,24,25,0.,0.),(32,0,0,.01,-.01)]:
  u=(r*mp.pi+mp.mpf(a))/n;v=(s*mp.pi+mp.mpf(b))/(n+1)
  val=mp.mpf(0);da=mp.mpf(0);db=mp.mpf(0)
  for i in range(n+1):
   for j in range(n+1-i):
    coeff=(1 if i==0 else 2)*(1 if j==0 else 2)-(1 if (i,j)==(n,0) else 0)
    val+=coeff*mp.cos(i*u)*mp.cos(j*v)
    da-=coeff*i*mp.sin(i*u)*mp.cos(j*v)/n
    db-=coeff*j*mp.cos(i*u)*mp.sin(j*v)/(n+1)
  out=(ctypes.c_double*6)();assert fn(n,r,s,a,b,out)==0
  # Diagnostic numerical agreement, not a proof of interval containment at
  # exact zero: mpmath residuals are allowed below 10^-70 there.
  ok=all(mp.mpf(out[2*i])-mp.mpf('1e-70')<=x<=mp.mpf(out[2*i+1])+mp.mpf('1e-70') for i,x in enumerate([val,da,db]));assert ok
  point_checks.append({'n':n,'r':r,'s':s,'alpha':a,'beta':b,'triangular_value_and_gradient_agree':ok})
 times=[]
 for n in [17,24,32,33]:
  t0=time.process_time();o=k.bounds(n,[.2,.20001,.3,.30001]);elapsed=time.process_time()-t0
  times.append({'n':n,'cpu_seconds_per_box':elapsed,'bounds':o[:3]})
 sources=[{'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(SOURCE.glob('*')) if p.is_file()]
 report={'status':'MEASURED bounded replay; full cover absent; independent review pending',
  'rules_input':'3dda890275a7599caa707b0fb8c0b6e6f6a80643','developer':'Codex Sol medium (as allocated; runtime metadata not independently exposed)',
  'samples':sample_reports,'negative_controls':corrupt,'overlap':overlap,'point_checks':point_checks,'cost':times,'sources':sources,
  'supplied_numeric_bounds_policy':'not trusted; leaf predicates recomputed independently; bound-only metadata corruption is intentionally irrelevant',
  'cpu_seconds':time.process_time()-t}
 (OUT/'controls-full.json').write_text(json.dumps(report,indent=2)+'\n')
 # Keep committed evidence compact; bulk replay stays local.
 compact=copy.deepcopy(report)
 for row in compact['samples']:row['replay'].pop('replay');row['replay'].pop('failed_leaves')
 p=BASE/'topics/padua-argmax-bridge-20261105/evidence/phase-checker-calibration.json';p.write_text(json.dumps(compact,indent=2)+'\n')
 print(json.dumps({'negative_controls':len(corrupt),'sample_predicates_pass':len(sample_reports),'overlap_degrees':[17,24,32],'cost':times,'cpu_seconds':report['cpu_seconds']},indent=2))
if __name__=='__main__':main()
