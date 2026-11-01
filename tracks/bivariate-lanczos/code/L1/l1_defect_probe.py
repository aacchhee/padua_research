"""Probe: growth of the implicit-operator (J) defect and of loss of orthogonality vs degree, for node sets of
different geometry (product vs non-product measures). MEASURED only.
Usage: python3 -I l1_defect_probe.py > logs/r01_defect_probe.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L

def probe(name, P, w, nmax=24, win='block', orth='cgs'):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, _, _ = L.recurrence(x, y, w, nmax, win=win, orth=orth)
    U, _ = np.linalg.qr(Q); G = Q.T @ Q
    Nof = lambda n: (n + 1) * (n + 2) // 2
    out = []
    for n in range(4, nmax + 1, 4):
        Nn, Nm = Nof(n), Nof(n - 1); Un = U[:, :Nn]
        AU = x[:, None] * U[:, :Nm]; D = AU - Un @ (Un.T @ AU)
        out.append((n, np.abs(G[:Nn, :Nn] - np.eye(Nn)).max(), np.linalg.norm(D, axis=0).max()))
    print(f"{name:34s} " + " ".join(f"n{n}:L={l:.0e},d={d:.0e}" for n, l, d in out), flush=True)

rng = np.random.default_rng(11)
M = 1681
sq = rng.uniform(-1, 1, (M, 2)); one = np.ones(M)
probe('square (product)', sq, one)
for th in [0.05, 0.3, np.pi / 4, np.pi / 2]:
    probe(f'square rotated {th:.3f}', L.rotate(sq, th), one)
probe('square, x<->y swapped', sq[:, ::-1].copy(), one)
# disk (rotation invariant, not a product)
dk = []
while len(dk) < M:
    p = rng.uniform(-1, 1, 2)
    if p @ p <= 1: dk.append(p)
probe('disk', np.array(dk), one)
# product, non-uniform: x uniform, y ~ Beta(0.5,2) mapped to [-1,1]
pr = np.column_stack([rng.uniform(-1, 1, M), 2 * rng.beta(0.5, 2.0, M) - 1])
probe('product x~U, y~Beta(.5,2)', pr, one)
probe('product, rotated 0.3', L.rotate(pr, 0.3), one)
# triangle (non-product)
tr = []
while len(tr) < M:
    p = rng.uniform(0, 1, 2)
    if p.sum() <= 1: tr.append(2 * p - 1)
probe('triangle', np.array(tr), one)
# square with product non-uniform weights vs non-product weights
probe('square, weights exp(x)exp(y) (product)', sq, np.exp(sq[:, 0]) * np.exp(sq[:, 1]))
probe('square, weights exp(x*y) (non-product)', sq, np.exp(2 * sq[:, 0] * sq[:, 1]))
# HL variant on rotated square
probe('square rotated 0.3, HL exact/orth', L.rotate(sq, 0.3), one, win='exact', orth='orth')
# shear (affine image of a product set: graded spaces invariant)
probe('square sheared (x, y+0.5x)', np.column_stack([sq[:, 0], sq[:, 1] + 0.5 * sq[:, 0]]), one)
probe('square sheared (x+0.5y, y)', np.column_stack([sq[:, 0] + 0.5 * sq[:, 1], sq[:, 1]]), one)
