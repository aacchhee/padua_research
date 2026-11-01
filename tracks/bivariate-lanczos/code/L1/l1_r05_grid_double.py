"""R05 context: BJ loss in double on the triangle grid T_m and the square grid Q_m (rescaled to [-1,1]), equal
weights.  MEASURED only.  Usage: python3 -I l1_r05_grid_double.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L
Nof = lambda n: (n + 1) * (n + 2) // 2
for m in (24, 30):
    for name, P in [('triangle', np.array([(i, j) for i in range(m + 1) for j in range(m + 1 - i)], float)),
                    ('square', np.array([(i, j) for i in range(m + 1) for j in range(m + 1)], float))]:
        P = P / m * 2 - 1
        Q, _, _ = L.recurrence(P[:, 0].copy(), P[:, 1].copy(), np.ones(len(P)), 14, win='block', orth='cgs'); G = Q.T @ Q
        print(f"{name:8s} grid m={m} M={len(P)} loss n=2..14: " + " ".join(f"{n}:{np.abs(G[:Nof(n), :Nof(n)] - np.eye(Nof(n))).max():.0e}" for n in range(2, 15, 2)), flush=True)
