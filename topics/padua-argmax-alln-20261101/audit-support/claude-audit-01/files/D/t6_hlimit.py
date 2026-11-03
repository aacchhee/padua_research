"""MEASURED consistency check of theory16 (1): horizontal-edge gap Lambda_c - max_{theta in I} lambda(cos theta, eps)
versus min_I g_h, with g_h computed by midpoint quadrature of codex-05/theory16's integral.  Finite-n only;
the theorem is an o(1) statement and this is not a proof of anything.
"""
import sys, os, json
import numpy as np
from scipy.optimize import minimize_scalar
sys.path.insert(0, os.path.dirname(__file__))
from padlib import *


def g_h(t, Na=3000, Nb=3000):
    a = (np.arange(Na) + 0.5) * PI / Na
    b = (np.arange(Nb) + 0.5) * PI / Nb
    B = np.cos(b)[None, :]
    zp = np.cos(t + a)[:, None]; zm = np.cos(t - a)[:, None]
    inside = (zp < B) & (B < zm)
    h = np.where(inside, (1 + B) * np.minimum(1 / np.where(inside, B - zp, 1), 1 / np.where(inside, zm - B, 1)), 0.0)
    return 2 / PI**2 * h.sum() * (PI / Na) * (PI / Nb)


out = {"I": None, "g_h": [], "edges": []}
A, Bend = PI / 4, 3 * PI / 4
out["I"] = [A, Bend]
ts = np.linspace(A, Bend, 21)
gs = [g_h(t) for t in ts]
gs2 = [g_h(t, 6000, 6000) for t in ts[::5]]
out["g_h"] = [[float(t), float(g)] for t, g in zip(ts, gs)]
out["g_h_refined_check"] = [[float(t), float(g)] for t, g in zip(ts[::5], gs2)]
gmin = min(gs)
print("g_h on I:", [round(g, 5) for g in gs], "min", gmin, flush=True)
for n in (25, 50, 100, 200, 400):
    m = n + 1
    Lc = corner_value(n)
    rec = {"n": n, "Lambda_c": Lc}
    for eps, ph in ((1, 0.0), (-1, PI)):
        th = np.linspace(A, Bend, 40 * n + 1)
        lam = lebesgue(n, th, np.full_like(th, ph))
        i = int(lam.argmax())
        lo, hi = th[max(i - 1, 0)], th[min(i + 1, len(th) - 1)]
        r = minimize_scalar(lambda x: -lebesgue(n, [x], [ph])[0], bounds=(lo, hi), method="bounded", options={"xatol": 1e-12})
        mx = max(-r.fun, lam[i])
        rec["eps%+d" % eps] = {"max": float(mx), "argmax_theta": float(r.x), "gap": float(Lc - mx)}
    rec["min_I_g_h"] = gmin
    out["edges"].append(rec)
    print(rec, flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "t6_hlimit.json"), "w"), indent=1)
