#!/usr/bin/env python3
"""[E] F08-entropy-constant-kernel: exact translated midpoint/hole moments.
Checks (1) exact M formula, (2),(3) bounds, sharpness of 1/4; (4) exact hole moment,
(5) exterior-hole bound, sharpness 1/2 (E=P(ell) at r=0); symbolic A(theta), A0(zeta) by sympy.
Usage: PYTHONPATH=<pylib> python3 f08_kernel_check.py
"""
import random
import sympy as sp
from mpmath import mp, mpf, log, quad, fabs, nstr, pi

mp.dps = 30
f = lambda r: (lambda x: mpf(0) if x == r else fabs(x - r)*log(fabs(x - r)))
P = lambda y: mpf(0) if y == 0 else y**2/2*log(y) - y**2/4

# symbolic: coefficient of log h and of log ell
th, z = sp.symbols('theta zeta', nonnegative=True)
A_sym = sp.expand(th - (sp.Rational(1, 4) + th**2))
print("A(theta) for theta>=0:", sp.factor(A_sym), " == -(1/2-theta)^2:", sp.simplify(A_sym + (sp.Rational(1, 2) - th)**2) == 0)
A0_sym = sp.expand((z**2 + (1 - z)**2)/2 - z)
print("A0(zeta):", A0_sym, " == (1-zeta)^2-1/2:", sp.simplify(A0_sym - ((1 - z)**2 - sp.Rational(1, 2))) == 0)

random.seed(8)
dev1 = 0; ratio2 = 0; ratio3 = 0
for _ in range(40):
    h = mpf(10)**mpf(random.uniform(-6, -0.5)); c = mpf(random.uniform(-1, 1))
    t = mpf(random.uniform(-0.5, 0.5)); r = c + t*h
    M = h*f(r)(c) - quad(f(r), [c - h/2, r, c + h/2])
    A = -(mpf(1)/2 - fabs(t))**2
    B = (fabs(t)*log(fabs(t)) if t != 0 else 0) - P(mpf(1)/2 + t) - P(mpf(1)/2 - t)
    dev1 = max(dev1, fabs(M - h**2*(A*log(h) + B))/h**2)
    ratio2 = max(ratio2, fabs(M)/(h**2*(fabs(log(h))/4 + mpf(1)/2)))
    # exterior root
    te = mpf(random.choice([-1, 1]))*mpf(random.uniform(0.5, 30)); re = c + te*h
    Me = h*f(re)(c) - quad(f(re), [c - h/2, c + h/2])
    ratio3 = max(ratio3, fabs(Me)/(h**2*(log(2)/2 - mpf(1)/4)))
print("cell: max |M - h^2(A log h + B)|/h^2 =", nstr(dev1, 5), "; max |M|/bound(2) =", nstr(ratio2, 5), "; max |M_ext|/((log2)/2-1/4)h^2 =", nstr(ratio3, 6), "(<=1)")
h = mpf('1e-12'); M0 = h*0 - quad(f(mpf(0)), [-h/2, 0, h/2])
print("sharpness at r=c: M/(h^2 |log h|) =", nstr(M0/(h**2*fabs(log(h))), 6), "(-> -1/4 as h->0; B(0)=", nstr(-2*P(mpf(1)/2), 6), ")")

dev4 = 0; ratio4 = 0; ratio5 = 0
for _ in range(40):
    ell = mpf(10)**mpf(random.uniform(-6, 0)); zeta = mpf(random.uniform(0, 1)); r = ell*zeta
    E = quad(lambda x: f(r)(x) - f(r)(0), [0, r, ell])
    A0 = (1 - zeta)**2 - mpf(1)/2; B0 = P(zeta) + P(1 - zeta) - (zeta*log(zeta) if zeta > 0 else 0)
    dev4 = max(dev4, fabs(E - ell**2*(A0*log(ell) + B0))/ell**2)
    ratio4 = max(ratio4, fabs(E)/(ell**2*(fabs(log(ell))/2 + mpf(1)/2)))
    for re in (mpf(random.uniform(-3.14159, 0)), ell + mpf(random.uniform(0, 3.14159 - float(ell))), -ell*mpf('1e-3'), ell*(1 + mpf('1e-3'))):
        Ee = quad(lambda x: f(re)(x) - f(re)(0), [0, ell])
        ratio5 = max(ratio5, fabs(Ee)/(ell**2*(log(1/ell)/2 + mpf(5)/2)))
print("hole: max |E - ell^2(A0 log ell + B0)|/ell^2 =", nstr(dev4, 5), "; max |E|/bound(4) =", nstr(ratio4, 5), "; max |E_ext|/bound(5) =", nstr(ratio5, 5), "(<=1)")
ell = mpf('1e-3'); E0 = quad(lambda x: f(mpf(0))(x), [0, ell])
print("hole sharpness r=0: E - P(ell) =", nstr(E0 - P(ell), 5))
