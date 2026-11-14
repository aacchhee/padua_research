#!/usr/bin/env python3
"""MEASURED guidance for the sharp constant: analyse evidence/mp-corner-values.json (lambda_n(1,1), even n <= 2000).
Appends an "analysis" block to that file.  Usage: python3 corner_analysis.py [--heuristic C] [--file ../../evidence/mp-corner-values.json]
Everything here is numerical (G5: no constant is set by these fits)."""
import argparse, json, numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="../../evidence/mp-corner-values.json")
    ap.add_argument("--heuristic", type=float, default=None, help="value of the heuristic constant from corner_limit_heuristic.py")
    a = ap.parse_args()
    d = json.load(open(a.file))
    lam = np.array(d["lam11_16sig"]); ns = np.arange(2, 2 * len(lam) + 1, 2).astype(float)
    r = lam / ns ** 2
    s = lam / ((ns + 1) * (ns + 2) / 2)
    pick = [10, 20, 50, 100, 200, 500, 1000, 1500, 2000]
    tab = [{"n": n, "lam/n^2": float("%.12g" % r[n // 2 - 1]), "lam/T": float("%.12g" % s[n // 2 - 1])} for n in pick]
    diffs = []
    for n in (100, 500, 1000, 1998):
        i = n // 2 - 1
        diffs.append({"n": n, "d(lam/n^2)": float("%.6g" % (r[i + 1] - r[i])), "d(lam/T)": float("%.6g" % (s[i + 1] - s[i])),
                      "d2(lam/n^2)": float("%.6g" % (r[i + 1] - 2 * r[i] + r[i - 1]))})
    fits = {}
    for n0 in (200, 500):
        sel = ns >= n0
        N = ns[sel]
        models = {
            "r = c + a/n + b/n^2 + e/n^3": [np.ones_like(N), 1 / N, 1 / N ** 2, 1 / N ** 3],
            "r = c + a/n + b log n/n + e/n^2 + f log n/n^2": [np.ones_like(N), 1 / N, np.log(N) / N, 1 / N ** 2, np.log(N) / N ** 2],
            "r = c + a/n + b/n^2 + e/n^3 + f/n^4": [np.ones_like(N), 1 / N, 1 / N ** 2, 1 / N ** 3, 1 / N ** 4],
        }
        for k, cols in models.items():
            X = np.vstack(cols).T
            coef, *_ = np.linalg.lstsq(X, r[sel], rcond=None)
            fits["n>=%d: %s" % (n0, k)] = [float("%.10g" % t) for t in coef[:3]]
    # Richardson on (n, 2n, 4n): r = c + a/n + b/n^2
    rich = []
    for n in (250, 500):
        r1, r2, r3 = r[n // 2 - 1], r[n - 1], r[2 * n - 1]
        # eliminate a/n then b/n^2
        u1 = 2 * r2 - r1; u2 = 2 * r3 - r2
        c = (4 * u2 - u1) / 3
        rich.append({"n,2n,4n": [n, 2 * n, 4 * n], "c_Richardson": float("%.10g" % c)})
    est = fits["n>=200: r = c + a/n + b/n^2 + e/n^3 + f/n^4"][0]
    res = {"label": "MEASURED / conjectural (numerical fits never set a constant, G5)",
           "table": tab, "successive_differences": diffs, "fits_[c,a,b]": fits, "richardson": rich,
           "lim_lam/n^2_estimate": est,
           "lim_lam/T_estimate": float("%.10g" % (2 * est)),
           "model_note": "lam ~ c n^2 + a n + O(1): the fitted 1/n coefficient a ~ 1.58 is the second entry of each fit; a log n/n term is not needed (its fitted coefficient is ~1e-3 or less). lam/T is NOT monotone: it rises to a maximum ~1.03396 near n ~ 500 and then decreases toward 2c.",
           "heuristic_constant_(conjectural derivation, corner_limit_heuristic.py)": a.heuristic,
           "heuristic_formula": "c = (8/pi^3) sum_{e odd} int_0^1 sin(pi x) | -(1+cos pi x)/(e-x)^3 + (pi/2) sin(pi x)/(e-x)^2 | dx",
           "monotone_increasing_ratio_lam/T_up_to_2000": bool(np.all(np.diff(s[5:]) > 0)),
           "lam/T_exceeds_1_from_n": int(ns[np.argmax(s > 1)])}
    d["analysis"] = res
    json.dump(d, open(a.file, "w"), separators=(",", ":"))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
