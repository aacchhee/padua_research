"""Rerun of the S_n scan with collision-safe offsets (MEASURED). See check_regions.py."""
import math, time, numpy as np
from check_regions import S_n, lam_corner
t0 = time.process_time()
for n in [192, 320]:
    Lc = lam_corner(n)
    worst = {'wide: S-Lc-P(rho), rho<=1': -1e9, 'outer: S-Lc+13/500, 1<=rho<=pi': -1e9, 'far: S-Lc+3/100, pi/2<=rho<=pi': -1e9}
    xs = np.linspace(0.0031, math.pi - 0.0027, 72)
    for x in xs:
        for y in xs:
            rho = x + y
            if rho > math.pi: continue
            val = S_n(n, x, y) - Lc
            if rho <= 1: worst['wide: S-Lc-P(rho), rho<=1'] = max(worst['wide: S-Lc-P(rho), rho<=1'], val - (141/10000 + 257/400*rho - 61/50*rho**2))
            if rho >= 1: worst['outer: S-Lc+13/500, 1<=rho<=pi'] = max(worst['outer: S-Lc+13/500, 1<=rho<=pi'], val + 13/500)
            if rho >= math.pi/2: worst['far: S-Lc+3/100, pi/2<=rho<=pi'] = max(worst['far: S-Lc+3/100, pi/2<=rho<=pi'], val + 3/100)
    print('n=%d Lc=%.6f' % (n, Lc), {k: round(v, 5) for k, v in worst.items()}, '(all must be <0)')
print('cpu_s', time.process_time() - t0)
