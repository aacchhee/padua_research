# Auditor check of the strict-positive witness lemma.
# (A) symbolic: on k.theta=0 (3-support), F=1-v^2-w^2+2uvw equals u^2; degree<=r; integral 0; F(1,1,1)=1.
# (B) exact-node LP: for cyclic H=<2pi g/q> with short dual (min l1 <= D), maximize identity weight s.t. w>=0, exact moments through D.
#     Lemma predicts max identity weight = 0 (and hence no strictly positive full-support rule).
import sympy as sp, itertools, math, numpy as np
from scipy.optimize import linprog
x1,x2,x3,t1,t2=sp.symbols('x1 x2 x3 t1 t2')
for (a,b,c) in [(1,1,1),(3,2,1),(5,1,1),(4,4,2),(7,3,2)]:
    # parametrize theta with a*t1 + b*t2 + c*t3 = 0  -> t3 = -(a t1 + b t2)/c ; use cos identities numerically at random points
    ok=True
    for _ in range(50):
        T1,T2=np.random.uniform(0,2*np.pi,2); T3=-(a*T1+b*T2)/c
        u,v,w=np.cos(a*T1),np.cos(b*T2),np.cos(c*T3)
        ok &= abs((1-v*v-w*w+2*u*v*w)-u*u)<1e-12
    Ta=sp.chebyshevt(a,x1); Tb=sp.chebyshevt(b,x2); Tc=sp.chebyshevt(c,x3)
    Fp=sp.expand(1-Tb**2-Tc**2+2*Ta*Tb*Tc)
    deg=sp.Poly(Fp,x1,x2,x3).total_degree()
    # integral under product arcsine measure: write in Chebyshev basis: 1 - (1+T_2b)/2 - (1+T_2c)/2 + 2 TaTbTc -> constant term 0
    print((a,b,c),"identity holds:",ok,"deg",deg,"<= r",a+b+c,"F(1,1,1)=",Fp.subs({x1:1,x2:1,x3:1}))
def nodes(g,q):
    th=np.array([[2*np.pi*((j*gi)%q)/q for gi in g] for j in range(q)])
    X=np.cos(th); key=np.round(X,12)
    _,idx=np.unique(key,axis=0,return_index=True)
    return X[np.sort(idx)]
def l1min(g,q,R):
    best=10**9
    for k in itertools.product(range(-R,R+1),repeat=3):
        if any(k) and sum(ki*gi for ki,gi in zip(k,g))%q==0: best=min(best,sum(map(abs,k)))
    return best
def maxid(X,D):
    T=lambda m,x: np.cos(m*np.arccos(np.clip(x,-1,1)))
    rows=[];rhs=[]
    for al in itertools.product(range(D+1),repeat=3):
        if sum(al)<=D:
            rows.append(T(al[0],X[:,0])*T(al[1],X[:,1])*T(al[2],X[:,2])); rhs.append(1.0 if sum(al)==0 else 0.0)
    A=np.array(rows); idn=np.argmin(np.sum(np.abs(X-1),axis=1)); assert np.allclose(X[idn],1)
    cvec=np.zeros(len(X)); cvec[idn]=-1
    r=linprog(cvec,A_eq=A,b_eq=rhs,bounds=[(0,None)]*len(X),method='highs')
    return (r.status, -r.fun if r.status==0 else None)
rng=np.random.default_rng(20261106)
res=[]
for trial in range(60):
    q=int(rng.integers(6,40)); g=tuple(int(v) for v in rng.integers(1,q,3))
    X=nodes(g,q); m=l1min(g,q,12)
    for D in sorted({m, m+1, max(m-1,1)}):
        st,val=maxid(X,D)
        res.append((q,g,len(X),m,D,st,val))
viol=[r for r in res if r[4]>=r[3] and r[5]==0 and r[6]>1e-7]
pos=[r for r in res if r[4]<r[3] and r[5]==0 and r[6]>1e-7]
print("cases:",len(res)," short-dual cases with identity weight>1e-7 (lemma violations):",len(viol))
print("cases D<min-dual with positive identity weight (expected, Haar works):",len(pos), "of", sum(1 for r in res if r[4]<r[3]))
print("short-dual statuses:",sorted({(r[5]) for r in res if r[4]>=r[3]}), "max identity weight found:",max([r[6] or 0 for r in res if r[4]>=r[3]]))
