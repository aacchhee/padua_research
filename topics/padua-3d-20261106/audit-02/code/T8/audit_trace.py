#!/usr/bin/env python3
"""Attempts to break T8 PD-N-02 (all-phase M=10) and PD-T-03 (half-period trace)."""
import itertools as it, math, random, sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from audit_census import modes, rank_mod_p, prim_root_of_unity, primes_1_mod, node_set

def D_brute(r, n, d=3):
    return sum((-1) ** sum(a[:r]) for a in it.product(range(n + 1), repeat=d) if sum(a) <= n)
def D_formula(r, n):
    m, odd = divmod(n, 2)
    return {1: [(m + 1) ** 2, (m + 1) * (m + 2)], 2: [m + 1, 0], 3: [(m + 1) ** 2, -(m + 1) * (m + 2)]}[r][odd]
assert all(D_brute(r, n) == D_formula(r, n) for r in (1, 2, 3) for n in range(0, 31))
print('D_r(n) formulas match brute force for n<=30, r=1,2,3')
# M=10 Pi_2 trace (1/2 from monomials): D_r(2)=4,2,4
assert [D_brute(r, 2) for r in (1, 2, 3)] == [4, 2, 4]
# N even at odd n (indeed 4|N) for n<=201
assert all(math.comb(n + 3, 3) % 4 == 0 for n in range(1, 202, 2))
# Padua d=2: half-period fixed nodes vs single-axis polynomial trace, n=1..30
for n in range(1, 31):
    M = 2 * n * (n + 1); z = (n + 1, n)
    pts = {tuple(min(k * c % M, -k * c % M) for c in z) for k in range(M)}
    assert len(pts) == (n + 1) * (n + 2) // 2
    shift = {tuple(min((k + M // 2) * c % M, -(k + M // 2) * c % M) for c in z): tuple(min(k * c % M, -k * c % M) for c in z) for k in range(M)}
    # physical: x -> -x on odd-generator axis means folded r -> M/2 - r
    oddax = [j for j in range(2) if z[j] % 2]; assert len(oddax) == 1
    fixed = [p for p in pts if all((p[j] * 4 == M) for j in oddax)]   # cos = 0 <=> r = M/4
    for p in pts:
        img = tuple((M // 2 - p[j]) if j in oddax else p[j] for j in range(2)); assert img in pts
    tr = sum((-1) ** a[oddax[0]] for a in it.product(range(n + 1), repeat=2) if sum(a) <= n)
    assert len(fixed) == n // 2 + 1 == tr, (n, len(fixed), tr)
print('Padua d=2: fixed nodes = polynomial trace = floor(n/2)+1 for n=1..30')

# ---- M=10, n=2: numerical ranks, all z mod 10, random real phases
rng = np.random.default_rng(20261106)
ms2 = modes(2)
def num_rank(P, n, ms):
    V = np.column_stack([np.prod([np.cos(a * np.arccos(np.clip(P[:, j], -1, 1))) for j, a in enumerate(e)], axis=0) for e in ms])
    s = np.linalg.svd(V, compute_uv=False); return int(np.sum(s > 1e-9 * s[0]))
maxr = {}; cnt = 0; distinct_cases = 0
for z in it.product(range(10), repeat=3):
    r = sum(c % 2 for c in z)
    for trial in range(8):
        phi = rng.uniform(0, 2 * np.pi, 3)
        k = np.arange(10)[:, None]
        P = np.cos(phi[None, :] + 2 * np.pi * k * np.array(z)[None, :] / 10)
        if len({tuple(np.round(p, 9)) for p in P}) < 10:
            continue
        distinct_cases += 1
        # check physical half-period action
        R = np.where(np.array(z) % 2 == 1, -1.0, 1.0)
        assert np.allclose(P[(np.arange(10) + 5) % 10], P * R[None, :], atol=1e-12)
        rk = num_rank(P, 2, ms2); maxr[r] = max(maxr.get(r, 0), rk); cnt += 1
print('M=10 n=2 random real phases: cases with 10 distinct nodes', distinct_cases, 'max numerical rank by #odd coords', maxr)

# ---- M=10 rigorous F_p search over rational phases in (2pi/120)Z^3: full rank would be a counterexample
L = 120; p = primes_1_mod(L, 1, start=10**6)[0]; w = prim_root_of_unity(L, p); i2 = pow(2, -1, p)
cv = [(pow(w, e, p) + pow(w, -e % L, p)) * i2 % p for e in range(L)]
best = {}; tested = 0
random.seed(7)
phase_list = [tuple(random.randrange(L) for _ in range(3)) for _ in range(40)] + [(0, 0, 0), (30, 20, 15), (1, 2, 3), (6, 4, 3)]
for z in it.product(range(10), repeat=3):
    r = sum(c % 2 for c in z)
    for ph in phase_list:
        angs = [tuple((h + 12 * k * c) % L for c, h in zip(z, ph)) for k in range(10)]
        if len({tuple(min(a, L - a) for a in t) for t in angs}) < 10: continue
        A = [[cv[a] ** e1 * cv[b] ** e2 * cv[c] ** e3 % p for e1, e2, e3 in ms2] for a, b, c in angs]
        rk = rank_mod_p(A, p); best[r] = max(best.get(r, 0), rk); tested += 1
        assert rk <= (8 if r % 2 else 9), (z, ph, rk)
print('M=10 F_p (rigorous lower bounds) rational phases: tested', tested, 'max rank by r', best)

# ---- M=N=20, n=3 (outside the theorem): numerical ranks by r
ms3 = modes(3); res = {}
for trial in range(3000):
    z = tuple(int(v) for v in rng.integers(0, 20, 3)); r = sum(c % 2 for c in z)
    phi = rng.uniform(0, 2 * np.pi, 3); k = np.arange(20)[:, None]
    P = np.cos(phi[None, :] + 2 * np.pi * k * np.array(z)[None, :] / 20)
    if len({tuple(np.round(q, 9)) for q in P}) < 20: continue
    rk = num_rank(P, 3, ms3); res.setdefault(r, []).append(rk)
print('M=N=20 n=3 random phases: max rank by r', {r: max(v) for r, v in res.items()},
      'count full rank by r', {r: sum(x == 20 for x in v) for r, v in res.items()}, 'cases', {r: len(v) for r, v in res.items()})

# ---- E class (M=2N-2, z=(1,b,c), zero phase): try to find full rank where theorem forbids
def e_class(n, parity_filter):
    N = math.comb(n + 3, 3); M = 2 * N - 2; p = primes_1_mod(M, 1, start=10**6)[0]
    w = prim_root_of_unity(M, p); i2 = pow(2, -1, p)
    cv = [(pow(w, e, p) + pow(w, -e % M, p)) * i2 % p for e in range(M)]
    ms = modes(n); mx = 0; tot = 0; ceil_ok = True
    f = 1 if M % 4 == 0 else 0
    for b in range(0, M):
        for c in range(b, M):
            z = (1, b, c); r = sum(v % 2 for v in z)
            if not parity_filter(r): continue
            pts = node_set(M, z); assert len(pts) == N
            A = [[cv[a] ** e1 * cv[bb] ** e2 * cv[cc] ** e3 % p for e1, e2, e3 in ms] for a, bb, cc in pts]
            rk = rank_mod_p(A, p); tot += 1; mx = max(mx, rk)
            Dr = D_brute(r, n); ceil = N - abs(Dr - f) // 2
            if rk > ceil: ceil_ok = False
    return dict(n=n, M=M, f=f, tested=tot, max_rank_lower_bound=mx, N=N, rank_le_trace_ceiling=ceil_ok)
print('E-class n=2 all (1,b,c):', e_class(2, lambda r: True))
print('E-class n=3 r in {1,3}:', e_class(3, lambda r: r % 2 == 1))
print('E-class n=4 all (1,b,c) [b<=c<M]:', e_class(4, lambda r: True))
