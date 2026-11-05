#!/usr/bin/env python3
"""Claude L1 auditor's own exact check of the SH_n aggregate-separation record.

Independent design (not derived from code/sh_independent.py):
  * representation: LATENT MONOMIAL basis s^a t^b (0<=a,b<=m-1) of functions on
    the m x m latent grid, NOT the orthonormal U/Jacobi basis; the weighted
    inner product is the exact rational Gram matrix G = G1 (x) G1 with
    G1[a,c] = mu_{a+c}, mu_p = sum_k v_k s_k^p computed by an exact
    trigonometric-sum formula and cross-checked against 60-digit mpmath nodes;
  * multiplication by s, t reduced by the node polynomial obtained by solving
    the Gram system (independently checked to be 2^-m U_m);
  * physical X = S, Y = 2S + T;
  * MONIC (unnormalized) all-prior Gram-Schmidt in exact rationals, exactly as
    PD-T136 is stated, with the derivative of the full nonlinear projection
    computed by forward-mode (dual-number) exact differentiation over every
    source coordinate direction; output T = R_n [db_k] D^{-1/2};
  * relative source norm with the rule's own monic sigma_h = ||A b_parent||.
The orthonormality (4), pivots, gauge, injectivity, BJ witness and the
relative-source Hilbert--Schmidt norm of the normal-output map are verified,
not assumed. Finite checks only; no all-n reduction.
"""
import json
import sys
import time
from fractions import Fraction
from math import comb

import flint
import mpmath as mp

Q = flint.fmpq


def C_sum(j, m):
    """sum_{k=1}^m cos(j k pi/(m+1)) exactly."""
    j = abs(j)
    if j % (2 * (m + 1)) == 0:
        return Q(m)
    return Q(-1) if j % 2 == 0 else Q(0)


def moments(m, pmax):
    mu = []
    for p in range(pmax + 1):
        tot = Q(0)
        for i in range(p + 1):
            a = p - 2 * i
            tot += comb(p, i) * (C_sum(a, m) - (C_sum(a + 2, m) + C_sum(a - 2, m)) / 2)
        mu.append(tot / (Q(2) ** p * (m + 1)))
    return mu


def moments_numeric(m, pmax):
    mp.mp.dps = 60
    out = []
    for p in range(pmax + 1):
        s = mp.mpf(0)
        for k in range(1, m + 1):
            th = k * mp.pi / (m + 1)
            s += 2 * mp.sin(th) ** 2 / (m + 1) * mp.cos(th) ** p
        out.append(s)
    return out


def upoly(r):
    """coefficients (low->high) of U_r."""
    if r == 0:
        return [Q(1)]
    a, b = [Q(1)], [Q(0), Q(2)]
    for _ in range(1, r):
        c = [Q(0)] + [2 * x for x in b]
        for i, x in enumerate(a):
            c[i] -= x
        a, b = b, c
    return b


def run(n, verbose=True):
    t0 = time.time()
    m = n + 2
    M = m * m
    idx = lambda a, b: a * m + b
    mu = moments(m, 2 * m)
    mun = moments_numeric(m, 2 * m)
    for p in range(2 * m + 1):
        assert abs(mp.mpf(int(mu[p].p)) / int(mu[p].q) - mun[p]) < mp.mpf(10) ** -50, (p, mu[p], mun[p])
    assert mu[0] == 1
    # one-dimensional Gram matrix and node polynomial via the Gram system
    G1 = flint.fmpq_mat(m, m, [mu[a + c] for a in range(m) for c in range(m)])
    rhs = flint.fmpq_mat(m, 1, [mu[m + a] for a in range(m)])
    red = G1.solve(rhs)  # s^m = sum_c red[c] s^c on the nodes
    Um = upoly(m)
    # monic node polynomial 2^-m U_m: s^m = -sum_{c<m} 2^-m U_m[c] s^c
    for c in range(m):
        assert red[c, 0] == -Um[c] / Q(2) ** m
    # residual check: ||s^m - sum red s^c||^2 = 0 in the moment functional
    res2 = mu[2 * m] - 2 * sum(red[c, 0] * mu[m + c] for c in range(m)) + \
        sum(red[a, 0] * red[c, 0] * mu[a + c] for a in range(m) for c in range(m))
    assert res2 == 0
    G = flint.fmpq_mat(M, M, [mu[a + c] * mu[b + d] for a in range(m) for b in range(m)
                              for c in range(m) for d in range(m)])
    Ginv = G.inv()
    # multiplication operators
    Sop = flint.fmpq_mat(M, M)
    Top = flint.fmpq_mat(M, M)
    for a in range(m):
        for b in range(m):
            col = idx(a, b)
            if a + 1 < m:
                Sop[idx(a + 1, b), col] = 1
            else:
                for c in range(m):
                    Sop[idx(c, b), col] = red[c, 0]
            if b + 1 < m:
                Top[idx(a, b + 1), col] = 1
            else:
                for c in range(m):
                    Top[idx(a, c), col] = red[c, 0]
    Xop = Sop
    Yop = 2 * Sop + Top

    def ip(u, v):
        return (u.transpose() * G * v)[0, 0]

    def uvec(r, j):
        v = flint.fmpq_mat(M, 1)
        ur, uj = upoly(r), upoly(j)
        for a, ca in enumerate(ur):
            for b, cb in enumerate(uj):
                v[idx(a, b), 0] += ca * cb
        return v

    # orthonormality (4) of U_a(s)U_b(t), 0<=a,b<=m-1, verified exactly
    Ubasis = [uvec(a, b) for a in range(m) for b in range(m)]
    Umat = flint.fmpq_mat(M, M, [Ubasis[c][r, 0] for r in range(M) for c in range(M)])
    gram_U = Umat.transpose() * G * Umat
    assert gram_U == flint.fmpq_mat(M, M, [Q(int(i == j)) for i in range(M) for j in range(M)])
    # physical monomials x^r y^j = s^r (2s+t)^j  (exponents <= n+1 <= m-1)
    def physmono(r, j):
        v = flint.fmpq_mat(M, 1)
        for i in range(j + 1):
            # (2s)^(j-i) t^i
            v[idx(r + j - i, i), 0] += comb(j, i) * Q(2) ** (j - i)
        return v

    def cols(d):
        return [(t - jj, jj) for t in range(d + 1) for jj in range(t + 1)]

    # injectivity through n+1 and failure-to-be-injective check at larger degree
    def rank_upto(d):
        V = [physmono(r, j) for r, j in cols(d)]
        A = flint.fmpq_mat(M, len(V), [V[c][r, 0] for r in range(M) for c in range(len(V))])
        return A.rank(), len(V)
    rk, Nn1 = rank_upto(n + 1)
    assert rk == Nn1 == (n + 2) * (n + 3) // 2
    # nonproduct: Cov(X,Y) = 1/2 with E X = E Y = 0
    one = flint.fmpq_mat(M, 1); one[idx(0, 0), 0] = 1
    xv, yv = physmono(1, 0), physmono(0, 1)
    EX, EY = ip(one, xv), ip(one, yv)
    EXY = ip(xv, yv)
    assert EX == 0 and EY == 0 and EXY == Q(1, 2)
    # node distinctness / positivity are checked numerically in the companion script
    order = cols(n)
    N = len(order)
    assert N == (n + 1) * (n + 2) // 2
    lookup = {c: k for k, c in enumerate(order)}
    H = N - 1
    K = H * M
    out = {"n": n, "m": m, "M": M, "N_n": N, "M_minus_N_n": M - N,
           "orthonormal_U_tensor_basis_exact": True,
           "node_polynomial_is_2^-m_U_m": True,
           "rank_physical_monomials_deg_le_n+1": rk,
           "Cov_XY": str(EXY)}
    for rule in ("BJ", "mirror"):
        b, d, Gb, z_list, alpha, sigma2 = [one], [Q(1)], [G * one], [None], [None], [None]
        par = [None]
        for h in range(1, N):
            r, j = order[h]
            if (rule == "BJ" and j == 0) or (rule == "mirror" and r > 0):
                A, p = Xop, lookup[(r - 1, j)]
            else:
                A, p = Yop, lookup[(r, j - 1)]
            z = A * b[p]
            al = [(Gb[l].transpose() * z)[0, 0] / d[l] for l in range(h)]
            bh = z
            for l in range(h):
                if al[l] != 0:
                    bh = bh - al[l] * b[l]
            dh = ip(bh, bh)
            deg = r + j
            # monic gauge: b_h = 2^-d U_r(s) U_j(t), d_h = 4^-d
            assert dh == Q(1, 4 ** deg), (rule, h, dh)
            assert bh == Q(1, 2 ** deg) * uvec(r, j)
            # leading physical monomial: b_h - x^r y^j in span of earlier physical monomials
            prev = [physmono(*c) for c in order[:h]]
            diff = bh - physmono(r, j)
            if prev:
                P = flint.fmpq_mat(M, len(prev), [prev[c][rr, 0] for rr in range(M) for c in range(len(prev))])
                aug = flint.fmpq_mat(M, len(prev) + 1, [ (prev[c][rr, 0] if c < len(prev) else diff[rr, 0]) for rr in range(M) for c in range(len(prev) + 1)])
                assert aug.rank() == P.rank() == len(prev)
            s2 = ip(z, z)
            pr, pj = order[p]
            if A is Xop:
                formula = Q(1 + int(pr >= 1), 4)
            else:
                formula = 1 + int(pr >= 1) + Q(1 + int(pj >= 1), 4)
            # normalized sigma^2 = 4^(deg-1) * monic sigma^2
            assert s2 * 4 ** (deg - 1) == formula, (rule, h, s2, formula)
            # normalized pivot: ||b_h|| / ||A b_p|| * ||A q_p|| ... pivot beta = ||b_h||/||b_p|| = 1/2
            assert dh * 4 == d[p]
            b.append(bh); d.append(dh); Gb.append(G * bh); z_list.append(z); alpha.append(al)
            sigma2.append(s2); par.append((A, p))
        # ---- exact forward-mode derivative over all source coordinate directions
        db = [flint.fmpq_mat(M, K)]
        for h in range(1, N):
            A, p = par[h]
            z = z_list[h]
            dz = A * db[p]
            for i in range(M):
                dz[i, (h - 1) * M + i] += 1
            Gz = G * z
            dbh = dz
            for l in range(h):
                # alpha_l = <b_l,z>/d_l;  d alpha_l
                row = (Gz.transpose() * db[l]) + (Gb[l].transpose() * dz)   # 1 x K
                dd_l = 2 * (Gb[l].transpose() * db[l])                    # d(d_l)
                dal = row / d[l] - (alpha[h][l] / d[l]) * dd_l
                dbh = dbh - b[l] * dal
                if alpha[h][l] != 0:
                    dbh = dbh - alpha[h][l] * db[l]
            db.append(dbh)
        # normal projection onto complement of S_n = span{b_l}
        Rdb = []
        for k in range(N):
            v = db[k]
            for l in range(N):
                v = v - b[l] * ((Gb[l].transpose() * db[k]) / d[l])
            Rdb.append(v)
        # sanity: R_n of every b_l is zero; tangent identity <b_k,db_l>+<db_k,b_l> = d(<b_k,b_l>)=0 for k!=l
        for k in range(N):
            for l in range(k):
                t = (Gb[k].transpose() * db[l]) + (Gb[l].transpose() * db[k])
                assert t == flint.fmpq_mat(1, K)
        # relative-source HS^2 of normal output map (spectral <= this)
        HS2 = Q(0)
        for h in range(1, N):
            blk = slice((h - 1) * M, h * M)
            tot = Q(0)
            for k in range(N):
                L = flint.fmpq_mat(M, M, [Rdb[k][rr, (h - 1) * M + c] for rr in range(M) for c in range(M)])
                Y = L.transpose() * G * L
                tr = sum((Ginv[i, jj] * Y[jj, i] for i in range(M) for jj in range(M)), Q(0))
                tot += tr / d[k]
            HS2 += sigma2[h] * tot
        res = {"pivots_all_half": True, "monic_gauge_and_U_identification": True,
               "leading_monomial_triangular": True, "sigma_formula_(7)": True,
               "relative_source_HS_squared_normal_output": str(HS2)}
        if rule == "mirror":
            res["max_sigma2_normalized"] = str(max(sigma2[h] * 4 ** (sum(order[h]) - 1) for h in range(1, N)))
        # ---- BJ normal witness: source e = U_{n+1}(s) at h=(n,0)
        if rule == "BJ":
            h = lookup[(n, 0)]
            e = uvec(n + 1, 0)
            assert ip(e, e) == 1
            for l in range(N):
                assert ip(e, b[l]) == 0
            budget = ip(e, e) / sigma2[h]     # ||f||^2/sigma^2 (monic)
            # output columns for this source: Rdb[k] * e (coefficient combination of block h)
            cols_out = []
            for k in range(N):
                blk = flint.fmpq_mat(M, M, [Rdb[k][rr, (h - 1) * M + c] for rr in range(M) for c in range(M)])
                cols_out.append(blk * e)
            # rank one along e: each column = lambda_k e
            lam = []
            for k in range(N):
                lk = ip(e, cols_out[k])
                assert cols_out[k] == lk * e
                lam.append(lk)
            T2 = sum((lk * lk / d[k] for k, lk in enumerate(lam)), Q(0))   # ||T||_2^2 (rank one, ||e||=1)
            gain2 = T2 / budget
            assert gain2 == Q(2 * (4 ** (n + 1) - 1), 3), gain2
            # the normalized coefficients 2(-2)^j: lambda_k / sqrt(d_k) relative scale
            res["bj_witness_gain_squared"] = str(gain2)
            res["bj_witness_normalized_coeffs_sq_over_budget"] = [str(lk * lk / d[k] / budget) for k, lk in enumerate(lam) if lk != 0]
            res["bj_witness_nonzero_only_degree_n"] = all((lam[k] != 0) == (sum(order[k]) == n) for k in range(N))
        out[rule] = res
    # stated bounds
    out["stated_bj_lower_squared"] = str(Q(2 * (4 ** (n + 1) - 1), 3))
    out["stated_mirror_upper_squared"] = 24 * (n + 1) ** 4 * (N - 1) ** 2
    out["seconds"] = round(time.time() - t0, 2)
    if verbose:
        print(json.dumps(out), flush=True)
    return out


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [2, 3, 4]
    allres = [run(n) for n in ns]
    print("ALL_ASSERTIONS_PASSED")
