#!/usr/bin/env python3
"""Audit A: exact/high-precision checks of the intermediate lemmas of
c2-sharp-upper.md in the integer node variable k (nodes 0..M).

Exact Fractions for polynomials, derivatives and Bernstein coefficients;
mpmath only for the logit constant ell_1=log(2/3) and box-sup ratios.
Independent of repository code.
"""
import sys, json, math
from fractions import Fraction as Fr
from math import comb, factorial
import mpmath as mp

mp.mp.dps = 50
RHO = 5 + 2 * mp.sqrt(6)
ELL1 = mp.log(mp.mpf(2) / 3)

def fm(x):
    if isinstance(x, Fr):
        return mp.mpf(x.numerator) / x.denominator
    return mp.mpf(x)

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

def peval(c, x):  # c[r] coefficient of x^r
    return sum(cr * x**r for r, cr in enumerate(c))

def pder(c):
    return [r * c[r] for r in range(1, len(c))]

def bernstein_power(vals, M):
    """power-basis coefficients in u of sum_k binom(M,k) vals[k] u^k (1-u)^(M-k)"""
    return [sum(Fr(comb(M, k) * comb(M - k, r - k) * (-1)**(r - k)) * vals[k] for k in range(r + 1)) for r in range(M + 1)]

def taylor(c, p, order):  # first `order` Taylor coefficients at p
    return [sum(c[i] * comb(i, r) * p**(i - r) for i in range(r, len(c))) for r in range(order)]

def run(N):
    M = N - 1
    ps = (Fr(2, 5), Fr(1, 2))
    w = [[Fr(comb(M, k)) * p**k * (1 - p)**(M - k) for k in range(N)] for p in ps]
    nc = 3 * N
    # box scales in k variable: |xi_l|<=M/2, |eta|<=1  (eta coordinate = dot w/w)
    scale = [Fr(M, 2)] * N + [Fr(1)] * (2 * N)
    Rm = 2 * N + 2
    mu = [[sum(w[s][k] * Fr(k)**r for k in range(N)) for r in range(Rm)] for s in range(2)]
    def dmu(s, r, i):
        if i < N:
            return w[s][i] * r * Fr(i)**(r - 1) if r else Fr(0)
        ss, l = divmod(i - N, N)
        return w[s][l] * Fr(l)**r if ss == s else Fr(0)
    C = 1000 * N**9 * RHO**M
    worst = {}
    def upd(key, val):
        val = fm(val)
        if key not in worst or val > worst[key][0]:
            worst[key] = (val, N)
    poly = {}
    HM = sum(Fr(1, j) for j in range(1, M + 1))
    for t in range(0, N + 1):
        for n in range(t + 1):
            nu = (n, t - n); m = t - n
            rows = [(s, j) for s in range(2) for j in range(nu[s])]
            A = [[mu[s][j + r] for r in range(t)] for s, j in rows]
            v = [-mu[s][j + t] for s, j in rows]
            c = solve_multi(A, [v])[0] + [Fr(1)]
            rhs = [[-sum(dmu(s, j + r, i) * c[r] for r in range(t + 1)) for s, j in rows] for i in range(nc)]
            dc = [d + [Fr(0)] for d in solve_multi(A, rhs)]
            poly[nu] = (c, dc)
            # top coefficients c_j = coeff of k^(t-j)
            cj = [c[t - j] if j <= t else Fr(0) for j in range(4)]
            dcj = [[dc[i][t - j] if j <= t else Fr(0) for i in range(nc)] for j in range(4)]
            if t == N:
                # terminal support polynomial and its node derivative
                supp = [Fr(1)]
                for l in range(N):
                    supp = [Fr(0)] + supp
                    for r in range(len(supp) - 1):
                        supp[r] -= l * supp[r + 1]
                assert c == supp
                for i in range(nc):
                    if i < N:
                        q = [Fr(1)]
                        for l in range(N):
                            if l != i:
                                q = [Fr(0)] + q
                                for r in range(len(q) - 1):
                                    q[r] -= l * q[r + 1]
                        assert dc[i] == [-qq for qq in q] + [Fr(0)]
                    else:
                        assert all(d == 0 for d in dc[i])
                for j in (1, 2, 3):
                    sup = sum(abs(dcj[j][i]) * scale[i] for i in range(nc))
                    upd('terminal_dc%d/(N^%d/2)' % (j, 2 * j), sup / (Fr(N**(2 * j), 2)))
                continue
            for j in (1, 2, 3):
                if j <= t:
                    upd('|c%d|/((j+1)N^2j)' % j, abs(cj[j]) / ((j + 1) * N**(2 * j)))
                    sup = sum(abs(dcj[j][i]) * scale[i] for i in range(nc))
                    upd('sup dc%d/(600N^(2j+3)rho^M)' % j, fm(sup) / (600 * N**(2 * j + 3) * RHO**M))
                    upd('sup dc%d/C' % j, fm(sup) / C)
            if t == 0:
                continue
            # (3): Bernstein of P equals (M)_t D
            Mt = Fr(factorial(M), factorial(M - t))
            pv = [peval(c, Fr(k)) for k in range(N)]
            Q = bernstein_power(pv, M)
            D = [Fr(1)]
            for root, mult in ((ps[0], n), (ps[1], m)):
                for _ in range(mult):
                    D = [Fr(0)] + D
                    for r in range(len(D) - 1):
                        D[r] -= root * D[r + 1]
            assert Q == [Mt * d for d in D] + [Fr(0)] * (M - t), (N, nu)
            # (12) weighted differentiation identity
            vk = [comb(M, k) * pv[k] for k in range(N)]
            ppv = [peval(pder(c), Fr(k)) for k in range(N)]
            H = lambda r: sum((Fr(1, i) for i in range(1, r + 1)), Fr(0))
            for k in range(N):
                pred = (H(k) - H(M - k)) * vk[k] + sum(Fr((-1)**abs(j - k), k - j) * vk[j] for j in range(N) if j != k)
                assert comb(M, k) * ppv[k] == pred
            # (13)
            upd('(13) sum|binom P\'|/(3H_M (M)_t 2^L)', sum(abs(comb(M, k) * ppv[k]) for k in range(N)) / (3 * HM * Mt * 2**(M - t)))
            upd('sum|v_k|/((M)_t 2^L)', sum(abs(x) for x in vk) / (Mt * 2**(M - t)))
            # R = B_M dot P, degree <= t-1
            Rcoef = []
            for i in range(nc):
                Ri = bernstein_power([peval(dc[i], Fr(k)) for k in range(N)], M)
                assert all(x == 0 for x in Ri[t:]), (N, nu, i)
                Rcoef.append(Ri)
            # Hermite interpolation operator: data at p1 (order n) and zeros at p2 (order m)
            V = []
            for r in range(n):
                V.append([Fr(comb(i, r)) * ps[0]**(i - r) if i >= r else Fr(0) for i in range(t)])
            for r in range(m):
                V.append([Fr(comb(i, r)) * ps[1]**(i - r) if i >= r else Fr(0) for i in range(t)])
            # f for node direction l: binom(M,l) P(l) u^l (1-u)^(M-l)
            fl = []
            for l in range(N):
                vals = [pv[k] if k == l else Fr(0) for k in range(N)]
                fl.append(bernstein_power(vals, M))
            datas = [taylor(fl[l], ps[0], n) + [Fr(0)] * m for l in range(N)]
            I1 = solve_multi(V, datas) if t else []
            for j in range(1, min(3, t) + 1):
                Mt = Fr(factorial(M), factorial(M - t))
                eta_sup = sum(abs(Rcoef[i][t - j]) for i in range(N, nc))
                xi_sup = sum(abs(Rcoef[i][t - j]) * Fr(M, 2) for i in range(N))
                tot = eta_sup + xi_sup
                base = fm(Mt) * RHO**M
                upd('(15) sup|[u^(t-j)]R|/(200N^4(M)_t rho^M)', fm(tot) / (200 * N**4 * base))
                upd('weight part/(48N^2(M)_t rho^M)', fm(eta_sup) / (48 * N**2 * base))
                upd('weight part/((M)_t rho^M)', fm(eta_sup) / base)
                upd('node part/((24M+8M(3M+7))N^2(M)_t rho^M)', fm(xi_sup) / ((24 * M + 8 * M * (3 * M + 7)) * N**2 * base))
                # split node part into -ell_s f piece and common G piece
                ellpiece = [-ELL1 * fm(I1[l][t - j]) if t else 0 for l in range(N)]
                # R_xi = -(ellpiece + Gpiece)  =>  Gpiece = -R_xi - ellpiece
                Gpiece = [-fm(Rcoef[l][t - j]) - ellpiece[l] for l in range(N)]
                ell_sup = sum(abs(e) for e in ellpiece) * M / 2
                G_sup = sum(abs(g) for g in Gpiece) * M / 2
                upd('-ell_s f piece/(24MN^2(M)_t rho^M)', ell_sup / (24 * M * N**2 * base))
                Gbound = mp.mpf(2) / 5 * 16 * N**2 * mp.mpf(M) / 2 * (3 * fm(HM) + 7) * fm(Mt) * 3**M
                upd('G piece/((2/5)16N^2(M/2)(3H_M+7)(M)_t 3^M)', G_sup / Gbound)
                upd('G piece/((M)_t 3^M)', G_sup / (fm(Mt) * 3**M))
    # Section 7: B,S,T,A in k variable and their derivatives
    def cget(nu, j):
        c, dc = poly[nu]; t = sum(nu)
        return c[t - j] if j <= t else Fr(0)
    def dget(nu, j, i):
        c, dc = poly[nu]; t = sum(nu)
        return dc[i][t - j] if j <= t else Fr(0)
    def hval(nu, s, i=None):
        c, dc = poly[nu]; t = sum(nu)
        if i is None:
            return sum(c[r] * mu[s][nu[s] + r] for r in range(t + 1))
        return sum(dc[i][r] * mu[s][nu[s] + r] + c[r] * dmu(s, nu[s] + r, i) for r in range(t + 1))
    kap = Fr(0)
    Bmax = {1: Fr(0), 2: Fr(0)}; Amax = {1: Fr(0), 2: Fr(0)}
    rowsums = []
    for t in range(0, M + 1):
        for n in range(t + 1):
            nu = (n, t - n); m = t - n
            for i_dir in (0, 1):
                up = tuple(nu[q] + (q == i_dir) for q in range(2))
                B = cget(nu, 1) - cget(up, 1)
                Bexp = ps[i_dir] * (M - t) + Fr(3, 5) * n + Fr(1, 2) * m
                assert B == Bexp
                S = cget(nu, 2) - cget(up, 2) - B * cget(nu, 1)
                T = cget(nu, 3) - cget(up, 3) - B * cget(nu, 2)
                A = {}
                if n: A[1] = Fr(6, 25) * n * (M - t + 1)
                if m: A[2] = Fr(1, 4) * m * (M - t + 1)
                assert S == sum(A.values())
                pred = {s: tuple(nu[q] - (q == s - 1) for q in range(2)) for s in A}
                assert T == sum(A[s] * cget(pred[s], 1) for s in A)
                for s in A:
                    assert A[s] == hval(nu, s - 1) / hval(pred[s], s - 1)
                if n and m:
                    gap = cget(pred[1], 1) - cget(pred[2], 1)
                    assert gap == -Fr(M - t + 2, 10)
                dB = [dget(nu, 1, i) - dget(up, 1, i) for i in range(nc)]
                dS = [dget(nu, 2, i) - dget(up, 2, i) - dB[i] * cget(nu, 1) - B * dget(nu, 1, i) for i in range(nc)]
                dT = [dget(nu, 3, i) - dget(up, 3, i) - dB[i] * cget(nu, 2) - B * dget(nu, 2, i) for i in range(nc)]
                sup = lambda vec: sum(abs(vec[i]) * scale[i] for i in range(nc))
                upd('sup dB/(2C)', fm(sup(dB)) / (2 * C))
                upd('sup dS/(7N^2C)', fm(sup(dS)) / (7 * N**2 * C))
                upd('sup dT/(9N^4C)', fm(sup(dT)) / (9 * N**4 * C))
                Bmax[i_dir + 1] = max(Bmax[i_dir + 1], sup(dB))
                # dA via h ratio (independent of (20)) and via (20)
                dA = {}
                for s in A:
                    g = hval(pred[s], s - 1)
                    dA[s] = [(hval(nu, s - 1, i) - A[s] * hval(pred[s], s - 1, i)) / g for i in range(nc)]
                if n and m:
                    tau1, tau2 = cget(pred[1], 1), cget(pred[2], 1)
                    for i in range(nc):
                        dtau1, dtau2 = dget(pred[1], 1, i), dget(pred[2], 1, i)
                        a1 = (dT[i] - dS[i] * tau2 - S * dtau2 - A[1] * (dtau1 - dtau2)) / (tau1 - tau2)
                        assert a1 == dA[1][i]
                        assert dS[i] - a1 == dA[2][i]
                    upd('sup dA1/(135N^4C)', fm(sup(dA[1])) / (135 * N**4 * C))
                    upd('sup dA2/(142N^4C)', fm(sup(dA[2])) / (142 * N**4 * C))
                else:
                    for s in A:
                        assert dA[s] == dS
                for s in A:
                    upd('sup dA/(150N^4C)', fm(sup(dA[s])) / (150 * N**4 * C))
                    Amax[s] = max(Amax[s], sup(dA[s]))
    # kappa from k-variable data via the scaling of section 7
    # a=4A/M^2 with ||a_1||=max a1, b=2B/M-1, ||b||=1/5; node box in k is M/2 (already)
    a1norm = max(Fr(4, M * M) * Fr(6, 25) * n * (M - n - m + 1) for n in range(M + 1) for m in range(M + 1 - n) if n)
    a2norm = max(Fr(4, M * M) * Fr(1, 4) * m * (M - n - m + 1) for n in range(M + 1) for m in range(M + 1 - n) if m)
    kap_k = max(Fr(4, M * M) * Amax[1] / a1norm, Fr(4, M * M) * Amax[2] / a2norm,
                Fr(2, M) * Bmax[1] * 5, Fr(2, M) * Bmax[2] * 5)
    upd('a-norm lower 1/(5M) ratio min', 1 / (min(a1norm, a2norm) * 5 * M))
    out = {k: [mp.nstr(v[0], 8), v[1]] for k, v in sorted(worst.items())}
    return dict(N=N, kappa_from_k_variable=float(kap_k), kappa_k_exact=str(kap_k)[:60], worst=out)

if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for N in range(lo, hi + 1):
        print(json.dumps(run(N)), flush=True)
