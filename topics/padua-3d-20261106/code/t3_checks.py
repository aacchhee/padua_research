#!/usr/bin/env python3
"""Small exact sanity checks for T3's analytic character reductions."""
import argparse
import hashlib
import itertools
import json
import platform
from fractions import Fraction
from pathlib import Path


def indices(d, n):
    return [a for a in itertools.product(range(n+1), repeat=d) if sum(a) <= n]


def rank(a, p=None):
    a = [[(x % p if p else Fraction(x)) for x in row] for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = pow(int(a[r][j]), -1, p) if p else 1/a[r][j]
        a[r] = [(x*q % p if p else x*q) for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                q = a[i][j]
                a[i] = [((x-q*y) % p if p else x-q*y)
                        for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def root(order, p):
    for a in range(1, p):
        if pow(a, order, p) == 1 and all(pow(a, e, p) != 1
                                       for e in range(1, order)):
            return a
    raise ValueError('No primitive root of requested order')


def cheb(n, x, p):
    if n == 0:
        return 1
    a, b = 1, x
    for _ in range(1, n):
        a, b = b, (2*x*b-a) % p
    return b


def dictionary(d, n, m, z):
    ids = indices(d, n)
    a = [[0]*len(ids) for _ in range(m//2+1)]
    for j, alpha in enumerate(ids):
        for eps in itertools.product((-1, 1), repeat=d):
            s = sum(e*b*c for e, b, c in zip(eps, alpha, z)) % m
            a[min(s, (-s) % m)][j] += 1
    return ids, a


def phase_case(d, n, m, z, order, phase, p):
    assert order % m == 0 and (p-1) % order == 0 and p % 2
    rho = root(order, p)
    omega = pow(rho, order//m, p)
    ids = indices(d, n)
    b = [[0]*len(ids) for _ in range(m)]
    for j, alpha in enumerate(ids):
        for eps in itertools.product((-1, 1), repeat=d):
            s = sum(e*a*c for e, a, c in zip(eps, alpha, z)) % m
            h = sum(e*a*c for e, a, c in zip(eps, alpha, phase)) % order
            b[s][j] = (b[s][j] + pow(rho, h, p)) % p
    v = []
    for k in range(m):
        x = []
        for zj, aj in zip(z, phase):
            t = pow(rho, (aj + (order//m)*k*zj) % order, p)
            x.append((t + pow(t, -1, p))*pow(2, -1, p) % p)
        row = []
        for j, alpha in enumerate(ids):
            value = 1
            for a, xx in zip(alpha, x):
                value = value*cheb(a, xx, p) % p
            transformed = sum(pow(omega, k*r, p)*b[r][j]
                              for r in range(m))*pow(2**d, -1, p) % p
            assert value == transformed
            row.append(value)
        v.append(row)
    assert rank(v, p) == rank(b, p)
    return {'d': d, 'n': n, 'M': m, 'z': z, 'root_order': order,
            'phase_numerators': phase, 'prime': p, 'primitive_root': rho,
            'rank': rank(b, p), 'factorization_equal': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = [phase_case(2, 2, 11, [1, 3], 11, [0, 0], 23),
              phase_case(3, 1, 7, [1, 2, 3], 28, [1, 3, 5], 29),
              phase_case(2, 2, 8, [1, 3], 16, [1, 3], 17)]
    ids, d = dictionary(2, 2, 11, [1, 3])
    rational_rank = rank(d)
    assert rational_rank == 6
    assert any(d[r][ids.index((2, 0))] and d[r][ids.index((1, 1))]
               for r in range(len(d)))
    assert all(sum(d[r][j] for r in range(len(d))) == 4
               for j in range(len(ids)))
    # Integer polynomial verification: (W-UV)^2=(1-U^2)(1-V^2)
    # gives U^2+V^2+W^2-2UVW-1 after cancellation.
    # Check by direct substitution on integer unit-circle parameterizations
    # scaled to rational cosines/sines; Fraction arithmetic is exact.
    surfaces = 0
    for u in range(1, 5):
        for v in range(1, 5):
            cu, su = Fraction(1-u*u, 1+u*u), Fraction(2*u, 1+u*u)
            cv, sv = Fraction(1-v*v, 1+v*v), Fraction(2*v, 1+v*v)
            for sign in (-1, 1):
                w = sign*(cu*cv-su*sv)
                assert cu*cu+cv*cv+w*w-2*sign*cu*cv*w-1 == 0
                surfaces += 1
    result = {'schema': 't3-exact-sanity-v1', 'python': platform.python_version(),
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'phase_cases': checks, 'shared_frequency_full_rank': rational_rank,
              'zero_index_multiplicity_preserved': True,
              'rational_surface_substitutions': surfaces,
              'all_assertions_passed': True,
              'independent_replay': 'not performed by developer'}
    output = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
