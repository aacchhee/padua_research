"""Sanity check of PD-T?...-401 Lemma 5: codim of S_n cap A S_n in S_n equals n+1 for affine A (and is
larger for a generic non-affine diagonal A), on random nodes. Monomial-free: bases from full CGS2.
Usage: python3 -I l4_codim_check.py"""
import numpy as np
rng = np.random.default_rng(3)
M = 400
P = rng.uniform(-1, 1, (M, 2)); x, y = P[:, 0], P[:, 1]; w = np.ones(M)
def basis(n):
    # orthonormal basis of S_n via CGS2 on Chebyshev-product columns (well conditioned enough for n <= 8)
    cols = [np.cos(a * np.arccos(x)) * np.cos(b * np.arccos(y)) for t in range(n + 1) for a, b in [(t - j, j) for j in range(t + 1)]]
    Q, _ = np.linalg.qr(np.array(cols).T); return Q
def dim_sum(A, B, tol=1e-9):
    s = np.linalg.svd(np.hstack([A, B]), compute_uv=False); return int(np.sum(s > tol * s[0]))
for n in range(1, 9):
    S = basis(n)
    for name, a in [('X', x), ('0.6X+0.8Y+0.3', 0.6 * x + 0.8 * y + 0.3), ('X^2+Y (non-affine)', x**2 + y)]:
        AS = np.linalg.qr(a[:, None] * S)[0]
        dint = S.shape[1] + AS.shape[1] - dim_sum(S, AS)
        print(f"n={n} N_n={S.shape[1]:3d} A={name:20s} codim(S_n cap A S_n in S_n) = {S.shape[1] - dint}")
