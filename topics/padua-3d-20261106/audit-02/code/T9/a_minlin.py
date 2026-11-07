# Minimal Lebesgue constant of degree-1 interpolation in [-1,1]^d (d=2,3): Lebesgue fn convex => max at vertices.
import numpy as np, itertools as it
from scipy.optimize import minimize
rng=np.random.default_rng(7)
def lam(p,d):
    X=np.clip(p.reshape(d+1,d),-1,1); V=np.hstack([np.ones((d+1,1)),X])
    if abs(np.linalg.det(V))<1e-12: return 1e6
    W=np.array(list(it.product([-1,1],repeat=d))); E=np.hstack([np.ones((len(W),1)),W])
    L=np.linalg.solve(V.T,E.T)  # cardinal values at vertices
    return np.abs(L).sum(0).max()
for d in (2,3):
    best=np.inf;bp=None
    for s in range(400):
        p0=rng.uniform(-1,1,(d+1)*d)
        r=minimize(lam,p0,args=(d,),method='Nelder-Mead',options={'maxiter':20000,'xatol':1e-10,'fatol':1e-12})
        r=minimize(lam,r.x,args=(d,),method='Nelder-Mead',options={'maxiter':20000,'xatol':1e-12,'fatol':1e-14})
        if r.fun<best:best=r.fun;bp=np.clip(r.x.reshape(d+1,d),-1,1)
    print('d',d,'min Lambda(n=1) found',best); print(np.round(bp,6))
print('Nevskii-type reference: d2 1+2/sqrt5 =',1+2/np.sqrt(5),' d3: 2')
