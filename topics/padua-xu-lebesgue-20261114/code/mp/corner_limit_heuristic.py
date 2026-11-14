#!/usr/bin/env python3
"""CONJECTURAL / heuristic asymptotic constant for lambda_n(1,1)/n^2 (not a proof).

Derivation sketch (formal, not rigorous): in Beberok's closed form, nodes with q - p = e (e odd integer; p = m, q = 2k or 2k-1)
form a one-parameter family p = x n.  With w = pi p/(n+2), v - w = pi*delta/((n+2)(n+3)), delta = e(n+2) - p ~ n (e - x),
cos v - cos w ~ -sin(w) (v - w) and sin v ~ sin w one gets, to leading order,
   omega |K| ~ n * 8 sin(pi x)/pi^3 * | -(1+cos pi x)/(e-x)^3 + (pi/2) sin(pi x)/(e-x)^2 |,
hence  c = lim lambda_n(1,1)/n^2 = (8/pi^3) sum_{e odd} int_0^1 sin(pi x) | -(1+cos pi x)/(e-x)^3 + (pi/2) sin(pi x)/(e-x)^2 | dx.
This script evaluates the partial sums over |e| <= E and extrapolates the tail (tail ~ 2/(pi^2 E) + ...).
Usage: python3 corner_limit_heuristic.py [E=161]
"""
import sys
import mpmath as mp
mp.mp.dps = 20
pi = mp.pi


def br(x, e):
    a = e - x
    return -(1 + mp.cos(pi * x)) / a ** 3 + pi * mp.sin(pi * x) / (2 * a ** 2)


def I(e):
    xs = [mp.mpf(i) / 16 for i in range(17)]
    pts = [xs[0]]
    for i in range(16):
        a, b = xs[i], xs[i + 1]
        if (e - a) != 0 and (e - b) != 0 and br(a, e) * br(b, e) < 0:
            pts.append(mp.findroot(lambda x: br(x, e), (a, b), solver='anderson'))
        pts.append(b)
    return 8 / pi ** 3 * mp.quad(lambda x: mp.sin(pi * x) * abs(br(x, e)), pts)


if __name__ == "__main__":
    E = int(sys.argv[1]) if len(sys.argv) > 1 else 161
    S = mp.mpf(0); out = []
    for j in range(1, E + 1, 2):
        S += I(j) + I(-j)
        out.append((j, S))
    js = [j for j, _ in out if j >= E // 4]
    Ss = [s for j, s in out if j >= E // 4]
    M = mp.matrix([[1, mp.mpf(1) / j, mp.mpf(1) / j ** 2, mp.mpf(1) / j ** 3, mp.mpf(1) / j ** 4] for j in js[-5:]])
    sol = mp.lu_solve(M, mp.matrix(Ss[-5:]))
    print("partial sum |e|<=%d: %s" % (E, mp.nstr(S, 12)))
    print("extrapolated c = %s ; fitted tail coefficient of 1/E = %s (2/pi^2 = %s)" % (mp.nstr(sol[0], 10), mp.nstr(sol[1], 8), mp.nstr(2 / pi ** 2, 8)))
