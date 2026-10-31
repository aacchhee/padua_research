"""L5 adversarial reconstruction experiments (auditor's own code; uses only alib.py / agivens.c).

usage (from this directory; AG_BUILD = dir with libagivens*.so; OPENBLAS_NUM_THREADS=1):
  python3 -I exp_review.py slopes  OUT.jsonl n1 n2 ...     Padua, cubature weights; orders given, sortx, r1-r3, gepp;
                                                         methods givens-scheme/largest, hl, cgs2, hh vs long-double reference
  python3 -I exp_review.py kill    OUT.jsonl n1 n2 ...     Padua, cubature weights; all-prefix-unisolvent orders gepp, geppR1, geppR2
                                                         (GEPP on randomly row-scaled matrices), LU prefix certificate,
                                                         scheme vs largest, Q accumulated: backward residual + structure defect
  python3 -I exp_review.py repro60 OUT.jsonl              Padua n = 60, unit weights, perm = default_rng(2).permutation(N)
                                                         (REPRO X60 order); error vs Householder H; LU prefix bounds
  python3 -I exp_review.py unif    OUT.jsonl M1 M2 ...     uniform random nodes, M/N ~ 3, unit weights, 3 seeds; cond of C
"""
import sys, os, json, time, hashlib, platform
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import alib as A

HERE = os.path.dirname(os.path.abspath(__file__))
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]

def emit(out, rec):
    out.write(json.dumps(rec) + "\n"); out.flush()
    print(json.dumps({k: (f"{v:.2e}" if isinstance(v, float) else v) for k, v in rec.items()}), flush=True)

def reference(x, y, w, N):
    Q = A.ref_Q(x, y, w, N); Rx, Ry = A.H_from_Q(Q, x, y)
    return A.signfix_H(Rx.astype(float), Ry.astype(float), N)

def givens_err(x, y, w, N, rule, Rx, Ry, accQ=False):
    v = np.sqrt(w)
    X, Y, wv, Qt, st = A.givens(x, y, v, rule, accQ=accQ)
    Hx, Hy = A.signfix_H(X, Y, N, np.sign(wv[0]))
    rec = {rule: A.relerr(Hx, Hy, Rx, Ry), "rot_" + rule: st.tolist()}
    if accQ:
        M = len(x); nH = np.sqrt(np.sum(x ** 2) + np.sum(y ** 2))
        bk = np.sqrt(np.sum((Qt @ (x[:, None] * Qt.T) - X) ** 2) + np.sum((Qt @ (y[:, None] * Qt.T) - Y) ** 2)) / nH
        rec["bkw_" + rule] = float(bk)                                   # Theorem A quantity, computed with computed Qt
        rec["orth_" + rule] = float(np.max(np.abs(Qt @ Qt.T - np.eye(M))))
        rec["q0_" + rule] = float(np.linalg.norm(np.abs(Qt[0]) - v / np.linalg.norm(v)))   # first column vs sqrt(w)
        rec["wres_" + rule] = float(np.linalg.norm(wv[1:]) / np.linalg.norm(v))
        # structure defect: entries that are zero in the exact structured form, below BOTH candidate pivots of every j
        pp, pc, ap, ac = A.pivot_tables(M); dmax = 0.0
        for j in range(1, M):
            for part, col in ((pp[j], pc[j]), (ap[j], ac[j])):
                if part < 0: continue
                H = X if part == 1 else Y
                if j + 1 < M: dmax = max(dmax, float(np.max(np.abs(H[j + 1:, col]))))
        rec["sdef_" + rule] = dmax / float(np.sqrt(np.sum(X ** 2) + np.sum(Y ** 2)) / np.sqrt(M))
    return rec

def comparators(x, y, w, N, Rx, Ry):
    v = np.sqrt(w); rec = {}
    for name, f in (("hl", lambda: A.krylov(x, y, v, N)), ("cgs2", lambda: A.krylov(x, y, v, N, window=False, mgs=False)),
                    ("hh", lambda: A.householder(x, y, w, N))):
        t = time.time(); Q = f()
        Hx, Hy = A.H_from_Q(Q, x, y); Hx, Hy = A.signfix_H(Hx, Hy, N, np.sign(np.sum(Q[:, 0])))
        rec[name] = A.relerr(Hx, Hy, Rx, Ry); rec["t_" + name] = round(time.time() - t, 1)
    return rec

def orth_cheb(x, y, w, N):
    C = np.sqrt(w)[:, None] * A.cheb_matrix(x, y, N)
    return C / np.linalg.norm(C, axis=0)

def prefix_summary(B):
    r = A.prefix_lu_bounds(B)
    if r is None: return dict(lu="breakdown")
    lo, up, g, res = r
    return dict(lu="ok", min_lo=float(lo.min()), K_min_lo=int(np.argmin(lo)) + 1, min_up=float(up.min()),
                K_min_up=int(np.argmin(up)) + 1, n_up_lt_1e11=int(np.sum(up < 1e-11)), growth=g, lu_resid=res)

def main():
    mode, outp = sys.argv[1], sys.argv[2]; args = [int(a) for a in sys.argv[3:]]
    out = open(outp, "a")
    emit(out, dict(meta=True, mode=mode, argv=sys.argv, start=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   numpy=np.__version__, python=platform.python_version(), blas=os.environ.get("OPENBLAS_NUM_THREADS"),
                   sha_exp=sha(__file__), sha_lib=sha(os.path.join(HERE, "alib.py")), sha_c=sha(os.path.join(HERE, "agivens.c"))))
    if mode in ("slopes", "kill"):
        for n in args:
            x, y, w = A.padua(n); N = len(x)
            t = time.time(); Rx, Ry = reference(x, y, w, N); tref = time.time() - t
            C = orth_cheb(x, y, w, N)
            if mode == "slopes":
                perms = {"given": np.arange(N), "sortx": np.lexsort((y, x)), "gepp": A.gepp_order(C)}
                for k in (1, 2, 3): perms[f"r{k}"] = np.random.default_rng(900 + 10 * n + k).permutation(N)
            else:
                perms = {"gepp": A.gepp_order(C)}
                for k in (1, 2):
                    s = np.exp(np.random.default_rng(500 + 10 * n + k).normal(0, 1.5, N))
                    perms[f"geppR{k}"] = A.gepp_order(s[:, None] * C)
            for lab, perm in perms.items():
                xp, yp, wp = x[perm].copy(), y[perm].copy(), w[perm].copy()
                rec = dict(mode=mode, n=n, M=N, order=lab, t_ref=round(tref, 1))
                t = time.time()
                for rule in ("scheme", "largest"):
                    rec.update(givens_err(xp, yp, wp, N, rule, Rx, Ry, accQ=(mode == "kill")))
                rec["t_givens"] = round(time.time() - t, 1)
                if mode == "slopes": rec.update(comparators(xp, yp, wp, N, Rx, Ry))
                if mode == "kill" or lab == "gepp" or lab.startswith("r"):
                    rec.update(prefix_summary(C[perm]))
                emit(out, rec)
    elif mode == "repro60":
        n = 60; x, y, w0 = A.padua(n); N = len(x); w = np.ones(N)
        perms = {"repro_rng2": np.random.default_rng(2).permutation(N)}
        for lab, perm in perms.items():
            xp, yp = x[perm].copy(), y[perm].copy()
            Q = A.householder(xp, yp, w, N); Hx, Hy = A.H_from_Q(Q, xp, yp)
            Rx, Ry = A.signfix_H(Hx, Hy, N, np.sign(np.sum(Q[:, 0])))
            rec = dict(mode=mode, n=n, M=N, order=lab, reference="householder(double)")
            t = time.time()
            for rule in ("scheme", "largest"): rec.update(givens_err(xp, yp, w, N, rule, Rx, Ry))
            rec["t_givens"] = round(time.time() - t, 1)
            Qh = A.krylov(xp, yp, np.ones(N), N); Hx, Hy = A.H_from_Q(Qh, xp, yp); Hx, Hy = A.signfix_H(Hx, Hy, N, np.sign(np.sum(Qh[:, 0])))
            rec["hl"] = A.relerr(Hx, Hy, Rx, Ry)
            C = orth_cheb(x, y, w0, N)        # prefix property is weight independent; use the orthogonal cubature-weighted matrix
            rec.update(prefix_summary(C[perm]))
            emit(out, rec)
    elif mode == "unif":
        TAB = {66: 5, 136: 8, 231: 11, 496: 17, 861: 22}
        for M in args:
            n = TAB[M]; N = (n + 1) * (n + 2) // 2
            for seed in (1, 2, 3):
                P = np.random.default_rng(31000 + 100 * seed + M).uniform(-1, 1, (M, 2)); x, y = P[:, 0].copy(), P[:, 1].copy(); w = np.ones(M)
                Rx, Ry = reference(x, y, w, N)
                C = A.cheb_matrix(x, y, N); sv = np.linalg.svd(np.column_stack([C[:, k] / np.linalg.norm(C[:, k]) for k in range(N)]), compute_uv=False)
                rec = dict(mode=mode, M=M, n=n, N=N, seed=seed, cond=float(sv[0] / sv[-1]))
                for rule in ("scheme", "largest"): rec.update(givens_err(x, y, w, N, rule, Rx, Ry))
                rec.update(comparators(x, y, w, N, Rx, Ry))
                emit(out, rec)

if __name__ == "__main__":
    main()
