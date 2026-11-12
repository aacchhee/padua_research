# MEASURED: Lebesgue constants (mesh lower estimates) of the 3D total-degree R-Leja lower set vs the transferred bound.
import numpy as np, math, itertools, json, sys
from math import comb
def rleja35(K):
    r=[1.0,-1.0,0.0]; j=2
    while len(r)<K:
        a=math.sqrt((r[j]+1)/2); r+=[a,-a]; j+=1
    return np.array(r[:K])
D=json.load(open(sys.argv[1]))["D"]
def cheb(m,x): return np.cos(m*np.arccos(np.clip(x,-1,1)))
def basis(P,n):
    idx=[(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
    cache=[[cheb(m,P[:,d]) for m in range(n+1)] for d in range(3)]
    return np.stack([cache[0][a]*cache[1][b]*cache[2][c] for a,b,c in idx],axis=1)
out=[]
g1=np.unique(np.concatenate([np.cos(np.linspace(0,np.pi,33)),np.linspace(-1,1,33)]))
for n in range(1,10):
    r=rleja35(n+1)
    X=np.array([(r[a],r[b],r[c]) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)])
    N=len(X); assert N==comb(n+3,3)
    V=basis(X,n); cond=np.linalg.cond(V)
    Vinv=np.linalg.inv(V)
    best=0.0; bestpt=None
    g=np.unique(np.concatenate([g1,r]))
    for i0 in range(0,len(g)):
        P=np.array(list(itertools.product([g[i0]],g,g)))
        lam=np.sum(np.abs(basis(P,n)@Vinv),axis=1); k=np.argmax(lam)
        if lam[k]>best: best=lam[k]; bestpt=P[k]
    # local refinement around best point
    from scipy.optimize import minimize
    f=lambda p: -np.sum(np.abs(basis(np.clip(p,-1,1)[None,:],n)@Vinv))
    res=minimize(f,bestpt,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':4000})
    lam_ref=max(best,-res.fun if np.all(np.abs(res.x)<=1+1e-12) else best)
    bound=sum(comb(3,j)*comb(n-j+9,9) for j in range(min(3,n)+1))
    sumDD=sum(D[a]*D[b]*D[c] for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b))
    explicit=sum((a+1)**2*(b+1)**2*(c+1)**2 for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b))
    out.append(dict(n=n,N=N,cond=float(cond),Lambda_mesh=float(best),Lambda_refined=float(lam_ref),sum_DaDbDc_mesh=float(sumDD),sum_explicit=explicit,closed_form=bound,eight_binom=8*comb(n+9,9)))
    print(out[-1],flush=True)
assert all(o["sum_explicit"]==o["closed_form"] for o in out)
print("closed form equals explicit sum n=1..9; Lambda below bound:",all(o["Lambda_refined"]<=o["closed_form"] for o in out))
json.dump(out,open(sys.argv[2],"w"),indent=1)
