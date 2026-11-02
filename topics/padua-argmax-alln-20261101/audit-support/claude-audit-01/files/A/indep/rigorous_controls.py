"""Negative controls for the auditor's rigorous kernel (must reject every defect)."""
import copy
import gzip
import json
import sys
from fractions import Fraction as F

import mpmath
from mpmath import iv, mp

import rigorous_kernel as rk

mp.dps = iv.dps = 90
out = {}


def evaluate(n, leaves, nodes, threshold_scale=F(1)):
    md = rk.modes_of(n)
    Cint, delta, normR, normC = rk.rigorous_inverse(n, nodes, md)
    Pl, G = rk.power_ints(n, md, Cint)
    nodeset = set(nodes)
    ci = {(1, 1): (0, 0), (1, -1): (0, n + 1), (-1, 1): (n, 0), (-1, -1): (n, n + 1)}
    nonnode = sorted(c for c, jk in ci.items() if jk not in nodeset)
    Cminus = min(rk.corner_lower(n, md, Cint, delta, c)[0] for c in nonnode) * threshold_scale
    paths = [r["path"] for r in leaves]
    prefix_free = all(not (p != q and q.startswith(p)) for p in paths for q in paths)
    kraft = sum(F(1, 2 ** len(p)) for p in paths)
    fails = 0
    cover = set()
    for row in leaves:
        box = rk.box_of_path(row["path"])
        U = rk.leaf_upper_bounds(n, Pl, G, delta, box)
        if max(max(r) for r in U) < Cminus:
            continue
        ok = False
        for c in nonnode:
            if (box[0][0] == c[0] or box[0][1] == c[0]) and (box[1][0] == c[1] or box[1][1] == c[1]):
                vi = 0 if box[0][0] == c[0] else n
                vk = 0 if box[1][0] == c[1] else n
                if max(U[i][k] for i in range(n + 1) for k in range(n + 1) if (i, k) != (vi, vk)) < Cminus:
                    ok = True
                    cover.add(c)
        fails += not ok
    accepted = prefix_free and kraft == 1 and fails == 0 and cover == set(nonnode)
    return {"accepted": accepted, "failed_leaves": fails, "kraft": str(kraft), "prefix_free": prefix_free,
            "corner_cover": sorted(map(list, cover)), "nonnode": nonnode}


def load(name):
    return json.loads(gzip.decompress(open(rk.REPO_OUT + name, "rb").read()))


d9 = load("finite_n9_general.json.gz")
n = 9
nodes = rk.nodes_of(n)
out["authentic_n9"] = evaluate(n, d9["leaves"], nodes)
L = copy.deepcopy(d9["leaves"])
L.pop(5)
out["missing_leaf_n9"] = evaluate(n, L, nodes)
L = copy.deepcopy(d9["leaves"])
L.append(copy.deepcopy(L[3]))
out["duplicate_leaf_n9"] = evaluate(n, L, nodes)
# merge two sibling bound leaves into their parent (coarser box must fail or still be valid)
paths = {r["path"] for r in d9["leaves"]}
sib = next(p for p in sorted(paths) if p.endswith("0") and p[:-1] + "1" in paths and len(p) > 2)
L = [r for r in d9["leaves"] if r["path"] not in (sib, sib[:-1] + "1")] + [{"path": sib[:-1], "kind": "bound"}]
out["coarsened_parent_" + sib[:-1] + "_n9"] = evaluate(n, L, nodes)
# odd checkerboard (wrong Padua family): corners/values change
odd = [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 1]
out["odd_checkerboard_nodes_n9"] = evaluate(n, d9["leaves"], odd)
# threshold lowered by 0.5% on n16 (recorded worst margin 0.23%)
d16 = load("finite_n16_general.json.gz")
out["threshold_minus_half_percent_n16"] = evaluate(16, d16["leaves"], rk.nodes_of(16), F(995, 1000))
out["authentic_n16"] = evaluate(16, d16["leaves"], rk.nodes_of(16))
json.dump(out, open(sys.argv[1], "w"), indent=1, default=str)
print(json.dumps(out, default=str, indent=1))
