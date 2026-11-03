"""(a) Local inequality of theory14 measured at moderate n near both nonnode corners.

R = (lambda - a*Lambda_c) / (rho^2 log(n+1))   (theory14 claims R <= 237000 for rho<=1/64)
Q = (Lambda_c - lambda) / (rho^2 Lambda_c)      (deficit relative to Lambda_c)
Evaluated by the direct physical kernel cardinals (validated vs Vandermonde), not by (3).
"""
import sys, json, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from padlib import *

ns = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [2, 3, 4, 5, 8, 10, 16, 20, 21, 30, 31, 50, 51, 64, 65, 100, 101, 150, 151, 200, 201]
rhos = [1e-4, 1e-3, 3e-3, 1e-2, 1 / 64, 0.03, 0.06, 0.125, 0.25, 0.5, 1.0, 2.0]
ts = np.linspace(0, 1, 21)
out = []
t0 = time.time()
for n in ns:
    m = n + 1
    Lc = corner_value(n)
    # second nonnode corner
    if n % 2 == 0:
        Lc2 = lebesgue(n, [0.0], [PI])[0]
    else:
        Lc2 = lebesgue(n, [PI], [0.0])[0]
    TH = []; PH = []; TH2 = []; PH2 = []; meta = []
    for rho in rhos:
        for t in ts:
            al = rho * t; be = rho * (1 - t)
            TH.append(PI - al / n); PH.append(PI - be / m)
            if n % 2 == 0:
                TH2.append(al / n); PH2.append(PI - be / m)
            else:
                TH2.append(PI - al / n); PH2.append(be / m)
            meta.append((rho, t, al, be))
    lam1 = lebesgue(n, TH, PH); lam2 = lebesgue(n, TH2, PH2)
    rec = {"n": n, "Lambda_c": Lc, "Lambda_c_other": Lc2, "PD-T157_lower": 4 / PI**2 * np.log(n)**2 - 54,
           "PD-T157_upper": 4 / PI**2 * np.log(n)**2 + 12 / PI * np.log(n) + 63, "by_rho": []}
    for rho in rhos:
        idx = [i for i, mm in enumerate(meta) if mm[0] == rho]
        Rs = []; Qs = []; strict = True
        for i in idx:
            _, t, al, be = meta[i]
            a = (np.cos(al) + np.cos(be)) / 2
            for lam in (lam1[i], lam2[i]):
                Rs.append((lam - a * Lc) / (rho**2 * np.log(n + 1)))
                Qs.append((Lc - lam) / (rho**2 * Lc))
                if not lam < Lc:
                    strict = False
        rec["by_rho"].append({"rho": rho, "R_max": max(Rs), "R_min": min(Rs), "Q_min": min(Qs), "Q_max": max(Qs),
                              "strict_below_corner_all_dirs": strict})
    out.append(rec)
    print(n, "Lc=%.12f" % Lc, "other=%.12f" % Lc2, "Rmax(rho<=1/64)=%.4f" % max(r["R_max"] for r in rec["by_rho"] if r["rho"] <= 1 / 64),
          "Qmin(rho<=1/64)=%.4f" % min(r["Q_min"] for r in rec["by_rho"] if r["rho"] <= 1 / 64), "t=%.1f" % (time.time() - t0), flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "t1_local.json"), "w"), indent=1)
