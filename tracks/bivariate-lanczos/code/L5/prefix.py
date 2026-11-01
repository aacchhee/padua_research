"""L5: prefix-unisolvence tests and unisolvent-prefix node orders.

Prefix K of an order: first K nodes z_1..z_K versus the first K monomials m_1..m_K of the graded order
(1, x, y, x^2, xy, y^2, ... as in monos(); x-power decreasing within a degree).  The prefix is unisolvent iff
det[m_j(z_i)]_{i,j<=K} != 0.  Writing V = Vandermonde of the whole (square, M = N) Padua set in the product Chebyshev basis
(same flag as the monomials: T_a(x)T_b(y) = x^a y^b + terms of lower total degree) and Q_c = diag(sqrt(w_cub)) V D with the
cubature weights and column normalisations of padua_weights_check.py, Q_c is orthogonal and leading K x K blocks of the row-permuted
Q_c are nonsingular iff the prefix is unisolvent (row scaling by positive weights and triangular change of basis do not change this).
sigma_min(B_K), B_K = Q_c[perm[:K], :K], is therefore a well-scaled measure in [0,1].

Exact singular certificate (pure combinatorics): if the first K nodes have only c distinct x-values and c(c+1)/2 < K (x^c is the
first monomial of degree c, index c(c+1)/2 in 0-based graded order), then prod_j (x - x_j) is a nonzero polynomial in the span of the
first K monomials vanishing at all K nodes => singular.  For c distinct y-values the monomial y^c is the last of its degree block,
so the condition is (c+1)(c+2)/2 <= K.
"""
import numpy as np
import scipy.linalg as sla
import l5_lib as L
F = L.F

def padua_orthogonal_basis(n):
    """returns (P, w_cub, Qc) with Qc the M x M orthogonal matrix sqrt(w) * orthonormal product-Chebyshev basis (graded order)."""
    P, w = L.padua_cubature(n); M = len(P)
    x, y = P[:, 0], P[:, 1]
    tx = np.cos(np.outer(np.arccos(np.clip(x, -1, 1)), np.arange(n + 1)))
    ty = np.cos(np.outer(np.arccos(np.clip(y, -1, 1)), np.arange(n + 1)))
    cols = []
    for a, b in F.monos(M):
        s = (np.sqrt(2) if a > 0 else 1.0) * (np.sqrt(2) if b > 0 else 1.0)
        cols.append(s * tx[:, a] * ty[:, b])
    V = np.array(cols).T
    G = V.T @ (w[:, None] * V)          # diagonal up to rounding; the (n, 0) element has norm^2 = 2 (Padua aliasing)
    Qc = np.sqrt(w)[:, None] * V / np.sqrt(np.diag(G))
    return P, w, Qc

def combinatorial_singular(x, y):
    """boolean array sing[K-1] = True if prefix K is certified singular by the line criterion (distinct x or y values)."""
    M = len(x); out = np.zeros(M, bool); sx, sy = set(), set()
    for K in range(1, M + 1):
        sx.add(round(float(x[K - 1]), 13)); sy.add(round(float(y[K - 1]), 13))
        cx, cy = len(sx), len(sy)
        out[K - 1] = (cx * (cx + 1) // 2 < K) or ((cy + 1) * (cy + 2) // 2 <= K)
    return out

def smin_exact(B):
    return float(np.linalg.svd(B, compute_uv=False)[-1])

def prefix_scan(Qp, tol=1e-11, rebase=1e-4, gmax=30, use_comb=None, exhaustive=False):
    """Scan all leading blocks B_K = Qp[:K,:K] of the (row-permuted) orthogonal matrix Qp.
    Returns dict(lo, hi) arrays (certified lower/upper bounds on sigma_min(B_K), hi = lo = exact where an SVD was done),
    flags unis[K] (lo >= tol), sing[K] (hi < tol), amb[K], and counts.  use_comb: boolean array of exact singular certificates.
    exhaustive=True: SVD of every block (validation, O(M^4))."""
    M = Qp.shape[0]
    lo = np.zeros(M); hi = np.zeros(M); ndirect = 0
    if exhaustive:
        for K in range(1, M + 1):
            lo[K - 1] = hi[K - 1] = smin_exact(Qp[:K, :K])
    else:
        L0 = 0; Binv = None; bF = None; Z = None   # base index L0 with inverse of B_{L0}
        for K in range(1, M + 1):
            if use_comb is not None and use_comb[K - 1]:
                lo[K - 1] = hi[K - 1] = 0.0; continue
            g = K - L0
            if Binv is None or g > gmax:
                s = smin_exact(Qp[:K, :K]); ndirect += 1
                lo[K - 1] = hi[K - 1] = s
                if s >= rebase:
                    Binv = np.linalg.inv(Qp[:K, :K]); L0 = K; bF = np.linalg.norm(Binv); Z = None
                else:
                    Binv = None; L0 = 0
                continue
            C = Qp[:L0, L0:K]; R = Qp[L0:K, :L0]; D = Qp[L0:K, L0:K]
            Zk = Binv @ C
            S = D - R @ Zk
            sS = float(np.linalg.svd(S, compute_uv=False)[-1])
            b = bF
            up = sS
            low = 1.0 / ((1 + b) ** 2 * max(b, 1.0 / max(sS, 1e-300)))
            if up < tol or low >= tol:
                lo[K - 1], hi[K - 1] = low, up
            else:
                s = smin_exact(Qp[:K, :K]); ndirect += 1
                lo[K - 1] = hi[K - 1] = s
            if low >= rebase and g >= 1:
                # block inverse of B_K from Binv, S
                Si = np.linalg.inv(S)
                RB = R @ Binv
                top_left = Binv + Zk @ Si @ RB
                top_right = -Zk @ Si
                bot_left = -Si @ RB
                Binv = np.block([[top_left, top_right], [bot_left, Si]]); L0 = K; bF = np.linalg.norm(Binv)
    unis = lo >= tol; sing = hi < tol; amb = ~(unis | sing)
    return dict(lo=lo, hi=hi, unis=unis, sing=sing, amb=amb, n_unis=int(unis.sum()), n_sing=int(sing.sum()), n_amb=int(amb.sum()),
                min_lo=float(lo.min()), min_hi=float(hi.min()), first_sing=(int(np.argmax(sing)) + 1 if sing.any() else None), ndirect=ndirect)

def gepp_order(Qc):
    """row order selected by Gaussian elimination with partial pivoting on Qc (columns in graded order): every prefix has det = product of
    nonzero pivots (Qc is nonsingular), i.e. every prefix is unisolvent."""
    P, Lf, U = sla.lu(Qc)           # Qc = P Lf U ;  rows of P^T Qc in pivot order
    return np.argmax(P, axis=0)     # perm such that Qc[perm] = Lf U   (P[perm[j], j] = 1)

def threshold_pivot_order(Qc, theta, rng):
    """randomised threshold pivoting: at step k choose uniformly among remaining rows whose current Schur entry in column k has
    |entry| >= theta * max.  All prefixes are unisolvent by construction (pivots nonzero); sigma_min is checked separately."""
    A = Qc.copy(); M = A.shape[0]; remaining = np.arange(M); perm = []
    rows = np.arange(M)
    for k in range(M):
        col = np.abs(A[remaining, k]); mx = col.max()
        cand = remaining[col >= theta * mx]
        r = int(rng.choice(cand)); perm.append(r)
        remaining = remaining[remaining != r]
        if k < M - 1 and remaining.size:
            piv = A[r, k]
            f = A[remaining, k] / piv
            A[np.ix_(remaining, np.arange(k + 1, M))] -= np.outer(f, A[r, k + 1:])
    return np.array(perm)


def refine_min(Qp, res, kmax=150, hi_cut=1e-4):
    """exact sigma_min (SVD) at the kmax prefixes with the smallest upper bound hi (only those with hi < hi_cut).
    Returns (min_exact_over_refined, K_of_min, n_refined)."""
    idx = np.argsort(res["hi"])[:kmax]
    idx = [int(k) for k in idx if res["hi"][k] < hi_cut and res["lo"][k] != res["hi"][k]]
    best, kbest = (float("inf"), None)
    for k in idx:
        s = smin_exact(Qp[:k + 1, :k + 1])
        if s < best: best, kbest = s, k + 1
    exact_direct = res["lo"][res["lo"] == res["hi"]]
    if exact_direct.size and exact_direct.min() < best: best = float(exact_direct.min())
    return best, kbest, len(idx)
