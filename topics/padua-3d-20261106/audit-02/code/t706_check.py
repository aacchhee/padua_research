# Independent check of T7-06: X = cos(2*pi*(a+H)), H=<(7,7,4)/10,(5,0,5)/10>, a=(1,2,4)/101.
# Angles are m/1010 of a full turn. Map Z[zeta_1010,1/2] -> F_p (zeta -> omega, primitive 1010th root);
# a nonzero image of det implies det != 0 (ring homomorphism). Also high-precision float check.
from fractions import Fraction as F
from sympy import isprime, primitive_root, factorint
import itertools, mpmath
H=set()
for k in range(10):
    for l in range(2):
        H.add(tuple((F(7*k,10)+F(5*l,10)*s) % 1 for s in (1,0,1)) if False else None)
H=set()
g=(F(7,10),F(7,10),F(4,10)); h=(F(5,10),F(0),F(5,10)); a=(F(1,101),F(2,101),F(4,101))
for k in range(10):
    for l in range(2):
        H.add(tuple((k*g[j]+l*h[j]) % 1 for j in range(3)))
assert len(H)==20
A=[tuple((a[j]+t[j])%1 for j in range(3)) for t in sorted(H)]
m=[tuple(int(x*1010) for x in pt) for pt in A]; assert all(F(mm,1010)==pt[j] for pt,row in zip(A,m) for j,mm in enumerate(row))
# distinct cosine nodes: cos equal iff m == +-m' mod 1010
key=lambda r: tuple(min(x%1010,(-x)%1010) for x in r)
assert len({key(r) for r in m})==20
mons=[(i,j,k) for i in range(4) for j in range(4) for k in range(4) if i+j+k<=3]; assert len(mons)==20
def det_mod(M,p):
    M=[row[:] for row in M]; n=len(M); d=1
    for c in range(n):
        piv=next((r for r in range(c,n) if M[r][c]%p),None)
        if piv is None: return 0
        if piv!=c: M[c],M[piv]=M[piv],M[c]; d=-d
        d=d*M[c][c]%p; inv=pow(M[c][c],p-2,p)
        for r in range(c+1,n):
            f=M[r][c]*inv%p
            if f: M[r]=[(x-f*y)%p for x,y in zip(M[r],M[c])]
    return d%p
res=[]
for p in [8081, 12121, 20201]:
    if not isprime(p) or (p-1)%1010: continue
    gpr=primitive_root(p); om=pow(gpr,(p-1)//1010,p)
    assert all(pow(om,1010//q,p)!=1 for q in factorint(1010))
    i2=pow(2,p-2,p); c=lambda x:(pow(om,x%1010,p)+pow(om,(-x)%1010,p))*i2%p
    V=[[c(r[0])**i*c(r[1])**j*c(r[2])**k%p for (i,j,k) in mons] for r in m]
    res.append((p,om,det_mod(V,p)))
mpmath.mp.dps=60
Vf=mpmath.matrix([[mpmath.cos(2*mpmath.pi*r[0]/1010)**i*mpmath.cos(2*mpmath.pi*r[1]/1010)**j*mpmath.cos(2*mpmath.pi*r[2]/1010)**k for (i,j,k) in mons] for r in m])
print({"nodes":20,"monomials":20,"det_mod_p":res,"det_float_60digits":mpmath.nstr(mpmath.det(Vf),15)})
