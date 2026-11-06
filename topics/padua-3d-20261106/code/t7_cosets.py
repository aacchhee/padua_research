#!/usr/bin/env python3
"""T7 exact character controls and bounded diagnostics; never an all-phase census.

Only this script's --output is written; inherited artifacts are read-only.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import shlex
import sys
import time
import sympy as s

TOP = Path(__file__).resolve().parents[1]
RULES = 'e5b64450fce42262dafc88ee357b72e5f203916b'


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def modes(n, d=3):
    return [a for a in it.product(range(n+1), repeat=d) if sum(a) <= n]


def dictionary(n, generators, modulus):
    """Integer zero-phase B, pairing global inverse character classes.

Generators are rational torus points with common denominator modulus.
A character is identified exactly by its values on these generators.
"""
    d = len(generators[0])
    cols = []
    for a in modes(n, d):
        col = Counter()
        for eps in it.product((-1, 1), repeat=d):
            key = tuple(sum(e*v*g for e, v, g in zip(eps, a, h)) % modulus
                        for h in generators)
            key = min(key, tuple((-v) % modulus for v in key))
            col[key] += 1
        cols.append(col)
    keys = sorted(set().union(*(set(c) for c in cols)))
    return [[c[k] for c in cols] for k in keys]


def rational_rank(rows):
    return s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix(rows)).convert_to(s.QQ).rank()


def rank_mod(rows, p):
    A = [[int(v) % p for v in row] for row in rows]
    r = 0
    for j in range(len(A[0])):
        k = next((k for k in range(r, len(A)) if A[k][j]), None)
        if k is None:
            continue
        A[r], A[k] = A[k], A[r]
        inv = pow(A[r][j], -1, p)
        A[r] = [v*inv % p for v in A[r]]
        for k in range(r+1, len(A)):
            c = A[k][j]
            if c:
                A[k] = [(x-c*y) % p for x, y in zip(A[k], A[r])]
        r += 1
        if r == len(A):
            break
    return r


def t2_control():
    reference = json.loads((TOP/'evidence/t2-generators.json').read_text())
    out = []
    for ref in reference['degrees']:
        n, N, M = ref['n'], ref['N'], ref['M']
        dist = Counter()
        for b, c in it.combinations(range(1, N), 2):
            D = dictionary(n, [(1, b, c)], M)
            r = rank_mod(D, 1000003)
            if r < N:
                r = rational_rank(D)
            dist[r] += 1
        require(dict(sorted(dist.items())) == {int(k): v for k, v in ref['rank_distribution'].items()}, 'T2 rank distribution mismatch')
        out.append({'n': n, 'cases': sum(dist.values()), 'ranks': dict(sorted(dist.items()))})
    cover = json.loads((TOP/'evidence/t2-n3-null-cover.json').read_text())
    checked = set()
    for b, c, _rank, witness in cover['witnesses']:
        a = modes(3)
        coeff = {tuple(u): v for u, v in witness}
        require(bool(coeff) and all(sum(u) <= 3 for u in coeff), 'bad H39 witness')
        D = dictionary(3, [(1, b, c)], 39)
        v = [coeff.get(u, 0) for u in a]
        require(all(sum(x*y for x, y in zip(row, v)) == 0 for row in D), 'H39 nonzero row')
        checked.add((b, c))
    require(checked == set(it.combinations(range(1, 20), 2)), 'H39 incomplete')
    return {'degrees': out, 'H39_exact_witnesses': len(checked)}


def padua_control():
    rows = []
    for n in range(1, 11):
        M = 2*n*(n+1)
        g = (n+1, n)
        X = {tuple(min((k*z) % M, (-k*z) % M) for z in g) for k in range(M)}
        D = dictionary(n, [g], M)
        rank = rational_rank(D)
        require(rank == len(X) == math.comb(n+2, 2), 'Padua mismatch')
        rows.append([n, len(X), rank])
    return rows


def invariant_control(n):
    """All six labelled T1 codes, every order <=2N and invariant phase."""
    N, hit, alive = math.comb(n+3, 3), 0, 0
    descriptions = [('product', (), [[()]]),
                    ('pair12', (0, 1), [[(0,0),(1,1)], [(0,1),(1,0)]]),
                    ('pair13', (0, 2), [[(0,0),(1,1)], [(0,1),(1,0)]]),
                    ('pair23', (1, 2), [[(0,0),(1,1)], [(0,1),(1,0)]]),
                    ('triple', (0,1,2), [[a for a in it.product((0,1), repeat=3) if sum(a)%2 == t] for t in (0,1)]),
                    ('plane', (0,1,2), [[a, tuple(1-v for v in a)] for a in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]])]
    for name, active, classes in descriptions:
        inactive = [j for j in range(3) if j not in active]
        ranges = [range(2, 2*N+1, 2) if j in active else range(1, 2*N+1) for j in range(3)]
        for m in it.product(*ranges):
            q = tuple(v//2 for v in m)
            for C in classes:
                coupled = sum(math.prod((q[j]+1)//2 if bit else q[j]//2+1 for j, bit in zip(active, pattern)) for pattern in C)
                for eps in it.product((0,1), repeat=len(inactive)):
                    projection = [q[j]+1 if j in active else None for j in range(3)]
                    for j, bit in zip(inactive, eps):
                        projection[j] = (m[j]+1)//2 if bit else m[j]//2+1
                    count = coupled*math.prod(projection[j] for j in inactive)
                    if count != N:
                        continue
                    hit += 1
                    alive += int(min(projection) > n and not (name == 'plane' and sum(v <= n for v in q) >= 2))
    require(alive == 0, 'T1 invariant survivor')
    require(hit == {2:636, 3:1392}[n], 'T1 full-class count mismatch')
    return {'n': n, 'projection_order_cap': 2*N, 'target_count_cosets': hit, 'screen_survivors': alive}


def fold(points):
    return {tuple(min(t % 1, (-t) % 1) for t in h) for h in points}


def rank2_example():
    H = sorted({(Q(i,4), Q(j,4), Q((i+j)%4,4)) for i, j in it.product(range(4), repeat=2)})
    F = sorted(fold(H))
    vals = {Q(0):1, Q(1,4):0, Q(1,2):-1}
    X = [tuple(vals[t] for t in row) for row in F]
    V = s.Matrix([[math.prod(x**a for x, a in zip(row, u)) for u in modes(2)] for row in X])
    weights = [Q(sum(tuple(min(t % 1, (-t) % 1) for t in h) == f for h in H),16) for f in F]
    invariant = [all(tuple(-v % 1 if k == j else v for k, v in enumerate(h)) in H for h in H) for j in range(3)]
    moments = {}
    for u in modes(3):
        average = sum(w*math.prod(x**a for x, a in zip(row, u)) for row, w in zip(X, weights))
        continuous = math.prod(Q(0) if a%2 else Q(math.comb(a,a//2),2**a) for a in u)
        if average != continuous:
            moments[str(u)] = [str(average), str(continuous)]
    require(abs(V.det()) == 256 and len(X) == 10 and not any(invariant), 'rank2 example mismatch')
    require(set(moments) == {'(1, 1, 1)'}, 'unexpected cubature defect')
    # Cubic P vanishes at every node but integral P=1/2. No weights can integrate it.
    require(all(x*x+y*y+z*z-2*x*y*z-1 == 0 for x,y,z in X), 'cubic relation mismatch')
    return {'H_order':16, 'nodes':X, 'monomial_det':int(V.det()), 'coordinate_reflections':invariant,
            'Haar_weights':[str(w) for w in weights], 'degree3_defects':moments,
            'integral_vanishing_cubic':'1/2', 'any_degree3_weights':'impossible by cubic'}


def lattice_counts(cap):
    by_order = {}
    for m in range(1, cap+1):
        # Row HNF diag(a,b,c), upper residues <b,<c,<c: b*c^2.
        by_order[m] = sum(b*c*c for a in range(1,m+1) if m%a == 0
                          for b in range(1,m//a+1) if m//a%b == 0
                          for c in [m//a//b])
    return {'cap':cap, 'all_subgroups':sum(by_order.values()),
            'order_target_count':by_order[cap//8],
            'formula':'sum_(a*b*c<=cap) b*c^2; labelled embedded subgroups, no symmetry quotient'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--controls-only', action='store_true')
    args = parser.parse_args()
    start = time.time()
    result = {'schema':'t7-general-coset-v1', 'rules_sha':RULES,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'command':shlex.join(['python', *sys.argv]),
              'versions':{'python':platform.python_version(), 'sympy':s.__version__},
              'status':'MEASURED finite exact diagnostics; written proofs are separate',
              'T2':t2_control(), 'Padua_n1_to_n10':padua_control(),
              'T1_full_invariant':[invariant_control(n) for n in (2,3)]}
    result['D0'] = 'PASS'
    if not args.controls_only:
        result['rank2_example'] = rank2_example()
        result['finite_reduction_cost'] = [lattice_counts(c) for c in (80,160)]
    result['seconds'] = round(time.time()-start,3)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    require(args.output.stat().st_size < 16384, 'receipt too large')
    print(json.dumps({'D0':result['D0'], 'output':str(args.output), 'seconds':result['seconds']}))

if __name__ == '__main__':
    main()
