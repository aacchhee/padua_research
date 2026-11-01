"""Adversarial check gen1-3: is the three-degree window of the linear-pole-per-degree
bivariate ORF recurrence a generic fact, and is it a Lanczos-type (locally
extractable) recurrence?

Setting (as in gen1-draft-3, pre-gate screen): M random nodes in [-1,1]^2, random
positive weights, one random real line l_k(x,y) = cos(th_k) x + sin(th_k) y - c_k per
degree k with |c_k| in [1.6, 2.5] (the line misses the square), pi_t = prod_{k<=t} l_k,
V_t = Pi_t / pi_t, W_t = V_t (-) V_{t-1}, phi_{t,s} an orthonormal basis of W_t.

Tests, for t = 1..n-1 and all s (relative weighted LS residual of g = l_{t+1} phi_{t+1,s}
against a candidate span; ambient space U_{t+1} = Pi_{t+1}/pi_t has dim (t+2)(t+3)/2):
  A  : W_{t-1} + W_t + x W_t + y W_t                (the draft's window claim)
  A1 : l_{t-1} W_{t-1} + W_t + x W_t + y W_t        (1-D-type pole-cancelled form)
  B  : W_t + x W_t + y W_t                          (two-degree window)
  D  : W_{t-2} + W_{t-1} + W_t + x W_t + y W_t      (four-degree window)
  C  : V_t + x W_t + y W_t                          (sanity: must be all of U_{t+1})
For each span we print its numerical rank, so vacuous cases (rank = ambient dim) are
visible. We also print dim ker{(v,w) in W_t^2 : x v + y w in V_t} (predicted t) and the
rank of the "lower-coefficient" map (predicted t-1, see the adversarial note).

Lanczos extractability: C_t := (W_{t-1} + W_t + xW_t + yW_t)/l_{t+1} subset V_{t+1}.
We compute dim(C_t cap V_t) (predicted 3t+1) and the subspace of C_t orthogonal to
W_t (+) W_{t-1}; if the window were Lanczos-type that subspace would equal W_{t+1}.
We report its dimension and the largest principal angle with W_{t+1}.

Also the 1-D analogue (nodes on [-1,1], real poles outside) for comparison:
  (z - xi_n) phi_n in span{phi_{n-2}, phi_{n-1}, z phi_{n-1}}        (draft-type form)
  (z - xi_n) phi_n in span{l_{n-2} phi_{n-2}, phi_{n-1}, z phi_{n-1}} (classical form)

Scope: n <= 8, M = 120, 3 seeds; seconds. MEASURED within this scope only.
"""
import numpy as np
from numpy.polynomial import chebyshev as C

rng_global = np.random.default_rng(20261101)


def cheb2(x, y, t):
    """Columns T_a(x) T_b(y), a+b = t (t+1 functions)."""
    cols = []
    for a in range(t + 1):
        b = t - a
        cols.append(C.chebval(x, [0] * a + [1]) * C.chebval(y, [0] * b + [1]))
    return np.column_stack(cols)


def build_orf(x, y, w, lines, n):
    """Weighted-orthonormal graded basis of V_n = Pi_n/pi_n. Returns Q (M x N), block
    index list, and the pole products pi_t evaluated on the nodes."""
    sw = np.sqrt(w)
    M = len(x)
    pis = [np.ones(M)]
    for (a, b, c) in lines:
        pis.append(pis[-1] * (a * x + b * y - c))
    cols, blocks = [], []
    for t in range(n + 1):
        A = cheb2(x, y, t) / pis[t][:, None]
        cols.append(A)
        blocks += [t] * (t + 1)
    A = np.column_stack(cols)
    Qw, R = np.linalg.qr(sw[:, None] * A)
    # blockwise re-orthonormalisation for safety (two passes)
    Qw, _ = np.linalg.qr(Qw)
    Q = Qw / sw[:, None]      # functions: Q^T diag(w) Q = I
    return Q, np.array(blocks), pis


def rel_resid(sw, span_cols, g):
    """relative weighted LS residual of g against span_cols, plus numerical rank."""
    A = sw[:, None] * span_cols
    b = sw * g
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    rank = int(np.sum(S > 1e-10 * S[0]))
    Ur = U[:, :rank]
    r = b - Ur @ (Ur.T @ b)
    return np.linalg.norm(r) / np.linalg.norm(b), rank


def run2d(seed, n=8, M=120, verbose=True):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, M)
    y = rng.uniform(-1, 1, M)
    w = rng.uniform(0.5, 1.5, M)
    sw = np.sqrt(w)
    lines = []
    for k in range(n + 2):
        th = rng.uniform(0, 2 * np.pi)
        c = rng.choice([-1, 1]) * rng.uniform(1.6, 2.5)
        lines.append((np.cos(th), np.sin(th), c))
    Q, blocks, pis = build_orf(x, y, w, lines, n)
    # orthonormality check
    G = Q.T @ (w[:, None] * Q)
    orth = np.max(np.abs(G - np.eye(G.shape[0])))
    W = lambda t: Q[:, blocks == t]
    lval = lambda k: lines[k - 1][0] * x + lines[k - 1][1] * y - lines[k - 1][2]  # l_k
    out = []
    for t in range(1, n):
        g = lval(t + 1)[:, None] * W(t + 1)          # l_{t+1} phi_{t+1,s}
        Wt, Wt1 = W(t), W(t - 1)
        xWt, yWt = x[:, None] * Wt, y[:, None] * Wt
        spans = {
            'A ': np.column_stack([Wt1, Wt, xWt, yWt]),
            'A1': np.column_stack([lval(t - 1)[:, None] * Wt1 if t >= 2 else Wt1, Wt, xWt, yWt]),
            'B ': np.column_stack([Wt, xWt, yWt]),
            'C ': np.column_stack([Q[:, blocks <= t], xWt, yWt]),
        }
        if t >= 2:
            spans['D '] = np.column_stack([W(t - 2), Wt1, Wt, xWt, yWt])
        amb = (t + 2) * (t + 3) // 2
        row = {'t': t, 'amb': amb}
        for key, S in spans.items():
            res = [rel_resid(sw, S, g[:, s]) for s in range(g.shape[1])]
            row[key] = (max(r for r, _ in res), res[0][1])
        # kernel dimension of (v,w) -> x v + y w mod V_t
        Vt = Q[:, blocks <= t]
        XY = np.column_stack([xWt, yWt])
        P = XY - Vt @ (Vt.T @ (w[:, None] * XY))      # project out V_t (weighted)
        sv = np.linalg.svd(sw[:, None] * P, compute_uv=False)
        row['ker'] = int(np.sum(sv < 1e-10 * sv[0]))
        # Lanczos extractability: C_t = span(A)/l_{t+1} inside V_{t+1}
        Ct = spans['A '] / lval(t + 1)[:, None]
        # orthonormal basis of C_t (weighted)
        U, S, _ = np.linalg.svd(sw[:, None] * Ct, full_matrices=False)
        rk = int(np.sum(S > 1e-10 * S[0]))
        Uc = U[:, :rk]                                    # weighted-orthonormal basis of C_t
        # dim(C_t cap V_t): C_t subset V_{t+1}; intersection = part orthogonal to W_{t+1}
        Wt1n = sw[:, None] * W(t + 1)
        Mx = Wt1n.T @ Uc                                  # (t+2) x rk
        s2 = np.linalg.svd(Mx, compute_uv=False)
        row['dimC'] = rk
        row['dimCcapVt'] = rk - int(np.sum(s2 > 1e-8))
        # subspace of C_t orthogonal to W_t (+) W_{t-1}
        Wlow = sw[:, None] * np.column_stack([Wt1, Wt])
        Nmat = Wlow.T @ Uc                                # (2t+1) x rk
        _, s3, V3 = np.linalg.svd(Nmat)
        null = V3[int(np.sum(s3 > 1e-8)):].T             # coordinates of null space
        Z = Uc @ null                                     # weighted-orthonormal columns
        row['dim_after_2blocks'] = Z.shape[1]
        # largest principal angle between Z and W_{t+1}: via singular values of W_{t+1}^T Z
        s4 = np.linalg.svd(Wt1n.T @ Z, compute_uv=False)
        row['extra_dirs'] = Z.shape[1] - (t + 2)
        row['min_sv_WZ'] = float(s4.min()) if len(s4) else float('nan')
        # three-block orthogonalisation: also against W_{t-2}
        if t >= 2:
            Wlow3 = sw[:, None] * np.column_stack([W(t - 2), Wt1, Wt])
            N3 = Wlow3.T @ Uc
            _, s5, V5 = np.linalg.svd(N3)
            null3 = V5[int(np.sum(s5 > 1e-8)):].T
            Z3 = Uc @ null3
            s6 = np.linalg.svd(Wt1n.T @ Z3, compute_uv=False)
            row['dim_after_3blocks'] = Z3.shape[1]
            row['min_sv_WZ3'] = float(s6.min()) if len(s6) else float('nan')
        else:
            row['dim_after_3blocks'] = Z.shape[1]
            row['min_sv_WZ3'] = row['min_sv_WZ']
        # skew form Phi on H_{t-1} (top-form coordinates): rank by parity
        out.append(row)
    if verbose:
        print(f"\n=== 2-D, seed {seed}, M={M}, n={n}, orthonormality defect {orth:.1e} ===")
        print(" t amb |  A(res,rk)      A1(res,rk)     B(res,rk)      D(res,rk)      C(res,rk) | ker dimC dimC&V_t  dim_after_2blk extra min_sv2 | dim_after_3blk (t+2) min_sv3")
        for r in out:
            def f(k):
                return f"{r[k][0]:.1e},{r[k][1]:3d}" if k in r else "      --   "
            print(f"{r['t']:2d} {r['amb']:3d} | {f('A ')}  {f('A1')}  {f('B ')}  {f('D ')}  {f('C ')} | "
                  f"{r['ker']:2d}  {r['dimC']:3d}   {r['dimCcapVt']:3d}        {r['dim_after_2blocks']:3d}        "
                  f"{r['extra_dirs']:2d}   {r['min_sv_WZ']:.2e} |     {r['dim_after_3blocks']:3d}       {r['t']+2:3d}   {r['min_sv_WZ3']:.2e}")
    return out


def run1d(seed, n=8, M=60):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, M)
    w = rng.uniform(0.5, 1.5, M)
    sw = np.sqrt(w)
    xi = rng.choice([-1, 1], n + 2) * rng.uniform(1.6, 2.5, n + 2)   # real poles outside
    pis = [np.ones(M)]
    for k in range(n + 1):
        pis.append(pis[-1] * (x - xi[k]))
    A = np.column_stack([C.chebval(x, [0] * t + [1]) / pis[t] for t in range(n + 1)])
    Qw, _ = np.linalg.qr(sw[:, None] * A)
    Qw, _ = np.linalg.qr(Qw)
    Q = Qw / sw[:, None]
    l = lambda k: x - xi[k - 1]
    print(f"\n=== 1-D analogue, seed {seed}: (z-xi_n) phi_n against two 3-term spans ===")
    print(" n  draft-form span{phi_{n-2},phi_{n-1},z phi_{n-1}}   classical span{l_{n-2}phi_{n-2},phi_{n-1},z phi_{n-1}}")
    for m in range(2, n + 1):
        g = l(m) * Q[:, m]
        S1 = np.column_stack([Q[:, m - 2], Q[:, m - 1], x * Q[:, m - 1]])
        S2 = np.column_stack([l(m - 2) * Q[:, m - 2] if m >= 3 else Q[:, m - 2], Q[:, m - 1], x * Q[:, m - 1]])
        r1, k1 = rel_resid(sw, S1, g)
        r2, k2 = rel_resid(sw, S2, g)
        print(f"{m:2d}      {r1:.1e} (rank {k1}, ambient {m + 1})                  {r2:.1e} (rank {k2})")


if __name__ == '__main__':
    for seed in (1, 2, 3):
        run2d(seed)
    for seed in (1, 2):
        run1d(seed)
