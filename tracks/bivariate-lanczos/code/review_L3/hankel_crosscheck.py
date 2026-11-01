#!/usr/bin/env python3
"""Reviewer cross-check of 309(b) against 306: for Padua n = 1, 2 the developer's dual certificate A_i
must make M = sum_i G_i A_i G_i^T a Hankel matrix (exact; since S1 = {p_C} exactly for n <= 3)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep_exact_check as R
import indep_generator_cert as Gm
LOG = sys.argv[1]
h, pstar, certs = R.parse_log(LOG)
for n in (1, 2):
    nodes, q = Gm.check_generators(n)
    qd = [Gm.to_dict(qq) for qq in q]
    sz = n + 2
    M = [[R.KZ] * sz for _ in range(sz)]
    for z, (a11, a12, a22) in zip(nodes, certs[n]):
        G = [(R.deriv_at(qj, z, 1, 0), R.deriv_at(qj, z, 0, 1)) for qj in qd]
        for j in range(sz):
            for k in range(sz):
                gj, gk = G[j], G[k]
                M[j][k] = M[j][k] + gj[0] * a11 * gk[0] + gj[0] * a12 * gk[1] + gj[1] * a12 * gk[0] + gj[1] * a22 * gk[1]
    hank = all(M[j][k] == M[j2][k2] for j in range(sz) for k in range(sz)
               for j2 in range(sz) for k2 in range(sz) if j + k == j2 + k2)
    print(f"Padua n={n}: sum_i G_i A_i G_i^T is Hankel (exact): {hank}; anti-diagonal values: "
          f"{[str(R.K.to_sympy(M[max(0, m - sz + 1)][m - max(0, m - sz + 1)])) for m in range(2 * sz - 1)]}")
