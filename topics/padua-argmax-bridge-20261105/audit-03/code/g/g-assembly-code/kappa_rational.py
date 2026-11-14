#!/usr/bin/env python3
"""Independent rigorous check (no Arb, no repository code) of the coarse
PD-T271 input used by the paper: 9/10 < kappa < 23/25 and C_* < 1847/1000,
C_* = 4(gamma+log(8/pi))^2/pi^2 + kappa.  Audit G-assembly.

Method (all exact rationals with outward rounding to a 2^-300 grid):
 * pi: Machin pi=16atan(1/5)-4atan(1/239), alternating-series brackets.
 * zeta(2r): exact Bernoulli formula zeta(2r)=(-1)^(r+1)B_2r(2pi)^2r/(2(2r)!)
   with sympy's exact Bernoulli rationals and the pi bracket.
 * zeta(odd s): sum_{k<=K} k^-s plus convex-tail bounds
   int_{K+1}^inf + f(K+1)/2 <= tail <= int_{K+1/2}^inf.
 * kappa = (8/pi^2) sum_{k>=0} c_k/(k+1), c_k = sum_{p+q=k} a_p b_q,
   |kappa - (8/pi^2) sum_{k<=K}| <= 8/(3(K+2)4^(K+1))  (paper uc:kappa-series;
   derivation re-checked by hand in the audit).
 * gamma: H_K - log(K+1) < gamma < H_K - log(K+1/2)  (elementary monotone
   sequences, proved in the audit report).
 * log z: 2 sum x^(2j+1)/(2j+1), x=(z-1)/(z+1); partial sums are lower
   bounds, tail <= 2 x^(2J+1)/((2J+1)(1-x^2)).
"""
from fractions import Fraction as F
import sympy, json, math
SC = 2 ** 300
def dn(x): return F(math.floor(x * SC), SC)
def up(x): return F(-math.floor(-x * SC), SC)
class I:
    def __init__(s, lo, hi=None):
        hi = lo if hi is None else hi; assert lo <= hi; s.lo, s.hi = dn(F(lo)), up(F(hi))
    def __add__(s, o): o = o if isinstance(o, I) else I(o); return I(s.lo + o.lo, s.hi + o.hi)
    __radd__ = __add__
    def __neg__(s): return I(-s.hi, -s.lo)
    def __sub__(s, o): o = o if isinstance(o, I) else I(o); return I(s.lo - o.hi, s.hi - o.lo)
    def __rsub__(s, o): return I(o) - s
    def __mul__(s, o):
        o = o if isinstance(o, I) else I(o); p = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]; return I(min(p), max(p))
    __rmul__ = __mul__
    def inv(s): assert s.lo > 0 or s.hi < 0; return I(1 / s.hi, 1 / s.lo)
    def __truediv__(s, o): o = o if isinstance(o, I) else I(o); return s * o.inv()
    def __rtruediv__(s, o): return I(o) * s.inv()
    def __pow__(s, k):
        r = I(1)
        for _ in range(k): r = r * s
        return r
    def widen(s, e): return I(s.lo - e, s.hi + e)
    def __repr__(s): return '[%.25f, %.25f]' % (float(s.lo), float(s.hi))

def atan_inv(m, terms=200):
    # alternating series atan(1/m)=sum (-1)^k /((2k+1) m^(2k+1)); bracket by consecutive partial sums
    s = F(0); x = F(1, m)
    for k in range(terms):
        s_prev = s; s += (-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
    return I(min(s, s_prev), max(s, s_prev))
PI = 16 * atan_inv(5) - 4 * atan_inv(239)

def log_series(z):
    z = F(z); assert 1 <= z <= 2
    if z == 1: return I(0)
    x = (z - 1) / (z + 1); s = F(0); J = 120
    for j in range(J): s += 2 * x ** (2 * j + 1) / (2 * j + 1)
    tail = 2 * x ** (2 * J + 1) / ((2 * J + 1) * (1 - x * x))
    return I(s, s + tail)
LOG2 = log_series(2)
def log_I(z):
    z = F(z); assert z > 1
    e = 0
    while z >= 2: z /= 2; e += 1
    return e * LOG2 + log_series(z)
def log_of_interval(iv):
    return I(log_I(iv.lo).lo, log_I(iv.hi).hi)

def zeta_even(r):
    B = sympy.bernoulli(2 * r); B = F(int(B.p), int(B.q))
    return (-1) ** (r + 1) * B * (2 * PI) ** (2 * r) / (2 * math.factorial(2 * r))
def zeta_odd(s, K=400):
    part = sum(F(1, k ** s) for k in range(1, K + 1))
    lo = part + F(1, (s - 1) * (K + 1) ** (s - 1)) + F(1, 2 * (K + 1) ** s)
    hi = part + 1 / ((s - 1) * F(2 * K + 1, 2) ** (s - 1))
    return I(lo, hi)
def zeta(s): return zeta_even(s // 2) if s % 2 == 0 else zeta_odd(s)

KMAX = 24
a = [I(1)]
for p in range(1, KMAX + 1):
    a.append(a[-1] - 2 * zeta(2 * p) / F(4 ** p))
lam = lambda s: (1 - F(1, 2 ** s)) * zeta(s)
b = [F(7, 8) * zeta(3)] + [lam(2 * q + 3) - lam(2 * q + 1) for q in range(1, KMAX + 1)]
S = I(0)
for k in range(KMAX + 1):
    c = I(0)
    for p in range(k + 1): c = c + a[p] * b[k - p]
    S = S + c / F(k + 1)
tail = F(8, 3 * (KMAX + 2) * 4 ** (KMAX + 1))
kappa = (8 / PI ** 2 * S).widen(tail)
Kg = 2000
H = sum(F(1, k) for k in range(1, Kg + 1))
gamma = I((H - log_I(Kg + 1)).lo, (H - log_I(F(2 * Kg + 1, 2))).hi)
l8pi = log_of_interval(8 / PI)
Cstar = 4 * (gamma + l8pi) ** 2 / PI ** 2 + kappa
res = {
    'pi': repr(PI), 'gamma': repr(gamma), 'log8_over_pi': repr(l8pi), 'kappa': repr(kappa), 'C_star': repr(Cstar),
    'kappa_gt_9_10': kappa.lo > F(9, 10), 'kappa_lt_23_25': kappa.hi < F(23, 25),
    'Cstar_lt_1847_1000': Cstar.hi < F(1847, 1000),
    'kappa_in_PDT271_decimal': (kappa.lo < F('0.919710118388492535099518225791') and kappa.hi > F('0.919710118388492535099518225790')),
    'Cstar_overlaps_PDT271_decimal': (Cstar.lo < F('1.846160310423926079759838737948') and Cstar.hi > F('1.846160310423926079759838737947')),
    'Cstar_gt_4383_2420': Cstar.lo > F(4383, 2420),
}
print(json.dumps(res, indent=1))
