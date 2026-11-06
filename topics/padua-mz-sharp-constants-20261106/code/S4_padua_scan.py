#!/usr/bin/env python3
"""Registered signed-Padua finite validation/pilot/minima; guarded measurements."""
import argparse,datetime,hashlib,importlib.util,json,os,platform,resource,sys,time
from pathlib import Path
import numpy as np
import scipy
from scipy.sparse.linalg import LinearOperator,eigsh
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
SOURCE=ROOT/'topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py'
PROPOSAL=HERE.parent/'S4-padua-proposal.json'
spec=importlib.util.spec_from_file_location('padua_frozen',SOURCE);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class BudgetLimit(RuntimeError):pass
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def moments(k):return 0. if k%2 else 2./(1-k*k)
def weights_check(m,op):
 nodes=[(j,k) for j in range(m+1) for k in range(m+2) if (j+k)%2==0];idx=[(a,d-a) for d in range(m+1) for a in range(d+1)];V=np.array([[np.cos(a*np.pi*j/m)*np.cos(b*np.pi*k/(m+1)) for a,b in idx] for j,k in nodes]);rhs=np.array([moments(a)*moments(b) for a,b in idx]);w=np.linalg.solve(V.T,rhs);err=float(max(abs(w[i]-op.w[j,k]) for i,(j,k) in enumerate(nodes)));return dict(moment_weight_max_absolute_difference=err,moment_weights_sum=float(w.sum()),pass_1e12=bool(err<=1e-12 and abs(w.sum()-4)<=1e-12))
def solve(m,sign,proposal,pilot=False,seed=None):
 cfg=proposal['solver'][sign];start=time.monotonic();cpu=time.process_time();row=dict(m=m,n=m-1,extreme=sign,started_utc=utc(),status='RUNNING',seed=proposal['solver']['seed'] if seed is None else seed,ncv=cfg['ncv'],tol=cfg['tol'],matvec_cap=cfg['maximum_matvecs'],wall_cap_seconds=1800 if pilot else 21600);op=None
 try:
  op=mod.PaduaOperator(m,m-1);row['dimension']=op.shape[0];row['weight_sum']=float(op.w.sum());row['negative_weight_count']=int(np.count_nonzero(op.w<0));row['negative_weight_mass']=float(-op.w[op.w<0].sum());assert abs(row['weight_sum']-4)<=1e-11
  def guarded(v):
   if op.calls>=cfg['maximum_matvecs']:raise BudgetLimit('matvec cap')
   if time.monotonic()-start>=row['wall_cap_seconds']:raise BudgetLimit('wall cap')
   if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>6*1024**2:raise BudgetLimit('6GiB process RSS safety cap')
   out=op@v
   if time.monotonic()-start>=row['wall_cap_seconds']:raise BudgetLimit('wall cap after matvec')
   return out
  wrapped=LinearOperator(op.shape,matvec=guarded,dtype=np.dtype(float));rng=np.random.default_rng(row['seed']);vals,vecs=eigsh(wrapped,k=1,which=cfg['which'],v0=rng.standard_normal(op.shape[0]),ncv=min(cfg['ncv'],op.shape[0]),tol=cfg['tol'],maxiter=proposal['solver']['maxiter']);v=vecs[:,0];v/=np.linalg.norm(v);av=guarded(v);value=float(v@av);res=float(np.linalg.norm(av-value*v));passed=bool(np.isfinite(value) and np.isfinite(res) and res<=1e-8*max(1,abs(value)));row.update(value=value,residual_2_float=res,residual_guard_pass=passed,status='COMPLETED' if passed else 'FAILED_RESIDUAL')
 except Exception as e:row.update(status='FAILED',error_type=type(e).__name__,error=str(e))
 row.update(matvecs=0 if op is None else op.calls,seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss);return row

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['validate','minimum','maximum-pilot','maximum'],required=True);ap.add_argument('--m',type=int,nargs='*');ap.add_argument('--output',type=Path,required=True);ap.add_argument('--seed',type=int);a=ap.parse_args();proposal=json.loads(PROPOSAL.read_text());r=dict(status='MEASURED',preregistration_commit='ec52c16569ea959dfe682fcd7985378a2ef1cd42',command=sys.argv,started_utc=utc(),script_sha256=sha(__file__),operator_sha256=sha(SOURCE),frozen_code_sha256=sha(mod.FROZEN),proposal_sha256=sha(PROPOSAL),python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),threads={k:os.getenv(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},results=[])
 def save():a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
 save()
 if a.mode=='validate':
  for m in [10,11,20,21]:
   op=mod.PaduaOperator(m,m-1);_,weights,idx=mod.frozen.operator(m,'padua');B=np.column_stack([np.outer(op.lx[:,i],op.ly[:,j]).ravel() for i,j in idx]);G=B.T@(weights.ravel()[:,None]*B);ev=np.linalg.eigvalsh(G);row=dict(m=m,dense_extrema=[float(ev[0]),float(ev[-1])],weight_sum=float(op.w.sum()),weight_max_difference=float(np.max(abs(op.w-weights))),signed_weight_count=int(np.count_nonzero(op.w<0)),solves=[solve(m,s,proposal,seed=a.seed) for s in ['minimum','maximum']]);row['max_relative_extrema_difference']=max(abs(x['value']/ref-1) for x,ref in zip(row['solves'],[ev[0],ev[-1]]));row['weights_moment_check']=weights_check(m,op) if m in [10,11] else None;row['pass']=bool(row['max_relative_extrema_difference']<=1e-10 and abs(row['weight_sum']-4)<=1e-12 and (row['weights_moment_check'] is None or row['weights_moment_check']['pass_1e12']));r['results'].append(row);save();print('validation',m,row['pass'],flush=True)
   if not row['pass']:raise RuntimeError('Finite validation failed; no scan acceptance.')
 else:
  sign='minimum' if a.mode=='minimum' else 'maximum';degrees=[800] if a.mode=='maximum-pilot' else a.m;assert degrees
  for m in degrees:
   r['running_degree']=m;save();row=solve(m,sign,proposal,pilot=a.mode=='maximum-pilot',seed=a.seed);r['results'].append(row);r.pop('running_degree',None);save();print('completed',m,sign,row,flush=True)
   if row['status']!='COMPLETED':r['completed']=False;save();return
 r['completed']=True;save()
if __name__=='__main__':main()
