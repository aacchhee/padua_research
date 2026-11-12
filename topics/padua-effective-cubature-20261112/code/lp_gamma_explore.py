"""(Session-1 exploration, round 3; NUMERICALLY UNRELIABLE, see attempts/E1-gamma.md. Kept for the record only.)
MEASURED exploration: Cohn-Elkies/Delsarte LP for int(O) (K-K = {|x|_1<=1}) in the class
f = P(x) e^{-pi|x|^2}, P in B3-invariants s1^i s2^j s3^k of degree <= 2D. Cut-plane LP.
maximize G(0) s.t. P(0) = 1, P(x) e^{-pi|x|^2} <= 0 on |x|_1 >= 1 (samples), G(u) e^{-pi|u|^2} >= 0 (samples).
gamma = 6 G(0)/P(0) - 1 (alpha = 1)."""
import sys, numpy as np, highspy
from math import pi, comb
import numpy.polynomial.polynomial as Pl
D = int(sys.argv[1]); rng = np.random.default_rng(0)
basis = [(i,j,k) for i in range(D+1) for j in range(D+1) for k in range(D+1) if i+2*j+3*k <= D]
nb = len(basis)
# monomial expansion of each basis element in y=x^2 variables (float), and transform
from collections import defaultdict
def mul(p,q):
    r=defaultdict(float)
    for a,v in p.items():
        for b,w in q.items(): r[(a[0]+b[0],a[1]+b[1],a[2]+b[2])]+=v*w
    return r
s={1:{(1,0,0):1.,(0,1,0):1.,(0,0,1):1.},2:{(2,0,0):1.,(0,2,0):1.,(0,0,2):1.},3:{(3,0,0):1.,(0,3,0):1.,(0,0,3):1.}}
cache={}
def pw(t,e):
    if (t,e) not in cache: cache[(t,e)]={(0,0,0):1.} if e==0 else mul(pw(t,e-1),s[t])
    return cache[(t,e)]
h=[np.array([1.0])]
for n in range(2*D+2):
    hn=h[-1]; d=Pl.polyder(hn) if len(hn)>1 else np.array([0.0]); h.append(Pl.polysub(d,Pl.polymulx(hn)*2*pi))
T={a: ((-1)**a)*(2*pi)**(-2*a)*h[2*a] for a in range(D+1)}  # poly in u (full), even
B_P=[]; B_G=[]
for (i,j,k) in basis:
    m=mul(mul(pw(1,i),pw(2,j)),pw(3,k)); B_P.append(m)
def evalP(m, X):  # X (n,3)
    Y=X**2; out=np.zeros(len(X))
    for a,v in m.items(): out+=v*Y[:,0]**a[0]*Y[:,1]**a[1]*Y[:,2]**a[2]
    return out
def evalG(m, U):
    vals={a:[Pl.polyval(U[:,i],T[a]) for i in range(3)] for a in range(D+1)}
    out=np.zeros(len(U))
    for a,v in m.items(): out+=v*vals[a[0]][0]*vals[a[1]][1]*vals[a[2]][2]
    return out
def rowsP(X): return np.stack([evalP(m,X) for m in B_P],1)*np.exp(-pi*(X**2).sum(1))[:,None]
def rowsG(U): return np.stack([evalG(m,U) for m in B_P],1)*np.exp(-pi*(U**2).sum(1))[:,None]
def fd(n,R):
    return np.sort(np.abs(rng.uniform(-R,R,(n,3))),axis=1)
def region(n,R):
    X=fd(4*n,R); X=X[X.sum(1)>=1.0]; return X[:n]
g0=rowsG(np.zeros((1,3)))[0]; p0=rowsP(np.zeros((1,3)))[0]
XP=region(4000,3.5); UG=fd(4000,4.0)
AP=rowsP(XP); AG=rowsG(UG)
scale=np.maximum(np.abs(np.vstack([AP,AG])).max(0),1e-300)
def solve(AP,AG):
    h=highspy.Highs(); h.setOptionValue('output_flag',False)
    inf=highspy.kHighsInf
    for c in range(nb): h.addVar(-inf,inf)
    h.changeColsCost(nb,np.arange(nb),-g0/scale)
    h.setOptionValue('primal_feasibility_tolerance',1e-10); h.setOptionValue('dual_feasibility_tolerance',1e-10)
    def add(A,lo,up):
        A=A/scale[None,:]
        for r in A: h.addRow(lo,up,nb,np.arange(nb),r)
    add(p0[None,:],1.0,1.0); add(AP,-inf,0.0); add(AG,0.0,inf)
    h.run(); sol=np.array(h.getSolution().col_value)/scale
    return sol, h.getInfo().objective_function_value
for it in range(25):
    c,obj=solve(AP,AG)
    Xn=region(60000,3.5); Un=fd(60000,4.5)
    vp=rowsP(Xn)@c; vg=rowsG(Un)@c
    gam=6*(g0@c)-1
    print(f'D={D} it {it} gamma(alpha=1)={gam:.6f} maxP*w={vp.max():.2e} minG*w={vg.min():.2e} rows {len(AP)+len(AG)}', flush=True)
    bp=np.argsort(vp)[-400:]; bg=np.argsort(vg)[:400]
    bp=bp[vp[bp]>0]; bg=bg[vg[bg]<0]
    if not len(bp) and not len(bg): break
    AP=np.vstack([AP,rowsP(Xn[bp])]); AG=np.vstack([AG,rowsG(Un[bg])])
np.save(f'sol_D{D}.npy',c)
