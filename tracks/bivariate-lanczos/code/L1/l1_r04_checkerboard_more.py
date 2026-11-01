"""R04 post-hoc diagnosis of the clustered checkerboard (no pre-registered criterion): u-scaling (double vs long
double BJ), two-relation block recurrence, and forward error of the BJ basis against a fully reorthogonalised one.
MEASURED only.  Usage: python3 -I l1_r04_checkerboard_more.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
import l1_both_relations as B
Nof = lambda n: (n + 1) * (n + 2) // 2
m = 30
X, Y = np.linspace(-1, 1, m + 1) ** 3, np.linspace(-1, 1, m + 2) ** 3
P, w, wx, wy = C.checkerboard(X, Y); x, y = P[:, 0].copy(), P[:, 1].copy()
def prof(Q, ts):
    G = Q.T @ Q
    return " ".join(f"{t}:{float(np.abs(G[:Nof(t), :Nof(t)] - np.eye(Nof(t), dtype=G.dtype)).max()):.0e}" for t in ts)
ts = range(4, m, 4)
Qd, _, _ = L.recurrence(x, y, w, m - 1, win='block', orth='cgs')
Ql, _, _ = L.recurrence(x, y, w, m - 1, win='block', orth='cgs', dtype=np.longdouble)
print("BJ double      :", prof(Qd, ts), flush=True)
print("BJ long double :", prof(Ql, ts), flush=True)
Qb = B.both(x, y, w, m - 1)
print("two-relation   :", prof(Qb, ts), flush=True)
# forward error vs a long-double BJ (column-wise sign-free distance within each prefix)
fe = []
for t in ts:
    Nn = Nof(t)
    fe.append(f"{t}:{float(np.abs(np.abs(Qd[:, :Nn]) - np.abs(Ql[:, :Nn].astype(float))).max()):.0e}")
print("max | |Q_d| - |Q_ld| | (entrywise):", " ".join(fe), flush=True)
