"""L5 R03 part B: windowed best-pivot deferral (deferbestW).  usage: [L5_ORDERS=rand1,rand2] [L5_WEIGHTS=cub] python3 -I exp_r03b.py OUT.jsonl W n [n ...]
At each step the first W pending nodes of the stream are tentatively inserted (on copies) and the one with the largest
min_j |pivot_j| (online detector of R03) is committed; the window is refilled from the stream."""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L, prefix as PF
from exp_r03 import to_err
F = L.F

def deferbest(x, y, v, W):
    M = len(x); Hx = np.zeros((M, M)); Hy = np.zeros((M, M)); w = np.zeros(M)
    Hx[0, 0] = x[0]; Hy[0, 0] = y[0]; w[0] = v[0]; K = 1
    nxt = 1; window = []; minpiv_log = []
    while K < M:
        while len(window) < W and nxt < M: window.append(nxt); nxt += 1
        best = None
        for t in window:
            hx, hy, ww = Hx.copy(), Hy.copy(), w.copy()
            mp = L.givens_insert(hx, hy, ww, K, x[t], y[t], v[t], M)
            if best is None or mp > best[0]: best = (mp, t, hx, hy, ww)
        mp, t, Hx, Hy, w = best; window.remove(t); K += 1; minpiv_log.append(mp)
    return Hx, Hy, dict(min_of_min_pivots=float(min(minpiv_log)))

def main():
    out = open(sys.argv[1], "a"); W = int(sys.argv[2]); sizes = [int(a) for a in sys.argv[3:]]
    for n in sizes:
        P, wc, Qc = PF.padua_orthogonal_basis(n); N = len(P)
        orders = {"given": np.arange(N), "sortx": np.lexsort((P[:, 1], P[:, 0])), "rand1": np.random.default_rng(10 * n + 1).permutation(N), "gepp": PF.gepp_order(Qc)}
        sel = os.environ.get("L5_ORDERS")
        if sel: orders = {k: v for k, v in orders.items() if k in sel.split(",")}
        for wname in os.environ.get("L5_WEIGHTS", "cub,rand").split(","):
            w0 = wc if wname == "cub" else np.random.default_rng(1000 + n).uniform(0.1, 1, N)
            Hxr, Hyr = L.reference_H(P[:, 0].copy(), P[:, 1].copy(), np.sqrt(w0), N)
            for lab, perm in orders.items():
                x, y, v = P[perm, 0].copy(), P[perm, 1].copy(), np.sqrt(w0[perm])
                Hx, Hy, st = L.givens_c(x, y, v, "scheme"); es = to_err(Hx, Hy, N, Hxr, Hyr)
                t = time.time(); Hx, Hy, info = deferbest(x, y, v, W); ed = to_err(Hx, Hy, N, Hxr, Hyr)
                rec = dict(n=n, weights=wname, order=lab, W=W, scheme=es, deferbest=ed, info=info, secs=round(time.time() - t, 1))
                out.write(json.dumps(rec) + "\n"); out.flush()
                print(f"n={n} {wname} {lab:6s} W={W} scheme:{es:.1e} deferbest:{ed:.1e} min-of-min-pivots={info['min_of_min_pivots']:.1e} ({rec['secs']}s)", flush=True)

if __name__ == "__main__":
    main()
