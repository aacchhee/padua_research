"""Claude audit-01, A2: compare the two independent audit outputs.

Direct Vandermonde enclosures (audit_a2_direct) versus -04 positive-form
enclosures (audit_a2_formula) of Lambda_c(n), on their common n; plus the
degree below which -01's lower bound is weaker than the trivial Lambda_c>=1.
Usage: python3 audit_a2_compare.py direct.json formula.json > out.json
"""
import json
import sys

from flint import arb, ctx

ctx.prec = 128
d = json.load(open(sys.argv[1]))
f = json.load(open(sys.argv[2]))
fd = {r["n"]: r for r in f["results"]}
rows, ok = [], True
for r in d["results"]:
    n = r["n"]
    if n not in fd:
        continue
    a, b = arb(r["Lambda_c"]), arb(fd[n]["Lambda_c"])
    agree = a.overlaps(b)
    ok &= agree
    rows.append({"n": n, "overlap": agree, "abs_mid_diff": float(abs(a.mid() - b.mid()))})
# smallest n with (4/pi^2) log^2 n - 54 > 1
PI = arb.pi()
lo = 2
while not (4 / PI ** 2 * arb(lo).log() ** 2 - 54 > 1):
    lo = lo * 2
hi, lo = lo, lo // 2
while hi - lo > 1:
    mid = (lo + hi) // 2
    if 4 / PI ** 2 * arb(mid).log() ** 2 - 54 > 1:
        hi = mid
    else:
        lo = mid
print(json.dumps({
    "common_n": [x["n"] for x in rows],
    "all_overlap": ok,
    "max_abs_mid_diff": max(x["abs_mid_diff"] for x in rows),
    "rows": rows,
    "first_n_where_01_lower_bound_exceeds_1": hi,
}, indent=1))
