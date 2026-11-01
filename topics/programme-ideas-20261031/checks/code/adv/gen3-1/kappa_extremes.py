"""Adversarial probe 3 for gen3-draft-1: kappa up to the last finite degree D-1 for the two
non-Chebyshev families that showed mild growth (phase-shifted Lissajous, rhodonea vs disk),
and the "diagonal" scaling kappa_{D-2}, kappa_{D-1} as the curve's trig degree grows.
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). 2026-11-01.
Scope: M = 4096 samples, n <= 13 (2 m n < 2048 holds for all cases), double precision; kappa
values above ~1e9 are not resolved. Reuses curve_kappa_adv.py.
"""
import numpy as np, math
import curve_kappa_adv as P

def kap(curve, nmax, ref):
    return [r[5] for r in P.kappa_table(curve, nmax, ref)]

print("# Phase-shifted Lissajous (cos n1 t, cos(n2 t + phi)), traced once, D = 2 max(n1,n2); kappa vs square, n = 0..D-1")
for (n1, n2) in ((5, 6), (6, 7)):
    for phi in (0.05, 0.5, 1.0, np.pi/2):
        f, m, tau = P.lissajous(n1, n2, phi); D = 2*m
        ks = kap(f, min(D-1, 13), "square")
        print(f"  ({n1},{n2}) phi={phi:.2f}: D={D}: ", " ".join("%.2e" % k for k in ks))

print("\n# Rhodonea r = cos(k theta), k odd (D = k+1): kappa vs disk at n = D-3, D-2, D-1; and vs square")
for k in (3, 5, 7, 9, 11, 13):
    f, m, tau = P.rhodonea(k); D = k+1
    kd = kap(f, D-1, "disk"); ks = kap(f, D-1, "square")
    print(f"  k={k:>2} D={D:>2}: disk  kappa_(D-3,D-2,D-1) = {kd[D-3]:.2e} {kd[D-2]:.2e} {kd[D-1]:.2e} | square {ks[D-3]:.2e} {ks[D-2]:.2e} {ks[D-1]:.2e}")

print("\n# Epitrochoid x=cos t - d cos kt (D = 2k): kappa vs disk at n = k-1, k, k+1 (half-degree regime) and D-1")
for k, d in ((4, .5), (6, .5), (8, .5), (10, .5), (12, .5)):
    f, m, tau = P.epitrochoid(k, d); D = 2*k
    nmax = min(D-1, 13)
    kd = kap(f, nmax, "disk")
    tail = f"{kd[D-1]:.2e}" if D-1 <= 13 else "n/a(>13)"
    print(f"  k={k:>2} D={D:>2}: disk kappa_(k-1,k,k+1) = {kd[k-1]:.2e} {kd[k]:.2e} {kd[k+1]:.2e} ; kappa_(D-1) = {tail}")

print("\n# Generic trig curves rescaled to the square (random, decaying coefficients): kappa vs square at n = m-1, m, 2m-1")
for m, seed in ((3, 1), (4, 2), (5, 3), (6, 4)):
    f, mm, tau = P.generic_trig(m, seed=seed); D = 2*m
    ks = kap(f, D-1, "square")
    print(f"  m={m} D={D}: kappa_(m-1,m) = {ks[m-1]:.2e} {ks[m]:.2e}; kappa_(D-1) = {ks[D-1]:.2e}; Dubiner radius (square) = {P.dubiner_radius(f,'square'):.2f}")
