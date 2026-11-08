import numpy as np, itertools, sys, scipy.linalg as sla
rng=np.random.default_rng(0)
def idx(n): return [k for k in itertools.product(range(n+1),repeat=3) if sum(k)<=n]
def basis(X,n,K):
    # orthonormal product Chebyshev (prob. measure): T_0=1, sqrt2 T_k
    th=np.arccos(np.clip(X,-1,1))
    cols=[]
    for k in K:
        c=np.ones(len(X))
        for i in range(3):
            if k[i]>0: c=c*np.sqrt(2)*np.cos(k[i]*th[:,i])
        cols.append(c)
    return np.array(cols).T
def grid(m):
    t=np.cos(np.pi*np.arange(m)/(m-1))
    return np.array(list(itertools.product(t,t,t)))
for n in [int(a) for a in sys.argv[1:]]:
    K=idx(n); N=len(K)
    C=grid(2*n+3)                     # tensor Lobatto candidates
    A=basis(C,n,K)
    _,_,piv=sla.qr(A.T,mode='economic',pivoting=True)
    S=C[piv[:N]]
    V=basis(S,n,K)
    Kjj=(V**2).sum(1)
    Gh=(V/np.sqrt(Kjj)[:,None])@(V/np.sqrt(Kjj)[:,None]).T
    ev=np.linalg.eigvalsh(Gh)
    E=np.vstack([grid(31),rng.uniform(-1,1,(20000,3)),np.cos(np.pi*rng.uniform(0,1,(20000,3)))])
    P=basis(E,n,K)
    L=np.linalg.solve(V.T,P.T)          # N x |E| Lagrange values
    Lam=np.abs(L).sum(0).max()
    Kx=(P**2).sum(1)
    fej=((Kjj[:,None]*L**2).sum(0)/Kx).max()
    sq=(L**2).sum(0).max()
    B=np.sqrt(Kx.max()*(1/Kjj).sum()/ev[0])
    print(f"n={n} N={N} AFP: Lam~{Lam:.2f} Lam/sqrtN={Lam/np.sqrt(N):.2f} Lam/N={Lam/N:.3f} riesz[min,max]=[{ev[0]:.3g},{ev[-1]:.3g}] fejer={fej:.2f} maxSumL2={sq:.2f} rieszBound={B:.1f}",flush=True)
