#!/usr/bin/env python3
"""Preregistered degree-five unbalanced dual-relation LP discovery screen."""
import argparse,hashlib,itertools as it,json,platform,sys,time
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
sys.path.insert(0,str(Path(__file__).resolve().parent));import t9_maxima as old
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();start=time.process_time();tested=skipped=0;escapes=[];unrun=[]
 shell=np.array([k for k in it.product(range(-5,6),repeat=3) if 0<sum(map(abs,k))<=5],dtype=int);norm=np.abs(shell).sum(axis=1);support=(shell!=0).sum(axis=1);balanced=2*np.abs(shell).max(axis=1)<=norm
 cases=[(q,b) for q in range(20,81,4) for b in range(1,q//2-2)]
 for pos,(q,b) in enumerate(cases):
  if tested>=512 or time.process_time()-start>60:unrun=cases[pos:];break
  g=np.array([1,b,b+3]);relations=(shell@g)%q==0
  if np.any(relations&((support<3)|balanced)):skipped+=1;continue
  points=np.unique(np.round(np.cos(2*np.pi*np.arange(q)[:,None]*g/q),13),axis=0);v=old.old.basis(points,5).T;rhs=np.zeros(v.shape[0]);rhs[0]=1
  ob=np.r_[np.zeros(len(points)),-1.];A=np.hstack([-np.eye(len(points)),np.ones((len(points),1))])
  r=linprog(ob,A_ub=A,b_ub=np.zeros(len(points)),A_eq=np.hstack([v,np.zeros((len(rhs),1))]),b_eq=rhs,bounds=[(0,None)]*(len(points)+1),method='highs');tested+=1
  if r.success and r.x[-1]>1e-7:escapes.append({'q':q,'g':g.tolist(),'floor':float(r.x[-1]),'points':points.tolist(),'weights':r.x[:-1].tolist()})
 digest=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
 out={'status':'MEASURED discovery only; no global obstruction','command':sys.argv,'code_sha256':digest(__file__),'inputs':{str(f):digest(f) for f in [old.__file__,old.old.__file__]},'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'seed':0,'scope':'degree5 q20..80 step4, g=(1,b,b+3),1<=b<=q/2-3; remove support1/2 and balanced3 short relations <=5','tested':tested,'analytically_excluded':skipped,'escapes':escapes,'unrun':unrun,'cpu_seconds':time.process_time()-start}
 a.output.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('inputs','versions','escapes')}))
if __name__=='__main__':main()
