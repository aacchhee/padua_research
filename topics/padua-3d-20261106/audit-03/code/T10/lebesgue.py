"""Auditor: independent Lebesgue-constant evaluation for n=6,7,8 restricted-QR vs global QR
(inherited degree-graded basis, and lexicographic-basis variant), on angular meshes
q=21,41,81 plus local maximization from the best mesh points."""
import sys, os, json, math, itertools as it
import numpy as np, scipy.linalg as la
from scipy.optimize import minimize
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from unisolvence import folded_parity, select
def exps_lex(n): return [(a,b,c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
def exps_deg(n): return [(a,b,d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]
def basis(P,n,E):
    T=[np.polynomial.chebyshev.chebvander(P[:,j],n) for j in range(3)]
    return np.array([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in E]).T
def lobatto(L): return np.cos(np.pi*np.arange(L)/(L-1))
def global_qr(n,E):
    g=np.array(list(it.product(lobatto(2*n+1),repeat=3)))
    perm=la.qr(basis(g,n,E).T,pivoting=True,mode='economic')[2]
    return g[perm[:math.comb(n+3,3)]]
def lebfun(C,n,X): return np.abs(basis(X,n,exps_lex(n))@C).sum(axis=1)
def mesh_max(C,n,q,top=0):
    ax=lobatto(q); best=[];
    for i in range(q):
        X=np.array([(ax[i],b,c) for b,c in it.product(ax,repeat=2)]); v=lebfun(C,n,X)
        if top:
            j=np.argsort(v)[-top:]; best+=list(zip(v[j],map(tuple,X[j])))
        else: best.append((v.max(),None))
    best.sort(key=lambda t:-t[0]); return best[0][0],best[:top] if top else None
def local_max(C,n,starts):
    f=lambda th: -lebfun(C,n,np.cos(th)[None,:])[0]
    vals=[]
    for v,x in starts:
        th0=np.arccos(np.clip(np.array(x),-1,1))
        r=minimize(f,th0,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':4000})
        vals.append(-r.fun)
    return max(vals)
out=[]
for n in map(int,sys.argv[2:]):
    N=math.comb(n+3,3); q,keys=folded_parity(n); sel=np.cos(2*np.pi*np.array(select(n,q,keys))/q)
    sets={'restrictedQR':sel,'QR_inherited_deg':global_qr(n,exps_deg(n)),'QR_lexicographic':global_qr(n,exps_lex(n))}
    for name,P in sets.items():
        V=basis(P,n,exps_lex(n)); C=la.solve(V,np.eye(N)); res=float(np.abs(C@V-np.eye(N)).max())
        m21,_=mesh_max(C,n,21); m41,st=mesh_max(C,n,41,top=12); m81,_=mesh_max(C,n,81)
        lm=local_max(C,n,st)
        rec={'n':n,'set':name,'cond':float(np.linalg.cond(V)),'resid':res,'mesh21':m21,'mesh41':m41,'mesh81':m81,'local_max_from41':lm,
             'cert_upper_from41':m41/(1-(n*math.pi/80)**2/2)**3}
        print(rec,flush=True); out.append(rec)
json.dump(out,open(sys.argv[1],'w'))
