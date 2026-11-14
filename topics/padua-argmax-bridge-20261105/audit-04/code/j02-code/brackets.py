#!/usr/bin/env python3
"""Claude audit-04 (J2): independent rigorous brackets for J02's consumed constants.

Independent of topics/.../code/onset512_analytic/check.py: own interval class
(integer dyadic endpoints, P-bit grid, directed rounding), different series and
cutoffs:
  pi    : Hutton  pi/4 = 2 atan(1/3) + atan(1/7), alternating remainders
  log 2 : -log(1-1/2) = sum 1/(k 2^k), positive-tail bound 1/((K+1) 2^K)
  log w : 2 atanh((w-1)/(w+1)) with geometric tail (used for log 3/2, log(pi/3), ...)
  gamma : H_M - log M - 1/(2M) <= gamma <= H_M - log M - 1/(2(M+1))   (trapezoid /
          midpoint convexity of 1/t; derivation in j02-constants.md), M = 1000
  zeta  : sum_{k<=m} k^-s + [ (m+1)^(1-s), m^(1-s) ]/(s-1)  (monotone integral test)
  kappa : J02/PD-T269 series with K = 14 and the analytic tail 8/(3(K+2)4^(K+1));
          also K = 3 to reproduce the developer interval.
No floating point and no mpmath in this file.
"""
from fractions import Fraction as Fr
from math import isqrt
import json, sys

P = 320                     # grid 2^-P
ONE = 1 << P


def fl(x):                  # floor(x * 2^P) for Fraction/int x
    x = Fr(x)
    return (x.numerator << P) // x.denominator


def ce(x):
    return -fl(-Fr(x))


class D:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi):         # integer endpoints on the 2^-P grid
        assert lo <= hi, (lo, hi)
        self.lo, self.hi = lo, hi

    @staticmethod
    def of(a, b=None):
        b = a if b is None else b
        return D(fl(a), ce(b))

    def __add__(s, o):
        o = cv(o); return D(s.lo + o.lo, s.hi + o.hi)
    __radd__ = __add__

    def __neg__(s):
        return D(-s.hi, -s.lo)

    def __sub__(s, o):
        return s + (-cv(o))

    def __rsub__(s, o):
        return cv(o) - s

    def __mul__(s, o):
        o = cv(o)
        pr = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]
        return D(min(pr) >> P, -((-max(pr)) >> P))
    __rmul__ = __mul__

    def inv(s):
        assert s.lo > 0 or s.hi < 0, 'division by interval containing 0'
        N = 1 << (2 * P)
        lo = N // s.hi            # floor(2^2P / hi)  (valid for both sign cases)
        hi = -((-N) // s.lo)      # ceil(2^2P / lo)
        return D(min(lo, hi), max(lo, hi))

    def __truediv__(s, o):
        return s * cv(o).inv()

    def __rtruediv__(s, o):
        return cv(o) * s.inv()

    def sq(s):                    # tight square
        if s.lo >= 0:
            return s * s
        if s.hi <= 0:
            return (-s) * (-s)
        m = max(-s.lo, s.hi)
        return D(0, -((-(m * m)) >> P))

    def sqrt(s):
        assert s.lo >= 0
        lo = isqrt(s.lo << P)
        n = s.hi << P
        hi = isqrt(n)
        if hi * hi < n:
            hi += 1
        return D(lo, hi)

    def flo(s):
        return Fr(s.lo, ONE)

    def fhi(s):
        return Fr(s.hi, ONE)

    def hull(s, o):
        return D(min(s.lo, o.lo), max(s.hi, o.hi))

    def __repr__(s):
        return '[%.15f, %.15f]' % (s.lo / ONE, s.hi / ONE)


def cv(x):
    return x if isinstance(x, D) else D.of(x)


def lt(iv, q):                    # certified  iv < q   (upper end below q)
    return iv.hi * Fr(q).denominator < Fr(q).numerator * ONE and Fr(iv.hi, ONE) < q


def gt(iv, q):                    # certified  iv > q
    return Fr(iv.lo, ONE) > q


# ---------------- pi (Hutton) ----------------
def atan_recip(q, N):
    """atan(1/q) for integer q>=2 by N terms; remainder bounded by the next term."""
    s = D(0, 0)
    for k in range(N):
        t = D.of(Fr(1, (2 * k + 1) * q ** (2 * k + 1)))
        s = s + t if k % 2 == 0 else s - t
    nxt = Fr(1, (2 * N + 1) * q ** (2 * N + 1))
    return D(s.lo - ce(nxt), s.hi + ce(nxt))


PI = 4 * (2 * atan_recip(3, 110) + atan_recip(7, 70))

# ---------------- logarithms ----------------
def log2_series(K):
    s = D(0, 0)
    for k in range(1, K + 1):
        s = s + D.of(Fr(1, k * 2 ** k))
    tail = Fr(1, (K + 1) * 2 ** K)
    return D(s.lo, s.hi + ce(tail))


LOG2 = log2_series(400)


def atanh2_rational(x, K):
    """2*atanh(x) for rational 0<=x<1 with K terms and geometric tail."""
    x = Fr(x)
    assert 0 <= x < 1
    s = D(0, 0)
    xp = x
    for k in range(K):
        s = s + D.of(2 * xp / (2 * k + 1))
        xp *= x * x
    tail = 2 * xp / ((2 * K + 1) * (1 - x * x))   # xp = x^(2K+1)
    return D(s.lo, s.hi + ce(tail))


def log_rational(z):
    """log of a positive rational z: z = 2^e * w, w in [2/3, 4/3), atanh of (w-1)/(w+1)."""
    z = Fr(z)
    assert z > 0
    e = 0
    while z >= Fr(4, 3):
        z /= 2; e += 1
    while z < Fr(2, 3):
        z *= 2; e -= 1
    x = (z - 1) / (z + 1)                # |x| <= 1/7
    if x >= 0:
        core = atanh2_rational(x, 130)
    else:
        core = -atanh2_rational(-x, 130)
    return e * LOG2 + core


def log_iv(iv):                          # monotone: evaluate at both endpoints
    return D(log_rational(iv.flo()).lo, log_rational(iv.fhi()).hi)


LOGPI = log_iv(PI)

# ---------------- zeta and gamma ----------------
def zeta(s, m=3000):
    part = D(0, 0)
    for k in range(1, m + 1):
        part = part + D.of(Fr(1, k ** s))
    lo = Fr(1, (s - 1) * (m + 1) ** (s - 1))
    hi = Fr(1, (s - 1) * m ** (s - 1))
    return D(part.lo + fl(lo), part.hi + ce(hi))


def euler_gamma(M=1000):
    H = D(0, 0)
    for k in range(1, M + 1):
        H = H + D.of(Fr(1, k))
    base = H - log_rational(M)
    return D((base - Fr(1, 2 * M)).lo, (base - Fr(1, 2 * (M + 1))).hi)


GAMMA = euler_gamma(1000)

# ---------------- kappa ----------------
ZCACHE = {}


def Z(s):
    if s not in ZCACHE:
        ZCACHE[s] = zeta(s)
    return ZCACHE[s]


def kappa(K):
    a = [D.of(1)]
    for p in range(1, K + 1):
        a.append(a[-1] - 2 * Z(2 * p) / (4 ** p))
    b = [Fr(7, 8) * Z(3)]
    for q in range(1, K + 1):
        b.append((1 - Fr(1, 2 ** (2 * q + 3))) * Z(2 * q + 3)
                 - (1 - Fr(1, 2 ** (2 * q + 1))) * Z(2 * q + 1))
    S = D(0, 0)
    cks = []
    for k in range(K + 1):
        ck = D(0, 0)
        for p in range(k + 1):
            ck = ck + a[p] * b[k - p]
        cks.append(ck)
        S = S + ck / (k + 1)
    tail = Fr(8, 3 * (K + 2) * 4 ** (K + 1))
    kap = 8 * S / PI.sq()
    return D(kap.lo - ce(tail), kap.hi + ce(tail)), a, b, cks


def main():
    out = {}
    chk = []

    def C(name, ok):
        chk.append((name, bool(ok)))

    KAP, a, b, cks = kappa(14)
    KAP3 = kappa(3)[0]
    C0 = 2 * GAMMA + 4 * LOG2
    k0 = C0 - 2 * LOGPI
    LOGPI2 = LOGPI - LOG2
    c1 = 2 * (GAMMA + 3 * LOG2 - LOGPI) / PI
    CSTAR = c1.sq() + KAP
    PI2 = PI.sq()
    d0 = C0 * (C0 - Fr(7, 2)) / PI2
    g0 = 4 * (LOGPI.sq() - LOG2.sq()) / PI2
    H0 = KAP / 2 - (2 * k0 / PI2) * LOGPI2
    j = H0 + d0 - g0
    t0 = 2 * LOG2 / PI
    Cinf_bound = CSTAR - j / 2 + (j.sq() / 4 + t0.sq()).sqrt()

    for nm, v in [('pi', PI), ('log2', LOG2), ('logpi', LOGPI), ('gamma', GAMMA),
                  ('kappa_K14', KAP), ('kappa_K3', KAP3), ('C0', C0), ('k0', k0),
                  ('c1', c1), ('Cstar', CSTAR), ('d0', d0), ('g0', g0), ('H0', H0),
                  ('j', j), ('t0', t0), ('Cinf_upper_bound', Cinf_bound)]:
        out[nm] = repr(v)
        out[nm + '_width'] = '%.3e' % ((v.hi - v.lo) / ONE)

    # ---- consumed inequalities of J02 (1) and the C_infinity consequence ----
    C('kappa > 9/10', gt(KAP, Fr(9, 10)))
    C('j > 23/250', gt(j, Fr(23, 250)))
    C('t0 > 0', gt(t0, 0))
    C('t0 < 221/500', lt(t0, Fr(221, 500)))
    C('Cstar < 4629/2500', lt(CSTAR, Fr(4629, 2500)))
    C('C_inf <= Cstar - j/2 + sqrt(j^2/4+t0^2) < 9/4', lt(Cinf_bound, Fr(9, 4)))
    # ---- J02 (9) inputs ----
    C('23/40 < gamma < 3/5', gt(GAMMA, Fr(23, 40)) and lt(GAMMA, Fr(3, 5)))
    C('69/100 < log2 < 6932/10000', gt(LOG2, Fr(69, 100)) and lt(LOG2, Fr(6932, 10000)))
    C('log pi < 23/20', lt(LOGPI, Fr(23, 20)))
    C('161/100 < k0 < 9/5', gt(k0, Fr(161, 100)) and lt(k0, Fr(9, 5)))
    C('0 < log(pi/2) < 23/50', gt(LOGPI2, 0) and lt(LOGPI2, Fr(23, 50)))
    C('157/50 < pi < 22/7', gt(PI, Fr(157, 50)) and lt(PI, Fr(22, 7)))
    C('197/20 < pi^2 < 10', gt(PI2, Fr(197, 20)) and lt(PI2, 10))
    # ---- intermediate rational claims of J02 sec. 4 / paper uc:scalar-constants ----
    C('H0 > 7/25 (direct)', gt(H0, Fr(7, 25)))
    C('d0 > 39/250 (direct)', gt(d0, Fr(39, 250)))
    C('g0 < 43/125 (direct)', lt(g0, Fr(43, 125)))
    C('C0 > 39/10 and C0-7/2 > 2/5', gt(C0, Fr(39, 10)) and gt(C0 - Fr(7, 2), Fr(2, 5)))
    # exact rational steps of the written proof (from the coarse inputs only)
    C('[exact] 2*23/40+4*69/100 > 39/10', 2 * Fr(23, 40) + 4 * Fr(69, 100) > Fr(39, 10))
    C('[exact] (39/10)(2/5)/10 = 39/250', Fr(39, 10) * Fr(2, 5) / 10 == Fr(39, 250))
    C('[exact] 2*(9/5)/(197/20)*(23/50) = 828/4925',
      2 * Fr(9, 5) / Fr(197, 20) * Fr(23, 50) == Fr(828, 4925))
    C('[exact] 9/20-828/4925 > 7/25', Fr(9, 20) - Fr(828, 4925) > Fr(7, 25))
    C('[exact] (80/197)((23/20)^2-(69/100)^2) < 43/125',
      Fr(80, 197) * (Fr(23, 20) ** 2 - Fr(69, 100) ** 2) < Fr(43, 125))
    C('[exact] 7/25+39/250-43/125 = 23/250', Fr(7, 25) + Fr(39, 250) - Fr(43, 125) == Fr(23, 250))
    C('[exact] 9/4-4629/2500 = 249/625', Fr(9, 4) - Fr(4629, 2500) == Fr(249, 625))
    C('[exact] (249/625)^2+(249/625)(23/250)-(221/500)^2 = 71/6250000',
      Fr(249, 625) ** 2 + Fr(249, 625) * Fr(23, 250) - Fr(221, 500) ** 2 == Fr(71, 6250000))
    C('[exact] 2*(69/100+... ) t0 coarse: 2*(6932/10000)/(157/50) < 221/500',
      2 * Fr(6932, 10000) / Fr(157, 50) < Fr(221, 500))
    C('[exact] k0 lower from coarse: 2*23/40+4*69/100-2*23/20 = 161/100',
      2 * Fr(23, 40) + 4 * Fr(69, 100) - 2 * Fr(23, 20) == Fr(161, 100))
    # ---- paper display claims (comparison-unified.tex 520-526) ----
    C('917166/10^6 < kappa < 921489/10^6', gt(KAP, Fr(917166, 10 ** 6)) and lt(KAP, Fr(921489, 10 ** 6)))
    C('Cstar < 1847940/10^6', lt(CSTAR, Fr(1847940, 10 ** 6)))
    # ---- K = 3 developer interval contains the K=14 interval's centre region ----
    C('K3 interval overlaps K14 interval', KAP3.lo <= KAP.hi and KAP.lo <= KAP3.hi)
    C('K3 lower > 9/10', gt(KAP3, Fr(9, 10)))
    # ---- coefficient majorants used by the tail bound (finite p,q only) ----
    C('0 < a_p <= 4^-p, p=0..10 (resolvable at this zeta precision; all p in mp_cross.py)', all(gt(a[p], 0) and lt(a[p], Fr(1, 4 ** p) + Fr(1, 10 ** 30)) for p in range(11)))
    C('0 < b_0 < 10/9', gt(b[0], 0) and lt(b[0], Fr(10, 9)))
    C('|b_q| < 9^-q, q=1..14', all(lt(b[q], 0) and gt(b[q], -Fr(1, 9 ** q)) for q in range(1, 15)))
    C('|c_k| < 2*4^-k, k=0..12 (resolvable; all k in mp_cross.py)', all(lt(cks[k], Fr(2, 4 ** k)) and gt(cks[k], -Fr(2, 4 ** k)) for k in range(13)))
    # ---- other elementary constants consumed in the same paper lemmas ----
    C('3/2 < gamma+log(8/pi) < 8/5', gt(GAMMA + 3 * LOG2 - LOGPI, Fr(3, 2)) and lt(GAMMA + 3 * LOG2 - LOGPI, Fr(8, 5)))
    w = Fr(17, 39)
    C('[exact] 2(w+w^3/3) > 37/40, w=17/39 (log(28/11)>37/40)', 2 * (w + w ** 3 / 3) > Fr(37, 40))
    C('log pi > 11/10 (companion; needed for J_0>1/pi)', gt(LOGPI, Fr(11, 10)))
    C('J_0 = 2(log pi - gamma)/pi > 1/pi', gt(LOGPI - GAMMA, Fr(1, 2)))
    C('lambda_0 = (2/pi)log(4/pi) < 1/(2 pi)', lt(2 * LOG2 - LOGPI, Fr(1, 4)))
    C('zeta(3) < 5/4 and 28 zeta(3)-16 < 19', lt(Z(3), Fr(5, 4)) and lt(28 * Z(3) - 16, 19))
    kk = 2 * GAMMA - 2 * LOGPI
    C('frak k = 2gamma-2log pi < -1 and -frak k < 5/4', lt(kk, -1) and lt(-kk, Fr(5, 4)))
    C('k0 > pi/2 and k0 < 2', gt(k0 - PI / 2, 0) and lt(k0, 2))
    C('4*I4/pi^2 < 9/25 with I4<319/360', lt(4 * Fr(319, 360) / PI2, Fr(9, 25)))

    out['checks'] = chk
    out['all_pass'] = all(ok for _, ok in chk)
    out['K14_tail'] = '%.3e' % float(Fr(8, 3 * 16 * 4 ** 15))
    out['grid_bits'] = P
    print(json.dumps(out, indent=1))
    return 0 if out['all_pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
