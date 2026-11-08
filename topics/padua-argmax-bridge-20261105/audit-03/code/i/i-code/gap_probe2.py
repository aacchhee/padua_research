"""MEASURED: gap at edge-midpoint odd vertices and a small local search around them."""
import numpy as np, sys, time
from fractions import Fraction as F
from indep_S import lambda_phys, S_n
t0 = time.process_time()
for n in [int(x) for x in sys.argv[1:]]:
    m = n + 1; Lc = S_n(n, 0, 0)
    res = []
    Kc = m // 2
    for J in (0, n):
        for K in range(Kc - 2, Kc + 3):
            if (J + K) % 2 == 1:
                # local search on a 9x9 sub-grid of phase offsets in units of pi/(8n), pi/(8m)
                bestv = -1; bo = None
                for da in range(-4, 5):
                    for db in range(-4, 5):
                        th = F(J, n) + F(da, 16 * n); ph = F(K, m) + F(db, 16 * m)
                        if not (0 <= th <= 1 and 0 <= ph <= 1): continue
                        v = lambda_phys(n, 1 - th, 1 - ph)
                        if v > bestv: bestv, bo = v, (da, db)
                res.append((round(Lc - bestv, 5), J, K, bo))
    res.sort()
    print(f"n={n} Lc={Lc:.5f} best local gaps near edge midpoints: {res[:3]} CPU={time.process_time()-t0:.1f}", flush=True)
