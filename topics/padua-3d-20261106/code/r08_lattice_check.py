#!/usr/bin/env python3
"""Independent round-08 checks; no imports of producer or audit checkers.

Enumerate forbidden HNF entries by solving linear congruences, then evaluate
dual groups by triangular equations and ranks with monomial Fourier columns.
All enumeration, folds and rational ranks are exact. Cosine residuals and
Lebesgue mesh values are separately marked numerical measurements.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools as it
import json
import math
from functools import lru_cache
from pathlib import Path
import platform
import sys
import time

import numpy as np
import sympy

INPUT_HEAD = '9042e1c42964150f30fdbe8563c12ba6c6a8692a'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def triples(q):
    for a in sympy.divisors(q):
        for d in sympy.divisors(q // a):
            yield int(a), int(d), q // a // d


def hnf_number(q):
    return sum(d * f * f for a, d, f in triples(q))


def forbidden_enumerator(n, q):
    """For x=a*u>0, solve u*c+v*e == k (mod f), |x|+|y|+|k|<2n.

    x=0 vectors are checked first. x<0 are their negatives. This marks
    precisely the HNFs admitting a short vector without testing each HNF.
    """
    R = 2 * n - 1
    for a, d, f in triples(q):
        if f <= R:
            continue
        es = np.arange(f, dtype=np.int64)
        keep = np.ones(f, dtype=bool)
        for v in range(1, R // d + 1):
            z = (v * es) % f
            keep &= np.minimum(z, f - z) > R - d * v
        es = es[keep]
        if not len(es):
            continue
        for b in range(d):
            bad = np.zeros((len(es), f), dtype=bool)
            erows = np.arange(len(es), dtype=np.int64)
            for u in range(1, R // a + 1):
                budget = R - a * u
                lo = (-budget - b * u + d - 1) // d
                hi = (budget - b * u) // d
                g = math.gcd(u, f)
                mod = f // g
                inv = pow(u // g, -1, mod) if mod > 1 else 0
                for v in range(lo, hi + 1):
                    S = budget - abs(b * u + d * v)
                    for k in range(-S, S + 1):
                        rhs = k - v * es
                        mask = rhs % g == 0
                        rows = erows[mask]
                        c0 = ((rhs[mask] // g) * inv) % mod
                        for j in range(g):
                            bad[rows, c0 + j * mod] = True
            for ei, c in np.argwhere(~bad):
                yield (a, b, int(c), d, int(es[ei]), f)


def canonical(k, h):
    a, b, c, d, e, f = h
    r0 = k[0] % a
    u = (k[0] - r0) // a
    y = k[1] - b * u
    r1 = y % d
    v = (y - r1) // d
    return (r0, r1, (k[2] - c * u - e * v) % f)


@lru_cache(maxsize=None)
def half_ball(n):
    R = 2 * n - 1
    return tuple(k for k in it.product(range(-R, R + 1), repeat=3)
                 if 0 < sum(map(abs, k)) <= R and next(x for x in k if x) > 0)


def admissible_direct(n, h):
    for k in half_ball(n):
        if canonical(k, h) == (0, 0, 0):
            return False
    return True


def dual(h):
    """Solve B theta=j in order theta3,theta2,theta1 with exact numerators."""
    a, b, c, d, e, f = h
    q = a * d * f
    out = []
    for j3 in range(f):
        z = j3 * a * d
        for j2 in range(d):
            y = (j2 * q - e * z) // d
            assert (j2 * q - e * z) % d == 0
            for j1 in range(a):
                x = (j1 * q - b * y - c * z) // a
                assert (j1 * q - b * y - c * z) % a == 0
                out.append((x % q, y % q, z % q))
    assert len(set(out)) == q
    return q, out


def folding(h):
    q, H = dual(h)
    counts = Counter(tuple(min(x, q - x) for x in v) for v in H)
    return q, counts


def exponents(n):
    return [(a, b, c) for a in range(n + 1) for b in range(n + 1 - a)
            for c in range(n + 1 - a - b)]


def rational_rank(h, n):
    """Exact rank of monomials on H from binomial Fourier expansions.

    The denominator 2**sum(alpha) scales one column and is dropped.
    Character frequencies are reduced directly modulo row lattice B.
    """
    pivots = {}
    for alpha in exponents(n):
        col = Counter()
        for rs in it.product(*(range(x + 1) for x in alpha)):
            k = tuple(alpha[j] - 2 * rs[j] for j in range(3))
            col[canonical(k, h)] += math.prod(math.comb(alpha[j], rs[j]) for j in range(3))
        col = {k: Fraction(v) for k, v in col.items()}
        while col:
            key = min(col)
            v = col[key]
            if key not in pivots:
                pivots[key] = {k: z / v for k, z in col.items()}
                break
            for k, z in pivots[key].items():
                val = col.get(k, 0) - v * z
                if val:
                    col[k] = val
                else:
                    col.pop(k, None)
    return len(pivots)


def modular_rank(rows, p):
    A = [[int(x) % p for x in row] for row in rows]
    r = 0
    for c in range(len(A[0])):
        j = next((j for j in range(r, len(A)) if A[j][c]), None)
        if j is None:
            continue
        A[r], A[j] = A[j], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [x * inv % p for x in A[r]]
        for j in range(r + 1, len(A)):
            v = A[j][c]
            if v:
                A[j] = [(x - v * y) % p for x, y in zip(A[j], A[r])]
        r += 1
        if r == len(A):
            break
    return r


def actual_node_rank(q, counts, n):
    t = 1
    while not sympy.isprime(t * q + 1):
        t += 1
    p = t * q + 1
    root = pow(int(sympy.primitive_root(p)), t, p)
    assert pow(root, q, p) == 1
    assert all(pow(root, q // ell, p) != 1 for ell in sympy.factorint(q))
    inv2 = pow(2, -1, p)
    points = [[(pow(root, x, p) + pow(root, -x, p)) * inv2 % p for x in k]
              for k in sorted(counts)]
    V = [[math.prod(pow(point[j], alpha[j], p) for j in range(3)) % p
          for alpha in exponents(n)] for point in points]
    return {'p': p, 'root_order': q, 'root': root, 'rank': modular_rank(V, p)}


def numerical_node_check(q, counts, n, quality=False):
    keys = sorted(counts)
    P = np.cos(2 * np.pi * np.array(keys) / q)
    w = np.array([counts[k] / q for k in keys])
    errors = []
    for alpha in exponents(2 * n - 1):
        exact = math.prod(0 if x % 2 else math.comb(x, x // 2) / 2**x for x in alpha)
        value = float(w @ np.prod(P ** np.array(alpha), axis=1))
        errors.append(abs(value - exact))
    result = {'weight_sum': float(w.sum()), 'min_weight': float(w.min()),
              'moment_max_abs_error': max(errors), 'monomials_checked': len(errors)}
    if quality:
        alpha = exponents(n)
        V = np.array([np.prod(P ** np.array(a), axis=1) for a in alpha]).T
        C = np.linalg.solve(V, np.eye(len(P)))
        axis = np.cos(np.pi * np.arange(41) / 40)
        best = 0.0
        for x in axis:
            test = np.array([(x, y, z) for y, z in it.product(axis, repeat=2)])
            E = np.array([np.prod(test ** np.array(a), axis=1) for a in alpha]).T
            best = max(best, float(np.abs(E @ C).sum(axis=1).max()))
        result['Lebesgue_mesh41'] = best
        result['interpolation_residual_inf'] = float(np.linalg.norm(V @ C - np.eye(len(V)), np.inf))
    return result


def examples():
    rows = []
    for z in [(1, 3, 7), (1, 4, 6), (1, 5, 8), (1, 7, 8)]:
        # h=(1,0,c,1,e,19) has dual generator (-c,-e,1).
        c = -z[0] * pow(z[2], -1, 19) % 19
        e = -z[1] * pow(z[2], -1, 19) % 19
        h = (1, 0, c, 1, e, 19)
        q, counts = folding(h)
        direct = Counter(tuple(min(x, 19-x) for x in (j*z[0]%19, j*z[1]%19, j*z[2]%19)) for j in range(19))
        assert counts == direct
        first = next(R for R in range(1, 10) if any(canonical(k, h) == (0, 0, 0)
            for k in it.product(range(-R, R + 1), repeat=3) if sum(map(abs, k)) == R))
        rows.append({'generator': z, 'hnf': h, 'det': q, 'fold': len(counts),
                     'dual_l1_minimum': first, 'rational_monomial_rank': rational_rank(h, 2),
                     'actual_node_modular_rank': actual_node_rank(q, counts, 2),
                     'numerical': numerical_node_check(q, counts, 2, quality=True),
                     'folded_nodes_sha256': hashlib.sha256(json.dumps(sorted(counts.items()),separators=(',', ':')).encode()).hexdigest()})
    h = (1, 3, 3, 6, 0, 10)
    q, counts = folding(h)
    rows.append({'n': 3, 'hnf': h, 'det': q, 'fold': len(counts),
                 'admissible': admissible_direct(3, h), 'rational_monomial_rank': rational_rank(h, 3),
                 'actual_node_modular_rank': actual_node_rank(q, counts, 3),
                 'numerical': numerical_node_check(q, counts, 3)})
    return rows


def controls():
    checked = 0
    for n in (1, 2, 3):
        for q in range(1, 41):
            actual = set(forbidden_enumerator(n, q))
            expected = set()
            for a, d, f in triples(q):
                for b, c, e in it.product(range(d), range(f), range(f)):
                    h = (a, b, c, d, e, f)
                    # This slower independent membership path exhausts all HNFs.
                    if admissible_direct(n, h):
                        expected.add(h)
                    checked += 1
            assert actual == expected, (n, q, actual ^ expected)
    return {'direct_membership_HNFs_checked': checked, 'n': [1, 2, 3], 'det_range': [1, 40]}


def complement(n, maxdet, rank_maxfold, raw_path):
    N = math.comb(n + 3, 3)
    started = time.monotonic()
    good = 0
    minfold = None
    detfirst = None
    distribution = Counter()
    small = []
    stream = hashlib.sha256()
    perq = []
    with raw_path.open('w') as out:
        for q in range(1, maxdet + 1):
            count = 0
            for h in forbidden_enumerator(n, q):
                count += 1
                good += 1
                _, fold = folding(h)
                m = len(fold)
                if detfirst is None:
                    detfirst = q
                if minfold is None or m < minfold[0]:
                    minfold = (m, q, h)
                record = [h, m]
                if m <= rank_maxfold:
                    r = rational_rank(h, n)
                    distribution[(m, r)] += 1
                    small.append([h, m, r])
                    record.append(r)
                line = json.dumps(record, separators=(',', ':')) + '\n'
                out.write(line)
                stream.update(line.encode())
            perq.append([q, count])
            if q % 20 == 0:
                print(json.dumps({'n': n, 'det_done': q, 'admissible': good,
                                  'seconds': round(time.monotonic()-started, 3)}), flush=True)
    return {'n': n, 'N': N, 'det_range': [1, maxdet], 'complete': True,
            'unrestricted_HNF_number': sum(hnf_number(q) for q in range(1, maxdet + 1)),
            'admissible': good, 'min_det': detfirst, 'min_fold': minfold,
            'rank_computed_through_fold': rank_maxfold,
            'fold_rank_histogram': sorted([m, r, c] for (m, r), c in distribution.items()),
            'full_rank_small': [row for row in small if row[-1] == N],
            'per_det_counts_sha256': hashlib.sha256(json.dumps(perq,separators=(',', ':')).encode()).hexdigest(),
            'admissible_stream_sha256': stream.hexdigest(), 'raw_path': str(raw_path),
            'raw_bytes': raw_path.stat().st_size, 'raw_sha256': digest(raw_path),
            'raw_policy': 'regenerate-only', 'seconds': time.monotonic()-started}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['examples', 'controls', 'complement'])
    parser.add_argument('--n', type=int)
    parser.add_argument('--maxdet', type=int)
    parser.add_argument('--rank-maxfold', type=int)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--raw', type=Path)
    args = parser.parse_args()
    if args.mode == 'examples':
        result = examples()
    elif args.mode == 'controls':
        result = controls()
    else:
        assert args.n and args.raw
        N = math.comb(args.n + 3, 3)
        result = complement(args.n, args.maxdet or 8*N, args.rank_maxfold or N, args.raw)
    payload = {'verification_record': True, 'input_head': INPUT_HEAD,
               'checker_sha256': digest(__file__),
               'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                               'sympy': sympy.__version__, 'platform': platform.platform()},
               'command': sys.argv, 'result': result}
    args.out.write_text(json.dumps(payload, separators=(',', ':')) + '\n')
    assert args.out.stat().st_size < 16384
    print(json.dumps({'output': str(args.out), 'bytes': args.out.stat().st_size,
                      'sha256': digest(args.out)}), flush=True)


if __name__ == '__main__':
    main()
