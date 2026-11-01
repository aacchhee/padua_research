#!/usr/bin/env python3
"""Claude audit-01, A4(a) sub-audit: n=3 scope check (supporting float64 numerics only).

Locates the largest noncorner values of lambda_3 on the closed square (angle grid +
local refinement, direct Vandermonde cardinals), to compare the historical searched
runner-up (~3.021223, MEASURED in the source) with C_3=8/3 and with R_cen(3).
Independent of developer code.
"""
import json, time
import numpy as np
from scipy.optimize import minimize

t0 = time.time()
n = 3; m = n + 1
nodes = [(np.cos(j * np.pi / n), np.cos(k * np.pi / m)) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]
basis = [(a, b) for a in range(n + 1) for b in range(n + 1 - a)]
def T(a, x):
    return np.cos(a * np.arccos(np.clip(x, -1, 1)))
V = np.array([[T(a, x) * T(b, y) for (a, b) in basis] for (x, y) in nodes])
Vinv = np.linalg.inv(V)
def lam_angles(th, ph):
    x, y = np.cos(th), np.cos(ph)
    phi = np.array([T(a, x) * T(b, y) for (a, b) in basis])
    return float(np.sum(np.abs(phi @ Vinv)))
G = 721
th = np.linspace(0, np.pi, G); ph = np.linspace(0, np.pi, G)
TH, PH = np.meshgrid(th, ph, indexing="ij")
X, Y = np.cos(TH), np.cos(PH)
Phi = np.stack([T(a, X) * T(b, Y) for (a, b) in basis], axis=-1)
Lam = np.sum(np.abs(Phi @ Vinv), axis=-1)
cands = []
for i in range(G):
    for j in range(G):
        v = Lam[i, j]
        nb = Lam[max(0, i - 1):i + 2, max(0, j - 1):j + 2]
        if v >= nb.max() - 1e-15:
            cands.append((v, i, j))
cands.sort(reverse=True)
res = []
seen = []
for (v, i, j) in cands[:60]:
    x0 = np.array([th[i], ph[j]])
    r = minimize(lambda z: -lam_angles(np.clip(z[0], 0, np.pi), np.clip(z[1], 0, np.pi)), x0, method="Nelder-Mead",
                 options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 4000})
    z = np.clip(r.x, 0, np.pi); val = -r.fun
    pt = (round(float(np.cos(z[0])), 6), round(float(np.cos(z[1])), 6))
    if any(abs(pt[0] - p[0]) < 1e-4 and abs(pt[1] - p[1]) < 1e-4 for p in seen):
        continue
    seen.append(pt)
    res.append({"x": pt[0], "y": pt[1], "theta": float(z[0]), "phi": float(z[1]), "value": val})
res.sort(key=lambda d: -d["value"])
corner = max(r_["value"] for r_ in res if abs(abs(r_["x"]) - 1) < 1e-6 and abs(abs(r_["y"]) - 1) < 1e-6)
noncorner = [r_ for r_ in res if not (abs(abs(r_["x"]) - 1) < 1e-6 and abs(abs(r_["y"]) - 1) < 1e-6)]
out = {"script": "audit_a4_n3.py", "n": 3, "Lambda_c_exact_claim": "17/6+(2/3)sqrt2", "Lambda_c_float": 17 / 6 + 2 / 3 * np.sqrt(2),
       "max_corner_found": corner, "top_noncorner_local_maxima": noncorner[:8],
       "C_3_midpoint_value_check": lam_angles(np.pi, np.pi / 2),
       "elapsed_seconds": round(time.time() - t0, 2)}
print(json.dumps(out, indent=1))
