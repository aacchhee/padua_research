"""Auditor's exact M/R witness certification (own folding, own primes). No producer imports."""
import sys, json, math, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from alib import modes, rank_mod, split_prime, root_of_order, is_prime, trial_prime, factor

OUT = sys.argv[1]
MT = {3: (7, 16, 238, 145, 116), 4: (5, 12, 247, 17, 114), 5: (53, 60, 243, 55, 119),
      6: (41, 132, 146, 196, 223), 7: (98, 105, 223, 19, 200), 8: (82, 169, 49, 70, 42)}
RT = {3: (2, 4, 3, 4, 26, 211, 254), 4: (1, 2, 10, 11, 99, 151, 194), 5: (1, 3, 5, 30, 124, 71, 116),
      6: (1, 5, 11, 69, 82, 182, 212), 7: (2, 2, 8, 17, 20, 86, 131), 8: (2, 1, 42, 131, 73, 101, 145)}


def fold(angles, L):
    return {tuple(min(a % L, L - a % L) for a in t) for t in angles}


def m_nodes(n, key):
    N = len(modes(n)); q = N - 9; b, c, t1, t2, t3 = key
    assert 1 <= b < c < 2 * q and all(1 <= t <= 256 for t in (t1, t2, t3))
    L = math.lcm(4 * q, 771)
    A = fold([tuple((2 * k + 1) * g * (L // (4 * q)) for g in (1, b, c)) for k in range(2 * q)], L)
    Bc = fold([((u * 257 + 3 * t1) * (L // 771), (v * 257 + 3 * t2) * (L // 771), (((u + v) % 3) * 257 + 3 * t3) * (L // 771))
               for u in range(3) for v in range(3)], L)
    return L, A, Bc


def r_nodes(n, key):
    N = len(modes(n)); q = N - 9; r, s, b, c, t1, t2, t3 = key
    assert 1 <= b < c < q and all(1 <= t <= 256 for t in (t1, t2, t3))
    L = math.lcm(12, 257 * q)
    base = fold([((4 * u + (2 * v + 1)) * (L // 12), (2 * v + 1) * (L // 12), (4 * r * u + s * (2 * v + 1)) * (L // 12))
                 for u in range(3) for v in range(6)], L)
    cyc = fold([tuple((257 * k * g + q * t) * (L // (257 * q)) for g, t in zip((1, b, c), (t1, t2, t3))) for k in range(q)], L)
    return L, base, cyc


def r_base_counts():
    out = {}
    for r in (1, 2):
        for s in range(6):
            L = 12
            out[f'{r},{s}'] = len(fold([((4 * u + 2 * v + 1), (2 * v + 1), (4 * r * u + s * (2 * v + 1))) for u in range(3) for v in range(6)], L))
    return out


def cheb_rank(n, L, X, p):
    w = root_of_order(L, p); inv2 = (p + 1) // 2
    assert pow(w, L, p) == 1 and all(pow(w, L // f, p) != 1 for f in factor(L))
    P = np.array([[(pow(w, v, p) + pow(w, (L - v) % L, p)) * inv2 % p for v in x] for x in X], dtype=np.int64)
    tabs = []
    for j in range(3):
        T = np.ones((len(X), n + 1), dtype=np.int64)
        if n:
            T[:, 1] = P[:, j]
        for k in range(2, n + 1):
            T[:, k] = ((2 * P[:, j]) % p * T[:, k - 1] - T[:, k - 2]) % p
        tabs.append(T)
    A = np.array([tabs[0][:, a] * tabs[1][:, b] % p * tabs[2][:, c] % p for a, b, c in modes(n)]).T
    return rank_mod(A, p)


def main():
    res = {'R_base_counts': r_base_counts()}; t0 = time.time()
    for route, tab, fn in (('M', MT, m_nodes), ('R', RT, r_nodes)):
        for n in range(3, 9):
            N = len(modes(n)); L, A, Bc = fn(n, tab[n]); U = A | Bc
            p1 = split_prime(L, 1_750_000_000); p2 = split_prime(L, 2_050_000_000)
            assert p1 != p2 and trial_prime(p1) and trial_prime(p2)
            r1, d1 = cheb_rank(n, L, sorted(U), p1); r2, d2 = cheb_rank(n, L, sorted(U), p2)
            # 257 disjointness: does any first-angle of one component equal (up to fold) one of the other?
            fa = {x[0] for x in A}; fb = {x[0] for x in Bc}
            res[f'{route}{n}'] = {'N': N, 'L': L, 'sizes': [len(A), len(Bc)], 'intersection': len(A & Bc),
                                  'first_axis_overlap': len(fa & fb), 'union': len(U), 'primes': [p1, p2],
                                  'ranks': [r1, r2], 'dets_nonzero': [d1 != 0, d2 != 0],
                                  'full_rank': len(U) == N and r1 == r2 == N and d1 != 0 and d2 != 0}
            print(route, n, res[f'{route}{n}'], round(time.time() - t0, 1), flush=True)
    # 257 does not divide 12q for the six q
    res['257_divides_12q'] = {n: (12 * (len(modes(n)) - 9)) % 257 == 0 for n in range(3, 9)}
    json.dump(res, open(OUT, 'w'), indent=1)
    print(res['R_base_counts'], res['257_divides_12q'])


if __name__ == '__main__':
    main()
