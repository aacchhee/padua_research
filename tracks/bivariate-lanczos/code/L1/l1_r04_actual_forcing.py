"""R04 post-hoc diagnosis (no pre-registered criterion): split the computed basis exactly as Qhat = Xibar - Phitilde
(PD-T?...-104): Xibar = the run's computed recurrence (computed coefficients) re-run in long double from q0 without
forcing; Phitilde = Xibar - Qhat = propagated actual local errors.  Reports max column norm of Phitilde, the Gram
defect of Xibar, and the loss, per degree.  MEASURED only.  Usage: python3 -I l1_r04_actual_forcing.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
LD = np.longdouble
Nof = lambda n: (n + 1) * (n + 2) // 2

def split(name, P, w, nmax, step=4):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, coef, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    idx, pos, parent, op, start = tab
    N = Q.shape[1]; xl, yl = x.astype(LD), y.astype(LD)
    Xi = np.zeros(Q.shape, dtype=LD); Xi[:, 0] = Q[:, 0].astype(LD)
    for k in range(1, N):
        W, h, beta = coef[k]; p = parent[k]; a = xl if op[k] == 'J' else yl
        Xi[:, k] = (a * Xi[:, p] - Xi[:, W] @ np.asarray(h, dtype=LD)) / LD(beta)
    Ph = Xi - Q.astype(LD)
    GX = Xi.T @ Xi; GQ = Q.astype(LD).T @ Q.astype(LD)
    out = []
    for n in range(step, nmax + 1, step):
        Nn = Nof(n); I = np.eye(Nn, dtype=LD)
        out.append(f"n{n}: loss={float(np.abs(GQ[:Nn,:Nn]-I).max()):.0e} |Phi~|={float(np.sqrt((Ph[:, :Nn]**2).sum(0)).max()):.0e} "
                   f"|Xi^T Xi - I|={float(np.abs(GX[:Nn,:Nn]-I).max()):.0e}")
    print(f"{name:26s} " + " | ".join(out), flush=True)

m = 30
X, Y = np.linspace(-1, 1, m + 1) ** 3, np.linspace(-1, 1, m + 2) ** 3
Pc, wc, wx, wy = C.checkerboard(X, Y)
split('checkerboard clustered', Pc, wc, 24)
rng = np.random.default_rng(11); sq = rng.uniform(-1, 1, (1681, 2))
split('square rot pi/4', L.rotate(sq, np.pi / 4), np.ones(1681), 20)
split('square', sq, np.ones(1681), 28)
