"""Referee checks (MEASURED): (ul:outer-geometry) on a grid, the literal
justification 'x>=1 via u>=11/48', (uc:weighted-C), and the closed forms of
Lemma uc:cancellation-lemma against quadrature."""
import math, time
import numpy as np
import mpmath as mp
t0 = time.process_time()
u1, a0, w0, p0, P0, eta = 47/384, 337/384, 721/384, 12/25, 24/25, 1.5
xs = np.linspace(0, math.pi, 1201)
X, Y = np.meshgrid(xs, xs, indexing='ij')
M = (X + Y >= 1) & (X + Y <= math.pi)
ce, cd = np.cos((X + Y) / 2), np.cos((X - Y) / 2)
a = ce * cd; u = 1 - a; v = u - u1
p, q = np.sin(X), np.sin(Y); P = p + q; dplus = np.maximum(q - p, 0)
sv = np.sqrt(np.maximum(v, 0))
viol = {
 'v>=0': np.min(np.where(M, v, 1)),
 'a0-a': np.min(np.where(M, a0 - a, 1)),
 'w0-(ce+cd)': np.min(np.where(M, w0 - (ce + cd), 1)),
 'p0+eta sqrt v - max(p,q)': np.min(np.where(M, p0 + eta * sv - np.maximum(p, q), 1)),
 '3sqrt v - d+': np.min(np.where(M, 3 * sv - dplus, 1)),
 'P0+4v-P': np.min(np.where(M, P0 + 4 * v - P, 1)),
 '2sqrt(2v)-|p-q|': np.min(np.where(M, 2 * np.sqrt(2 * np.maximum(v, 0)) - np.abs(p - q), 1)),
}
print('outer-geometry minimal slacks (>=0 required):', {k: round(float(x), 5) for k, x in viol.items()})
# literal justification for x>=1: v>=11/48-u1 only
vmin = 11/48 - u1
print('literal x>=1 route: p0+eta*sqrt(11/48-u1)=%.4f vs max sin x on [1,pi] = 1 -> %s' % (p0 + eta * math.sqrt(vmin), 'insufficient' if p0 + eta * math.sqrt(vmin) < 1 else 'ok'))
xx = np.linspace(1, math.pi, 2001)
print('x-dependent route max_{x in[1,pi]} sin x - eta*sqrt((1-cos x)/2-u1) = %.4f (< p0=0.48 needed)' % np.max(np.sin(xx) - eta * np.sqrt((1 - np.cos(xx)) / 2 - u1)))
# (uc:weighted-C)
mp.mp.dps = 30
C0 = 2 * mp.euler + 4 * mp.log(2); bst = C0 - mp.mpf(7) / 2
Ccal = lambda t: -mp.digamma(t) - mp.digamma(1 - t)
worst = min(C0 - bst * (1 - mp.cos(th / 2)) - mp.cos(th / 2) * Ccal(mp.mpf(1) / 2 + th / (2 * mp.pi)) for th in [mp.pi * (-1 + 2 * i / 400) for i in range(1, 400)])
print('(uc:weighted-C) min slack over theta grid:', mp.nstr(worst, 6))
# cancellation lemma closed forms vs quadrature
def I_num(C, D, e):
    f = lambda t: abs(C * mp.cot(t) + D * mp.cot(t + e)) - abs(C * mp.cot(t)) - abs(D * mp.cot(t + e))
    pts = sorted(set([mp.mpf(0), mp.pi - e, mp.pi] + [mp.pi * k / 16 for k in range(1, 16)]))
    return mp.quad(f, pts, maxdegree=10)
def J_closed(v, s, e):
    if s <= v:
        c, b = (v - s) / 2, (v + s) / 2
        g = lambda z: z * mp.log(z / v) if z > 0 else mp.mpf(0)
        return 2 * (g(c) + g(b))
    if s * mp.sin(e) >= v:
        return 2 * s * mp.log(mp.sin(e))
    c, b = (s - v) / 2, (s + v) / 2
    t1 = (mp.asin(s * mp.sin(e) / v) - e) / 2
    return 2 * s * mp.log(mp.sin(e)) + 2 * (b * mp.log(mp.cos(t1) / mp.sin(t1 + e)) - c * mp.log(mp.cos(t1 + e) / mp.sin(t1)))
rows = []
for (v, s, e) in [(1, 0.3, 0.7), (1, 0.9, 1.2), (0.5, 1.2, 0.3), (0.5, 1.2, 1.4), (0.8, 2.0, 0.2), (0.3, 0.31, 0.05)]:
    v, s, e = mp.mpf(v), mp.mpf(s), mp.mpf(e)
    num = I_num((v - s) / 2, (v + s) / 2, e)
    cl = J_closed(v, s, e)
    Rv = cl - 2 * max(s - v, 0) * mp.log(mp.sin(e))
    rows.append((float(v), float(s), float(e), float(num - cl), float(Rv), float(Rv) <= 1e-20, abs(Rv) <= max(2 * v, s + v) * math.log(2) + 1e-20))
print('cancellation lemma (v,s,e, quad-closed, R, R<=0, |R|<=max(2v,s+v)log2):')
for r in rows: print('  ', r)
print('cpu_s', time.process_time() - t0)
