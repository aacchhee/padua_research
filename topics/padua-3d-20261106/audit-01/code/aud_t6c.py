import numpy as np, math
from scipy.integrate import quad
# d=1 nontrivial regime of (1): ||P|| >= ||D_n||_1/3 with ||D_n||_1 > 3
def L1D(n):
    f=lambda t: abs(math.sin((n+0.5)*t)/math.sin(t/2)) if t>1e-14 else 2*n+1
    pts=[2*math.pi*j/(2*n+1) for j in range(1,n+1)]
    return quad(f,0,math.pi,points=pts,limit=4*n+50)[0]/math.pi
def leb_cheb(n,M=200001):
    k=np.arange(n+1); x=np.cos((2*k+1)*np.pi/(2*n+2))
    z=np.cos(np.linspace(0,np.pi,M))
    # barycentric weights for Chebyshev zeros
    w=(-1.0)**k*np.sin((2*k+1)*np.pi/(2*n+2))
    diff=z[:,None]-x[None,:]; diff[diff==0]=1e-300
    t=w/diff; return np.max(np.abs(t).sum(1)/np.abs(t.sum(1)))
for n in (100,300,1000,3000):
    L=L1D(n); lam=leb_cheb(n)
    print(n,"||D||_1=%.4f"%L,"/3=%.4f"%(L/3),"Lambda_cheb>=%.4f"%lam,"(2/pi)log(n+1)+0.9625=%.4f"%(2/math.pi*math.log(n+1)+0.9625))
