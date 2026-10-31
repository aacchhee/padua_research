"""L5 R02 diagnostic: growth of the Givens ('scheme') rounding error with the number of points processed, measured by running
double and long double in lockstep (givens_dual.c) -- no external reference needed (the prefix property of point-by-point updating:
the state after i points is the state of the algorithm run on the first i points).

usage: python3 -I exp_r02_dual.py OUT.jsonl FAMILY n [n ...]      FAMILY in {padua_cub, padua_unif, random}
Checkpoints: 8 values log-spaced from 40 to M.  Output: relative Frobenius difference of the active blocks (double vs long double).
"""
import sys, os, json, time, ctypes
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L
HERE = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(os.path.join(HERE, "libgivens_dual.so"))
dp = np.ctypeslib.ndpointer(np.float64, flags="C_CONTIGUOUS"); ip = np.ctypeslib.ndpointer(np.int32, flags="C_CONTIGUOUS")
lp = np.ctypeslib.ndpointer(np.int64, flags="C_CONTIGUOUS")
lib.givens_dual.argtypes = [dp, dp, dp, ctypes.c_long, ip, ip, lp, ctypes.c_int, dp]

def dual(x, y, v, ck):
    M = len(x); pi, pv, ai, av = L.tables(M); out = np.zeros(3 * len(ck))
    lib.givens_dual(np.ascontiguousarray(x), np.ascontiguousarray(y), np.ascontiguousarray(v), M, pi, pv, np.array(ck, np.int64), len(ck), out)
    return out.reshape(-1, 3)

def main():
    outp, fam = sys.argv[1], sys.argv[2]; sizes = [int(a) for a in sys.argv[3:]]
    out = open(outp, "a")
    for s in sizes:
        if fam.startswith("padua"):
            P, wc = L.padua_cubature(s); M = len(P); w = wc if fam == "padua_cub" else np.ones(M)
            perms = {"given": np.arange(M), "rand1": np.random.default_rng(10 * s + 1).permutation(M)}
        else:
            M = s; perms = {}
            for k in (1, 2):
                rng = np.random.default_rng(7000 * k + M); P = rng.uniform(-1, 1, (M, 2)); perms[f"seed{k}"] = None
            w = np.ones(M)
        for lab, perm in perms.items():
            if fam == "random":
                k = int(lab[-1]); P = np.random.default_rng(7000 * k + M).uniform(-1, 1, (M, 2)); perm = np.arange(M)
            ck = sorted(set(int(round(c)) for c in np.geomspace(40, M, 8)))
            t = time.time()
            r = dual(P[perm, 0], P[perm, 1], np.sqrt(w[perm]), ck)
            rec = dict(family=fam, size=s, M=M, order=lab, ckpt=ck, relfro=r[:, 0].tolist(), maxabs=r[:, 1].tolist(), nrot=r[:, 2].tolist(), secs=round(time.time() - t, 1))
            sl = np.polyfit(np.log(ck), np.log(r[:, 0]), 1)[0]
            rec["slope_in_i"] = float(sl)
            out.write(json.dumps(rec) + "\n"); out.flush()
            print(fam, s, lab, "relfro", " ".join(f"{a:.1e}" for a in r[:, 0]), "slope", round(sl, 2), f"{rec['secs']}s", flush=True)

if __name__ == "__main__":
    main()
