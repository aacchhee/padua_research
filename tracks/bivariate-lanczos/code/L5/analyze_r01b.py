"""L5 R01 part B analysis: join prefix statistics (exp_r01b.py) with 'largest'/'scheme' errors (exp_r01.py, exp_r01b.py).
usage: python3 -I analyze_r01b.py LOGDIR
Definitions (candidates.md IDEA 502): catastrophe = err(largest) >= 1e3 * err(scheme) and >= 1e-10.
non-unisolvent order = at least one prefix K with certified sigma_min < 1e-11 ('sing'); 'unisolvent order' = none.
'well-conditioned unisolvent' = none sing and exact min sigma >= 1e-8 (the tolerance pre-registered in candidates.md).
"""
import sys, glob, json, collections
import numpy as np
from scipy import stats

def main():
    logdir = sys.argv[1]
    pre = {}; err = {}
    for f in sorted(glob.glob(logdir + "/r01_*.jsonl")):
        for line in open(f):
            r = json.loads(line)
            if r.get("meta"): continue
            if r.get("kind") == "prefix": pre[(r["n"], r["order"])] = r
            elif "givens-largest" in r and r["family"] in ("padua_cub", "padua_rand"):
                n = r.get("n"); err[(r["family"], n, r["order"])] = (r["givens-scheme"], r["givens-largest"])
    rows = []
    for (fam, n, lab), (es, el) in sorted(err.items()):
        p = pre.get((n, lab))
        if p is None: continue
        mex = p["min_exact_refined"]
        rows.append(dict(fam=fam, n=n, order=lab, nsing=p["n_sing"], namb=p["n_amb"], minsig=mex, es=es, el=el, ratio=el / es,
                         cat=(el >= 1e3 * es and el >= 1e-10), first_sing=p["first_sing"], n_below_1e8=p["n_below_1e8"]))
    print(f"{'fam':10s} {'n':>3s} {'order':6s} {'nsing':>5s} {'minsig':>9s} {'scheme':>9s} {'largest':>9s} {'ratio':>9s} cat")
    for r in rows:
        print(f"{r['fam']:10s} {r['n']:3d} {r['order']:6s} {r['nsing']:5d} {r['minsig']:9.1e} {r['es']:9.1e} {r['el']:9.1e} {r['ratio']:9.1e} {'CAT' if r['cat'] else ''}")
    print("\n2x2 table over all joined (family, n, order) rows with n >= 20: rows = catastrophe, cols = non-unisolvent order (nsing > 0)")
    tab = collections.Counter()
    for r in rows:
        if r["n"] < 20: continue
        tab[(r["cat"], r["nsing"] > 0)] += 1
    for cat in (True, False):
        print(f"  catastrophe={cat!s:5s}: non-unisolvent {tab[(cat, True)]:3d}   all-prefixes-unisolvent {tab[(cat, False)]:3d}")
    kill = [r for r in rows if r["cat"] and r["nsing"] == 0 and r["n"] >= 20]
    print("\nKILL TEST (catastrophe on an all-unisolvent order, n>=20):", "FIRES" if kill else "does not fire", len(kill), "orders")
    for r in kill: print("   ", r["fam"], r["n"], r["order"], f"min sigma {r['minsig']:.1e} ratio {r['ratio']:.1e} largest {r['el']:.1e}")
    strict = [r for r in kill if r["minsig"] >= 1e-8]
    print("   of which with exact min sigma >= 1e-8 (pre-registered tolerance):", len(strict))
    rr = [r for r in rows if r["n"] >= 20]
    x = np.log10([max(r["minsig"], 1e-17) for r in rr]); y = np.log10([r["ratio"] for r in rr])
    print("\nSpearman(log10 min-sigma, log10 largest/scheme), all n>=20 rows:", stats.spearmanr(x, y))
    uni = [r for r in rr if r["nsing"] == 0]
    if len(uni) > 3:
        x = np.log10([r["minsig"] for r in uni]); y = np.log10([r["ratio"] for r in uni])
        print("Spearman among all-unisolvent orders only:", stats.spearmanr(x, y))
    print("\nper n: median log10(ratio) by order class")
    for n in sorted(set(r["n"] for r in rows)):
        d = collections.defaultdict(list)
        for r in rows:
            if r["n"] == n:
                cls = "gepp/rpiv" if (r["order"] == "gepp" or r["order"].startswith("rpiv")) else ("rand" if r["order"].startswith("rand") else r["order"])
                d[cls].append(r["ratio"])
        print(f"  n={n:3d} " + "  ".join(f"{k}: {np.median(v):.1e}(k={len(v)})" for k, v in sorted(d.items())))

if __name__ == "__main__":
    main()
