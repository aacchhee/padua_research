"""R04: Harris-Simanek checkerboard control (IDEA?bivariate-lanczos-claude-113, PD-T?...-111).
S_e = {(x_i, y_j) : i + j = e mod 2}, X ordered (m+1 points), Y ordered (m+2 points), weights |1/omega_X'(x_i)| *
|1/omega_Y'(y_j)| (normalised), M = N_m.  Checks (C1) product type of the exact window coefficients below degree m
against the product reference (X, |w_X|) (x) (Y, |w_Y|), (C2) 2D BJ loss vs univariate Lanczos losses of the two
factors, and reports the propagator response.  MEASURED only.
Usage: python3 -I l1_r04_checkerboard.py > logs/r04_checkerboard.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_near_product as R

EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2


def alt_weights(h):
    """|1/omega_h'(h_i)| computed in logs, normalised to sum 1."""
    lw = np.array([-np.sum(np.log(np.abs(h[i] - np.delete(h, i)))) for i in range(len(h))])
    w = np.exp(lw - lw.max()); return w / w.sum()


def checkerboard(X, Y, e=0):
    wx, wy = alt_weights(X), alt_weights(Y)
    pts, w = [], []
    for i in range(len(X)):
        for j in range(len(Y)):
            if (i + j) % 2 == e:
                pts.append((X[i], Y[j])); w.append(wx[i] * wy[j])
    w = np.array(w); return np.array(pts), w / w.sum(), wx, wy


def lanczos_loss_1d(t, w, n):
    """Plain univariate Lanczos (no reorthogonalisation): loss max|Q_k^T Q_k - I| for k = 1..n+1 vectors."""
    M = len(t); Q = np.zeros((M, n + 1)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    b_prev = 0.0
    for k in range(n):
        u = t * Q[:, k] - (b_prev * Q[:, k - 1] if k > 0 else 0)
        a = Q[:, k] @ u; u = u - a * Q[:, k]
        b = np.linalg.norm(u); Q[:, k + 1] = u / b; b_prev = b
    G = Q.T @ Q
    return [float(np.abs(G[:k + 1, :k + 1] - np.eye(k + 1)).max()) for k in range(n + 1)]


def run(name, X, Y, m):
    P, w, wx, wy = checkerboard(X, Y)
    x, y = P[:, 0].copy(), P[:, 1].copy()
    M = len(x)
    assert M == Nof(m), (M, Nof(m))
    nmax = m - 1
    coef, tab = R.exact_coefs(x, y, w, nmax)
    idx, pos, parent, op, start = tab
    # product reference built from the FACTOR measures (X, wx), (Y, wy)
    ax, bx = R.jacobi_1d(X, wx, nmax); ay, by = R.jacobi_1d(Y, wy, nmax)
    dev, coup = 0.0, 0.0
    for k in range(1, Nof(nmax)):
        t, j = idx[k]; W, h, beta = coef[k]
        ref = np.zeros(len(W))
        for ii, l in enumerate(W):
            if j == 0:
                if idx[l] == (t - 1, 0): ref[ii] = ax[t - 1]
                if idx[l] == (t - 2, 0): ref[ii] = bx[t - 1]
            else:
                if idx[l] == (t - 1, j - 1): ref[ii] = ay[j - 1]
                if idx[l] == (t - 2, j - 2): ref[ii] = by[j - 1]
            if idx[l][0] == t and idx[l][1] >= 1 and j >= 1:
                coup = max(coup, abs(h[ii]) / beta)
        rb = bx[t] if j == 0 else by[j]
        dev = max(dev, float(np.abs(h - ref).max()), abs(beta - rb))
    # 2D BJ loss up to degree m (complete basis at degree m)
    Q, cbj, tbj = L.recurrence(x, y, w, m, win='block', orth='cgs')
    G = Q.T @ Q
    loss2 = {t: float(np.abs(G[:Nof(t), :Nof(t)] - np.eye(Nof(t))).max()) for t in range(1, m + 1)}
    lx = lanczos_loss_1d(X, wx, m); ly = lanczos_loss_1d(Y, wy, m + 1)
    worst = 0.0
    for t in range(1, m - 1):
        ref = max(1e3 * EPS, lx[t], ly[t])
        worst = max(worst, loss2[t] / ref)
    print(f"== {name}: m={m} M={M} min wx={wx.min():.1e} min wy={wy.min():.1e}", flush=True)
    print(f"   (C1) max |window coef - product-reference coef| (deg <= {nmax}) = {dev:.1e};  max within-degree coupling ratio = {coup:.1e}")
    print("   2D BJ loss t=4,8,..: " + " ".join(f"{t}:{loss2[t]:.0e}" for t in range(4, m + 1, 4)) + f" | t={m}: {loss2[m]:.0e}")
    print("   1D Lanczos loss X  : " + " ".join(f"{t}:{lx[t]:.0e}" for t in range(4, m + 1, 4)))
    print("   1D Lanczos loss Y  : " + " ".join(f"{t}:{ly[t]:.0e}" for t in range(4, m + 2, 4)))
    print(f"   (C2) max_t<=m-2 loss2D / max(1e3u, Lx, Ly) = {worst:.1e}", flush=True)


if __name__ == '__main__':
    print(f"# l1_r04_checkerboard.py numpy={np.__version__}")
    m = 30
    run('Chebyshev-Lobatto (Padua-type)', -np.cos(np.arange(m + 1) * np.pi / m), -np.cos(np.arange(m + 2) * np.pi / (m + 1)), m)
    run('equispaced', np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2), m)
    s1, s2 = np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)
    run('clustered (cubic at 0)', s1 * np.abs(s1) ** 2, s2 * np.abs(s2) ** 2, m)
