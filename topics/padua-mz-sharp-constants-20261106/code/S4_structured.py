#!/usr/bin/env python3
"""CC pencil via nodal Q-orthonormal coordinates, FFT T+H, MEASURED only.
No dense allocations except optional finite --validate mode.
"""
import argparse, hashlib, json, os, platform, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.fft import dct
from scipy.linalg import matmul_toeplitz
from scipy.sparse.linalg import LinearOperator, eigsh
ROOT=Path(__file__).resolve().parents[3]

def moments(k):
 k=np.asarray(k);out=np.zeros(k.shape);even=k%2==0;out[even]=2/(1-k[even].astype(float)**2);return out

class ContinuousOverCC(LinearOperator):
 def __init__(self,N):
  self.N=N;self.d=np.ones(N+1);self.d[[0,-1]]=.5
  self.w=self.transform(moments(np.arange(N+1)));assert np.all(self.w>0)
  self.sw=np.sqrt(self.w);h=self.d*(-1.)**np.arange(N+1)/self.sw
  self.h=h/np.linalg.norm(h);self.mu=moments(np.arange(2*N+1));self.calls=0
  super().__init__(dtype=np.dtype(float),shape=(N+1,N+1))
 def transform(self,y):return self.d*dct(y,type=1)/self.N
 def project(self,z):return z-self.h*(self.h@z)
 def _matvec(self,z):
  self.calls+=1;z=np.asarray(z).ravel();c=self.transform(self.project(z)/self.sw)
  # Integral Gram T_ij=(mu_|i-j|+mu_i+j)/2.
  t=matmul_toeplitz(self.mu[:self.N+1],c,check_finite=False)
  h=matmul_toeplitz((self.mu[self.N:],self.mu[self.N::-1]),c[::-1],check_finite=False)
  b=self.transform((t+h)/2)/self.sw
  return self.project(b)+self.h*(self.h@z)

def solve(N,tol=2e-12):
 tick=time.monotonic();op=ContinuousOverCC(N);rng=np.random.default_rng(20261106);out={}
 for name,which in [('minimum','LA'),('maximum','SA')]:
  before=op.calls;vals,vecs=eigsh(op,k=1,which=which,v0=rng.standard_normal(N+1),tol=tol,ncv=40,maxiter=3000);v=vecs[:,0];av=op@v;mu=float(v@av)
  out[name]=dict(eigenvalue=1/mu,inverse_eigenvalue=mu,inverse_residual_2_float=float(np.linalg.norm(av-mu*v)),constraint_residual_float=float(abs(op.h@v)),matvecs=op.calls-before)
 return dict(N=N,n=N-1,seconds=time.monotonic()-tick,results=out)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--validate',type=int,nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 import importlib.util
 p=ROOT/'topics/mz-constants/sources/padua_mz_inputs/code/cc_mz_large.py';spec=importlib.util.spec_from_file_location('cc_pinned',p);cc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cc)
 report=dict(status='MEASURED',command=sys.argv,seed=20261106,tol=2e-12,ncv=40,maxiter=3000,python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),reference_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),threads={k:os.getenv(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},results=[])
 for N in args.validate:
  assert N<=1280,'Finite dense validation only; large scan requires separate preregistration.'
  row=solve(N);ref=[cc.extremes(N,N-1,p) for p in [0,1]];targets=[min(x[0] for x in ref),max(x[1] for x in ref)];row['dense_reference']=targets;row['maximum_relative_error']=max(abs(row['results'][k]['eigenvalue']/v-1) for k,v in zip(['minimum','maximum'],targets));row['pass_1e10']=bool(row['maximum_relative_error']<=1e-10)
  op=ContinuousOverCC(N);rng=np.random.default_rng(711);u=rng.standard_normal(N+1);v=rng.standard_normal(N+1);row['symmetry_relative_error']=float(abs(u@(op@v)-v@(op@u))/max(np.linalg.norm(u)*np.linalg.norm(v),1))
  report['results'].append(row);args.output.write_text(json.dumps(report,indent=2)+'\n');print(row,flush=True)
if __name__=='__main__':main()
