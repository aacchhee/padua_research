# Unstructured 3-D Padua-type search: N=binom(n+3,3) nodes, weights s^2>0, exact for
# product first-kind Chebyshev probability measure on Pi_{2n-1}; optional soft push of the
# degree-2n moments (weight beta) to make the top-degree Gram close to I. Then Pi_n
# unisolvence (cond V) and sampled Lebesgue constant. Plain numpy LM. MEASURED only.
import numpy as np, sys, itertools
from math import comb
def idx(m): return np.array([(i,j,k) for i in range(m+1) for j in range(m+1-i) for k in range(m+1-i-j)])
def evalT(A,th): return np.prod(np.cos(th[:,None,:]*A[None,:,:]),axis=2)
def resid_jac(z,A,N,wt):
    th=z[:3*N].reshape(N,3); s=z[3*N:]; w=s*s
    C=np.cos(th[:,None,:]*A[None,:,:]); S=np.sin(th[:,None,:]*A[None,:,:])
    T=np.prod(C,axis=2)
    tgt=np.zeros(len(A)); tgt[0]=1.0
    r=(T.T@w-tgt)*wt
    J=np.zeros((len(A),4*N))
    for d in range(3):
        others=np.prod(np.delete(C,d,axis=2),axis=2)
        dT=-A[None,:,d]*S[:,:,d]*others
        J[:,d:3*N:3]=(dT*w[:,None]).T
    J[:,3*N:]=(T*(2*s)[:,None]).T
    return r,J*wt[:,None]
def lm(z,A,N,wt,it=4000,mu=1e-2):
    r,J=resid_jac(z,A,N,wt); f=r@r
    for k in range(it):
        H=J.T@J; g=J.T@r
        try: dz=-np.linalg.solve(H+mu*np.diag(np.diag(H)+1e-12),g)
        except np.linalg.LinAlgError: mu*=10; continue
        z2=z+dz; r2,J2=resid_jac(z2,A,N,wt); f2=r2@r2
        if f2<f:
            rel=(f-f2)/max(f,1e-300); z,r,J,f=z2,r2,J2,f2; mu=max(mu/3,1e-12)
            if rel<1e-13 and k>200: break
        else: mu*=4
        if f<1e-28 or mu>1e12: break
    return z,f
def lebesgue(X,n,mesh):
    A=idx(n); V=evalT(A,np.arccos(np.clip(X,-1,1)))
    L=np.linalg.solve(V.T,evalT(A,np.arccos(mesh)).T)
    return np.abs(L).sum(axis=0).max(),np.linalg.cond(V)
n=int(sys.argv[1]); starts=int(sys.argv[2]); beta=float(sys.argv[3]); seed=int(sys.argv[4])
N=comb(n+3,3); A=idx(2*n); deg=A.sum(1); rng=np.random.default_rng(seed)
lo=deg<=2*n-1
wt=np.where(lo,1.0,beta)
g=np.cos(np.pi*np.arange(0,31)/30); mesh=np.vstack([np.array(list(itertools.product(g,g,g))),np.cos(np.pi*rng.random((20000,3)))])
res=[]
for s in range(starts):
    z0=np.concatenate([np.pi*rng.random(3*N),np.full(N,1/np.sqrt(N))*(1+0.1*rng.standard_normal(N))])
    z,f=lm(z0,A[lo],N,np.ones(lo.sum()))           # stage 1: exact Pi_{2n-1}
    if beta>0:
        z,_=lm(z,A,N,np.where(lo,1e4,beta))          # stage 2: push degree-2n
        z,f=lm(z,A[lo],N,np.ones(lo.sum()),it=500)  # stage 3: re-polish exactness
    th=z[:3*N].reshape(N,3); w=z[3*N:]**2; X=np.cos(th)
    T2=evalT(A,th); top=(T2.T@w)[~lo];
    if f<1e-24:
        lam,cond=lebesgue(X,n,mesh); res.append(lam)
        print(f"n{n} s{s}: exact2n-1 res {f:.1e} minw*N {w.min()*N:.2e} |deg2n defect| {np.abs(top).max():.2e} condV {cond:.1e} Lam~{lam:.2f}",flush=True)
    else: print(f"n{n} s{s}: fail res {f:.1e}",flush=True)
if res: print("n",n,"beta",beta,"min Lambda",min(res),"median",float(np.median(res)),"successes",len(res),"/",starts)
