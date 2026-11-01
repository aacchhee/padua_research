#!/usr/bin/env python3
"""Claude audit-01, A4(a) sub-audit: scope numerics (float64, SUPPORTING ONLY).

For moderate n, finds the largest interior local maximum of lambda_n restricted to
each of the four edges (edge formula 70, validated separately), and compares it with
R_cen(n) (central cell |t-pi/2|<=pi/m on x=+-1).  Also evaluates the literal edge
midpoints lambda_n(+-1,0) for even n, where the central cell's maxima sit at the
complementary ordinates pi/2 +- pi/(2m) instead.  None of this is used as a premise.
Imports the audit's own audit_a4_rcen.py helpers (not developer code).
"""
import json, sys, time, importlib.util, os
import numpy as np
from scipy.optimize import minimize_scalar

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rc", os.path.join(here, "audit_a4_rcen.py"))
rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
PI = np.pi

def interior_local_maxima(f, G):
    ts = np.linspace(0, PI, G)
    vals = np.array([f(t) for t in ts])
    out = []
    for i in range(1, G - 1):
        if vals[i] >= vals[i - 1] and vals[i] >= vals[i + 1]:
            r = minimize_scalar(lambda t: -f(t), bounds=(ts[i - 1], ts[i + 1]), method="bounded",
                                options={"xatol": 1e-12})
            out.append((-r.fun, float(r.x)))
    return sorted(out, reverse=True)

t0 = time.time()
res = []
for n in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 24, 25, 32, 33, 48, 49, 64, 65]:
    P = rc.Padua(n); m = n + 1
    G = max(1201, 40 * m)
    edges = {"x=+1": lambda t: P.lam_xedge(1, t), "x=-1": lambda t: P.lam_xedge(-1, t),
             "y=+1": lambda t: P.lam_yedge(0.0, t), "y=-1": lambda t: P.lam_yedge(PI, t)}
    best = {}
    for name, f in edges.items():
        lm = interior_local_maxima(f, G)
        best[name] = {"value": lm[0][0], "angle": lm[0][1], "angle_minus_pi2_units_pi_over_m": (lm[0][1] - PI / 2) * m / PI} if lm else None
    Lc = max(P.lam_xedge(1, 0.0), P.lam_xedge(1, PI), P.lam_xedge(-1, 0.0), P.lam_xedge(-1, PI))
    lo, hi = PI / 2 - PI / m, PI / 2 + PI / m
    Rc = max(rc.maximize_on(lambda t: P.lam_xedge(e, t), lo, hi, 201)[1] for e in (1, -1))
    top_edge = max(best.items(), key=lambda kv: kv[1]["value"])
    rec = {"n": n, "Lambda_c": Lc, "R_cen": Rc, "best_interior_edge_local_max": best,
           "largest_edge_local_max_edge": top_edge[0], "largest_edge_local_max_value": top_edge[1]["value"],
           "R_cen_equals_largest_edge_local_max": bool(abs(top_edge[1]["value"] - Rc) < 1e-9)}
    if n % 2 == 0:
        rec["literal_midpoints_even_n"] = {"(1,0)": P.lam_xedge(1, PI / 2), "(-1,0)": P.lam_xedge(-1, PI / 2)}
    res.append(rec)
    print(f"n={n} Lc={Lc:.6f} Rcen={Rc:.6f} top={top_edge[0]}:{top_edge[1]['value']:.6f} t={time.time()-t0:.0f}s",
          file=sys.stderr, flush=True)
print(json.dumps({"script": "audit_a4_edges_scope.py", "records": res, "elapsed_seconds": round(time.time() - t0, 2)}, indent=1))
