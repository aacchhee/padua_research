"""Check that the non-product loss growth is amplified rounding (scales with the unit roundoff), not an
algebraic defect of the window: same run in double and long double (x87 80-bit, u_ld = 2^-64).
Usage: python3 -I l1_precision_scaling.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L
rng = np.random.default_rng(11)
P = L.rotate(rng.uniform(-1, 1, (1681, 2)), 0.3); w = np.ones(1681)
print('finfo longdouble eps', np.finfo(np.longdouble).eps)
for dt in (float, np.longdouble):
    Q, _, _ = L.recurrence(P[:, 0], P[:, 1], w, 20, win='block', orth='cgs', dtype=dt)
    G = Q.T @ Q
    out = []
    for n in (8, 12, 16, 20):
        Nn = (n + 1) * (n + 2) // 2
        out.append(f"n{n}:{float(np.abs(G[:Nn, :Nn] - np.eye(Nn, dtype=dt)).max()):.1e}")
    print(dt.__name__ if hasattr(dt, '__name__') else dt, ' '.join(out))
