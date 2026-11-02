"""MEASURED check of theorem 10's explicit thin-line constructions with the true polynomial kernel.
For every n in the list, s=1..4, all four orientations, phases on the rho=1/64 diamond boundary (and 0):
verify parity, physical index range, strict band, numerator>=1/32 (via formula (A) numerators),
actual point defect >= m/416 (vertical) or n/416 (horizontal) computed from the polynomial kernel,
and the selected-line lower bound for Qv/Qh >= 1/3328."""
import json, math, sys
import numpy as np
sys.path.insert(0, '.')
import numeric_checks as nc
PI = math.pi
res = []
for n in (48, 49, 50, 51, 64, 97, 128):
    m = n + 1
    C = nc.coef_matrix(n)
    worst = {'n': n, 'min_point_defect_ratio': math.inf, 'min_numerator': math.inf, 'min_selected_Q': math.inf,
             'max_span_times_m_or_n': 0., 'band_fail': 0, 'parity_fail': 0, 'range_fail': 0, 'cases': 0}
    phases = [(0., 0.)] + [((1/64) * math.cos(t) / (abs(math.cos(t)) + abs(math.sin(t))),
                             (1/64) * math.sin(t) / (abs(math.cos(t)) + abs(math.sin(t)))) for t in np.linspace(0, 2*PI, 17)[:-1]]
    for s in (1, 2, 3, 4):
        for orient in ('Vtop', 'Vbot', 'Htop', 'Hbot'):
            for al, be in phases:
                a = (math.cos(al) + math.cos(be)) / 2
                if orient[0] == 'V':
                    ls = [l for l in range(0, n + 1) if n / 4 <= l <= n / 2]
                    if orient == 'Vtop':
                        K = m - s; t = (s * PI - be) / m; phi = PI - t; q = 1 if s % 2 else 0
                    else:
                        K = s; t = (s * PI + be) / m; phi = t; q = 0 if s % 2 else 1
                    Jpar = (1 - K) % 2           # J+K odd
                    tot = 0.
                    for l in ls:
                        k = l + q
                        jp = n - l if orient == 'Vtop' else l
                        if not (1 <= k <= m - 1): worst['range_fail'] += 1
                        if (jp + k - Jpar) % 2: worst['parity_fail'] += 1
                        u = (jp * PI + al) / n
                        b = k * PI / m
                        vp, vm = phi + b, phi - b
                        cu = math.cos(u)
                        lo, hi = sorted((math.cos(vp), math.cos(vm)))
                        if not (lo < cu < hi): worst['band_fail'] += 1
                        worst['max_span_times_m_or_n'] = max(worst['max_span_times_m_or_n'], (hi - lo) * m)
                        for v in (vp, vm):
                            A = a * (1 + math.cos(v)) - .5 * math.sin(al) * math.sin(u) + .5 * math.sin(be) * math.sin(v)
                            worst['min_numerator'] = min(worst['min_numerator'], A)
                        Gp, Gm = nc.G_rhombus(n, np.array([u, u]), np.array([vp, vm]), C)
                        dv = (abs(Gp) + abs(Gm) - abs(Gp + Gm)) / 2
                        worst['min_point_defect_ratio'] = min(worst['min_point_defect_ratio'], dv / (m / 416))
                        tot += dv
                    worst['min_selected_Q'] = min(worst['min_selected_Q'], tot / (n * m) * 3328)
                else:
                    ls = [l for l in range(0, m + 1) if m / 4 <= l <= m / 2]
                    if orient == 'Htop':
                        J = n - s; t = (s * PI - al) / n; th = PI - t; q = -1 if s % 2 else 0
                    else:
                        J = s; t = (s * PI + al) / n; th = t; q = 0 if s % 2 else -1
                    Kpar = (1 - J) % 2
                    tot = 0.
                    for l in ls:
                        j = l + q
                        kp = m - l if orient == 'Htop' else l
                        if not (1 <= j <= n - 1): worst['range_fail'] += 1
                        if (kp + j - Kpar) % 2: worst['parity_fail'] += 1
                        v = (kp * PI + be) / m
                        aj = j * PI / n
                        up, um = th + aj, th - aj
                        cv = math.cos(v)
                        lo, hi = sorted((math.cos(up), math.cos(um)))
                        if not (lo < cv < hi): worst['band_fail'] += 1
                        worst['max_span_times_m_or_n'] = max(worst['max_span_times_m_or_n'], (hi - lo) * n)
                        for u in (up, um):
                            A = a * (1 + math.cos(v)) + .5 * math.sin(be) * math.sin(v) - .5 * math.sin(al) * math.sin(u)
                            worst['min_numerator'] = min(worst['min_numerator'], A)
                        Gp, Gm = nc.G_rhombus(n, np.array([up, um]), np.array([v, v]), C)
                        dh = (abs(Gp) + abs(Gm) - abs(Gp + Gm)) / 2
                        worst['min_point_defect_ratio'] = min(worst['min_point_defect_ratio'], dh / (n / 416))
                        tot += dh
                    worst['min_selected_Q'] = min(worst['min_selected_Q'], tot / (n * m) * 3328)
                worst['cases'] += 1
    worst['pass'] = (worst['band_fail'] == worst['parity_fail'] == worst['range_fail'] == 0 and worst['min_point_defect_ratio'] >= 1
                     and worst['min_numerator'] > 1 / 32 and worst['min_selected_Q'] >= 1 and worst['max_span_times_m_or_n'] < 26)
    res.append(worst)
    print(worst, file=sys.stderr, flush=True)
print(json.dumps({'kind': 'MEASURED float64 check of theorem 10 thin-line constructions (ratios: >=1 means bound holds)', 'results': res}, indent=1))
