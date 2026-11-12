#!/usr/bin/env python3
"""Auditor (Claude) independent group enumeration for T7 n2.

Own parameterisation: LOWER-triangular row basis of L=H^perp,
B=[[a,0,0],[r,b,0],[s,t,c]], 0<=r,s<a, 0<=t<b.  H = B^{-1}Z^3/Z^3,
points computed in closed form (scaled by m).  Checks: count formula
sum_{d|m} d*sigma(d) (sublattices of index m in Z^3), every group has
m distinct points annihilated by B, and all groups of one order are
distinct as point sets.  Also brute-force small-m subgroup count of
(Z/m)^3 by closure, independent of any lattice formula.
"""
import hashlib, itertools as it, json, math, sys
from collections import Counter
import numpy as np


def sigma(d):
    return sum(k for k in range(1, d+1) if d % k == 0)


def formula(m):
    return sum(d*sigma(d) for d in range(1, m+1) if m % d == 0)


def groups(m):
    for a in range(1, m+1):
        if m % a: continue
        for b in range(1, m//a+1):
            if (m//a) % b: continue
            c = m//a//b
            for r, s, t in it.product(range(a), range(a), range(b)):
                yield (a, b, c, r, s, t)


def points(g):
    a, b, c, r, s, t = g; m = a*b*c
    k = np.array(list(it.product(range(a), range(b), range(c))), dtype=np.int64)
    k1, k2, k3 = k[:, 0], k[:, 1], k[:, 2]
    x1 = k1*b*c
    x2 = (k2*a - r*k1)*c
    x3 = a*b*k3 - s*b*k1 - t*(a*k2 - r*k1)
    P = np.stack([x1, x2, x3], axis=1) % m
    return P


def check_group(g):
    a, b, c, r, s, t = g; m = a*b*c
    P = points(g)
    B = np.array([[a, 0, 0], [r, b, 0], [s, t, c]], dtype=np.int64)
    assert not np.any((P @ B.T) % m), g          # L annihilates H
    codes = np.unique(P[:, 0]*m*m + P[:, 1]*m + P[:, 2])
    assert len(codes) == m, g                      # |H| = m
    # closed under addition (subgroup): sum of two random points in set
    S = set(codes.tolist())
    for i in range(min(m, 5)):
        for j in range(min(m, 5)):
            q = (P[i]+P[j]) % m
            assert int(q[0]*m*m+q[1]*m+q[2]) in S
    return P, hashlib.sha1(codes.tobytes()).digest()


def brute_small(m):
    """Count subgroups of order m of (Z/m)^3 by closure (<=3 generators)."""
    els = list(it.product(range(m), repeat=3))
    add = lambda x, y: tuple((x[i]+y[i]) % m for i in range(3))
    def cyc(e):
        S = [(0, 0, 0)]; x = e
        while x != (0, 0, 0): S.append(x); x = add(x, e)
        return frozenset(S)
    C = {e: cyc(e) for e in els}
    subs = set(C.values()); layer = set(subs)
    for _ in range(2):
        new = set()
        for S in layer:
            for e in els:
                if e in S: continue
                T = frozenset(add(s, c) for s in S for c in C[e])
                if T not in subs: new.add(T)
        subs |= new; layer = new
    return sum(1 for S in subs if len(S) == m)


def main():
    res = {}
    total_formula = sum(formula(m) for m in range(10, 81))
    total_bc2 = sum(sum(b*c*c for a in range(1, m+1) if m % a == 0 for b in range(1, m//a+1) if (m//a) % b == 0 for c in [m//a//b]) for m in range(10, 81))
    res['formula_sum_d_sigma_d_10_80'] = total_formula
    res['producer_formula_sum_bc2_10_80'] = total_bc2
    small = {}
    for m in range(1, 7):
        small[m] = (brute_small(m), formula(m))
    res['bruteforce_small_m_(closure,formula)'] = small
    n_enum = 0; per = Counter(); dup = 0
    for m in range(10, 81):
        hs = set()
        for g in groups(m):
            P, hsh = check_group(g)
            n_enum += 1
            if hsh in hs: dup += 1
            hs.add(hsh)
        per[m] = len(hs)
        assert len(hs) == formula(m), (m, len(hs), formula(m))
    res['enumerated_lower_triangular_groups'] = n_enum
    res['duplicates'] = dup
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
