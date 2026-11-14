# Can the coarse certified input (uc:coarse-input) 9/10<kappa<23/25, C_*<1847/1000
# be proved by a short hand calculation from the paper's own series (uc:kappa-series)?
# [E] exact Fraction enclosure with elementary rational bounds; mpmath only as a cross-check.
from fractions import Fraction as F
import mpmath as mp

# --- elementary rational brackets -------------------------------------------
PI_LO, PI_HI = F(333, 106), F(355, 113)          # classical convergents
def zeta_odd(s, M=12):
    """lower/upper for zeta(s), s>=3 odd: partial sum + integral tails."""
    S = sum(F(1, k**s) for k in range(1, M + 1))
    lo = S + F(1, (s - 1) * (M + 1) ** (s - 1))   # sum_{k>M} k^-s > int_{M+1}^inf
    hi = S + F(1, (s - 1) * M ** (s - 1))         # sum_{k>M} k^-s < int_M^inf
    return lo, hi
def zeta_even(s):
    # zeta(2r) = |B_2r| (2pi)^2r / (2 (2r)!) ; use exact Bernoulli via sympy-free table
    B = {2: F(1, 6), 4: F(1, 30), 6: F(1, 42), 8: F(1, 30), 10: F(5, 66), 12: F(691, 2730)}
    import math
    c = B[s] * F(2 ** s, 2 * math.factorial(s))
    return c * PI_LO ** s, c * PI_HI ** s

def iv_mul(a, b):
    p = [a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1]]
    return min(p), max(p)
def iv_add(a, b): return a[0]+b[0], a[1]+b[1]
def iv_scale(c, a): return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])

def enclose(K):
    a = [(F(1), F(1))]
    acc = (F(0), F(0))
    for p in range(1, K + 1):
        z = zeta_even(2 * p)
        acc = iv_add(acc, iv_scale(F(2, 4 ** p), z))
        a.append((1 - acc[1], 1 - acc[0]))
    z3 = zeta_odd(3)
    b = [iv_scale(F(7, 8), z3)]
    for q in range(1, K + 1):
        zA = zeta_odd(2 * q + 3); zB = zeta_odd(2 * q + 1)
        b.append(iv_add(iv_scale(1 - F(1, 2 ** (2 * q + 3)), zA),
                        iv_scale(-(1 - F(1, 2 ** (2 * q + 1))), zB)))
    S = (F(0), F(0))
    for k in range(K + 1):
        ck = (F(0), F(0))
        for p in range(k + 1):
            ck = iv_add(ck, iv_mul(a[p], b[k - p]))
        S = iv_add(S, iv_scale(F(1, k + 1), ck))
    tail = F(8, 3 * (K + 2) * 4 ** (K + 1))
    pre = (F(8) / PI_HI ** 2, F(8) / PI_LO ** 2)
    kap = iv_mul(pre, S)
    return (kap[0] - tail, kap[1] + tail), a, b

# gamma + log(8/pi) bracket by elementary means (for C_*)
GAM = (F(57721, 100000), F(57722, 100000))
# log(8/pi)=3log2-log(pi); log2 in (0.693147,0.693148); log pi in (1.144729,1.144730)
LOG2 = (F(693147, 10**6), F(693148, 10**6)); LOGPI = (F(1144729, 10**6), F(1144730, 10**6))
d = (GAM[0] + 3*LOG2[0] - LOGPI[1], GAM[1] + 3*LOG2[1] - LOGPI[0])

mp.mp.dps = 40
def kappa_mp():
    f = lambda t: t**2*mp.cot(mp.pi*t/2)*mp.nsum(lambda l: 1/((2*l+1)*((2*l+1)**2-t**2)), [0, mp.inf])
    return 8/mp.pi*mp.quad(f, [0, 0.5, 1])
km = kappa_mp()
dm = mp.euler + mp.log(8/mp.pi)
print('mpmath kappa =', mp.nstr(km, 15), ' C_* =', mp.nstr(4*dm**2/mp.pi**2 + km, 15))
for K in range(1, 7):
    kap, a, b = enclose(K)
    Cs_hi = F(4) * d[1]**2 / PI_LO**2 + kap[1]
    print(f'K={K}: kappa in [{float(kap[0]):.6f},{float(kap[1]):.6f}]',
          ' 9/10<k:', kap[0] > F(9, 10), ' k<23/25:', kap[1] < F(23, 25),
          ' C_*<1847/1000:', Cs_hi < F(1847, 1000), f' C*_hi={float(Cs_hi):.6f}')
for name, (lo, hi) in [('zeta3', zeta_odd(3)), ('zeta5', zeta_odd(5)), ('zeta7', zeta_odd(7)), ('zeta9', zeta_odd(9))]:
    print(name, float(lo), float(hi))
# H0 and j from kappa (uc:origin-identity), to see the margins of (uc:scalar-constants)
k0 = 2*mp.euler + 4*mp.log(2) - 2*mp.log(mp.pi)
H0 = km/2 + 2*k0/mp.pi**2*mp.log(2/mp.pi)
C0 = 2*mp.euler + 4*mp.log(2); bst = C0 - mp.mpf(7)/2
d0 = C0*bst/mp.pi**2; g0 = 4*(mp.log(mp.pi)**2 - mp.log(2)**2)/mp.pi**2
print('H0 =', mp.nstr(H0, 10), ' j =', mp.nstr(H0 + d0 - g0, 10), ' (paper uses j>23/250=0.092)')
