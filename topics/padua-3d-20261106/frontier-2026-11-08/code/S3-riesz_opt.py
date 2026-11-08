import numpy as np, itertools, sys, time, scipy.linalg as sla
from scipy.optimize import minimize
rng=np.random.default_rng(1)
def idx(n): return [k for k in itertools.product(range(n+1),repeat=3) if sum(k)<=n]
def basis_th(th,K):
    Kc=np.array(K)                          # Nb x 3
    c=np.cos(th[:,None,:]*Kc[None,:,:])     # M x Nb x 3
    s=np.where(Kc[None,:,:]>0,np.sqrt(2),1.0)
    return np.prod(c*s,axis=2)
def grid(m):
    t=np.cos(np.pi*np.arange(m)/(m-1)); return np.array(list(itertools.product(t,t,t)))
def stats(X,K,E):
    th=np.arccos(np.clip(X,-1,1)); V=basis_th(th,K)
    Kjj=(V**2).sum(1); B=V/np.sqrt(Kjj)[:,None]; ev=np.linalg.eigvalsh(B@B.T)
    P=basis_th(np.arccos(E),K); L=np.linalg.solve(V.T,P.T)
    return np.abs(L).sum(0).max(), ev[0], ev[-1]
def softmin_obj(z,K,N,t):
    th=z.reshape(N,3); V=basis_th(th,K); Kjj=(V**2).sum(1); B=V/np.sqrt(Kjj)[:,None]
    ev=np.linalg.eigvalsh(B@B.T)
    return (1/t)*np.log(np.exp(-t*(ev-ev[0])).sum())-ev[0]   # = -softmin
E=np.vstack([grid(31),rng.uniform(-1,1,(20000,3)),np.cos(np.pi*rng.uniform(0,1,(20000,3)))])
for n in [int(a) for a in sys.argv[1:]]:
    K=idx(n); N=len(K); C=grid(2*n+3); A=basis_th(np.arccos(np.clip(C,-1,1)),K)
    # Christoffel-weighted AFP (normalized rows)
    An=A/np.linalg.norm(A,axis=1)[:,None]
    _,_,piv=sla.qr(An.T,mode='economic',pivoting=True); X0=C[piv[:N]]
    lam,a,b=stats(X0,K,E); print(f"n={n} N={N} CFP: Lam={lam:.2f} riesz=[{a:.3g},{b:.3g}]",flush=True)
    z0=np.arccos(np.clip(X0,-1,1)).ravel()+1e-3*rng.standard_normal(3*N)
    t0=time.time(); best=z0
    for t in [20,60,200]:
        r=minimize(softmin_obj,best,args=(K,N,t),method='L-BFGS-B',options={'maxiter':150,'maxfun':200000})
        best=r.x
    X=np.cos(best.reshape(N,3)); lam,a,b=stats(X,K,E)
    print(f"n={n} N={N} maxLmin: Lam={lam:.2f} Lam/sqrtN={lam/np.sqrt(N):.2f} riesz=[{a:.3g},{b:.3g}] time={time.time()-t0:.0f}s",flush=True)
