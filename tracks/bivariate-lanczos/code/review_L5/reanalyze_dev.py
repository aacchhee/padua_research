"""Re-analysis (review, not a rerun) of the developer's R01 logs: slope uncertainty and conditioning confound.
usage: python3 -I reanalyze_dev.py DEV_LOGDIR
For each family/method: (1) developer-style pooled OLS slope; (2) slope of the size-level geometric means with a
t-interval on (#sizes - 2) df (sizes are the effective sample); (3) quadratic term in log-log (curvature, t-stat);
(4) for every family, slopes of error RATIOS to Householder on the same instance (a per-instance conditioning control).
"""
import sys, json, glob, collections
import numpy as np
from scipy import stats

METH = ["givens-scheme", "givens-largest", "hl", "bj", "cgs2", "hh"]

def load(d):
    R = collections.defaultdict(list)
    for f in sorted(glob.glob(d + "/r01_*.jsonl")):
        if "prefix" in f: continue
        for line in open(f):
            r = json.loads(line)
            if r.get("meta") or "givens-scheme" not in r: continue
            R[r["family"]].append(r)
    return R

def ols(lx, ly):
    res = stats.linregress(lx, ly); t = stats.t.ppf(0.975, len(lx) - 2)
    return res.slope, res.slope - t * res.stderr, res.slope + t * res.stderr

def quad(lx, ly):
    X = np.column_stack([np.ones_like(lx), lx - lx.mean(), (lx - lx.mean()) ** 2])
    beta, *_ = np.linalg.lstsq(X, ly, rcond=None); r = ly - X @ beta
    s2 = r @ r / (len(ly) - 3); cov = s2 * np.linalg.inv(X.T @ X)
    return beta[2], beta[2] / np.sqrt(cov[2, 2])

def main():
    R = load(sys.argv[1])
    for fam, rs in sorted(R.items()):
        sizes = sorted(set(r["M"] for r in rs))
        print(f"\n=== {fam}: sizes {sizes}, {len(rs)} runs")
        for sel_name, sel in (("all orders", None), ("structured", ("given", "sortx")), ("random orders", ("rand1", "rand2", "rand3"))):
            if sel is not None and not fam.startswith("padua"): continue
            rr = [r for r in rs if sel is None or r["order"] in sel]
            print(f" -- {sel_name}")
            for m in METH:
                M = np.array([r["M"] for r in rr], float); E = np.array([r[m] for r in rr], float)
                lx, ly = np.log(M), np.log(E)
                s_pool = ols(lx, ly)
                gm = np.array([np.mean(ly[M == s]) for s in sizes]); ls = np.log(np.array(sizes, float))
                s_gm = ols(ls, gm)
                q, qt = quad(ls, gm) if len(sizes) >= 4 else (np.nan, np.nan)
                # ratio to Householder on the same instance
                Er = np.array([r[m] / r["hh"] for r in rr]); gr = np.array([np.mean(np.log(Er)[M == s]) for s in sizes])
                s_r = ols(ls, gr)
                print(f"   {m:15s} pooled {s_pool[0]:5.2f} [{s_pool[1]:5.2f},{s_pool[2]:5.2f}]  size-means {s_gm[0]:5.2f} "
                      f"[{s_gm[1]:5.2f},{s_gm[2]:5.2f}] (df {len(sizes)-2})  curvature {q:+.3f} (t {qt:+.1f})   ratio-to-HH slope {s_r[0]:+5.2f} [{s_r[1]:+5.2f},{s_r[2]:+5.2f}]")
        if "cond" in rs[0]:
            M = np.array([r["M"] for r in rs], float); c = np.array([r["cond"] for r in rs])
            gc = np.array([np.mean(np.log(c[M == s])) for s in sizes])
            print(f"   cond slope (size means) {ols(np.log(np.array(sizes, float)), gc)[0]:.2f}")

if __name__ == "__main__":
    main()
