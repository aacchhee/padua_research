"""R04: node-propagator predictor with componentwise-scaled forcing.  The R02 predictor (PD-T?...-107 (c)) drove
the propagator with iid forcing u/sqrt(M) at every node; for strongly non-uniform node magnitudes (triangle corners,
clustered checkerboards with weights down to 1e-33) the actual local error at node i is ~ u (|a q_p(i)| +
sum |h_l||q_l(i)| + beta |q_k(i)|) instead.  Drive the propagator with forcing u*N(0,1)*(that magnitude), computed
from the run's own vectors, with (a) the run's coefficients and (b) where available the product-reference
coefficients (factorised propagator, PD-T?...-105).  Compare with the measured loss.  MEASURED only.
Usage: python3 -I l1_r04_scaled_predictor.py > logs/r04_scaled_predictor.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_near_product as R
import l1_r04_checkerboard as C

EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2


def scaled_response(x, y, Q, coef_run, coef_prop, tab, N, seed=0):
    idx, pos, parent, op, start = tab
    M = len(x); rng = np.random.default_rng(seed)
    g = np.zeros((M, N)); g[:, 0] = rng.standard_normal(M) * EPS * np.abs(Q[:, 0])
    for k in range(1, N):
        W, h, beta = coef_run[k]; p = parent[k]; a = x if op[k] == 'J' else y
        mag = np.abs(a * Q[:, p]) + np.abs(Q[:, W]) @ np.abs(h) + beta * np.abs(Q[:, k])
        Wp, hp, bp = coef_prop[k]
        g[:, k] = (a * g[:, p] - g[:, Wp] @ np.asarray(hp, dtype=float) + rng.standard_normal(M) * EPS * mag) / float(bp)
    return np.linalg.norm(g, axis=0)


def run(name, P, w, nmax, ref_factors=None, step=4):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, coef, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    N = Q.shape[1]; G = Q.T @ Q
    pa = scaled_response(x, y, Q, coef, coef, tab, N)
    pb = None
    if ref_factors is not None:
        (X, wx), (Y, wy) = ref_factors
        ax, bx = R.jacobi_1d(X, wx, nmax); ay, by = R.jacobi_1d(Y, wy, nmax)
        ref = []
        idx, pos, parent, op, start = tab
        ref = [None] * N
        for k in range(1, N):
            t, j = idx[k]; W = coef[k][0]; h = np.zeros(len(W))
            for ii, l in enumerate(W):
                if j == 0:
                    if idx[l] == (t - 1, 0): h[ii] = ax[t - 1]
                    if idx[l] == (t - 2, 0): h[ii] = bx[t - 1]
                else:
                    if idx[l] == (t - 1, j - 1): h[ii] = ay[j - 1]
                    if idx[l] == (t - 2, j - 2): h[ii] = by[j - 1]
            ref[k] = (W, h, bx[t] if j == 0 else by[j])
        pb = scaled_response(x, y, Q, coef, ref, tab, N)
    out = []
    for n in range(step, nmax + 1, step):
        Nn = Nof(n); loss = np.abs(G[:Nn, :Nn] - np.eye(Nn)).max()
        s = f"n{n}: L={loss:.0e} Ps={pa[:Nn].max():.0e}"
        if pb is not None: s += f" Ps_factorised={pb[:Nn].max():.0e}"
        out.append(s)
    print(f"{name:30s} " + " | ".join(out), flush=True)


if __name__ == '__main__':
    print(f"# l1_r04_scaled_predictor.py numpy={np.__version__}")
    rng = np.random.default_rng(11)
    M = 1681
    sq = rng.uniform(-1, 1, (M, 2)); one = np.ones(M)
    run('square', sq, one, 32)
    run('square rot pi/4', L.rotate(sq, np.pi / 4), one, 24)
    dk = []
    while len(dk) < M:
        p = rng.uniform(-1, 1, 2)
        if p @ p <= 1: dk.append(p)
    run('disk', np.array(dk), one, 24)
    tr = []
    while len(tr) < M:
        p = rng.uniform(0, 1, 2)
        if p.sum() <= 1: tr.append(2 * p - 1)
    run('triangle', np.array(tr), one, 20)
    m = 30
    for lab, X, Y in [('checkerboard Cheb-Lobatto', -np.cos(np.arange(m + 1) * np.pi / m), -np.cos(np.arange(m + 2) * np.pi / (m + 1))),
                      ('checkerboard equispaced', np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)),
                      ('checkerboard clustered', np.linspace(-1, 1, m + 1) ** 3, np.linspace(-1, 1, m + 2) ** 3)]:
        Pc, wc, wx, wy = C.checkerboard(X, Y)
        run(lab, Pc, wc, m - 1, ref_factors=((X, wx), (Y, wy)))
