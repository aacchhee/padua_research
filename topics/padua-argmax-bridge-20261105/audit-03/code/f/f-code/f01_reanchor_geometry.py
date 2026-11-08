#!/usr/bin/env python3
"""[E] F01-seam-reanchor section 1-2 cross-check (MEASURED, finite grid).

(a) exact-rational check of the fixed-phase constants (2) via Fraction Taylor bounds;
(b) dense grid on the closed outer domain 5/4<=x+y<=pi, x,y>=0 (both boundaries,
    axes, x=pi included): p,q<=3/5+(3/2)sqrt(v), |p-q|<=3sqrt(v), P<=6/5+3v;
(c) the literal E08 CEphi (as restated in E13 section 2) plus KD*P, evaluated
    at actual phases, against F01's envelope C_b+P0*KD+C_s sqrt(v)+(C_l+3KD)v.
This is a numerical cross-check of an algebraic majorization, not a proof.
"""
from fractions import Fraction as Fr
import math, sys
sys.path.insert(0, '.')
import numpy as np

# (a) exact rational Taylor inequalities at 5/8
x = Fr(5, 8)
cos_up = 1 - x**2/2 + x**4/24          # alternating series upper bound
cos_lo = 1 - x**2/2                    # lower bound (next term positive minus smaller)
sin_lo = x - x**3/6
sin_up = x - x**3/6 + x**5/120
print("cos(5/8) upper", cos_up, "=", cos_up*98304, "/98304 < 13/16:", cos_up < Fr(13, 16))
print("cos(5/8) lower 103/128 <= 1-x^2/2:", Fr(103, 128) <= cos_lo)
print("sin(5/8) lower", sin_lo, "> 1/2:", sin_lo > Fr(1, 2), "; upper", sin_up, "< 3/5:", sin_up < Fr(3, 5))
print("743/1536 = 1/2 - (5/8)^2/24:", Fr(1, 2) - x**2/24 == Fr(743, 1536), "; 1536*4*c<=6144<6687:", 6144 < 6687)
S = lambda u: 2*math.sqrt(2*u - u*u)
print("S(3/16)=sqrt87/8=%.6f <6/5; S'(3/16)=26/sqrt87=%.6f <3" % (S(3/16), 26/math.sqrt(87)))

# (b),(c)
def env(n):
    pi = math.pi; m = n + 1; L = math.log(n); H = 1 + L
    a0, w0, p0, P0, eta = 13/16, 29/16, 3/5, 6/5, 1.5
    b = 4/pi**2; hr = math.log(2.5) + 1/18
    Da = ((52/pi**2)*H + 7)/n + 20*H/(pi*n**2)
    KD = ((6 + 16/(3*pi))*H + 2/pi)/n
    eps = 3*pi/(2*m); ell = -math.log(math.sin(eps))
    W = (3*math.log(m) + math.log(2) + 2*math.log(pi) + 2)/(pi*m)
    C = 1 + 8*a0*m/(3*pi)
    Gb = p0*(1 + math.log(1 + C/p0)); gb = 1 + math.log(1 + C/p0) - C/(p0 + C)
    MAb = p0/pi + a0*b
    VBb = 23 + (3*Gb + (2*p0 + 6*P0)*ell + 26*a0 + 20)/pi
    CBb = 6 + (4 + 4*a0/math.e)/pi
    Genv = 7*L*MAb/m + VBb/(2*m) + (4/m)*(7 + (P0/pi)*(5 + 2*math.log(2*m))) + 2*CBb/m
    Denv = a0*Da + 10/n**2
    R6 = (21 + 21*a0 + 2*L + ((1 + 48*p0)*H + 24*p0)/pi)/n + (317 + 5/12)/n**2
    Dm = 4*w0/pi + a0*b*math.log(pi); Zm = Dm + a0*b/n
    Menv = (a0*b*(2*L + 2*hr)/n + (Dm + a0*b*(L + 1/n))/(4*n**2 - 1) + a0*b/(2*n - 1)**2
            + (Zm + a0*b*(math.log(n + .5) + 2))/(4*(n - .5)**2))
    Cb = Denv + Genv + R6 + Menv
    Cs = eta*(7*L/(pi*m) + (3*gb + 2*ell)/(2*pi*m) + (48*H + 24)/(pi*n)) + 3*((math.log(2) + 4*math.log(pi))/(pi*m) + W)
    Cl = (9*ell + 12*(5 + 2*math.log(2*m)))/(pi*m)
    def CE(xp, yp):
        p, q = math.sin(xp), math.sin(yp); P = p + q; d = max(q - p, 0)
        ce, cd = math.cos((xp + yp)/2), math.cos((xp - yp)/2); a = ce*cd
        Gam = 0.0 if p == 0 else p*(1 + math.log(1 + (1 + 8*a*m/(3*pi))/p))
        MA = max(p, q)/pi + 4*a/pi**2
        VB = 23 + (3*Gam + (2*p + 6*P)*ell + 26*a + 20 + 2*d*math.log(2))/pi
        CB = 6 + (4 + 4*a/math.e)/pi
        Gphi = 7*L*MA/m + VB/(2*m) + (4/m)*(7 + (P/pi)*(5 + 2*math.log(2*m))) + 4*d*math.log(pi)/(pi*m) + 2*CB/m
        C6 = (21 + 21*a + 2*L + ((1 + 48*p)*H + 24*q)/pi)/n + (317 + 5/12)/n**2
        Dphi = a*Da + 10/n**2
        Dbar = 4*(ce + cd)/pi + a*b*math.log(pi); Zbar = Dbar + a*b/n
        Mphi = (a*b*(2*L + 2*hr)/n + (Dbar + a*b*(L + 1/n))/(4*n**2 - 1) + a*b/(2*n - 1)**2
                + (Zbar + a*b*(math.log(n + .5) + 2))/(4*(n - .5)**2))
        return Dphi + Gphi + C6 + Mphi + d*W + KD*P, (p, q, P, d, a)
    return Cb, Cs, Cl, KD, CE

worst = {}
for n in (32, 33, 64, 128, 256, 257, 1000, 10**5):
    Cb, Cs, Cl, KD, CE = env(n)
    g1 = g2 = g3 = g4 = -1e9
    N = 500
    for i in range(N + 1):
        rho = 1.25 + (math.pi - 1.25)*i/N
        for k in range(N + 1):
            xp = rho*k/N; yp = rho - xp
            val, (p, q, P, d, a) = CE(xp, yp)
            v = (1 - a) - 3/16
            sv = math.sqrt(max(v, 0))
            g1 = max(g1, max(p, q) - (0.6 + 1.5*sv))
            g2 = max(g2, abs(p - q) - 3*sv)
            g3 = max(g3, P - (1.2 + 3*v))
            g4 = max(g4, val - (Cb + 1.2*KD + Cs*sv + (Cl + 3*KD)*v))
    print(f"n={n}: max[p,q - cap]={g1:.4g}  max[|p-q|-3sqrt v]={g2:.4g}  max[P-(6/5+3v)]={g3:.4g}  max[CE+KD P - envelope]={g4:.4g}  (all must be <=0)")
