import json, glob, os
rows = []
for fn in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "t3_global_*_K*.json"))):
    if fn.endswith("17_18_K4.json") or fn.endswith("17-40_K4.json"):
        continue  # timing trials, superseded by the full runs
    for r in json.load(open(fn)):
        b = r["best_refined"]; nc = r["best_noncorner"]
        rows.append((r["n"], r["K"], r["grid_shape"], r["Lambda_c"], r["max_over_cands_minus_Lc"], b["scaled_dist_nonnode_corner"],
                     r["grid_argmax"], r["gap_Lc_minus_best_noncorner"], nc["refined"] if nc else None, r["grid_direct_check_maxabs"], r["secs"]))
rows.sort()
print("n K grid Lambda_c bestcand-Lc best_scaled_dist_to_nonnode_corner grid_argmax(theta,phi) gap_to_best_noncorner best_noncorner(theta,phi) gridcheck secs")
for x in rows:
    print(x[0], x[1], "x".join(map(str, x[2])), "%.12f" % x[3], "%.1e" % x[4], "%.1e" % x[5], "(%.6f,%.6f)" % tuple(x[6]), "%.6f" % x[7],
          "(%.6f,%.6f)" % tuple(x[8]) if x[8] else None, "%.1e" % x[9], "%.0f" % x[10])
print("all best candidates at a nonnode corner:", all(x[5] < 1e-6 for x in rows), "max |best-Lc|:", max(abs(x[4]) for x in rows),
      "min gap:", min(x[7] for x in rows), "count:", len(rows))
