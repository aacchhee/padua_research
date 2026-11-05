"""Executed evaluator cross-check and precision diagnostic; not a certificate."""
import json,sys
from pathlib import Path
import numpy as np
from evaluator import Evaluator
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'padua-argmax-alln-20261101'/'code'))
from maj import setup,lam
rng=np.random.default_rng(20261103);rows=[]
for n in [3,4,17,48,96]:
    e=Evaluator(n);pts=list(rng.uniform(0,np.pi,(4,2)))+[(0,0),(np.pi,np.pi),(np.pi,0.)]
    err=max(max(abs(x-y) for x,y in zip(e.point(t,p),[a[0] for a in lam(n,[t],[p],setup(n))])) for t,p in pts)
    rows.append({'n':n,'points':len(pts),'max_abs_difference_dense':err})
stability=[]
for n in [192,200,999,1000]:
    vals=[]
    for dtype in [np.float64,np.longdouble]:
        e=Evaluator(n,dtype);rho=dtype(1)/64;J,K=e.corner()[0];t,p=J*e.pi/n,K*e.pi/(n+1);lc=e.point(t,p)[0]
        l=e.point(t,p+(1 if K==0 else -1)*rho/(n+1))[0]
        kk=(l-(1+float(np.cos(rho)))*lc/2)/(float(rho)**2*np.log(n+1));vals.append(kk)
    stability.append({'n':n,'K_float64':vals[0],'K_longdouble':vals[1],'difference':vals[0]-vals[1]})
print(json.dumps({'dense_agreement':rows,'longdouble_axis':stability,'longdouble_bits':np.finfo(np.longdouble).nmant+1},indent=2))
