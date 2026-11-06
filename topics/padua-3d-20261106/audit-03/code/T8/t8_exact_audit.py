#!/usr/bin/env python3
"""Audit03 T8 independent exact checker (Claude, Opus 5.5 xhigh).

Written from scratch; imports nothing from the repository.  For rational
phased cyclic cosine orbits (and unions of cosets) it
  * builds exact torus angles as integers modulo L = lcm(M, D),
  * folds v -> min(v, L-v) (cos injective on [0, pi]) and counts distinct nodes,
  * chooses its own primes p = mL+1 in [1e9, 2^31) (own Miller-Rabin),
    an element w of exact order L (own factorisation), and
  * evaluates the MONOMIAL basis x^alpha, |alpha| <= n, at
    x_j = (w^v + w^-v)/2 mod p, then computes rank mod p by its own
    Gaussian elimination.
Ring hom Z[zeta_L, 1/2] -> F_p (zeta_L -> w; Phi_L(w)=0 since ord w = L and
p !| L) maps the actual-node monomial Vandermonde to this matrix; so a
modular rank r is a lower bound for the complex rank, and r = N on N
distinct nodes proves Pi_n-unisolvence.  Deficiency proves nothing.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np


def is_prime(n):
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for q in small:
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in small:
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


def prime_factors(L):
    out, q = [], 2
    while q * q <= L:
        if L % q == 0:
            out.append(q)
            while L % q == 0:
                L //= q
        q += 1
    if L > 1:
        out.append(L)
    return out


def primes_for(L, count=2, lo=10**9):
    """First `count` primes p = mL+1 >= lo (p < 2^31), each with an exact-order-L root."""
    res = []
    m = max(1, -(-lo // L))
    qs = prime_factors(L)
    while len(res) < count:
        p = m * L + 1
        m += 1
        if p >= 2**31:
            raise ValueError('prime too large for int64 elimination')
        if not is_prime(p):
            continue
        for g in range(2, 500):
            w = pow(g, (p - 1) // L, p)
            if pow(w, L, p) == 1 and all(pow(w, L // q, p) != 1 for q in qs):
                res.append((p, w))
                break
    return res


def exponents(n):
    return [(a, b, c) for a in range(n + 1) for b in range(n + 1 - a) for c in range(n + 1 - a - b)]


def nodes_exact(M, z, phase_rows, D):
    L = M * D // math.gcd(M, D)
    S = set()
    for a in phase_rows:
        for k in range(M):
            t = []
            for j in range(3):
                v = (k * z[j] * (L // M) + a[j] * (L // D)) % L
                t.append(min(v, L - v))
            S.add(tuple(t))
    return L, sorted(S)


def rank_mod_p(A, p):
    A = A.copy() % p
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c] != 0:
                piv = i
                break
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy()
        col[r] = 0
        nz = np.nonzero(col)[0]
        if len(nz):
            A[nz] = (A[nz] - (col[nz, None] * A[r][None, :]) % p) % p
        r += 1
        if r == rows:
            break
    return r


def modular_rank(n, L, nodes, p, w):
    inv2 = (p + 1) // 2
    E = exponents(n)
    X = np.zeros((len(nodes), 3), dtype=np.int64)
    for i, t in enumerate(nodes):
        for j in range(3):
            v = t[j]
            X[i, j] = (pow(w, v, p) + pow(w, (L - v) % L, p)) * inv2 % p
    pw = [np.ones((len(nodes), n + 1), dtype=np.int64) for _ in range(3)]
    for j in range(3):
        for e in range(1, n + 1):
            pw[j][:, e] = pw[j][:, e - 1] * X[:, j] % p
    V = np.empty((len(nodes), len(E)), dtype=np.int64)
    for col, (a, b, c) in enumerate(E):
        V[:, col] = pw[0][:, a] * pw[1][:, b] % p * pw[2][:, c] % p
    return rank_mod_p(V, p)


def certify(n, M, z, phase_rows, D, nprimes=2):
    N = math.comb(n + 3, 3)
    L, nodes = nodes_exact(M, z, phase_rows, D)
    out = {'n': n, 'M': M, 'z': list(z), 'D': D, 'L': L, 'distinct_nodes': len(nodes), 'N': N, 'checks': []}
    for p, w in primes_for(L, nprimes):
        assert (p - 1) % L == 0 and p % 2 == 1
        out['checks'].append({'p': p, 'w': w, 'rank': modular_rank(n, L, nodes, p, w)})
    out['unisolvent_certified'] = len(nodes) == N and all(c['rank'] == N for c in out['checks'])
    return out


# Phi1 witnesses transcribed from theory/t8-r06-measurements.md table (not from receipts)
PHI1 = [(1, (1, 2, 1), (105, 28, 211), 257), (3, (1, 2, 7), (30, 75, 69), 120),
        (4, (1, 22, 25), (240, 90, 109), 257), (5, (1, 8, 45), (225, 15, 115), 257),
        (7, (1, 33, 92), (29, 48, 56), 257), (8, (1, 37, 144), (59, 84, 55), 257),
        (9, (1, 32, 101), (97, 59, 127), 257), (11, (1, 16, 129), (156, 248, 227), 257),
        (12, (1, 267, 119), (132, 236, 237), 257)]
# Phi3b cubic M21 witness transcribed from attempts/T8-round06.md: z(1,4,6), (257,1028,10080)/10794
NEAR = (3, 21, (1, 4, 6), (257, 1028, 10080), 10794)


def main():
    ev = Path(sys.argv[1])  # authored evidence directory (read-only)
    out = {'phi1': [], 'near_m21': None, 'receipt_rows': []}
    for n, z, a, D in PHI1:
        N = math.comb(n + 3, 3)
        r = certify(n, N, z, [a], D)
        r['odd_coords'] = sum(t % 2 for t in z)
        out['phi1'].append(r)
        print('phi1', json.dumps(r), flush=True)
    n, M, z, a, D = NEAR
    out['near_m21'] = certify(n, M, z, [a], D)
    print('near', json.dumps(out['near_m21']), flush=True)
    # every certified / rank-reported row of the authored receipts
    for name in ['phi2', 'union2', 'union3', 'union4']:
        d = json.loads((ev / f't8-r06-{name}.json').read_text())
        for row in d['rows']:
            if 'phase_nums' not in row:
                continue
            ph = row['phase_nums']
            ph = ph if isinstance(ph[0], list) else [ph]
            r = certify(row['n'], row['M'], row['z'], ph, row['phase_den'])
            r.update(route=name, claimed=[c['rank'] for c in row['certificate']['checks']])
            out['receipt_rows'].append(r)
            print(name, json.dumps(r), flush=True)
    d = json.loads((ev / 't8-r06-phi3.json').read_text())
    for row in d['rows']:
        if 'z' not in row:
            continue
        r = certify(row['n'], row['M'], row['z'], [row['mask']], row['phase_den'])
        r.update(route='phi3-' + str(row['rule']), claimed=[c['rank'] for c in row['certificate']['checks']])
        out['receipt_rows'].append(r)
        print('phi3', json.dumps(r), flush=True)
    d = json.loads((ev / 't8-r06-strata.json').read_text())
    for row in d['rows']:
        for s in row['survivors']:
            r = certify(row['n'], row['M'], s['z'], [s['phase_nums']], s['phase_den'])
            r.update(route='strata', states=s['states'], claimed=[c['rank'] for c in s['certificate']['checks']])
            out['receipt_rows'].append(r)
            print('strata', json.dumps(r), flush=True)
    d = json.loads((ev / 't8-r06-near-orders.json').read_text())
    for row in d['rows']:
        if 'phase_nums' in row:
            r = certify(row['n'], row['M'], row['z'], [row['phase_nums']], row['phase_den'])
            r.update(route='near', claimed=[c['rank'] for c in row['certificate']['checks']])
            out['receipt_rows'].append(r)
            print('near-receipt', json.dumps(r), flush=True)
    Path(sys.argv[2]).write_text(json.dumps(out, indent=0))


if __name__ == '__main__':
    main()
