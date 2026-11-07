#!/usr/bin/env python3
"""Bounded non-Haar positive-weight escape search; binary64 discovery only."""
import argparse,itertools as it,json,time,sys,hashlib,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
sys.path.insert(0,str(Path(__file__).resolve().parent));import t9_maxima as old

def main():
 a=argparse.ArgumentParser();a.add_argument('--output',type=Path,required=True);a=a.parse_args();t=time.monotonic();rows=[];tested=0
 for q in (6,8,10,12,16,20,24):
  for b in range(1,q//2+1):
   for c in range(b,q//2+1):
    g=np.array([1,b,c]);ex=old.exponents(3)
    short=min(sum(abs(np.array(k))) for k in it.product(range(-3,4),repeat=3) if any(k) and sum(abs(np.array(k)))<=3 and sum(np.array(k)*g)%q==0) if any(any(k) and sum(abs(np.array(k)))<=3 and sum(np.array(k)*g)%q==0 for k in it.product(range(-3,4),repeat=3)) else 4
    if short>=4:continue
    p=np.unique(np.round(np.cos(2*np.pi*np.arange(q)[:,None]*g/q),13),axis=0);v=old.old.basis(p,3).T;rhs=np.zeros(len(ex));rhs[0]=1
    # Maximize common strictly positive mass floor; no rounding accepted as proof.
    A=np.hstack([-np.eye(len(p)),np.ones((len(p),1))]);ob=np.r_[np.zeros(len(p)),-1.]
    r=linprog(ob,A_ub=A,b_ub=np.zeros(len(p)),A_eq=np.hstack([v,np.zeros((len(ex),1))]),b_eq=rhs,bounds=[(0,None)]*(len(p)+1),method='highs');tested+=1
    if r.success and r.x[-1]>1e-7:
     rows.append({'q':q,'g':g.tolist(),'short':short,'nodes':p.tolist(),'weights':r.x[:-1].tolist(),'floor':r.x[-1]});print(rows[-1],flush=True)
 digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 a.output.write_text(json.dumps({'status':'MEASURED discovery only','scope':'cyclic q6,8,10,12,16,20,24, g=(1,b,c), b<=c<=q/2; degree3; positive floor>1e-7','tested':tested,'escapes':rows,'seconds':time.monotonic()-t,'command':sys.argv,'seed':0,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'code_sha256':digest(__file__),'input_sha256':{str(p):digest(p) for p in [old.__file__,old.old.__file__]}},separators=(',',':'))+'\n')
if __name__=='__main__':main()
