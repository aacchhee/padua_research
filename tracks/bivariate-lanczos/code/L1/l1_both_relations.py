"""R03 control: a two-relation block recurrence.  Degree block n is obtained from BOTH X Qblk_{n-1} and
Y Qblk_{n-1} (2n columns), orthogonalised (CGS, one pass) against blocks n-2 and n-1 only (exact block-tridiagonal
truncation, Xu-type), then an orthonormal basis of rank n+1 is taken by SVD (largest n+1 singular directions).
Same graded spaces S_n; different basis inside each degree block.  Compared with the BJ window recurrence.
Hypothesis tested: the non-product amplification comes from the single-relation triangular row selection
(one operator per column), not from the truncation itself.  MEASURED only.  Usage: python3 -I l1_both_relations.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L


def both(x, y, w, nmax, passes=1):
    M = len(x)
    blocks = [ (np.sqrt(w) / np.linalg.norm(np.sqrt(w)))[:, None] ]
    for n in range(1, nmax + 1):
        P = blocks[-1]
        V = np.hstack([x[:, None] * P, y[:, None] * P])
        Wn = np.hstack(blocks[max(0, n - 2):])
        for _ in range(passes):
            V = V - Wn @ (Wn.T @ V)
        U, s, _ = np.linalg.svd(V, full_matrices=False)
        blocks.append(U[:, :n + 1])
    return np.hstack(blocks)


def loss_profile(Q, nmax, step=4):
    G = Q.T @ Q
    return [float(np.abs(G[:(n + 1) * (n + 2) // 2, :(n + 1) * (n + 2) // 2] - np.eye((n + 1) * (n + 2) // 2)).max())
            for n in range(step, nmax + 1, step)]


rng = np.random.default_rng(11)
M = 1681
sq = rng.uniform(-1, 1, (M, 2)); one = np.ones(M)
dk = []
while len(dk) < M:
    p = rng.uniform(-1, 1, 2)
    if p @ p <= 1: dk.append(p)
tr = []
while len(tr) < M:
    p = rng.uniform(0, 1, 2)
    if p.sum() <= 1: tr.append(2 * p - 1)
sets = [('square', sq), ('square rot 0.3', L.rotate(sq, 0.3)), ('square rot pi/4', L.rotate(sq, np.pi / 4)),
        ('disk', np.array(dk)), ('triangle', np.array(tr))]
for name, P in sets:
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Qbj, _, _ = L.recurrence(x, y, one, 24, win='block', orth='cgs')
    Qb = both(x, y, one, 24)
    lb = loss_profile(Qbj, 24); lt = loss_profile(Qb, 24)
    print(f"{name:18s} BJ window   n=4..24: " + " ".join(f"{v:.0e}" for v in lb), flush=True)
    print(f"{'':18s} two-relation n=4..24: " + " ".join(f"{v:.0e}" for v in lt), flush=True)
