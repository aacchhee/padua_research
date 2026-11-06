#!/usr/bin/env python3
"""Audit A: contour geometry and a direct numerical reproduction of the
inverse-jet formula (8) with the source split (6)-(7) of c2-sharp-upper.md.

For random mixed directions (all nodes and both weight vectors moving at
once) the top three Bernstein coefficients of R=B_M dot P (exact Fractions)
are compared with
  -[ sum_s (1/2pi i) oint_{Gamma_s} (f_s - ell_s f) h_{j-1}/D
     + (1/2pi i) oint_{Gamma_0} (g + ell f) h_{j-1}/D ]
evaluated by mpmath quadrature on the stated rectangles and circle.
Independent of repository code.
"""
import sys, json, random
from fractions import Fraction as Fr
from math import comb, factorial
import mpmath as mp

mp.mp.dps = 30
RHO = 5 + 2 * mp.sqrt(6)
c = mp.sqrt(6) - 2
p1, p2 = mp.mpf(2) / 5, mp.mpf(1) / 2

def fm(x):
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, Fr) else mp.mpf(x)

def solve_multi(A, Bs):
    n = len(A)
    if n == 0:
        return [[] for _ in Bs]
    rows = [list(A[i]) + [B[i] for B in Bs] for i in range(n)]
    for j in range(n):
        piv = next(i for i in range(j, n) if rows[i][j] != 0)
        rows[j], rows[piv] = rows[piv], rows[j]
        d = rows[j][j]
        rows[j] = [v / d for v in rows[j]]
        for i in range(n):
            if i != j and rows[i][j] != 0:
                f = rows[i][j]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[j])]
    return [[rows[i][n + r] for i in range(n)] for r in range(len(Bs))]

def peval(cf, x):
    return sum(cr * x**r for r, cr in enumerate(cf))

def rect(x0, x1, y0, y1, n):
    pts = []
    corners = [mp.mpc(x0, y0), mp.mpc(x1, y0), mp.mpc(x1, y1), mp.mpc(x0, y1)]
    for a, b in zip(corners, corners[1:] + corners[:1]):
        for i in range(n):
            pts.append(a + (b - a) * mp.mpf(i) / n)
    return pts

def geometry():
    out = {}
    n = 4000
    G1 = rect(-1, c, -1, 1, n); G2 = rect(c, 2, -1, 1, n)
    def A1(u): return mp.mpf(2) / 5 * abs(1 - u) + mp.mpf(3) / 5 * abs(u)
    def A2(u): return (abs(u) + abs(1 - u)) / 2
    r1 = max(A1(u) / abs(u - p1) for u in G1 + G2)
    r2 = max(A2(u) / abs(u - p2) for u in G1 + G2)
    S = max(abs(u) + abs(1 - u) for u in G1 + G2)
    zeta_max = max(abs(u) for u in G1 + G2)
    out['Gamma1uGamma2'] = dict(max_A1_over_dist=mp.nstr(r1, 15), max_A2_over_dist=mp.nstr(r2, 15),
                                rho=mp.nstr(RHO, 15), max_S=mp.nstr(S, 10), max_abs_zeta=mp.nstr(zeta_max, 10),
                                at_c_A1=mp.nstr(A1(mp.mpc(c, 0)) / abs(c - p1), 20),
                                at_c_A2=mp.nstr(A2(mp.mpc(c, 0)) / abs(c - p2), 20),
                                length_over_2pi=mp.nstr((2 * (c + 1) + 4 + 2 * (2 - c) + 4) / (2 * mp.pi), 10))
    # finer check near the shared side
    ys = [mp.mpf(i) / 20000 - mp.mpf(1) / 2 for i in range(20001)]
    out['shared_side_max'] = mp.nstr(max(max(A1(mp.mpc(c, y)) / abs(mp.mpc(c, y) - p1), A2(mp.mpc(c, y)) / abs(mp.mpc(c, y) - p2)) for y in ys), 20)
    cen, rad = mp.mpf(9) / 20, mp.mpf(2) / 5
    G0 = [cen + rad * mp.expj(2 * mp.pi * i / 20000) for i in range(20000)]
    ell = lambda u: mp.log(u) - mp.log(1 - u)
    out['Gamma0'] = dict(max_abs_u=mp.nstr(max(abs(u) for u in G0), 10), max_abs_1mu=mp.nstr(max(abs(1 - u) for u in G0), 10),
                         min_dist_p1=mp.nstr(min(abs(u - p1) for u in G0), 10), min_dist_p2=mp.nstr(min(abs(u - p2) for u in G0), 10),
                         max_abs_ell=mp.nstr(max(abs(ell(u)) for u in G0), 10),
                         max_S=mp.nstr(max(abs(u) + abs(1 - u) for u in G0), 10),
                         max_A1=mp.nstr(max(A1(u) for u in G0), 10), max_A2=mp.nstr(max(A2(u) for u in G0), 10))
    return out

def poly_data(N, nu):
    M = N - 1
    ps = (Fr(2, 5), Fr(1, 2))
    w = [[Fr(comb(M, k)) * p**k * (1 - p)**(M - k) for k in range(N)] for p in ps]
    nc = 3 * N
    t = sum(nu)
    mu = [[sum(w[s][k] * Fr(k)**r for k in range(N)) for r in range(2 * N + 2)] for s in range(2)]
    def dmu(s, r, i):
        if i < N:
            return w[s][i] * r * Fr(i)**(r - 1) if r else Fr(0)
        ss, l = divmod(i - N, N)
        return w[s][l] * Fr(l)**r if ss == s else Fr(0)
    rows = [(s, j) for s in range(2) for j in range(nu[s])]
    A = [[mu[s][j + r] for r in range(t)] for s, j in rows]
    cf = solve_multi(A, [[-mu[s][j + t] for s, j in rows]])[0] + [Fr(1)]
    rhs = [[-sum(dmu(s, j + r, i) * cf[r] for r in range(t + 1)) for s, j in rows] for i in range(nc)]
    dc = [d + [Fr(0)] for d in solve_multi(A, rhs)]
    return cf, dc

def bernstein_power(vals, M):
    return [sum(Fr(comb(M, k) * comb(M - k, r - k) * (-1)**(r - k)) * vals[k] for k in range(r + 1)) for r in range(M + 1)]

def reproduce(N, nu, rng):
    M = N - 1; t = sum(nu); n, m = nu
    cf, dc = poly_data(N, nu)
    # random mixed direction in the box: xi in [-M/2,M/2], eta in [-1,1]
    xi = [Fr(rng.randint(-1000, 1000), 2000) * M for _ in range(N)]
    eta = [[Fr(rng.randint(-1000, 1000), 1000) for _ in range(N)] for _ in range(2)]
    coords = xi + eta[0] + eta[1]
    ddir = [sum(coords[i] * dc[i][r] for i in range(3 * N)) for r in range(t + 1)]
    R = bernstein_power([peval(ddir, Fr(k)) for k in range(N)], M)
    assert all(x == 0 for x in R[t:])
    Pk = [fm(peval(cf, Fr(k))) for k in range(N)]
    dP = [r * cf[r] for r in range(1, len(cf))]
    Ppk = [fm(peval(dP, Fr(k))) for k in range(N)]
    xim = [fm(x) for x in xi]; etam = [[fm(x) for x in e] for e in eta]
    def Bz(arr, z):
        return sum(comb(M, k) * arr[k] * z**k * (1 - z)**(M - k) for k in range(N))
    def D(z):
        return (z - p1)**n * (z - p2)**m
    # coefficients d_i of D
    Dc = [mp.mpf(1)]
    for root, mult in ((p1, n), (p2, m)):
        for _ in range(mult):
            Dc = [0] + Dc
            for r in range(len(Dc) - 1):
                Dc[r] -= root * Dc[r + 1]
    d = [Dc[t - i] for i in range(t + 1)]
    def hj(j, z):
        return sum(d[i] * z**(j - 1 - i) for i in range(j))
    ell = lambda z: mp.log(z) - mp.log(1 - z)
    ells = [mp.log(p1 / (1 - p1)), mp.mpf(0)]
    def seg_int(F, a, b):
        return mp.quad(lambda s: F(a + (b - a) * s) * (b - a), [0, 1])
    def rect_int(F, x0, x1):
        corners = [mp.mpc(x0, -1), mp.mpc(x1, -1), mp.mpc(x1, 1), mp.mpc(x0, 1)]
        return sum(seg_int(F, a, b) for a, b in zip(corners, corners[1:] + corners[:1]))
    def circ_int(F):
        cen, rad = mp.mpf(9) / 20, mp.mpf(2) / 5
        return mp.quad(lambda th: F(cen + rad * mp.expj(th)) * 1j * rad * mp.expj(th), [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
    fx = [Pk[k] * xim[k] for k in range(N)]
    gx = [Ppk[k] * xim[k] for k in range(N)]
    res = []
    for j in range(1, min(3, t) + 1):
        tot = 0
        for s, (x0, x1) in enumerate(((-1, c), (c, 2))):
            fs = [Pk[k] * etam[s][k] for k in range(N)]
            F = lambda z, s=s, fs=fs: (Bz(fs, z) - ells[s] * Bz(fx, z)) * hj(j, z) / D(z)
            tot += rect_int(F, x0, x1) / (2j * mp.pi)
        Gf = lambda z: (Bz(gx, z) + ell(z) * Bz(fx, z)) * hj(j, z) / D(z)
        tot += circ_int(Gf) / (2j * mp.pi)
        exact = fm(R[t - j])
        err = abs(-tot - exact) / max(1, abs(exact))
        res.append(float(err))
    return res

def pointwise(N):
    """(5)/(11) on Gamma1uGamma2 and (14) on Gamma0, sup over the direction box."""
    M = N - 1
    worst11 = 0; worst14 = 0; worst5 = 0
    G12 = rect(-1, c, -1, 1, 60) + rect(c, 2, -1, 1, 60)
    cen, rad = mp.mpf(9) / 20, mp.mpf(2) / 5
    G0 = [cen + rad * mp.expj(2 * mp.pi * i / 240) for i in range(240)]
    ell = lambda z: mp.log(z) - mp.log(1 - z)
    HM = sum(mp.mpf(1) / i for i in range(1, M + 1))
    for t in range(1, M + 1):
        for n in range(t + 1):
            nu = (n, t - n); m = t - n; L = M - t
            cf, _ = poly_data(N, nu)
            Mt = mp.mpf(factorial(M)) / factorial(M - t)
            v = [comb(M, k) * fm(peval(cf, Fr(k))) for k in range(N)]
            dP = [r * cf[r] for r in range(1, len(cf))]
            vp = [comb(M, k) * fm(peval(dP, Fr(k))) for k in range(N)]
            for z in G12:
                maj = sum(abs(v[k]) * abs(z)**k * abs(1 - z)**(M - k) for k in range(N))
                S = abs(z) + abs(1 - z); A1 = mp.mpf(2) / 5 * abs(1 - z) + mp.mpf(3) / 5 * abs(z); A2 = S / 2
                worst5 = max(worst5, maj / (Mt * S**L * A1**n * A2**m))
                D = abs(z - p1)**n * abs(z - p2)**m
                worst11 = max(worst11, maj / D / (Mt * 5**L * RHO**t))
            for z in G0:
                D = abs(z - p1)**n * abs(z - p2)**m
                G = mp.mpf(M) / 2 * sum(abs(vp[k] + ell(z) * v[k]) * abs(z)**k * abs(1 - z)**(M - k) for k in range(N))
                worst14 = max(worst14, G / D / (mp.mpf(M) / 2 * (3 * HM + 7) * Mt * (mp.mpf(19) / 10)**L * (mp.mpf(19) / 7)**t))
    return dict(N=N, max_ratio_5=mp.nstr(worst5, 8), max_ratio_11=mp.nstr(worst11, 8), max_ratio_14=mp.nstr(worst14, 8))

if __name__ == '__main__':
    for N in (2, 3, 5, 8, 10):
        print(json.dumps(pointwise(N)), flush=True)
