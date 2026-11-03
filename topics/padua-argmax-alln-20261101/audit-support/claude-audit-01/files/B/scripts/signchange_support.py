"""MEASURED: on the regular physical odd mesh, pairs whose (A)-numerator is negative satisfy
y <= C(rho+sqrt(rho x)) (gated-03 (10)), and y/rho is NOT bounded (an O(rho)-width band is false)."""
import numpy as np, json
out = []
for n in (200, 801):
    m = n+1
    j, r = np.meshgrid(np.arange(n+1), np.arange(m+1), indexing='ij')
    odd = ((j + r) % 2 == 1) & ~((r == j + 1) & (j >= 2*n/3))
    j, r = j[odd], r[odd]
    for rho in (1e-1, 1e-2, 1e-3):
        best = {'n': n, 'rho': rho, 'max_y_over_rho_plus_sqrt': 0., 'max_y_over_rho': 0., 'count_negative': 0}
        for (al, be) in ((rho, 0.), (-rho, 0.), (rho/2, rho/2), (rho/2, -rho/2), (0., rho), (0., -rho)):
            u = j*np.pi/n + al/n; v = r*np.pi/m + be/m
            A = (np.cos(al)+np.cos(be))/2*(1+np.cos(v)) - np.sin(al)/2*np.sin(u) + np.sin(be)/2*np.sin(v)
            neg = A < 0
            x = np.pi - j[neg]*np.pi/n; y = np.pi - r[neg]*np.pi/m
            best['count_negative'] += int(neg.sum())
            if neg.any():
                best['max_y_over_rho_plus_sqrt'] = max(best['max_y_over_rho_plus_sqrt'], float(np.max(y/(rho + np.sqrt(rho*x)))))
                best['max_y_over_rho'] = max(best['max_y_over_rho'], float(np.max(y/rho)))
        out.append(best)
print(json.dumps(out, indent=1))
