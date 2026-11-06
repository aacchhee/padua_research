#!/usr/bin/env python3
"""Pinned K0 replay only: no fitting or extrapolation. All outputs MEASURED."""
import argparse, datetime, hashlib, importlib.util, json, os, platform, resource, sys, time
from pathlib import Path
import numpy as np
import scipy
import mpmath as mp
from scipy.special import roots_legendre
from scipy.sparse.linalg import eigsh
ROOT=Path(__file__).resolve().parents[3]
PIN='2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861'
SOURCES=['topics/mz-constants/sources/padua_mz_inputs/code/cc_mz_large.py',
 'tracks/mz-constants/code/mz2d_spectra.py',
 'topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py',
 'topics/padua-mz-2d-frontier-20261105/evidence/g1-minimum-only.json',
 'tracks/mz-constants/theory/reproduced-spectra.md',
 'topics/padua-mz-cleanup-20261105/theory/growth-carrier-bounds.md']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def blob(p):
 b=Path(p).read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def module(path,name):
 spec=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def finite_mass(r,h=0):
 """Exact integer Fourier convolution then 75-digit rational moment summation.
 Fejer F_r=sum_{j=-r}^r (r+1-|j|) exp(ij theta)/(r+1).
 For h>0 integrate F_r^2 cos(h theta)^2; h=0 integrates F_r^2.
 """
 L=r+1;t=L-np.abs(np.arange(-r,r+1,dtype=np.int64));b=np.convolve(t,t)
 assert int(b.max())<2**63
 def moment(k):return mp.mpf(0) if k%2 else mp.mpf(2)/(1-k*k)
 terms=[]
 for k,v in zip(range(-2*r,2*r+1),b):
  z=moment(k) if h==0 else moment(k)/2+(moment(k+2*h)+moment(k-2*h))/4
  terms.append(int(v)*z)
 return mp.fsum(terms)/(L*L)

def quad_mass(r,h=0):
 # Composite 24-point Gauss integration in angle avoids global x-quadrature
 # endpoint root/weight errors; each panel resolves at most four oscillations.
 degree=r+h;panels=degree+1;nodes,w=roots_legendre(24)
 theta=(np.arange(panels)[:,None]+(nodes+1)/2)*np.pi/panels
 f=(np.sin((r+1)*theta/2)/np.sin(theta/2))**2/(r+1)
 terms=f*f*np.cos(h*theta)**2*np.sin(theta)*w[None,:]*np.pi/(2*panels)
 return float(np.sum(terms,dtype=np.longdouble))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--suite',choices=['cc','padua','carrier'],required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 tick=time.monotonic();r={'status':'MEASURED','pin':PIN,'command':sys.argv,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'model':'gpt-6.1-sol medium','python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__,'platform':platform.platform(),'threads':{k:os.getenv(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},'script_sha256':sha(__file__),'input_hashes':{p:{'sha256':sha(ROOT/p),'git_blob':blob(ROOT/p)} for p in SOURCES},'results':[]}
 def save():
  r['seconds']=time.monotonic()-tick;r['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
 if args.suite=='cc':
  cc=module(SOURCES[0],'cc_replay');expected=[(40,.259849024875495,1.004471120722071),(80,.216153284009021,1.004439734729248),(160,.182490276565946,1.004439101388067),(320,.156015183642123,1.004437800957723),(640,.134833488162936,1.004437221578550),(1280,.117635155992213,1.004437035065849)]
  for N,lo0,hi0 in expected:
   t=time.monotonic();p=[cc.extremes(N,N-1,z) for z in [0,1]];lo=min(x[0] for x in p);hi=max(x[1] for x in p);err=max(abs(lo/lo0-1),abs(hi/hi0-1));row=dict(N=N,n=N-1,minimum=float(lo),maximum=float(hi),parity=np.asarray(p).tolist(),reference=[lo0,hi0],maximum_relative_error=float(err),pass_1e10=bool(err<=1e-10),seconds=time.monotonic()-t);r['results'].append(row);save();print(row,flush=True)
 elif args.suite=='padua':
  mod=module(SOURCES[2],'padua_replay');ref=json.loads((ROOT/SOURCES[3]).read_text());r.update(seed=20261105,tolerance=2e-11,ncv=40,maxiter=20000)
  for m in [800,1000]:
   t=time.monotonic();op=mod.PaduaOperator(m,m-1);rng=np.random.default_rng(r['seed']);values,vectors=eigsh(op,k=1,which='SA',v0=rng.standard_normal(op.shape[0]),ncv=40,tol=2e-11,maxiter=20000);v=vectors[:,0];v/=np.linalg.norm(v);av=op@v;val=float(v@av);old=next(x for x in ref['results'] if x['m']==m)['minimum'];err=abs(val/old-1);row=dict(m=m,n=m-1,dimension=op.shape[0],minimum=val,reference=old,relative_error=err,pass_1e10=bool(err<=1e-10),residual_2_float=float(np.linalg.norm(av-val*v)),matvecs=op.calls,seconds=time.monotonic()-t);r['results'].append(row);save();print(row,flush=True)
 else:
  mp.mp.dps=75
  def xlog(x):return 0 if x==0 else x*x*mp.log(abs(x))
  def C(q):return 3*xlog(q)-2*xlog(q+1)-2*xlog(q-1)+(xlog(q+2)+xlog(q-2))/2
  A=4*mp.log(2);J=(A+C(mp.mpf(4)))/2;limit=A*J;r.update(carrier='even minus, a=1/4 b=1/5, strict a+b<1/2',limit=mp.nstr(limit,60),A=mp.nstr(A,60),J_minus=mp.nstr(J,60),comparison_policy='1e-10 finite norm formula vs independent Gauss quadrature; finite-to-limit discrepancies separately recorded, no fit or extrapolation')
  for m in [512,1024,2048,4096]:
   t=time.monotonic();rr=m//4;s=m//5;exact=finite_mass(rr,m//2)*finite_mass(s);q=quad_mass(rr,m//2)*quad_mass(s);err=abs(mp.mpf(q)/exact-1);row=dict(m=m,r=rr,s=s,degree=m//2+rr+s,finite_norm_squared_75digit=mp.nstr(exact,60),gauss_norm_squared=q,quadrature_relative_error=float(err),pass_1e10=bool(err<=mp.mpf('1e-10')),relative_difference_from_limit=float(exact/limit-1),seconds=time.monotonic()-t);r['results'].append(row);save();print(row,flush=True)
 save()
if __name__=='__main__':main()
