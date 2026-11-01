#!/usr/bin/env python3
"""Auditor E5 check D (optional, beyond the claim): ball-arithmetic (Arb via
python-flint) sign of P_n(zeta_n) and enclosure of |zeta_n - z_(1,1)| for
n = 4..NMAX.  Uses T_j(cos psi) = cos(j psi) with psi = pi/n + a/n^4 in [0, pi].
Rigorous modulo trust in Arb; this is NOT part of the developer's claim (the
record claims no finite threshold) and is reported only as a finite check.
"""
import json, sys
import flint
from flint import arb

flint.ctx.prec = 400
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 300
pi = arb.pi()
a = 20*pi**3/9
neg_certified = []
not_certified = []
maxratio = None
for n in range(4, NMAX+1):
    t = a/arb(n)**4
    psx = pi/n + t
    psy = pi/(n+1) + t
    def Tx(j):
        return (j*psx).cos()
    def Ty(j):
        return (j*psy).cos()
    g = [Tx(n-m)*Ty(m) - Tx(m)*Ty(n+1-m) for m in range(4)]
    P = 9*(g[1]**2 - g[0]*g[2]/2) + g[2]**2 - g[1]*g[3]
    if P < 0:   # arb comparison is True only if certainly true
        neg_certified.append(n)
    else:
        not_certified.append(n)
    dx = psx.cos() - (pi/n).cos()
    dy = psy.cos() - (pi/(n+1)).cos()
    dist = (dx**2 + dy**2).sqrt()
    r = arb(n)**5*dist
    ub = float(r.upper()) if hasattr(r, 'upper') else float(r.mid() + r.rad())
    maxratio = ub if maxratio is None else max(maxratio, ub)
print(json.dumps({'prec_bits': 400, 'range': [4, NMAX],
                  'n_certified_negative_count': len(neg_certified),
                  'n_not_certified': not_certified,
                  'max_upper_n5_dist_over_range': maxratio}, indent=1))
