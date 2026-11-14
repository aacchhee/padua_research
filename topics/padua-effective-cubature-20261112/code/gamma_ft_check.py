"""Independent numerical check (MEASURED) of the exact Fourier transform used by
gamma_certificate.py: compare G(u) e^{-pi|u|^2} with direct Gauss-Hermite quadrature of
int P(x) e^{-pi|x|^2} cos(2 pi u.x) dx at sample points u (mpmath, 60 digits).
Usage: python3 -B gamma_ft_check.py --anc PATH/octa_double.func.cpp
"""
import argparse, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import mpmath as mp
import gamma_certificate as g

ap = argparse.ArgumentParser(); ap.add_argument("--anc", required=True); a = ap.parse_args()
mp.mp.dps = 60
C, sha = g.read_coeffs(a.anc); P = g.P_in_y(C); G = g.G_in_y(P, g.T_tables(13))
# 1-D moments I_a(u) = int x^(2a) e^{-pi x^2} cos(2 pi u x) dx by Gauss-Hermite (weight e^{-t^2}, x = t/sqrt(pi))
nodes = 120
X, W = mp.gauss_hermite(nodes) if hasattr(mp, "gauss_hermite") else (None, None)
if X is None:
    import numpy as np
    t, w = np.polynomial.hermite.hermgauss(nodes)
    X = [mp.mpf(v) for v in t]; W = [mp.mpf(v) for v in w]
def I(aexp, u):
    return sum(w * (x / mp.sqrt(mp.pi)) ** (2 * aexp) * mp.cos(2 * mp.pi * u * x / mp.sqrt(mp.pi))
               for x, w in zip(X, W)) / mp.sqrt(mp.pi)
worst = 0
for u in [(0, 0, 0), (0.3, 0, 0), (0.2, 0.5, 0.7), (1, 1, 0.5), (0.05, 1.3, 1.48), (1.5, 0.2, 0.9)]:
    u = [mp.mpf(v) for v in u]
    tab = {(i, k): I(k, u[i]) for i in range(3) for k in range(14)}
    quad = sum(mp.mpf(c.numerator) / c.denominator * tab[(0, k[0])] * tab[(1, k[1])] * tab[(2, k[2])]
               for k, c in P.items())
    exact = sum(g.pi_poly_to_mp(d, mp) * (u[0] ** 2) ** k[0] * (u[1] ** 2) ** k[1] * (u[2] ** 2) ** k[2]
                for k, d in G.items()) * mp.e ** (-mp.pi * (u[0] ** 2 + u[1] ** 2 + u[2] ** 2))
    rel = abs(quad - exact) / max(abs(exact), mp.mpf(10) ** -30)
    worst = max(worst, rel)
    print([float(v) for v in u], mp.nstr(exact, 15), mp.nstr(quad, 15), "rel diff", mp.nstr(rel, 3))
print("worst relative difference", mp.nstr(worst, 3))
