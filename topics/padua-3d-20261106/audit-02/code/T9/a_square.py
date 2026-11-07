# Audit checks for T9-02 square-wave dual.
import sympy as sp, itertools as it, json, math
from fractions import Fraction as F
import mpmath as mp
A=sp.Matrix([[-1,-1,-1],[-1,1,-1],[-1,-1,1]]); print('det A',A.det(),' A^-1',A.inv().tolist())
t=sp.symbols('t',real=True)
for r in range(1,8):
    c=(sp.integrate(sp.exp(sp.I*r*t),(t,0,sp.pi))-sp.integrate(sp.exp(sp.I*r*t),(t,sp.pi,2*sp.pi)))/(2*sp.pi)
    print('r',r,'coef',sp.simplify(c),' expected',(2*sp.I/(sp.pi*r)) if r%2 else 0)
Ainv=A.inv()
def S_independent(n):
    # enumerate odd positive r-vectors, map back k=A^{-1}(r-(n+1)1), keep integer k with |k|_1<=n
    s=F(0); seen=set()
    R=range(1,2*n+2,2)
    for r in it.product(R,repeat=3):
        k=Ainv*sp.Matrix([r[i]-(n+1) for i in range(3)])
        if any(x.q!=1 for x in k): continue
        k=tuple(int(x) for x in k)
        if sum(map(abs,k))>n: continue
        assert k not in seen; seen.add(k)
        s+=F(1,2**sum(x!=0 for x in k)*r[0]*r[1]*r[2])
    return s
def S_fast(n):
    s=F(0); rmin=10**9
    for k in it.product(range(-n,n+1),repeat=3):
        if sum(map(abs,k))>n: continue
        r=(n+1-k[0]-k[1]-k[2],n+1-k[0]+k[1]-k[2],n+1-k[0]-k[1]+k[2]); rmin=min(rmin,*r)
        if all(x%2 for x in r): s+=F(1,2**sum(x!=0 for x in k)*r[0]*r[1]*r[2])
    return s,rmin
rec=json.load(open('topics/padua-3d-20261106/evidence/t9-checks.json'))
for row in rec['squarewave']:
    n=row['n']
    if n<=16:
        si=S_independent(n); print('n',n,'independent==receipt',str(si)==row['sum'])
    else:
        print('n',n,'fast==receipt',str(S_fast(n)[0])==row['sum'])
O=lambda m: sum((F(1,2*a+1) for a in range(m+1)),F(0))
ok=True; worst=None
for n in range(1,61):
    s,rmin=S_fast(n); assert rmin>=1
    ratio=s/(O(n//2)**3/24)
    if ratio<1: ok=False
    worst=ratio if worst is None or ratio<worst else worst
print('S_n >= O_m^3/24 for n=1..60:',ok,' min ratio',float(worst))
# compare finite formula with ||K_n||_1 grid values from a_kernel (should be <=)
for n in (1,2,3,4,8):
    print('n',n,'finite square-wave lower',float(8*S_fast(n)[0]/math.pi**3))
# threshold where O_m^3/(3 pi^3) exceeds 1 and 3/4+3/(2pi), with interval arithmetic for pi and exact O_m
mp.iv.dps=60
def first(target_iv):
    o=F(0); a=0
    while True:
        o+=F(1,2*a+1)
        ov=mp.iv.mpf(o.numerator)/o.denominator
        val=ov**3/(3*mp.iv.pi**3)
        if val.a>target_iv.b: return 2*a, a, val
        if not (val.b<target_iv.a): print('UNDECIDED at a',a);
        a+=1
n1,m1,v1=first(mp.iv.mpf(1)); print('first n with O_m^3/(3pi^3)>1 (interval-certified):',n1,'m',m1,'value',v1)
tgt=mp.iv.mpf(3)/4+mp.iv.mpf(3)/(2*mp.iv.pi)
n2,m2,v2=first(tgt); print('first n with O_m^3/(3pi^3)>3/4+3/(2pi) (interval-certified):',n2,'m',m2,'value',v2)
mp.mp.dps=30
for m in (10,100,1000,10**5):
    om=mp.harmonic(2*m+1)-mp.harmonic(m)/2
    print('m',m,'O_m-(1/2)ln m',om-mp.log(m)/2,' limit ln2+gamma/2',mp.log(2)+mp.euler/2)
print('coefficient ratio (1/(24pi^3))/(1/(648pi^3)) =',sp.Rational(648,24))
