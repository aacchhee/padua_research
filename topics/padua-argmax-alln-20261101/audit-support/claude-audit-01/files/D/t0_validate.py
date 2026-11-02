"""Validate kernel cardinals against first-principles Vandermonde inversion; validate theory14 (3)."""
import sys, json
import numpy as np
import mpmath as mp
sys.path.insert(0, __import__('os').path.dirname(__file__))
from padlib import *

rng = np.random.default_rng(20261102)
res = {"ker_vs_vdm": [], "cardinality": [], "refl3": [], "mp_vdm": []}
for n in range(1, 16):
    m = n + 1
    th = rng.uniform(0, PI, 40); ph = rng.uniform(0, PI, 40)
    # include corners, edges and near-collision points
    th = np.concatenate([th, [0, PI, 0, PI, PI / 2, 0.0, PI]])
    ph = np.concatenate([ph, [0, 0, PI, PI, 0.0, PI / 3, PI * (1 - 1e-9)]])
    Lk = ker_cardinals(n, th, ph)
    Lv = vdm_cardinals(n, np.cos(th), np.cos(ph))
    err = np.abs(Lk - Lv).max()
    J, K, a, b, w = nodes(n)
    Ln = ker_cardinals(n, a, b)
    cerr = np.abs(Ln - np.eye(len(a))).max()
    res["ker_vs_vdm"].append([n, float(err)])
    res["cardinality"].append([n, float(cerr)])
    # theory14 formula (3)
    worst = 0.0
    for _ in range(10):
        al, be = rng.uniform(0, 1 / 64, 2) * rng.uniform(0, 1)
        l1 = lebesgue(n, [PI - al / n], [PI - be / m])[0]
        l2 = lam_reflected(n, al, be)
        worst = max(worst, abs(l1 - l2))
    for al, be in [(0, 0), (0.3, 0.0), (0.0, 2.0), (1.5, 1.5)]:
        l1 = lebesgue(n, [PI - al / n], [PI - be / m])[0]
        l2 = lam_reflected(n, al, be)
        worst = max(worst, abs(l1 - l2))
    res["refl3"].append([n, float(worst)])

# high precision first-principles check for n<=5 (mpmath Vandermonde)
mp.mp.dps = 40
for n in range(1, 6):
    m = n + 1
    J, K, a, b, w = nodes(n)
    basis = [(A, Bb) for A in range(n + 1) for Bb in range(n + 1 - A)]
    V = mp.matrix(len(J), len(basis))
    for i in range(len(J)):
        x = mp.cos(mp.pi * int(J[i]) / n); y = mp.cos(mp.pi * int(K[i]) / m)
        for c, (A, Bb) in enumerate(basis):
            V[i, c] = mp.chebyt(A, x) * mp.chebyt(Bb, y)
    Vi = mp.inverse(V)
    worst = mp.mpf(0)
    for (t1, t2) in [(mp.pi, mp.pi), (0.37, 2.1), (mp.pi, 0), (0, mp.pi), (1.0, mp.pi)]:
        x = mp.cos(t1); y = mp.cos(t2)
        P = mp.matrix(1, len(basis))
        for c, (A, Bb) in enumerate(basis):
            P[0, c] = mp.chebyt(A, x) * mp.chebyt(Bb, y)
        L = P * Vi
        lk = ker_cardinals(n, [float(t1)], [float(t2)])[0]
        worst = max(worst, max(abs(L[0, i] - lk[i]) for i in range(len(J))))
    lam_c = sum(abs(x) for x in (mp.matrix([[mp.chebyt(A, -1) * mp.chebyt(Bb, -1) for (A, Bb) in basis]]) * Vi))
    res["mp_vdm"].append([n, float(worst), mp.nstr(lam_c, 20), float(corner_value(n))])

print(json.dumps(res, indent=1))
