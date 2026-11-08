# Tight elementary zeta bounds (convexity: trapezoid/midpoint tails), then which K closes
# the inequalities ACTUALLY consumed downstream: kappa>9/10 (=> j>23/250) and C_*<c_crit,
# where c_crit is what C_infty<9/4 needs: delta=9/4-C_*, delta^2+delta*j>t0^2 with j>23/250,t0<221/500.
from fractions import Fraction as F
import math, mpmath as mp
import kappa_hand as kh
def zeta_odd(s, M=10):
    S = sum(F(1, k**s) for k in range(1, M + 1))
    lo = S + F(1, (s-1)*M**(s-1)) - F(1, 2*M**s)          # trapezoid (convex) lower
    hi = S + F(2**(s-1), (s-1)*(2*M+1)**(s-1))             # midpoint (convex) upper
    return lo, hi
kh.zeta_odd = zeta_odd
# critical C_*: smallest delta with delta^2 + (23/250)delta > (221/500)^2
j, t0 = F(23,250), F(221,500)
dcrit = (-j + mp.sqrt(j**2 + 4*t0**2))/2
print('C_infty<9/4 needs C_* <', mp.nstr(mp.mpf(9)/4 - dcrit, 8))
for K in (2, 3, 4):
    kap, a, b = kh.enclose(K)
    Cs_hi = F(4)*kh.d[1]**2/kh.PI_LO**2 + kap[1]
    print(f'K={K}: kappa in [{float(kap[0]):.6f},{float(kap[1]):.6f}]  kappa>9/10: {kap[0]>F(9,10)}'
          f'  C*_hi={float(Cs_hi):.6f}  C*<1849/1000: {Cs_hi<F(1849,1000)}  C*<1847/1000: {Cs_hi<F(1847,1000)}')
for s in (3,5,7,9): lo,hi=zeta_odd(s); print(f'zeta({s}) in [{float(lo):.9f},{float(hi):.9f}]')
# paper's coefficient bound |c_k|<=2*4^-k: numerical check
mp.mp.dps=30
def ak(p): return 1-2*sum(mp.zeta(2*r)/4**r for r in range(1,p+1))
def bk(q): return 7*mp.zeta(3)/8 if q==0 else (1-mp.mpf(2)**(-2*q-3))*mp.zeta(2*q+3)-(1-mp.mpf(2)**(-2*q-1))*mp.zeta(2*q+1)
c=[sum(ak(p)*bk(k-p) for p in range(k+1)) for k in range(25)]
print('max_k |c_k|4^k/2 =', mp.nstr(max(abs(c[k])*4**k/2 for k in range(25)),6), ' series kappa =', mp.nstr(8/mp.pi**2*sum(c[k]/(k+1) for k in range(25)),12))
