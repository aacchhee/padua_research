#!/usr/bin/env python3
"""Audit03 T8 sanity checks of the analytic claims (Claude, Opus 5.5 xhigh).

These are finite consistency checks of proofs reconstructed by hand in the
audit report, never substitutes for them.
 (A) D_r(n) closed forms (trace of the sign action on Pi_n) by enumeration, n<=40.
 (B) parity of N = binom(n+3,3) by n mod 4, n<=400.
 (C) random M=N orbits with arbitrary rational phases at n=2,6,10 (the
     non-admissible degrees): modular rank never exceeds N-|D_t(n)|/2.
 (D) first-unit fold-count formula vs direct exact folding, for all
     M=3..40, all b,c, all t=2M a_1 in [0,2M), compatible/incompatible axes.
 (E) direct (formula-free) exact folding over the four Phi3b terminal
     count-obstruction orders and the s1 n3/n4/n5, s4 n3 permitted counts.
"""
import itertools as it
import json
import math
import random
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import t8_exact_audit as ex  # own code (this directory), not the repository


def D(r, n):
    return sum((-1) ** sum(al[:r]) for al in ex.exponents(n))


def closed(r, n):
    m, odd = divmod(n, 2)
    return {1: [(m + 1) ** 2, (m + 1) * (m + 2)], 2: [m + 1, 0],
            3: [(m + 1) ** 2, -(m + 1) * (m + 2)]}[r][odd]


def count_direct(M, z, a):
    """Distinct cosine nodes; a = 3 Fractions (turns)."""
    Dd = math.lcm(*(x.denominator for x in a))
    nums = [int(x * Dd) % Dd for x in a]
    return len(ex.nodes_exact(M, z, [nums], Dd)[1])


def predicted(M, z, t, J):
    h = t % 2
    d = math.gcd(M, *(z[j] for j in J)) if J else M
    q = M // d
    g = math.gcd(2, q)
    K = d * g if h % g == 0 else 0
    f = math.gcd(2, M) if h % math.gcd(2, M) == 0 else 0
    return M - (K - f) // 2


def main():
    out = {}
    # (A)
    out['A_trace_closed_forms_ok'] = all(D(r, n) == closed(r, n) for r in (1, 2, 3) for n in range(0, 41))
    out['A_zero_trace_cases_n1_40'] = sorted({(r, n) for r in (1, 2, 3) for n in range(1, 41) if D(r, n) == 0})[:6]
    out['A_zero_trace_iff_odd_n_r2'] = all((D(r, n) == 0) == (n % 2 == 1 and r == 2)
                                           for r in (1, 2, 3) for n in range(1, 41))
    # (B)
    out['B_N_odd_iff_n0mod4'] = all((math.comb(n + 3, 3) % 2 == 1) == (n % 4 == 0) for n in range(0, 401))
    out['B_permitted_le12'] = [n for n in range(1, 13) if not (n % 4 == 2)]
    # (C)
    rng = random.Random(20261106)
    rows = []
    for n, trials in [(2, 40), (6, 12), (10, 3)]:
        N = math.comb(n + 3, 3)
        for _ in range(trials):
            while True:
                z = [rng.randrange(N) for _ in range(3)]
                if math.gcd(N, *z) == 1:
                    break
            den = rng.choice([257, 263, 120, 2 * N, 4 * N])
            a = [rng.randrange(den) for _ in range(3)]
            L, nodes = ex.nodes_exact(N, z, [a], den)
            t = sum(v % 2 for v in z)
            bound = N - abs(D(t, n)) // 2 if len(nodes) == N else len(nodes)
            p, w = ex.primes_for(L, 1)[0]
            rk = ex.modular_rank(n, L, nodes, p, w)
            rows.append({'n': n, 'z': z, 'den': den, 'a': a, 'nodes': len(nodes), 't': t,
                         'bound': bound, 'modrank': rk})
    out['C_rows'] = len(rows)
    out['C_violations'] = [r for r in rows if r['modrank'] > r['bound'] or r['modrank'] >= math.comb(r['n'] + 3, 3)]
    out['C_tight'] = sum(r['modrank'] == r['bound'] for r in rows)
    out['C_full_count_rows'] = sum(r['nodes'] == math.comb(r['n'] + 3, 3) for r in rows)
    # (D) fold-count formula, brute force (integer phases, denominator 2M*257)
    def cnt(M, z, nums, Dd):
        return len(ex.nodes_exact(M, z, [nums], Dd)[1])
    bad, tested = [], 0
    for M in list(range(3, 19)) + [24, 30, 36, 42]:
        Dd = 2 * M * 257
        bcs = [(b, c) for b in range(M) for c in range(M)] if M < 19 else \
              [(rng.randrange(M), rng.randrange(M)) for _ in range(60)]
        for b, c in bcs:
            z = (1, b, c)
            for t in range(2 * M):
                for Jm in it.product((0, 1, 2), repeat=2):
                    nums = [t * 257]
                    J = []
                    for j, sflag in zip((1, 2), Jm):
                        base = t * z[j] * 257
                        nums.append((base + (M * 257 if sflag == 1 else 0) + (2 * M * (j + 1) if sflag == 2 else 0)) % Dd)
                        if sflag == 2:
                            J.append(j)
                    got = cnt(M, z, nums, Dd)
                    exp = predicted(M, z, t, J)
                    tested += 1
                    if got != exp:
                        bad.append((M, z, t, Jm, got, exp))
            nums = [(257 + 2 * M) % Dd, 0, 0]  # 2M a_1 = 1 + 2M/257 not integral
            tested += 1
            if cnt(M, z, nums, Dd) != M:
                bad.append((M, z, 'generic'))
    out['D_tested'] = tested
    out['D_mismatches'] = bad[:10]
    # (E) formula-free folding at Phi3b orders: which (t mod 2, J) patterns attain N
    E = {}
    for s, n in [(1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (3, 3), (4, 3), (4, 4)]:
        N = math.comb(n + 3, 3)
        M = N + s
        Dd = 2 * M * 257
        hits = total = 0
        hit_lt = 0
        for b in range(1, M):
            for c in range(1, M):
                z = (1, b, c)
                for t in (0, 1):
                    for Jm in [(2, 0), (0, 2), (2, 2)]:
                        nums = [t * 257]
                        for j, sflag in zip((1, 2), Jm):
                            nums.append((t * z[j] * 257 + (2 * M * (j + 1) if sflag == 2 else 0)) % Dd)
                        total += 1
                        ok = cnt(M, z, nums, Dd) == N
                        hits += ok
                        hit_lt += ok and b < c
        E[f's{s}_n{n}_M{M}'] = {'ordered_bc_all_1_to_M-1': total, 'count_equals_N': hits, 'b_lt_c_hits': hit_lt}
    out['E'] = E
    Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps({k: v for k, v in out.items() if k != 'C_rows'}, default=str)[:3000])


if __name__ == '__main__':
    main()
