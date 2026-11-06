import numpy as np, itertools, math
from numpy.polynomial import chebyshev as C
rng=np.random.default_rng(1)
def idx(d,n): return [a for a in itertools.product(range(n+1),repeat=d) if sum(a)<=n]
def chebV(X,I):  # Vandermonde in tensor Chebyshev basis
    return np.array([[np.prod([np.cos(a[j]*np.arccos(np.clip(x[j],-1,1))) for j in range(len(a))]) for a in I] for x in X])
# (1) multiplier of R for a concrete interpolation projection P=I_X, d=3,n=2
d,n=3,2; I=idx(d,n); N=len(I)
X=rng.uniform(-1,1,(N,d)); V=chebV(X,I); print("cond",np.linalg.cond(V))
g=24; th=2*np.pi*np.arange(g)/g
TH=np.meshgrid(*([th]*d),indexing='ij')
maxerr=0
for k in itertools.product(range(-4,5),repeat=d):
    # J^{-1} E e_k = prod T_|k_j|
    data=np.array([np.prod([np.cos(abs(k[j])*np.arccos(x[j])) for j in range(d)]) for x in X])
    coef=np.linalg.solve(V,data)          # interpolant in Chebyshev basis
    lift=sum(c*np.prod([np.cos(a[j]*TH[j]) for j in range(d)],axis=0) for c,a in zip(coef,I))
    F=np.fft.fftn(lift)/g**d
    ckk=F[tuple(t%g for t in k)]
    s=sum(t!=0 for t in k)
    expect = 2.0**(-s) if sum(map(abs,k))<=n else 0.0
    maxerr=max(maxerr,abs(ckk-expect))
print("max |c_kk - expected| over k in [-4,4]^3:",maxerr)
# (2) sampled Lebesgue constants of some unisolvent sets (sampled max <= true Lambda)
def leb(X,n,M=60000):
    I=idx(3,n); V=chebV(X,I); Vi=np.linalg.inv(V)
    Z=np.vstack([rng.uniform(-1,1,(M,3)), np.array(list(itertools.product(np.cos(np.linspace(0,np.pi,13)),repeat=3)))])
    L=np.abs(chebV(Z,I)@Vi).sum(1); return L.max()
for n in (2,3,4,5):
    I=idx(3,n); cl=np.cos(np.pi*np.arange(n+1)/n)
    Xl=np.array([[cl[a[0]],cl[a[1]],cl[a[2]]] for a in I])  # Chebyshev-Lobatto simplex lower set
    Xr=rng.uniform(-1,1,(len(I),3))
    m=n//2; b=max(1,sum(1/a for a in range(1,m+1))**3/(648*math.pi**3))
    print(n,"bound",b,"lowerset Lambda>=",round(leb(Xl,n),3),"random Lambda>=",round(leb(Xr,n),1))
