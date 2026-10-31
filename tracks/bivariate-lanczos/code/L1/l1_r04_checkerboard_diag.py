"""R04 diagnosis of the clustered checkerboard: (i) are the exact window coefficients product type when computed in
long double (C1 re-check at higher precision)?  (ii) propagator responses at the nodes with (a) the BJ run's computed
coefficients, (b) the product-reference coefficients (univariate Jacobi coefficients of the factors, long double),
(c) the double CGS2 coefficients.  MEASURED only.  Usage: python3 -I l1_r04_checkerboard_diag.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_near_product as R
import l1_r04_checkerboard as C

LD = np.longdouble
EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2


def exact_coefs_ld(x, y, w, nmax):
    idx, pos, parent, op, start = L.tables(nmax)
    N = len(idx); M = len(x); xl, yl = x.astype(LD), y.astype(LD)
    Q = np.zeros((M, N), dtype=LD); v = np.sqrt(w.astype(LD)); Q[:, 0] = v / np.sqrt(np.sum(v * v))
    coef = [None] * N
    for k in range(1, N):
        p = parent[k]; a = xl if op[k] == 'J' else yl
        u0 = a * Q[:, p]; u = u0.copy()
        for _ in range(3):
            u = u - Q[:, :k] @ (Q[:, :k].T @ u)
        beta = np.sqrt(np.sum(u * u)); Q[:, k] = u / beta
        W = L.window(k, idx, start, 'block')
        coef[k] = (W, Q[:, W].T @ u0, beta)
    return coef, (idx, pos, parent, op, start)


def jacobi_1d_ld(t, w, n):
    t = t.astype(LD); M = len(t); Q = np.zeros((M, n + 2), dtype=LD); v = np.sqrt(w.astype(LD))
    Q[:, 0] = v / np.sqrt(np.sum(v * v)); a = np.zeros(n + 1, dtype=LD); b = np.zeros(n + 2, dtype=LD)
    for k in range(n + 1):
        u = t * Q[:, k]; a[k] = Q[:, k] @ u
        for _ in range(3):
            u = u - Q[:, :k + 1] @ (Q[:, :k + 1].T @ u)
        b[k + 1] = np.sqrt(np.sum(u * u)); Q[:, k + 1] = u / b[k + 1]
    return a, b


def ref_coefs(ax, bx, ay, by, tab):
    idx, pos, parent, op, start = tab
    N = len(idx); coef = [None] * N
    for k in range(1, N):
        t, j = idx[k]; W = L.window(k, idx, start, 'block'); h = np.zeros(len(W), dtype=LD)
        for ii, l in enumerate(W):
            if j == 0:
                if idx[l] == (t - 1, 0): h[ii] = ax[t - 1]
                if idx[l] == (t - 2, 0): h[ii] = bx[t - 1]
            else:
                if idx[l] == (t - 1, j - 1): h[ii] = ay[j - 1]
                if idx[l] == (t - 2, j - 2): h[ii] = by[j - 1]
        coef[k] = (W, h, bx[t] if j == 0 else by[j])
    return coef


def response(x, y, coef, tab, N, seed=0):
    idx, pos, parent, op, start = tab
    M = len(x); rng = np.random.default_rng(seed)
    g = np.zeros((M, N)); g[:, 0] = rng.standard_normal(M) * EPS / np.sqrt(M)
    for k in range(1, N):
        W, h, beta = coef[k]; p = parent[k]; a = x if op[k] == 'J' else y
        g[:, k] = (a * g[:, p] - g[:, W] @ np.asarray(h, dtype=float) + rng.standard_normal(M) * EPS / np.sqrt(M)) / float(beta)
    cn = np.linalg.norm(g, axis=0)
    return {n: cn[:Nof(n)].max() for n in range(4, 29, 4)}


m = 30
s1, s2 = np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)
X, Y = s1 * np.abs(s1) ** 2, s2 * np.abs(s2) ** 2
P, w, wx, wy = C.checkerboard(X, Y)
x, y = P[:, 0].copy(), P[:, 1].copy()
nmax = m - 1
cld, tab = exact_coefs_ld(x, y, w, nmax)
ax, bx = jacobi_1d_ld(X, wx, nmax); ay, by = jacobi_1d_ld(Y, wy, nmax)
cref = ref_coefs(ax, bx, ay, by, tab)
dev = max(float(np.abs(cld[k][1] - cref[k][1]).max()) for k in range(1, Nof(nmax)))
devb = max(float(abs(cld[k][2] - cref[k][2])) for k in range(1, Nof(nmax)))
print(f"clustered checkerboard m={m}: long-double |coef - product reference| max {dev:.1e}, |beta - ref| max {devb:.1e}")
Qbj, cbj, tbj = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
cdb, _ = R.exact_coefs(x, y, w, nmax)
N = Nof(nmax)
for lab, cf in [('BJ computed (double)', cbj), ('CGS2 double', cdb), ('product reference (ld)', cref), ('exact 2D (ld)', cld)]:
    r = response(x, y, cf, tab, N)
    print(f"   propagator response, {lab:24s}: " + " ".join(f"n{n}:{v:.0e}" for n, v in r.items()), flush=True)
dbj = max(float(np.abs(np.asarray(cbj[k][1], dtype=LD) - cref[k][1]).max()) for k in range(1, N))
print(f"   max |BJ computed coef - product reference| = {dbj:.1e}")
