"""L5 R03: candidate pivot / deflation rules for point-by-point Givens updating on Padua sets (M = N), compared on the same streams.

Rules (all on the same data, error = relative Frobenius error of (Hx,Hy) vs the long-double reference of exp_r01.py):
  scheme        fixed order-determined primary pivot (VB-C 'downside-up')                      [baseline]
  largest       alt pivot if |alt pivot| > |primary pivot|                                    [seed p. 395 / Humet-style]
  pivk10, pivk100   alt pivot only if |alt pivot| > kappa |primary pivot|  (kappa = 10, 100)
  pairnorm1, pairnorm100   alt pair (pivot, entry below) only if its norm exceeds kappa x the primary pair norm
  defer         scheme + prefix-aware deferral: a node whose insertion makes min_j |pivot_j| < tau (tau = 1e-8) is held in a buffer and
                retried (oldest first) after every acceptance; at stream end the buffer is drained by taking the node with the largest min-pivot.
usage: [L5_TAUS=1e-8,1e-3] python3 -I exp_r03.py OUT.jsonl n [n ...]
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L, prefix as PF
F = L.F
TAU = 1e-8
TAUS = [float(t) for t in os.environ.get("L5_TAUS", "1e-8").split(",")]   # deferral thresholds

def to_err(Hx, Hy, N, Hxr, Hyr):
    _, hx, hy = F.fixsign(np.eye(Hx.shape[0], N), N, Hx[:N, :N], Hy[:N, :N])
    return L.rel_err_H(hx, hy, Hxr, Hyr, N)

def defer_run(x, y, v, tau=TAU):
    M = len(x); Hx = np.zeros((M, M)); Hy = np.zeros((M, M)); w = np.zeros(M)
    Hx[0, 0] = x[0]; Hy[0, 0] = y[0]; w[0] = v[0]; K = 1
    pending = []; deferred_events = 0; forced = 0
    def try_pending():
        nonlocal Hx, Hy, w, K, deferred_events
        progress = True
        while progress and pending:
            progress = False
            for t in list(pending):
                hx, hy, ww = Hx.copy(), Hy.copy(), w.copy()
                mp = L.givens_insert(hx, hy, ww, K, x[t], y[t], v[t], M)
                if mp >= tau:
                    Hx, Hy, w = hx, hy, ww; K += 1; pending.remove(t); progress = True; break
                deferred_events += 1
    for t in range(1, M):
        pending.append(t); try_pending()
    while pending:                       # drain: best min-pivot
        best = None
        for t in pending:
            hx, hy, ww = Hx.copy(), Hy.copy(), w.copy()
            mp = L.givens_insert(hx, hy, ww, K, x[t], y[t], v[t], M)
            if best is None or mp > best[0]: best = (mp, t, hx, hy, ww)
        mp, t, Hx, Hy, w = best; K += 1; pending.remove(t)
        if mp < tau: forced += 1
        try_pending()
    return Hx, Hy, dict(deferred_events=deferred_events, forced=forced)

RULES = {"scheme": ("c", 0, 1.0), "largest": ("c", 1, 1.0), "pivk10": ("c2", 4, 10.0), "pivk100": ("c2", 4, 100.0),
         "pairnorm1": ("c2", 3, 1.0), "pairnorm100": ("c2", 3, 100.0)}

def main():
    out = open(sys.argv[1], "a"); sizes = [int(a) for a in sys.argv[2:]]
    out.write(json.dumps(dict(meta=True, argv=sys.argv, start=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), tau=TAU)) + "\n")
    for n in sizes:
        P, wc, Qc = PF.padua_orthogonal_basis(n); N = len(P)
        orders = {"given": np.arange(N), "sortx": np.lexsort((P[:, 1], P[:, 0]))}
        for k in (1, 2, 3): orders[f"rand{k}"] = np.random.default_rng(10 * n + k).permutation(N)
        orders["gepp"] = PF.gepp_order(Qc)
        for wname in ("cub", "rand"):
            w0 = wc if wname == "cub" else np.random.default_rng(1000 + n).uniform(0.1, 1, N)
            Hxr, Hyr = L.reference_H(P[:, 0].copy(), P[:, 1].copy(), np.sqrt(w0), N)
            for lab, perm in orders.items():
                x, y, v = P[perm, 0].copy(), P[perm, 1].copy(), np.sqrt(w0[perm])
                rec = dict(n=n, N=N, weights=wname, order=lab)
                for rname, (kind, rule, kap) in RULES.items():
                    if kind == "c": Hx, Hy, st = L.givens_c(x, y, v, rule=["scheme", "largest"][rule])
                    else: Hx, Hy, st = L.givens_c2(x, y, v, rule, kap)
                    rec[rname] = to_err(Hx, Hy, N, Hxr, Hyr)
                    rec["nalt_" + rname] = float(st[2]); rec["nnoise_" + rname] = float(st[3]) if kind == "c2" else None
                for tau in TAUS:
                    t = time.time(); Hx, Hy, info = defer_run(x, y, v, tau)
                    key = "defer" if tau == 1e-8 else f"defer_tau{tau:g}"
                    rec[key] = to_err(Hx, Hy, N, Hxr, Hyr); rec[key + "_info"] = info; rec[key + "_secs"] = round(time.time() - t, 1)
                out.write(json.dumps(rec) + "\n"); out.flush()
                print(f"n={n} {wname} {lab:6s} " + " ".join(f"{k}:{rec[k]:.1e}" for k in list(RULES) + [k for k in rec if k.startswith("defer") and not k.endswith(("_info", "_secs"))]) + f"  info={info}", flush=True)

if __name__ == "__main__":
    main()
