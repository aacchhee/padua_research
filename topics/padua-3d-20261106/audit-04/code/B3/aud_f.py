"""Auditor's independent U3-F folded rank-two census (no producer/checker imports).
For every registered parameter: exact folded count; for every exact-N case (not only the
460 left after trace/axis kills): exact Q-rank of the rephased integer dictionary
(rows normalised by an independently chosen reference), actual-node modular rank at
an auditor prime (lower bound) and floating SVD rank (non-rigorous corroboration).
Also recomputes the producer's axis/trace predicates and checks their soundness
against the exact rank."""
import sys, json, math, time
from collections import Counter
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from alib import modes, sparse_gcd_rank, rank_mod, split_prime, root_of_order

OUT = sys.argv[1]
SIG = [(s1, s2, s3) for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]


def nodes(a, b, r, s, e1, e2):
    L = 2 * b  # common denominator: a|b
    h1 = (L // a, 0, (L // a) * r); h2 = (L // b, L // b, (L // b) * s)
    ph = (e1 * h1[0] // 2 + e2 * h2[0] // 2, e2 * h2[1] // 2, e1 * h1[2] // 2 + e2 * h2[2] // 2)
    # h1/2 has numerators b/a*(1,0,r): integer since a|b; h2/2 = (1,1,s)
    assert all(2 * p == e1 * x + e2 * y for p, x, y in zip(ph, h1, h2))
    X = set()
    for u in range(a):
        for v in range(b):
            ang = [(ph[j] + u * h1[j] + v * h2[j]) % L for j in range(3)]
            X.add(tuple(min(t, L - t) for t in ang))
    return L, sorted(X)


def dictionary(n, a, b, r, s, e1, e2):
    L = 2 * b
    ph = (e1 * (b // a) + e2, e2, e1 * (b // a) * r + e2 * s)  # phase numerators over 2b
    mo = modes(n); N = len(mo); rows = {}; ref = {}
    for j, al in enumerate(mo):
        for eps in SIG:
            be = [x * y for x, y in zip(al, eps)]
            f1 = be[0] + r * be[2]; f2 = be[0] + be[1] + s * be[2]
            cl = (f1 % a, f2 % b)
            t = sum(x * y for x, y in zip(be, ph))  # 2b * beta.phase
            # reference: the LARGEST t seen first is not needed; use first-seen but
            # verify the integrality claim t - t_ref in b*Z for every member.
            if cl not in ref:
                ref[cl] = t; rows[cl] = [0] * N
            d = t - ref[cl]
            assert d % b == 0, 'phase ratio not +-1'
            rows[cl][j] += -1 if (d // b) % 2 else 1
    out = set()
    for row in rows.values():
        nz = [x for x in row if x]
        if not nz:
            continue
        g = 0
        for x in nz:
            g = math.gcd(g, x)
        if nz[0] < 0:
            g = -g
        out.add(tuple(x // g for x in row))
    return tuple(sorted(out))


def cheb_tab(xs, n, p):
    T = np.ones((len(xs), n + 1), dtype=np.int64)
    if n:
        T[:, 1] = xs
    for k in range(2, n + 1):
        T[:, k] = (2 * xs * T[:, k - 1] - T[:, k - 2]) % p
    return T


def node_rank_mod(n, L, X, p):
    w = root_of_order(L, p); inv2 = (p + 1) // 2
    P = np.array([[(pow(w, v, p) + pow(w, (L - v) % L, p)) * inv2 % p for v in x] for x in X], dtype=np.int64)
    tabs = [cheb_tab(P[:, j], n, p) for j in range(3)]
    A = np.array([tabs[0][:, a] * tabs[1][:, b] % p * tabs[2][:, c] % p for a, b, c in modes(n)]).T
    return rank_mod(A, p)


def float_rank(n, L, X):
    TH = 2 * np.pi * np.array(X, dtype=float) / L
    mo = np.array(modes(n))
    V = np.cos(TH[:, None, 0] * mo[None, :, 0]) * np.cos(TH[:, None, 1] * mo[None, :, 1]) * np.cos(TH[:, None, 2] * mo[None, :, 2])
    sv = np.linalg.svd(V, compute_uv=False)
    return int(np.sum(sv > 1e-9 * sv[0])), float(sv[-1] / sv[0])


_PR = {}
def sp_cached(L, start):
    if (L, start) not in _PR:
        _PR[(L, start)] = split_prime(L, start)
    return _PR[(L, start)]


def trace_poly(n, e):
    return sum((-1) ** sum(x * y for x, y in zip(al, e)) for al in modes(n))


def main():
    t0 = time.time(); res = {}; cache = {}; pos = []; disagree = []
    for n in range(3, 9):
        N = len(modes(n)); hist = Counter(); rk = Counter(); total = 0; types = []
        kill_unsound = 0; producer_like_remaining = 0; rank_on_remaining = Counter(); flt_mismatch = 0
        for M in (2 * N, 2 * N - 4):
            for a in range(2, M + 1):
                if M % a or (M // a) % a:
                    continue
                b = M // a; types.append((M, a, b))
                for r in range(a):
                    for s in range(b):
                        for pid, (e1, e2) in enumerate(((0, 0), (1, 0), (0, 1), (1, 1))):
                            total += 1
                            L, X = nodes(a, b, r, s, e1, e2)
                            if len(X) != N:
                                hist['wrong-count'] += 1; continue
                            hist['exact-N'] += 1
                            D = dictionary(n, a, b, r, s, e1, e2)
                            if D not in cache:
                                cache[D] = sparse_gcd_rank(D)
                            R = cache[D]; rk[R] += 1
                            # analytic predicates (auditor's own recomputation)
                            axes = [len({x[j] for x in X}) for j in range(3)]
                            axis_kill = min(axes) <= n
                            tr_kill = False
                            for (k, l) in ((a // 2 if a % 2 == 0 else None, 0), (0, b // 2 if b % 2 == 0 else None),
                                           (a // 2 if a % 2 == 0 else None, b // 2 if b % 2 == 0 else None)):
                                if k is None or l is None or (k == 0 and l == 0):
                                    continue
                                hv = [(k * (L // a) * c1 + l * (L // b) * c2) % L for c1, c2 in ((1, 1), (0, 1), (r, s))]
                                if all(x == 0 for x in hv):
                                    continue
                                assert all(x in (0, L // 2) for x in hv)
                                e = [1 if x == L // 2 else 0 for x in hv]
                                fixed = sum(all((not e[j]) or 4 * x[j] == L for j in range(3)) for x in X)
                                if fixed != trace_poly(n, e):
                                    tr_kill = True
                            if (axis_kill or tr_kill) and R == N:
                                kill_unsound += 1
                            if not (axis_kill or tr_kill):
                                producer_like_remaining += 1; rank_on_remaining[R] += 1
                            if R == N:
                                p1 = sp_cached(L, 1_700_000_000); p2 = sp_cached(L, 2_000_000_000)
                                r1, d1 = node_rank_mod(n, L, X, p1); r2, d2 = node_rank_mod(n, L, X, p2)
                                pos.append({'n': n, 'key': [M, a, b, r, s, pid], 'L': L, 'nodes': X, 'ranks': [r1, r2],
                                            'primes': [p1, p2], 'dets': [d1, d2]})
                            # lower-bound/non-rigorous cross-checks for every exact-N case
                            p0 = sp_cached(L, 1_500_000_000)
                            rm, _ = node_rank_mod(n, L, X, p0)
                            if rm > R:
                                disagree.append(('modular>exact', n, M, a, b, r, s, pid, rm, R))
                            fr, _ = float_rank(n, L, X)
                            if fr != R:
                                flt_mismatch += 1
        res[n] = {'N': N, 'types': types, 'parameters': total, 'hist': dict(hist), 'exact_rank_hist_allN': dict(rk),
                  'remaining_after_axis_trace': producer_like_remaining,
                  'rank_hist_on_remaining': dict(rank_on_remaining), 'kills_contradicted_by_exact_rank': kill_unsound,
                  'float_rank_mismatch': flt_mismatch, 'seconds': time.time() - t0}
        print(n, res[n], flush=True)
    res['positives'] = pos; res['modular_exceeds_exact'] = disagree; res['distinct_dictionaries'] = len(cache)
    if len(pos) == 2:
        res['positives_same_nodes'] = pos[0]['nodes'] == pos[1]['nodes'] and pos[0]['L'] == pos[1]['L']
    json.dump(res, open(OUT, 'w'))
    print('positives', [(p['n'], p['key'], p['ranks'], p['primes']) for p in pos], 'same', res.get('positives_same_nodes'),
          'disagree', disagree, 'distinct dict', len(cache), time.time() - t0)


if __name__ == '__main__':
    main()
