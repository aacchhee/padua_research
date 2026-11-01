"""L5 R03: controls for the REPRO n=60 outlier: scheme error (vs the Householder H, as diag_repro_x60.py) on the gepp order and on random
permutations default_rng(s).permutation(N), s in SEEDS; unit weights. usage: python3 -I diag_x60_controls.py OUT.jsonl [n=60] [seeds ...]"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L, prefix as PF
F = L.F
out = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 60
seeds = [int(s) for s in sys.argv[3:]] or [3, 4, 5]
P, wc, Qc = PF.padua_orthogonal_basis(n); N = len(P)
orders = {"gepp": PF.gepp_order(Qc)}
for s in seeds: orders[f"rng{s}"] = np.random.default_rng(s).permutation(N)
for name, perm in orders.items():
    t = time.time()
    x, y, v = P[perm, 0].copy(), P[perm, 1].copy(), np.ones(N)
    Hxh, Hyh = L.method_H("hh", x, y, v, N)
    Hx, Hy, st = L.givens_c(x, y, v, "scheme")
    _, hx, hy = F.fixsign(np.eye(N), N, Hx, Hy)
    hlx, hly = L.method_H("hl", x, y, v, N)
    r = dict(n=n, N=N, order=name, scheme=L.rel_err_H(hx, hy, Hxh, Hyh, N), hl=L.rel_err_H(hlx, hly, Hxh, Hyh, N), secs=round(time.time() - t))
    print(json.dumps(r), flush=True)
    open(out, "a").write(json.dumps(r) + "\n")
