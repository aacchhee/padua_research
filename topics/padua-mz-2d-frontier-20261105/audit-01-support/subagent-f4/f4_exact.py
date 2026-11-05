#!/usr/bin/env python3
"""Exact rational checks of the F4 tail bookkeeping (auditor's own code)."""
from fractions import Fraction as F
import math

def t(r):
    return F(2) if r == 0 else F(-4, 4*r*r-1)

ok = True
Rmax = 400
worst_ratio = F(0)
for R in range(1, Rmax+1):
    N = 2*R+1
    S = sum(F(1, 2*i-1) for i in range(1, R+1))
    # direct triangular sum
    ts = [t(r) for r in range(R+1)]
    pref = [F(0)]
    for v in ts:
        pref.append(pref[-1]+v)
    # A_R = sum_r t_r * sum_{s<=R-r} t_s
    A = sum(ts[r]*pref[R-r+1] for r in range(R+1))
    if A != F(8, N*(N+1)) - 16*S/(N*N-1):
        print("A identity FAIL", R); ok = False
    # telescoping partial sums
    if pref[R+1] != F(2, 2*R+1):
        print("telescoping FAIL", R); ok = False
    # absolute triangle
    abs_pref = [F(0)]
    for v in ts:
        abs_pref.append(abs_pref[-1]+abs(v))
    absT = sum(abs(ts[r])*abs_pref[R-r+1] for r in range(R+1))
    # one-dim absolute tail: 4 - sum_{r<=R}|t_r| == 2/N
    if F(4) - abs_pref[R+1] != F(2, N):
        print("1D abs tail FAIL", R); ok = False
    tail = F(16) - absT
    if tail != F(16, N) - A:
        print("tail identity FAIL", R); ok = False
    if absT - A != 16 - F(16, N):
        print("axis change FAIL", R); ok = False
    if not (A >= F(-4, N)):
        print("A>=-4/N FAIL", R); ok = False
    if not (S <= F(R+2, 3) <= F(R*(R+2), N)):
        print("S bound FAIL", R); ok = False
    if not (tail <= F(20, N)):
        print("tail<=20/N FAIL", R); ok = False
    # how tight is A>=-4/N ?
    worst_ratio = max(worst_ratio, -A*N/4)
    # m = 2R (even) and m=2R+1 (odd) both map to R
    for m in (2*R, 2*R+1):
        hm = F(2, 1-m*m) if m % 2 == 0 else F(0)
        exc = 2*abs(hm)
        if m % 2 == 0 and not (exc <= F(8, 3*m)):
            print("exceptional FAIL", m); ok = False
        total = tail + exc
        if not (total <= F(68, 3*m)):
            print("68/(3m) FAIL", m); ok = False
print("exact checks R=1..%d (m=2..%d) ok=%s; max(-A_R*N/4)=%.6f" % (Rmax, 2*Rmax+1, ok, float(worst_ratio)))
# equality cases
print("m=2: tail+exc =", F(16,3)-(F(8,12)-16*F(1)/8) + F(4,3), " 68/6=", F(68,6))
# rational constant check
print("54/5+170/9 =", F(54,5)+F(170,9), float(F(54,5)+F(170,9)))
a = math.pi-4/3
kappa = 0.5+1/math.pi
Cstar = 4*math.sqrt(2)*math.pi/a + 68/3*kappa
print("C* = %.12f; first term %.10f second term %.10f" % (Cstar, 4*math.sqrt(2)*math.pi/a, 68/3*kappa))
print("pi/(pi-4/3)=%.6f <9/5=1.8 ; kappa=%.6f<5/6=%.6f" % (math.pi/a, kappa, 5/6))
