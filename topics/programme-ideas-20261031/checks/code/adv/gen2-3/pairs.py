"""Shared constructions for the adversarial check of gen2-draft-3 (two-index Sturm counts).

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). Adversarial check gen2-3, 2026-11-01.

Builds commuting symmetric block-tridiagonal pairs (H_x, H_y) exactly as the generator's
probe does (graded-lex Chebyshev-Vandermonde, weighted QR, H = Q^T diag(x) Q), plus the
Padua pair, an unpivoted LDL^T inertia routine (the "banded Sturm" evaluation; with the
option of truncating to the exact block band), and the generator's box-count formula.
Everything here is a seconds-long probe; results are MEASURED only in their stated scope.
"""
import numpy as np
from numpy.polynomial import chebyshev as C


def graded_cheb_vandermonde(x, y, n):
    cols = []
    deg = []
    for k in range(n + 1):
        for i in range(k, -1, -1):
            j = k - i
            cols.append(C.chebval(x, np.eye(i + 1)[i]) * C.chebval(y, np.eye(j + 1)[j]))
            deg.append(k)
    return np.array(cols).T, np.array(deg)


def pair_from_nodes(x, y, w, n):
    """Sections H_x = Q^T X Q, H_y = Q^T Y Q from the weighted graded Chebyshev Vandermonde (square case M = N)."""
    V, deg = graded_cheb_vandermonde(x, y, n)
    Q, R = np.linalg.qr(np.sqrt(w)[:, None] * V)
    Hx = Q.T @ (x[:, None] * Q)
    Hy = Q.T @ (y[:, None] * Q)
    return Hx, Hy, deg


def random_pair(n, seed=1):
    rng = np.random.default_rng(seed)
    N = (n + 1) * (n + 2) // 2
    x = rng.uniform(-1, 1, N)
    y = rng.uniform(-1, 1, N)
    w = rng.uniform(0.5, 1.5, N)
    Hx, Hy, deg = pair_from_nodes(x, y, w, n)
    return Hx, Hy, deg, x, y, w


def padua_points(n):
    """Padua points of degree n (one of the four families) and the Padua cubature weights
    (normalised product-Chebyshev measure of total mass 1).  Checked below by exactness on Pi_{2n-1}."""
    pts = []
    wts = []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                xj = np.cos(j * np.pi / n)
                yk = np.cos(k * np.pi / (n + 1))
                edge_x = j in (0, n)
                edge_y = k in (0, n + 1)
                if edge_x and edge_y:
                    f = 0.5
                elif edge_x or edge_y:
                    f = 1.0
                else:
                    f = 2.0
                pts.append((xj, yk))
                wts.append(f / (n * (n + 1)))
    P = np.array(pts)
    return P[:, 0], P[:, 1], np.array(wts)


def padua_exactness_residual(n):
    x, y, w = padua_points(n)
    V, _ = graded_cheb_vandermonde(x, y, 2 * n - 1)
    mom = w @ V  # should be e_1 (only T_0 T_0 has nonzero mean)
    tgt = np.zeros_like(mom); tgt[0] = 1.0
    return np.abs(mom - tgt).max()


def ldl_inertia(S, band=None, return_growth=False):
    """Unpivoted LDL^T (the banded Sturm evaluation; no pivoting, so the band is preserved).
    If band is an array of degree labels and width b, entries with |deg_i - deg_j| > b are
    treated as exact zeros first (the banded algorithm never touches them).
    Returns (#positive pivots, #negative pivots, #zero pivots[, growth factor])."""
    A = np.array(S, dtype=float, copy=True)
    N = A.shape[0]
    if band is not None:
        deg, b = band
        mask = np.abs(deg[:, None] - deg[None, :]) > b
        A[mask] = 0.0
    amax0 = np.abs(A).max()
    npos = nneg = nzero = 0
    growth = 1.0
    for k in range(N):
        d = A[k, k]
        if d > 0:
            npos += 1
        elif d < 0:
            nneg += 1
        else:
            nzero += 1
            continue  # breakdown; skip (does not happen in practice with random data)
        if k + 1 < N:
            col = A[k + 1:, k]
            nz = np.nonzero(col)[0]
            if nz.size:
                lo, hi = nz.min(), nz.max() + 1
                c = col[lo:hi]
                A[k + 1 + lo:k + 1 + hi, k + 1 + lo:k + 1 + hi] -= np.outer(c, c) / d
                growth = max(growth, np.abs(A[k + 1 + lo:k + 1 + hi, k + 1 + lo:k + 1 + hi]).max() / amax0)
    if return_growth:
        return npos, nneg, nzero, growth
    return npos, nneg, nzero


def eig_inertia(S):
    ev = np.linalg.eigvalsh(0.5 * (S + S.T))
    return int((ev > 0).sum())


def box_matrices(Hx, Hy, a, a2, b, b2):
    N = Hx.shape[0]
    I = np.eye(N)
    Mx = (Hx - a * I) @ (a2 * I - Hx)
    My = (Hy - b * I) @ (b2 * I - Hy)
    P = Mx @ My
    S = 0.5 * (P + P.T)
    return Mx, My, S


def box_count_numerator(nx, ny, nprod, N):
    """n_box = (nprod - N + nx + ny)/2; returns the numerator (odd numerator = not a count)."""
    return nprod - N + nx + ny


def line_distance(x, y, a, a2, b, b2):
    """Distance of the four boundary lines to the nearest node coordinate (generator's criterion)."""
    return min(np.abs(np.r_[x - a, x - a2]).min(), np.abs(np.r_[y - b, y - b2]).min())
