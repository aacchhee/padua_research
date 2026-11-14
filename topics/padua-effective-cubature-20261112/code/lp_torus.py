#!/usr/bin/env python3
"""Torus Delsarte LP for positive exact designs on T^3 (spectrum |k|_1 <= 2n-2).

R_n = sup f(0)/c_0, f real trig poly, spectrum {|k|_1<=2n-2}, f>=0 on T^3.
B3-invariant parametrisation f = 1 + sum_{O != 0} c_O sum_{k in O} cos(k.t), |c_O| <= 1
(|c_k| <= c_0 holds for every positive-definite f, so the box is without loss).
Cutting-plane LP (HiGHS). Final optimum = UPPER bound on R_n (relaxation).
Validated LOWER bound: second-order branch-and-bound lower bound on min f (and,
for comparison, the first-order Lipschitz grid bound of the pre-registration), then
(f(0)+eps)/(1+eps) with eps = max(0, -min f lower bound).  MEASURED, floating point.
Modes:  --n N [--tol ...]   run LP for degree N
        --q1a               integer check f=|D_n|^2/m_n, n=2..8
"""
import argparse, hashlib, json, sys, time, os, platform
import numpy as np, scipy
import scipy.fft
import highspy

PI = np.pi


def m_n(n):
    return (2 * n - 1) * (2 * n * n - 2 * n + 3) // 3


def build_spectrum(n, extra=0):
    R = 2 * n - 2 + extra
    r = np.arange(-R, R + 1)
    K1, K2, K3 = np.meshgrid(r, r, r, indexing="ij")
    mask = (abs(K1) + abs(K2) + abs(K3)) <= R
    ks = np.stack([K1[mask], K2[mask], K3[mask]], 1)
    key = -np.sort(-np.abs(ks), axis=1)  # sorted descending
    # orbit ids ordered by (|k|_1, key) for determinism
    uniq, inv = np.unique(key, axis=0, return_inverse=True)
    inv = inv.ravel()
    order_o = np.lexsort((uniq[:, 2], uniq[:, 1], uniq[:, 0], uniq.sum(1)))
    rank = np.empty(len(uniq), int)
    rank[order_o] = np.arange(len(uniq))
    oid = rank[inv]
    reps = uniq[order_o]
    sizes = np.bincount(oid)
    assert tuple(reps[0]) == (0, 0, 0)
    srt = np.argsort(oid, kind="stable")
    ks, oid = ks[srt], oid[srt]
    starts = np.concatenate([[0], np.cumsum(sizes)[:-1]])
    return dict(R=R, ks=ks.astype(float), kint=ks, oid=oid, reps=reps, sizes=sizes, starts=starts)


def orbit_basis(sp, T, chunk=2000):
    """B[j,O] = sum_{k in O} cos(k.t_j)."""
    out = np.empty((len(T), len(sp["sizes"])))
    for a in range(0, len(T), chunk):
        C = np.cos(T[a:a + chunk] @ sp["ks"].T)
        out[a:a + chunk] = np.add.reduceat(C, sp["starts"], axis=1)
    return out


def fold(T):
    T = np.mod(T, 2 * PI)
    T = np.where(T > PI, 2 * PI - T, T)
    return -np.sort(-T, axis=1)


class FEval:
    """Evaluate f, grad, hessian from full coefficient vector (half-space)."""

    def __init__(self, sp, corb):
        ck = corb[sp["oid"]]
        ks = sp["ks"]
        # half-space: first nonzero coordinate > 0
        first = np.where(ks[:, 0] != 0, ks[:, 0], np.where(ks[:, 1] != 0, ks[:, 1], ks[:, 2]))
        h = first > 0
        self.k = ks[h]
        self.c = 2.0 * ck[h]
        self.c0 = corb[0]
        self.kk = np.stack([self.k[:, i] * self.k[:, j] for i, j in
                            [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]], 1)
        self.L1 = float(np.sum(np.abs(self.c) * np.linalg.norm(self.k, axis=1)))  # = sum_k |c_k||k|_2 (full)
        self.L2 = float(np.sum(np.abs(self.c) * np.sum(self.k ** 2, axis=1)))
        self.sumabs = float(np.sum(np.abs(self.c)) + abs(self.c0))

    def f(self, T, chunk=2000):
        out = np.empty(len(T))
        for a in range(0, len(T), chunk):
            out[a:a + chunk] = self.c0 + np.cos(T[a:a + chunk] @ self.k.T) @ self.c
        return out

    def fg(self, T, chunk=2000, hess=False):
        n = len(T)
        f = np.empty(n); g = np.empty((n, 3)); H = np.empty((n, 3, 3)) if hess else None
        for a in range(0, n, chunk):
            ph = T[a:a + chunk] @ self.k.T
            C = np.cos(ph); S = np.sin(ph)
            f[a:a + chunk] = self.c0 + C @ self.c
            g[a:a + chunk] = -(S * self.c) @ self.k
            if hess:
                h6 = -(C * self.c) @ self.kk
                Hh = np.empty((len(h6), 3, 3))
                idx = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
                for q, (i, j) in enumerate(idx):
                    Hh[:, i, j] = h6[:, q]; Hh[:, j, i] = h6[:, q]
                H[a:a + chunk] = Hh
        return (f, g, H) if hess else (f, g)


def fft_grid(sp, corb, N):
    A = np.zeros((N, N, N), complex)
    ki = sp["kint"] % N
    A[ki[:, 0], ki[:, 1], ki[:, 2]] = corb[sp["oid"]]
    return np.real(scipy.fft.ifftn(A, workers=4)) * N ** 3


def local_minima(F, thr, cap):
    N = F.shape[0]
    ok = F < thr
    for ax in range(3):
        ok &= F <= np.roll(F, 1, ax)
        ok &= F <= np.roll(F, -1, ax)
    idx = np.argwhere(ok)
    vals = F[ok]
    o = np.argsort(vals)[:cap]
    return idx[o] * (2 * PI / N), vals[o]


def refine(fe, T, iters=15):
    T = T.copy()
    f, g, H = fe.fg(T, hess=True)
    for _ in range(iters):
        # Newton with eigenvalue safeguard
        w, V = np.linalg.eigh(H)
        w = np.maximum(np.abs(w), 1e-3 * np.max(np.abs(w), axis=1, keepdims=True) + 1e-12)
        step = -np.einsum("nij,nj->ni", V, np.einsum("nji,nj->ni", V, g) / w)
        alpha = np.ones(len(T))
        Tn = T + step
        fn = fe.f(Tn)
        for _ in range(8):
            bad = fn > f
            if not bad.any():
                break
            alpha[bad] *= 0.5
            Tn[bad] = T[bad] + alpha[bad, None] * step[bad]
            fn[bad] = fe.f(Tn[bad])
        acc = fn <= f
        T[acc] = Tn[acc]
        f, g, H = fe.fg(T, hess=True)
    return T, f


def bnb_lower(fe, delta, max_boxes=3_000_000, chunk=3000, rmin=1e-9):
    """Rigorous (up to rounding) lower bound of f on the fundamental simplex via
    f(t) >= f(c) - |grad f(c)| rho - L2 rho^2 / 2,  rho = box half-diagonal."""
    r = PI / 2
    levels = []
    ax = np.arange(2) * PI / 2 + PI / 4
    C = np.stack(np.meshgrid(ax, ax, ax, indexing="ij"), -1).reshape(-1, 3)
    r = PI / 4  # half-width of the root boxes (side pi/2)
    lo, hi = C - r, C + r
    keep = (hi[:, 0] >= np.maximum(lo[:, 1], lo[:, 2])) & (hi[:, 1] >= lo[:, 2])
    C = C[keep]
    glb = np.inf
    nbox = 0
    maxlvl = 0
    off = np.array([[a, b, c] for a in (-1, 1) for b in (-1, 1) for c in (-1, 1)], float)
    while len(C):
        rho = r * np.sqrt(3.0)
        newC = []
        surv = 0
        smin = np.inf
        for a in range(0, len(C), chunk):
            Cc = C[a:a + chunk]
            f, g = fe.fg(Cc)
            lb = f - np.linalg.norm(g, axis=1) * rho - 0.5 * fe.L2 * rho ** 2
            nbox += len(Cc)
            s = lb < -delta
            if (~s).any():
                glb = min(glb, lb[~s].min())  # terminal (discarded) boxes only
            if s.any():
                newC.append(Cc[s]); smin = min(smin, lb[s].min())
        if not newC:
            break
        C = np.concatenate(newC)
        surv = len(C)
        maxlvl += 1
        if r < rmin or nbox + 8 * surv > max_boxes:
            glb = min(glb, smin)
            return dict(glb=float(glb), boxes=nbox, levels=maxlvl, unresolved=int(surv), r_last=float(r), complete=False)
        r2 = r / 2
        ch = (C[:, None, :] + off[None] * r2).reshape(-1, 3)
        lo, hi = ch - r2, ch + r2
        keep = (hi[:, 0] >= np.maximum(lo[:, 1], lo[:, 2])) & (hi[:, 1] >= lo[:, 2])
        C = ch[keep]
        r = r2
    return dict(glb=float(glb), boxes=nbox, levels=maxlvl, unresolved=0, r_last=float(r), complete=True)


def run_lp(n, args):
    t0 = time.time()
    sp = build_spectrum(n, args.extra)
    O = len(sp["sizes"])
    V = O - 1
    sizes = sp["sizes"].astype(float)
    h = highspy.Highs()
    h.setOptionValue("output_flag", False)
    h.setOptionValue("primal_feasibility_tolerance", 1e-10)
    h.setOptionValue("dual_feasibility_tolerance", 1e-10)
    h.setOptionValue("threads", 1)
    inf = highspy.kHighsInf
    ub = np.where(sp["reps"][1:].sum(1) > 2 * n - 2, 0.0, 1.0)  # Delsarte: c_k<=0 beyond 2n-2
    h.addVars(V, -np.ones(V), ub)
    h.changeColsCost(V, np.arange(V, dtype=np.int32), sizes[1:])
    h.changeObjectiveSense(highspy.ObjSense.kMaximize)
    G = args.grid_factor * n + 2
    pts = [(i, j, k) for i in range(G + 1) for j in range(i + 1) for k in range(j + 1)]
    T = np.array(pts, float) * PI / G
    T = T[np.any(T > 0, axis=1)]
    allpts = {tuple(np.round(t, 9)) for t in T}
    N = args.fft_factor * n
    hist = []
    nrows = 0
    it = 0
    ordered = []
    while True:
        it += 1
        ordered.append(T)
        B = orbit_basis(sp, T)[:, 1:]
        m = len(T)
        starts = (np.arange(m) * V).astype(np.int32)
        idx = np.tile(np.arange(V, dtype=np.int32), m)
        h.addRows(m, -np.ones(m), np.full(m, inf), m * V, starts, idx, B.ravel())
        nrows += m
        h.run()
        sol = h.getSolution()
        c = np.array(sol.col_value)
        f0 = 1.0 + float(sizes[1:] @ c)
        corb = np.concatenate([[1.0], c])
        # locate minima
        fe = FEval(sp, corb)
        F = fft_grid(sp, corb, N)
        gmin = float(F.min())
        cand, cv = local_minima(F, args.cand_thr, args.cand_cap)
        Tr, fr = refine(fe, cand)
        Tf = fold(Tr)
        cmin = float(fr.min()) if len(fr) else 0.0
        mn = min(cmin, gmin)
        tol = args.tol * f0
        hist.append(dict(it=it, rows=nrows, f0=f0, min_found=mn, t=round(time.time() - t0, 2)))
        if args.verbose:
            print(f"n={n} it={it} rows={nrows} f(0)={f0:.9f} min={mn:.3e} ({time.time()-t0:.1f}s)", flush=True)
        if mn >= -tol or it >= args.max_iter:
            break
        viol = fr < -0.1 * tol  # add refined violated and near-violated minima
        sel = np.concatenate([Tf[viol], fold(cand[cv < 0])]) if True else Tf[viol]
        # also add all refined minima below small threshold to speed convergence
        sel = np.concatenate([sel, Tf[fr < 1e-3]])
        new = []
        for t in sel:
            kk = tuple(np.round(t, 9))
            if kk not in allpts and np.any(t > 0):
                allpts.add(kk); new.append(t)
        if not new:
            break
        T = np.array(new)
    lp_time = time.time() - t0
    # dual
    return dict(Tord=np.concatenate(ordered), sp=sp, corb=corb, f0=f0, hist=hist, lp_time=lp_time, h=h, nrows=nrows, N=N, it=it,
                converged=bool(mn >= -tol), min_found=mn, fe=fe)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int)
    ap.add_argument("--extra", type=int, default=0, help="K=2n-2+extra; extra>0 gives the Delsarte variant (c_k<=0 beyond 2n-2)")
    ap.add_argument("--q1a", action="store_true")
    ap.add_argument("--tol", type=float, default=1e-10)
    ap.add_argument("--grid-factor", type=int, default=2)
    ap.add_argument("--fft-factor", type=int, default=12)
    ap.add_argument("--cand-thr", type=float, default=3.0)
    ap.add_argument("--cand-cap", type=int, default=800)
    ap.add_argument("--max-iter", type=int, default=200)
    ap.add_argument("--delta", type=float, default=1e-4)
    ap.add_argument("--delta-max", type=float, default=1e-2)
    ap.add_argument("--max-boxes", type=int, default=100_000)
    ap.add_argument("--lip-N", type=int, default=128)
    ap.add_argument("--out", type=str)
    ap.add_argument("--workdir", default="/tmp/claude-0/-workspace-padua-research/e2057052-bb3b-5345-abf7-4ff7dc19c8ac/scratchpad/lp")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    os.makedirs(args.workdir, exist_ok=True)
    receipt = dict(script_sha256=hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
                   python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                   highspy=getattr(highspy, "__version__", "1.16.0"), argv=sys.argv, args=vars(args))
    if args.q1a:
        receipt["q1a"] = q1a()
        json.dump(receipt, open(args.out, "w"), indent=1)
        print(json.dumps(receipt["q1a"]))
        return
    n = args.n
    t0 = time.time()
    res = run_lp(n, args)
    sp, corb, fe = res["sp"], res["corb"], res["fe"]
    sizes = sp["sizes"]
    f0 = res["f0"]
    # dual consistency: rebuild (points are not stored in order) -> use HiGHS dual objective
    y = np.abs(np.array(res["h"].getSolution().row_dual))
    dual_mass = 1.0 + float(y.sum())
    Bd = orbit_basis(sp, res["Tord"])
    stat = sizes.astype(float)[1:] + y @ Bd[:, 1:]   # should be ~0 (up to active box bounds)
    stat_res = float(np.max(np.abs(stat)))
    n_supp = int(np.sum(y > 1e-9))
    nb_active = int(np.sum(np.abs(np.abs(corb[1:]) - 1) < 1e-9))
    # validated lower bounds
    tb = time.time()
    # Bernstein: every line restriction of f is a 1D trig poly of frequency <= K, so |grad f|<=K*||f||_inf,
    # |Hessian|_op <= K^2 ||f||_inf;  ||f||_inf <= max_grid|f| / (1 - K h sqrt3/2).
    Kdeg = 2 * n - 2 + args.extra
    fe.L2_crude, fe.L1_crude = fe.L2, fe.L1
    Minf = None  # Bernstein variant (L<=K*||f||inf) was tried at n=3 and was not tighter than the crude sums; not used
    # (b1) pre-registered Lipschitz grid bound: min over full-torus FFT grid, L = sum_k |c_k||k|_2
    Nl = args.lip_N
    F = fft_grid(sp, corb, Nl)
    h_ = 2 * PI / Nl
    gm = float(F.min())
    lip_bound = gm - fe.L1 * h_ * np.sqrt(3) / 2
    eps_lip = max(0.0, -lip_bound)
    lower_lip = (f0 + eps_lip) / (1 + eps_lip)
    # (b2) second-order branch and bound
    ladder = []
    d = args.delta
    while True:
        bb = bnb_lower(fe, d, max_boxes=args.max_boxes)
        bb["delta"] = d
        ladder.append((d, bb["complete"], bb["boxes"]))
        if bb["complete"] or d >= args.delta_max:
            break
        d *= 10
    bb["ladder"] = ladder
    eps_bb = max(0.0, -bb["glb"])
    lower_bb = (f0 + eps_bb) / (1 + eps_bb)
    mn = m_n(n)
    out = dict(n=n, extra=args.extra, K=2 * n - 2 + args.extra, m_n=mn, R_upper_gridLP=f0, rho_upper=f0 / mn,
               R_lower_validated_bnb=lower_bb, rho_lower_bnb=lower_bb / mn, eps_bnb=eps_bb, bnb=bb,
               R_lower_lipschitz_grid=lower_lip, eps_lip=eps_lip, bernstein=dict(Minf_bound=Minf, L1_crude=fe.L1_crude, L2_crude=fe.L2_crude, L1_used=fe.L1, L2_used=fe.L2), lip=dict(N=Nl, h=h_, grid_min=gm, L=fe.L1, L2=fe.L2),
               lp=dict(rows=res["nrows"], iterations=res["it"], converged=res["converged"],
                       min_found_over_f0=res["min_found"] / f0, tol=args.tol,
                       dual_mass_total=dual_mass, dual_stationarity_maxabs=stat_res, dual_support_points=n_supp, primal=f0, box_bound_active=nb_active, dual_stationarity_note='meaningful only for extra=0 (sign-constrained orbits add reduced costs)',
                       orbits=int(len(sizes))),
               timings=dict(lp_s=res["lp_time"], validation_s=time.time() - tb, total_s=time.time() - t0),
               note="R_upper_gridLP is an upper bound for the discretised LP only (relaxation of the continuum LP "
                    "once converged). Lower bounds are MEASURED (floating point), not exact-arithmetic proofs.",
               history_tail=res["hist"][-5:])
    receipt["result"] = out
    np.savez(os.path.join(args.workdir, f"torus_f_n{n}_e{args.extra}.npz"), corb=corb, reps=sp["reps"])
    if args.out:
        json.dump(receipt, open(args.out, "w"), indent=1)
    print(json.dumps(out, indent=1))


def q1a():
    from collections import Counter
    res = {}
    for n in range(2, 9):
        A = [(a, b, c) for a in range(-n + 1, n) for b in range(-n + 1, n) for c in range(-n + 1, n)
             if abs(a) + abs(b) + abs(c) <= n - 1]
        m = len(A)
        assert m == m_n(n)
        arr = np.array(A, dtype=np.int64)
        cnt = Counter()
        for p in arr:
            d = p[None, :] - arr
            for row in map(tuple, d):
                cnt[row] += 1
        a0 = cnt[(0, 0, 0)]
        tot = sum(cnt.values())
        spec_ok = all(sum(abs(x) for x in k) <= 2 * n - 2 for k in cnt)
        # f = |D|^2 / m : c_k = cnt/m, c_0 = a0/m = 1; f(0) = tot/m = m
        res[n] = dict(m_n=m, a0=a0, sum_a=tot, m_squared=m * m, f0_over_c0_equals_m=(tot == m * m and a0 == m),
                      spectrum_ok=spec_ok, f0_over_c0=f"{tot}/{a0}", exact=tot // a0 if tot % a0 == 0 else None)
    return res


if __name__ == "__main__":
    main()
