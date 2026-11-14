#!/usr/bin/env python3
"""Cross-checks only (mpmath/sympy, MEASURED corroboration, not proof).

1. kappa by direct quadrature of the DEFINING integral (digamma closed form of
   the odd sum), versus the c_k series at large K, versus brackets.py.
2. Series identities of J02 sec.1 at sample t; majorants a_p<=4^-p,
   |b_q|<9^-q, |c_k|<2*4^-k for all p,q,k<=80; a_p alternative formula.
3. Introduction decimals b, c, kappa; C_*, H0, j, t0, C_infinity bound values.
4. sympy: origin identity H0 = (C_* - B + g0)/2 with C_* = c1^2+kappa
   <=> H0 = kappa/2 + (2 k0/pi^2) log(2/pi); H04 f_k'' formula and both majorants.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 50
out = []


def rep(name, ok, extra=''):
    out.append(('PASS' if ok else 'FAIL', name, extra))


pi = mp.pi


def S_odd(t):           # sum_{l odd>=1} 1/(l(l^2-t^2))
    if t == 0:
        return (1 - mp.mpf(2) ** -3) * mp.zeta(3)
    return (2 * mp.digamma(mp.mpf(1) / 2) - mp.digamma((1 - t) / 2) - mp.digamma((1 + t) / 2)) / (4 * t * t)


def integrand(t):
    return t * t * mp.cot(pi * t / 2) * S_odd(t)


kap_quad = 8 / pi * mp.quad(integrand, [0, mp.mpf(1) / 2, 1])
# check S_odd against brute force partial sums at t=0.3
t = mp.mpf('0.3')
brute = mp.nsum(lambda j: 1 / ((2 * j + 1) * ((2 * j + 1) ** 2 - t * t)), [0, mp.inf])
rep('digamma closed form of odd sum (t=0.3)', abs(brute - S_odd(t)) < mp.mpf(10) ** -40, mp.nstr(brute - S_odd(t), 5))


def a_p(p):
    return 1 - 2 * mp.fsum(mp.zeta(2 * r) / 4 ** r for r in range(1, p + 1))


def b_q(q):
    if q == 0:
        return (1 - mp.mpf(2) ** -3) * mp.zeta(3)
    return (1 - mp.mpf(2) ** (-2 * q - 3)) * mp.zeta(2 * q + 3) - (1 - mp.mpf(2) ** (-2 * q - 1)) * mp.zeta(2 * q + 1)


mp.mp.dps = 120          # cancellation in a_p for large p needs extra digits
KMAX = 80
A = [a_p(p) for p in range(KMAX + 1)]
Bq = [b_q(q) for q in range(KMAX + 1)]
Cc = [mp.fsum(A[p] * Bq[k - p] for p in range(k + 1)) for k in range(KMAX + 1)]
rep('0<a_p<=4^-p, p<=80', all(0 < A[p] <= mp.mpf(4) ** -p for p in range(KMAX + 1)))
alt = [2 * mp.nsum(lambda r: (4 * r * r) ** (-p) / (4 * r * r - 1), [1, mp.inf]) for p in range(0, 12)]
rep('a_p = 2 sum (4r^2)^-p/(4r^2-1), p<=11', max(abs(alt[p] - A[p]) for p in range(12)) < mp.mpf(10) ** -40)
rep('0<b_0<10/9 and b_0<35/32', 0 < Bq[0] < mp.mpf(35) / 32)
rep('-9^-q<b_q<0, q=1..80', all(-mp.mpf(9) ** -q < Bq[q] < 0 for q in range(1, KMAX + 1)))
rep('|c_k|<2*4^-k, k<=80', all(abs(Cc[k]) < 2 * mp.mpf(4) ** -k for k in range(KMAX + 1)))
ratio = max(abs(Cc[k]) * mp.mpf(4) ** k for k in range(KMAX + 1))
rep('max_k |c_k| 4^k (informative)', True, mp.nstr(ratio, 8))
kap_series = 8 / pi ** 2 * mp.fsum(Cc[k] / (k + 1) for k in range(KMAX + 1))
kap3 = 8 / pi ** 2 * mp.fsum(Cc[k] / (k + 1) for k in range(4))
rep('series(K=80) = quadrature', abs(kap_series - kap_quad) < mp.mpf(10) ** -35, mp.nstr(kap_series - kap_quad, 5))
rep('|kappa - K3 partial| <= 1/480', abs(kap_quad - kap3) <= mp.mpf(1) / 480, mp.nstr(kap_quad - kap3, 8))
rep('actual K3 truncation error vs radius 1/480 (informative)', True,
    'err=%s, radius=%s' % (mp.nstr(kap_quad - kap3, 6), mp.nstr(mp.mpf(1) / 480, 6)))
for K in (1, 2, 3, 5, 8):
    pk = 8 / pi ** 2 * mp.fsum(Cc[k] / (k + 1) for k in range(K + 1))
    rep('tail bound (4) holds at K=%d' % K, abs(kap_quad - pk) <= mp.mpf(8) / (3 * (K + 2) * 4 ** (K + 1)))
# expansions at sample t
for tt in ('0.37', '0.9', '0.999'):
    t = mp.mpf(tt)
    lhs = t * t * mp.cot(pi * t / 2) / (1 - t * t)
    rhs = 2 * t / pi * mp.fsum(A[p] * t ** (2 * p) for p in range(KMAX + 1))
    lhs2 = (1 - t * t) * S_odd(t)
    rhs2 = mp.fsum(Bq[q] * t ** (2 * q) for q in range(KMAX + 1))
    tol = mp.mpf(10) ** -30 if tt != '0.999' else mp.mpf(10) ** -3
    rep('a-series identity at t=%s' % tt, abs(lhs - rhs) < tol, mp.nstr(lhs - rhs, 3))
    rep('b-series identity at t=%s' % tt, abs(lhs2 - rhs2) < tol, mp.nstr(lhs2 - rhs2, 3))

mp.mp.dps = 50
g = mp.euler
c1 = 2 * (g + mp.log(8 / pi)) / pi
kap = kap_quad
Cstar = c1 ** 2 + kap
b = 2 * (2 / pi) * c1
C0 = 2 * g + 4 * mp.log(2)
k0 = C0 - 2 * mp.log(pi)
d0 = C0 * (C0 - mp.mpf(7) / 2) / pi ** 2
g0 = 4 * (mp.log(pi) ** 2 - mp.log(2) ** 2) / pi ** 2
H0 = kap / 2 - 2 * k0 / pi ** 2 * mp.log(pi / 2)
Bc = C0 ** 2 / pi ** 2
j = H0 + d0 - g0
t0 = 2 * mp.log(2) / pi
Cinf = Cstar - j / 2 + mp.sqrt(j * j / 4 + t0 * t0)
rep('kappa ~ 0.919710118388 (intro)', abs(kap - mp.mpf('0.919710118388')) < 5e-13, mp.nstr(kap, 20))
rep('b ~ 1.225522125742 (intro)', abs(b - mp.mpf('1.225522125742')) < 5e-13, mp.nstr(b, 20))
rep('c ~ 1.846160310424 (intro)', abs(Cstar - mp.mpf('1.846160310424')) < 5e-13, mp.nstr(Cstar, 20))
rep('C_* = B - g0 + 2 H0 (paper uc:master, at zero)', abs(Cstar - (Bc - g0 + 2 * H0)) < mp.mpf(10) ** -40)
for nm, v in [('H0', H0), ('d0', d0), ('g0', g0), ('j', j), ('t0', t0), ('Cinf_bound', Cinf),
              ('margin 9/4-Cinf_bound', mp.mpf(9) / 4 - Cinf), ('margin j-23/250', j - mp.mpf(23) / 250),
              ('margin 4629/2500-C*', mp.mpf(4629) / 2500 - Cstar), ('margin kappa-9/10', kap - mp.mpf(9) / 10),
              ('margin 221/500-t0', mp.mpf(221) / 500 - t0)]:
    rep('value ' + nm, True, mp.nstr(v, 15))
# worst case of the J02 coarse chain: C_* at its threshold, j and t0 at theirs
w = mp.mpf(4629) / 2500 - mp.mpf(23) / 500 + mp.sqrt((mp.mpf(23) / 250) ** 2 / 4 + (mp.mpf(221) / 500) ** 2)
rep('coarse-chain worst case < 9/4', w < mp.mpf(9) / 4, mp.nstr(mp.mpf(9) / 4 - w, 8))

# ---- sympy ----
gS, l2, lp, kS = sp.symbols('gamma log2 logpi kappa', real=True)
piS = sp.Symbol('pi', positive=True)
C0S = 2 * gS + 4 * l2
k0S = C0S - 2 * lp
c1S = 2 * (gS + 3 * l2 - lp) / piS
CstarS = c1S ** 2 + kS
BS = C0S ** 2 / piS ** 2
g0S = 4 * (lp ** 2 - l2 ** 2) / piS ** 2
H0_from_master = (CstarS - BS + g0S) / 2
H0_paper = kS / 2 + 2 * k0S / piS ** 2 * (l2 - lp)       # log(2/pi) = log2 - logpi
rep('sympy: origin identity uc:origin-identity <=> C_*=B-g0+2H0', sp.simplify(H0_from_master - H0_paper) == 0)
tS, kk = sp.symbols('t k', positive=True)
f = tS ** 2 / (4 * kk ** 2 - tS ** 2)
f2 = sp.simplify(sp.diff(f, tS, 2))
rep('sympy: f_k\'\' = 8k^2(4k^2+3t^2)/(4k^2-t^2)^3', sp.simplify(f2 - 8 * kk ** 2 * (4 * kk ** 2 + 3 * tS ** 2) / (4 * kk ** 2 - tS ** 2) ** 3) == 0)
rep('sympy: split = 8k^2/(4k^2-t^2)^2 + 32k^2t^2/(4k^2-t^2)^3',
    sp.simplify(f2 - 8 * kk ** 2 / (4 * kk ** 2 - tS ** 2) ** 2 - 32 * kk ** 2 * tS ** 2 / (4 * kk ** 2 - tS ** 2) ** 3) == 0)
hist = sp.Rational(8, 9) / kk ** 2 + sp.Rational(32, 27) / kk ** 4
rev = sp.Rational(32, 27) / kk ** 2 + sp.Rational(8, 9) / kk ** 4
rep('sympy: revised - historical termwise = (8/27)(k^2-1)/k^4 >= 0',
    sp.simplify(rev - hist - sp.Rational(8, 27) * (kk ** 2 - 1) / kk ** 4) == 0)
# numerical validation of both termwise majorants on a grid, k=1..200
ok_h = ok_r = True
worst = 0
from fractions import Fraction as Fq
for kv in range(1, 201):
    for i in range(0, 101):
        tv = Fq(i, 100)
        val = 8 * kv ** 2 * (4 * kv ** 2 + 3 * tv ** 2) / (4 * kv ** 2 - tv ** 2) ** 3
        h = Fq(8, 9) / kv ** 2 + Fq(32, 27) / kv ** 4
        r = Fq(32, 27) / kv ** 2 + Fq(8, 9) / kv ** 4
        ok_h &= bool(val <= h)
        ok_r &= bool(val <= r)
rep('historical termwise majorant f_k\'\'<=8/(9k^2)+32/(27k^4) on grid', ok_h)
rep('revised termwise majorant f_k\'\'<=32/(27k^2)+8/(9k^4) on grid', ok_r)
S2, S4 = sp.pi ** 2 / 6, sp.pi ** 4 / 90
H_exact = 8 / sp.pi * (sp.Rational(4, 9) * S2 + sp.Rational(16, 27) * S4)
R_exact = 8 / sp.pi * (sp.Rational(16, 27) * S2 + sp.Rational(4, 9) * S4)
H_coarse = sp.Rational(8, 3) * (sp.Rational(4, 9) * 2 + sp.Rational(16, 27) * sp.Rational(4, 3))
R_coarse = sp.Rational(8, 3) * (sp.Rational(16, 27) * 2 + sp.Rational(4, 9) * sp.Rational(4, 3))
rep('coarse historical bound (pi>3,S2<=2,S4<=4/3) < 5', H_coarse < 5, str(H_coarse))
rep('coarse revised bound < 5 and = 128/27', R_coarse < 5 and R_coarse == sp.Rational(128, 27), str(R_coarse))
rep('exact-series values (informative): historical, revised', True,
    '%s, %s' % (sp.N(H_exact, 8), sp.N(R_exact, 8)))
mp.mp.dps = 30
Wpp = lambda tv: mp.diff(lambda s: s * mp.cot(pi * s / 2), tv, 2)
supW = max(abs(Wpp(mp.mpf(i) / 200)) for i in range(1, 201))
rep('sup|W\'\'| on (0,1] grid (informative)', supW < 5, mp.nstr(supW, 8))

for st, nm, ex in out:
    print(st, nm, ex)
print('ALL_PASS' if all(s == 'PASS' for s, _, _ in out) else 'SOME_FAIL')
