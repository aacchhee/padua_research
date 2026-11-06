import sys; sys.path.insert(0,'.')
from residual import lam
import numpy as np
# Q-dependence check
for Q in [400,800,1600,2400]:
    print("Qcheck",Q,lam(80,80,0.005,Q),lam(40,40,0.005,Q),lam(160,80,0.005,Q) if Q>=800 else None,flush=True)
# best certified-style bound for given Qcert, using float estimate of lambda(B_Q) at Q=1200
for Qcert in [2e4,1e5,1e6,1e7]:
    best=None
    for alpha in [0.005,0.006,0.008,0.01,0.015,0.02,0.03]:
        for T in [5,10,15,20,30,40]:
            for Y in [3,4,5,6,8,10,12,15,20,25,30]:
                A=1+Y**3/6+alpha*T**3/3
                if A/Qcert>0.05: continue
                l=lam(T,Y,alpha,1200)
                ub=1+alpha+max(0,l)+A/Qcert
                if best is None or ub<best[0]: best=(ub,alpha,T,Y,l,A)
    print("Qcert",Qcert,"best UB",best,flush=True)
