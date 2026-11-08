# MEASURED, data-only: tree statistics of the 276 old native certificates (replay276 originals) and
# a comparison of the manuscript's constant leaf test (Q-hat) with the polygon-maximum test of check.py,
# both evaluated with the STORED native uppers (not independent arithmetic; diagnostic only).
import json, glob, sys
from fractions import Fraction as F
sys.path.insert(0, "/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/independent_phase_checker")
import check as C   # trusted repo source; only pure helpers used: parse, fold, vertices, maximum, floor, PHI
S = "/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/replay276/out"
nodes, methods, corners, fcount, rows = {}, {}, {}, {}, []
qfail_near = qfail_far = 0; tested = 0; worst = None
for p in sorted(glob.glob(S + "/verify-*/original-certificate.json")):
    d = json.load(open(p)); n = d["n"]
    leaves = C.parse(d["tree"], n)
    nodes[n] = len(d["tree"]["preorder"]); methods[n] = d["norm"]["method"]; corners[n] = d["corner"]["kind"]
    fcount[n] = sum(t == "f" for t, r in leaves)
    W = {(F(a), F(b)): F(float.fromhex(h)) for a, b, h in d["S_upper_rows"]}
    L = F(float.fromhex(d["origin_lower_hex"])); M = F(d["norm"]["M"]); k = F(n, n + 1)
    for tok, r in leaves:
        if r[0] + r[2] > 1 or tok == "f": continue
        ws = [W[C.fold(*v)] for v in C.vertices(r)]
        V = max(ws); Qhat = V + M * C.PHI**2 / 8 * ((r[1]-r[0])**2 + k*k*(r[3]-r[2])**2)
        delta = C.floor(n, min(F(1, 2), C.PHI * (r[1] + r[3])))
        for side in ("near", "far"):
            qp = C.maximum(r, ws, M, k, side)
            if qp is None: continue
            tested += 1
            ok_poly = (L + (delta if side == "near" else 0) - qp) > 0
            ok_hat = (L + (delta if side == "near" else 0) - Qhat) > 0
            if ok_poly and not ok_hat:
                if side == "near": qfail_near += 1
                else: qfail_far += 1
                m = float(L + (delta if side == "near" else 0) - Qhat)
                if worst is None or m < worst[0]: worst = (m, n, side, [str(x) for x in r])
ns = sorted(nodes)
print("certificates:", len(ns), "degrees", ns[0], "..", ns[-1], "missing in 41..319:", sorted(set(range(41, 320)) - set(ns)))
print("node range:", min(nodes.values()), max(nodes.values()))
print("norm methods:", {m: sum(1 for x in methods.values() if x == m) for m in set(methods.values())})
print("corner kinds:", {c: sum(1 for x in corners.values() if x == c) for c in set(corners.values())},
      "first ANALYTIC corner n:", min([n for n in ns if corners[n] != "ACTUAL_THREE"], default=None),
      "last ACTUAL_THREE n:", max([n for n in ns if corners[n] == "ACTUAL_THREE"]))
print("analytic far leaves: degrees with f>0:", sum(1 for v in fcount.values() if v), "min n with f:", min([n for n in ns if fcount[n]], default=None))
print("proxy tests:", tested, "pass polygon but FAIL constant Q-hat: near", qfail_near, "far", qfail_far, "worst", worst)
