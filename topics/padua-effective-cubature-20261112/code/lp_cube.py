#!/usr/bin/env python3
"""Cube-native LP (plan.md section 2) for positive cubature on [-1,1]^3, mu = product Chebyshev.

lambda_n = sup lambda,  G(x,y) = sum_{|a|_1,|b|_1<=2n-1} g_ab T_a(x) T_b(y),
 G >= 0 on cube^2,  G(x,x) >= lambda K(x,x)^2 on the cube,  g_00 = D.
Symmetry reduction: g_ab = g_ba, simultaneous S3 permutation, sign flips force a_i+b_i even.
Cutting-plane LP (HiGHS) with x=cos(theta).  Output is an UPPER bound (relaxation) and a
local-search-based (NOT rigorous) eps-shift lower estimate.
  --q1a : exact rational check that G=K^2 gives integral D and G(x,x)=K(x,x)^2 (n=2..8)
  --n N : run the LP
"""
import argparse, hashlib, itertools, json, os, platform, sys, time
from fractions import Fraction
import numpy as np, scipy
import scipy.optimize
import highspy

PI = np.pi


def multi(deg):
    return [(i, j, k) for i in range(deg + 1) for j in range(deg + 1 - i) for k in range(deg + 1 - i - j)]


def nnz(a):
    return sum(1 for x in a if x)


def D_of(n):
    return (n + 2) * (n + 1) * n // 6


def tprod(p, q):
    """T_p T_q = (T_{p+q} + T_{|p-q|})/2 as dict {r: Fraction}."""
    if p == 0 or q == 0:
        return {p + q: Fraction(1)}
    d = {}
    for r in (p + q, abs(p - q)):
        d[r] = d.get(r, 0) + Fraction(1, 2)
    return d


def q1a():
    res = {}
    pts = [(Fraction(1, 3), Fraction(2, 5), Fraction(-3, 7)), (Fraction(5, 11), Fraction(-1, 2), Fraction(7, 13)),
           (Fraction(-9, 10), Fraction(3, 4), Fraction(1, 17))]

    def Tev(deg, x):
        T = [Fraction(1), x]
        for _ in range(2, deg + 1):
            T.append(2 * x * T[-1] - T[-2])
        return T
    for n in range(2, 9):
        A = [a for a in multi(n - 1)]
        w = {a: 2 ** nnz(a) for a in A}
        g = {}
        # K(x,y)^2 = sum_{a,a'} w_a w_a' (T_a T_a')(x) (T_a T_a')(y)
        for a in A:
            for a2 in A:
                # expand prod_i T_{a_i} T_{a2_i}
                terms = {(): Fraction(1)}
                for i in range(3):
                    dd = tprod(a[i], a2[i])
                    new = {}
                    for k, v in terms.items():
                        for r, c in dd.items():
                            new[k + (r,)] = new.get(k + (r,), 0) + v * c
                    terms = new
                ww = w[a] * w[a2]
                for p, cp in terms.items():
                    for q, cq in terms.items():
                        g[(p, q)] = g.get((p, q), 0) + ww * cp * cq
        D = D_of(n)
        g00 = g[((0, 0, 0), (0, 0, 0))]
        maxdeg = max(max(p) for p, q in g)
        tot_deg = max(sum(p) for p, q in g)
        # exact identity G(x,x) = K(x,x)^2 at rational points
        ok = True
        for x in pts:
            Tx = [Tev(2 * n, xi) for xi in x]
            def Tm(a):
                return Tx[0][a[0]] * Tx[1][a[1]] * Tx[2][a[2]]
            Gxx = sum(c * Tm(p) * Tm(q) for (p, q), c in g.items())
            Kxx = sum(w[a] * Tm(a) ** 2 for a in A)
            ok &= (Gxx == Kxx ** 2)
        res[n] = dict(D=D, g00=str(g00), g00_equals_D=bool(g00 == D), identity_G_xx_eq_Kxx_sq_at_3_rational_points=bool(ok),
                      max_total_degree_in_each_variable=tot_deg, within_2n_minus_1=bool(tot_deg <= 2 * n - 1 + 0 or tot_deg <= 2 * n - 2),
                      lambda_G_eq_K2=1)
    return res


class Setup:
    def __init__(self, n):
        self.n = n
        self.D = D_of(n)
        self.Aall = multi(2 * n - 1)
        self.A_idx = {a: i for i, a in enumerate(self.Aall)}
        self.amat = np.array(self.Aall)  # A x 3
        self.Kidx = [i for i, a in enumerate(self.Aall) if sum(a) <= n - 1]
        self.Kw = np.array([2.0 ** nnz(self.Aall[i]) for i in self.Kidx])
        perms = list(itertools.permutations(range(3)))
        orb = {}
        pair_orb = []
        self.pairs = []
        for ia, a in enumerate(self.Aall):
            for ib, b in enumerate(self.Aall):
                if any((a[i] + b[i]) % 2 for i in range(3)):
                    continue
                best = None
                for p in perms:
                    ap = tuple(a[p[i]] for i in range(3)); bp = tuple(b[p[i]] for i in range(3))
                    for t in (ap + bp, bp + ap):
                        if best is None or t < best:
                            best = t
                if best not in orb:
                    orb[best] = len(orb)
                self.pairs.append((ia, ib)); pair_orb.append(orb[best])
        self.pairs = np.array(self.pairs); self.pair_orb = np.array(pair_orb)
        self.nv = len(orb)
        self.reps = list(orb.keys())
        self.v0 = orb[(0,) * 6]
        # bound |g| <= D 2^{nnz a + nnz b} (uses orthogonality of T_a)
        self.ub = np.array([self.D * 2.0 ** (nnz(r[:3]) + nnz(r[3:])) for r in self.reps])

    def Tmat(self, theta):
        """theta: P x 3 -> P x A matrix of prod_i cos(a_i theta_i)."""
        C = np.cos(theta[:, :, None] * np.arange(2 * self.n)[None, None, :])  # P x 3 x deg
        return C[:, 0, self.amat[:, 0]] * C[:, 1, self.amat[:, 1]] * C[:, 2, self.amat[:, 2]]

    def rows_G(self, th, ph):
        Ta, Tb = self.Tmat(th), self.Tmat(ph)
        prod = Ta[:, self.pairs[:, 0]] * Tb[:, self.pairs[:, 1]]  # P x npairs
        out = np.zeros((len(th), self.nv))
        for v in range(0):
            pass
        # aggregate by orbit
        order = np.argsort(self.pair_orb, kind="stable")
        so = self.pair_orb[order]
        starts = np.concatenate([[0], np.nonzero(np.diff(so))[0] + 1])
        out = np.add.reduceat(prod[:, order], starts, axis=1)
        return out

    def Kxx(self, th):
        T = self.Tmat(th)[:, self.Kidx]
        return (T ** 2) @ self.Kw

    def Gval(self, gv, th, ph):
        return self.rows_G(th, ph) @ gv


def fund_x(P, rng):
    th = np.sort(rng.uniform(0, PI / 2, (P, 3)), axis=1)[:, ::-1]  # x_i>=0 sorted: theta ascending <-> x descending
    return np.ascontiguousarray(th[:, ::-1])


def run(n, args):
    t0 = time.time()
    S = Setup(n)
    rng = np.random.default_rng(args.seed)
    nv = S.nv
    h = highspy.Highs(); h.setOptionValue("output_flag", False)
    h.setOptionValue("primal_feasibility_tolerance", 1e-9); h.setOptionValue("dual_feasibility_tolerance", 1e-9)
    inf = highspy.kHighsInf
    lb = -S.ub.copy(); ub = S.ub.copy()
    lb[S.v0] = ub[S.v0] = S.D
    h.addVars(nv + 1, np.concatenate([lb, [0.0]]), np.concatenate([ub, [50.0]]))
    cost = np.zeros(nv + 1); cost[nv] = 1.0
    h.changeColsCost(nv + 1, np.arange(nv + 1, dtype=np.int32), cost)
    h.changeObjectiveSense(highspy.ObjSense.kMaximize)

    def add_rows(Rm, lo):
        m = len(Rm)
        idx = np.tile(np.arange(Rm.shape[1], dtype=np.int32), m)
        h.addRows(m, lo, np.full(m, inf), m * Rm.shape[1], (np.arange(m) * Rm.shape[1]).astype(np.int32), idx, Rm.ravel())

    def add_G(th, ph):
        Rm = S.rows_G(th, ph)
        add_rows(np.hstack([Rm, np.zeros((len(Rm), 1))]), np.zeros(len(Rm)))

    def add_diag(th):
        Rm = S.rows_G(th, th); Kx = S.Kxx(th)
        add_rows(np.hstack([Rm, -(Kx ** 2)[:, None]]), np.zeros(len(Rm)))
    # initial points
    th = fund_x(args.init, rng); ph = rng.uniform(0, PI, (args.init, 3))
    add_G(th, ph)
    thd = fund_x(args.init_diag, rng)
    add_diag(thd)
    hist = []
    for it in range(1, args.max_iter + 1):
        h.run()
        sol = np.array(h.getSolution().col_value)
        gv, lam = sol[:nv], sol[nv]
        # search violations of G >=0
        cth = fund_x(args.cand, rng); cph = rng.uniform(0, PI, (args.cand, 3))
        vals = S.Gval(gv, cth, cph)
        sel = np.argsort(vals)[:args.nref]
        def fG(z):
            t = np.clip(z[:3], 0, PI / 2)[None]; p = z[3:][None]
            return float(S.Gval(gv, t, p)[0])
        newt, newp, minG = [], [], np.inf
        for i in sel:
            z0 = np.concatenate([cth[i], cph[i]])
            r = scipy.optimize.minimize(fG, z0, method="L-BFGS-B", bounds=[(0, PI / 2)] * 3 + [(0, PI)] * 3,
                                        options=dict(maxiter=60, ftol=1e-15, gtol=1e-10))
            minG = min(minG, r.fun)
            z = r.x
            t = np.sort(z[:3]); newt.append(t); newp.append(z[3:])
        # diag
        cd = fund_x(args.cand, rng)
        dvals = S.Gval(gv, cd, cd) - lam * S.Kxx(cd) ** 2
        seld = np.argsort(dvals)[:args.nref]
        def fD(z):
            t = np.clip(z, 0, PI / 2)[None]
            return float((S.Gval(gv, t, t) - lam * S.Kxx(t) ** 2)[0])
        newd, minD = [], np.inf
        for i in seld:
            r = scipy.optimize.minimize(fD, cd[i], method="L-BFGS-B", bounds=[(0, PI / 2)] * 3, options=dict(maxiter=60, ftol=1e-15, gtol=1e-10))
            minD = min(minD, r.fun); newd.append(np.sort(r.x))
        hist.append((it, lam, minG, minD))
        if args.verbose:
            print(f"n={n} it={it} lam={lam:.8f} minG={minG:.3e} minD={minD:.3e} {time.time()-t0:.0f}s", flush=True)
        if minG >= -args.tol * S.D and minD >= -args.tol * S.D:
            break
        add_G(np.array(newt), np.array(newp)); add_diag(np.array(newd))
    return S, gv, lam, minG, minD, hist, time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int); ap.add_argument("--q1a", action="store_true")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--init", type=int, default=4000); ap.add_argument("--init-diag", type=int, default=1500)
    ap.add_argument("--cand", type=int, default=30000); ap.add_argument("--nref", type=int, default=150)
    ap.add_argument("--max-iter", type=int, default=150); ap.add_argument("--tol", type=float, default=1e-9)
    ap.add_argument("--verbose", action="store_true"); ap.add_argument("--out", required=True)
    args = ap.parse_args()
    rec = dict(script_sha256=hashlib.sha256(open(__file__, "rb").read()).hexdigest(), python=platform.python_version(),
               numpy=np.__version__, scipy=scipy.__version__, argv=sys.argv, args=vars(args))
    if args.q1a:
        rec["q1a"] = q1a(); json.dump(rec, open(args.out, "w"), indent=1); print(json.dumps(rec["q1a"])); return
    S, gv, lam, minG, minD, hist, secs = run(args.n, args)
    D = S.D
    eps = max(0.0, -minG, -minD)  # K(x,x)^2 >= 1 so a diagonal defect <= eps is absorbed by +eps
    lam_low = max(0.0, lam * D / (D + eps)) if eps > 0 else lam
    lam_low_conservative = lam * D / (D + eps)
    rec["result"] = dict(n=args.n, D=D, variables=S.nv, lambda_upper_LP=lam, minG_found=minG, minDiag_found=minD,
                         eps_shift=eps, lambda_lower_estimate=lam_low_conservative, iterations=len(hist),
                         seconds=secs, tolerance=args.tol, history_tail=hist[-4:],
                         note="UPPER bound is for the discretised (cut) LP; lower estimate uses local-search minima, NOT rigorous.")
    json.dump(rec, open(args.out, "w"), indent=1)
    print(json.dumps(rec["result"], indent=1))


if __name__ == "__main__":
    main()
