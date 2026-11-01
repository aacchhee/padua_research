"""Separate algorithmic error of the Q-free downdate from the intrinsic conditioning of
(nodes,weights) -> (Hx,Hy): perturb nodes by 1e-14 (relative) and recompute from scratch."""
import numpy as np
from qfree_bivariate_downdate import ref_H, modify
rng = np.random.default_rng(0)
for (W, n, steps) in [(400, 12, 400), (150, 12, 400), (100, 12, 400), (95, 12, 200)]:
    M = W + steps; pts = rng.uniform(-1, 1, (M, 2)); w = rng.uniform(0.5, 1.5, M)
    Hx, Hy = ref_H(pts[:W], w[:W], n); sw = w[:W].sum(); gaps = []
    for k in range(steps):
        Hx, Hy, sw, _ = modify(Hx, Hy, sw, pts[W + k], w[W + k], n, +1)
        Hx, Hy, sw, lev = modify(Hx, Hy, sw, pts[k], w[k], n, -1); gaps.append(1 - lev)
    P, ww = pts[steps:], w[steps:]
    Rx, Ry = ref_H(P, ww, n)
    err = max(abs(Hx - Rx).max(), abs(Hy - Ry).max())
    sens = 0
    for t in range(5):
        Rx2, Ry2 = ref_H(P * (1 + 1e-14 * rng.standard_normal(P.shape)), ww, n)
        sens = max(sens, abs(Rx2 - Rx).max(), abs(Ry2 - Ry).max())
    g = np.array(gaps)
    print(f"W={W} N=91: final err {err:.1e}; ref sensitivity to 1e-14 node noise {sens:.1e}; "
          f"min(1-lev)={g.min():.1e}; sum log10(1/(1-lev))={np.log10(1/g).sum():.1f}")
