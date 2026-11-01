"""Checks for the 2023-2026 open-problem round (Padua / Clenshaw-Curtis / MZ constants).

1. Padua hyperinterpolation (An-Ran-Wu survey, DRNA 18 (2025), Sec. 2.3, "remains an open problem"):
   Gram matrix of the orthonormal product-Chebyshev basis of P_n under the degree-n Padua rule.
2. Weak MZ constant eta = ||I - G||_2 (An-Sommariva-Vianello, arXiv 2601.04708) for
   (a) 1D Clenshaw-Curtis with N+1 Chebyshev-Lobatto nodes, orthonormal Legendre basis of degree n;
   (b) 2D interpolatory Padua rule for the Lebesgue measure on [-1,1]^2, orthonormal Legendre basis of P_n.
"""
import numpy as np
from numpy.polynomial import chebyshev as C, legendre as L


def padua(n):
    pts, w = [], []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                x, y = np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1))
                bx = j in (0, n)
                by = k in (0, n + 1)
                fac = 0.5 if (bx and by) else (1.0 if (bx or by) else 2.0)
                pts.append((x, y)); w.append(fac / (n * (n + 1)))
    return np.array(pts), np.array(w)


def cheb_hat(k, t):
    c = np.zeros(k + 1); c[k] = 1
    return C.chebval(t, c) * (1.0 if k == 0 else np.sqrt(2))


def leg_hat(k, t):  # orthonormal w.r.t. dx on [-1,1]
    c = np.zeros(k + 1); c[k] = 1
    return L.legval(t, c) * np.sqrt((2 * k + 1) / 2)


def total_degree(n):
    return [(a, b) for s in range(n + 1) for a in range(s, -1, -1) for b in [s - a]]


def padua_hyper_gram(n):
    P, w = padua(n)
    idx = total_degree(n)
    V = np.column_stack([cheb_hat(a, P[:, 0]) * cheb_hat(b, P[:, 1]) for a, b in idx])
    G = V.T @ (w[:, None] * V)
    ev = np.linalg.eigvalsh(G)
    off = G - np.diag(np.diag(G))
    return w.sum(), ev.min(), ev.max(), np.abs(off).max(), [idx[i] for i in np.where(np.abs(np.diag(G) - 1) > 1e-10)[0]]


def cc_eta(N, n):
    x = np.cos(np.pi * np.arange(N + 1) / N)
    # CC weights: integrate the interpolant exactly (Lebesgue measure)
    V = np.column_stack([C.chebval(x, np.eye(N + 1)[k]) for k in range(N + 1)])
    mom = np.array([0 if k % 2 else 2 / (1 - k * k) for k in range(N + 1)])
    w = np.linalg.solve(V.T, mom)
    B = np.column_stack([leg_hat(k, x) for k in range(n + 1)])
    G = B.T @ (w[:, None] * B)
    return np.linalg.norm(np.eye(n + 1) - G, 2), w.min()


def padua_leb_eta(m, n):
    P, _ = padua(m)
    idx_m = total_degree(m)
    V = np.column_stack([cheb_hat(a, P[:, 0]) * cheb_hat(b, P[:, 1]) for a, b in idx_m])
    def mom1(k):
        return 0.0 if k % 2 else 2 / (1 - k * k)
    mom = np.array([mom1(a) * mom1(b) * (1 if a == 0 else np.sqrt(2)) * (1 if b == 0 else np.sqrt(2)) for a, b in idx_m])
    w = np.linalg.lstsq(V.T, mom, rcond=None)[0]  # interpolatory weights (V square, unisolvent)
    idx = total_degree(n)
    B = np.column_stack([leg_hat(a, P[:, 0]) * leg_hat(b, P[:, 1]) for a, b in idx])
    G = B.T @ (w[:, None] * B)
    ev = np.linalg.eigvalsh((G + G.T) / 2)
    return max(abs(1 - ev.min()), abs(1 - ev.max())), np.linalg.cond(G), (w < 0).sum()


if __name__ == "__main__":
    print("1) Padua rule, product-Chebyshev orthonormal basis of P_n:")
    for n in (4, 9, 16):
        s, lo, hi, off, bad = padua_hyper_gram(n)
        print(f"  n={n}: sum w={s:.15f}  eig(G) in [{lo:.12f},{hi:.12f}]  max|offdiag|={off:.1e}  diag!=1 at {bad}")
    print("2a) Clenshaw-Curtis, N+1 nodes, Legendre basis degree n: eta=||I-G||")
    for N in (10, 21, 40, 81):
        row = []
        for n in (N // 2, N // 2 + 1, N - 2, N - 1, N, N + 1):
            row.append(f"n={n}:{cc_eta(N, n)[0]:.3f}")
        print(f"  N={N}: " + "  ".join(row))
    print("2b) Padua interpolatory rule for Lebesgue measure (degree m), Legendre basis of P_n:")
    for m in (10, 20, 31):
        row = []
        for n in (m // 2, m // 2 + 1, m - 2, m - 1, m, m + 1):
            e, c, neg = padua_leb_eta(m, n)
            row.append(f"n={n}:eta={e:.3f},cond={c:.1e}")
        print(f"  m={m} (neg. weights: {padua_leb_eta(m, 1)[2]}): " + "  ".join(row))
