# Unrecorded floating screen (Claude): phase-shifted cyclic orbits M=N, nodes cos(2pi(k z/N + phi)), k<N.
import numpy as np, itertools
from math import comb
rng=np.random.default_rng(20261106)
def cheb(n,X):
    idx=[(a,b,c) for a in range(n+1) for b in range(n+1) for c in range(n+1) if a+b+c<=n]
    T=lambda k,x: np.cos(k*np.arccos(np.clip(x,-1,1)))
    return np.array([[T(a,x[0])*T(b,x[1])*T(c,x[2]) for a,b,c in idx] for x in X])
for n in [2,3,4,5,6]:
    N=comb(n+3,3); best=None; full=0; trials=0
    for _ in range(300):
        z=np.array([1,*rng.integers(2,N,2)]); phi=rng.random(3)
        X=np.cos(2*np.pi*(np.outer(np.arange(N),z)/N+phi))
        s=np.linalg.svd(cheb(n,X),compute_uv=False); trials+=1
        r=s[-1]/s[0]
        if r>1e-10: full+=1
        best=r if best is None else max(best,r)
    print(n,N,"numerically full-rank fraction",full/trials,"best sigma_min/sigma_max",f"{best:.3g}")
