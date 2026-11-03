"""Exploratory float64 evaluation of the Padua Lebesgue function and its
shifted-lattice majorant (topic padua-argmax-alln-20261101).

Status: MEASURED exploration only (float64, NumPy). Not a certificate.

Conventions (as in PD-T101 / OPEN_TARGETS of programme-ideas-20261031):
nodes B_jk = (cos th_j, cos ph_k), th_j = j*pi/n, ph_k = k*pi/(n+1),
0<=j<=n, 0<=k<=n+1, j+k even; weights w_jk = 2 eps_j eta_k / (n(n+1))
(eps, eta = 1/2 at the ends), normalised to total mass 1.

Kernel: L_B(x) = w_B * Ktilde(x, B) with
  Ktilde = sum_{a+b<=n} c_ab T_a(x1) T_b(x2) T_a(B1) T_b(B2),
  c_ab = h_a h_b (h_0 = 1, h_k = 2), except c_{n,0} = 1 (half of h_n h_0).
Because T_a(cos t) T_a(cos s) = (cos a(t+s) + cos a(t-s))/2,
  Ktilde = 1/4 * sum_{s1,s2 = +-1} g(theta + s1 th_j, phi + s2 ph_k),
  g(u, v) = sum_ab c_ab cos(a u) cos(b v).
lambda_n(x) = sum_B w_B |1/4 sum_s g(...)|      (exact identity)
majorant(x) = sum_B w_B  1/4 sum_s |g(...)|      (>= lambda_n; = at corners)

check.py verifies the kernel against direct Vandermonde inversion (n = 3, 4).
"""
import numpy as np
import sys


def setup(n):
    J = np.arange(n + 1)
    K = np.arange(n + 2)
    th = J * np.pi / n
    ph = K * np.pi / (n + 1)
    eps = np.where((J == 0) | (J == n), .5, 1.)
    eta = np.where((K == 0) | (K == n + 1), .5, 1.)
    W = 2 * np.outer(eps, eta) / (n * (n + 1))
    mask = ((J[:, None] + K[None, :]) % 2 == 0)
    W = W * mask
    a = np.arange(n + 1)
    h = np.where(a == 0, 1., 2.)
    C = np.outer(h, h) * ((a[:, None] + a[None, :]) <= n)
    C[n, 0] = 1.0
    return th, ph, W, C, a


def lam(n, X, Y, S):
    """Return (lambda_n, majorant) at the angle points (X[i], Y[i])."""
    th, ph, W, C, a = S
    out_l = []
    out_m = []
    for t, p in zip(X, Y):
        G = []
        for s1 in (1, -1):
            Cu = np.cos(np.outer(t + s1 * th, a))
            for s2 in (1, -1):
                Cv = np.cos(np.outer(p + s2 * ph, a))
                G.append(Cu @ C @ Cv.T)
        G = np.array(G)
        out_l.append((W * np.abs(G.mean(0))).sum())
        out_m.append((W * np.abs(G).mean(0)).sum())
    return np.array(out_l), np.array(out_m)


if __name__ == "__main__":
    # Coarse whole-square scan: lambda_n and majorant on a 161x161 angle grid.
    for n in [int(v) for v in sys.argv[1:]]:
        S = setup(n)
        M = 161
        T = np.linspace(0, np.pi, M)
        X, Y = np.meshgrid(T, T, indexing='ij')
        l, m = lam(n, X.ravel(), Y.ravel(), S)
        Lc = max(lam(n, [0.0], [np.pi], S)[0][0], lam(n, [np.pi], [0.0], S)[0][0])
        l = l.reshape(M, M)
        m = m.reshape(M, M)
        edge = np.zeros_like(l, bool)
        edge[0, :] = edge[-1, :] = edge[:, 0] = edge[:, -1] = True
        print(n, "Lc=%.5f" % Lc, "grid max lam=%.5f" % l.max(),
              "grid max maj=%.5f" % m.max(), "maj-Lc=%.2e" % (m.max() - Lc),
              "grid interior lam max=%.4f" % l[~edge].max(),
              "grid edge lam max(non-corner)=%.4f" % np.max(
                  [l[0, 1:-1].max(), l[-1, 1:-1].max(), l[1:-1, 0].max(), l[1:-1, -1].max()]))
