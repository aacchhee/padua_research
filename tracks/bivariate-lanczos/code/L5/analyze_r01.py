"""L5 R01 analysis: log-log slopes (with uncertainty) of the relative H error vs M, kill-test verdicts, ratio tables.

usage: python3 -I analyze_r01.py LOGDIR   (reads LOGDIR/r01_*.jsonl)
Slope = OLS slope of log(err) on log(M) over all (order/seed) replicates of a (family, method); standard error from OLS residuals
(df = n-2) and a 95% interval from a cluster bootstrap that resamples the replicates within each size (4000 draws, seed 0).
Ranges: 'full' = all sizes (66..2016), 'upper' = M >= 496.
"""
import sys, glob, json, collections
import numpy as np
from scipy import stats

METHODS = ["givens-scheme", "givens-largest", "hl", "bj", "cgs2", "hh"]

def load(logdir):
    recs = []
    for f in sorted(glob.glob(logdir + "/r01_*.jsonl")):
        for line in open(f):
            r = json.loads(line)
            if r.get("meta") or r.get("kind") == "prefix": continue
            if r.get("kind") == "err" and r["order"] not in ("gepp",) and not r["order"].startswith("rpiv"): continue
            recs.append(r)
    return recs

def fit(M, E, nboot=4000, seed=0):
    M = np.asarray(M, float); E = np.asarray(E, float)
    lx, ly = np.log(M), np.log(E)
    res = stats.linregress(lx, ly)
    n = len(lx); t = stats.t.ppf(0.975, n - 2)
    sizes = sorted(set(M)); groups = [np.nonzero(M == s)[0] for s in sizes]
    rng = np.random.default_rng(seed); bs = []
    for _ in range(nboot):
        idx = np.concatenate([rng.choice(g, len(g)) for g in groups])
        if len(set(lx[idx])) < 2: continue
        bs.append(np.polyfit(lx[idx], ly[idx], 1)[0])
    return res.slope, res.stderr, (res.slope - t * res.stderr, res.slope + t * res.stderr), (np.percentile(bs, 2.5), np.percentile(bs, 97.5))

def main():
    logdir = sys.argv[1]
    recs = load(logdir)
    fams = collections.defaultdict(list)
    for r in recs:
        if r["order"] in ("gepp",) or r["order"].startswith("rpiv"): continue   # unisolvent-order runs are reported separately
        fams[r["family"]].append(r)
    verdict = {}
    for fam, rs in sorted(fams.items()):
        print(f"\n=== family {fam}: {len(rs)} runs; sizes {sorted(set(r['M'] for r in rs))}; replicates per size "
              f"{ {s: sum(1 for r in rs if r['M']==s) for s in sorted(set(r['M'] for r in rs))} }")
        sizes = sorted(set(r["M"] for r in rs))
        print("geometric-mean error by size:")
        print("   M     " + " ".join(f"{m:>15s}" for m in METHODS))
        for s in sizes:
            row = []
            for m in METHODS:
                e = [r[m] for r in rs if r["M"] == s and m in r]
                row.append(f"{np.exp(np.mean(np.log(e))):15.2e}")
            print(f"{s:6d} " + " ".join(row))
        print("slopes (OLS, SE, 95% t-interval, 95% cluster-bootstrap interval):")
        for rng_name, lo in (("full", 0), ("upper(M>=496)", 496)):
            print(f" range {rng_name}")
            for m in METHODS:
                pts = [(r["M"], r[m]) for r in rs if r["M"] >= lo and m in r and r[m] > 0]
                if len(set(p[0] for p in pts)) < 3: continue
                sl, se, ci, bci = fit([p[0] for p in pts], [p[1] for p in pts])
                verdict[(fam, rng_name, m)] = (sl, se, ci, bci)
                print(f"   {m:15s} slope {sl:6.2f}  SE {se:.2f}  t-CI [{ci[0]:5.2f},{ci[1]:5.2f}]  boot-CI [{bci[0]:5.2f},{bci[1]:5.2f}]")
        print("ratio of geometric means (Givens-scheme / X):")
        print("   M     " + " ".join(f"{m:>8s}" for m in ["hl", "cgs2", "hh", "bj"]))
        for s in sizes:
            g = lambda m: np.exp(np.mean(np.log([r[m] for r in rs if r["M"] == s])))
            print(f"{s:6d} " + " ".join(f"{g('givens-scheme')/g(m):8.1f}" for m in ["hl", "cgs2", "hh", "bj"]))
    print("\n=== kill test (plan L5-Q1; operational reading in candidates.md IDEA 501) ===")
    for fam in sorted(fams):
        for rng_name in ("full", "upper(M>=496)"):
            try:
                g = verdict[(fam, rng_name, "givens-scheme")][0]; h = verdict[(fam, rng_name, "hl")][0]; c = verdict[(fam, rng_name, "cgs2")][0]
            except KeyError: continue
            k1 = g <= 0.7; k2 = (h >= 0.9) or (c >= 0.9)
            print(f"{fam:11s} {rng_name:14s} Givens {g:5.2f} (<=0.7 kills: {k1})   HL {h:5.2f} CGS2 {c:5.2f} (>=0.9 kills: {k2})   => {'KILLED' if (k1 or k2) else 'not killed'}")

if __name__ == "__main__":
    main()
