"""MEASURED: isolation gap of the corner maximum. For each n, evaluate lambda_n on a
fine physical-angle grid (theta,phi) in the corner region and on odd mesh vertices
globally (small n), report the largest value outside the corner patch of radius c/n."""
import numpy as np, sys, time
from fractions import Fraction as F
from indep_S import lambda_phys, S_n
def lam_angles(n, th, ph):  # th, ph as Fractions of pi; z=(cos(pi th), cos(pi ph))
    return lambda_phys(n, 1 - F(th), 1 - F(ph))
t0 = time.process_time()
for n in [int(x) for x in sys.argv[1:]]:
    m = n + 1
    Lc = S_n(n, 0, 0)
    best = []
    # odd vertices (J,K), J+K odd, physical point (cos(J pi/n), cos(K pi/m)); all of them for small n
    for J in range(n + 1):
        for K in range(m + 1):
            if (J + K) % 2 == 1:
                v = lam_angles(n, F(J, n), F(K, m))
                best.append((v, J, K))
    best.sort(reverse=True)
    top = [(round(Lc - v, 5), J, K) for v, J, K in best[:6]]
    print(f"n={n} Lambda_c={Lc:.6f}  gaps at top odd vertices (gap,J,K): {top}  CPU={time.process_time()-t0:.1f}")
