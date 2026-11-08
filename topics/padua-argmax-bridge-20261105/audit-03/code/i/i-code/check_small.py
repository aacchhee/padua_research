# Cross-check indep_S against brute-force Vandermonde interpolation (independent of kernel formula).
import numpy as np, sys
from fractions import Fraction as F
from indep_S import S_n, lambda_phys

def padua(n):
    pts=[]
    for j in range(n+1):
        for k in range(n+2):
            if (j+k)%2==0: pts.append((np.cos(j*np.pi/n), np.cos(k*np.pi/(n+1))))
    return np.array(pts)

def leb_brute(n, z):
    P=padua(n); modes=[(p,q) for p in range(n+1) for q in range(n+1-p)]
    T=lambda r,x: np.cos(r*np.arccos(np.clip(x,-1,1)))
    V=np.array([[T(p,x)*T(q,y) for (p,q) in modes] for (x,y) in P])
    v=np.array([T(p,z[0])*T(q,z[1]) for (p,q) in modes])
    L=np.linalg.solve(V.T, v)   # cardinal values L_B(z)
    return np.abs(L).sum()

for n in [1,2,3,4,5,8]:
    for (xi,ze) in [(0,0),(F(1,7),F(2,9)),(F(3,10),F(1,3)),(F(1,2),F(1,5))]:
        z=(-np.cos(np.pi*float(xi)), -np.cos(np.pi*float(ze)))
        b=leb_brute(n,z); l=lambda_phys(n,xi,ze)
        print(n,xi,ze, round(b,12), round(l,12), abs(b-l))
    print('S_n(0,0)=',S_n(n,0,0),' brute corner',leb_brute(n,(-1,-1)))
