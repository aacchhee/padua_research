#!/usr/bin/env python3
"""(i) Exact check of the n=3 survivor M=38, z=(1,6,17): 20 distinct nodes and
Pi_3 unisolvence via det != 0 over F_p (hom Z[zeta_38,1/2] -> F_p, zeta_38 -> verified
primitive 38th root mod p), plus mpmath 50-digit determinant as a sanity value.
(ii) Exact Q(zeta_120) verification of the three written quadratic annihilators of
PK/PT/PO at n=2 and of their 10-node cardinality."""
import itertools as it, math
import sympy as sp, mpmath as mp
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from audit_census import modes, prim_root_of_unity, primes_1_mod

def det_mod_p(A, p):
    A = [r[:] for r in A]; n = len(A); d = 1
    for j in range(n):
        k = next((i for i in range(j, n) if A[i][j] % p), None)
        if k is None: return 0
        if k != j: A[j], A[k] = A[k], A[j]; d = -d
        d = d * A[j][j] % p; inv = pow(A[j][j], -1, p)
        for i in range(j + 1, n):
            f = A[i][j] * inv % p
            if f: A[i] = [(x - f * y) % p for x, y in zip(A[i], A[j])]
    return d % p

M, z, n = 38, (1, 6, 17), 3
fold = lambda r: min(r % M, -r % M)
pts = sorted({tuple(fold(k * c) for c in z) for k in range(M)})
assert len(pts) == 20 and all(0 <= r <= M // 2 for pt in pts for r in pt)
print('M38 folded nodes (numerators over 38):', pts)
for p in primes_1_mod(M, 4, start=10**6) + [191, 229]:
    if (p - 1) % M: continue
    w = prim_root_of_unity(M, p); i2 = pow(2, -1, p)
    cv = [(pow(w, r, p) + pow(w, -r % M, p)) * i2 % p for r in range(M)]
    A = [[cv[a] ** e1 * cv[b] ** e2 * cv[c] ** e3 % p for e1, e2, e3 in modes(n)] for a, b, c in pts]
    print('p', p, 'w', w, 'det mod p', det_mod_p(A, p))
mp.mp.dps = 50
V = mp.matrix([[mp.cos(2 * mp.pi * a / M) ** e1 * mp.cos(2 * mp.pi * b / M) ** e2 * mp.cos(2 * mp.pi * c / M) ** e3
                for e1, e2, e3 in modes(n)] for a, b, c in pts])
print('mpmath det (monomial basis):', mp.nstr(mp.det(V), 20))
# all distinct physical nodes check also via mpmath values
phys = {tuple(mp.nstr(mp.cos(2 * mp.pi * r / M), 30) for r in pt) for pt in pts}; assert len(phys) == 20

# ---- P rules, exact in Q(zeta_120)
x_ = sp.Symbol('x'); L = 120
PHI = sp.Poly(sp.cyclotomic_poly(L, x_), x_, domain=sp.QQ)
def red(e): return sp.Poly(e, x_, domain=sp.QQ).rem(PHI)
def cosv(e): return red((x_ ** (e % L) + x_ ** (-e % L)) / 2)   # cos(2 pi e / 120)
S2 = red(x_ ** 15 + x_ ** (L - 15))            # 2cos(pi/4) = sqrt2
S3 = red(x_ ** 10 + x_ ** (L - 10))            # 2cos(pi/6) = sqrt3
assert red((S2 ** 2).as_expr() - 2).is_zero and red((S3 ** 2).as_expr() - 3).is_zero
phase = (30, 20, 15)  # pi/2, pi/3, pi/4 in units 2pi/120
gens = {'PK': (1, 3, 9), 'PT': (1, 3, 6), 'PO': (1, 5, 3)}
# check generator formulas at n=2 from the frozen preregistration
n2 = 2; Nn = 10
assert gens['PK'] == tuple(v % Nn for v in (1, n2 + 1, (n2 + 1) ** 2))
assert gens['PT'] == tuple(v % Nn for v in (1, n2 + 1, (n2 + 1) * (n2 + 2) // 2))
assert gens['PO'] == tuple(v % Nn for v in (1, 2 * n2 + 1, 2 * n2 * n2 + 2 * n2 + 1))
s2, s3 = S2.as_expr(), S3.as_expr(); s6 = s2 * s3
T2 = lambda v: 2 * v ** 2 - 1
polys = {
  'PK': lambda X, Y, W: X ** 2 + W ** 2 + s2 * X * W - sp.Rational(1, 2),
  'PO': lambda X, Y, W: 4 * Y ** 2 - 1,
  'PT': lambda X, Y, W: (2 * s2 - 2 * s6 / 3) * W + (s3 / 3) * T2(W) + (2 - 4 * s3 / 3) * T2(Y)
                        + (4 * s3 / 3) * X * Y + T2(X)}
for name, z in gens.items():
    angs = [tuple((ph + 12 * k * c) % L for c, ph in zip(z, phase)) for k in range(10)]
    folded = {tuple(min(a, L - a) for a in t) for t in angs}
    vals = [polys[name](*[cosv(a).as_expr() for a in t]) for t in angs]
    zero = all(red(sp.expand(v)).is_zero for v in vals)
    # nonzero-ness: generic numeric point
    nz = polys[name](*[sp.Rational(1, 7), sp.Rational(2, 9), sp.Rational(3, 11)])
    nzv = complex(sp.N(nz.subs(x_, sp.exp(2 * sp.pi * sp.I / L))))
    print(name, 'distinct nodes', len(folded), 'annihilator vanishes at all 10:', zero, 'value at generic pt', nzv)
    # mutation: add 1 -> must not vanish
    assert not all(red(sp.expand(v + 1)).is_zero for v in vals)
