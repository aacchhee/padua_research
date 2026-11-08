#!/usr/bin/env python3
"""[E] MEASURED: F03 primary target E_n(0)=Lambda_c-A_n^2-kappa at sampled n (float64, F03 eq.(3),
verified against direct Lagrange computation in f03_origin_check.py), compared with the leading
terms implied by the H corner expansion: (4/pi^2)[(log N+c)^2-(log n+c)^2]-1/N, N=n+1/2,
c=gamma+log(8/pi). kappa enclosure from PD-T271 (0.9197101183884925...). Finite sample only."""
import numpy as np
kappa = 0.919710118388492535; g = 0.5772156649015329; c = g + np.log(8/np.pi)
def lam(n):
    m = n + 1; tot = 0.0
    for r in range(1, n + 1):
        v = r*np.pi/m; j = np.arange(-r + 1, r, 2)
        tot += np.sum((1 + np.cos(v))/(np.cos(j*np.pi/n) - np.cos(v)))
    return 1 - 2*n/m + 4/(n*m)*tot
print("    n     E_n(0)        n*E_n(0)   H-leading pred   n*(E-pred)/log n")
for n in (32, 64, 128, 160, 161, 200, 256, 320, 512, 1000, 2000, 4000):
    A = 2/np.pi*(np.log(n) + c); E = lam(n) - A*A - kappa; N = n + 0.5
    pred = 4/np.pi**2*((np.log(N) + c)**2 - (np.log(n) + c)**2) - 1/N
    print(f"{n:5d}  {E: .6e}  {n*E: .5f}   {pred: .6e}   {n*(E - pred)/np.log(n): .4f}")
