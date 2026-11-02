"""Corrected adaptive-block (theorem 08) MEASURED check: only points satisfying the
theorem's hypotheses (odd representation with rho<=1/8, endpoint distance>=4pi/n)."""
import json, math, sys
import numpy as np
sys.path.insert(0, '.')
import numeric_checks as nc
PI = math.pi
rng = np.random.default_rng(7)
out = []
for n in (48, 49, 64, 65):
    m = n + 1
    C = nc.coef_matrix(n)
    res = {'n': n, 'min_Qv': math.inf, 'min_Qh': math.inf, 'nV': 0, 'nH': 0,
           'min_endpoint_dist_tested_V_over_4pi/n': math.inf, 'min_endpoint_dist_tested_H_over_4pi/n': math.inf}
    Js = [3, 4, 5, n - 5, n - 4, n - 3, n // 2]
    Ks = [3, 4, 5, m - 5, m - 4, m - 3, m // 2]
    for trial in range(220):
        J = int(rng.choice(Js + [int(rng.integers(0, n + 1))]))
        K = int(rng.choice(Ks + [int(rng.integers(0, m + 1))]))
        if (J + K) % 2 == 0:
            K = K + 1 if K < m else K - 1
        rho = 1 / 8 * (1 if trial % 2 == 0 else rng.uniform(0, 1))
        ang = rng.uniform(0, 2 * PI)
        sc = abs(math.cos(ang)) + abs(math.sin(ang))
        al, be = rho * math.cos(ang) / sc, rho * math.sin(ang) / sc
        th, ph = (J * PI + al) / n, (K * PI + be) / m
        if not (0 <= th <= PI and 0 <= ph <= PI):
            continue
        dv, dh = min(ph, PI - ph), min(th, PI - th)
        if dv < 4 * PI / n and dh < 4 * PI / n:
            continue
        lam, S, Qv, Qh = nc.lam_kernel(n, th, ph, C)
        if dv >= 4 * PI / n:
            res['min_Qv'] = min(res['min_Qv'], Qv); res['nV'] += 1
            res['min_endpoint_dist_tested_V_over_4pi/n'] = min(res['min_endpoint_dist_tested_V_over_4pi/n'], dv / (4 * PI / n))
        if dh >= 4 * PI / n:
            res['min_Qh'] = min(res['min_Qh'], Qh); res['nH'] += 1
            res['min_endpoint_dist_tested_H_over_4pi/n'] = min(res['min_endpoint_dist_tested_H_over_4pi/n'], dh / (4 * PI / n))
    res['bound'] = 1 / 1536
    res['pass'] = res['min_Qv'] >= 1 / 1536 and res['min_Qh'] >= 1 / 1536
    out.append(res)
    print(res, file=sys.stderr, flush=True)
print(json.dumps({'kind': 'MEASURED float64 check of theorem 08 under its hypotheses', 'results': out}, indent=1))
