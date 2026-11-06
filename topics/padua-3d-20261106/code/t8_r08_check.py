#!/usr/bin/env python3
"""Independent T8 round08 checks. No imports of project mathematics.

Exact ranks use monomials at actual cosine nodes modulo fresh splitting
primes. A separate integer cosine-coefficient reduction decides the complete
n3 half-shift census over Q. Floating mesh norms are MEASURED lower samples.
"""
import argparse
from collections import Counter
from functools import reduce
import hashlib
import itertools as it
import json
import math
import os
from pathlib import Path
import platform
import sys
import tempfile
import time

import numpy as np
import scipy
import scipy.linalg as la

RULES = '9042e1c42964150f30fdbe8563c12ba6c6a8692a'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def object_digest(value):
    return hashlib.sha256(json.dumps(value, separators=(',', ':')).encode()).hexdigest()


def modes(n):
    return [(a, b, c) for a in range(n + 1) for b in range(n + 1 - a)
            for c in range(n + 1 - a - b)]


def nodes(M, z, nums, D):
    L = math.lcm(M, D)
    folded = sorted({tuple(min(v, -v % L) for v in
                           ((k * zj * (L // M) + aj * (L // D)) % L
                            for zj, aj in zip(z, nums))) for k in range(M)})
    return L, folded


def prime_factors(n):
    factors = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            factors.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        factors.append(n)
    return factors


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # These bases are deterministic below 2**64; our guard is much smaller.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def splitting_prime(L, floor):
    p = ((floor - 1 + L - 1) // L) * L + 1
    while not is_prime(p):
        p += L
    if not 3 <= p < 1900000000:
        raise ValueError('exact int64 product bound requires p < 1.9e9')
    for a in range(2, p):
        omega = pow(a, (p - 1) // L, p)
        if pow(omega, L, p) == 1 and all(
                pow(omega, L // q, p) != 1 for q in prime_factors(L)):
            return p, omega
    raise RuntimeError('no primitive Lth root')


def rank_det(matrix, p):
    A = np.array(matrix, dtype=np.int64, copy=True) % p
    nr, nc = A.shape
    rank, det = 0, 1
    for col in range(nc):
        nonzero = np.flatnonzero(A[rank:, col])
        if not len(nonzero):
            continue
        pivot_row = rank + int(nonzero[0])
        if pivot_row != rank:
            A[[rank, pivot_row]] = A[[pivot_row, rank]]
            det = -det
        pivot = int(A[rank, col])
        det = det * pivot % p
        A[rank, col:] = A[rank, col:] * pow(pivot, -1, p) % p
        A[rank + 1:, col:] = (A[rank + 1:, col:] -
                             A[rank + 1:, col, None] * A[rank, None, col:]) % p
        rank += 1
        if rank == nr:
            break
    return rank, det % p if nr == nc and rank == nc else None


def certificate(n, M, z, nums, D, prime_floor=1700000000):
    L, folded = nodes(M, z, nums, D)
    result = {'n': n, 'M': M, 'z': list(z), 'phase_nums': list(nums),
              'phase_den': D, 'L': L, 'nodes': len(folded),
              'nodes_sha256': object_digest(folded), 'checks': []}
    previous_prime = 0
    for floor in (prime_floor, prime_floor + 1000000):
        floor = max(floor, previous_prime + L)
        p, omega = splitting_prime(L, floor)
        previous_prime = p
        inv2 = pow(2, -1, p)
        x = [[(pow(omega, v, p) + pow(omega, -v, p)) * inv2 % p
              for v in row] for row in folded]
        # Scalar Python powers/products remove any ambiguity about overflow
        # in building monomials. Elimination products are below p**2 < 2**63.
        A = [[math.prod(pow(t, a, p) for t, a in zip(row, alpha)) % p
              for alpha in modes(n)] for row in x]
        rank, det = rank_det(A, p)
        result['checks'].append({'p': p, 'omega': omega, 'rank': rank,
                                 'det': det, 'matrix_sha256': object_digest(A)})
    return result


def integer_rank(matrix):
    """Exact row elimination over Q, keeping primitive integer rows."""
    A = [list(map(int, row)) for row in matrix]
    r = 0
    for j in range(len(A[0])):
        pivot = next((i for i in range(r, len(A)) if A[i][j]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        p = A[r][j]
        for i in range(r + 1, len(A)):
            c = A[i][j]
            if c:
                row = [p * x - c * y for x, y in zip(A[i][j:], A[r][j:])]
                g = reduce(math.gcd, row)
                A[i][j:] = [v // g for v in row] if g else row
        r += 1
        if r == len(A):
            break
    return r


def integer_determinant(matrix):
    """Bareiss determinant; all divisions are checked for exactness."""
    A = [list(map(int, row)) for row in matrix]
    previous, sign = 1, 1
    for k in range(len(A) - 1):
        pivot_row = next((i for i in range(k, len(A)) if A[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, len(A)):
            for j in range(k + 1, len(A)):
                numerator = pivot * A[i][j] - A[i][k] * A[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ValueError('Bareiss division not exact')
                A[i][j] = quotient
            A[i][k] = 0
        previous = pivot
    return sign * A[-1][-1]


def cosine_coefficients(n, z):
    """Integer coefficient matrix for 8*product cos(a_j*z_j*theta).

    theta=(2k+1)*pi/M, M=2N. Independent DCT basis cos(r*theta),
    0<=r<N. cos(N*theta)=0; cos((M-r)*theta)=-cos(r*theta).
    """
    N = math.comb(n + 3, 3)
    M = 2 * N
    C = [[0] * N for _ in range(N)]
    for col, alpha in enumerate(modes(n)):
        for signs in it.product((-1, 1), repeat=3):
            r = sum(e * a * zj for e, a, zj in zip(signs, alpha, z)) % (2 * M)
            r = min(r, 2 * M - r)
            sign = 1
            if r > N:
                r, sign = M - r, -1
            if r != N:
                C[r][col] += sign
    return C


def census_n3():
    n, N, M = 3, 20, 40
    distribution, survivors = Counter(), []
    count_failures = 0
    modular_agreements = 0
    catalogue = []
    for b, c in it.combinations(range(1, M), 2):
        z = (1, b, c)
        L, folded = nodes(M, z, z, 2 * M)
        count_failures += len(folded) != N
        r = integer_rank(cosine_coefficients(n, z))
        cert = certificate(n, M, z, z, 2 * M)
        if any(c['rank'] > r for c in cert['checks']):
            raise ValueError('finite-field rank exceeds exact coefficient rank')
        modular_agreements += all(c['rank'] == r for c in cert['checks'])
        catalogue.append({'z': list(z), 'exact_rank': r,
                          'modular_ranks': [c['rank'] for c in cert['checks']]})
        distribution[r] += 1
        if r == N:
            cert['abs_det_integer_cosine_coefficients'] = abs(integer_determinant(cosine_coefficients(n, z)))
            survivors.append(cert)
    if count_failures:
        raise ValueError('half-shift count derivation contradicted')
    raw = Path(tempfile.mkdtemp(prefix='padua-t8-r08-independent-')) / 'n3-ranks.jsonl'
    raw.write_text(''.join(json.dumps(r, separators=(',', ':')) + '\n' for r in catalogue))
    return {'n': n, 'N': N, 'M': M, 'pairs': math.comb(M - 1, 2),
            'count_failures': count_failures, 'exact_rational_rank_distribution': dict(distribution),
            'two_prime_actual_node_rank_agreements': modular_agreements,
            'raw_regenerate_only': {'path': str(raw), 'bytes': raw.stat().st_size,
                                   'sha256': digest(raw)}, 'survivors': survivors}


def structural():
    rows = []
    for n in range(1, 41):
        N = math.comb(n + 3, 3)
        m = n // 2
        closed = ([(m + 1) ** 2, m + 1, (m + 1) ** 2] if n % 2 == 0 else
                  [(m + 1) * (m + 2), 0, -(m + 1) * (m + 2)])
        direct = [sum((-1) ** sum(alpha[:t]) for alpha in modes(n)) for t in (1, 2, 3)]
        if closed != direct or (N % 2 == 1) != (n % 4 == 0):
            raise ValueError('trace/parity formula mismatch')
        if 3 <= n <= 8:
            M, f = 2 * N, N % 2
            counts = []
            for b, c in [(1, 2), (2, M - 1), (M - 2, M - 1)]:
                _, folded = nodes(M, (1, b, c), (1, b, c), 2 * M)
                # x_j=0 iff v=L/4. For odd z_j all must vanish.
                fixed = sum(all(zj % 2 == 0 or 4 * v == 2 * M
                                for v, zj in zip(row, (1, b, c))) for row in folded)
                if len(folded) != N or fixed != f:
                    raise ValueError('direct count/fixed-node mismatch')
                counts.append([b, c, len(folded), fixed])
            rows.append({'n': n, 'N': N, 'fixed_nodes': f, 'trace_t123': direct,
                         'rank_ceiling_t123': [N - abs(d - f) // 2 for d in direct],
                         'direct_fold_samples': counts})
    return {'trace_formula_degrees': [1, 40], 'rows': rows}


def basis(points, n):
    points = np.asarray(points)
    tables = [np.polynomial.chebyshev.chebvander(points[:, j], n) for j in range(3)]
    return np.column_stack([tables[0][:, a] * tables[1][:, b] * tables[2][:, c]
                            for a, b, c in modes(n)])


def mesh_quality(n, points, side=21):
    V = basis(points, n)
    # Independent numerical route: explicit inverse and batched evaluation.
    inverse = np.linalg.inv(V)
    singular = np.linalg.svd(V, compute_uv=False)
    axis = np.cos(np.pi * np.arange(side) / (side - 1))
    maximum, where = 0.0, None
    for x in axis:
        grid = np.array([(x, y, z) for y, z in it.product(axis, repeat=2)])
        values = np.sum(np.abs(basis(grid, n) @ inverse), axis=1)
        k = int(np.argmax(values))
        if values[k] > maximum:
            maximum, where = float(values[k]), grid[k].tolist()
    return {'sampled_lambda': maximum, 'mesh_side': side, 'maximizer': where,
            'condition2': float(singular[0] / singular[-1]),
            'inverse_residual_inf': float(np.linalg.norm(V @ inverse - np.eye(len(V)), np.inf)),
            'points_sha256': object_digest(np.asarray(points).tolist())}


def quality_with_controls(n, z):
    N = math.comb(n + 3, 3)
    L, folded = nodes(2 * N, z, z, 4 * N)
    points = np.cos(2 * np.pi * np.array(folded) / L)
    axis = np.cos(np.pi * np.arange(n + 1) / n)
    remaining, order = list(range(1, n + 1)), [0]
    while remaining:
        score = [float(np.prod([abs(axis[i] - axis[j]) for j in order])) for i in remaining]
        k = max(range(len(remaining)), key=lambda k: (score[k], -remaining[k]))
        order.append(remaining.pop(k))
    axis = axis[order]
    leja = np.array([[axis[a], axis[b], axis[c]] for a, b, c in modes(n)])
    caxis = np.cos(np.pi * np.arange(2 * n + 1) / (2 * n))
    candidates = np.array(list(it.product(caxis, repeat=3)))
    # The frozen QR implementation uses total-degree order, not lexicographic
    # mode order; floating pivot ties depend on this ordering.
    graded = [(a, b, d - a - b) for d in range(n + 1)
              for a in range(d + 1) for b in range(d - a + 1)]
    position = {alpha: i for i, alpha in enumerate(modes(n))}
    qr_matrix = basis(candidates, n)[:, [position[a] for a in graded]].T.copy()
    _, _, pivots = la.qr(qr_matrix, pivoting=True, mode='economic')
    qr = candidates[pivots[:N]]
    return {'n': n, 'z': list(z), 'halfshift': mesh_quality(n, points),
            'Leja': mesh_quality(n, leja), 'QR': mesh_quality(n, qr),
            'leja_axis_order': order, 'qr_candidate_side': 2 * n + 1,
            'qr_mode_order': 'graded total degree, then a, then b'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--old-witnesses', type=Path)
    parser.add_argument('--structure', action='store_true')
    parser.add_argument('--census-n3', action='store_true')
    parser.add_argument('--halfshift', type=Path)
    parser.add_argument('--quality', action='store_true')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    result = {'schema': 't8-r08-independent-v1', 'rules_input': RULES,
              'model': 'gpt-6.1-sol xhigh (assigned; runtime metadata unexposed)',
              'command': sys.argv, 'code_sha256': digest(__file__),
              'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                           'scipy': scipy.__version__},
              'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')},
              'inputs': {}, 'results': {}}
    if args.old_witnesses:
        result['inputs'][str(args.old_witnesses)] = digest(args.old_witnesses)
        rows = json.loads(args.old_witnesses.read_text())['rows']
        result['results']['old_witnesses'] = [certificate(r['n'], r['M'], r['z'],
                r['phase_nums'], r['phase_den']) for r in rows]
    if args.structure:
        result['results']['structure'] = structural()
    if args.census_n3:
        result['results']['census_n3'] = census_n3()
        if args.quality:
            result['results']['n3_survivor_quality'] = [quality_with_controls(3, r['z'])
                for r in result['results']['census_n3']['survivors']]
    if args.halfshift:
        result['inputs'][str(args.halfshift)] = digest(args.halfshift)
        # Producer receipt selection is data; no producer code is imported.
        data = json.loads(args.halfshift.read_text())
        root = Path(__file__).resolve().parents[3]
        for filename, expected in data['code_dependencies_sha256'].items():
            actual = digest(root / filename)
            if actual != expected:
                raise ValueError('producer executable dependency changed: ' + filename)
            result['inputs'][filename] = actual
        rows = data['rows']
        positives = [r for r in rows if r.get('selected')]
        result['results']['halfshift'] = [certificate(r['n'], r['M'], r['selected']['z'],
                r['selected']['z'], 2 * r['M']) for r in positives]
        if args.quality:
            result['results']['quality'] = [quality_with_controls(r['n'], r['selected']['z'])
                                             for r in positives]
            for q, reference in zip(result['results']['quality'], positives):
                q['reference_absolute_deltas'] = {
                    'halfshift_lambda': abs(q['halfshift']['sampled_lambda'] - reference['selected']['quality']['sampled_lebesgue']),
                    'Leja_lambda': abs(q['Leja']['sampled_lambda'] - reference['baselines']['Leja']['sampled_lebesgue']),
                    'QR_lambda': abs(q['QR']['sampled_lambda'] - reference['baselines']['QR']['sampled_lebesgue'])}
                if max(q['reference_absolute_deltas'].values()) > 1e-7:
                    raise ValueError('frozen quality control differs from producer')
                q['D2'] = {'QR_loss_n_ge4': q['n'] >= 4 and q['halfshift']['sampled_lambda'] > q['QR']['sampled_lambda'],
                           'Leja_loss_eligible_n_ge6': q['n'] >= 6 and q['halfshift']['sampled_lambda'] > q['Leja']['sampled_lambda']}
    result['elapsed_seconds'] = round(time.monotonic() - start, 3)
    encoded = json.dumps(result, separators=(',', ':')) + '\n'
    if len(encoded.encode()) >= 16384:
        raise ValueError('durable receipt must be <16 KiB')
    args.output.write_text(encoded)
    print(json.dumps({'output': str(args.output), 'bytes': len(encoded.encode()),
                      'sha256': digest(args.output), 'seconds': result['elapsed_seconds']}))


if __name__ == '__main__':
    main()
