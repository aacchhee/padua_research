"""L5 post-review re-analysis (response to reconstruction 01, findings M2, M3): size-level slopes with honest degrees of freedom, curvature,
per-order-class slopes, and the Householder-normalised comparison (post-hoc, secondary).
usage: python3 -I analyze_r01c.py LOGDIR
For each family / order class / method: the per-size mean of log10(error) over the replicates; OLS of those size means on log10(M)
(df = number of sizes - 2, t-interval); the quadratic coefficient of the same fit in x = log10(M/M0) with its t-statistic (df = sizes - 3);
'upper' = M >= 496. Normalised: per instance log10(err/err_hh) (err_hh = Householder error of the same instance), then the same fit."""
import sys, glob, json, collections
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyze_r01 import load, METHODS

def sizefit(Ms, ys, quad=True):
    """Ms: list of sizes; ys: list of per-size mean log10 error. returns slope, ci, quad coef, t(quad)"""
    x = np.log10(np.asarray(Ms, float)); y = np.asarray(ys, float); n = len(x)
    if n < 3: return None
    r = stats.linregress(x, y); t = stats.t.ppf(0.975, n - 2)
    out = [r.slope, r.slope - t * r.stderr, r.slope + t * r.stderr, np.nan, np.nan]
    if quad and n >= 4:
        xc = x - x.mean(); A = np.vstack([np.ones(n), xc, xc ** 2]).T
        beta, res, rk, sv = np.linalg.lstsq(A, y, rcond=None)
        s2 = ((y - A @ beta) ** 2).sum() / (n - 3); cov = s2 * np.linalg.inv(A.T @ A)
        out[3] = beta[2]; out[4] = beta[2] / np.sqrt(cov[2, 2])
    return out

def classes(fam, rs):
    if fam.startswith("padua"):
        return {"all5": rs, "structured": [r for r in rs if r["order"] in ("given", "sortx")], "random": [r for r in rs if r["order"].startswith("rand")]}
    return {"all": rs}

def table(rs, methods, norm=False, lo=0):
    out = {}
    for m in methods:
        by = collections.defaultdict(list)
        for r in rs:
            if r["M"] < lo or m not in r: continue
            v = np.log10(r[m] / r["hh"]) if norm else np.log10(r[m])
            by[r["M"]].append(v)
        Ms = sorted(by)
        out[m] = sizefit(Ms, [np.mean(by[M]) for M in Ms]) , len(Ms)
    return out

def fmt(t):
    f, k = t
    if f is None: return "n/a"
    s = f"{f[0]:5.2f} [{f[1]:5.2f},{f[2]:5.2f}] (df {k-2})"
    if not np.isnan(f[3]): s += f" quad {f[3]:+.2f} (t={f[4]:+.1f})"
    return s

def main():
    recs = load(sys.argv[1]); fams = collections.defaultdict(list)
    for r in recs:
        if r["order"] == "gepp" or r["order"].startswith("rpiv"): continue
        fams[r["family"]].append(r)
    print("SIZE-LEVEL slopes (OLS on per-size mean log10 error vs log10 M; 95% t-interval with df = sizes-2; quad = curvature in log-log)")
    for fam, rs in sorted(fams.items()):
        for cname, crs in classes(fam, rs).items():
            print(f"\n== {fam} / {cname}: sizes {sorted(set(r['M'] for r in crs))}")
            for rng_name, lo in (("full", 0), ("upper(M>=496)", 496)):
                T = table(crs, METHODS, False, lo)
                print(f"  [{rng_name}]")
                for m in METHODS: print(f"    {m:15s} {fmt(T[m])}")
    print("\n\nHOUSEHOLDER-NORMALISED (post-hoc, secondary): per instance log10(err/err_hh), then size-level fit")
    for fam, rs in sorted(fams.items()):
        for cname, crs in classes(fam, rs).items():
            if cname not in ("all5", "all"): continue
            print(f"\n== {fam} / {cname}")
            for rng_name, lo in (("full", 0), ("upper(M>=496)", 496)):
                T = table(crs, [m for m in METHODS if m != "hh"], True, lo)
                print(f"  [{rng_name}]")
                for m in T: print(f"    {m:15s} {fmt(T[m])}")
main()
