"""Elementary exact-rational enclosure of the coarse constant input (paper uc:coarse-input):
   9/10 < kappa < 23/25 and C_* = 4(gamma+log(8/pi))^2/pi^2 + kappa < 1847/1000,
using ONLY the paper's series (uc:kappa-series) with its stated tail 8/(3(K+2)4^(K+1)),
rational pi bracket, elementary zeta(odd)/zeta(even) brackets, gamma and log brackets.
No Arb/MPFR/mpmath: Python Fractions only. Interval = (lo, hi) pairs of Fractions."""
from fractions import Fraction as F
import sys
K = int(sys.argv[1]) if len(sys.argv) > 1 else 6
M = int(sys.argv[2]) if len(sys.argv) > 2 else 60       # partial-sum length for zeta
PI = (F(333, 106), F(355, 113))                          # 333/106 < pi < 355/113 (classical)
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[1], -x[0])
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    p = [x[0]*y[0], x[0]*y[1], x[1]*y[0], x[1]*y[1]]; return (min(p), max(p))
def sc(c, x): return (min(c*x[0], c*x[1]), max(c*x[0], c*x[1]))
def inv(x):
    assert x[0] > 0 or x[1] < 0; return (1/x[1], 1/x[0])
def powi(x, k):
    r = (F(1), F(1))
    for _ in range(k): r = mul(r, x)
    return r
def zeta(s):
    """sum_{k<=M} k^-s + tail; integral comparison of decreasing k^-s:
       int_{M+1}^inf <= tail <= int_M^inf."""
    ps = sum(F(1, k**s) for k in range(1, M+1))
    lo = ps + F(1, (s-1)*(M+1)**(s-1)); hi = ps + F(1, (s-1)*M**(s-1))
    return (lo, hi)
# a_p = 1 - 2 sum_{r<=p} zeta(2r)/4^r  ;  b_0 = 7 zeta(3)/8 ; b_q = (1-2^{-2q-3})zeta(2q+3)-(1-2^{-2q-1})zeta(2q+1)
Z = {s: zeta(s) for s in range(2, 2*K+4)}
a = [(F(1), F(1))]
acc = (F(0), F(0))
for p in range(1, K+1):
    acc = add(acc, sc(F(1, 4**p), Z[2*p])); a.append(sub((F(1), F(1)), sc(F(2), acc)))
b = [sc(F(7, 8), Z[3])]
for q in range(1, K+1):
    b.append(sub(sc(1-F(1, 2**(2*q+3)), Z[2*q+3]), sc(1-F(1, 2**(2*q+1)), Z[2*q+1])))
S = (F(0), F(0))
for k in range(K+1):
    ck = (F(0), F(0))
    for p in range(k+1): ck = add(ck, mul(a[p], b[k-p]))
    S = add(S, sc(F(1, k+1), ck))
tail = F(8, 3*(K+2)*4**(K+1))
kap = add(mul(sc(F(8), inv(powi(PI, 2))), S), (-tail, tail))
# gamma: H_M - log M - 1/(2M) < gamma < H_M - log M - 1/(2M) + 1/(8M^2)  (trapezoid/Euler-Maclaurin, elementary)
# log via atanh series: log x = 2 sum atanh((x-1)/(x+1)) terms; bracket with geometric tail.
def log_rat(x, T=40):
    x = F(x); z = (x-1)/(x+1); s = F(0)
    for i in range(T): s += z**(2*i+1)/(2*i+1)
    t = abs(z)**(2*T+1)/((2*T+1)*(1-z*z))
    lo, hi = 2*s, 2*s
    return (lo - 2*t, hi + 2*t) if z >= 0 else (lo - 2*t, hi + 2*t)
Mg = 64
H = sum(F(1, k) for k in range(1, Mg+1))
l2 = log_rat(2)
lM = (6*l2[0], 6*l2[1])  # Mg=64
gam = (H - lM[1] - F(1, 2*Mg), H - lM[0] - F(1, 2*Mg) + F(1, 8*Mg*Mg))
l4pi = (log_rat(4/PI[1])[0], log_rat(4/PI[0])[1])
l8pi = (l2[0]+l4pi[0], l2[1]+l4pi[1])
d = add(gam, l8pi)
Cst = add(sc(F(4), mul(mul(d, d), inv(powi(PI, 2)))), kap)
f = lambda x: (float(x[0]), float(x[1]))
print("K=%d M=%d" % (K, M))
print("kappa in", f(kap), " width %.2e" % float(kap[1]-kap[0]))
print("C_* in", f(Cst))
print("9/10<kappa:", kap[0] > F(9, 10), " kappa<23/25:", kap[1] < F(23, 25), " C_*<1847/1000:", Cst[1] < F(1847, 1000))
print("H0>7/25 needs kappa > ", end="")
# H0 = kappa/2 + (2k0/pi^2) log(2/pi); paper uses 161/100<k0<9/5, log(pi/2)<23/50 -> H0 > kappa/2 - (2*9/5/(197/20))*23/50
print(float(2*(F(7, 25) + F(2)*F(9, 5)/F(197, 20)*F(23, 50))))
