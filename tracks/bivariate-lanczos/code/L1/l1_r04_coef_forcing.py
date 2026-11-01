"""R04: coefficient-aware forcing for the node-propagator predictor (IDEA?bivariate-lanczos-claude-115).
Forcing at node i, step k: u*N(0,1)*(|a q_p(i)| + sum_l (|h_l| + ||q_l|| ||A q_p||) |q_l(i)| + beta |q_k(i)|).
MEASURED only.  Usage: python3 -I l1_r04_coef_forcing.py > logs/r04_coef_forcing.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2

def run(name, P, w, nmax, step=4):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, coef, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    idx, pos, parent, op, start = tab
    M, N = Q.shape; rng = np.random.default_rng(0); G = Q.T @ Q
    g = np.zeros((M, N)); g[:, 0] = rng.standard_normal(M) * EPS * np.abs(Q[:, 0])
    for k in range(1, N):
        W, h, beta = coef[k]; p = parent[k]; a = x if op[k] == 'J' else y
        Aq = a * Q[:, p]; nAq = np.linalg.norm(Aq)
        habs = np.abs(h) + np.linalg.norm(Q[:, W], axis=0) * nAq
        mag = np.abs(Aq) + np.abs(Q[:, W]) @ habs + beta * np.abs(Q[:, k])
        g[:, k] = (a * g[:, p] - g[:, W] @ h + rng.standard_normal(M) * EPS * mag) / beta
    cn = np.linalg.norm(g, axis=0)
    out = []
    for n in range(step, nmax + 1, step):
        Nn = Nof(n)
        out.append(f"n{n}: L={np.abs(G[:Nn, :Nn] - np.eye(Nn)).max():.0e} Pc={cn[:Nn].max():.0e}")
    print(f"{name:26s} " + " | ".join(out), flush=True)

if __name__ == '__main__':
    print(f"# l1_r04_coef_forcing.py numpy={np.__version__}")
    rng = np.random.default_rng(11); M = 1681
    sq = rng.uniform(-1, 1, (M, 2)); one = np.ones(M)
    run('square', sq, one, 32)
    run('square rot pi/4', L.rotate(sq, np.pi / 4), one, 24)
    dk = []
    while len(dk) < M:
        p = rng.uniform(-1, 1, 2)
        if p @ p <= 1: dk.append(p)
    run('disk', np.array(dk), one, 24)
    tr = []
    while len(tr) < M:
        p = rng.uniform(0, 1, 2)
        if p.sum() <= 1: tr.append(2 * p - 1)
    run('triangle', np.array(tr), one, 20)
    m = 30
    for lab, X, Y in [('checkerboard Cheb-Lobatto', -np.cos(np.arange(m + 1) * np.pi / m), -np.cos(np.arange(m + 2) * np.pi / (m + 1))),
                      ('checkerboard equispaced', np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)),
                      ('checkerboard clustered', np.linspace(-1, 1, m + 1) ** 3, np.linspace(-1, 1, m + 2) ** 3)]:
        Pc, wc, wx, wy = C.checkerboard(X, Y)
        run(lab, Pc, wc, m - 1)
