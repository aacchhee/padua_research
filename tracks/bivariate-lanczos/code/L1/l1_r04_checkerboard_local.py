"""R04: is the clustered-checkerboard loss a local (within-window) Gram-Schmidt effect?  Compare BJ (block window,
CGS once), block window with CGS twice, exact window with ORTH (HL), and report the largest local loss (Gram entries
inside the window) vs the global loss.  MEASURED only.  Usage: python3 -I l1_r04_checkerboard_local.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
Nof = lambda n: (n + 1) * (n + 2) // 2

def cgs2_block(x, y, w, nmax):
    idx, pos, parent, op, start = L.tables(nmax); N = len(idx); M = len(x)
    Q = np.zeros((M, N)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    for k in range(1, N):
        p = parent[k]; a = x if op[k] == 'J' else y; u = a * Q[:, p]; W = L.window(k, idx, start, 'block')
        for _ in range(2):
            u = u - Q[:, W] @ (Q[:, W].T @ u)
        Q[:, k] = u / np.linalg.norm(u)
    return Q, (idx, pos, parent, op, start)

def report(lab, Q, tab, m):
    idx, pos, parent, op, start = tab
    G = Q.T @ Q; N = Q.shape[1]
    loc = 0.0
    for k in range(1, N):
        W = L.window(k, idx, start, 'block')
        if W: loc = max(loc, float(np.abs(G[W, k]).max()))
    prof = " ".join(f"{t}:{np.abs(G[:Nof(t), :Nof(t)] - np.eye(Nof(t))).max():.0e}" for t in range(4, m, 4))
    print(f"   {lab:22s} loss t=4,8,..: {prof} | max local (in-window) |q_l^T q_k| = {loc:.0e}", flush=True)

m = 30
for name, X, Y in [('clustered (cubic)', np.linspace(-1, 1, m + 1) ** 3, np.linspace(-1, 1, m + 2) ** 3),
                   ('equispaced', np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2))]:
    P, w, wx, wy = C.checkerboard(X, Y); x, y = P[:, 0].copy(), P[:, 1].copy()
    print(f"== checkerboard {name}, m={m}", flush=True)
    Q, _, tab = L.recurrence(x, y, w, m - 1, win='block', orth='cgs'); report('BJ (CGS once)', Q, tab, m)
    Q2, tab2 = cgs2_block(x, y, w, m - 1); report('block window CGS2', Q2, tab2, m)
    Q3, _, tab3 = L.recurrence(x, y, w, m - 1, win='exact', orth='orth'); report('HL (exact, ORTH)', Q3, tab3, m)
