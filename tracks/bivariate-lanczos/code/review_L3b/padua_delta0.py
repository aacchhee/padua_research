"""Reviewer (L3 reconstruction 02): rigorous explicit positivity radius delta_0(n) for the Padua
certificate P_n of PD-T?...-313 (the radius needed by PD-T?...-303(e) / PD-N?...-303).

At each Padua node z (certified rational interval enclosure), the exact Taylor expansion
P_n(z + h) = (1/2) h^T H h + sum_{k=3}^{2n+1} P_k(h) is enclosed coefficientwise by an interval
Taylor shift. With S_k := sum over |gamma| = k of an upper bound of |c_gamma| and
lam := det(H)/tr(H) (a lower bound of lambda_min(H) for PD H, from rigorous intervals):
    P_n(z + h) >= |h|^2 ( lam/2 - sum_k S_k |h|^{k-2} )   (|h_1|, |h_2| <= |h|).
r(z) := a rational radius at which the bracket is certified > 0 (exact Fraction check); the bracket
is decreasing in |h|, so P_n > 0 on the punctured disc of radius r(z). delta_0(n) >= min_z r(z).
Usage: python3 -I padua_delta0.py nmin nmax
"""
import sys
import os
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rigorous import Iv, certified_cos_nodes          # noqa: E402
from padua_turan_check import certificate, scal, padua_nodes, node_class  # noqa: E402  (reviewer's own)


def taylor_shift_univ(coeffs, z0):
    c = list(coeffs)
    d = len(c) - 1
    for i in range(d):
        for j in range(d - 1, i - 1, -1):
            c[j] = c[j] + z0 * c[j + 1]
    return c


def taylor_coeffs(pdict, x0, y0):
    D = max(a + b for (a, b) in pdict)
    # rows by y-power b: polynomial in x
    rows = {}
    for (a, b), cf in pdict.items():
        rows.setdefault(b, [Iv(0)] * (D + 1))
        rows[b][a] = Iv(cf)
    shifted = {b: taylor_shift_univ(r, x0) for b, r in rows.items()}   # coefficient of h1^a y^b
    out = {}
    for a in range(D + 1):
        col = [shifted[b][a] if b in shifted else Iv(0) for b in range(D + 1)]
        col = taylor_shift_univ(col, y0)
        for b, v in enumerate(col):
            if a + b <= D:
                out[(a, b)] = v
    return out, D


def absup(v):
    return max(abs(v.lo), abs(v.hi))


def radius(lam, S, D):
    def f(r):
        return lam / 2 - sum(S[k] * r ** (k - 2) for k in range(3, D + 1))
    lo, hi = Fr(0), Fr(1)
    if f(hi) > 0:
        return hi
    for _ in range(60):
        mid = (lo + hi) / 2
        mid = Fr(int(mid * 2 ** 40), 2 ** 40)
        if mid <= lo:
            break
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    assert lo == 0 or f(lo) > 0
    return lo


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    print("padua_delta0.py: rigorous positivity radius of P_n around Padua nodes", flush=True)
    for n in range(nmin, nmax + 1):
        t0 = time.time()
        Pc, _ = certificate(n)
        Pn = scal(10, Pc)
        X, Y = certified_cos_nodes(n), certified_cos_nodes(n + 1)
        rmin = None
        for (j, k) in padua_nodes(n):
            tc, D = taylor_coeffs(Pn, X[j], Y[k])
            # zero and gradient enclosures must contain 0 (sanity)
            for g in ((0, 0), (1, 0), (0, 1)):
                assert tc[g].lo <= 0 <= tc[g].hi
            a = tc[(2, 0)] * 2; bxy = tc[(1, 1)]; d = tc[(0, 2)] * 2   # Hessian entries
            det = a * d - bxy * bxy; tr = a + d
            assert det.lo > 0 and a.lo > 0
            lam = det.lo / tr.hi
            S = {kk: sum(absup(tc[(al, kk - al)]) for al in range(kk + 1)) for kk in range(3, D + 1)}
            r = radius(lam, S, D)
            if rmin is None or r < rmin[0]:
                rmin = (r, j, k, node_class(n, j, k))
        print(f"n={n:2d}: certified delta_0(n) >= {float(rmin[0]):.4e} = {rmin[0]} (binding node (j,k)=({rmin[1]},{rmin[2]}) [{rmin[3]}])  ({time.time()-t0:.1f}s)", flush=True)
        print(f"       MEASURED (float sampling, 720 directions, radii geometric): first radius with min P_n < 0 on the circle: {sampled_radius(n):.3e}", flush=True)


def sampled_radius(n):
    """MEASURED only: smallest sampled radius r at which P_n < 0 somewhere on the circle |h| = r around
    some Padua node (Chebyshev evaluation of g_m in double precision)."""
    import numpy as np
    from numpy.polynomial import chebyshev as Ch

    def T(k, z):
        cc = np.zeros(k + 1); cc[k] = 1
        return Ch.chebval(z, cc)

    def P(xx, yy):
        g = [T(n - m, xx) * T(m, yy) - T(m, xx) * T(n + 1 - m, yy) for m in range(4)]
        return 9 * (g[1] ** 2 - 0.5 * g[0] * g[2]) + (g[2] ** 2 - g[1] * g[3])
    ang = np.linspace(0, 2 * np.pi, 720, endpoint=False)
    nodes = [(np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1))) for (j, k) in padua_nodes(n)]
    for r in np.geomspace(1e-4, 0.5, 200):
        for (x0, y0) in nodes:
            if np.min(P(x0 + r * np.cos(ang), y0 + r * np.sin(ang))) < 0:
                return r
    return float('inf')


if __name__ == '__main__':
    main()
