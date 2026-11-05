#!/usr/bin/env python3
"""Auditor check (Claude subC2): whole-grid majorant (2) of odd-weight-asymptotic.md,
  |w_jk| <= 8192 m^-4 [(1+j)(1+k) + log(m+1)],  odd m>=5, all retained nodes,
and the intermediate bound (6): m^2|S_R| <= pi^4 jk + (5pi^2/2)(j+k) + 25/4 + 400(1+log R).
Weights from formula (3) (verified against arb moment solves for m<=21) in float64,
plus float64 moment solves at a few moderate odd m as a cross-check of formula (3)."""
import numpy as np, sys

def weights(m):
    R = m // 2
    a = np.arange(R + 1)
    t = np.where(a == 0, 2.0, -4.0 / (4.0 * a * a - 1.0))
    j = np.arange(m + 1); k = np.arange(m + 2)
    Cx = np.cos(2.0 * np.outer(a, j) * np.pi / m)          # (R+1) x (m+1)
    Cy = np.cos(2.0 * np.outer(a, k) * np.pi / (m + 1))    # (R+1) x (m+2)
    Mt = np.outer(t, t) * (np.add.outer(a, a) <= R)
    S = Cx.T @ Mt @ Cy                                      # (m+1) x (m+2)
    hm = 0.0 if m % 2 else 2.0 / (1 - m * m)
    S = S - 2 * hm * np.cos(np.pi * j)[:, None]
    eps = np.ones(m + 1); eps[[0, m]] = 0.5
    eta = np.ones(m + 2); eta[[0, m + 1]] = 0.5
    W = 2.0 * np.outer(eps, eta) * S / (m * (m + 1))
    mask = (np.add.outer(j, k) % 2 == 0)
    return W, S, mask

def moment_solve(m):
    nodes = [(j, k) for j in range(m + 1) for k in range(m + 2) if (j + k) % 2 == 0]
    modes = [(a, d - a) for d in range(m + 1) for a in range(d + 1)]
    J = np.array([n[0] for n in nodes]); K = np.array([n[1] for n in nodes])
    A = np.array([np.cos(a * np.pi * J / m) * np.cos(b * np.pi * K / (m + 1)) for (a, b) in modes])
    h = lambda r: 0.0 if r % 2 else 2.0 / (1 - r * r)
    rhs = np.array([h(a) * h(b) for (a, b) in modes])
    return J, K, np.linalg.solve(A, rhs)

if __name__ == '__main__':
    for m in (31, 41, 61):
        J, K, w = moment_solve(m)
        W, _, _ = weights(m)
        print(f"float64 moment solve m={m}: max|solve-formula|={np.max(np.abs(w - W[J, K])):.3e}, sum w-4={w.sum()-4:.2e}")
    worst2 = (0, 0); worst6 = (0, 0)
    mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 601
    for m in range(5, mmax + 1, 2):
        W, S, mask = weights(m)
        R = (m - 1) // 2
        j = np.arange(m + 1)[:, None]; k = np.arange(m + 2)[None, :]
        r2 = (m ** 4 * np.abs(W)) / ((1 + j) * (1 + k) + np.log(m + 1))
        r2 = np.where(mask, r2, 0).max()
        b6 = np.pi ** 4 * j * k + 2.5 * np.pi ** 2 * (j + k) + 25 / 4 + 400 * (1 + np.log(R))
        r6 = np.where(mask, m * m * np.abs(S) / b6, 0).max()
        if r2 > worst2[0]: worst2 = (r2, m)
        if r6 > worst6[0]: worst6 = (r6, m)
        if m in (5, 7, 9, 11, 21, 51, 101, 201, 401, 601):
            print(f"m={m:4d}: max m^4|w|/[(1+j)(1+k)+log(m+1)] = {r2:9.4f} (bound 8192);"
                  f"  max m^2|S_R|/RHS(6) = {r6:.4f} (bound 1)")
    print(f"over odd m=5..{mmax}: worst ratio for (2) = {worst2[0]:.4f} at m={worst2[1]}; worst ratio for (6) = {worst6[0]:.4f} at m={worst6[1]}")
