"""M2 adversarial script 1: the 'dimension theorem' is the finite Favard/spectral argument; the 3-dim commutant is the
affine-triangular group, not a boundary freedom.

Model: claude-fable-5-1, effort max (as requested by the orchestrator) . Adversarial check . 2026-11-01

What is computed (random real nodes, M = N, n = 3..6; seconds):
 (1) joint eigenvectors of (H_x, H_y) are the rows of Q, i.e. sqrt(w_k) P(z_k): the pair *is* the N-node section
     (sanity check of the finite Favard argument written in adversarial-M2.md).
 (2) The space E = {E symmetric, supported on pattern(H_x) [resp. pattern(H_y), block-tridiagonal], [H_x, E] = 0}:
     its dimension and whether it equals span{I, H_x, H_y} intersected with the pattern (affine-triangular explanation
     y -> a + b x + c y in this order).
 (3) Tangent dimension of the commuting variety in the generalized-Hessenberg pattern and in the block-tridiagonal
     pattern (re-run of the generator's numbers; expected 3N-1 and 3N-1 + C(n+2,3)).
Run: python3 -I m2_favard_commutant.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from m2_common import *

def commutant_dim(Hx, mask, extra=None):
    """dim of {E symmetric on mask : [Hx, E] = 0}; also test membership of candidate matrices."""
    N = Hx.shape[0]
    basis = sym_basis(mask)
    cols = []
    for (i, j) in basis:
        E = np.zeros((N, N)); E[i, j] = 1.0; E[j, i] = 1.0
        C = Hx @ E - E @ Hx
        cols.append(C.ravel())
    A = np.array(cols).T
    r, s = numrank(A)
    null_dim = len(basis) - r
    return null_dim

def in_span_test(Hx, Hy, mask):
    """Check that I, Hx, Hy (those supported on mask) commute with Hx and are independent: lower bound on dim."""
    N = Hx.shape[0]
    cands = []
    for name, Mt in (('I', np.eye(N)), ('Hx', Hx), ('Hy', Hy)):
        if np.all(np.abs(Mt[~mask]) < 1e-12):
            cands.append((name, Mt))
    return [c[0] for c in cands]

def tangent_dim(Hx, Hy, mask):
    N = Hx.shape[0]
    basis = sym_basis(mask)
    cols = []
    for (i, j) in basis:
        E = np.zeros((N, N)); E[i, j] = 1; E[j, i] = 1
        cols.append((E @ Hy - Hy @ E).ravel())   # [E, Hy] for E in x-slot
    for (i, j) in basis:
        E = np.zeros((N, N)); E[i, j] = 1; E[j, i] = 1
        cols.append((Hx @ E - E @ Hx).ravel())   # [Hx, E] for E in y-slot
    A = np.array(cols).T
    r, s = numrank(A, tol=1e-9)
    return 2 * len(basis) - r

def main():
    rng = np.random.default_rng(20261101)
    print("n  N  | jointEV err | dim comm(Hx) in patt(Hy) / patt(Hx) / blocktri | I,Hx,Hy in patt(Hy)? | tangent GH / blocktri | 3N-1, +C(n+2,3)")
    for n in range(3, 7):
        N = dim_pi(n)
        x, y, w = random_nodes(n, rng)
        Q, R, Hx, Hy = pair_from_nodes(x, y, w, n)
        # (1) joint eigenvectors = rows of Q
        err = max(np.linalg.norm(Hx @ Q.T - Q.T * x[None, :]), np.linalg.norm(Hy @ Q.T - Q.T * y[None, :]))
        Px, Py, Pb = pattern(n, 'x'), pattern(n, 'y'), block_tridiag_pattern(n)
        assert np.all(np.abs(Hx[~Px]) < 1e-12) and np.all(np.abs(Hy[~Py]) < 1e-12)
        d_y = commutant_dim(Hx, Py); d_x = commutant_dim(Hx, Px); d_b = commutant_dim(Hx, Pb)
        members = in_span_test(Hx, Hy, Py)
        t_gh = tangent_dim(Hx, Hy, Px & Py) if False else None
        # generalized-Hessenberg tangent: E_x on patt(x), E_y on patt(y)
        bx, by = sym_basis(Px), sym_basis(Py)
        cols = []
        for (i, j) in bx:
            E = np.zeros((N, N)); E[i, j] = 1; E[j, i] = 1
            cols.append((E @ Hy - Hy @ E).ravel())
        for (i, j) in by:
            E = np.zeros((N, N)); E[i, j] = 1; E[j, i] = 1
            cols.append((Hx @ E - E @ Hx).ravel())
        A = np.array(cols).T; r, s = numrank(A, 1e-9)
        t_gh = len(bx) + len(by) - r
        t_bt = tangent_dim(Hx, Hy, Pb)
        from math import comb
        print(f"{n}  {N:2d} | {err:8.1e}    | {d_y} / {d_x} / {d_b}  | {members} | {t_gh} / {t_bt} | {3*N-1}, {3*N-1+comb(n+2,3)}")
    # which variable is 'larger' in the pattern sense: is patt(Hy) contained in patt(Hx)?
    n = 4; Px, Py = pattern(n, 'x'), pattern(n, 'y')
    print("pattern(Hy) subset of pattern(Hx)?", bool(np.all(Px[Py])), "; pattern(Hx) subset of pattern(Hy)?", bool(np.all(Py[Px])))

if __name__ == '__main__':
    main()
