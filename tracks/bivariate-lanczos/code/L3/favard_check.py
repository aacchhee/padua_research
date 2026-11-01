"""Checks for theory file 301 (truncated Favard / consistency of sections).

Part A [EXACT, rational]: for a random rational discrete measure AND for a
random rational functional L on Pi_{2n+1} with M_n(L) > 0 (not nec. a measure),
with Gram G = [L(m_a m_b)], G_x = [L(x m_a m_b)], G_y (monomials of Pi_n),
the matrix C = G_x G^{-1} G_y - G_y G^{-1} G_x has all rows (and columns) of
degree < n equal to zero.  Since [H_x, H_y] = R^{-T} C R^{-1} with G = R^T R,
this is the statement "the section commutator is supported on the last
diagonal block" (exact, no square roots needed).
Part B [FP, MEASURED]: for the same functional, sections H via Cholesky, then
reconstruct moments by the words formula L(x^g) = e0^T w_g(H_x,H_y) e0 for two
different random words per monomial; report max error.
Part C [counts]: number of entries in the structural pattern of the full pair,
number of entries the recurrence computes (H_x fully, H_y only rows/cols (k,0)),
and dim Pi_{2n+1} - 1.

Usage: python3 favard_check.py [nmax] [seed]
"""
import sys
import random
from fractions import Fraction as F
import numpy as np


def exps(d):
    return [(s, k - s) for k in range(d + 1) for s in range(k + 1)]


def mat_inv(A):
    n = len(A)
    aug = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c, n) if aug[i][c] != 0)
        aug[c], aug[p] = aug[p], aug[c]
        inv = 1 / aug[c][c]
        aug[c] = [v * inv for v in aug[c]]
        for i in range(n):
            if i != c and aug[i][c] != 0:
                f = aug[i][c]
                aug[i] = [vi - f * vc for vi, vc in zip(aug[i], aug[c])]
    return [row[n:] for row in aug]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def gram(Lmom, n):
    E = exps(n)
    G = [[Lmom[(a1 + a2, b1 + b2)] for (a2, b2) in E] for (a1, b1) in E]
    Gx = [[Lmom[(a1 + a2 + 1, b1 + b2)] for (a2, b2) in E] for (a1, b1) in E]
    Gy = [[Lmom[(a1 + a2, b1 + b2 + 1)] for (a2, b2) in E] for (a1, b1) in E]
    return G, Gx, Gy


def measure_moments(pts, w, d):
    return {(a, b): sum(wi * x ** a * y ** b for (x, y), wi in zip(pts, w)) for (a, b) in exps(d)}


def is_pd_exact(G):
    # exact LDL^T pivots
    A = [row[:] for row in G]
    n = len(A)
    for c in range(n):
        if A[c][c] <= 0:
            return False
        for i in range(c + 1, n):
            f = A[i][c] / A[c][c]
            for j in range(c, n):
                A[i][j] -= f * A[c][j]
    return True


def partA(n, rng):
    d = 2 * n + 1
    E = exps(n)
    N = len(E)
    deg = [a + b for (a, b) in E]
    out = []
    # (i) random rational discrete measure with M = dim Pi_{2n+1} + 3 nodes
    M = (d + 1) * (d + 2) // 2 + 3
    pts = [(F(rng.randint(-20, 20), 20), F(rng.randint(-20, 20), 20)) for _ in range(M)]
    w = [F(rng.randint(1, 9), 9) for _ in range(M)]
    L1 = measure_moments(pts, w, d)
    # (ii) random functional: perturb the measure moments by random rationals of size 1/50 in ALL degrees <= 2n+1
    L2 = {k: v + F(rng.randint(-10, 10), 500) for k, v in L1.items()}
    for name, L in (("measure", L1), ("functional", L2)):
        G, Gx, Gy = gram(L, n)
        if not is_pd_exact(G):
            out.append((name, None)); continue
        Gi = mat_inv(G)
        Cm = [[u - v for u, v in zip(r1, r2)] for r1, r2 in zip(matmul(matmul(Gx, Gi), Gy), matmul(matmul(Gy, Gi), Gx))]
        bad_low = any(Cm[i][j] != 0 for i in range(N) for j in range(N) if deg[i] < n or deg[j] < n)
        top_nonzero = any(Cm[i][j] != 0 for i in range(N) for j in range(N) if deg[i] == n and deg[j] == n)
        out.append((name, (not bad_low, top_nonzero)))
    return out, L2


def sections_fp(L, n):
    G, Gx, Gy = gram(L, n)
    G = np.array(G, dtype=float); Gx = np.array(Gx, dtype=float); Gy = np.array(Gy, dtype=float)
    R = np.linalg.cholesky(G).T  # G = R^T R
    Ri = np.linalg.inv(R)
    return Ri.T @ Gx @ Ri, Ri.T @ Gy @ Ri


def partB(L, n, rng):
    Hx, Hy = sections_fp(L, n)
    d = 2 * n + 1
    e0 = np.zeros(Hx.shape[0]); e0[0] = 1
    L0 = float(L[(0, 0)])
    err = 0.0
    for (a, b) in exps(d):
        for _ in range(2):
            word = ['x'] * a + ['y'] * b
            rng.shuffle(word)
            v = e0.copy()
            for ch in word:
                v = (Hx if ch == 'x' else Hy) @ v
            val = e0 @ v * L0
            err = max(err, abs(val - float(L[(a, b)])) / max(1.0, abs(float(L[(a, b)]))))
    return err


def counts(n):
    full = 0; part = 0
    for k in range(n + 1):
        nb = k + 1
        full += 2 * nb * (nb + 1) // 2  # B_{k,x}, B_{k,y}
        part += nb * (nb + 1) // 2 + nb  # B_{k,x} full; B_{k,y} row 0
    for k in range(n):
        ax = sum(min(s + 2, k + 2) for s in range(k + 1))  # A_{k,x}: t <= s+1
        ay = sum(s + 1 for s in range(k + 1))  # A_{k,y}: t <= s
        full += ax + ay
        part += ax + (k + 1) + 1  # A_{k,x} full; A_{k,y} column 0 (all s) + row 0 pivot counted in column 0
    # correction: A_{k,y} column 0 has k+1 entries (rows s=0..k, t=0 <= s) - includes the pivot (0,0); remove double count
    part -= n
    D = (2 * n + 2) * (2 * n + 3) // 2
    return full, part, D - 1


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    rng = random.Random(seed)
    print(f"favard_check nmax={nmax} seed={seed}")
    for n in range(1, nmax + 1):
        res, L2 = partA(n, rng)
        errB = partB(L2, n, rng)
        full, part, Dm1 = counts(n)
        print(f"n={n}: exact commutator support (low rows/cols zero, top block nonzero): {res}; "
              f"words-formula max rel err (FP) = {errB:.2e}; counts full={full} computed={part} D-1={Dm1} "
              f"excess full={full-Dm1} computed={part-Dm1} n(n+1)/2={n*(n+1)//2}")


if __name__ == '__main__':
    main()
