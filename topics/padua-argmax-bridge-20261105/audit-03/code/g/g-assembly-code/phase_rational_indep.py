#!/usr/bin/env python3
"""Independent exact-rational re-verification of a FINAL-HYBRID essential
receipt (audit G-assembly, Claude Opus 5.5).  Written from the D32/D14/D19/
D29/C02/D08/E12/E15 statements as reconstructed in the audit, NOT importing
the repository checker.  Native outward S/lambda uppers and the origin
lower are TRUSTED inputs (Arb/MPFR); everything else is recomputed here.

Checks: tree grammar and full token consumption; closed midpoint cover of
[0,1]^2; OUTSIDE iff al+bl>1; canonical folding of raw vertices; presence
of every needed key; global norm (GRID: M>=784 V_E/663 over the 15-point
quarter grid folded to 13 keys; TREE: M>=max V_B/(1-theta_B), no f leaf,
all theta<1); per-leaf Peano upper U=V+theta*M with theta=(22/7)^2[da^2+
k^2 db^2]/8; FAR (U<L) or NEAR (2*p_hi*high<=1 and U-delta(r_B)<L) with
the degree tier floor; f-leaf guard (n>=192, 1/2<=al+bl<=1, positive
widths); corner: n<256 three actual points at the exact physical turns
and q > M p_hi^4 max(u',k^4 v')/6; n>=256 analytic E12 (no rows needed).
"""
import json, sys
from fractions import Fraction as Fr

def hexfr(h):
    return Fr(float.fromhex(h))  # exact: binary64 -> rational

def floor_tier(n, r):
    a = 1 - r * r / 4
    U = Fr(347, 1000) * a - Fr(157, 500) * r
    V = Fr(17, 20) * a - r / 2
    W = Fr(779, 750) * a - Fr(5, 6) * r
    B = Fr(11711, 48400) * U - 120 * V / (157 * n) - 250 * W / (157 * n) - 100 * V / (3 * n * n)
    if 41 <= n < 64: return max(Fr(1, 512), min(Fr(1, 32), B))
    if 64 <= n < 160: return max(Fr(1, 64), min(Fr(1, 20), B))
    if 160 <= n < 512: return max(Fr(1, 32), min(Fr(1, 20), B))
    raise ValueError('no tier')

def canon(a, b):
    if a + b > 1: a, b = 1 - a, 1 - b
    if a + b == 1: a, b = min((a, b), (b, a))
    return (a, b)

def verify(path):
    d = json.load(open(path)); n = int(d['n']); m = n + 1; kap = Fr(n, m)
    p_lo, p_hi = (Fr(x) for x in d['pi_bracket'])
    assert p_lo == Fr(157, 50) and p_hi == Fr(22, 7)
    S = {}
    for a, b, h in d['S_upper_rows']:
        key = (Fr(a), Fr(b)); assert key not in S; assert canon(*key) == key, ('noncanonical key', key)
        S[key] = hexfr(h)
    L = hexfr(d['origin_lower_hex'])
    toks = d['tree']['preorder']; pos = [0]; leaves = []
    def parse(box, depth):
        t = toks[pos[0]]; pos[0] += 1
        (al, ah), (bl, bh) = box
        if t == 'a':
            mid = (al + ah) / 2; assert al < mid < ah
            parse(((al, mid), (bl, bh)), depth + 1); parse(((mid, ah), (bl, bh)), depth + 1)
        elif t == 'b':
            mid = (bl + bh) / 2; assert bl < mid < bh
            parse(((al, ah), (bl, mid)), depth + 1); parse(((al, ah), (mid, bh)), depth + 1)
        elif t in '.f':
            leaves.append((box, t, depth))
        else: raise ValueError('bad token')
    parse(((Fr(0), Fr(1)), (Fr(0), Fr(1))), 0)
    assert pos[0] == len(toks), 'trailing tokens'
    area = sum((bx[0][1] - bx[0][0]) * (bx[1][1] - bx[1][0]) for bx, _, _ in leaves)
    assert area == 1, 'cover area'
    # norm
    grid = set(canon(Fr(i, 4), Fr(j, 4)) for i in range(5) for j in range(5) if i + j <= 4)
    assert len(grid) == 13
    assert grid <= set(S), 'missing grid premise'
    VE = max(S[k] for k in grid)
    method = d['norm']['method']; M = Fr(d['norm']['M'])
    has_f = any(t == 'f' for _, t, _ in leaves)
    def theta(bx):
        (al, ah), (bl, bh) = bx
        return p_hi ** 2 * ((ah - al) ** 2 + kap ** 2 * (bh - bl) ** 2) / 8
    def vmax(bx):
        (al, ah), (bl, bh) = bx
        ks = [canon(x, y) for x in (al, ah) for y in (bl, bh)]
        for k in ks: assert k in S, ('missing vertex key', k)
        return max(S[k] for k in ks)
    num = [(bx, t) for bx, t, _ in leaves if t == '.' and bx[0][0] + bx[1][0] <= 1]
    if method == 'GRID':
        assert M >= Fr(784, 663) * VE, 'GRID norm too small'
    elif method == 'TREE':
        assert not has_f, 'TREE with analytic leaf'
        R = Fr(0)
        for bx, _ in num:
            th = theta(bx); assert th < 1
            R = max(R, vmax(bx) / (1 - th))
        assert M >= R, 'TREE norm too small'
    else: raise ValueError(method)
    counts = {'OUTSIDE': 0, 'FAR': 0, 'NEAR': 0, 'ANALYTIC_FAR': 0}
    minfar = None; minnear = None
    for bx, t, _ in leaves:
        (al, ah), (bl, bh) = bx
        if al + bl > 1:
            counts['OUTSIDE'] += 1; continue
        if t == 'f':
            assert n >= 192 and 0 <= al < ah <= 1 and 0 <= bl < bh <= 1 and Fr(1, 2) <= al + bl <= 1, 'bad f leaf'
            counts['ANALYTIC_FAR'] += 1; continue
        U = vmax(bx) + theta(bx) * M
        if U < L:
            counts['FAR'] += 1; g = L - U; minfar = g if minfar is None else min(minfar, g); continue
        high = min(ah + bh, Fr(1))
        r = min(Fr(1, 2), p_hi * (ah + bh))
        dl = floor_tier(n, r)
        assert 2 * p_hi * high <= 1, ('leaf neither FAR nor guarded NEAR', bx)
        assert U - dl < L, ('NEAR fails', bx)
        counts['NEAR'] += 1; g = L - (U - dl); minnear = g if minnear is None else min(minnear, g)
    # corner
    corner = {}
    if n < 256:
        lam = {(Fr(x), Fr(y)): hexfr(h) for x, y, h in d['lambda_upper_rows']}
        want = [(Fr(1, 4 * n), Fr(0)), (Fr(0), Fr(3, 16 * m)), (Fr(1, 4 * n), Fr(3, 16 * m))]
        assert set(lam) == set(want), 'wrong actual points'
        up, vp = Fr(1, 32), Fr(9, 512)
        q = min((L - lam[want[0]]) / up, (L - lam[want[1]]) / vp, (L - lam[want[2]]) / (up + vp))
        thr = M * p_hi ** 4 * max(up, kap ** 4 * vp) / 6
        assert q > thr, 'corner descent fails'
        corner = {'kind': 'three actual points', 'q': str(q), 'threshold': str(thr), 'radial_coeff_lower': str((q - thr) / (2 * p_hi ** 2))}
    else:
        assert not d.get('lambda_upper_rows'), 'unexpected actual rows from 256'
        corner = {'kind': 'E12 analytic (n>=256)'}
    return {'file': path.split('/')[-1], 'n': n, 'method': method, 'M': str(M), 'V_E': float(VE), 'grid_bound': float(Fr(784, 663) * VE),
            'L': float(L), 'leaves': len(leaves), 'counts': counts, 'min_far_margin': str(minfar), 'min_near_margin': str(minnear),
            'corner': corner, 'S_keys': len(S), 'ok': True}

if __name__ == '__main__':
    out = [verify(p) for p in sys.argv[1:]]
    print(json.dumps(out, indent=1))
