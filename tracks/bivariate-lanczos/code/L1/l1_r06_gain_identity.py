"""R06: first-order coefficient-channel gains on product-type measures (PD-T?bivariate-lanczos-claude-114).
For the exact product-type window coefficients c* of a checkerboard (= product reference, PD-T?...-111), the
derivative of the Gram matrix of Xi(c* + delta e_{k,l}) is -(A + A^T), A = Xi*^T R^{(k,l)}, and A is given by
univariate data of the factor measures (formula below).  This script (1) checks the formula against direct
long-double propagation on sampled entries, (2) reports the gain census (max |A + A^T| over degrees <= n) for
on-pattern and off-pattern entries, (3) compares first-order predictions with the IDEA?...-117 measurements.
Usage: python3 -I l1_r06_gain_identity.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
import l1_r06_coefficient_channel as K

LD = np.longdouble
EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2


def univ(t, a, b, n):
    """orthonormal polynomial values P[s, node], s = 0..n, from Jacobi coefficients (a, b), b[0] = 0"""
    t = t.astype(LD); P = np.zeros((n + 1, len(t)), dtype=LD); P[0] = 1
    if n >= 1: P[1] = (t - a[0]) * P[0] / b[1]
    for s in range(1, n):
        P[s + 1] = ((t - a[s]) * P[s] - b[s] * P[s - 1]) / b[s + 1]
    return P


def assoc(t, a, b, s0, n):
    """homogeneous solution G[s] (s = 0..n) with G[s0-1] = 0, G[s0] = 1/b[s0]; zero below s0"""
    t = t.astype(LD); G = np.zeros((n + 1, len(t)), dtype=LD); G[s0] = 1 / b[s0]
    for s in range(s0, n):
        prev = G[s - 1] if s >= 1 else 0
        G[s + 1] = ((t - a[s]) * G[s] - b[s] * prev) / b[s + 1]
    return G


def formula_A(k, l, tab, n, Px, Py, wx, wy, X, Y, ax, bx, ay, by):
    """A = Xi*^T R for the unit forcing f = xi*_l injected at column k (e_k = f / beta_k), degrees <= n"""
    idx, pos, parent, op, start = tab
    Nn = Nof(n); A = np.zeros((Nn, Nn), dtype=LD)
    t, j = idx[k]; i = t - j; tl, jl = idx[l]; il = tl - jl
    xdeg = np.array([a - b for (a, b) in idx[:Nn]]); ydeg = np.array([b for (a, b) in idx[:Nn]])
    if j >= 1:
        G = assoc(Y, ay, by, j, n)
        rr = list(range(0, n - t + 1)); dcols = [pos[(t + r, j + r)] for r in rr]
        src = Py[jl] * G[[j + r for r in rr]]                      # (nr, My)
        Yf = (Py * wy.astype(LD)) @ src.T                         # (n+1, nr): <r_b, r_jl G_{j+r}>
        erows = np.where(xdeg == il)[0]
        A[np.ix_(erows, dcols)] = Yf[ydeg[erows]]
    else:
        G = assoc(X, ax, bx, t, n)
        Xf = (Px * wx.astype(LD)) @ (Px[il] * G).T                # (n+1, n+1): <p_a, p_il G_i'>
        Yf2 = (Py * wy.astype(LD)) @ (Py[jl] * Py).T              # (n+1, n+1): <r_b, r_jl r_r>
        dcols, ip, rr = [], [], []
        for i2 in range(t, n + 1):
            for r in range(0, n - i2 + 1):
                dcols.append(pos[(i2 + r, r)]); ip.append(i2); rr.append(r)
        A[:, dcols] = Xf[np.ix_(xdeg, ip)] * Yf2[np.ix_(ydeg, rr)]
    return A


def direct_A(k, l, cst, Xi, x, y, tab, n):
    idx, pos, parent, op, start = tab
    Nn = Nof(n); M = Xi.shape[0]; R = np.zeros((M, Nn), dtype=LD); xl, yl = x.astype(LD), y.astype(LD)
    R[:, k] = Xi[:, l] / LD(cst[k][2])
    for c in range(k + 1, Nn):
        W, h, beta = cst[c]; p = parent[c]; a = xl if op[c] == 'J' else yl
        R[:, c] = (a * R[:, p] - R[:, W] @ np.asarray(h, dtype=LD)) / LD(beta)
    return Xi[:, :Nn].T @ R, np.sqrt(np.sum(R * R, axis=0))


def build_xi(cst, x, y, w, tab, N):
    idx, pos, parent, op, start = tab
    xl, yl = x.astype(LD), y.astype(LD); Xi = np.zeros((len(x), N), dtype=LD)
    v = np.sqrt(w.astype(LD)); Xi[:, 0] = v / np.sqrt(np.sum(v * v))
    for k in range(1, N):
        W, h, beta = cst[k]; p = parent[k]; a = xl if op[k] == 'J' else yl
        Xi[:, k] = (a * Xi[:, p] - Xi[:, W] @ np.asarray(h, dtype=LD)) / LD(beta)
    return Xi


def run(name, X, Y, nmax=24, ncheck=20, seeds=(0, 1, 2)):
    P, w, wx, wy = C.checkerboard(X, Y); x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, cbj, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    idx, pos, parent, op, start = tab; N = Q.shape[1]
    ax, bx = K.jacobi_1d_ld(X, wx, nmax); ay, by = K.jacobi_1d_ld(Y, wy, nmax)
    cst = K.ref_coefs(ax, bx, ay, by, tab); masks = K.pattern_mask(tab, N)
    Px, Py = univ(X, ax, bx, nmax), univ(Y, ay, by, nmax)
    ox = float(np.abs((Px * wx.astype(LD)) @ Px.T - np.eye(nmax + 1)).max())
    oy = float(np.abs((Py * wy.astype(LD)) @ Py.T - np.eye(nmax + 1)).max())
    Xi = build_xi(cst, x, y, w, tab, N)
    print(f"== {name}: M={len(x)}, univariate orthonormality defects {ox:.1e} (x), {oy:.1e} (y)", flush=True)
    uni = (Px, Py, wx, wy, X, Y, ax, bx, ay, by)
    # (1) identity check on sampled entries
    worst = 0.0; nchk = 0; rng = np.random.default_rng(7)
    ks = [pos[(t, j)] for (t, j) in [(4, 0), (6, 3), (9, 0), (10, 1), (12, 6), (14, 14), (15, 0), (17, 9)]]
    for k in ks:
        W = cst[k][0]; ls = list(W) if len(W) <= 12 else list(rng.choice(W, 12, replace=False))
        for l in ls:
            Af = formula_A(k, l, tab, ncheck, *uni); Ad, rn = direct_A(k, l, cst, Xi, x, y, tab, ncheck)
            scale = np.maximum(rn, LD(1e-300))[None, :]
            worst = max(worst, float((np.abs(Ad - Af) / scale).max())); nchk += 1
    print(f"   identity check: {nchk} entries, max_(e,d) |A_direct - A_formula| / ||R_d|| = {worst:.1e} "
          f"(criterion <= 1e-8: {'PASS' if worst <= 1e-8 else 'FAIL'})", flush=True)
    # (2) gain census and (3) first-order predictions at n = 16, 20
    n = 20; Nn = Nof(n); N16 = Nof(16)
    gains = {16: {'on': [], 'off': []}, 20: {'on': [], 'off': []}}
    deltas = {'BJ off-pattern values': [], **{f'abs u-noise off, seed {sd}': [] for sd in seeds}}
    noise = {}
    for sd in seeds:  # replicate the IDEA-117 noise draws exactly (same generator call order, N = N_24)
        r = np.random.default_rng(sd); noise[sd] = [None] + [r.standard_normal(len(cst[k][1])) * EPS for k in range(1, N)]
    acc = {lab: np.zeros((Nn, Nn)) for lab in deltas}
    for k in range(1, Nn):
        W = cst[k][0]
        for ii, l in enumerate(W):
            A = formula_A(k, l, tab, n, *uni); S = (A + A.T).astype(float)
            cls = 'on' if masks[k][ii] else 'off'
            gains[20][cls].append(float(np.abs(S).max())); gains[16][cls].append(float(np.abs(S[:N16, :N16]).max()))
            if not masks[k][ii]:
                acc['BJ off-pattern values'] += float(cbj[k][1][ii]) * S
                for sd in seeds:
                    acc[f'abs u-noise off, seed {sd}'] += float(noise[sd][k][ii]) * S
    for nn in (16, 20):
        g = gains[nn]
        print(f"   gains n={nn}: on-pattern max {max(g['on']):.1e} (median {np.median(g['on']):.1e}); "
              f"off-pattern max {max(g['off']):.1e} (median {np.median(g['off']):.1e}, "
              f"#>1e6: {sum(v > 1e6 for v in g['off'])}/{len(g['off'])})", flush=True)
    for lab, S in acc.items():
        print(f"   first-order D predicted, {lab:28s}: n16 {np.abs(S[:N16, :N16]).max():.1e}  n20 {np.abs(S).max():.1e}", flush=True)
    return gains


if __name__ == '__main__':
    print(f"# l1_r06_gain_identity.py numpy={np.__version__}")
    m = 30
    s1, s2 = np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)
    run('cubic-clustered checkerboard m=30', s1 * np.abs(s1) ** 2, s2 * np.abs(s2) ** 2)
    run('equispaced checkerboard m=30', s1, s2)
