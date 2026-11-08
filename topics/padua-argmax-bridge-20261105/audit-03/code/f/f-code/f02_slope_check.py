#!/usr/bin/env python3
"""[E] F02: direct full projected defect Q_n at J=1,K=2, zero phase (eq.(4), all z and k),
compared with the claimed lim Q_n/log n = 16/(3pi^2) via doubling differences
Q_{2n}-Q_n -> (16/(3pi^2))log 2; and the continuous reference g_v(2pi/(n+1)) of
eq. defining h_gamma by scipy adaptive quadrature, doubling differences -> (8log2/pi^2)log2.
MEASURED finite-range trend check only; it cannot prove a limit."""
import numpy as np
from scipy.integrate import quad
exec(open('f06_floor_check.py').read().split('if __name__')[0])

def gv(gam):
    def inner(b):
        yp, ym = np.cos(b + gam), np.cos(b - gam); A, B = 1 + yp, 1 + ym
        lo = abs(b - gam); hi = min(b + gam, 2*np.pi - b - gam)
        if hi <= lo: return 0.0
        xs = (A*ym + B*yp)/(A + B); us = np.arccos(np.clip(xs, -1, 1))
        f = lambda u: min(A/(np.cos(u) - yp), B/(ym - np.cos(u))) if yp < np.cos(u) < ym else 0.0
        pts = sorted(set([lo, hi] + ([us] if lo < us < hi else [])))
        return sum(quad(f, pts[i], pts[i + 1], limit=200, epsabs=1e-13, epsrel=1e-11)[0] for i in range(len(pts) - 1))
    br = [0, gam, np.pi - gam, np.pi]
    return 2/np.pi**2*sum(quad(inner, br[i], br[i + 1], limit=400, epsabs=1e-12, epsrel=1e-10)[0] for i in range(3))

cQ = 16/(3*np.pi**2)*np.log(2); cg = 8*np.log(2)/np.pi**2*np.log(2)
prevQ = prevg = None
print("   n      Q_n         Q_n/log n   dQ(doubling) [->%.5f]   g_v       dg [->%.5f]   g_v-Q_n" % (cQ, cg))
for n in (128, 256, 512, 1024, 2048, 4096):
    q = Qv(n, 1, 2, 0.0, 0.0); g = gv(2*np.pi/(n + 1))
    dq = '' if prevQ is None else '%.5f' % (q - prevQ)
    dg = '' if prevg is None else '%.5f' % (g - prevg)
    print(f"{n:5d}  {q:.6f}  {q/np.log(n):.5f}   {dq:>10s}             {g:.6f}  {dg:>8s}       {g - q:.5f}")
    prevQ, prevg = q, g
