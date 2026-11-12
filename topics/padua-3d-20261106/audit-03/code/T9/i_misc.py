# Auditor independent enumerations (exact integer / numerical as labeled).
import itertools, math, numpy as np
from fractions import Fraction as F
# (1) 2D Padua cyclic group generator (n,n+1) mod 2n(n+1): brute-force dual l1 minimum (exact integers)
ok=True
for n in range(1,17):
    q=2*n*(n+1); best=min(abs(a)+abs(b) for a in range(-3*n,3*n+1) for b in range(-3*n,3*n+1) if (a or b) and (a*n+b*(n+1))%q==0)
    ok&=(best==2*n)
print("Padua 2D dual l1 minimum == 2n for n=1..16 (brute force):",ok)
# (2) parity-anisotropic family: H = grid (n,n+1,n+1) U half-step translate; count folded cos-points exactly and numerical rank
def T(m,x): return np.cos(m*np.arccos(np.clip(x,-1,1)))
for n in range(1,9):
    ords=(n,n+1,n+1); pts=set()
    for sh in (0,1):
        for idx in itertools.product(*[range(o) for o in ords]):
            # angle = 2pi (i + sh/2)/o ; cos key as reduced fraction of pi: use exact (2i+sh)/(2o) mod 2, folded by sign
            key=[]
            for i,o in zip(idx,ords):
                f=F(2*i+sh,o)  # angle/pi in [0,2)
                f=f%2; f=min(f,2-f)  # fold theta -> -theta
                key.append(f)
            pts.add(tuple(key))
    A=lambda m:m//2+1; B=lambda m:(m+1)//2
    Fn=A(n)*A(n+1)**2+B(n)*B(n+1)**2
    X=np.array([[math.cos(math.pi*float(k)) for k in p] for p in pts])
    idx=[(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
    V=np.stack([T(a,X[:,0])*T(b,X[:,1])*T(c,X[:,2]) for a,b,c in idx],axis=1)
    rk=np.linalg.matrix_rank(V,tol=1e-9*np.linalg.norm(V,2))
    print(f"n={n} folded={len(pts)} formula={Fn} rank={rk} N={math.comb(n+3,3)}")
# (3) tetrahedron Lambda on a fine mesh (not only vertices), several t
for t in (1.0,0.5,0.25,0.1):
    eps=[e for e in itertools.product((-1,1),repeat=3) if e[0]*e[1]*e[2]==1]
    g=np.linspace(-1,1,41); P=np.array(list(itertools.product(g,g,g)))
    lam=sum(np.abs((1+e[0]*P[:,0]/t+e[1]*P[:,1]+e[2]*P[:,2])/4) for e in eps)
    print("t",t,"mesh max",lam.max(),"formula",max(1/t,(1/t+3)/2))
# (4) Gauss tensor phase counterexample: q points cos(a+2pi j/q), a=pi/(2q): exact Chebyshev moments through 2q-1 (1D suffices for tensor)
for q in range(2,9):
    x=np.cos(np.pi/(2*q)+2*np.pi*np.arange(q)/q)
    mom=[abs(np.mean(T(m,x))) for m in range(1,2*q)]
    zeros=np.sort(np.cos((2*np.arange(q)+1)*np.pi/(2*q)))
    print("q",q,"max|moment| m=1..2q-1:",f"{max(mom):.1e}","nodes=Tq zeros:",np.allclose(np.sort(x),zeros), "dual min of qZ^3 = q < 2q")
