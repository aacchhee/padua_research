"""Localise the non-product instability: run the BJ recurrence with the F-products and the J-products in
different precisions (the other operator's products and all storage in long double).
  'F-double': F-products in double, J-products in long double;  'J-double': the reverse;
  'all-double', 'all-long': references.  MEASURED only.  Usage: python3 -I l1_mixed_precision.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L
LD = np.longdouble

def run(x, y, w, nmax, dbl):
    idx, pos, parent, op, start = L.tables(nmax); N = len(idx)
    xl, yl = x.astype(LD), y.astype(LD); M = len(x)
    Q = np.zeros((M, N), dtype=LD); v = np.sqrt(w.astype(LD)); Q[:, 0] = v / np.sqrt(np.sum(v * v))
    for k in range(1, N):
        p = parent[k]; W = L.window(k, idx, start, 'block')
        if op[k] in dbl:
            a = (x if op[k] == 'J' else y); q = Q[:, p].astype(float); Qw = Q[:, W].astype(float)
            u = a * q; h = Qw.T @ u; u = u - Qw @ h; Q[:, k] = (u / np.sqrt(np.sum(u * u))).astype(LD)
        else:
            a = (xl if op[k] == 'J' else yl); u = a * Q[:, p]; Qw = Q[:, W]
            h = Qw.T @ u; u = u - Qw @ h; Q[:, k] = u / np.sqrt(np.sum(u * u))
    G = Q.T @ Q
    return [float(np.abs(G[:(n+1)*(n+2)//2, :(n+1)*(n+2)//2] - np.eye((n+1)*(n+2)//2, dtype=LD)).max()) for n in (8, 12, 16, 20)]

rng = np.random.default_rng(11)
sq = rng.uniform(-1, 1, (1681, 2)); w = np.ones(1681)
for name, P in [('square', sq), ('square rotated 0.3', L.rotate(sq, 0.3))]:
    for lab, dbl in [('all-double', ('F', 'J')), ('F-double only', ('F',)), ('J-double only', ('J',)), ('all-long', ())]:
        r = run(P[:, 0].copy(), P[:, 1].copy(), w, 20, dbl)
        print(f"{name:20s} {lab:14s} loss n=8,12,16,20: " + " ".join(f"{v:.1e}" for v in r), flush=True)
