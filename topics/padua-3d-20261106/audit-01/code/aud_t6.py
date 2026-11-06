import numpy as np, itertools, math
from fractions import Fraction
# (a) Fourier L1 of D_n^3 vs bound H^3/(24 pi^3)
def D_L1(n,grid):
    f=np.zeros((grid,)*3)
    for k in itertools.product(range(-n,n+1),repeat=3):
        if sum(map(abs,k))<=n: f[tuple(t%grid for t in k)]=1
    v=np.fft.ifftn(f)*grid**3
    return float(np.mean(np.abs(v.real))), float(np.max(np.abs(v.imag)))
H=lambda m: sum(1/a for a in range(1,m+1))
print("n  L1(grid g)  L1(grid 2g)  bound24  ratio   bound648")
for n,g in ((2,48),(3,48),(4,64),(6,64),(8,96),(12,96),(16,128),(24,160),(32,192)):
    a,_=D_L1(n,g); b,_=D_L1(n,2*g) if n<=16 else (float('nan'),0)
    m=n//2; lb=H(m)**3/(24*math.pi**3)
    print(n, round(a,5), round(b,5), round(lb,6), round(a/lb,1), lb/27)
# crossover where H_m^3 > 648 pi^3
target=(648*math.pi**3)**(1/3)
print("need H_m >",target, " => m ~ exp(",target-0.5772156649,") =", math.exp(target-0.5772156649), " n ~",2*math.exp(target-0.5772156649))
# exact facet/subset checks, own implementation, d=3..6
def facet(k,n):
    s=sum(k); return tuple([n-s]+[n-s+2*k[j] for j in range(1,len(k))])
for d in (3,4,5,6):
    for n in range(d-1,(13 if d<=4 else 9)):
        m=n//(d-1)
        ball=[k for k in itertools.product(range(-n,n+1),repeat=d) if sum(map(abs,k))<=n]
        rs=[facet(k,n) for k in ball]
        assert min(min(r) for r in rs)>=0 and len(set(rs))==len(ball)
        S=Fraction(0); hits=0
        for a in itertools.product(range(1,m+1),repeat=d):
            if a[0]<=min(a[1:]):
                k=(n-sum(a[1:])+(d-3)*a[0],)+tuple(a[j]-a[0] for j in range(1,d))
                assert min(k)>=0 and sum(map(abs,k))<=n and facet(k,n)==tuple(2*x for x in a)
                S+=Fraction(1,math.prod(a)); hits+=1
        Hm=sum((Fraction(1,a) for a in range(1,m+1)),Fraction(0))
        assert d*S>=Hm**d
print("facet/subset checks d=3..6 ok")
# det A
for d in range(2,8):
    A=-np.ones((d,d)); 
    for j in range(1,d): A[j,j]+=2
    print(d, round(np.linalg.det(A)), -2**(d-1))
