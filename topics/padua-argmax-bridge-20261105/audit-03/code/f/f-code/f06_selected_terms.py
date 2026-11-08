#!/usr/bin/env python3
"""[E] F06 key step (14): every selected regular term (l in [M/6,M/2], R=l+-1, both sigma
branches, both orientations, both projections) has defect d >= F(b)/t, with the literal
F(b)=a cot(b/2)-C of eq.(11). Float64, sampled phases; MEASURED cross-check only."""
import numpy as np
exec(open('f06_floor_check.py').read().split('if __name__')[0])
rng = np.random.default_rng(7)
worst = (9, None); cnt = 0; neg = 0
for n in (128, 129, 200, 256):
    m = n + 1
    for trial in range(12):
        r0 = rng.uniform(0, np.pi/4); w = rng.uniform(0, 1)
        al = w*r0*rng.choice([-1, 1]); be = (r0 - abs(al))*rng.choice([-1, 1])
        if trial == 0: al, be = np.pi/4, 0.0
        if trial == 1: al, be = -np.pi/8, np.pi/8
        r = abs(al) + abs(be); a = (np.cos(al) + np.cos(be))/2; Pabs = abs(np.sin(al)) + abs(np.sin(be))
        for proj in ('v', 'h'):
            M, L, mu, et = (m, n, be, al) if proj == 'v' else (n, m, al, be)
            D = 2*np.pi + r; T = D/M; C = Pabs/2 + (a + Pabs)*T + a*T**2
            for eps in (1, -1):
                xi = eps*mu; t = (2*np.pi + xi)/M
                for l in range(int(np.ceil(M/6)), int(np.floor(M/2)) + 1):
                    b = l*np.pi/M; Fb = a/np.tan(b/2) - C
                    krow = l if eps == 1 else M - l
                    for R in (l - 1, l + 1):
                        for z in (R, 2*L - R):
                            if proj == 'v':
                                u = np.array([(z*np.pi + al)/n]); phi = (2*np.pi + be)/m if eps == 1 else ((m - 2)*np.pi + be)/m
                                sg = 1.0 if z % 2 == 0 else -1.0
                                Xp = sg*G(n, u, np.array([phi + krow*np.pi/m]))/2; Xm = sg*G(n, u, np.array([phi - krow*np.pi/m]))/2
                            else:
                                v = np.array([(z*np.pi + be)/m]); th = (2*np.pi + al)/n if eps == 1 else ((n - 2)*np.pi + al)/n
                                Xp = G(n, np.array([th + krow*np.pi/n]), v)/2; Xm = G(n, np.array([th - krow*np.pi/n]), v)/2
                            d = dfun(Xp, Xm)[0]; cnt += 1
                            rr = d*t/Fb
                            if Fb <= 0: neg += 1
                            if rr < worst[0]: worst = (rr, (proj, n, eps, l, R, z, al, be, d, Fb/t))
print("selected terms checked:", cnt, "; F(b)<=0 cases:", neg)
print("min d*t/F(b) (must be >=1):", worst[0], "at", worst[1])
