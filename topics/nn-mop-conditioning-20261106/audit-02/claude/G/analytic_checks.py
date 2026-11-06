#!/usr/bin/env python3
"""Claude audit-02: exact checks of the analytic tail ingredients in
response-gauge-infimum.md sections 2-4 (own code)."""
from fractions import Fraction as Fr
from math import comb, factorial, sqrt
import sympy as S


def rising(a, k):
    r = Fr(1)
    for i in range(k):
        r *= a + i
    return r


def var_of(z, w):
    W = sum(w); pi = [x / W for x in w]
    mu = sum(p * x for p, x in zip(pi, z))
    return sum(p * (x - mu) ** 2 for p, x in zip(pi, z)), pi, mu


def r_mixed(z, w, sx, mass):
    v, pi, mu = var_of(z, w)
    node = sum(2 * p * abs(x - mu) * s for p, x, s in zip(pi, z, sx))
    g = [(x - mu) ** 2 - v for x in z]
    wt = min(sum(p * abs(gl - lam) for p, gl in zip(pi, g)) for lam in g) if mass else sum(p * abs(gl) for p, gl in zip(pi, g))
    return v, (node + wt) / v


res = {}
# Hahn variance formula and both specializations; Krawtchouk variance
a, b, M = S.symbols('a b M', positive=True)
vform = 4 * a * b * (M + a + b) / (M * (a + b) ** 2 * (a + b + 1))
assert S.simplify(vform.subs({a: 2, b: 2}) - (M + 4) / (5 * M)) == 0
assert S.simplify(vform.subs({a: S.Rational(5, 2), b: 2}) - S.Rational(160, 891) * (1 + 9 / (2 * M))) == 0
# combining E k and E k(k-1) into Var(k) symbolically
Ek = M * a / (a + b); Ekk = M * (M - 1) * a * (a + 1) / ((a + b) * (a + b + 1))
assert S.simplify(4 * (Ekk + Ek - Ek ** 2) / M ** 2 - vform) == 0
worst_r_bound_gap = []
for MM in range(1, 61):
    z = [Fr(2 * k, MM) - 1 for k in range(MM + 1)]
    for al in (Fr(1), Fr(3, 2)):
        A = al + 1
        w = [rising(A, k) / factorial(k) * rising(Fr(2), MM - k) / factorial(MM - k) for k in range(MM + 1)]
        v, _, _ = var_of(z, w)
        assert v == 4 * A * 2 * (MM + A + 2) / (MM * (A + 2) ** 2 * (A + 3)), (MM, al)
        assert v >= Fr(1, 5) if al == 1 else v > Fr(4, 25)
        for mass in (False, True):
            _, r = r_mixed(z, w, [Fr(1)] * (MM + 1), mass)
            bound = 2 / sqrt(v) + 2
            assert float(r) <= bound + 1e-12 and r < 7, (MM, al, r)
            worst_r_bound_gap.append(float(r) / bound)
    for p in (Fr(2, 5), Fr(1, 2)):
        w = [comb(MM, k) * p ** k * (1 - p) ** (MM - k) for k in range(MM + 1)]
        v, _, _ = var_of(z, w)
        assert v == 4 * p * (1 - p) / MM and v >= Fr(24, 25 * MM)
        for mass in (False, True):
            _, r = r_mixed(z, w, [Fr(1)] * (MM + 1), mass)
            assert float(r) <= 2 / sqrt(v) + 2 + 1e-12
            assert float(r) <= 5 * sqrt(MM / 6) + 2 + 1e-12 and r <= Fr(9, 2) * MM
            assert Fr(5) ** MM / MM >= 5 * MM > Fr(9, 2) * MM
res['variance_and_r_bounds_M1_60'] = 'PASS'
res['max_r_over_bound9'] = max(worst_r_bound_gap)
# M=1 spacing: r with node scale 2 (exception) vs K lower 5
z = [Fr(-1), Fr(1)]
for p in (Fr(2, 5), Fr(1, 2)):
    w = [1 - p, p]
    for mass in (False, True):
        res['kraw_M1_spacing_r_p%s_mass%s' % (p, mass)] = str(r_mixed(z, w, [Fr(2)] * 2, mass)[1])
# 5^M >= 5M^2
assert all(5 ** m >= 5 * m * m for m in range(1, 400))
# A_M >= 2^M (M-1), f_M monotone, onset
def A_M(M):
    T = lambda k: sum(comb(k, h) * comb(M + k + 3 - h, M - k) for h in range(k + 1))
    return sum(T(k) * sum(comb(M - 1, 2 * i + 1) * comb(k + i, k) for i in range(M // 2)) for k in range(M + 1))
assert all(sum(comb(MM, h) * comb(2 * MM + 3 - h, 0) for h in range(MM + 1)) == 2 ** MM for MM in range(1, 40))
assert all(A_M(m) >= 2 ** m * (m - 1) for m in range(2, 41))
f = lambda m: Fr(2 ** m * (m - 1), 27 * m * (2 * m + 3))
assert all(f(m + 1) > f(m) for m in range(2, 200))
assert all(f(m + 1) / f(m) == Fr(2 * m * m * (2 * m + 3), (m + 1) * (m - 1) * (2 * m + 5)) for m in range(2, 50))
assert f(14) / 2 == Fr(106496, 11718) and f(14) / 2 > 7 and f(13) / 2 < 7 and f(13) > 7
res['f_M_over2'] = {m: float(f(m) / 2) for m in (12, 13, 14, 15)}
res['A_M_over_2^M(M-1)'] = {m: float(Fr(A_M(m), 2 ** m * (m - 1))) for m in (2, 5, 10, 13, 14, 20)}
mm = S.symbols('m')
assert S.expand(2 * mm ** 2 * (2 * mm + 3) - (mm + 1) * (mm - 1) * (2 * mm + 5)) == 2 * mm ** 3 + mm ** 2 + 2 * mm + 5
res['all'] = 'PASS'
print(res)
