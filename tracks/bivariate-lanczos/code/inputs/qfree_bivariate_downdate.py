"""Q-free (truncated) up/downdating of bivariate discrete OPs: the 2D transcription of
Elhay-Golub-Kautsky (SIMAX 1991) sec. 4.5/5.2 (Cholesky factor of a rank-one modification
of the identity, 'special form of L' from Gill-Golub-Murray-Saunders 1974).

State kept: only the N x N sections Hx = Phi^T X Phi, Hy = Phi^T Y Phi of the orthonormal
(graded-lex) basis of Pi_n on the current weighted node set (N = dim Pi_n), plus sum of weights.
No M x M (or M x N) Q is stored.

Up/downdate by node z=(x0,y0), weight w:
  u = sqrt(w) * p(z)        (p evaluated by the recurrence encoded in Hx, Hy)
  L L^T = I +/- u u^T       (downdate exists iff ||u||^2 = w K_n(z,z) < 1: leverage < 1;
                             this is EGK Thm 5.2's condition ||q|| < 1)
  Hx <- L^{-1} (Hx +/- x0 u u^T) L^{-T},  Hy likewise.
Exact in exact arithmetic (Phi_new = Phi_+/- L^{-T}; L lower triangular keeps graded spans).
Reference: recompute from scratch by QR of the weighted Chebyshev-Vandermonde.
"""
import numpy as np
rng = np.random.default_rng(0)

def gl(n):  # graded order: degree t, inside degree x-power increasing
    return [(i, t - i) for t in range(n + 1) for i in range(t + 1)]

def parents(n):
    idx = gl(n); pos = {m: k for k, m in enumerate(idx)}; par = [None]
    for (i, j) in idx[1:]:
        par.append((pos[(i - 1, j)], 0) if i > 0 else (pos[(0, j - 1)], 1))
    return par

def ref_H(pts, w, n):
    idx = gl(n); x, y = pts[:, 0], pts[:, 1]
    V = np.column_stack([np.cos(a * np.arccos(x)) * np.cos(b * np.arccos(y)) for a, b in idx])
    Q, R = np.linalg.qr(np.sqrt(w)[:, None] * V)
    Q = Q * np.sign(np.diag(R))
    # fix signs so that recurrence pivots are positive (same convention as graded Cholesky)
    Hx, Hy = Q.T @ (x[:, None] * Q), Q.T @ (y[:, None] * Q)
    par = parents(n); s = np.ones(len(idx))
    for j in range(1, len(idx)):
        jp, v = par[j]; H = Hx if v == 0 else Hy
        s[j] = s[jp] * np.sign(H[j, jp])
    Q = Q * s; return Q.T @ (x[:, None] * Q), Q.T @ (y[:, None] * Q)

def evalp(Hx, Hy, z, sw, n):
    par = parents(n); N = Hx.shape[0]; p = np.zeros(N); p[0] = 1 / np.sqrt(sw)
    for j in range(1, N):
        jp, v = par[j]; H = (Hx, Hy)[v]
        p[j] = (z[v] * p[jp] - H[:j, jp] @ p[:j]) / H[j, jp]
    return p

def modify(Hx, Hy, sw, z, w, n, sign):
    u = np.sqrt(w) * evalp(Hx, Hy, z, sw, n)
    lev = u @ u
    L = np.linalg.cholesky(np.eye(len(u)) + sign * np.outer(u, u))
    Li = np.linalg.inv(L)          # demo only; structured O(N) solves exist (GGMS special form)
    return (Li @ (Hx + sign * z[0] * np.outer(u, u)) @ Li.T,
            Li @ (Hy + sign * z[1] * np.outer(u, u)) @ Li.T, sw + sign * w, lev)

def run(M, W, n, steps, dist="uniform"):
    if dist == "uniform": pts = rng.uniform(-1, 1, (M, 2))
    else: pts = np.cos(np.pi * rng.uniform(0, 1, (M, 2)))   # Chebyshev-like clustering
    w = rng.uniform(0.5, 1.5, M)
    Hx, Hy = ref_H(pts[:W], w[:W], n); sw = w[:W].sum()
    errs, levs = [], []
    for k in range(steps):
        Hx, Hy, sw, _ = modify(Hx, Hy, sw, pts[W + k], w[W + k], n, +1)      # update (new point)
        Hx, Hy, sw, lev = modify(Hx, Hy, sw, pts[k], w[k], n, -1)            # downdate (oldest)
        levs.append(lev)
        if (k + 1) % max(1, steps // 5) == 0:
            Rx, Ry = ref_H(pts[k + 1:W + k + 1], w[k + 1:W + k + 1], n)
            errs.append((k + 1, max(np.abs(Hx - Rx).max(), np.abs(Hy - Ry).max())))
    return errs, max(levs)

if __name__ == "__main__":
    for (M, W, n, steps, dist) in [(1200, 400, 8, 800, "uniform"), (1200, 400, 12, 800, "uniform"),
                                   (1200, 150, 12, 800, "uniform"), (1200, 100, 12, 600, "uniform"),
                                   (1200, 400, 12, 800, "cheb"), (1200, 95, 12, 300, "uniform")]:
        N = (n + 1) * (n + 2) // 2
        errs, lmax = run(M, W, n, steps, dist)
        print(f"W={W:4d} N={N:3d} n={n:2d} {dist:7s} max leverage={lmax:.3f}  err vs recompute:",
              " ".join(f"[{k}] {e:.1e}" for k, e in errs))
