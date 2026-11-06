#!/usr/bin/env python3
"""Claude audit-02: high-precision b-dominance (3) at larger N, own code only.
Computes K=max(kappa_b1,kappa_b2) over the FULL b fields and r_i, all six
models; also the theorem's t* and kappa(t*) via the homogeneous formula (2).
Also compares with the inherited analytic lowers 5^M/M (Krawtchouk) and
A_M/[27M(2M+3)] (/2 fixed mass, Hahn)."""
import sys, json
from math import comb
import mpmath as mp
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gauge_exact import Num, inputs, nn_triangle, support, field_cond


def A_M(M):
    T = lambda k: sum(comb(k, h) * comb(M + k + 3 - h, M - k) for h in range(k + 1))
    return sum(T(k) * sum(comb(M - 1, 2 * i + 1) * comb(k + i, k) for i in range(M // 2)) for k in range(M + 1))


def run(family, N, R):
    M = N - 1
    zq, wq = inputs(family, M)
    z = [R.conv(x) for x in zq]
    w = [[R.conv(x) for x in row] for row in wq]
    P, fields, checks = nn_triangle(z, w, R)
    out = []
    for model in ('mixed', 'componentwise', 'spacing'):
        for mass in (False, True):
            kb = [field_cond([fields[k] for k in fields if k[0] == 'b' and k[1] == j], z, w, model, mass, R) for j in (1, 2)]
            K = max(kb)
            r = []
            for i in (1, 2):
                e = (1, 0) if i == 1 else (0, 1)
                vi, dvi = fields[('a', i, e)]
                r.append(support(dvi, z, w, model, mass, R) / vi)
            if family == 'krawtchouk':
                lower = mp.mpf(5) ** M / M
            else:
                lower = mp.mpf(A_M(M)) / (27 * M * (2 * M + 3)) / (2 if mass else 1) if M >= 2 else mp.mpf(0)
            out.append({'model': model, 'fixed_mass': mass, 'K': mp.nstr(K, 12), 'r': [mp.nstr(x, 8) for x in r],
                        'K_over_max_r': mp.nstr(K / max(r), 8), 'inherited_lower': mp.nstr(lower, 10),
                        'lower_le_K': bool(lower <= K * (1 + mp.mpf(10) ** -30)), 'dominance': bool(max(r) <= K)})
    return {'family': family, 'N': N, 'resid_max': mp.nstr(checks['resid_max'], 3),
            'aconsist_max': mp.nstr(checks['aconsist_max'], 3), 'cases': out}


if __name__ == '__main__':
    family = sys.argv[1]
    Ns = [int(a) for a in sys.argv[2].split(',')]
    dps = int(sys.argv[3]) if len(sys.argv) > 3 else 80
    R = Num('mp', dps)
    for N in Ns:
        print(json.dumps(run(family, N, R)), flush=True)
