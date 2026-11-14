#!/usr/bin/env python3
"""G1 argmax screen for Xu points (gates.md G1), MEASURED only.

Usage:  python3 code/xu/g1_screen.py --nmin 2 --nmax 60 [--summary evidence/xu-g1-summary.json] [--raw /tmp/xu-runs]
                                     [--digits 40] [--ns 2,3,5]
Per n: uniform angle grid M = max(64,12n) in (theta,phi) in [0,pi]^2; lambda_n by float64 kernel (xu_kernel.XuFloat);
symmetry reduction by Lemma S only (even n: full dihedral group, odd n: swap and (x,y)->(-x,-y)); discrete local
maxima (8-neighbourhood in the interior, 1-D along edges, corners always) with value >= 0.9 max_{V*} lambda;
bounded L-BFGS-B refinement on the face; polish at `digits` digits by Newton on the frozen-sign cosine polynomial
(python-flint arb) with a direct enclosure evaluation of lambda; classify points within 1e-8 of a vertex as vertex;
g_n = 1 - max_nonvertex / min_{V*} lambda; g_n < 1e-6 are re-polished at 60 digits.
Path-A cross-check (xu_exact) of the float64 grid for n <= 12.
"""
import sys, os, json, time, argparse, platform
import numpy as np
import mpmath as mp
import flint
from flint import arb, arb_mat, ctx
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import xu_kernel as K

PI = np.pi
EDGE_TOL = 1e-10
VERT_TOL = 1e-8


# ------------------------------------------------------------------ symmetry helpers
def group(n):
    """List of maps on (theta,phi) angle pairs (floats or arb) -> as (swap, flipx, flipy), Lemma S."""
    if n % 2 == 0:
        return [(sw, fx, fy) for sw in (0, 1) for fx in (0, 1) for fy in (0, 1)]
    return [(0, 0, 0), (1, 0, 0), (0, 1, 1), (1, 1, 1)]


def act_idx(g, i, j, M):
    sw, fx, fy = g
    a = M - i if fx else i
    b = M - j if fy else j
    return (b, a) if sw else (a, b)


def act_ang(g, th, ph):
    sw, fx, fy = g
    a = PI - th if fx else th
    b = PI - ph if fy else ph
    return (b, a) if sw else (a, b)


def canon_idx(n, i, j, M):
    return min(act_idx(g, i, j, M) for g in group(n))


def canon_ang(n, th, ph, nd=6):
    return min((round(x, nd) + 0.0, round(y, nd) + 0.0) for (x, y) in (act_ang(g, th, ph) for g in group(n)))


# ------------------------------------------------------------------ grid
def full_grid(n, X, M):
    h = np.arange(0, M + 1) * PI / M
    half = np.arange(0, M // 2 + 1) * PI / M
    idx = np.arange(M + 1)
    if n % 2 == 0:
        Q = X.grid(half, half)
        im = np.minimum(idx, M - idx)
        L = Q[np.ix_(im, im)]
    else:
        H = X.grid(half, h)  # rows theta<=pi/2, all phi
        L = np.empty((M + 1, M + 1))
        L[: M // 2 + 1] = H
        for i in range(M // 2 + 1, M + 1):
            L[i] = H[M - i][::-1]
    return L


def grid_local_max(L, thr):
    """Return list of (i,j,face) discrete local maxima with value >= thr. face in
    'int','e_th0','e_thpi','e_ph0','e_phpi','corner'."""
    M = L.shape[0] - 1
    out = []
    c = L[1:-1, 1:-1]
    mask = c >= thr
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            mask &= c >= L[1 + di:M + di, 1 + dj:M + dj]
    for i, j in zip(*np.nonzero(mask)):
        out.append((i + 1, j + 1, "int"))
    # edges (1-D)
    e = L[0, 1:-1]; m = (e >= thr) & (e >= L[0, :-2]) & (e >= L[0, 2:])
    out += [(0, j + 1, "e_th0") for j in np.nonzero(m)[0]]
    e = L[M, 1:-1]; m = (e >= thr) & (e >= L[M, :-2]) & (e >= L[M, 2:])
    out += [(M, j + 1, "e_thpi") for j in np.nonzero(m)[0]]
    e = L[1:-1, 0]; m = (e >= thr) & (e >= L[:-2, 0]) & (e >= L[2:, 0])
    out += [(i + 1, 0, "e_ph0") for i in np.nonzero(m)[0]]
    e = L[1:-1, M]; m = (e >= thr) & (e >= L[:-2, M]) & (e >= L[2:, M])
    out += [(i + 1, M, "e_phpi") for i in np.nonzero(m)[0]]
    for (i, j) in [(0, 0), (0, M), (M, 0), (M, M)]:
        if L[i, j] >= thr:
            out.append((i, j, "corner"))
    return out


# ------------------------------------------------------------------ float refinement
def refine_float(X, th, ph, face):
    if face == "corner":
        return th, ph
    if face == "int":
        f = lambda p: tuple(-v if k == 0 else -v for k, v in enumerate((0, 0))) if False else None
        def fun(p):
            lam, g, _ = X.val_grad(p[0], p[1])
            return -lam, -g
        r = minimize(fun, [th, ph], jac=True, method="L-BFGS-B", bounds=[(0, PI), (0, PI)],
                     options={"ftol": 1e-16, "gtol": 1e-11, "maxiter": 300, "maxcor": 20})
        return float(r.x[0]), float(r.x[1])
    # edge: 1-D along the free coordinate
    if face in ("e_th0", "e_thpi"):
        fixed = 0.0 if face == "e_th0" else PI
        def fun(p):
            lam, g, _ = X.val_grad(fixed, p[0])
            return -lam, np.array([-g[1]])
        r = minimize(fun, [ph], jac=True, method="L-BFGS-B", bounds=[(0, PI)],
                     options={"ftol": 1e-16, "gtol": 1e-11, "maxiter": 300})
        return fixed, float(r.x[0])
    fixed = 0.0 if face == "e_ph0" else PI
    def fun(p):
        lam, g, _ = X.val_grad(p[0], fixed)
        return -lam, np.array([-g[0]])
    r = minimize(fun, [th], jac=True, method="L-BFGS-B", bounds=[(0, PI)],
                 options={"ftol": 1e-16, "gtol": 1e-11, "maxiter": 300})
    return float(r.x[0]), fixed


def snap_face(th, ph):
    th2 = 0.0 if th < EDGE_TOL else (PI if PI - th < EDGE_TOL else th)
    ph2 = 0.0 if ph < EDGE_TOL else (PI if PI - ph < EDGE_TOL else ph)
    on_t = th2 in (0.0, PI)
    on_p = ph2 in (0.0, PI)
    if on_t and on_p:
        face = "corner"
    elif on_t:
        face = "e_th0" if th2 == 0.0 else "e_thpi"
    elif on_p:
        face = "e_ph0" if ph2 == 0.0 else "e_phpi"
    else:
        face = "int"
    return th2, ph2, face


# ------------------------------------------------------------------ arb polish
class Polisher:
    def __init__(self, n, digits):
        self.n = n
        self.digits = digits
        self.prec = int(digits * 3.33) + 64
        ctx.prec = self.prec
        k = np.arange(n + 1)
        self.sig = K.sigma(n)
        Cn = arb_mat(n + 1, n + 1)
        for a in range(n + 1):
            for b in range(n + 1):
                Cn[a, b] = (arb((a * b) % (2 * n)) / n).cos_pi()
        self.Cn = Cn
        self.CnT = Cn.transpose()
        self.eps = [arb(1) if i == 0 else arb(2) for i in range(n + 1)]
        Qm = arb_mat(n + 1, n + 1)
        for a in range(n + 1):
            for b in range(n + 1):
                if a + b <= n - 1:
                    Qm[a, b] = 1
                elif a + b == n:
                    Qm[a, b] = arb(1) / 2
        self.Qm = Qm
        self.W = {}
        for (r, s) in K.nodes(n):
            self.W[(r, s)] = arb(2) / (n * n * 2 ** K.beta(n, r, s))

    def trig(self, th, ph):
        n = self.n
        ck = [(th * i).cos() for i in range(n + 1)]
        sk = [(th * i).sin() for i in range(n + 1)]
        cl = [(ph * i).cos() for i in range(n + 1)]
        sl = [(ph * i).sin() for i in range(n + 1)]
        return ck, sk, cl, sl

    def kt_matrix(self, th, ph):
        n = self.n
        ck, sk, cl, sl = self.trig(th, ph)
        Au = arb_mat(n + 1, n + 1)
        Bv = arb_mat(n + 1, n + 1)
        for a in range(n + 1):
            for b in range(n + 1):
                Au[a, b] = self.CnT[a, b] * self.eps[b] * ck[b]   # [r,k] = Cn[k,r] eps_k cos k th
                Bv[a, b] = self.Cn[a, b] * self.eps[a] * cl[a]    # [l,s] = Cn[l,s] eps_l cos l ph
        Km = (Au * self.Qm) * Bv
        cn_t = ck[n]; cn_p = cl[n]
        return Km, cn_t, cn_p

    def lam_signs(self, th, ph):
        n = self.n
        Km, cnt, cnp = self.kt_matrix(th, ph)
        tot = arb(0)
        S = {}
        minabs = None
        for (r, s) in K.nodes(n):
            kt = Km[r, s] - arb(1) / 2 * (-1) ** r * (cnt - self.sig * cnp)
            tot += self.W[(r, s)] * abs(kt)
            m = float(kt.mid())
            S[(r, s)] = 1 if m > 0 else -1
            ab = abs(m) * float(self.W[(r, s)].mid())
            minabs = ab if minabs is None else min(minabs, ab)
        return tot, S, minabs

    def coeff_matrix(self, S):
        n = self.n
        U = arb_mat(n + 1, n + 1)
        E = arb(0)
        for (r, s), sg in S.items():
            u = self.W[(r, s)] * sg
            U[r, s] = u
            E += u * (-1) ** r
        base = self.Cn * U * self.CnT   # [k,l] = sum Cn[k,r] U[r,s] Cn[l,s]
        C = arb_mat(n + 1, n + 1)
        for a in range(n + 1):
            for b in range(n + 1):
                C[a, b] = base[a, b] * self.Qm[a, b] * self.eps[a] * self.eps[b]
        E = -E / 2
        C[n, 0] = C[n, 0] + E
        C[0, n] = C[0, n] - self.sig * E
        return C

    def derivs(self, C, th, ph):
        n = self.n
        ck, sk, cl, sl = self.trig(th, ph)
        L = arb_mat(n + 1, 3)
        for l in range(n + 1):
            L[l, 0] = cl[l]
            L[l, 1] = -l * sl[l]
            L[l, 2] = -(l * l) * cl[l]
        Mv = C * L
        F = Ft = Ftt = Fp = Fpp = Ftp = arb(0)
        for k in range(n + 1):
            a0, a1, a2 = Mv[k, 0], Mv[k, 1], Mv[k, 2]
            F += ck[k] * a0
            Ft += (-k * sk[k]) * a0
            Ftt += (-(k * k) * ck[k]) * a0
            Fp += ck[k] * a1
            Fpp += ck[k] * a2
            Ftp += (-k * sk[k]) * a1
        return F, (Ft, Fp), (Ftt, Ftp, Fpp)

    def polish(self, th0, ph0, face, S0=None):
        """Newton on frozen-sign polynomial restricted to the face; re-freeze signs until consistent."""
        n = self.n
        ctx.prec = self.prec
        th, ph = arb(th0), arb(ph0)
        th_start, ph_start = th, ph
        S = S0
        if S is None:
            _, S, _ = self.lam_signs(th, ph)
        tol = arb(10) ** (-(self.digits + 6))
        info = {}
        for outer in range(8):
            C = self.coeff_matrix(S)
            for it in range(40):
                F, g, H = self.derivs(C, th, ph)
                if face == "int":
                    det = H[0] * H[2] - H[1] * H[1]
                    if not (abs(float(det.mid())) > 1e-12):
                        break
                    dth = -(g[0] * H[2] - g[1] * H[1]) / det
                    dph = -(g[1] * H[0] - g[0] * H[1]) / det
                    if face == "int":
                        th, ph = th + dth, ph + dph
                    step = max(abs(float(dth)), abs(float(dph)))
                    gn = max(abs(float(g[0])), abs(float(g[1])))
                elif face in ("e_th0", "e_thpi"):
                    if not (abs(float(H[2].mid())) > 1e-12):
                        break
                    dph = -g[1] / H[2]
                    ph = ph + dph
                    step = abs(float(dph)); gn = abs(float(g[1]))
                elif face in ("e_ph0", "e_phpi"):
                    if not (abs(float(H[0].mid())) > 1e-12):
                        break
                    dth = -g[0] / H[0]
                    th = th + dth
                    step = abs(float(dth)); gn = abs(float(g[0]))
                else:
                    step = 0.0; gn = 0.0
                if face == "corner" or step < 10.0 ** (-(self.digits + 8)) or (step == 0.0):
                    break
                if step < 1e-30 and step < float(tol) :
                    # quadratic convergence: one more evaluation done at loop top; finish
                    pass
            lam, S2, minabs = self.lam_signs(th, ph)
            if all(S2[k] == S[k] for k in S):
                break
            S = S2
        F, g, H = self.derivs(self.coeff_matrix(S), th, ph)
        lam, S2, minabs = self.lam_signs(th, ph)
        consistent = all(S2[k] == S[k] for k in S)
        gmax = max(abs(float(g[0].mid())), abs(float(g[1].mid())))
        if face in ("e_th0", "e_thpi"):
            gmax = abs(float(g[1].mid()))
        elif face in ("e_ph0", "e_phpi"):
            gmax = abs(float(g[0].mid()))
        converged = bool(gmax < 10.0 ** (-(self.digits - 8)))
        if not converged:  # degenerate (flat) critical set or failure: report value at the float point
            th, ph = th_start, ph_start
            lam, S2, minabs = self.lam_signs(th, ph)
            consistent = False
        Hf = [float(H[0]), float(H[1]), float(H[2])]
        gfl = [float(g[0]), float(g[1])]
        return dict(th=th, ph=ph, lam=lam, sign_consistent=consistent, min_abs_wl=minabs, converged=converged, gmax=gmax,
                    grad=gfl, hess=Hf, face=face, S=S)


def hess_class(face, hess):
    """True if the Hessian (full 2-D, even extension across the boundary) is negative semidefinite-ish:
    all eigenvalues <= 1e-9 (local max in Q for the polished critical point)."""
    a, b, c = hess
    H = np.array([[a, b], [b, c]])
    ev = np.linalg.eigvalsh(H)
    return bool(ev[1] <= 1e-9), [float(ev[0]), float(ev[1])]


# ------------------------------------------------------------------ main per-n
def run_n(n, digits, raw_dir, xexact_check=True):
    t0 = time.time()
    X = K.XuFloat(n)
    M = max(64, 12 * n)
    L = full_grid(n, X, M)
    tgrid = time.time() - t0
    if n % 2 == 0:
        Vidx = [(0, 0), (0, M), (M, 0), (M, M)]
    else:
        Vidx = [(0, M), (M, 0)]  # (1,-1) and (-1,1)
    Vmax = max(L[i, j] for i, j in Vidx)
    Vminf = min(L[i, j] for i, j in Vidx)
    cand = grid_local_max(L, 0.9 * Vmax)
    # dedupe grid candidates by symmetry orbit
    orb = {}
    for (i, j, f) in cand:
        key = canon_idx(n, i, j, M)
        if key not in orb:
            orb[key] = (i, j, f)
    ncand_grid = len(cand)
    reps = list(orb.values())
    reps.sort(key=lambda r: -L[r[0], r[1]])
    reps = reps[:80]
    # make sure at least 6 non-vertex orbit reps are refined (even below 0.9 threshold) for reporting
    nonv = [r for r in reps if r[2] != "corner"]
    if len(nonv) < 6:
        extra = grid_local_max(L, 0.0)
        extra = [e for e in extra if e[2] != "corner"]
        extra.sort(key=lambda e: -L[e[0], e[1]])
        have = set(canon_idx(n, i, j, M) for (i, j, f) in reps)
        for (i, j, f) in extra:
            key = canon_idx(n, i, j, M)
            if key in have:
                continue
            have.add(key)
            reps.append((i, j, f))
            nonv.append((i, j, f))
            if len(nonv) >= 6:
                break
    # additionally refine the top-3 INTERIOR local-maximum orbits regardless of threshold (structure report)
    have = set(canon_idx(n, i, j, M) for (i, j, f) in reps)
    ints = [e for e in grid_local_max(L, 0.0) if e[2] == "int"]
    ints.sort(key=lambda e: -L[e[0], e[1]])
    added = 0
    for (i, j, f) in ints:
        key = canon_idx(n, i, j, M)
        if key in have:
            continue
        have.add(key)
        reps.append((i, j, f))
        added += 1
        if added >= 3:
            break
    pol = Polisher(n, digits)
    results = []
    vtx_ang = [(0.0, 0.0), (0.0, PI), (PI, 0.0), (PI, PI)]
    for (i, j, f) in reps:
        th0, ph0 = i * PI / M, j * PI / M
        th, ph = refine_float(X, th0, ph0, f)
        th, ph, face = snap_face(th, ph)
        isvert = any(max(abs(th - a), abs(ph - b)) < VERT_TOL for (a, b) in vtx_ang)
        rec = dict(grid=(int(i), int(j)), grid_face=f, grid_val=float(L[i, j]), th_f=th, ph_f=ph, face=face)
        if isvert:
            rec["vertex"] = True
            results.append(rec)
            continue
        P = pol.polish(th, ph, face)
        rec.update(vertex=False, converged=P["converged"], th=P["th"], ph=P["ph"], lam=P["lam"], sign_consistent=P["sign_consistent"],
                   min_abs_wl=P["min_abs_wl"], grad=P["grad"], hess=P["hess"])
        # classify vertex again after polishing
        thf, phf = float(P["th"]), float(P["ph"])
        if any(max(abs(thf - a), abs(phf - b)) < VERT_TOL for (a, b) in vtx_ang):
            rec["vertex"] = True
        results.append(rec)
    # vertex values (enclosures)
    ctx.prec = pol.prec
    vvals = []
    for (a, b) in [(0, 0), (0, 1), (1, 0), (1, 1)] if n % 2 == 0 else [(0, 1), (1, 0)]:
        lam, _, _ = pol.lam_signs(arb(a) * arb.pi(), arb(b) * arb.pi()) if False else pol.lam_signs(arb(a) * arb.pi(), arb(b) * arb.pi())
        vvals.append(lam)
    vmin = min(vvals, key=lambda x: float(x.mid()))
    # distinct non-vertex orbits
    nv = [r for r in results if not r.get("vertex")]
    seen = {}
    for r in nv:
        key = canon_ang(n, float(r["th"]), float(r["ph"]))
        if key not in seen or float(r["lam"].mid()) > float(seen[key]["lam"].mid()):
            seen[key] = r
    classes = sorted(seen.values(), key=lambda r: -float(r["lam"].mid()))
    # g_n
    best = classes[0] if classes else None
    out = dict(n=n, M=M, parity="even" if n % 2 == 0 else "odd", ncand_grid=ncand_grid, n_orbits_refined=len(reps),
               n_vertex_orbits=sum(1 for r in results if r.get("vertex")), n_nonvertex_orbits=len(classes),
               grid_vertex_max=float(Vmax), grid_max=float(L.max()))
    out["vertex_lam"] = [v.str(30, radius=False) for v in vvals]
    out["min_vertex_lam"] = vmin.str(30, radius=False)
    if best is not None:
        g = 1 - best["lam"] / vmin
        out["g_n"] = float(g.mid())
        out["g_n_str"] = g.str(12, radius=False)
        out["best_nonvertex"] = fmt_class(best, n)
        out["classes"] = [fmt_class(r, n) for r in classes[:6]]
        ints_c = [r for r in classes if r["face"] == "int"]
        if ints_c:
            bi = fmt_class(ints_c[0], n)
            bi["ratio_to_vertex"] = float((ints_c[0]["lam"] / vmin).mid())
            out["best_interior"] = bi
        edges_c = [r for r in classes if r["face"] != "int"]
        out["n_edge_classes"] = len(edges_c)
        out["n_interior_classes"] = len(ints_c)
        out["raw_classes_all"] = [fmt_class(r, n) for r in classes]
        if float(g.mid()) < 1e-6:
            pol60 = Polisher(n, 60)
            P = pol60.polish(float(best["th"]), float(best["ph"]), best["face"])
            ctx.prec = pol60.prec
            vv60 = [pol60.lam_signs(arb(a) * arb.pi(), arb(b) * arb.pi())[0]
                    for (a, b) in ([(0, 0), (0, 1), (1, 0), (1, 1)] if n % 2 == 0 else [(0, 1), (1, 0)])]
            vm60 = min(vv60, key=lambda x: float(x.mid()))
            g60 = 1 - P["lam"] / vm60
            out["repolish60"] = dict(g_n=g60.str(20, radius=False), lam=P["lam"].str(60, radius=False),
                                     vertex=vm60.str(60, radius=False))
    else:
        out["g_n"] = None
        out["note"] = "no non-vertex local maximum found"
    # path A cross-check
    if xexact_check and n <= 12:
        from xu_exact import XuExact
        XA = XuExact(n, 256)
        rng = np.random.default_rng(20261114 + n)
        md = 0.0
        for _ in range(30):
            i, j = rng.integers(0, M + 1, 2)
            lamA = XA.lam((arb(float(i * PI / M)), arb(float(j * PI / M))))
            md = max(md, abs(float(lamA.mid()) - L[i, j]))
        out["pathA_grid_crosscheck_max_abs_diff"] = md
        ctx.prec = pol.prec
    out["seconds"] = round(time.time() - t0, 1)
    out["seconds_grid"] = round(tgrid, 1)
    # raw dump
    if raw_dir:
        raw = dict(out)
        raw["all_refined"] = []
        for r in results:
            d = {k: (v.str(40, radius=False) if hasattr(v, "str") else v) for k, v in r.items() if k not in ("S",)}
            raw["all_refined"].append(d)
        with open(os.path.join(raw_dir, "g1_raw_n%d.json" % n), "w") as fh:
            json.dump(raw, fh, default=str)
    return out


def fmt_class(r, n):
    th, ph = float(r["th"]), float(r["ph"])
    ishmax, ev = hess_class(r["face"], r["hess"])
    return dict(face=r["face"], th_pi=round(th / PI, 10), ph_pi=round(ph / PI, 10),
                lam=r["lam"].str(30, radius=False), locmax_Q=ishmax,
                signs_ok=bool(r["sign_consistent"]), converged=bool(r.get("converged", False)))


def compact(o, digits_keep=20):
    """Compact per-n record for the summary file."""
    c = dict(n=o["n"], M=o["M"], v=o["min_vertex_lam"][:22], nloc=o["ncand_grid"], nnv=o["n_nonvertex_orbits"],
             ne=o.get("n_edge_classes"), ni=o.get("n_interior_classes"), g=o.get("g_n"), t=o["seconds"])
    if o.get("best_nonvertex"):
        b = o["best_nonvertex"]
        c["best"] = [b["face"], b["th_pi"], b["ph_pi"], b["lam"][:22], int(b["locmax_Q"])]
        c["top"] = [[x["face"], round(x["th_pi"], 4), round(x["ph_pi"], 4), x["lam"][:9]] for x in o["classes"][1:2]]
        if o.get("best_interior"):
            bi = o["best_interior"]
            c["bi"] = [round(bi["th_pi"], 4), round(bi["ph_pi"], 4), bi["lam"][:9], round(bi["ratio_to_vertex"], 4)]
    if "repolish60" in o:
        c["g60"] = o["repolish60"]["g_n"][:14]
    if "pathA_grid_crosscheck_max_abs_diff" in o:
        c["pA"] = float("%.2g" % o["pathA_grid_crosscheck_max_abs_diff"])
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmin", type=int, default=2)
    ap.add_argument("--nmax", type=int, default=60)
    ap.add_argument("--ns", default=None, help="comma list overriding nmin/nmax")
    ap.add_argument("--digits", type=int, default=40)
    ap.add_argument("--summary", default=os.path.join(HERE, "..", "..", "evidence", "xu-g1-summary.json"))
    ap.add_argument("--raw", default="/tmp/xu-runs")
    a = ap.parse_args()
    ns = [int(x) for x in a.ns.split(",")] if a.ns else list(range(a.nmin, a.nmax + 1))
    os.makedirs(a.raw, exist_ok=True)
    summ = dict(what="G1 screen, X1 Xu points (MEASURED only); keys: n, M, v=vertex lambda (V*), nloc=#grid local maxima >=0.9V*, "
                     "nnv=#distinct non-vertex orbits refined, g=g_n, best=[face,theta/pi,phi/pi,lambda,locmaxQ], "
                     "top=2nd non-vertex class [face,th/pi,ph/pi,lambda], bi=best interior local max [th/pi,ph/pi,lambda,ratio to vertex], ne/ni=#edge/#interior non-vertex orbits refined, g60=60-digit g_n if g<1e-6, pA=pathA grid cross-check, t=seconds",
                command=" ".join(sys.argv),
                versions=dict(python=platform.python_version(), numpy=np.__version__, scipy=__import__("scipy").__version__,
                              mpmath=mp.__version__, python_flint=flint.__version__),
                digits=a.digits, per_n=[])
    t0 = time.time()
    for n in ns:
        o = run_n(n, a.digits, a.raw)
        summ["per_n"].append(compact(o))
        gs = [r["g"] for r in summ["per_n"] if r["g"] is not None]
        summ["min_g"] = min(gs) if gs else None
        summ["n_at_min_g"] = [r["n"] for r in summ["per_n"] if r["g"] == summ["min_g"]]
        summ["total_seconds"] = round(time.time() - t0, 1)
        summ["supported_all_tested"] = bool(gs) and all(g > 1e-9 for g in gs) and len(gs) == len(summ["per_n"])
        with open(a.summary, "w") as fh:
            json.dump(summ, fh, separators=(",", ":"))
        b = o.get("best_nonvertex")
        print("n=%d M=%d V*=%s nloc=%d nnv=%d g=%s best=%s t=%.1fs" % (
            n, o["M"], o["min_vertex_lam"][:14], o["ncand_grid"], o["n_nonvertex_orbits"], o.get("g_n"),
            None if b is None else (b["face"], b["th_pi"], b["ph_pi"], b["lam"][:12]), o["seconds"]), flush=True)


if __name__ == "__main__":
    main()
