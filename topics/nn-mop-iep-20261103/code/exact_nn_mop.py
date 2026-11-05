#!/usr/bin/env python3
"""Finite rational sanity checks of defining MOP systems and NN recurrences.

Standard-library only. Polynomial coefficients are in ascending degree order.
No numerical tolerance, random input, or general-proof claim is used.
"""
from fractions import Fraction as Q
from math import comb
import argparse
import hashlib
import json
from pathlib import Path
import platform


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0) for i in range(max(len(p), len(q)))])


def scale(c, p):
    return trim([c * v for v in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, v in enumerate(p):
        for j, w in enumerate(q):
            out[i+j] += v*w
    return trim(out)


def solve_det(matrix, rhs):
    """Exact elimination, including a singular flag; determinant of [] is 1."""
    n = len(rhs)
    a = [list(row) + [b] for row, b in zip(matrix, rhs)]
    det = Q(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Q(0), None
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            det = -det
        v = a[k][k]
        det *= v
        a[k] = [z/v for z in a[k]]
        for i in range(k+1, n):
            v = a[i][k]
            a[i] = [z-v*w for z, w in zip(a[i], a[k])]
    out = [Q(0)] * n
    for i in reversed(range(n)):
        out[i] = a[i][-1] - sum(a[i][j]*out[j] for j in range(i+1, n))
    return det, out


def matrix_mul(a, b):
    return [[sum_poly(mul(a[i][k], b[k][j]) for k in range(3))
             for j in range(3)] for i in range(3)]


def sum_poly(ps):
    out = (Q(0),)
    for p in ps:
        out = add(out, p)
    return out


def inputs(family, size):
    if family == 'generic':
        nodes = [Q(k*k+k+1, k+2) for k in range(size)]
        weights = [[Q(2**k, 3**k) for k in range(size)],
                   [Q(3**k, 5**k) for k in range(size)]]
    else:
        nodes = [Q(k) for k in range(size)]
        # Binomial(size-1,p), p=1/3 and p=2/3, exactly normalized.
        weights = [[Q(comb(size-1, k)*p**k*(3-p)**(size-1-k),
                      3**(size-1)) for k in range(size)] for p in (1, 2)]
    assert len(set(nodes)) == size
    assert all(w > 0 for row in weights for w in row)
    return nodes, weights


def run_case(family, size):
    nodes, weights = inputs(family, size)
    moments = [[sum(w*x**j for x, w in zip(nodes, ws))
                for j in range(2*size+3)] for ws in weights]
    polys, determinants = {}, {}
    counts = dict(normality_interior=0, normality_terminal=0,
                  orthogonality=0, recurrence=0, successor_difference=0,
                  transfer_action=0, flatness=0, terminal_product=0,
                  terminal_support_zero=0, terminal_h_zero=0,
                  proportional_singular=0, terminal_d_zero=0,
                  nonterminal_d_nonzero=0, fixed_site_noncommuting=0,
                  beyond_support_singular=0)

    def moment(p, direction, power):
        return sum(v*moments[direction][i+power] for i, v in enumerate(p))

    for total in range(size+1):
        for n in range(total+1):
            m = total-n
            rows = [(j, k) for j, bound in enumerate((n, m)) for k in range(bound)]
            mat = [[moments[j][k+i] for i in range(total)] for j, k in rows]
            rhs = [-moments[j][k+total] for j, k in rows]
            det, solution = solve_det(mat, rhs)
            assert det != 0, (family, size, n, m, 'normality')
            counts['normality_terminal' if total == size else 'normality_interior'] += 1
            p = tuple(solution) + (Q(1),)
            polys[n, m], determinants[n, m] = p, det
            for j, k in rows:
                assert moment(p, j, k) == 0
                counts['orthogonality'] += 1

    coeffs = {}
    for (n, m), p in polys.items():
        if n+m >= size:
            continue
        # h ratios fix a,c separately even when predecessor polynomials depend.
        a = moment(p, 0, n)/moment(polys[n-1, m], 0, n-1) if n else Q(0)
        c = moment(p, 1, m)/moment(polys[n, m-1], 1, m-1) if m else Q(0)
        sub = p[-2] if n+m else Q(0)
        b = [sub-polys[n+1, m][-2], sub-polys[n, m+1][-2]]
        coeffs[n, m] = (a, c, b[0], b[1])
        if n+m == size-1:
            assert b[1]-b[0] == 0
            counts['terminal_d_zero'] += 1
        else:
            assert b[1]-b[0] != 0
            counts['nonterminal_d_nonzero'] += 1
        lower = sum_poly([scale(a, polys[n-1, m])] if n else [])
        if m:
            lower = add(lower, scale(c, polys[n, m-1]))
        for j, successor in enumerate(((n+1, m), (n, m+1))):
            assert mul((0, 1), p) == add(polys[successor], add(scale(b[j], p), lower))
            counts['recurrence'] += 1
        assert add(polys[n+1, m], scale(-1, polys[n, m+1])) == scale(b[1]-b[0], p)
        counts['successor_difference'] += 1

    def transfer(n, m, direction):
        a, c, b1, b2 = coeffs[n, m]
        if direction == 0:
            lo = coeffs[n, m-1]
            return [[(-b1, Q(1)), (-a,), (-c,)],
                    [(Q(1),), (Q(0),), (Q(0),)],
                    [(Q(1),), (Q(0),), (lo[3]-lo[2],)]]
        lo = coeffs[n-1, m]
        return [[(-b2, Q(1)), (-a,), (-c,)],
                [(Q(1),), (lo[2]-lo[3],), (Q(0),)],
                [(Q(1),), (Q(0),), (Q(0),)]]

    commutator_witness = None
    for n, m in coeffs:
        if n == 0 or m == 0:
            continue
        state = [polys[n, m], polys[n-1, m], polys[n, m-1]]
        # Fixed-site products do NOT express index-shift compatibility.
        t1, t2 = transfer(n, m, 0), transfer(n, m, 1)
        prod12, prod21 = matrix_mul(t1, t2), matrix_mul(t2, t1)
        comm_at_zero = [[prod12[i][j][0]-prod21[i][j][0]
                         for j in range(3)] for i in range(3)]
        nonzero = [(i, j, comm_at_zero[i][j]) for i in range(3)
                   for j in range(3) if comm_at_zero[i][j]]
        if nonzero:
            counts['fixed_site_noncommuting'] += 1
            if commutator_witness is None:
                i, j, value = nonzero[0]
                commutator_witness = dict(n=n, m=m, x='0', row=i+1,
                                          column=j+1, value=str(value))
        for j, dest in enumerate(((n+1, m), (n, m+1))):
            t = transfer(n, m, j)
            target = [polys[dest], polys[dest[0]-1, dest[1]], polys[dest[0], dest[1]-1]]
            assert [sum_poly(mul(v, p) for v, p in zip(row, state)) for row in t] == target
            counts['transfer_action'] += 1
        if n+m <= size-2:
            assert matrix_mul(transfer(n+1, m, 1), transfer(n, m, 0)) == \
                   matrix_mul(transfer(n, m+1, 0), transfer(n, m, 1))
            counts['flatness'] += 1

    common = (Q(1),)
    for x in nodes:
        common = mul(common, (-x, Q(1)))
    for n in range(size+1):
        p = polys[n, size-n]
        assert p == common
        counts['terminal_product'] += 1
        for x in nodes:
            assert sum(v*x**k for k, v in enumerate(p)) == 0
            counts['terminal_support_zero'] += 1
        for j in range(2):
            assert moment(p, j, n if j == 0 else size-n) == 0
            counts['terminal_h_zero'] += 1

    # First layer beyond the support size has no unique monic solution.
    for n in range(size+2):
        m, total = size+1-n, size+1
        rows = [(j, k) for j, bound in enumerate((n, m)) for k in range(bound)]
        mat = [[moments[j][k+i] for i in range(total)] for j, k in rows]
        rhs = [-moments[j][k+total] for j, k in rows]
        det, solution = solve_det(mat, rhs)
        assert det == 0 and solution is None
        counts['beyond_support_singular'] += 1

    # Positive proportional measures: duplicate rows at (1,1).
    mu = moments[0]
    det, solution = solve_det([[mu[0], mu[1]], [2*mu[0], 2*mu[1]]],
                              [-mu[2], -2*mu[2]])
    assert det == 0 and solution is None
    counts['proportional_singular'] += 1
    # The underdetermined monic equations are consistent: choose x^2-mu2/mu0.
    assert mu[2] - (mu[2]/mu[0])*mu[0] == 0
    identity = json.dumps({'nodes': list(map(str, nodes)),
                           'weights': [list(map(str, ws)) for ws in weights]}, sort_keys=True)
    return dict(family=family, N=size, input_sha256=hashlib.sha256(identity.encode()).hexdigest(),
                counts=counts, fixed_site_commutator_witness=commutator_witness,
                all_passed=True)


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are the exact checks.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--min-n', type=int, default=2)
    parser.add_argument('--max-n', type=int, default=8)
    args = parser.parse_args()
    if not 2 <= args.min_n <= args.max_n <= 8:
        parser.error('require 2 <= min-n <= max-n <= 8')
    cases = [run_case(family, size) for family in ('generic', 'binomial')
             for size in range(args.min_n, args.max_n+1)]
    totals = {key: sum(c['counts'][key] for c in cases) for key in cases[0]['counts']}
    print(json.dumps(dict(status='MEASURED finite exact sanity checks; no general proof',
                         python=platform.python_version(), arithmetic='fractions.Fraction',
                         code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         cases=cases, totals=totals, all_passed=True), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
