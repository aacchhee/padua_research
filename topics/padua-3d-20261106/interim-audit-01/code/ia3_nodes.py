#!/usr/bin/env python3
"""Independent U3 actual-node certificates and fixed-witness boundary probes.

No producer/checker module imports. Exact nodes use direct generator powers;
trial-division primality and exact root-order checks certify new primes.
General-H coherent tests include folding, redundant generators and changed
row representatives. Mixed diagnostics examine existing fixed witnesses only.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
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
from scipy.linalg import null_space, svdvals

PIN = "5440555cf326afdbd66b75bed195802013901c2d"
TOP = Path(__file__).resolve().parents[2]


def serial(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def indices(n, d=3):
    # Same total-degree ordering as the registered measurements for d=3.
    if d == 1:
        return [(k,) for k in range(n+1)]
    return sorted((a for a in it.product(range(n+1), repeat=d) if sum(a) <= n),
                  key=lambda a: (sum(a), a))


def prime(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p)+1))


def factors(n):
    result, d = [], 2
    while d*d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d += 1
    return result+([n] if n > 1 else [])


def splitting(L, start):
    p = (start//L+1)*L+1
    while not prime(p):
        p += L
    for g in it.count(2):
        w = pow(g, (p-1)//L, p)
        if pow(w, L, p) == 1 and all(pow(w, L//q, p) != 1 for q in factors(L)):
            assert p < 100_000_000
            return p, w


def rank_mod(matrix, p):
    a = np.array(matrix, dtype=np.int64, copy=True) % p
    rank, det = 0, 1
    for col in range(a.shape[1]):
        candidates = np.flatnonzero(a[rank:, col])
        if not len(candidates):
            continue
        row = rank+int(candidates[0])
        if row != rank:
            a[[rank, row]] = a[[row, rank]]
            det = -det
        pivot = int(a[rank, col])
        det = det*pivot % p
        a[rank, col:] = a[rank, col:]*pow(pivot, -1, p) % p
        if rank+1 < len(a):
            a[rank+1:, col:] = (a[rank+1:, col:]-a[rank+1:, col, None]*a[rank, col:]) % p
        rank += 1
        if rank == min(a.shape):
            break
    return rank, det % p if rank == a.shape[0] == a.shape[1] else None


def exact_rank(rows):
    a = [[Q(v) for v in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        t = a[rank][col]
        a[rank] = [v/t for v in a[rank]]
        for r in range(rank+1, len(a)):
            if a[r][col]:
                t = a[r][col]
                a[r] = [x-t*y for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def finite_group(L, generators):
    d = len(generators[0])
    orders = [math.lcm(*(L//math.gcd(x, L) for x in g)) for g in generators]
    return {tuple(sum(k*g[j] for k, g in zip(ks, generators)) % L for j in range(d))
            for ks in it.product(*(range(o) for o in orders))}


def construct(components):
    L = math.lcm(*(q for c in components for v in [c['phase']]+c['generators'] for _, q in v))
    sets, groups = [], []
    for c in components:
        gens = [tuple(int(Q(*x)*L) for x in g) for g in c['generators']]
        phase = [int(Q(*x)*L) for x in c['phase']]
        group = finite_group(L, gens)
        folded = {tuple(min((x+t) % L, (-x-t) % L) for x, t in zip(h, phase)) for h in group}
        groups.append(group)
        sets.append(folded)
    return L, sets, groups


def monomials(n, L, nodes, p, w):
    modes = indices(n, len(nodes[0]))
    rows = []
    for angle in nodes:
        point = [(pow(w, t, p)+pow(w, -t % L, p))*pow(2, -1, p) % p for t in angle]
        rows.append([math.prod(pow(x, k, p) for x, k in zip(point, alpha)) % p for alpha in modes])
    return rows


def cheb(n, L, nodes):
    theta = np.array(nodes, dtype=float)*(2*np.pi/L)
    return np.column_stack([np.prod(np.cos(theta*np.array(alpha)), axis=1) for alpha in indices(n)])


def mesh(n, inverse, m):
    axis = np.linspace(0, np.pi, m)
    yz = np.array(list(it.product(axis, repeat=2)))
    best = 0.
    for x in axis:
        angles = np.column_stack((np.full(len(yz), x), yz))
        vals = np.column_stack([np.prod(np.cos(angles*np.array(a)), axis=1) for a in indices(n)])
        best = max(best, float(np.abs(vals@inverse).sum(axis=1).max()))
    return best


def selected(raw):
    path = TOP/'evidence/uc3-selected-inputs.json'
    inputs = json.loads(path.read_text())
    expected_path = TOP/'evidence/uc3-selected-check.json'
    expected = {r['id']: r for r in json.loads(expected_path.read_text())['rows']}
    summary, maxdelta, params = [], 0., {}
    for case in inputs['witnesses']:
        n, name = case['n'], case['id']
        N = math.comb(n+3, 3)
        L, pieces, groups = construct(case['components'])
        nodes = sorted(set.union(*pieces))
        assert len(nodes) == N
        if len(pieces) == 2:
            assert not pieces[0] & pieces[1]
            assert sorted(map(len, pieces)) == sorted([9, N-9])
        if L not in params:
            p, w = splitting(L, 20_000_000)
            params[L] = [(p, w), splitting(L, p)]
        certs = []
        for p, w in params[L]:
            rank, det = rank_mod(monomials(n, L, nodes, p, w), p)
            assert rank == N and det
            certs.append([p, w, rank, det])
        V = cheb(n, L, nodes)
        inverse = np.linalg.solve(V, np.eye(N))
        values = [mesh(n, inverse, m) for m in (21, 41)]
        for v, old in zip(values, expected[name]['qualities']):
            maxdelta = max(maxdelta, abs(v-old[1]))
        row = {'id': name, 'n': n, 'N': N, 'L': L, 'component_sizes': list(map(len, pieces)),
               'two_prime_certificates': certs, 'Lambda21_41': values,
               'residual_inf': float(np.linalg.norm(V@inverse-np.eye(N), np.inf))}
        if len(pieces) == 2:
            large = max(pieces, key=len)
            small = min(pieces, key=len)
            weights = np.array([2**(sum(k > 0 for k in alpha)/2) for alpha in indices(n)])
            A = cheb(n, L, sorted(large))*weights
            B = cheb(n, L, sorted(small))*weights
            full = np.vstack((A, B))
            sA, sV = svdvals(A), svdvals(full)
            Z = null_space(A)
            assert Z.shape == (N, 9)
            sBZ = svdvals(B@Z)
            assert sV[-1] <= sA[-1]*(1+1e-10)
            p, w = params[L][0]
            rankA, _ = rank_mod(monomials(n, L, sorted(large), p, w), p)
            rankB, _ = rank_mod(monomials(n, L, sorted(small), p, w), p)
            assert rankA == N-9 and rankB == 9
            row.update(large_component_exact_rank=rankA, small_component_exact_rank=rankB,
                       large_sigma_min=float(sA[-1]), union_sigma_min=float(sV[-1]),
                       repair_on_kernel_sigma_min=float(sBZ[-1]),
                       repair_on_kernel_condition=float(sBZ[0]/sBZ[-1]),
                       numerical_continuum_norm_lower_from_large=1/float(sA[-1]),
                       numerical_continuum_norm_lower_from_union=1/float(sV[-1]))
        raw.append({'row': row, 'node_numerators': nodes})
        summary.append(row)
        print(json.dumps({'selected': name, 'samples': values,
                          'sigmaA': row.get('large_sigma_min')}), flush=True)
    assert maxdelta < 1e-8
    return {'input': {'path': str(path), 'sha256': sha(path)},
            'comparison': {'path': str(expected_path), 'sha256': sha(expected_path)},
            'rows': summary, 'max_mesh_difference': maxdelta,
            'singular_value_caveat': 'Floating diagnostics, not interval certificates or universal family obstructions.'}


def general_phase(raw):
    # Explicit tiny groups, including redundant generators and noncyclic groups.
    definitions = [(6, [(2, 2)]), (6, [(2, 0), (0, 3)]),
                   (4, [(1, 1, 0), (0, 2, 2), (2, 2, 0)]),
                   (6, [(2, 0, 2), (0, 2, 2)]), (2, [(0, 0, 0)])]
    count, ranks, changed_refs = 0, Counter(), 0
    for L, generators in definitions:
        H = sorted(finite_group(L, generators))
        d = len(generators[0])
        for h in H:
            a = [Q(x, 2*L) for x in h]
            for degree in range(1, 5):
                modes = indices(degree, d)
                rows, refs = {}, {}
                for col, alpha in enumerate(modes):
                    for eps in it.product((-1, 1), repeat=d):
                        beta = tuple(x*y for x, y in zip(alpha, eps))
                        cl = tuple(sum(x*y for x, y in zip(beta, g)) % L for g in generators)
                        if cl not in rows:
                            rows[cl], refs[cl] = [0]*len(modes), beta
                        exponent = sum(2*x*(b-r) for x, b, r in zip(a, beta, refs[cl]))
                        assert exponent.denominator == 1
                        rows[cl][col] += -1 if int(exponent) % 2 else 1
                rankQ = exact_rank(list(rows.values()))
                # Change each representative by L*e0, which lies in H-perp.
                changed = []
                for cl, row in rows.items():
                    sign = -1 if int(2*a[0]*L) % 2 else 1
                    changed.append([sign*x for x in row])
                assert exact_rank(changed) == rankQ
                changed_refs += 1
                nodes = sorted({tuple(min((2*x+y) % (2*L), (-2*x-y) % (2*L))
                                      for x, y in zip(g, h)) for g in H})
                p, w = splitting(2*L, 30_000_000)
                rankp, _ = rank_mod(monomials(degree, 2*L, nodes, p, w), p)
                assert rankp == rankQ
                count += 1
                ranks[rankQ] += 1
                raw.append({'H_L': L, 'generators': generators, 'half_h': h,
                            'degree': degree, 'count': len(nodes), 'rankQ': rankQ, 'p': p, 'w': w})
    return {'coherent_cases': count, 'changed_representative_cases': changed_refs,
            'rank_histogram': dict(ranks),
            'outside_hypothesis': {'H': 'C3 in R/Z', 'a': '1/12', 'same_character_frequencies': [0, 3],
                                   'coefficient_ratio': 'exp(2pi*i*3/12)=i, not an integer sign',
                                   'twice_a_in_H': False}}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--receipt', required=True)
    args = p.parse_args()
    started = time.monotonic()
    source = Path(__file__).read_bytes()
    scratch = Path(tempfile.mkdtemp(prefix='padua-ia3-nodes-'))
    (scratch/Path(__file__).name).write_bytes(source)
    raw = []
    result = {'selected': selected(raw), 'general_phase': general_phase(raw)}
    output = scratch/'complete-checks.json'
    output.write_bytes(serial(raw)+b'\n')
    assert Path(__file__).read_bytes() == source
    receipt = {'pin': PIN, 'command': sys.argv, 'code_sha256': sha(__file__),
               'source_snapshot': str(scratch/Path(__file__).name),
               'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
               'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')},
               'raw': {'path': str(output), 'bytes': output.stat().st_size, 'sha256': sha(output),
                       'retention': 'local regenerate-only; no cold-storage delivery'},
               'result': result, 'seconds': time.monotonic()-started}
    data = serial(receipt)+b'\n'
    assert len(data) < 16384, len(data)
    Path(args.receipt).write_bytes(data)
    print(json.dumps({'receipt': args.receipt, 'bytes': len(data), 'seconds': receipt['seconds']}), flush=True)


if __name__ == '__main__':
    main()
