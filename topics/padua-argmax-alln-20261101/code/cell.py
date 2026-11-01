"""Maximise the shifted-lattice majorant over one fundamental cell [0,2pi/n) x [0,pi/(n+1)] of the Padua torus lattice and compare with its value at the coset point (pi/n, 0) = non-node corner class (float64 + Nelder-Mead, MEASURED)."""
import numpy as np, maj, sys
from scipy.optimize import minimize
for n in [int(v) for v in sys.argv[1:]]:
    S=maj.setup(n); M=41
    A=np.linspace(0,2*np.pi/n,M); B=np.linspace(0,np.pi/(n+1),M//2+1)
    X,Y=np.meshgrid(A,B,indexing='ij')
    l,m=maj.lam(n,X.ravel(),Y.ravel(),S)
    star=maj.lam(n,[np.pi/n],[0.0],S)[1][0]
    i=m.argmax(); x0=(X.ravel()[i],Y.ravel()[i])
    f=lambda z:-maj.lam(n,[z[0]],[z[1]],S)[1][0]
    r=minimize(f,x0,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12})
    print(n,"S(t*)=%.6f"%star,"cell grid max=%.6f"%m.max(),"opt max=%.8f at (%.4f*pi/n, %.4f*pi/(n+1))"%(-r.fun,r.x[0]*n/np.pi,r.x[1]*(n+1)/np.pi),"excess=%.2e"%(-r.fun-star))
