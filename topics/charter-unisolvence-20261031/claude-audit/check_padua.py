"""Claude audit-01 independent checker for PD-T004..PD-T008, PD-T010, PD-T012 support.

Written from the theorem statements only; imports no developer/source module.
All finite-field arithmetic is exact (gf.py). The char-0 Dickson determinant
check uses mpmath at high precision and is a MEASURED cross-check only.
Usage: python3 check_padua.py OUTPUT.json
"""
import hashlib
import itertools
import json
import os
import platform
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gf import GF

import numpy as np


def factor_pk(q):
    for p in range(2, q + 1):
        if q % p == 0:
            k = 0
            while q % p == 0:
                q //= p
                k += 1
            return p, k


def T(F, r, t):
    # Chebyshev T_r at t via recurrence, exact
    if r == 0:
        return F.one
    a, b = F.one, t
    two = 2 % F.p
    for _ in range(r - 1):
        a, b = b, F.sub(F.mul(F.mul(two, t), b), a)
    return b


def element_of_order(F, L):
    assert (F.q - 1) % L == 0
    return F.exp[(F.q - 1) // L]  # exp[1] is a generator, so exp[(q-1)/L] has exact order L


def padua_nodes(F, n):
    inv2 = F.inv(2 % F.p)
    z = element_of_order(F, 2 * n)
    h = element_of_order(F, 2 * (n + 1))
    xs = [F.mul(inv2, F.add(F.pow(z, j), F.inv(F.pow(z, j)))) for j in range(n + 1)]
    ys = [F.mul(inv2, F.add(F.pow(h, k), F.inv(F.pow(h, k)))) for k in range(n + 2)]
    S = [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    return xs, ys, S


def in_subfield(F, x, q):
    return F.pow(x, q) == x


def chk_padua_field(q, n, out, gram_limit=10):
    p, kq = factor_pk(q)
    F = GF(p, 2 * kq)  # F_{q^2}; F_q is the subfield fixed by x->x^q
    rec = {'q': q, 'n': n}
    good = (2 * n * (n + 1)) % p != 0
    rec['good_char'] = good
    if not good or (q * q - 1) % (2 * n) or (q * q - 1) % (2 * n + 2):
        return None
    xs, ys, S = padua_nodes(F, n)
    N = (n + 1) * (n + 2) // 2
    cong = ((q - 1) % (2 * n) == 0 or (q + 1) % (2 * n) == 0) and \
           ((q - 1) % (2 * n + 2) == 0 or (q + 1) % (2 * n + 2) == 0)
    rational = all(in_subfield(F, x, q) for x in xs) and all(in_subfield(F, y, q) for y in ys)
    assert rational == cong, ('PD-T005 rationality iff failed', q, n)
    rec['rational'] = rational
    # PD-T005 residue table
    if rational:
        M = 2 * n * (n + 1)
        sx = '+' if (q - 1) % (2 * n) == 0 else '-'
        sy = '+' if (q - 1) % (2 * n + 2) == 0 else '-'
        table = {('+', '+'): 1, ('+', '-'): 2 * n + 1, ('-', '+'): 2 * n * n - 1, ('-', '-'): M - 1}
        if n >= 2:
            assert q % M == table[(sx, sy)] % M, 'PD-T005 residue table'
        else:
            # n=1: x sign ambiguous; q mod 4 determined by y sign only
            assert q % 4 in (1, 3)
            ok = any(q % M == table[(s, sy)] % M for s in '+-')
            assert ok
        assert q >= 2 * n + 1
        rec['signs'] = sx + sy
    # distinctness & count (over E = F_{q^2} subfield generated)
    assert len(set(xs)) == n + 1 and len(set(ys)) == n + 2 and len(S) == N
    # moment identity (PD-T004)
    inv = F.inv
    nn1 = (n * (n + 1)) % p
    def ehalf(i, mm):
        return F.inv(2 % p) if i in (0, mm) else F.one
    w = {}
    for (j, k) in S:
        w[(j, k)] = F.div(F.mul(2 % p, F.mul(ehalf(j, n), ehalf(k, n + 1))), nn1)
    Tx = {(a, j): T(F, a, xs[j]) for a in range(2 * n + 2) for j in range(n + 1)}
    Ty = {(b, k): T(F, b, ys[k]) for b in range(2 * n + 2) for k in range(n + 2)}
    for a in range(2 * n + 2 if n <= 12 else 0):
        for b in range(2 * n + 2 - a):
            s = 0
            for (j, k) in S:
                s = F.add(s, F.mul(w[(j, k)], F.mul(Tx[(a, j)], Ty[(b, k)])))
            expect = F.one if (a, b) in ((0, 0), (2 * n, 0), (n, n + 1)) else 0
            assert s == expect, ('PD-T004 moment', q, n, a, b)
    rec['moments_checked'] = n <= 12
    if n <= gram_limit:
        cols = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
        V = [[F.mul(Tx[(a, j)], Ty[(b, k)]) for (a, b) in cols] for (j, k) in S]
        half = F.inv(2 % p)
        for c1, (a, b) in enumerate(cols):
            for c2, (c, d) in enumerate(cols):
                s = 0
                for r, (j, k) in enumerate(S):
                    s = F.add(s, F.mul(w[(j, k)], F.mul(V[r][c1], V[r][c2])))
                if c1 != c2:
                    exp_ = 0
                elif (a, b) == (n, 0):
                    exp_ = F.one
                else:
                    exp_ = F.mul(half if a > 0 else F.one, half if b > 0 else F.one)
                assert s == exp_, ('PD-T004 Gram', q, n, (a, b), (c, d))
        rec['gram_checked'] = True
        # PD-T006: Dickson monomial det^2
        two = 2 % p
        A = [[F.mul(F.pow(F.mul(two, xs[j]), a), F.pow(F.mul(two, ys[k]), b)) for (a, b) in cols] for (j, k) in S]
        dA = F.det(A)
        e2 = (n * n + 3 * n + 6)
        assert e2 % 2 == 0
        pred = F.mul(F.pow(two, e2 // 2), F.pow(nn1, N))
        assert F.mul(dA, dA) == pred and dA != 0, ('PD-T006', q, n)
        rec['dickson_det_checked'] = True
    out.append(rec)
    return F, xs, ys, S, w


def chk_bad_reduction(p, n, out):
    """Reduce canonical integral Dickson coordinates at a prime above p | 2n(n+1): det must vanish."""
    L = 2 * n * (n + 1)  # lcm(2n, 2n+2)
    rL = L
    while rL % p == 0:
        rL //= p
    k = 1
    while (p ** k - 1) % rL:
        k += 1
    if p ** k > 4096:
        return
    F = GF(p, k)
    zL = element_of_order(F, rL)  # image of a primitive L-th root: a primitive rL-th root
    z = F.pow(zL, L // (2 * n))
    h = F.pow(zL, L // (2 * n + 2))
    X = [F.add(F.pow(z, j), F.inv(F.pow(z, j))) for j in range(n + 1)]
    Y = [F.add(F.pow(h, kk), F.inv(F.pow(h, kk))) for kk in range(n + 2)]
    S = [(j, kk) for j in range(n + 1) for kk in range(n + 2) if (j + kk) % 2 == 0]
    cols = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    A = [[F.mul(F.pow(X[j], a), F.pow(Y[kk], b)) for (a, b) in cols] for (j, kk) in S]
    d = F.det(A)
    assert d == 0, ('PD-T006 bad reduction nonsingular', p, n)
    out.append({'p': p, 'n': n, 'field': repr(F), 'det': 0})


def chi(Fq_elems_pow, x):
    return Fq_elems_pow(x)


def chk_quadratic(q, out):
    n = (q - 1) // 2
    p, kq = factor_pk(q)
    res = chk_padua_field(q, n, [], gram_limit=6)
    assert res is not None
    F, xs, ys, S, _ = res
    Fq = [x for x in range(F.q) if in_subfield(F, x, q)]
    assert len(Fq) == q
    e = (q - 1) // 2
    one, m1 = F.one, F.neg(F.one)
    def ch(x):
        if x == 0:
            return 0
        v = F.pow(x, e)
        return 1 if v == one else -1
    two = 2 % p
    Xs = [x for x in Fq if ch(F.sub(F.mul(x, x), one)) != -1]
    Ys = [y for y in Fq if ch(F.sub(F.mul(y, y), one)) != 1]
    assert set(Xs) | set(Ys) == set(Fq) and set(Xs) & set(Ys) == {one, m1}
    assert len(Xs) == n + 1 and len(Ys) == n + 2
    def eps(x):
        return ch(m1) if x == m1 else ch(F.mul(two, F.add(x, one)))
    def dlt(y):
        return -ch(m1) if y == m1 else ch(F.mul(two, F.add(y, one)))
    desc = {(x, y) for x in Xs for y in Ys if eps(x) == dlt(y)}
    canon = {(xs[j], ys[k]) for (j, k) in S}
    assert desc == canon, ('PD-T007 description', q)
    assert len(canon) * 8 == (q + 1) * (q + 3)
    for (x, y) in canon:
        if x != m1 and y != m1:
            assert ch(F.mul(F.add(x, one), F.add(y, one))) == 1
    out.append({'q': q, 'n': n, 'points': len(canon), 'description_equal': True})


def code_checks(q, n, out, dist_max_msgs=3_000_000):
    """PD-T008 dual + lower bound; exact min distance by full enumeration when feasible."""
    tmp = []
    res = chk_padua_field(q, n, tmp, gram_limit=n)
    assert tmp and tmp[0]['rational'], ('code check needs rational Padua set', q, n)
    F, xs, ys, S, w = res
    p, kq = factor_pk(q)
    # Map F_q subfield elements to compact indices for numpy tables
    Fq = [x for x in range(F.q) if in_subfield(F, x, q)]
    idx = {x: i for i, x in enumerate(Fq)}
    addT = np.array([[idx[F.add(a, b)] for b in Fq] for a in Fq], dtype=np.int64)
    mulT = np.array([[idx[F.mul(a, b)] for b in Fq] for a in Fq], dtype=np.int64)
    zero_i = idx[0]
    N = len(S)
    cols_all = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    Vcheb = [[F.mul(T(F, a, xs[j]), T(F, b, ys[k])) for (a, b) in cols_all] for (j, k) in S]
    recs = []
    for kdeg in range(0, n + 1):
        lo = [c for c, (a, b) in enumerate(cols_all) if a + b <= kdeg]
        hi = [c for c, (a, b) in enumerate(cols_all) if a + b > kdeg]
        mons = [(a, d - a) for d in range(kdeg + 1) for a in range(d, -1, -1)]
        G = [[F.mul(F.pow(xs[j], a), F.pow(ys[k], b)) for (j, k) in S] for (a, b) in mons]
        K = len(mons)
        assert F.rank(G) == K
        # dual: W * Cheb columns of degree > k are orthogonal to C_k and span N-K
        D = [[F.mul(w[S[r]], Vcheb[r][c]) for r in range(N)] for c in hi]
        for drow in D:
            for g in G:
                s = 0
                for a_, b_ in zip(drow, g):
                    s = F.add(s, F.mul(a_, b_))
                assert s == 0, 'PD-T008 dual orthogonality'
        if hi:
            assert F.rank(D) == N - K
        lb = (n - kdeg + 1) * (n - kdeg + 2) // 2
        rec = {'q': q, 'n': n, 'k': kdeg, 'N': N, 'K': K, 'lower_bound': lb}
        if q ** K <= dist_max_msgs and K >= 1:
            Gi = np.array([[idx[v] for v in row] for row in G], dtype=np.int64)
            best = N + 1
            total = 0
            # enumerate messages with last nonzero coefficient equal to 1 (projective reps)
            one_i = idx[F.one]
            for last in range(K):
                free = last
                chunk_iter = itertools.product(range(q), repeat=free)
                # vectorize: build all messages for coords 0..last-1
                if free:
                    msgs = np.array(list(chunk_iter), dtype=np.int64).reshape(-1, free)
                else:
                    msgs = np.zeros((1, 0), dtype=np.int64)
                cw = np.broadcast_to(Gi[last], (msgs.shape[0], N)).copy()  # coefficient 1 on 'last'
                for c in range(free):
                    cw = addT[cw, mulT[msgs[:, c][:, None], Gi[c][None, :]]]
                wt = (cw != zero_i).sum(axis=1)
                best = min(best, int(wt.min()))
                total += msgs.shape[0]
            assert total == (q ** K - 1) // (q - 1)
            assert best >= lb, 'PD-T008 lower bound violated'
            rec['min_distance'] = best
            rec['projective_messages'] = total
        recs.append(rec)
    out.extend(recs)


def max_arc_pg2(q):
    # points of PG(2,q) for prime q, normalized
    pts = []
    for x in range(q):
        for y in range(q):
            pts.append((1, x, y))
    for y in range(q):
        pts.append((0, 1, y))
    pts.append((0, 0, 1))
    def coll(a, b, c):
        d = (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0])) % q
        return d == 0
    P = len(pts)
    best = [0]
    # symmetry: PGL(3,q) is transitive on ordered 4-arcs (frames); fix first four points
    frame = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]
    def norm(v):
        v = [c % q for c in v]
        for c in v:
            if c:
                inv = pow(c, q - 2, q)
                return tuple((t * inv) % q for t in v)
    pindex = {norm(pt): i for i, pt in enumerate(pts)}
    fixed = [pindex[norm(f)] for f in frame]
    def extend(arc, start):
        best[0] = max(best[0], len(arc))
        for i in range(start, P):
            if i in arc:
                continue
            ok = True
            for a, b in itertools.combinations(arc, 2):
                if coll(pts[a], pts[b], pts[i]):
                    ok = False
                    break
            if ok:
                extend(arc + [i], i + 1)
    extend(fixed, 0)
    return best[0]


def mp_dickson(n, dps=120):
    import mpmath as mp
    mp.mp.dps = dps
    X = [2 * mp.cos(mp.pi * j / n) for j in range(n + 1)]
    Y = [2 * mp.cos(mp.pi * k / (n + 1)) for k in range(n + 2)]
    S = [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    cols = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    A = mp.matrix([[X[j] ** a * Y[k] ** b for (a, b) in cols] for (j, k) in S])
    d2 = mp.det(A) ** 2
    N = len(S)
    pred = mp.mpf(2) ** ((n * n + 3 * n + 6) // 2) * mp.mpf(n * (n + 1)) ** N
    return float(abs(d2 / pred - 1))


def main(outpath):
    out = {'checker': 'claude-audit-01 check_padua.py', 'python': platform.python_version(),
           'numpy': np.__version__,
           'checker_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'gf_sha256': hashlib.sha256(open(os.path.join(os.path.dirname(__file__), 'gf.py'), 'rb').read()).hexdigest()}
    fields = []
    qs = [3, 5, 7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 37, 41, 43, 47, 49]
    for q in qs:
        for n in range(1, (q + 1) // 2 + 3):
            try:
                chk_padua_field(q, n, fields, gram_limit=8)
            except AssertionError:
                raise
    out['padua_field_cases'] = fields
    out['rational_cases'] = sum(1 for r in fields if r['rational'])
    out['nonrational_in_Fq2_cases'] = sum(1 for r in fields if not r['rational'])
    print('padua field cases', len(fields), out['rational_cases'], flush=True)
    bad = []
    for n in range(1, 9):
        for p in (2, 3, 5, 7):
            if (2 * n * (n + 1)) % p == 0:
                chk_bad_reduction(p, n, bad)
    out['bad_char_reductions_singular'] = bad
    print('bad reductions', len(bad), flush=True)
    quad = []
    for q in [3, 5, 7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 37, 41, 43, 47, 49]:
        chk_quadratic(q, quad)
    out['quadratic_character_cases'] = quad
    print('quadratic', len(quad), flush=True)
    codes = []
    for q, n in [(5, 2), (7, 3), (7, 2), (7, 1), (9, 4), (11, 5), (13, 6), (17, 8), (13, 2), (11, 2), (5, 1), (25, 12)]:
        code_checks(q, n, codes, dist_max_msgs=30_000_000)
        print('codes', q, n, flush=True)
    out['code_cases'] = codes
    out['max_arc_PG2_7'] = max_arc_pg2(7)
    assert out['max_arc_PG2_7'] == 8
    out['mp_dickson_char0_relerr'] = {n: mp_dickson(n) for n in range(1, 11)}
    assert all(v < 1e-60 for v in out['mp_dickson_char0_relerr'].values())
    out['all_assertions'] = 'PASS'
    json.dump(out, open(outpath, 'w'), indent=1)
    print('ALL PASS')


if __name__ == '__main__':
    main(sys.argv[1])
