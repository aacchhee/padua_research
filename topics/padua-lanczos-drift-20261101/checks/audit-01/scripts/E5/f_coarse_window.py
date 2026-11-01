#!/usr/bin/env python3
"""Auditor E5 check F: sign windows of P_n(eta_n(A)) for fixed A (record32 case 3):
finite-n negative points exist on fixed-A paths; eta_n0(a/n0) == zeta_n0."""
import json
import mpmath as mp
mp.mp.dps = 80
a = 20*mp.pi**3/9
def Pe(n, t):
    ax, ay = mp.pi/n + t, mp.pi/(n+1) + t
    g = [mp.cos((n-m)*ax)*mp.cos(m*ay) - mp.cos(m*ax)*mp.cos((n+1-m)*ay) for m in range(4)]
    return 9*(g[1]**2 - g[0]*g[2]/2) + g[2]**2 - g[1]*g[3]
out = {}
for A in ('0.25', '0.5', '1', '2', '5', '10', '17.2', '20'):
    Am = mp.mpf(A)
    neg = [n for n in range(4, 3001) if Pe(n, Am/mp.mpf(n)**3) < 0]
    out[A] = {'negative_n_count_4_3000': len(neg), 'min': min(neg) if neg else None,
              'max': max(neg) if neg else None}
# identity eta_n0(a/n0) = zeta_n0
n0 = 50
out['eta_n0_a_over_n0_equals_zeta_n0_P'] = mp.nstr(Pe(n0, (a/n0)/mp.mpf(n0)**3), 12)
print(json.dumps(out, indent=1))
