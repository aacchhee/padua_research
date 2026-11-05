#!/usr/bin/env python3
"""Auditor check (Claude subC2): solve the Padua moment equations V^T w = (h_a h_b)_{a+b<=m}
in arb ball arithmetic and compare every weight with the integrated cardinal formula
  w_jk = 2 eps_j eta_k /(m(m+1)) * [ S_R(theta_j,phi_k) - 2 h_m cos(m theta_j) ],
R = floor(m/2). At odd m the exceptional term is identically zero (h_m = 0).
Written independently of the developer code."""
import sys
from flint import arb, arb_mat, fmpq, ctx

ctx.prec = 256


def h(r):
    return fmpq(0) if r % 2 else fmpq(2, 1 - r * r)


def t(a):
    return fmpq(2) if a == 0 else fmpq(-4, 4 * a * a - 1)


def formula(m, j, k, include_exc=True):
    R = m // 2
    cx = [arb.cos_pi_fmpq(fmpq(2 * a * j, m)) for a in range(R + 1)]
    cy = [arb.cos_pi_fmpq(fmpq(2 * b * k, m + 1)) for b in range(R + 1)]
    S = arb(0)
    for a in range(R + 1):
        inner = arb(0)
        for b in range(R + 1 - a):
            inner += arb(t(b)) * cy[b]
        S += arb(t(a)) * cx[a] * inner
    exc = 2 * arb(h(m)) * arb.cos_pi_fmpq(fmpq(m * j, m)) if include_exc else arb(0)
    e = fmpq(1, 2) if j in (0, m) else fmpq(1)
    g = fmpq(1, 2) if k in (0, m + 1) else fmpq(1)
    return arb(2 * e * g / (m * (m + 1))) * (S - exc)


def solve(m):
    nodes = [(j, k) for j in range(m + 1) for k in range(m + 2) if (j + k) % 2 == 0]
    modes = [(a, d - a) for d in range(m + 1) for a in range(d + 1)]
    assert len(nodes) == len(modes) == (m + 1) * (m + 2) // 2
    A = arb_mat([[arb.cos_pi_fmpq(fmpq(a * j, m)) * arb.cos_pi_fmpq(fmpq(b * k, m + 1)) for (j, k) in nodes]
                 for (a, b) in modes])
    rhs = arb_mat([[arb(h(a) * h(b))] for (a, b) in modes])
    w = A.solve(rhs)
    return nodes, [w[i, 0] for i in range(len(nodes))]


if __name__ == '__main__':
    ms = [int(x) for x in sys.argv[1:]] or [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 4, 6, 8]
    for m in ms:
        nodes, w = solve(m)
        maxdiff = arb(0)
        maxdiff_noexc = arb(0)
        tot = arb(0)
        for (j, k), wi in zip(nodes, w):
            d = abs(wi - formula(m, j, k))
            tot += wi
            if d.upper() > maxdiff.upper():
                maxdiff = d
            if m % 2 == 0:
                d2 = abs(wi - formula(m, j, k, include_exc=False))
                if d2.upper() > maxdiff_noexc.upper():
                    maxdiff_noexc = d2
        # symmetry y -> -y at odd m
        sym = arb(0)
        if m % 2 == 1:
            idx = {nk: i for i, nk in enumerate(nodes)}
            for (j, k), wi in zip(nodes, w):
                d = abs(wi - w[idx[(j, m + 1 - k)]])
                if d.upper() > sym.upper():
                    sym = d
        neg = sum(1 for wi in w if wi < 0)
        print(f"m={m:3d} nodes={len(nodes):4d} max|solve-formula|<= {maxdiff.upper().str(3, radius=False)}"
              + (f"  max|solve-formula_without_exc|<= {maxdiff_noexc.upper().str(3, radius=False)}" if m % 2 == 0 else "")
              + f"  |sum w-4|<= {abs(tot - 4).upper().str(3, radius=False)}"
              + (f"  max|w_jk-w_j,m+1-k|<= {sym.upper().str(3, radius=False)}" if m % 2 else "")
              + f"  #neg={neg}  w00={w[0].mid().str(12, radius=False)}", flush=True)
