"""Per-node marching propagator of the computed window recurrence (PD-T?...-104 node-row representation):
row i of Qhat solves  beta_k xi_k = a_k(z_i) xi_{p(k)} - sum_{l in W_k} h_l xi_l - phi_k(i).
Drive the computed recurrence (computed coefficients, all nodes at once) with iid forcing of size u/sqrt(M)
per node and step, and compare the response growth P(n) = max_{k <= N_n} ||gamma_k|| with the measured loss
and with u/min joint Ritz residual.  MEASURED only.  Usage: python3 -I l1_node_propagator.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L
EPS = L.EPS

def propagator_response(x, y, coef, tab, N, seed=0):
    idx, pos, parent, op, start = tab
    M = len(x); rng = np.random.default_rng(seed)
    g = np.zeros((M, N)); g[:, 0] = rng.standard_normal(M) * EPS / np.sqrt(M)
    for k in range(1, N):
        W, h, beta = coef[k]; p = parent[k]
        a = x if op[k] == 'J' else y
        g[:, k] = (a * g[:, p] - g[:, W] @ h + rng.standard_normal(M) * EPS / np.sqrt(M)) / beta
    return g

def run(name, P, w, nmax, ritz=True):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, coef, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    N = Q.shape[1]
    g = propagator_response(x, y, coef, tab, N)
    G = Q.T @ Q; cn = np.linalg.norm(g, axis=0)
    U = np.linalg.qr(Q)[0] if ritz else None
    out = []
    for n in range(4, nmax + 1, 4):
        Nn = (n + 1) * (n + 2) // 2
        loss = np.abs(G[:Nn, :Nn] - np.eye(Nn)).max(); Pn = cn[:Nn].max()
        rz = L.ritz_min(U[:, :Nn], x + 1j * y, False)[0][0] if ritz else np.nan
        out.append(f"n{n}: L={loss:.0e} P={Pn:.0e} u/rZ={EPS / rz:.0e}")
    print(f"{name:26s} " + " | ".join(out), flush=True)

rng = np.random.default_rng(11)
M = 1681; sq = rng.uniform(-1, 1, (M, 2)); one = np.ones(M)
run('square', sq, one, 32)
run('square rot 0.3', L.rotate(sq, 0.3), one, 24)
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
P, w = L.nodes_tensor_cheb(41); run('tensor 41^2', P, w, 40)
P, w = L.nodes_padua(48); run('Padua 48 cubature', P, w, 44)
P, w = L.nodes_random(1681, 0); run('random1681_s0', P, w, 40)
