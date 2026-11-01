"""L5 response to Codex audit-01 (findings M1, L2): paired slope differences and lockstep non-monotonicity, from the committed logs only.
usage: python3 -I analyze_r01d.py LOGDIR   (LOGDIR = directions/L5/logs; reads r01_*.jsonl and r02_dual.jsonl; no new experiment)

Part 1 (M1). For a pair of methods (A, B) and a family / order class: per instance d = log10(err_A / err_B), per-size mean of d over the
replicates, OLS of that size-mean series on log10(M); 95% t-interval with df = sizes - 2 (the same convention as analyze_r01c.py). Because
the OLS slope is linear in the response and the size-mean of d equals mean(log10 err_A) - mean(log10 err_B), the fitted slope of d is
exactly slope(A) - slope(B); the Householder-normalised slopes of analyze_r01c.py are the pairs (A, hh), and their difference
(G/hh) - (HL/hh) is the unnormalised pair (G, HL). The intervals are DESCRIPTIVE size-level intervals: the sizes share nodes, the log-log
curves are partly convex, and the number of sizes is 5-7; they are not a significance test and carry no causal reading.

Part 2 (L2). For every record of r02_dual.jsonl (double vs long-double Givens-scheme in lockstep) list the consecutive checkpoints at
which the relative Frobenius difference decreases ('local decreases'), and the overall log-log slope in i recorded by the producer.
"""
import sys, json, collections
import numpy as np
from scipy import stats
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyze_r01 import load

KEY = {"G": "givens-scheme", "HL": "hl", "CGS2": "cgs2", "HH": "hh", "BJ": "bj"}
PAIRS = [("G", "HL"), ("G", "CGS2"), ("G", "HH"), ("HL", "HH"), ("CGS2", "HH"), ("HL", "CGS2")]


def classes(fam, rs):
    """same order classes as analyze_r01c.py (not imported: that module runs its main() at import)"""
    if fam.startswith("padua"):
        return {"all5": rs, "structured": [r for r in rs if r["order"] in ("given", "sortx")], "random": [r for r in rs if r["order"].startswith("rand")]}
    return {"all": rs}


def sizefit(Ms, ys):
    x = np.log10(np.asarray(Ms, float)); y = np.asarray(ys, float); n = len(x)
    if n < 3:
        return None
    r = stats.linregress(x, y); t = stats.t.ppf(0.975, n - 2)
    return r.slope, r.slope - t * r.stderr, r.slope + t * r.stderr, n - 2


def paired(rs, a, b, lo=0):
    by = collections.defaultdict(list)
    for r in rs:
        if r["M"] < lo or KEY[a] not in r or KEY[b] not in r:
            continue
        by[r["M"]].append(np.log10(r[KEY[a]] / r[KEY[b]]))
    Ms = sorted(by)
    return sizefit(Ms, [np.mean(by[M]) for M in Ms])


def marginal(rs, a, lo=0):
    by = collections.defaultdict(list)
    for r in rs:
        if r["M"] < lo or KEY[a] not in r:
            continue
        by[r["M"]].append(np.log10(r[KEY[a]]))
    Ms = sorted(by)
    return sizefit(Ms, [np.mean(by[M]) for M in Ms])


def main():
    logdir = sys.argv[1]
    recs = load(logdir)
    fams = collections.defaultdict(list)
    for r in recs:
        if r["order"] == "gepp" or r["order"].startswith("rpiv"):
            continue
        fams[r["family"]].append(r)
    print("PAIRED SLOPE DIFFERENCES slope(A) - slope(B) = OLS slope of the size-mean of log10(err_A/err_B) vs log10 M;")
    print("95% t-interval, df = sizes - 2 (descriptive, size level; NOT a significance test, no causal reading).")
    print("check = slope(A) - slope(B) from the marginal fits (must equal the paired slope to rounding).\n")
    for fam, rs in sorted(fams.items()):
        for cname, crs in classes(fam, rs).items():
            print(f"== {fam} / {cname}: sizes {sorted(set(r['M'] for r in crs))}")
            for A, B in PAIRS:
                f = paired(crs, A, B)
                ma, mb = marginal(crs, A), marginal(crs, B)
                chk = ma[0] - mb[0]
                print(f"   {A:>4s} - {B:<4s} {f[0]:6.3f} [{f[1]:6.3f}, {f[2]:6.3f}] (df {f[3]})  check {chk:6.3f}  "
                      f"{'interval contains 0' if f[1] <= 0 <= f[2] else 'interval excludes 0'}")
            print()
    print("\nLOCKSTEP (r02_dual.jsonl): consecutive-checkpoint decreases of the relative Frobenius difference, double vs long double")
    for line in open(logdir + "/r02_dual.jsonl"):
        r = json.loads(line)
        if r.get("meta"):
            continue
        ck, v = r["ckpt"], r["relfro"]
        dec = [(ck[k], ck[k + 1], v[k], v[k + 1]) for k in range(len(v) - 1) if v[k + 1] < v[k]]
        print(f"n={r['size']:2d} {r['order']:6s} checkpoints {len(v)}  local decreases {len(dec)}  producer slope_in_i {r.get('slope_in_i', float('nan')):+.3f}")
        if r["order"] == "gepp":
            for i0, i1, a, b in dec:
                print(f"      i {i0} -> {i1}: {a:.7e} -> {b:.7e}")


main()
