#!/usr/bin/env python3
"""Claude L1 auditor's physical-coordinate numerical checks of SH_n.

Part A (mpmath, 50 digits): build the actual physical nodes/weights exactly as
the Statement defines them; run the Statement's literal normalized all-prior
projection algorithm (two-pass projection at high precision) with the epsilon
perturbation; measure ||(I-P_n)P_n(eps;f)||_2/eps at eps=1e-20 for (i) the BJ
witness source and (ii) a random all-position unit relative source for both
rules, and compare (ii) with the mirror closed form (17)-(18) evaluated with
diagonal U_a(S), U_a(T) operators in physical coordinates.

Part B (float64): forward-mode linearization of the same physical algorithm
over every source coordinate direction; relative-source Hilbert-Schmidt norm
(compared with the exact rationals of the companion exact script) and an
alternating-maximization LOWER estimate of the spectral capacity
kappa = sup_u ||R_n L(u)||_2 for both rules. The HS norm is an upper bound.
Measurements only.
"""
import json
import sys
import time

import mpmath as mp
import numpy as np


def order(n):
    return [(t - j, j) for t in range(n + 1) for j in range(t + 1)]


def creator(rule, r, j, lookup):
    if (rule == "BJ" and j == 0) or (rule == "mirror" and r > 0):
        return "X", lookup[(r - 1, j)]
    return "Y", lookup[(r, j - 1)]


# ---------------------------------------------------------------- Part A
def partA(n, eps_exp=20, seed=1):
    mp.mp.dps = 50
    m = n + 2
    M = m * m
    th = [mp.mpf(k) * mp.pi / (m + 1) for k in range(1, m + 1)]
    s = [mp.cos(t) for t in th]
    v = [2 * mp.sin(t) ** 2 / (m + 1) for t in th]
    X, Y, W, Sl, Tl = [], [], [], [], []
    for k in range(m):
        for l in range(m):
            X.append(s[k]); Y.append(2 * s[k] + s[l]); W.append(v[k] * v[l])
            Sl.append(s[k]); Tl.append(s[l])
    assert min(W) > 0
    assert abs(mp.fsum(W) - 1) < mp.mpf(10) ** -45
    dmin = min(mp.sqrt((X[a] - X[b]) ** 2 + (Y[a] - Y[b]) ** 2) for a in range(M) for b in range(a))
    EX = mp.fsum(w * x for w, x in zip(W, X)); EY = mp.fsum(w * y for w, y in zip(W, Y))
    cov = mp.fsum(w * (x - EX) * (y - EY) for w, x, y in zip(W, X, Y))
    sq = [mp.sqrt(w) for w in W]
    cols = order(n)
    N = len(cols)
    lookup = {c: k for k, c in enumerate(cols)}

    def U(a, z):
        if a < 0:
            return mp.mpf(0)
        u0, u1 = mp.mpf(1), 2 * z
        if a == 0:
            return u0
        for _ in range(1, a):
            u0, u1 = u1, 2 * z * u1 - u0
        return u1

    def gs(rule, eps, F):
        Q = [mp.matrix(sq)]
        piv = []
        for h in range(1, N):
            r, j = cols[h]
            kind, p = creator(rule, r, j, lookup)
            D = X if kind == "X" else Y
            a = mp.matrix([D[i] * Q[p][i] for i in range(M)])
            if F is not None and F[h] is not None:
                a = a + eps * F[h]
            res = a
            for _ in range(2):
                for q in Q:
                    c = mp.fsum(q[i] * res[i] for i in range(M))
                    res = res - c * q
            beta = mp.sqrt(mp.fsum(res[i] ** 2 for i in range(M)))
            piv.append(beta)
            Q.append(res / beta)
        return Q, piv

    out = {"n": n, "M": M, "min_weight": mp.nstr(min(W), 8), "min_node_distance": mp.nstr(dmin, 8),
           "Cov_XY": mp.nstr(cov, 30)}
    for rule in ("BJ", "mirror"):
        Q0, piv = gs(rule, 0, None)
        err_piv = max(abs(p - mp.mpf(1) / 2) for p in piv)
        err_q = mp.mpf(0)
        for k, (r, j) in enumerate(cols):
            for i in range(M):
                err_q = max(err_q, abs(Q0[k][i] - sq[i] * U(r, Sl[i]) * U(j, Tl[i])))
        # exact R_n
        Qn = mp.matrix(M, N)
        for k in range(N):
            for i in range(M):
                Qn[i, k] = Q0[k][i]
        Rn = mp.eye(M) - Qn * Qn.T
        # sigma_h
        sig = [None]
        for h in range(1, N):
            r, j = cols[h]
            kind, p = creator(rule, r, j, lookup)
            D = X if kind == "X" else Y
            sig.append(mp.sqrt(mp.fsum((D[i] * Q0[p][i]) ** 2 for i in range(M))))
        eps = mp.mpf(10) ** (-eps_exp)

        def ratio(F):
            Qe, _ = gs(rule, eps, F)
            Qm = mp.matrix(M, N)
            for k in range(N):
                for i in range(M):
                    Qm[i, k] = Qe[k][i]
            # spectral norm of R_n P_n(eps) = spectral norm of R_n Qm (orthonormal columns)
            Z = Rn * Qm
            sv = mp.svd_r(Z, compute_uv=False)
            return max(sv[i] for i in range(len(sv))) / eps, Z

        res = {"max_pivot_error": mp.nstr(err_piv, 5), "max_q_vs_sqrtw_UU_error": mp.nstr(err_q, 5),
               "sigma_max": mp.nstr(max(sig[1:]), 20)}
        if rule == "BJ":
            e = mp.matrix([sq[i] * U(n + 1, Sl[i]) for i in range(M)])
            F = [None] * N
            F[lookup[(n, 0)]] = e / mp.sqrt(2)
            budget = mp.fsum(F[lookup[(n, 0)]][i] ** 2 for i in range(M)) / sig[lookup[(n, 0)]] ** 2
            kap, _ = ratio(F)
            pred = mp.sqrt(mp.mpf(2) * (4 ** (n + 1) - 1) / 3)
            res.update({"witness_budget": mp.nstr(budget, 25), "witness_ratio_eps": mp.nstr(kap, 25),
                        "predicted": mp.nstr(pred, 25), "rel_diff": mp.nstr(abs(kap - pred) / pred, 5)})
        # random all-position unit relative source
        rng = np.random.default_rng(seed + n)
        raw = [None] + [rng.standard_normal(M) for _ in range(1, N)]
        nrm = mp.sqrt(mp.fsum(mp.fsum(mp.mpf(float(x)) ** 2 for x in raw[h]) for h in range(1, N)))
        F = [None] + [mp.matrix([sig[h] * mp.mpf(float(x)) / nrm for x in raw[h]]) for h in range(1, N)]
        bud = mp.fsum(mp.fsum(F[h][i] ** 2 for i in range(M)) / sig[h] ** 2 for h in range(1, N))
        kap_r, Z = ratio(F)
        res["random_source_budget"] = mp.nstr(bud, 20)
        res["random_source_ratio_eps"] = mp.nstr(kap_r, 20)
        if rule == "mirror":
            # closed form (17),(18) in physical coordinates, diag U_a(S), U_a(T)
            def Udiag(a, coord, vec):
                return mp.matrix([U(a, coord[i]) * vec[i] for i in range(M)])
            Vcf = []
            for k, (r, j) in enumerate(cols):
                V0 = mp.matrix(M, 1)
                for b_ in range(1, j + 1):
                    g = 2 * F[lookup[(0, b_)]] - 4 * F[lookup[(1, b_ - 1)]]
                    V0 = V0 + Udiag(j - b_, Tl, g)
                Vk = Udiag(r, Sl, V0)
                for a_ in range(1, r + 1):
                    Vk = Vk + 2 * Udiag(r - a_, Sl, F[lookup[(a_, j)]])
                Vcf.append(Vk)
            Vm = mp.matrix(M, N)
            for k in range(N):
                for i in range(M):
                    Vm[i, k] = Vcf[k][i]
            RV = Rn * Vm
            sv = mp.svd_r(RV, compute_uv=False)
            pred = max(sv[i] for i in range(len(sv)))
            res["random_source_closed_form_pred"] = mp.nstr(pred, 20)
            res["random_closed_form_rel_diff"] = mp.nstr(abs(pred - kap_r) / pred, 5)
            # entrywise: Z/eps vs R_n V
            res["random_closed_form_matrix_maxdiff"] = mp.nstr(max(abs(Z[i, k] / eps - RV[i, k]) for i in range(M) for k in range(N)), 5)
            Hh = N - 1
            res["stated_upper"] = mp.nstr(2 * mp.sqrt(6) * (n + 1) ** 2 * Hh, 10)
        out[rule] = res
    return out


# ---------------------------------------------------------------- Part B
def linear_map(n, rule):
    m = n + 2
    M = m * m
    th = np.arange(1, m + 1) * np.pi / (m + 1)
    s = np.cos(th); v = 2 * np.sin(th) ** 2 / (m + 1)
    S = np.repeat(s, m); T = np.tile(s, m)
    X = S; Y = 2 * S + T
    w = np.outer(v, v).ravel(); sq = np.sqrt(w)
    cols = order(n); N = len(cols); lookup = {c: k for k, c in enumerate(cols)}
    H = N - 1; K = H * M
    Q = np.zeros((M, N)); dQ = np.zeros((N, M, K))
    Q[:, 0] = sq
    sig = np.zeros(N)
    for h in range(1, N):
        r, j = cols[h]
        kind, p = creator(rule, r, j, lookup)
        D = X if kind == "X" else Y
        a = D * Q[:, p]
        sig[h] = np.linalg.norm(a)
        da = D[:, None] * dQ[p]
        da[:, (h - 1) * M:h * M] += np.eye(M)
        Qp = Q[:, :h]
        c = Qp.T @ a
        res = a - Qp @ c
        c2 = Qp.T @ res; res -= Qp @ c2; c += c2
        beta = np.linalg.norm(res)
        qh = res / beta
        dc = np.einsum('i,lik->lk', a, dQ[:h]) + Qp.T @ da          # h x K
        dr = da - Qp @ dc - np.einsum('l,lik->ik', c, dQ[:h])
        dbeta = qh @ dr
        dQ[h] = (dr - np.outer(qh, dbeta)) / beta
        Q[:, h] = qh
    R = np.eye(M) - Q @ Q.T
    L = np.einsum('ij,kjK->ikK', R, dQ)    # M x N x K normal output
    scale = np.repeat(sig[1:], M)          # relative source: f_h = sigma_h u_h
    L = L * scale[None, None, :]
    return L, sig, Q


def spectral_capacity_lower(L, restarts=60, iters=400, seed=0):
    M, N, K = L.shape
    rng = np.random.default_rng(seed)
    best = 0.0
    starts = [np.eye(N)[k] for k in range(N)] + [rng.standard_normal(N) for _ in range(restarts)]
    for c in starts:
        c = c / np.linalg.norm(c)
        val = 0.0
        for _ in range(iters):
            Gc = np.einsum('ikK,k->iK', L, c)
            U_, sv, Vt = np.linalg.svd(Gc, full_matrices=False)
            u = Vt[0]
            Wu = np.einsum('ikK,K->ik', L, u)
            U2, sv2, Vt2 = np.linalg.svd(Wu, full_matrices=False)
            cnew = Vt2[0]
            if abs(sv2[0] - val) < 1e-14 * max(1, sv2[0]):
                val = sv2[0]
                break
            val = sv2[0]; c = cnew
        best = max(best, val)
    return best


def partB(n):
    out = {"n": n}
    for rule in ("BJ", "mirror"):
        L, sig, Q = linear_map(n, rule)
        HS2 = float(np.sum(L ** 2))
        lower = spectral_capacity_lower(L)
        out[rule] = {"HS2_float": HS2, "kappa_lower_altmax": lower}
    N = (n + 1) * (n + 2) // 2
    out["stated_bj_lower"] = float(np.sqrt(2 * (4 ** (n + 1) - 1) / 3))
    out["stated_mirror_upper"] = float(2 * np.sqrt(6) * (n + 1) ** 2 * (N - 1))
    out["ratio_lower_estimates_bj_over_mirrorHS"] = out["BJ"]["kappa_lower_altmax"] / np.sqrt(out["mirror"]["HS2_float"])
    return out


if __name__ == "__main__":
    which = sys.argv[1]
    ns = [int(a) for a in sys.argv[2:]]
    for n in ns:
        t0 = time.time()
        r = partA(n) if which == "A" else partB(n)
        r["seconds"] = round(time.time() - t0, 2)
        print(json.dumps(r), flush=True)
