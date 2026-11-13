# Search for small Lebesgue constants of 10-point Pi_2 interpolation in [-1,1]^3 (n=2). Lower samples of sup; only consistency check.
import numpy as np, itertools as it, sys
from scipy.optimize import minimize
E=[a for a in it.product(range(3),repeat=3) if sum(a)<=2]
def basis(P):
    P=np.atleast_2d(P); T=np.stack([np.ones_like(P),P,2*P**2-1],-1)  # Chebyshev T0,T1,T2
    return np.stack([T[:,0,a]*T[:,1,b]*T[:,2,c] for a,b,c in E],1)
g=np.cos(np.linspace(0,np.pi,11)); M=np.array(list(it.product(g,repeat=3))); BM=basis(M)
def lam(p,BM=BM):
    X=np.clip(p.reshape(10,3),-1,1); V=basis(X)
    if np.linalg.cond(V)>1e8: return 1e3
    return np.abs(np.linalg.solve(V.T,BM.T)).sum(0).max()
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
starts=[np.load(sys.argv[2]).ravel()] if len(sys.argv)>2 else []
starts+= [rng.uniform(-1,1,30) for _ in range(40)]
best=(np.inf,None)
for p0 in starts:
    r=minimize(lam,p0,method='Nelder-Mead',options={'maxiter':12000,'maxfev':12000,'xatol':1e-8,'fatol':1e-10,'adaptive':True})
    if r.fun<best[0]: best=(r.fun,np.clip(r.x.reshape(10,3),-1,1))
print('best mesh-11 value',best[0])
# re-evaluate best on finer mesh + local maximization of the Lebesgue function
X=best[1]; Vi=np.linalg.inv(basis(X))
g2=np.cos(np.linspace(0,np.pi,41)); M2=np.array(list(it.product(g2,repeat=3)))
L2=np.abs(basis(M2)@Vi).sum(1); i=np.argsort(L2)[-8:]
f=lambda x: -np.abs(basis(np.clip(x,-1,1))@Vi).sum()
loc=max(-minimize(f,M2[j],method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-14}).fun for j in i)
print('best set: mesh41',L2.max(),'local',max(loc,L2.max()))
print(np.round(X,5).tolist())
