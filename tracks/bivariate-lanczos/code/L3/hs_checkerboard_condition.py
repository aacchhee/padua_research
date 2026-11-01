"""MEASURED: condition (H) (theory file 303) on ordered Harris-Simanek checkerboards.

S_e = {(X_i, Y_j) : i + j = e mod 2}, X ordered (length n+1), Y ordered (length n+2):
M = N_n points (square case). plan.md "Benchmarks": positive alternation weights for
ordered X, Y (source codex/charter-unisolvence-20261031@eb7bdcd PD-T001/PD-T003,
developer PROVED, NOT accepted; cited by branch/SHA/ID only). (H) and S_1 depend only
on the nodes, so the weights are not needed here; the checkerboard is used as a
square-case control family that contains Padua (X = cos(i pi/n), Y = cos(j pi/(n+1))).

Families: cheb (Chebyshev-Lobatto = Padua), equi (equispaced), rand (sorted uniform,
numpy default_rng(seed)), graded (x = -1 + 2 t^2 on equispaced t, clustering at -1).
Usage: python3 hs_checkerboard_condition.py nmax [seed]
"""
import sys
import numpy as np
from hess_condition import analyse


def checker(X, Y, e=0):
    return np.array([(x, y) for i, x in enumerate(X) for j, y in enumerate(Y) if (i + j) % 2 == e])


def fam(name, n, rng):
    if name == 'cheb':
        return np.cos(np.arange(n + 1) * np.pi / n), np.cos(np.arange(n + 2) * np.pi / (n + 1))
    if name == 'equi':
        return np.linspace(-1, 1, n + 1), np.linspace(-1, 1, n + 2)
    if name == 'rand':
        return np.sort(rng.uniform(-1, 1, n + 1)), np.sort(rng.uniform(-1, 1, n + 2))
    if name == 'graded':
        return -1 + 2 * np.linspace(0, 1, n + 1) ** 2, -1 + 2 * np.linspace(0, 1, n + 2) ** 2
    raise ValueError(name)


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    rng = np.random.default_rng(seed)
    print(f"HS checkerboards e=0, nmax={nmax}, seed={seed}")
    for name in ('cheb', 'equi', 'graded', 'rand', 'rand'):
        for n in range(1, nmax + 1):
            X, Y = fam(name, n, rng)
            r = analyse(checker(X, Y, 0), n)
            verdict = ('(H) holds' if (r['tD'] or -1) > 1e-6 else
                       'robust failure' if (r['lP'] or 0) > 1e-6 else 'unresolved')
            print(f"  {name:6s} n={n}: dimS1={r['dimS1']} (exp {r['expected']}) kerHess={r['kerHess']} "
                  f"tD={r['tD']:.3e} lP={r['lP']:.3e} -> {verdict}", flush=True)


if __name__ == '__main__':
    main()
