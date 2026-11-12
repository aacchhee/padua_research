import sys,os,json,math,itertools as it,numpy as np,scipy.linalg as la
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from minfold_search import dual_numerators, rank_mod
from window_search import admissible
def exps(n): return [(a,b,c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
def basis(P,n):
    T=[np.polynomial.chebyshev.chebvander(P[:,j],n) for j in range(3)]
    return np.array([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in exps(n)]).T
v=(1,3,3,6,0,10); n=3
q,H=dual_numerators(v); F=np.minimum(H,q-H); keys,cnt=np.unique(F,axis=0,return_counts=True)
P=np.cos(2*np.pi*keys/q); w=cnt/q
mom=w@basis(P,5); err=np.abs(mom-np.eye(len(exps(5)))[0]).max()
mom6=w@basis(P,6); err6=np.abs(mom6-np.eye(len(exps(6)))[0]).max()
good,_=admissible(3,60);
V=basis(P,3); G=V.T@(w[:,None]*V)
ax=np.cos(np.pi*np.arange(41)/40); M=np.array(list(it.product(ax,repeat=3)))
C=la.solve(G,V.T*w); LS=np.abs(basis(M,3)@C).sum(axis=1).max()
print({'B':v,'det':q,'nodes':len(keys),'deg5_err':float(err),'deg6_err':float(err6),'in_window_search_det60':v in good,
       'rank_mod_p':rank_mod(v,3),'LS_projection_Lambda41':float(LS),'gram_cond':float(np.linalg.cond(G))})
