"""MEASURED: physical four-copy majorant S(theta,phi) equals the odd-board primitive S_n(alpha,beta)
for EVERY odd-vertex representation of the point (used by theorems 09/11); also lambda<=S."""
import json, math, sys
import numpy as np
sys.path.insert(0, '.')
import numeric_checks as nc
PI = math.pi
rng = np.random.default_rng(11)
out = []
for n in (2, 3, 5, 6, 9, 12):
    m = n + 1
    C = nc.coef_matrix(n)
    worst = 0.; worst_rho = 0.; minDelta = math.inf; reps_checked = 0
    for _ in range(25):
        th, ph = rng.uniform(0, PI, 2)
        if _ < 3:
            th, ph = [(0., PI / 2), (PI, rng.uniform(0, PI)), (PI / n, 0.)][_]
        lam, S, Qv, Qh = nc.lam_kernel(n, th, ph, C)
        minDelta = min(minDelta, S - lam)
        J0 = min(int(th * n / PI), n - 1); K0 = min(int(ph * m / PI), m - 1)
        best = math.inf
        for J in (J0, J0 + 1):
            for K in (K0, K0 + 1):
                if (J + K) % 2 == 0:
                    continue
                al, be = n * th - J * PI, m * ph - K * PI
                rho = abs(al) + abs(be)
                best = min(best, rho)
                Sp = nc.S_primitive(n, al, be, C)
                worst = max(worst, abs(Sp - S)); reps_checked += 1
        worst_rho = max(worst_rho, best)
    out.append({'n': n, 'max_|S_phys - S_odd_board|': worst, 'reps_checked': reps_checked,
                'max_min_rho_over_pi': worst_rho / PI, 'min_Delta': minDelta})
    print(out[-1], file=sys.stderr)
print(json.dumps(out, indent=1))
