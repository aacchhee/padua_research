#!/usr/bin/env python3
"""Aggregate scratchpad run receipts into the small evidence files (lp-torus.json, lp-lattice.json, lp-cube.json).
Usage: lp_report.py --scratch DIR --evidence DIR"""
import argparse, glob, hashlib, json, os, re, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--scratch", required=True)
ap.add_argument("--evidence", required=True)
a = ap.parse_args()
sha = hashlib.sha256(open(__file__, "rb").read()).hexdigest()

# ---- torus
rows = []
shas = set()
for f in sorted(glob.glob(os.path.join(a.scratch, "runs", "n*_e*.json"))):
    d = json.load(open(f))
    r = d["result"]; shas.add(d["script_sha256"])
    eps_m = max(0.0, -r["lp"]["min_found_over_f0"] * r["R_upper_gridLP"])
    rows.append(dict(R_lower_measured=round((r["R_upper_gridLP"] + eps_m) / (1 + eps_m), 6), n=r["n"], extra=r["extra"], K=r["K"], m_n=r["m_n"], R_upper=round(r["R_upper_gridLP"], 6),
                     rho_upper=round(r["rho_upper"], 6), R_lower_bnb=round(r["R_lower_validated_bnb"], 4),
                     bnb_complete=r["bnb"]["complete"],
                     eps_found=round(-r["lp"]["min_found_over_f0"] * r["R_upper_gridLP"], 12),
                     lp_iters=r["lp"]["iterations"], lp_converged=r["lp"]["converged"],
                     seconds=round(r["timings"]["total_s"], 1)))
rows.sort(key=lambda x: (x["n"], x["extra"]))
# lattice
lat = []
for f in sorted(glob.glob(os.path.join(a.scratch, "lat_*.json"))):
    d = json.load(open(f))
    for e in d["results"]:
        if e.get("M"):
            lat.append(dict(n=e["n"], m_n=e["m_n"], M=e["M"], ratio=round(e["M_over_m"], 6), kind=e["kind"], basis=e["basis"], source=os.path.basename(f), sha=d["script_sha256"][:12]))
best = {}
for e in lat:
    if e["n"] not in best or e["M"] < best[e["n"]]["M"] or (e["M"] == best[e["n"]]["M"] and e["kind"].startswith("EXACT")):
        best[e["n"]] = e
lat_best = [best[k] for k in sorted(best)]
# cap check
viol = []
Mn = {e["n"]: e["M"] for e in lat_best}
for r in rows:
    if r["n"] in Mn and r["R_upper"] > Mn[r["n"]] + 1e-6:
        viol.append((r["n"], r["extra"], r["R_upper"], Mn[r["n"]]))
    if r["R_upper"] < r["m_n"] - 1e-6:
        viol.append(("below Fisher", r["n"], r["extra"], r["R_upper"], r["m_n"]))
json.dump(dict(script_sha256=sha, torus_script_sha256=sorted(shas), note="R_upper = optimum of the cut-plane LP on a finite point set (UPPER bound for the continuum LP once min f >= -1e-10 f(0) is reached); R_lower_measured = (f(0)+eps)/(1+eps) with eps = -(min of f found by FFT grid + Newton refinement), NOT rigorous; R_lower_bnb = second-order branch-and-bound validated lower bound (weak; R_n >= m_n holds exactly via |D_n|^2); MEASURED.",
               cap_violations=viol, rows=rows), open(os.path.join(a.evidence, "lp-torus.json"), "w"), indent=0, separators=(",", ":"))
json.dump(dict(script_sha256=sha, note="exact = exhaustive over all HNF of each index in [m_n, M]; others upper bounds via rank-1 random search; all re-verified by exact integer enumeration",
               rows=lat_best), open(os.path.join(a.evidence, "lp-lattice.json"), "w"), indent=0, separators=(",", ":"))
cube = []
for f in sorted(glob.glob(os.path.join(a.scratch, "cube[0-9].json"))):
    d = json.load(open(f))
    if "result" in d:
        r = d["result"]; r.pop("history_tail", None); r["script_sha256"] = d["script_sha256"]; cube.append(r)
q = os.path.join(a.scratch, "cube_q1a.json")
json.dump(dict(script_sha256=sha, results=cube, q1a=json.load(open(q))["q1a"] if os.path.exists(q) else None,
               q1a_torus=json.load(open(os.path.join(a.scratch, "q1a.json")))["q1a"] if os.path.exists(os.path.join(a.scratch, "q1a.json")) else None),
          open(os.path.join(a.evidence, "lp-cube.json"), "w"), indent=0, separators=(",", ":"))
# best Delsarte f
bestf = None
for r in rows:
    if r["extra"] > 0 and (bestf is None or (r["n"], r["rho_upper"]) > (bestf["n"], bestf["rho_upper"])):
        bestf = r
if bestf:
    z = np.load(os.path.join(a.scratch, f"torus_f_n{bestf['n']}_e{bestf['extra']}.npz"))
    corb, reps = z["corb"], z["reps"]
    out = dict(n=bestf["n"], extra=bestf["extra"], rho_upper=bestf["rho_upper"], R_upper=bestf["R_upper"],
               convention="f(t)=sum_O c_O sum_{k in O} cos(k.t), O = B3 orbit of rep k (sorted desc, nonneg); c_{000}=1",
               orbits=[[list(map(int, k)), round(float(c), 10)] for k, c in zip(reps, corb)])
    s = json.dumps(out, separators=(",", ":"))
    if len(s) < 16000:
        open(os.path.join(a.evidence, "lp-torus-delsarte-best.json"), "w").write(s)
        print("saved best f", len(s))
    else:
        print("best f too large for evidence:", len(s))
print("violations:", viol)
