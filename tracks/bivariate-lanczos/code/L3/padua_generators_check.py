"""R02 (MEASURED sanity check of PD-T?bivariate-lanczos-claude-309(b)): the two-term generators
g_m = T_{n-m}(x)T_m(y) - T_m(x)T_{n+1-m}(y), m = 0..n, and w = (x^2-1)U_{n-1}(x) vanish on padua(n),
are independent (rank n+2 on 60 random points), and the interior-node gradient formula holds.
Usage: python3 padua_generators_check.py"""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import numpy as np
from numpy.polynomial import chebyshev as C
from l3lib import padua
def T(k,t): c=np.zeros(k+1); c[k]=1; return C.chebval(t,c)
def dT(k,t):
    if k==0: return 0*t
    c=np.zeros(k+1); c[k]=1; return C.chebval(t,C.chebder(c))
for n in range(1,9):
    P=padua(n); x,y=P[:,0],P[:,1]
    vals=[T(n-m,x)*T(m,y)-T(m,x)*T(n+1-m,y) for m in range(n+1)]
    om=(x**2-1)*(dT(n,x)/n)  # (x^2-1)U_{n-1}(x), U_{n-1}=T_n'/n
    vals.append(om)
    mx=max(np.max(np.abs(v)) for v in vals)
    # independence: sample the polynomials on random points
    R=np.random.default_rng(0).uniform(-1,1,(60,2)); xr,yr=R[:,0],R[:,1]
    A=np.array([T(n-m,xr)*T(m,yr)-T(m,xr)*T(n+1-m,yr) for m in range(n+1)]+[(xr**2-1)*dT(n,xr)/n])
    rk=np.linalg.matrix_rank(A,tol=1e-10)
    # gradient formula at interior nodes
    err=0
    for (xi,yi) in P:
        if abs(abs(xi)-1)<1e-12 or abs(abs(yi)-1)<1e-12: continue
        s=T(n,xi)
        for m in range(1,n+1):
            gx=dT(n-m,xi)*T(m,yi)-dT(m,xi)*T(n+1-m,yi)
            gy=T(n-m,xi)*dT(m,yi)-T(m,xi)*dT(n+1-m,yi)
            U=lambda k,t: dT(k+1,t)/(k+1)
            fx=-s*n*U(m-1,xi)*T(m,yi); fy=s*(n+1)*T(m,xi)*U(m-1,yi)
            err=max(err,abs(gx-fx),abs(gy-fy))
    print(f"n={n}: max|gen at nodes|={mx:.1e} rank(gens)={rk} (n+2={n+2}) interior-gradient-formula err={err:.1e}")
