#!/usr/bin/env python3
"""Auditor E5 check E: record32 identities evaluated from the raw Chebyshev
recurrence (no trig reduction) at random parameters; coarse fixed-A limit."""
import json, random
import mpmath as mp

mp.mp.dps = 60
random.seed(20261101)


def cheb(x, N):
    T = [mp.mpf(1), x]
    for j in range(2, N+1):
        T.append(2*x*T[-1] - T[-2])
    return T


def P(x, y, n):
    Tx, Ty = cheb(x, n+1), cheb(y, n+1)
    g = [Tx[n-m]*Ty[m] - Tx[m]*Ty[n+1-m] for m in range(4)]
    return 9*(g[1]**2 - g[0]*g[2]/2) + g[2]**2 - g[1]*g[3]


out = {'equal_phase_maxrelerr': 0, 'edge_x1_maxrelerr': 0, 'edge_y1_maxrelerr': 0,
       'edge_min_P_scaled': None, 'samples': 0}
mins = []
for _ in range(400):
    n = random.randint(4, 60)
    al = mp.mpf(random.uniform(-40, 40))
    v = P(mp.cos(al/n), mp.cos(al/(n+1)), n)
    w = 10*mp.sin(al)**2*mp.sin(al/(n*(n+1)))**2
    out['equal_phase_maxrelerr'] = max(out['equal_phase_maxrelerr'],
                                       float(abs(v-w)/(abs(w)+mp.mpf(10)**-50)))
    ph = mp.mpf(random.uniform(0, float(mp.pi)))
    v = P(mp.mpf(1), mp.cos(ph), n)
    b, C, d = 2*mp.sin((n+1)*ph/2), (n+1)*ph/2, ph
    w = b**2*(mp.mpf(9)/2*mp.sin(C-d)**2 + mp.mpf(11)/2*mp.sin(d)**2)
    out['edge_x1_maxrelerr'] = max(out['edge_x1_maxrelerr'], float(abs(v-w)/(abs(w)+mp.mpf(10)**-50)))
    mins.append(float(v))
    th = mp.mpf(random.uniform(0, float(mp.pi)))
    v = P(mp.cos(th), mp.mpf(1), n)
    b, C, d = -2*mp.sin(n*th/2), n*th/2, th
    w = b**2*(mp.mpf(9)/2*mp.sin(C-d)**2 + mp.mpf(11)/2*mp.sin(d)**2)
    out['edge_y1_maxrelerr'] = max(out['edge_y1_maxrelerr'], float(abs(v-w)/(abs(w)+mp.mpf(10)**-50)))
    mins.append(float(v))
    out['samples'] += 1
out['edge_min_P_sampled'] = min(mins)
# coarse fixed-A path
mp.mp.dps = 120
coarse = {}
for A in (mp.mpf(-3), mp.mpf('0.5'), mp.mpf(2), mp.mpf(10)):
    rows = []
    for n in (100, 1000, 10000):
        t = A/mp.mpf(n)**3
        x, y = mp.cos(mp.pi/n + t), mp.cos(mp.pi/(n+1) + t)
        ax, ay = mp.acos(x), mp.acos(y)
        Tx = lambda j: mp.cos(j*ax)
        Ty = lambda j: mp.cos(j*ay)
        g = [Tx(n-m)*Ty(m) - Tx(m)*Ty(n+1-m) for m in range(4)]
        Pv = 9*(g[1]**2 - g[0]*g[2]/2) + g[2]**2 - g[1]*g[3]
        rows.append([n, mp.nstr(mp.mpf(n)**10*Pv/(mp.mpf(9)/2*A**4), 12)])
    coarse[mp.nstr(A, 3)] = rows
out['coarse_n10P_over_9A4half'] = coarse
print(json.dumps(out, indent=1))
