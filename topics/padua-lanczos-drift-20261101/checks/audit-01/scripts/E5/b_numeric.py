#!/usr/bin/env python3
"""Auditor E5 check B: high-precision numerical corroboration of record30.

Evaluates P_n at zeta_n directly from the definition.  Two evaluators:
 (i)  T_j(x) by the three-term Chebyshev recurrence on x (no trig identity), n<=2000;
 (ii) T_j(x) = cos(j*acos(x)) at high precision, all n.
Also: nearest Padua node to zeta_n (brute force for n<=400, local search above),
and the first n>=4 with P_n(zeta_n)<0 plus a sign sweep up to NMAX.
MEASURED corroboration only.
"""
import json, sys
import mpmath as mp

mp.mp.dps = 130
PI = mp.pi
a = 20*PI**3/9
L = -6400*PI**12/729
Dlim = 20*mp.sqrt(2)*PI**4/9


def cheb_rec(x, N):
    T = [mp.mpf(1), x]
    for j in range(2, N+1):
        T.append(2*x*T[-1] - T[-2])
    return T


def P_from_T(Tx, Ty, n):
    g = [Tx[n-m]*Ty[m] - Tx[m]*Ty[n+1-m] for m in range(4)]
    return 9*(g[1]**2 - g[0]*g[2]/2) + g[2]**2 - g[1]*g[3], g


def P_rec(x, y, n):
    return P_from_T(cheb_rec(x, n+1), cheb_rec(y, n+1), n)


def P_cos(x, y, n):
    ax, ay = mp.acos(x), mp.acos(y)
    Tx = {j: mp.cos(j*ax) for j in [0, 1, 2, 3, n-3, n-2, n-1, n]}
    Ty = {j: mp.cos(j*ay) for j in [0, 1, 2, 3, n+1-3, n+1-2, n+1-1, n+1]}
    g = [Tx[n-m]*Ty[m] - Tx[m]*Ty[n+1-m] for m in range(4)]
    return 9*(g[1]**2 - g[0]*g[2]/2) + g[2]**2 - g[1]*g[3], g


def zeta(n, aa=a):
    t = aa/mp.mpf(n)**4
    return mp.cos(PI/n + t), mp.cos(PI/(n+1) + t)


def node(n, j, k):
    return mp.cos(j*PI/n), mp.cos(k*PI/(n+1))


def nearest(n, zx, zy, brute):
    best = None
    if brute:
        rng = [(j, k) for j in range(n+1) for k in range(n+2) if (j+k) % 2 == 0]
    else:
        rng = [(j, k) for j in range(0, 6) for k in range(0, 7) if (j+k) % 2 == 0]
    for j, k in rng:
        X, Y = node(n, j, k)
        d = mp.sqrt((zx-X)**2 + (zy-Y)**2)
        if best is None or d < best[0]:
            best = (d, j, k)
    return best


res = {'dps': mp.mp.dps, 'limit_L': mp.nstr(L, 20), 'limit_D': mp.nstr(Dlim, 20),
       'table': [], 'checks': {}}
ns = [4, 5, 6, 8, 10, 12, 16, 20, 30, 50, 100, 200, 300, 1000, 2000, 3000,
      10000, 30000, 100000]
for n in ns:
    zx, zy = zeta(n)
    Pc, gc = P_cos(zx, zy, n)
    row = {'n': n, 'P': mp.nstr(Pc, 12),
           'n14P_over_L': mp.nstr(mp.mpf(n)**14*Pc/L, 15),
           'n7g_over_lim': [mp.nstr(mp.mpf(n)**7*gc[m] /
                                    (-a**2 - mp.mpf(2)/3*a*PI**3*m**3), 12)
                            for m in range(4)]}
    if n <= 2000:
        Pr, gr = P_rec(zx, zy, n)
        row['rec_vs_cos_relerr'] = mp.nstr(abs(Pr-Pc)/abs(Pc), 5)
    d, j, k = nearest(n, zx, zy, n <= 400)
    row['nearest_node'] = [j, k]
    X, Y = node(n, 1, 1)
    d11 = mp.sqrt((zx-X)**2 + (zy-Y)**2)
    row['n5_dist11_over_D'] = mp.nstr(mp.mpf(n)**5*d11/Dlim, 15)
    row['dist11'] = mp.nstr(d11, 8)
    row['zeta_in_open_square'] = bool(-1 < zx < 1 and -1 < zy < 1)
    res['table'].append(row)
    print(row, file=sys.stderr)

# sign sweep with cos evaluator at lower precision
mp.mp.dps = 80
a = 20*mp.pi**3/9
first_neg = None
pos_after = []
NMAX = 3000
for n in range(4, NMAX+1):
    zx, zy = zeta(n, a)
    Pc, _ = P_cos(zx, zy, n)
    if Pc < 0 and first_neg is None:
        first_neg = n
    if first_neg is not None and Pc >= 0:
        pos_after.append(n)
res['checks']['sweep_range'] = [4, NMAX]
res['checks']['first_n_with_P_negative'] = first_neg
res['checks']['n_after_first_with_P_nonneg'] = pos_after
res['checks']['nonneg_before_first'] = list(range(4, first_neg)) if first_neg else None
# sharper constant within the same common-increment method
c = 2*mp.pi**3/3
amin = c*(10-2*mp.sqrt(2))/3
res['checks']['a_min_for_negative_limit'] = mp.nstr(amin, 15)
res['checks']['sharper_const_sqrt2_pi_amin'] = mp.nstr(mp.sqrt(2)*mp.pi*amin, 15)
res['checks']['claimed_const'] = mp.nstr(20*mp.sqrt(2)*mp.pi**4/9, 15)
print(json.dumps(res, indent=1))
