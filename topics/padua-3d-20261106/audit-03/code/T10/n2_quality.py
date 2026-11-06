"""Auditor: Lebesgue constants of the 24 admissible (degree-3 Haar-exact) 10-node unisolvent
order-19 lattice node sets at n=2, plus exact degree-3 cubature check on actual nodes."""
import sys,os,json,math,itertools as it,numpy as np,scipy.linalg as la
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from minfold_search import dual_numerators
d=json.load(open(sys.argv[1])); full=[tuple(v) for v,m in d['full'] if m==10]
def exps(n): return [(a,b,c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
def basis(P,n):
    T=[np.polynomial.chebyshev.chebvander(P[:,j],n) for j in range(3)]
    return np.array([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in exps(n)]).T
ax=np.cos(np.pi*np.arange(41)/40); M=np.array(list(it.product(ax,repeat=3)))
out=[]
for v in full:
    q,H=dual_numerators(v); F=np.minimum(H,q-H); keys,cnt=np.unique(F,axis=0,return_counts=True)
    P=np.cos(2*np.pi*keys/q); w=cnt/q
    # cubature check: exact Chebyshev moments of T_a T_b T_c through degree 3 (integral = [a=b=c=0])
    Vc=basis(P,3); mom=w@Vc; err=np.abs(mom-np.eye(len(exps(3)))[0]).max()
    V=basis(P,2); C=la.solve(V,np.eye(10)); lam=np.abs(basis(M,2)@C).sum(axis=1).max()
    out.append({'B':v,'nodes':len(keys),'deg3_moment_err':float(err),'cond':float(np.linalg.cond(V)),'Lambda41':float(lam)})
lams=sorted(r['Lambda41'] for r in out)
print(len(out),'max moment err',max(r['deg3_moment_err'] for r in out),'Lambda41 range',lams[0],lams[-1])
json.dump(out,open(sys.argv[2],'w'))
