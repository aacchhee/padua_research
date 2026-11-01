"""Analysis of the auditor's own runs (exp_review.py logs).  usage: python3 -I analyze_review.py LOGDIR"""
import sys, json, collections
import numpy as np
from scipy import stats

def load(p):
    return [r for r in (json.loads(l) for l in open(p)) if not r.get("meta")]

def ols(lx, ly):
    res = stats.linregress(lx, ly); t = stats.t.ppf(0.975, len(lx) - 2)
    return res.slope, res.slope - t * res.stderr, res.slope + t * res.stderr

def slopes(rs, sel, meth, lo=0):
    rr = [r for r in rs if r["order"] in sel and r["M"] >= lo]
    M = np.array([r["M"] for r in rr], float); E = np.log(np.array([r[meth] for r in rr], float))
    sizes = sorted(set(M)); gm = np.array([E[M == s].mean() for s in sizes]); ls = np.log(sizes)
    out = dict(pooled=ols(np.log(M), E), means=ols(ls, gm) if len(sizes) > 2 else (np.nan,) * 3)
    if len(sizes) >= 4:
        X = np.column_stack([np.ones_like(ls), ls - ls.mean(), (ls - ls.mean()) ** 2]); b, *_ = np.linalg.lstsq(X, gm, rcond=None)
        out["curv"] = b[2]
    return out

def main():
    d = sys.argv[1]
    rs = load(d + "/a_slopes.jsonl")
    print("=== (a) Padua cubature weights, auditor's implementation; sizes", sorted(set(r["M"] for r in rs)))
    print(f"{'M':>5s} {'order':6s} {'scheme':>9s} {'largest':>9s} {'hl':>9s} {'cgs2':>9s} {'hh':>9s}  min_up(prefix sigma upper bd)")
    for r in sorted(rs, key=lambda r: (r["M"], r["order"])):
        print(f"{r['M']:5d} {r['order']:6s} {r['scheme']:9.2e} {r['largest']:9.2e} {r['hl']:9.2e} {r['cgs2']:9.2e} {r['hh']:9.2e}  {r.get('min_up', float('nan')):.1e}")
    classes = (("5 orders (given,sortx,r1-r3)", ("given", "sortx", "r1", "r2", "r3")), ("structured", ("given", "sortx")),
               ("random r1-r3", ("r1", "r2", "r3")), ("gepp", ("gepp",)))
    for lo, lab in ((0, "full range"), (496, "M >= 496")):
        print(f"\nslopes, {lab}: pooled OLS [95% t] | size-means OLS [95% t, df = #sizes-2] | curvature")
        for cname, sel in classes:
            for m in ("scheme", "largest", "hl", "cgs2", "hh"):
                s = slopes(rs, sel, m, lo)
                p, q = s["pooled"], s["means"]
                print(f"  {cname:28s} {m:8s} {p[0]:6.2f} [{p[1]:5.2f},{p[2]:5.2f}] | {q[0]:6.2f} [{q[1]:5.2f},{q[2]:5.2f}] | {s.get('curv', np.nan):+.2f}")
    print("\nkill test as written (Givens-scheme slope <= 0.7, or HL or CGS2 slope >= 0.9), 5-order pooled:")
    for lo, lab in ((0, "full"), (496, "upper")):
        g = slopes(rs, classes[0][1], "scheme", lo)["pooled"][0]; h = slopes(rs, classes[0][1], "hl", lo)["pooled"][0]
        c = slopes(rs, classes[0][1], "cgs2", lo)["pooled"][0]
        print(f"  {lab}: Givens {g:.2f} HL {h:.2f} CGS2 {c:.2f} -> {'KILLED' if (g <= 0.7 or h >= 0.9 or c >= 0.9) else 'not killed'}")
    try:
        ks = load(d + "/b_kill.jsonl")
    except FileNotFoundError:
        ks = []
    if ks:
        print("\n=== (b) all-prefix-unisolvent orders (GEPP-type), cubature weights")
        print(f"{'n':>3s} {'order':7s} {'min_lo':>8s} {'min_up':>8s} {'scheme':>9s} {'largest':>9s} {'ratio':>8s} CAT  bkw_s    bkw_l    q0_l     sdef_s   sdef_l")
        for r in ks:
            ratio = r["largest"] / r["scheme"]; cat = ratio >= 1e3 and r["largest"] >= 1e-10
            print(f"{r['n']:3d} {r['order']:7s} {r['min_lo']:8.1e} {r['min_up']:8.1e} {r['scheme']:9.2e} {r['largest']:9.2e} {ratio:8.1e} {'CAT' if cat else '   '}  "
                  f"{r['bkw_scheme']:.1e}  {r['bkw_largest']:.1e}  {r['q0_largest']:.1e}  {r['sdef_scheme']:.1e}  {r['sdef_largest']:.1e}")
    for f in ("c_repro60.jsonl", "d_unif.jsonl"):
        try:
            for r in load(d + "/" + f): print(f, json.dumps({k: (f"{v:.2e}" if isinstance(v, float) else v) for k, v in r.items()}))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    main()
