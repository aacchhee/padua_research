# MEASURED: (i) timing of the binary64 evaluator at n=319 (45 S points + 3 lambda points + corner);
# (ii) float-vs-mpmath(40 digits) error of S_n at n=41 vertices, as a check of the float path.
import time, numpy as np
from fractions import Fraction as F
from indep_S import S_n, lambda_phys
from mpmath import mp, mpf, sinpi, cospi, fabs
mp.dps = 40
n = 319
pts = [(F(i, 32), F(j, 32)) for i in range(0, 33, 4) for j in range(0, 33 - i, 4)][:45]
t0 = time.process_time()
for a, b in pts: S_n(n, a, b)
for x, z in [(F(1, 4*n), 0), (0, F(3, 16*(n+1))), (F(1, 4*n), F(3, 16*(n+1)))]: lambda_phys(n, x, z)
print("n=319: %d S points + 3 lambda + corner: CPU %.2fs" % (len(pts), time.process_time() - t0))
def S_mp(n, a, b):
    m = n + 1; tot = mpf(0)
    for r in range(2*n):
        for s in range(2*m):
            if (r + s) % 2 == 0: continue
            # S = pi*((r+a)/n + (s+b)/m)/2, T = pi*((s+b)/m - (r+a)/n)/2 as multiples of pi
            A_ = mpf((r + a).numerator)/(r + a).denominator; B_ = mpf((s + b).numerator)/(s + b).denominator; Sx = (A_/n + B_/m)/2; Tx = (B_/m - A_/n)/2
            def R(k, x):
                sx = sinpi(x)
                if fabs(sx) < mpf(10)**-30:
                    j = int(mp.nint(x)); return k * (1 if (j*(k-1)) % 2 == 0 else -1)
                return sinpi(k*x)/sx
            D = R(n+1, Sx)*R(n+1, Tx) + R(n, Sx)*R(n, Tx)
            tot += fabs(D - (1 if r % 2 == 0 else -1)*cospi(mpf(F(a).numerator)/F(a).denominator))
    return tot/(2*n*m)
t0 = time.process_time(); worst = 0
for a, b in [(F(0), F(0)), (F(1, 32), F(3, 32)), (F(1, 4), F(1, 4)), (F(5, 8), F(1, 8)), (F(1, 2), F(1, 2))]:
    e = abs(mpf(S_n(41, a, b)) - S_mp(41, a, b)); worst = max(worst, e)
print("n=41 float vs mpmath40 max |diff| = %.2e  (CPU %.1fs)" % (float(worst), time.process_time() - t0))
