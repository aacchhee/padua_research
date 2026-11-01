"""R04: Ritz residuals (H_x, H_y, Z) vs loss on the checkerboards (is the clustered growth Ritz-type?).
Post-hoc diagnosis (no pre-registered criterion).  MEASURED only.  Usage: python3 -I l1_r04_checkerboard_ritz.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2
m = 30
for name, X, Y in [('clustered (cubic)', np.linspace(-1, 1, m + 1) ** 3, np.linspace(-1, 1, m + 2) ** 3),
                   ('equispaced', np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2))]:
    P, w, wx, wy = C.checkerboard(X, Y); x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, _, _ = L.recurrence(x, y, w, m - 1, win='block', orth='cgs'); G = Q.T @ Q
    U, _ = np.linalg.qr(Q)
    print(f"== checkerboard {name}", flush=True)
    for n in range(8, m, 4):
        Nn = Nof(n); Un = U[:, :Nn]
        rx = L.ritz_min(Un, x, True)[0][0]; ry = L.ritz_min(Un, y, True)[0][0]
        rz, thz, _ = L.ritz_min(Un, x + 1j * y, False)
        i, d = L.nearest_node(thz[0], P)
        loss = np.abs(G[:Nn, :Nn] - np.eye(Nn)).max()
        print(f"   n={n:2d} loss={loss:.1e} u/rho_X={EPS/rx:.1e} u/rho_Y={EPS/ry:.1e} u/rho_Z={EPS/rz[0]:.1e}  "
              f"Z-min Ritz value near node {tuple(np.round(P[i], 3))} (weight {w[i]:.1e}, dist {d:.0e})", flush=True)
