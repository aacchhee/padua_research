"""MEASURED: full-square scan of lambda_n on a grid of resolution 1/res mesh cell; reports
the largest values outside the two maximizing corner cells (excluded box: one mesh cell)."""
import numpy as np, sys, time
from fractions import Fraction as F
from indep_S import lambda_phys, S_n
n = int(sys.argv[1]); res = int(sys.argv[2]); m = n + 1
t0 = time.process_time(); Lc = S_n(n, 0, 0)
vals = []
for i in range(n * res + 1):
    th = F(i, n * res)
    for k in range(m * res + 1):
        ph = F(k, m * res)
        # corners theta=pi (x=-1): (th=1,ph=1)=(-1,-1); even n: (th=0,ph=1)=(1,-1); odd: (th=1,ph=0)=(-1,1)
        corners = [(1, 1), (0, 1)] if n % 2 == 0 else [(1, 1), (1, 0)]
        if any(abs(th - c[0]) <= F(1, n) and abs(ph - c[1]) <= F(1, m) for c in corners): continue
        vals.append((lambda_phys(n, 1 - th, 1 - ph), th, ph))
vals.sort(key=lambda t: -t[0])
print(f"n={n} res={res} Lc={Lc:.6f} points={len(vals)} CPU={time.process_time()-t0:.1f}")
for v, th, ph in vals[:5]:
    print(f"   gap={Lc - v:.5f} at theta/pi={float(th):.4f} (J~{float(th)*n:.2f}), phi/pi={float(ph):.4f} (K~{float(ph)*m:.2f})")
