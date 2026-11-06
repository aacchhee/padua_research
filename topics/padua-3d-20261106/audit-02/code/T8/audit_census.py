#!/usr/bin/env python3
"""Auditor's independent zero-phase cyclic census (Claude audit T8).

Does NOT import repository code.  For each order M<=8N enumerates EVERY sorted
individually-folded primitive triple (no unit-orbit reduction is used for coverage),
computes the exact cosine node set (folded residues -> reduced fractions), keeps the
N-node ones, and deduplicates exact node sets up to axis permutation.
Generator classes (unit x sign x permutation orbits) are counted twice: canonical
minimum and Burnside.  Rank of each distinct N-node set:
  lower bound: rank over F_p of the monomial evaluation matrix at the ACTUAL nodes,
               cos(2 pi r/M) -> (w^r + w^-r)/2 with w a verified primitive M-th root
               mod a prime p = 1 mod M (ring hom Z[zeta_M,1/2] -> F_p);
  upper bound: exact rational null space of the unfolded character matrix
               C[r][a] = #{s in {+-1}^3 : s.(a*z) = r mod M}; for v in ker C the
               polynomial p_v = sum v_a T_a satisfies 8 p_v(x_k) = g_v(zeta^k) with
               g_v == 0 identically, so p_v vanishes on every node.
  Exact rank is certified when the two bounds coincide.
"""
import itertools as it, math, sys, json, time
from fractions import Fraction
from collections import Counter
import numpy as np

def modes(n):
    return [a for a in it.product(range(n + 1), repeat=3) if sum(a) <= n]

def primes_1_mod(M, count=1, start=None):
    out = []; p = (start or M) + 1
    p += (-(p - 1)) % M
    while len(out) < count:
        if p > 2 and all(p % q for q in range(2, int(p ** 0.5) + 1)):
            out.append(p)
        p += M
    return out

def prim_root_of_unity(M, p):
    qs = [q for q in range(2, M + 1) if M % q == 0 and all(q % r for r in range(2, q))]
    for g in range(2, p):
        w = pow(g, (p - 1) // M, p)
        if pow(w, M, p) == 1 and all(pow(w, M // q, p) != 1 for q in qs):
            return w
    raise ValueError

def rank_mod_p(rows, p):
    A = [list(r) for r in rows]; rank = 0; ncol = len(A[0])
    for j in range(ncol):
        piv = next((i for i in range(rank, len(A)) if A[i][j] % p), None)
        if piv is None: continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = pow(A[rank][j], -1, p)
        A[rank] = [x * inv % p for x in A[rank]]
        for i in range(len(A)):
            if i != rank and A[i][j] % p:
                f = A[i][j]; A[i] = [(x - f * y) % p for x, y in zip(A[i], A[rank])]
        rank += 1
    return rank

def actual_node_rank(n, M, pts, p):
    """pts: folded integer residues (r1,r2,r3) with denominator M."""
    w = prim_root_of_unity(M, p); i2 = pow(2, -1, p)
    cosv = [(pow(w, r, p) + pow(w, (-r) % M, p)) * i2 % p for r in range(M)]
    A = [[cosv[a] ** e1 * cosv[b] ** e2 * cosv[c] ** e3 % p for (e1, e2, e3) in modes(n)]
         for (a, b, c) in pts]
    return rank_mod_p(A, p)

def nullspace_Q(C):
    """Exact RREF over Q; returns basis of {v : C v = 0} as integer vectors."""
    A = [[Fraction(x) for x in row] for row in C]; ncol = len(A[0]); piv = []; r = 0
    for j in range(ncol):
        k = next((i for i in range(r, len(A)) if A[i][j] != 0), None)
        if k is None: continue
        A[r], A[k] = A[k], A[r]
        pv = A[r][j]; A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][j] != 0:
                f = A[i][j]; A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(j); r += 1
    basis = []
    for free in (j for j in range(ncol) if j not in piv):
        v = [Fraction(0)] * ncol; v[free] = Fraction(1)
        for i, j in enumerate(piv): v[j] = -A[i][free]
        den = math.lcm(*[x.denominator for x in v]); vi = [int(x * den) for x in v]
        basis.append(vi)
    return basis

def character_matrix(n, M, z):
    ms = modes(n); C = [[0] * len(ms) for _ in range(M)]
    for j, a in enumerate(ms):
        for s in it.product((-1, 1), repeat=3):
            C[sum(si * ai * zi for si, ai, zi in zip(s, a, z)) % M][j] += 1
    return C

def verify_null(n, M, z, v):
    g = [0] * M
    for (a, c) in zip(modes(n), v):
        if c:
            for s in it.product((-1, 1), repeat=3):
                g[sum(si * ai * zi for si, ai, zi in zip(s, a, z)) % M] += c
    return any(v) and not any(g)

def triples(M):
    h = M // 2
    T = np.array(list(it.combinations_with_replacement(range(h + 1), 3)), dtype=np.int64)
    if M == 1:
        return T  # (0,0,0): the trivial group, order 1, primitive
    g = np.gcd(np.gcd(np.gcd(T[:, 0], T[:, 1]), T[:, 2]), M)
    return T[g == 1]

def fold(R, M):
    R = R % M
    return np.minimum(R, M - R) if M > 1 else R * 0

def encode_sorted(F, B):
    F = np.sort(F, axis=-1)
    return (F[..., 0] * B + F[..., 1]) * B + F[..., 2]

def class_counts(M, T):
    if M == 1: return 1, 1
    units = [u for u in range(1, M) if math.gcd(u, M) == 1]
    B = M // 2 + 1
    own = encode_sorted(T, B)
    canon = own.copy(); fix = 0
    for u in units:
        c = encode_sorted(fold(u * T, M), B)
        canon = np.minimum(canon, c); fix += int(np.sum(c == own))
    assert fix % len(units) == 0
    return len(np.unique(canon)), fix // len(units)

def node_counts(M, T, chunk=6000):
    B = M // 2 + 1; k = np.arange(M, dtype=np.int64)[:, None]
    out = np.empty(len(T), dtype=np.int64)
    for s in range(0, len(T), chunk):
        Z = T[s:s + chunk]
        code = (fold(k * Z[None, :, 0], M) * B + fold(k * Z[None, :, 1], M)) * B + fold(k * Z[None, :, 2], M)
        code.sort(axis=0)
        out[s:s + chunk] = 1 + np.count_nonzero(np.diff(code, axis=0), axis=0)
    return out

def node_set(M, z):
    return sorted({tuple(min(k * c % M, -k * c % M) for c in z) for k in range(M)})

def node_key(M, pts):
    fr = [tuple(Fraction(r, M) for r in pt) for pt in pts]
    return min(tuple(sorted(tuple(pt[i] for i in perm) for pt in fr))
               for perm in it.permutations(range(3)))

def subgroup_reflection_invariant(M, z):
    pts = {tuple(k * c % M for c in z) for k in range(M)}
    return all(tuple((-z[i] if i == j else z[i]) % M for i in range(3)) in pts for j in range(3))

def census(n):
    N = math.comb(n + 4 - 1, 3); cap = 8 * N; t0 = time.time()
    stats = Counter(); sets = {}; reps_by_key = {}
    for M in range(1, cap + 1):
        T = triples(M)
        stats['sorted_folded_primitive_triples'] += len(T)
        canon_cnt, burn_cnt = class_counts(M, T)
        assert canon_cnt == burn_cnt, (M, canon_cnt, burn_cnt)
        stats['generator_classes'] += canon_cnt
        cnt = node_counts(M, T)
        for z in T[cnt == N]:
            z = tuple(int(x) for x in z)
            pts = node_set(M, z); assert len(pts) == N
            key = node_key(M, pts)
            sets.setdefault(key, []).append((M, z))
        stats['N_node_triples'] += int(np.sum(cnt == N))
    # classes among N-node triples (unit orbits) per node set
    results = []; rankdist = Counter(); full = []; inv_classes = 0
    for key, reps in sets.items():
        Ms = sorted({M for M, _ in reps})
        orbit_codes = set()
        for M, z in reps:
            units = [u for u in range(1, M) if math.gcd(u, M) == 1] or [1]
            orbit_codes.add((M, min(tuple(sorted(min(u * c % M, -u * c % M) for c in z)) for u in units)))
        M, z = min(reps)
        pts = node_set(M, z)
        p = primes_1_mod(M, 1, start=10**6)[0]
        lo = actual_node_rank(n, M, pts, p)
        nb = nullspace_Q(character_matrix(n, M, z))
        assert all(verify_null(n, M, z, v) for v in nb)
        hi = N - len(nb)
        assert lo <= hi
        exact = lo == hi
        if not exact:  # second prime for the lower bound
            p2 = primes_1_mod(M, 1, start=2 * 10**6)[0]; lo = max(lo, actual_node_rank(n, M, pts, p2)); exact = lo == hi
        inv = [subgroup_reflection_invariant(Mm, zz) for Mm, zz in reps]
        inv_classes += sum(inv)
        rankdist[hi if exact else ('?', lo, hi)] += 1
        unit_free = all(all(math.gcd(c, Mm) != 1 for c in zz) for Mm, zz in reps)
        results.append(dict(M=M, z=z, orders=Ms, unit_orbits=len(orbit_codes), lo=lo, hi=hi,
                            invariant=any(inv), no_unit_coord=unit_free, even=M % 2 == 0))
        if hi == N and lo == N: full.append((M, z, p))
    out = dict(n=n, N=N, cap=cap, stats=dict(stats), distinct_node_sets=len(sets),
               unit_orbit_classes_with_N_nodes=sum(r['unit_orbits'] for r in results),
               sets_with_multiple_unit_orbits=sum(r['unit_orbits'] > 1 for r in results),
               rank_distribution={str(k): v for k, v in sorted(rankdist.items(), key=str)},
               all_ranks_exact=all(r['lo'] == r['hi'] for r in results),
               fullrank=full, invariant_classes=sum(r["invariant"] for r in results),
               invariant_fullrank=sum(r['invariant'] and r['lo'] == N for r in results),
               even_order_sets=sum(r['even'] for r in results),
               no_unit_coordinate_sets=sum(r['no_unit_coord'] for r in results),
               fullrank_details=[r for r in results if r['lo'] == N],
               seconds=round(time.time() - t0, 1))
    return out

if __name__ == '__main__':
    res = [census(int(a)) for a in sys.argv[1:]]
    print(json.dumps(res, indent=1, default=str))
