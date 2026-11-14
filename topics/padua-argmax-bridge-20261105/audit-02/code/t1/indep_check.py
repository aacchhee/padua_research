"""Auditor-written independent finite-layer checker (Claude, audit2 t1).
Written from the D32/D14/D19/C02/D29/E15/E12 statements, NOT importing
or copying the engine's checker.py. Checks a committed essential receipt's
finite combinatorial/rational layer given its recorded outward endpoints.
Native Arb enclosures are trusted inputs here (not re-evaluated).
Usage: python3 -I indep_check.py CERT.json [CERT.json ...]
"""
import json, sys
from fractions import Fraction as Q

PLO, PHI = Q(157, 50), Q(22, 7)


def hexq(s):
    x = float.fromhex(s)
    assert x == x and abs(x) != float('inf') and x.hex() == s, s
    return Q(x)


def fold(a, b):
    # value-preserving phase folding (D32 (7)): above hypotenuse reflect, swap only ON it
    if a + b > 1:
        a, b = 1 - a, 1 - b
    if a + b == 1 and (b, a) < (a, b):
        a, b = b, a
    return (a, b)


def boxes(preorder, maxdepth=18):
    """Decode midpoint preorder; return list of (token, box). Closed children."""
    out = []
    pos = 0

    def rec(al, ah, bl, bh, d):
        nonlocal pos
        assert d <= maxdepth and pos < len(preorder), 'depth/missing'
        t = preorder[pos]; pos += 1
        assert ah > al and bh > bl
        if t == 'a':
            mid = (al + ah) / 2
            rec(al, mid, bl, bh, d + 1); rec(mid, ah, bl, bh, d + 1)
        elif t == 'b':
            mid = (bl + bh) / 2
            rec(al, ah, bl, mid, d + 1); rec(al, ah, mid, bh, d + 1)
        elif t in '.f':
            out.append((t, (al, ah, bl, bh)))
        else:
            raise AssertionError('token ' + t)
    rec(Q(0), Q(1), Q(0), Q(1), 0)
    assert pos == len(preorder), 'trailing tokens'
    assert len(preorder) <= 2047
    return out


def area_check(leaves):
    # Independent completeness sanity: leaf areas sum to 1 (partition of [0,1]^2).
    return sum((ah - al) * (bh - bl) for _, (al, ah, bl, bh) in leaves) == 1


def floor_delta(n, r):
    # C02 (3)/(4) and D29-radius41 (1); D29-floor512 for n>=512.
    if n >= 512:
        return Q(1, 20)
    a = 1 - r * r / 4
    U = Q(347, 1000) * a - Q(157, 500) * r
    V = Q(17, 20) * a - r / 2
    W = Q(779, 750) * a - Q(5, 6) * r
    B = Q(11711, 48400) * U - Q(120, 157) * V / n - Q(250, 157) * W / n - Q(100, 3) * V / (n * n)
    if n < 64:
        return max(Q(1, 512), min(Q(1, 32), B))
    if n < 160:
        return max(Q(1, 64), min(Q(1, 20), B))
    return max(Q(1, 32), min(Q(1, 20), B))


def ceil_q(x):
    return Q(-((-x.numerator) // x.denominator))


def check(path):
    d = json.load(open(path))
    n = d['n']; assert type(n) is int and n >= 41
    m = n + 1; kap = Q(n, m)
    hybrid = d['format'] == 'FINAL-HYBRID-kept-proof-v1'
    corner_cut = 256 if hybrid else 1024
    W = {}
    for a, b, h in d['S_upper_rows']:
        k = (Q(a), Q(b)); assert fold(*k) == k and k not in W
        W[k] = hexq(h)
    L = hexq(d['origin_lower_hex'])
    assert 0 < L <= W[(Q(0), Q(0))]
    leaves = boxes(d['tree']['preorder'])
    assert area_check(leaves), 'leaf areas do not sum to 1'
    has_f = any(t == 'f' for t, _ in leaves)
    if has_f:
        assert hybrid
    live = [(t, B) for t, B in leaves if B[0] + B[2] <= 1]

    def theta(B):
        al, ah, bl, bh = B
        return PHI ** 2 * ((ah - al) ** 2 + kap ** 2 * (bh - bl) ** 2) / 8

    def Vmax(B):
        al, ah, bl, bh = B
        return max(W[fold(a, b)] for a in (al, ah) for b in (bl, bh))

    grid = sorted({fold(Q(i, 4), Q(j, 4)) for i in range(5) for j in range(5 - i)})
    assert len(grid) == 13
    method = d['norm']['method']
    if method == 'GRID':
        M = ceil_q(Q(784, 663) * max(W[k] for k in grid))
    else:
        assert method == 'TREE' and not has_f
        assert all(theta(B) < 1 for _, B in live)
        M = ceil_q(max(Vmax(B) / (1 - theta(B)) for _, B in live))
    assert M == Q(d['norm']['M']), ('M', M, d['norm']['M'])
    counts = {}; minmarg = {}
    for t, B in live:
        al, ah, bl, bh = B
        if t == 'f':
            assert n >= 192 and al + bl >= Q(1, 2) and al + bl <= 1, 'E15 guard'
            counts['f'] = counts.get('f', 0) + 1
            continue
        U = Vmax(B) + theta(B) * M
        if U < L:
            tag, g = 'FAR', L - U
        else:
            high = min(ah + bh, Q(1))
            r = min(Q(1, 2), PHI * (ah + bh))
            delta = floor_delta(n, r)
            assert 2 * PHI * high <= 1 and U - delta < L, ('leaf fails', B)
            tag, g = 'NEAR', L - U + delta
        assert g > 0
        counts[tag] = counts.get(tag, 0) + 1
        minmarg[tag] = min(minmarg.get(tag, g), g)
    counts['OUTSIDE'] = len(leaves) - len(live)
    if n < corner_cut:
        keys = [(Q(1, 4 * n), Q(0)), (Q(0), Q(3, 16 * m)), (Q(1, 4 * n), Q(3, 16 * m))]
        rows = d['lambda_upper_rows']; assert len(rows) == 3
        A = []
        for (x, z, h), k in zip(rows, keys):
            assert (Q(x), Q(z)) == k
            A.append(hexq(h))
        u, v = Q(1, 32), Q(9, 512)
        qv = min((L - A[0]) / u, (L - A[1]) / v, (L - A[2]) / (u + v))
        thr = M * PHI ** 4 * max(u, kap ** 4 * v) / 6
        assert qv > thr, 'corner'
        corner = ('ACTUAL3', qv - thr)
    else:
        assert d['lambda_upper_rows'] == []
        corner = ('ANALYTIC', None)
    needed = set(grid) if hybrid else set()
    for t, B in live:
        if t == '.':
            al, ah, bl, bh = B
            needed |= {fold(a, b) for a in (al, ah) for b in (bl, bh)}
    extra = set(W) - needed
    missing = needed - set(W)
    assert not missing
    return dict(n=n, method=method, M=str(M), nodes=len(d['tree']['preorder']), leaves=len(leaves),
                S=len(W), extra_S=len(extra), counts=counts,
                minmarg={k: str(v) for k, v in minmarg.items()},
                corner=corner[0], corner_gap=None if corner[1] is None else str(corner[1]),
                agrees_with_recorded_margins=all(Q(d['verification']['minimum_strict_margins'][k]) == v for k, v in minmarg.items()))


if __name__ == '__main__':
    for p in sys.argv[1:]:
        try:
            print(json.dumps(check(p)))
        except Exception as e:
            print(json.dumps({'path': p, 'FAIL': repr(e)}))
