#!/usr/bin/env python3
"""Auditor (Claude) exact checks of the 36 listed n2 representatives.

* producer HNF rows (a,r,s),(0,b,t),(0,0,c) -> H by brute-force solving
  B x = 0 mod 1 over (1/m)Z^3 (no adjugate formula);
* actual-node Pi_2 rank in the MONOMIAL basis over F_p, p = 1 mod D, with
  primes different from the producer's (64577 / 1000003);
* all 381 order-19 subgroups as projective lines of F_19^3; exact rational
  rank of the actual-node matrix via an independent route: Gram matrix
  sum over the 19 torus points of products of cosines, written exactly as
  integers through character sums (no T7-01 dictionary code reused);
* node-set coincidences among the 36 representatives (torus negations,
  coordinate permutations).
"""
import itertools as it, json, math, sys
from fractions import Fraction
import numpy as np
import sympy as sp

MON = [v for v in it.product(range(3), repeat=3) if sum(v) <= 2]


def H_from_upper_hnf(h):
    a, b, c, r, s, t = h; m = a*b*c
    B = [(a, r, s), (0, b, t), (0, 0, c)]
    pts = [x for x in it.product(range(m), repeat=3)
           if all(sum(row[i]*x[i] for i in range(3)) % m == 0 for row in B)]
    assert len(pts) == m
    return m, pts


def splitting_prime(D, skip=()):
    k = 1
    while True:
        p = k*D+1
        if sp.isprime(p) and p not in skip and p > 3: return p
        k += 1


def rank_mod(A, p):
    A = [[x % p for x in row] for row in A]; r = 0
    for j in range(len(A[0])):
        piv = next((i for i in range(r, len(A)) if A[i][j]), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]; inv = pow(A[r][j], -1, p)
        A[r] = [v*inv % p for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][j]:
                f = A[i][j]; A[i] = [(x-f*y) % p for x, y in zip(A[i], A[r])]
        r += 1
    return r


def nodes(m, pts, D=None):
    """folded integer nodes with denominator m (phase 0)."""
    return sorted({tuple(min(x % m, (-x) % m) for x in q) for q in pts})


def actual_rank_mod(m, nd, skip=()):
    p = splitting_prime(m, skip)
    g = sp.primitive_root(p); w = pow(int(g), (p-1)//m, p)
    assert sp.n_order(w, p) == m
    inv2 = pow(2, -1, p)
    X = [[(pow(w, t, p)+pow(w, -t % m, p))*inv2 % p for t in q] for q in nd]
    A = [[math.prod(pow(x, e, p) for x, e in zip(row, al)) % p for al in MON] for row in X]
    return rank_mod(A, p), p


def exact_rank_cos(m, nd):
    """exact rank of actual-node monomial matrix over Q(zeta_m)^+ via sympy
    algebraic simplification of the 10x10 determinant (only used if square)."""
    xs = [[sp.cos(2*sp.pi*sp.Rational(t, m)) for t in q] for q in nd]
    A = sp.Matrix([[sp.prod([x**e for x, e in zip(row, al)]) for al in MON] for row in xs])
    return A


def main():
    cert = json.load(open(sys.argv[1]))
    out = {}
    reps = [(r['hnf'], 'nonprime') for r in cert['nonprime_survivors']] + [(h, 'p19') for h in cert['prime_survivors_HNF']]
    sets = []
    for h, kind in reps:
        m, pts = H_from_upper_hnf(h)
        nd = nodes(m, pts)
        assert len(nd) == 10, (h, len(nd))
        r1, p1 = actual_rank_mod(m, nd, skip=(64577, 1000003))
        r2, p2 = actual_rank_mod(m, nd, skip=(64577, 1000003, p1))
        sets.append((h, m, frozenset(pts), tuple(nd), r1, r2, p1, p2))
    out['all36_count10'] = True
    out['all36_actual_node_monomial_rank_modp'] = sorted({(s[4], s[5]) for s in sets})
    out['primes_used'] = sorted({(s[1], s[6], s[7]) for s in sets})
    # coincidences of node sets
    nsets = {}
    for s in sets: nsets.setdefault((s[1], s[3]), []).append(tuple(s[0]))
    out['distinct_node_sets_order16'] = sum(1 for k in nsets if k[0] == 16)
    out['distinct_node_sets_order19'] = sum(1 for k in nsets if k[0] == 19)
    def canon(m, nd):
        best = None
        for perm in it.permutations(range(3)):
            v = tuple(sorted(tuple(q[i] for i in perm) for q in nd))
            best = v if best is None or v < best else best
        return best
    out['distinct_node_sets_up_to_coordinate_permutation'] = {
        16: len({canon(16, k[1]) for k in nsets if k[0] == 16}),
        19: len({canon(19, k[1]) for k in nsets if k[0] == 19})}
    # also up to coordinate sign changes x_j -> -x_j (fold value t -> m/2 - t only when m even)
    # all 381 order-19 groups as lines; dictionary-free exact rank via Q-rank of integer Gram-like
    # matrix: rank of V over C equals rank of V V^* ; entries of the cosine matrix lie in Q(zeta19)^+;
    # use exact rank of the integer matrix W[t, alpha] = sum_eps zeta^(...) represented in the
    # power basis of Z[zeta19]: rank_C(V) = rank_Q(R) where R stacks the coordinate vectors? No --
    # instead compute rank over Q(zeta) exactly with sympy's AlgebraicField on 10x10 minors.
    from collections import Counter
    dist = Counter(); pos = []
    lines = set()
    for v in it.product(range(19), repeat=3):
        if not any(v): continue
        # normalise to first nonzero = 1
        i = next(j for j in range(3) if v[j]); inv = pow(v[i], -1, 19)
        lines.add(tuple(x*inv % 19 for x in v))
    assert len(lines) == 381
    zero_proj = 0
    for g in sorted(lines):
        if 0 in g: zero_proj += 1; continue
        pts = [tuple(t*x % 19 for x in g) for t in range(19)]
        nd = nodes(19, pts)
        assert len(nd) == 10
        r, p = actual_rank_mod(19, nd, skip=(1000003,))
        if r < 10:
            # exact characteristic-zero rank: numeric 60-digit SVD as corroboration and
            # rational rank of the trace-form matrix Tr(V^T V) entries (exact rationals).
            import mpmath as mp
            mp.mp.dps = 60
            Vm = mp.matrix(10, 10)
            for i, q in enumerate(nd):
                xs = [mp.cos(2*mp.pi*mp.mpf(t)/19) for t in q]
                for j, al in enumerate(MON):
                    Vm[i, j] = xs[0]**al[0]*xs[1]**al[1]*xs[2]**al[2]
            sv = mp.svd_r(Vm, compute_uv=False)
            svs = sorted([abs(sv[i]) for i in range(10)])
            numrank = sum(1 for s in svs if s > mp.mpf(10)**-40)
            # exact: Gram matrix G = V^T V has rational entries (Galois-invariant sums over the
            # full orbit are not available for 10 folded nodes) -> use the 19 torus points instead:
            # G19[a,b] = sum_t prod_j cos(2pi t g_j/19)^(a_j+b_j) is rational (sum over a full group).
            # rank(G19) = rank(V19) = rank(V) since rows of V19 repeat rows of V.
            Gq = sp.zeros(10, 10)
            for i, a in enumerate(MON):
                for j, b in enumerate(MON):
                    e = [a[k]+b[k] for k in range(3)]
                    # cos^e expansion: cos(x)^e = 2^-e sum_{l} C(e,l) e^{i(e-2l)x};
                    # sum over t of exp(2pi i t (sum_k g_k (e_k-2l_k))/19) = 19*[sum == 0 mod 19]
                    tot = Fraction(0)
                    for ls in it.product(*(range(ek+1) for ek in e)):
                        if sum(g[k]*(e[k]-2*ls[k]) for k in range(3)) % 19 == 0:
                            tot += math.prod(math.comb(e[k], ls[k]) for k in range(3))
                    Gq[i, j] = sp.Rational(tot.numerator*19, tot.denominator*2**sum(e))
            r_exact = Gq.rank()
            assert r_exact == numrank, (g, r_exact, numrank)
            r = r_exact
        dist[r] += 1
        if r == 10: pos.append(g)
    out['p19_lines'] = 381; out['p19_zero_projection'] = zero_proj
    out['p19_rank_distribution_exact'] = dict(sorted(dist.items()))
    # compare positive p19 lines with certificate groups
    cert19 = {frozenset(H_from_upper_hnf(h)[1]) for h in cert['prime_survivors_HNF']}
    mine19 = {frozenset(tuple(t*x % 19 for x in g) for t in range(19)) for g in pos}
    out['p19_positive_sets_equal_certificate'] = cert19 == mine19
    print(json.dumps(out, indent=1, default=str))
    return sets


if __name__ == '__main__':
    main()
