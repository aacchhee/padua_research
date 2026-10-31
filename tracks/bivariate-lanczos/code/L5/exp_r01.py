"""L5 R01 experiment: relative error of (H_x, H_y) for Givens (scheme, largest), HL, BJ, CGS2, Householder
against a long-double reference, over M = 66 .. 2016.

usage: python3 -I exp_r01.py FAMILY OUT.jsonl [n_or_M ...]
  FAMILY = padua_cub   Padua n, cubature weights            (sizes = n; default 10 15 20 30 40 50 62)
           padua_rand  Padua n, weights ~ U(0.1, 1)        (one weight vector per n shared by the 5 orders)
           padua_unif  Padua n, unit weights               (as in the supplier inputs / VB-C 2010)
           random      M uniform random nodes in [-1,1]^2, unit weights, 5 seeds (sizes = M; N = (n+1)(n+2)/2 from TABLE)
Padua orders: given, sortx, rand1, rand2, rand3.  Random: seed1..seed5 (each its own node set, drawn order).
Error metric: relative Frobenius error of the leading N x N blocks of (Hx, Hy) after positive-primary-pivot sign fixing.
Environment: OPENBLAS_NUM_THREADS=1. Input module imported unchanged by path (see l5_lib.py).
"""
import sys, os, json, time, hashlib, platform
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L
F = L.F

METHODS = ["givens-scheme", "givens-largest", "hl", "bj", "cgs2", "hh"]
RANDOM_N = {66: 5, 136: 8, 231: 11, 496: 17, 861: 22, 1326: 28, 2016: 34}   # polynomial degree n -> N = (n+1)(n+2)/2

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def one_case(fam, size, label, x, y, w, N, Hxr, Hyr, out, extra=None):
    v = np.sqrt(w)
    rec = dict(family=fam, size=size, M=len(x), N=N, order=label, **(extra or {}))
    for m in METHODS:
        t = time.time()
        if m.startswith("givens"):
            Hx, Hy, st = L.givens_c(x, y, v, rule=m.split("-")[1])
            _, Hx, Hy = F.fixsign(np.eye(len(x), N), N, Hx[:N, :N], Hy[:N, :N])
            rec["stats_" + m] = [float(s) for s in st]
        else:
            Hx, Hy = L.method_H(m, x, y, v, N)
        rec[m] = L.rel_err_H(Hx, Hy, Hxr, Hyr, N)
        rec["t_" + m] = round(time.time() - t, 2)
    out.write(json.dumps(rec) + "\n"); out.flush()
    print(fam, size, label, " ".join(f"{m}:{rec[m]:.1e}" for m in METHODS), flush=True)

def main():
    fam, outp = sys.argv[1], sys.argv[2]
    sizes = [int(a) for a in sys.argv[3:]]
    out = open(outp, "a")
    meta = dict(meta=True, argv=sys.argv, start=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), numpy=np.__version__,
                python=platform.python_version(), machine=platform.machine(), blas_threads=os.environ.get("OPENBLAS_NUM_THREADS"),
                sha256_exp=sha(__file__), sha256_lib=sha(L.__file__), sha256_input=sha(L._INP))
    out.write(json.dumps(meta) + "\n"); out.flush()
    if fam.startswith("padua"):
        for n in (sizes or [10, 15, 20, 30, 40, 50, 62]):
            P, wc = L.padua_cubature(n); N = len(P)
            rng = np.random.default_rng(1000 + n)
            w = {"padua_cub": wc, "padua_rand": rng.uniform(0.1, 1, N), "padua_unif": np.ones(N)}[fam]
            t = time.time()
            Hxr, Hyr = L.reference_H(P[:, 0].copy(), P[:, 1].copy(), np.sqrt(w), N)
            print(f"[ref n={n} N={N} {time.time()-t:.0f}s]", flush=True)
            perms = {"given": np.arange(N), "sortx": np.lexsort((P[:, 1], P[:, 0]))}
            for k in (1, 2, 3): perms[f"rand{k}"] = np.random.default_rng(10 * n + k).permutation(N)
            for lab, perm in perms.items():
                one_case(fam, n, lab, P[perm, 0].copy(), P[perm, 1].copy(), w[perm], N, Hxr, Hyr, out, dict(n=n))
    else:
        for M in (sizes or sorted(RANDOM_N)):
            n = RANDOM_N[M]; N = (n + 1) * (n + 2) // 2
            for seed in range(1, 6):
                rng = np.random.default_rng(7000 * seed + M)
                P = rng.uniform(-1, 1, (M, 2)); w = np.ones(M)
                x, y = P[:, 0].copy(), P[:, 1].copy()
                Hxr, Hyr = L.reference_H(x, y, np.sqrt(w), N)
                V = np.column_stack([np.cos(a * np.arccos(x)) * np.cos(b * np.arccos(y)) for a, b in F.monos(N)])
                sv = np.linalg.svd(V, compute_uv=False)
                one_case(fam, M, f"seed{seed}", x, y, w, N, Hxr, Hyr, out, dict(n=n, cond=float(sv[0] / sv[-1])))

if __name__ == "__main__":
    main()
