#!/usr/bin/env python3
"""Exact seeded ranks of total-degree evaluation on C0 congruence fibres.

All arithmetic in rank_det is integer modular arithmetic. The catalogue is an
input, never silently regenerated. Axis reversal is the only extra symmetry
used here; the explicit map is included for every source row.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import random
import sys
import time


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exponents(n):
    return [(a, b, c) for degree in range(n + 1)
            for a in range(degree + 1) for b in range(degree - a + 1)
            for c in [degree - a - b]]


def selected(row):
    lengths = row['lengths']
    if 'indices' in row:
        return sorted(tuple(i) for i in row['indices'])
    a = row.get('a', row.get('coefficients'))
    residues = row.get('residues', [row.get('c', row.get('residue'))])
    return [i for i in itertools.product(*(range(L) for L in lengths))
            if sum(x * y for x, y in zip(a, i)) % row['k'] in residues]


def canonical_reversal(points, lengths):
    candidates = []
    for mask in range(1 << len(lengths)):
        transformed = tuple(sorted(tuple(L - 1 - x if mask >> j & 1 else x
                                         for j, (x, L) in enumerate(zip(i, lengths)))
                                   for i in points))
        candidates.append((transformed, mask))
    return min(candidates)


def rank_det(matrix, p):
    """Return rank and determinant; full elimination over F_p, no tolerance."""
    A = [[v % p for v in row] for row in matrix]
    m, width = len(A), len(A[0]) if A else 0
    rank, determinant = 0, 1
    for col in range(width):
        pivot = next((i for i in range(rank, m) if A[i][col]), None)
        if pivot is None:
            continue
        if pivot != rank:
            A[pivot], A[rank] = A[rank], A[pivot]
            determinant = -determinant
        v = A[rank][col]
        determinant = determinant * v % p
        inverse = pow(v, -1, p)
        pivotrow = [(value * inverse) % p for value in A[rank]]
        A[rank] = pivotrow
        for i in range(rank + 1, m):
            multiple = A[i][col]
            if multiple:
                A[i][col:] = [(a - multiple * b) % p
                             for a, b in zip(A[i][col:], pivotrow[col:])]
        rank += 1
        if rank == m:
            break
    return rank, determinant % p if rank == m == width else 0


def evaluation(points, axes, n, modulus=None):
    powers = [[[pow(value, degree, modulus) if modulus else value ** degree
                for degree in range(n + 1)] for value in axis] for axis in axes]
    powers_list = exponents(n)
    return [[powers[0][i][a] * powers[1][j][b] * powers[2][k][c]
             for a, b, c in powers_list] for i, j, k in points]


def load_rows(data):
    if isinstance(data, list):
        return data
    for key in ('patterns', 'rows', 'catalogue', 'admissible_patterns'):
        if key in data:
            return data[key]
    raise ValueError('Catalogue has no patterns/rows/catalogue key')


def run(args):
    started = time.time()
    data = json.loads(Path(args.catalogue).read_text())
    rows = [row for row in load_rows(data)
            if row.get('d', len(row['lengths'])) == 3 and 1 <= row['n'] <= 6]
    representatives, mapping = {}, []
    for serial, row in enumerate(rows):
        n, lengths = row['n'], tuple(row['lengths'])
        points = selected(row)
        assert len(points) == math.comb(n + 3, 3), row
        assert all(n + 1 <= L <= n + 3 for L in lengths), row
        canonical, reversal = canonical_reversal(points, lengths)
        key = (n, lengths, canonical)
        if key not in representatives:
            digest = hashlib.sha256(json.dumps(key, separators=(',', ':')).encode()).hexdigest()
            representatives[key] = {'id': 'C3-' + digest[:12], 'n': n,
                                    'lengths': list(lengths), 'points': canonical,
                                    'point_sha256': digest, 'tests': []}
        mapping.append({'pattern_id': row.get('id', row.get('pattern_id', str(serial))),
                        'representative': representatives[key]['id'],
                        'reversal_mask': reversal,
                        'properties': {'periodic': True, 'axis_criterion': 'unknown',
                                       'Lebesgue': 'untested'}})
    for record in representatives.values():
        n, lengths = record['n'], record['lengths']
        for prime in args.primes:
            assert prime > max(lengths)
            for trial in range(args.trials):
                seed = (args.seed + int(record['point_sha256'][:16], 16)
                        + 1000003 * prime + 1000000007 * trial)
                rng = random.Random(seed)
                axes = [rng.sample(range(prime), L) for L in lengths]
                rank, det = rank_det(evaluation(record['points'], axes, n, prime), prime)
                record['tests'].append({'p': prime, 'trial': trial, 'seed': seed,
                                        'axes': axes, 'rank': rank, 'det': det})
        record['points'] = [list(point) for point in record['points']]
        ranks = [test['rank'] for test in record['tests']]
        record['rank_min'], record['rank_max'] = min(ranks), max(ranks)
        record['N'] = math.comb(n + 3, 3)
    records = list(representatives.values())
    summary = []
    for n in range(1, 7):
        group = [r for r in records if r['n'] == n]
        ids = {r['id'] for r in group}
        summary.append({'n': n, 'patterns': sum(m['representative'] in ids for m in mapping),
                        'representatives': len(group),
                        'full_at_least_once': sum(r['rank_max'] == r['N'] for r in group),
                        'full_every_test': sum(r['rank_min'] == r['N'] for r in group),
                        'rank_histogram': {str(rank): sum(r['rank_max'] == rank for r in group)
                                           for rank in sorted({r['rank_max'] for r in group})}})
    output = {'schema': 'c3-ranks-v1', 'status': 'MEASURED finite exact ranks',
              'rules_base_sha': 'e949ef06895acd5463cdf8df7e0e5f795218f70f',
              'command': sys.argv, 'python': sys.version, 'platform': platform.platform(),
              'code_sha256': sha256(__file__), 'catalogue_sha256': sha256(args.catalogue),
              'base_seed': args.seed, 'primes': args.primes, 'trials': args.trials,
              'elapsed_seconds': round(time.time() - started, 3),
              'summary': summary, 'mapping': mapping, 'representatives': records}
    Path(args.output).write_text(json.dumps(output, separators=(',', ':')) + '\n')
    print(json.dumps({'output': args.output, 'bytes': Path(args.output).stat().st_size,
                      'sha256': sha256(args.output), 'summary': summary}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('catalogue')
    parser.add_argument('--output', required=True)
    parser.add_argument('--primes', nargs='+', type=int, default=[1009, 1013, 1019])
    parser.add_argument('--trials', type=int, default=2)
    parser.add_argument('--seed', type=int, default=2026103103)
    run(parser.parse_args())
