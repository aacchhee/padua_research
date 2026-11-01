"""Within-degree triangular solve of the F-marching: for degree t, A'_t (t x t, lower triangular) has entries
(j, r) = coefficient of q_(t,r) in F q_(t-1,j-1) for 1 <= r <= j <= t (r = j: beta_(t,j)).  The F-marching solves
A'_t P_t[1:] = rhs at every node; ||inv(A'_t)|| measures the within-degree amplification.  Product measures:
A'_t is diagonal (decoupled chains).  Computed coefficients of the bj run, degrees where loss is still small.
MEASURED only.  Usage: python3 -I l1_block_solve_growth.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L

def growth(name, P, w, nmax):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, coef, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    idx, pos, parent, op, start = tab
    out = []
    for t in range(2, nmax + 1, 2):
        A = np.zeros((t, t))
        for j in range(1, t + 1):
            k = pos[(t, j)]; W, h, beta = coef[k]
            for hl, l in zip(h, W):
                tl, r = idx[l]
                if tl == t and r >= 1:
                    A[j - 1, r - 1] = hl
            A[j - 1, j - 1] = beta
        offd = np.abs(np.tril(A, -1)).max() if t > 1 else 0.0
        inv = np.linalg.norm(np.linalg.inv(A), 2)
        out.append(f"t{t}: |inv A'|={inv:.1e} max|offdiag|/min beta={offd / np.diag(A).min():.1e}")
    print(f"{name:22s} " + " ".join(out), flush=True)

rng = np.random.default_rng(11)
sq = rng.uniform(-1, 1, (1681, 2)); one = np.ones(1681)
growth('square', sq, one, 16)
growth('square rot 0.3', L.rotate(sq, 0.3), one, 16)
growth('square rot pi/4', L.rotate(sq, np.pi / 4), one, 16)
tr = []
while len(tr) < 1681:
    p = rng.uniform(0, 1, 2)
    if p.sum() <= 1: tr.append(2 * p - 1)
growth('triangle', np.array(tr), one, 14)
P, w = L.nodes_tensor_cheb(41); growth('tensor 41^2', P, w, 16)
