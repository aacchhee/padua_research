#!/usr/bin/env python3
"""[E] F03 routine origin identities versus a convention-free direct computation.

Direct: Lagrange basis of total-degree-n polynomials at the node set
{(cos(j pi/n), cos(k pi/(n+1))): 0<=j<=n, 0<=k<=n+1, j+k even}, Lebesgue function
lambda(x)=sum|ell_xi(x)| at the nonnode corner (-1,-1) (float64 Chebyshev-basis solve).
Formula F03(3): Lambda_c=1-2n/m+(4/(nm)) sum_{r=1}^n P_r, P_r=sum_{j=-r+1,-r+3..r-1} F_r(j pi/n).
Also (4) P_r=w_r T_{n,r}, (5) full sum = n, (6) Z_r=P_r-n>0 (r<n), Z_n=0, (7) digamma split,
and the coarse 8M/pi bound with M=sup|B|. mpmath for the identities.
Usage: PYTHONPATH=<pylib> python3 f03_origin_check.py
"""
import numpy as np
from numpy.polynomial import chebyshev as Ch
from mpmath import mp, mpf, cos, cot, pi, nstr, fabs, digamma, tan

mp.dps = 30

def lebesgue_corner_direct(n, x=(-1.0, -1.0)):
    nodes = [(np.cos(j*np.pi/n), np.cos(k*np.pi/(n + 1))) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    idx = [(a, b) for a in range(n + 1) for b in range(n + 1 - a)]
    assert len(nodes) == len(idx) == (n + 1)*(n + 2)//2
    def basis(pt):
        ta = Ch.chebvander(np.array([pt[0]]), n)[0]; tb = Ch.chebvander(np.array([pt[1]]), n)[0]
        return np.array([ta[a]*tb[b] for a, b in idx])
    V = np.array([basis(p) for p in nodes])          # V[node, basis]
    ell = np.linalg.solve(V.T, basis(x))             # Lagrange values at x
    return float(np.abs(ell).sum()), np.linalg.cond(V)

def F03_terms(n):
    m = n + 1
    P = []
    for r in range(1, n + 1):
        v = r*pi/m
        P.append(sum((1 + cos(v))/(cos(j*pi/n) - cos(v)) for j in range(-r + 1, r, 2)))
    lam3 = 1 - mpf(2*n)/m + mpf(4)/(n*m)*sum(P)
    lam6 = 1 + mpf(2*n)/m + mpf(4)/(n*m)*sum(p - n for p in P)
    dev4 = dev7 = 0; Zmin = None
    for r in range(1, n + 1):
        a = (1 - mpf(r)/m)/2; w = cot(pi*r/(2*m))
        T = sum(cot(pi*(l + a)/n) for l in range(r))
        dev4 = max(dev4, fabs(P[r - 1] - w*T))
        Hr = lambda b: digamma(b + r) - digamma(b)
        Bf = lambda x: cot(pi*x) - 1/(pi*x) + 1/(pi*(1 - x))
        T7 = (n/pi)*(Hr(a) - Hr(n - r + 1 - a)) + sum(Bf((l + a)/n) for l in range(r))
        dev7 = max(dev7, fabs(T - T7))
        full = sum(cot(pi*(l + a)/n) for l in range(n))
        dev5 = fabs(full - n*tan(pi*r/(2*m)))
        Z = P[r - 1] - n
        if r < n:
            Zmin = Z if Zmin is None else min(Zmin, Z)
    return lam3, lam6, dev4, dev7, dev5, Zmin, P[-1] - n

print(" n   direct lambda(-1,-1)    F03 (3)              |dir-(3)|   |(3)-(6)|  max|P-wT|  max|T-(7)|  min Z_r(r<n)  Z_n   cond(V)")
for n in list(range(2, 21)) + [25, 31, 40, 48]:
    d, cond = lebesgue_corner_direct(n)
    lam3, lam6, dev4, dev7, dev5, Zmin, Zn = F03_terms(n)
    print(f"{n:3d}  {d:.15f}  {nstr(lam3, 16):>20s}  {abs(d - float(lam3)):.2e}  {float(fabs(lam3 - lam6)):.1e}  {float(dev4):.1e}  {float(dev7):.1e}  {nstr(Zmin, 4) if Zmin is not None else '-':>10s}  {nstr(Zn, 2):>5s}  {cond:.1e}")
# B bounds: B(0)=1/pi, B(1)=-1/pi; sup|B| on [0,1]
Bf = lambda x: cot(pi*x) - 1/(pi*x) + 1/(pi*(1 - x))
xs = [mpf(k)/2000 for k in range(1, 2000)]
print("sup|B| on grid (0,1):", nstr(max(fabs(Bf(x)) for x in xs), 8), " 1/pi =", nstr(1/pi, 8), "; B(1e-9) =", nstr(Bf(mpf('1e-9')), 8), "; B(1-1e-9)=", nstr(Bf(1 - mpf('1e-9')), 8))
