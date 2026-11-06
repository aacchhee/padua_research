import numpy as np
from numpy.polynomial.legendre import leggauss
import scipy.linalg as sla


def cc_weights(N):
    k = np.arange(N + 1)
    th = k * np.pi / N
    w = np.ones(N + 1)
    for j in range(1, N // 2 + 1):
        b = 1.0 if 2 * j == N else 2.0
        w -= b / (4 * j * j - 1) * np.cos(2 * j * th)
    c = np.full(N + 1, 2.0); c[0] = c[-1] = 1.0
    return c * w / N


def cheb_mass(N):
    n = np.arange(2 * N + 1)
    m = np.where(n % 2 == 0, 2.0 / (1.0 - n.astype(float) ** 2), 0.0)
    i = np.arange(N + 1)
    return 0.5 * (m[i[:, None] + i[None, :]] + m[np.abs(i[:, None] - i[None, :])])


def coef_matrix(N):
    """b = C u gives p = sum_j b_j T_j (ends already halved)."""
    j = np.arange(N + 1); k = np.arange(N + 1)
    C = (2.0 / N) * np.cos(np.outer(j, k) * np.pi / N)
    C[:, 0] *= 0.5; C[:, -1] *= 0.5
    C[0, :] *= 0.5; C[-1, :] *= 0.5
    return C


def gram(N):
    C = coef_matrix(N)
    return C.T @ cheb_mass(N) @ C, C


def lam_min(N, sub=False):
    G, C = gram(N)
    w = cc_weights(N)
    s = 1 / np.sqrt(w)
    A = s[:, None] * G * s[None, :]
    if sub:
        # restrict to b_N = 0 : row C[N,:] u = 0, i.e. (C[N]*s) v = 0
        c = C[-1] * s; c = c / np.linalg.norm(c)
        P = np.eye(N + 1) - np.outer(c, c)
        A = P @ A @ P
    ev, V = np.linalg.eigh(A)
    mu = ev[-1]; v = V[:, -1]
    return 1 / mu, s * v, w   # lambda_min, nodal minimizer u, weights


def eval_interp(u, N, theta):
    C = coef_matrix(N)
    b = C @ u
    out = np.zeros_like(theta)
    for j0 in range(0, N + 1, 256):
        jj = np.arange(j0, min(N + 1, j0 + 256))
        out += np.cos(np.outer(theta, jj)) @ b[jj]
    return out


def cell_grid(T, q=12):
    """Gauss nodes on unit cells covering [0,T]."""
    x, wq = leggauss(q)
    m = int(np.ceil(T))
    a = np.arange(m)
    b = np.minimum(a + 1.0, T)
    t = (a[:, None] + b[:, None]) / 2 + (b - a)[:, None] / 2 * x[None, :]
    wt = (b - a)[:, None] / 2 * wq[None, :]
    return t.ravel(), wt.ravel()
