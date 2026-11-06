#!/usr/bin/env python3
"""Auditor-authored floating/multiprecision checks of the finite weighted model.

Independent paths:
 * derivative tensor by complex-step differentiation of the perturbed
   represented Gram-Schmidt (real bilinear dot -> analytic), not dual Fractions;
 * capacity kappa(J)=sup_{a,f} ||T(f)a|| by alternating power maximisation with
   restarts (a certified LOWER estimate of the sup, up to float error);
 * the attained terminal block norm ||M_T|| and the P4-02/P4-03 finite bounds
   are compared against it;
 * the angle expansion is validated by an actual finite-epsilon perturbed
   projection in mpmath (60 digits).
MEASURED supplementary evidence only.
"""
import json, sys
import numpy as np
import mpmath as mp
from fractions import Fraction as F

rng = np.random.default_rng(20261106)


def family(kind, n):
    if kind == "dev_triangle":
        L = n + 1
        nodes = [(i, j) for j in range(L + 1) for i in range(L + 1 - j)]
        w = np.array([1 + i + 2 * j for i, j in nodes], float)
    elif kind == "randT":
        N = n + 2
        nodes = [(2 * i / N - 1, 2 * j / N - 1) for i in range(N + 1) for j in range(N + 1 - i)]
        w = rng.uniform(0.2, 3.0, len(nodes))
    elif kind == "D65x9":
        dirs = {(65, 0), (-65, 0), (0, 65), (0, -65)}
        for a, b in [(16, 63), (25, 60), (33, 56), (39, 52)]:
            for u, v in [(a, b), (b, a)]:
                for sx in (-1, 1):
                    for sy in (-1, 1):
                        dirs.add((sx * u, sy * v))
        nodes = [(k * a / 585, k * b / 585) for k in range(1, 10) for a, b in sorted(dirs)]
        w = np.ones(len(nodes))
    z = np.array(nodes, float)
    return z, w / w.sum()


def rule_axis(rule, r, j):
    if j == 0:
        return 0
    if r == 0:
        return 1
    return 1 if rule == "BJ" else 0


def setup(z, w, n, rule):
    ms = [(d - j, j) for d in range(n + 1) for j in range(d + 1)]
    idx = {m: k for k, m in enumerate(ms)}
    sw = np.sqrt(w)
    B = [sw.copy()]
    alpha, sig2, choice = [[]], [0.0], [None]
    for k, (r, j) in enumerate(ms[1:], 1):
        ax = rule_axis(rule, r, j)
        par = idx[(r - 1, j) if ax == 0 else (r, j - 1)]
        raw = z[:, ax] * B[par]
        al = [raw @ b / (b @ b) for b in B]
        res = raw - sum(a * b for a, b in zip(al, B))
        B.append(res)
        alpha.append(al)
        sig2.append(raw @ raw)
        choice.append((ax, par))
    return ms, np.array(B).T, alpha, np.array(sig2), choice


def perturbed_basis(z, w, choice, inj, eps):
    """Perturbed represented GS; inj[k] vector; eps may be complex."""
    sw = np.sqrt(w).astype(complex)
    B = [sw]
    for k in range(1, len(choice)):
        ax, par = choice[k]
        v = z[:, ax] * B[par] + eps * inj[k]
        for b in B:
            v = v - (b @ v) / (b @ b) * b   # bilinear (no conjugate) -> analytic
        B.append(v)
    return np.array(B).T


def derivative_tensor(z, w, choice, sources, h_eps=1e-30):
    M = len(z)
    K = len(choice)
    T = {}
    for h in sources:
        for i in range(M):
            inj = [np.zeros(M, complex) for _ in range(K)]
            inj[h][i] = 1.0
            Bp = perturbed_basis(z, w, choice, inj, 1j * h_eps)
            T[(h, i)] = Bp.imag / h_eps
    return T


def capacity(T, B, d, sig2, sources, M, restarts=None, iters=None):
    restarts = restarts or (30 if M < 100 else 6)
    iters = iters or (300 if M < 100 else 80)
    Q = B / np.sqrt(d)
    R = np.eye(M) - Q @ Q.T
    keys = [(h, i) for h in sources for i in range(M)]
    # Kmat[:, col, k]: normalized output column k for unit relative source coordinate
    Kt = np.stack([np.sqrt(sig2[h]) * (R @ T[(h, i)]) / np.sqrt(d) for h, i in keys], axis=1)  # M x S x Ns
    best = 0.0
    Ns = B.shape[1]
    for _ in range(restarts):
        a = rng.standard_normal(Ns); a /= np.linalg.norm(a)
        for _ in range(iters):
            La = Kt @ a                       # M x S
            _, s, vt = np.linalg.svd(La, full_matrices=False)
            u = vt[0]
            Tu = np.tensordot(u, Kt, axes=([0], [1]))  # M x Ns
            _, s2, vt2 = np.linalg.svd(Tu, full_matrices=False)
            a = vt2[0]
        best = max(best, s2[0])
    return best, R, keys, Kt


def g_responses(z, alpha, choice):
    K = len(choice)
    M = len(z)
    g = np.zeros((K, K, M))
    for k in range(1, K):
        ax, par = choice[k]
        row = z[:, ax] * g[par]
        for l, a in enumerate(alpha[k]):
            row = row - a * g[l]
        row[k] += 1.0
        g[k] = row
    return g


def run_case(kind, n, rule):
    z, w = family(kind, n)
    ms, B, alpha, sig2, choice = setup(z, w, n, rule)
    M, Ns = B.shape
    d = np.sum(B * B, axis=0)
    out = {"family": kind, "n": n, "rule": rule, "M": M, "Ns": Ns}
    g = g_responses(z, alpha, choice)
    P = (B / np.sqrt(d)) @ (B / np.sqrt(d)).T
    # all-source J
    J = list(range(1, Ns))
    T = derivative_tensor(z, w, choice, J)
    kap, R, keys, Kt = capacity(T, B, d, sig2, J, M)
    C = [np.array([[g[k, h, i] * np.sqrt(sig2[h]) / np.sqrt(d[k]) for h in J] for k in range(Ns)]) for i in range(M)]
    Cn = np.array([np.linalg.norm(Ci, 2) for Ci in C])
    lower2 = max(np.sqrt(1 - P[i, i]) * Cn[i] for i in range(M))
    upper2 = Cn.max()
    v = np.array([[sig2[h] * sum(g[k, h, i] ** 2 / d[k] for k in range(h, Ns)) for i in range(M)] for h in J])
    ell = (1 - np.diag(P))[None, :] * v
    out.update({"kappa_all_altmax": kap,
                "P403_lower_rowspectral": lower2, "P403_upper_rowspectral": upper2,
                "P402_L": np.sqrt(ell.max()), "P402_H": np.sqrt(ell.sum()),
                "P402_U": np.sqrt(v.sum(axis=0).max())})
    tol = 1e-9 * max(1, upper2)
    out["sandwich_ok"] = bool(out["P402_L"] <= kap + tol and lower2 <= kap + tol and
                              kap <= upper2 + tol and kap <= out["P402_H"] + tol and kap <= out["P402_U"] + tol
                              and upper2 <= out["P402_U"] + tol)
    # derivative-tensor vs frozen-response normal output (independent paths)
    err = 0.0
    for (h, i) in keys:
        froz = np.zeros((M, Ns))
        for k in range(Ns):
            froz[i, k] = g[k, h, i]
        err = max(err, np.abs(R @ T[(h, i)] - R @ froz).max())
    out["complexstep_vs_frozen_normal_maxabs"] = err
    # terminal block
    first = n * (n + 1) // 2
    Tset = list(range(first, Ns))
    A = np.eye(n + 1)
    for a_, k in enumerate(Tset):
        for b_, l in enumerate(Tset):
            if l < k:
                A[a_, b_] = alpha[k][l]
    G = np.linalg.inv(A)
    MT = np.diag(1 / np.sqrt(d[Tset])) @ G @ np.diag(np.sqrt(sig2[Tset]))
    nMT = np.linalg.norm(MT, 2)
    TT = {key: T[key] for key in T if key[0] in Tset}
    kapT, RT, keysT, KtT = capacity(TT, B, d, sig2, Tset, M)
    out.update({"terminal_norm_MT": nMT, "terminal_kappa_altmax": kapT,
                "terminal_rel_diff": abs(kapT - nMT) / nMT,
                "terminal_le_all": bool(nMT <= kap * (1 + 1e-9))})
    # finite-epsilon angle check of the attaining terminal source u_h = v_h e
    _, _, vt = np.linalg.svd(MT)
    vv = vt[0]
    evec = RT[:, 0] / np.linalg.norm(RT[:, 0])
    mp.mp.dps = 60
    eps = mp.mpf('1e-25')
    zz = [[mp.mpf(F(float(t)).numerator) / F(float(t)).denominator for t in row] for row in z]
    ww = [mp.mpf(F(float(t)).numerator) / F(float(t)).denominator for t in w]
    sw = [mp.sqrt(t) for t in ww]

    def gs(epsv):
        Bm = [sw[:]]
        for k in range(1, Ns):
            ax, par = choice[k]
            vec = [zz[i][ax] * Bm[par][i] for i in range(M)]
            if k in Tset and epsv != 0:
                c = mp.sqrt(sig2_mp[k]) * vv[Tset.index(k)]
                vec = [vec[i] + epsv * c * evec[i] for i in range(M)]
            for b in Bm:
                cf = mp.fsum(b[i] * vec[i] for i in range(M)) / mp.fsum(t * t for t in b)
                vec = [vec[i] - cf * b[i] for i in range(M)]
            Bm.append(vec)
        return mp.matrix(Bm).T
    sig2_mp = [None]
    B0 = gs(0)
    for k in range(1, Ns):
        ax, par = choice[k]
        raw = [zz[i][ax] * B0[i, par] for i in range(M)]
        sig2_mp.append(mp.fsum(t * t for t in raw))
    B0 = gs(0)
    Be = gs(eps)
    def mgs(Bm):
        cols = []
        for k in range(Ns):
            v = [Bm[i, k] for i in range(M)]
            for q in cols:
                c = mp.fsum(q[i] * v[i] for i in range(M))
                v = [v[i] - c * q[i] for i in range(M)]
            nv = mp.sqrt(mp.fsum(t * t for t in v))
            cols.append([t / nv for t in v])
        return mp.matrix(cols).T
    Q0 = mgs(B0)
    Qe = mgs(Be)
    W = Qe - Q0 * (Q0.T * Qe)
    sv = mp.svd_r(W, compute_uv=False)
    sine = max(sv[i] for i in range(len(sv)))
    out["fd_sine_over_eps"] = float(sine / eps)
    out["fd_rel_diff_vs_MT"] = float(abs(sine / eps - nMT) / nMT)
    return out


if __name__ == "__main__":
    import time
    cases = [c for c in [("dev_triangle", 2), ("dev_triangle", 3), ("randT", 2), ("randT", 3), ("D65x9", 2)]
             if len(sys.argv) < 2 or c[0] in sys.argv[1:]]
    print(json.dumps({"python": sys.version.split()[0], "numpy": np.__version__,
                      "mpmath": mp.__version__, "seed": 20261106}), flush=True)
    for kind, n in cases:
        for rule in ("BJ", "mirror"):
            t = time.time()
            r = run_case(kind, n, rule)
            r["elapsed_s"] = round(time.time() - t, 2)
            print(json.dumps(r, default=float), flush=True)
