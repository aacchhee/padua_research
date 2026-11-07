#!/usr/bin/env python3
"""Audit03 T8 own sampled-Lebesgue evaluator (Claude, Opus 5.5 xhigh).

Own code: nodes from exact rational angles, Lagrange cardinals by solving with
the Legendre product basis (a different basis from the producer's Chebyshev
one; Lambda is basis independent), maxima over the 21^3 tensor Chebyshev-
Lobatto mesh cos(pi k/20) and, as a refinement probe, over 41^3.  Leja
baseline rebuilt from an own discrete-Leja ordering of cos(pi k/n).
MEASURED lower samples only.
"""
import itertools as it
import json
import math
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre as Lg

sys.path.insert(0, str(Path(__file__).resolve().parent))
import t8_exact_audit as ex


def basis(P, n):
    T = [Lg.legvander(P[:, j], n) for j in range(3)]
    return np.stack([T[0][:, a] * T[1][:, b] * T[2][:, c] for a, b, c in ex.exponents(n)], axis=1)


def mesh(m):
    g = np.cos(np.pi * np.arange(m) / (m - 1))
    return np.array(list(it.product(g, repeat=3)))


def lebesgue(P, n, m=21):
    V = basis(P, n)
    s = np.linalg.svd(V, compute_uv=False)
    best = 0.0
    G = mesh(m)
    for i in range(0, len(G), 20000):
        B = basis(G[i:i + 20000], n)
        C = np.linalg.solve(V.T, B.T)
        best = max(best, float(np.abs(C).sum(axis=0).max()))
    return best, float(s[0] / s[-1])


def nodes(M, z, rows, D):
    L, S = ex.nodes_exact(M, z, rows, D)
    return np.cos(2 * np.pi * np.array(S, dtype=float) / L)


def leja_axis(n):
    x = list(np.cos(np.pi * np.arange(n + 1) / n)) if n else [1.0]
    order = [0]
    rest = list(range(1, len(x)))
    while rest:
        vals = [np.prod([abs(x[i] - x[j]) for j in order]) for i in rest]
        k = rest[int(np.argmax(vals))]  # first index among ties
        order.append(k)
        rest.remove(k)
    return np.array([x[i] for i in order])


def leja_set(n):
    a = leja_axis(n)
    return np.array([[a[i], a[j], a[k]] for i, j, k in ex.exponents(n)])


def main():
    ev = Path(sys.argv[1])
    out = {}
    lam, cond = lebesgue(nodes(21, (1, 4, 6), [(257, 1028, 10080)], 10794), 3)
    lam41, _ = lebesgue(nodes(21, (1, 4, 6), [(257, 1028, 10080)], 10794), 3, 41)
    out['near_M21'] = {'Lambda21': lam, 'Lambda41': lam41, 'cond_legendre': cond}
    print(json.dumps(out), flush=True)
    d = json.loads((ev / 't8-r06-phi2.json').read_text())
    out['phi2'] = []
    for row in d['rows']:
        n = row['n']
        lamF, _ = lebesgue(nodes(row['M'], row['z'], row['phase_nums'] if isinstance(row['phase_nums'][0], list) else [row['phase_nums']], row['phase_den']), n)
        lamL, _ = lebesgue(leja_set(n), n)
        out['phi2'].append({'n': n, 'Lambda_F': lamF, 'Lambda_F_receipt': row['quality']['sampled_lebesgue'],
                            'Leja': lamL, 'Leja_receipt': row['baselines']['Leja'], 'F_loses_to_Leja': lamF > lamL})
        print(json.dumps(out['phi2'][-1]), flush=True)
    Path(sys.argv[2]).write_text(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
