"""L5 R03: diagnose the REPRO.md n=60 random-order outlier (Givens-scheme 2.0e-12, 182x HL, uniform weights).
Permutation reproduced exactly as in inputs/f6_run_padua_large.py: rng = default_rng(2); perm = rng.permutation(N) (first draw; the 'given' case uses no rng).
Error proxy: relative Frobenius difference of (Hx,Hy) from the Householder H (Householder error ~3e-15 << 2e-12), because the long-double reference at n=60 is too slow here.
Prefix scan: prefix.py (certified sigma_min of every prefix block of the orthogonal Chebyshev matrix).  usage: python3 -I diag_repro_x60.py [n=60]"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L, prefix as PF
F = L.F
n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
P, wc, Qc = PF.padua_orthogonal_basis(n); N = len(P)
perm = np.random.default_rng(2).permutation(N)
x, y, v = P[perm, 0].copy(), P[perm, 1].copy(), np.ones(N)          # uniform weights, as REPRO
Hxh, Hyh = L.method_H("hh", x, y, v, N)
out = {}
for rule in ("scheme", "largest"):
    Hx, Hy, st = L.givens_c(x, y, v, rule)
    _, hx, hy = F.fixsign(np.eye(N), N, Hx, Hy)
    out[rule] = L.rel_err_H(hx, hy, Hxh, Hyh, N)
hl_x, hl_y = L.method_H("hl", x, y, v, N); out["hl"] = L.rel_err_H(hl_x, hl_y, Hxh, Hyh, N)
print(f"n={n} N={N} uniform weights, rng(2) permutation: error vs Householder H: " + " ".join(f"{k}:{v:.1e}" for k, v in out.items()), flush=True)
t = time.time(); comb = PF.combinatorial_singular(x, y)
r = PF.prefix_scan(Qc[perm], use_comb=comb)
mex, kmex, nref = PF.refine_min(Qc[perm], r)
print(f"prefix scan ({time.time()-t:.0f}s): n_sing={r['n_sing']} n_amb={r['n_amb']} min exact sigma over refined={mex:.2e} at K={kmex}; number of prefixes with hi<1e-6: {(r['hi']<1e-6).sum()}, <1e-8: {(r['hi']<1e-8).sum()}", flush=True)
json.dump(dict(n=n, N=N, err=out, n_sing=r["n_sing"], n_amb=r["n_amb"], min_exact=mex, K_at_min=kmex, n_hi_lt_1e6=int((r["hi"] < 1e-6).sum()),
               n_hi_lt_1e8=int((r["hi"] < 1e-8).sum())), open(sys.argv[2] if len(sys.argv) > 2 else "/dev/stdout", "w"))
