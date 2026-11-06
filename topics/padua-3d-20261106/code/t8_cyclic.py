#!/usr/bin/env python3
"""Exact cyclic fold/rank census. Raw records are regenerate-only in /tmp."""
import argparse
import collections
from fractions import Fraction
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import time

import numpy as np
import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix

TOP = Path(__file__).resolve().parents[1]
SCRATCH = Path('/tmp/padua-3d-20261106')


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def modes(n, d=3):
    return [a for a in it.product(range(n + 1), repeat=d) if sum(a) <= n]


def fold(r, M):
    r %= M
    return min(r, M - r)


def nodes(M, z, phases=None):
    """Integer angle representatives with one common exact denominator."""
    L = M if phases is None else math.lcm(M, 24)
    a = [0] * len(z) if phases is None else [h * (L // 24) for h in phases]
    return L, tuple(sorted({tuple(fold(a[j] + k * z[j] * (L // M), L)
                                   for j in range(len(z))) for k in range(M)}))


def node_key(L, pts):
    # Full exact tuples are compared; hashing is used only for receipts.
    return min(tuple(sorted(tuple(Fraction(pt[j], L) for j in p) for pt in pts))
               for p in it.permutations(range(len(pts[0]))))


def dictionary(n, M, z):
    D = [[0] * len(modes(n, len(z))) for _ in range(M // 2 + 1)]
    for j, a in enumerate(modes(n, len(z))):
        for e in it.product((-1, 1), repeat=len(z)):
            D[fold(sum(s * b * c for s, b, c in zip(e, a, z)), M)][j] += 1
    return D


def mod_rank(D, p=1000003):
    A = np.array(D, dtype=np.int64) % p
    rank = 0
    for j in range(A.shape[1]):
        choices = np.flatnonzero(A[rank:, j])
        if not len(choices):
            continue
        i = rank + int(choices[0])
        A[[rank, i]] = A[[i, rank]]
        A[rank] = A[rank] * pow(int(A[rank, j]), -1, p) % p
        A[rank + 1:] = (A[rank + 1:] - A[rank + 1:, j, None] * A[rank]) % p
        rank += 1
        if rank == A.shape[0]:
            break
    return rank


def rank_null(D):
    N = len(D[0])
    mr = mod_rank(D)
    if mr == N:
        return N, None
    R, den, piv = DomainMatrix.from_list(D, ZZ).rref_den()
    rank = len(piv)
    if rank == N:
        return rank, None
    free = next(j for j in range(N) if j not in piv)
    R = R.to_list()
    v = [0] * N
    v[free] = int(den)
    for i, j in enumerate(piv):
        v[j] = -int(R[i][free])
    g = math.gcd(*v)
    v = [x // g for x in v]
    assert any(v) and all(sum(a * b for a, b in zip(row, v)) == 0 for row in D)
    return rank, v


def canonical(z, M):
    return min(tuple(sorted(fold(u * v, M) for v in z))
               for u in range(1, M) if math.gcd(u, M) == 1)


def generator_classes(M):
    units = [u for u in range(1, M) if math.gcd(u, M) == 1]
    if M == 1:
        yield (0, 0, 0)
        return
    seen = set()
    for z in it.combinations_with_replacement(range(M // 2 + 1), 3):
        if z in seen or math.gcd(M, *z) != 1:
            continue
        orbit = {tuple(sorted(fold(u * v, M) for v in z)) for u in units}
        seen.update(orbit)
        yield z


def invariant(M, z):
    torus = {tuple(k * v % M for v in z) for k in range(M)}
    return all(tuple((-pt[i] if i == j else pt[i]) % M for i in range(3)) in torus
               for pt in torus for j in range(3))


def metadata(command):
    return {'schema': 't8-cyclic-v1', 'command': command,
            'source_sha256': sha(__file__),
            'preregistration_sha256': sha(TOP / 'preregistration-T8.md'),
            'rules_sha': 'e5b64450fce42262dafc88ee357b72e5f203916b',
            'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                         'numpy': np.__version__},
            'status': 'MEASURED exact finite results; independent rerun required'}


def write_receipt(name, data):
    p = TOP / 'evidence' / name
    p.write_text(json.dumps(data, sort_keys=True, separators=(',', ':')) + '\n')
    assert p.stat().st_size < 16384
    print(json.dumps({'output': str(p), 'bytes': p.stat().st_size}), flush=True)


def controls():
    start = time.time()
    out = metadata('python topics/padua-3d-20261106/code/t8_cyclic.py controls')
    original = []
    for n, expected in [(2, 4), (3, 0), (4, 4)]:
        N = math.comb(n + 3, 3)
        M = 2 * N - 1
        dist = collections.Counter()
        for b, c in it.combinations(range(1, N), 2):
            r, _ = rank_null(dictionary(n, M, (1, b, c)))
            dist[r] += 1
        assert dist[N] == expected
        original.append({'n': n, 'M': M, 'rank_distribution': dict(dist)})
    cover = json.loads((TOP / 'evidence/t2-n3-null-cover.json').read_text())
    checked = set()
    ix = {a: j for j, a in enumerate(modes(3))}
    for b, c, _, terms in cover['witnesses']:
        v = [0] * 20
        for a, coeff in terms:
            v[ix[tuple(a)]] = coeff
        D = dictionary(3, 39, (1, b, c))
        assert any(v) and all(sum(x * y for x, y in zip(row, v)) == 0 for row in D)
        checked.add((b, c))
    assert checked == set(it.combinations(range(1, 20), 2))
    padua = []
    for n in range(1, 11):
        M = 2 * n * (n + 1)
        L, pts = nodes(M, (n + 1, n))
        grid = {(i * (n + 1), j * n) for i in range(n + 1)
                for j in range(n + 2) if (i + j) % 2 == 0}
        assert set(pts) == grid
        N = math.comb(n + 2, 2)
        assert len(pts) == N and mod_rank(dictionary(n, M, (n + 1, n))) == N
        padua.append({'n': n, 'M': M, 'nodes': len(pts), 'rank': N})
    # A bounded whole-subgroup reflection control, before the full census.
    inv = 0
    for M in range(1, 25):
        for z in generator_classes(M):
            if not invariant(M, z):
                continue
            inv += 1
            _, pts = nodes(M, z)
            for n in (2, 3):
                if len(pts) == math.comb(n + 3, 3):
                    assert rank_null(dictionary(n, M, z))[0] < len(pts)
    out.update({'original_T2': original, 'H39_checked': len(checked),
                'padua': padua, 'invariant_classes_M_le24': inv,
                'invariant_survivors': 0, 'verdict': 'PASS',
                'seconds': round(time.time() - start, 3)})
    write_receipt('t8-controls.json', out)


def census(n):
    assert n in (2, 3)
    start = time.time()
    N = math.comb(n + 3, 3)
    SCRATCH.mkdir(exist_ok=True)
    path = SCRATCH / f't8-unshifted-n{n}.jsonl'
    stats = collections.Counter()
    ranks = collections.Counter()
    distinct = {}
    full = []
    inv_count = 0
    with path.open('w') as fp:
        for M in range(1, 8 * N + 1):
            for z in generator_classes(M):
                stats['generator_classes'] += 1
                L, pts = nodes(M, z)
                row = {'M': M, 'z': z, 'nodes': len(pts)}
                if len(pts) != N:
                    row['disposition'] = 'wrong_count'
                    stats['wrong_count'] += 1
                else:
                    stats['correct_count_generators'] += 1
                    key = node_key(L, pts)
                    if key in distinct:
                        row['duplicate_of'] = distinct[key]
                        stats['duplicate_node_sets'] += 1
                    else:
                        distinct[key] = [M, z]
                        r, v = rank_null(dictionary(n, M, z))
                        inv = invariant(M, z)
                        inv_count += int(inv)
                        assert not (inv and r == N)
                        row.update({'rank': r, 'null': v, 'invariant': inv})
                        ranks[r] += 1
                        if r == N:
                            full.append([M, list(z)])
                fp.write(json.dumps(row, separators=(',', ':')) + '\n')
            if M % 20 == 0:
                print(json.dumps({'n': n, 'M': M, 'classes': stats['generator_classes'],
                                  'distinct_minimal': len(distinct), 'full': len(full)}), flush=True)
    out = metadata(f'python topics/padua-3d-20261106/code/t8_cyclic.py census --n {n}')
    out.update({'n': n, 'N': N, 'M_cap': 8 * N, 'counts': dict(stats),
                'distinct_node_sets': len(distinct), 'rank_distribution': dict(ranks),
                'fullrank_count': len(full), 'fullrank': full,
                'invariant_minimal_classes': inv_count, 'invariant_survivors': 0,
                'raw_path': str(path), 'raw_bytes': path.stat().st_size,
                'raw_sha256': sha(path), 'seconds': round(time.time() - start, 3)})
    write_receipt(f't8-unshifted-n{n}.json', out)


def odd(n):
    assert n in (5, 6)
    start = time.time()
    N = math.comb(n + 3, 3)
    M = 2 * N - 1
    SCRATCH.mkdir(exist_ok=True)
    path = SCRATCH / f't8-odd-n{n}.jsonl'
    seen = set()
    sets = set()
    dist = collections.Counter()
    full = []
    pairs = 0
    with path.open('w') as fp:
        for b, c in it.combinations(range(1, N), 2):
            pairs += 1
            z = (1, b, c)
            key = canonical(z, M)
            if key in seen:
                continue
            seen.add(key)
            L, pts = nodes(M, key)
            assert len(pts) == N
            nk = node_key(L, pts)
            if nk in sets:
                continue
            sets.add(nk)
            r, v = rank_null(dictionary(n, M, key))
            dist[r] += 1
            row = {'M': M, 'z': key, 'rank': r, 'null': v}
            fp.write(json.dumps(row, separators=(',', ':')) + '\n')
            if r == N:
                full.append(list(key))
    out = metadata(f'python topics/padua-3d-20261106/code/t8_cyclic.py odd --n {n}')
    out.update({'n': n, 'N': N, 'M': M, 'pairs': pairs,
                'unit_permutation_classes': len(seen), 'distinct_node_sets': len(sets),
                'rank_distribution': dict(dist), 'fullrank': full,
                'raw_path': str(path), 'raw_bytes': path.stat().st_size,
                'raw_sha256': sha(path), 'seconds': round(time.time() - start, 3)})
    write_receipt(f't8-odd-n{n}.json', out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['controls', 'census', 'odd'])
    parser.add_argument('--n', type=int)
    args = parser.parse_args()
    if args.command == 'controls':
        controls()
    else:
        assert json.loads((TOP / 'evidence/t8-controls.json').read_text())['verdict'] == 'PASS'
        (census if args.command == 'census' else odd)(args.n)


if __name__ == '__main__':
    main()
