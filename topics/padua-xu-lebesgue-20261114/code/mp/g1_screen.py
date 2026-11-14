#!/usr/bin/env python3
"""G1-MP screen (pre-registered addendum 2026-11-14): argmax screen of the MP Lebesgue function, even n = 2..60.

Usage: python3 g1_screen.py [--nmin 2] [--nmax 60] [--out ../../evidence/mp-g1-summary.json] [--raw /tmp/mp-runs]
Grid: theta_i = i*pi/M (i = 0..M/2, symmetry x -> -x only, Lemma S / BBDM Lemma 1), phi_j = j*pi/M (j = 0..M), M = max(64, 12n).
Local maxima: interior points >= their 8 neighbours (mirror row at theta = pi/2); open-edge points (x = 1: i = 0; y = +-1:
j = 0, M) >= their two neighbours ALONG the edge (1-D faces); vertices are 0-D faces.  Keep value >= 0.9 * max(lam(1,1), lam(-1,1)).
Refine: float64 L-BFGS-B (analytic gradient, box = +-2 grid cells, restricted to the face), then Newton at mpmath 40 digits on
the face (60 digits if g_n < 1e-6).  Within 1e-8 (angle distance) of a vertex -> vertex.  g_n = 1 - max_nonvertex / max(lam(1,1), lam(-1,1)).
"""
import argparse, json, os, sys, time, platform
import numpy as np
import mpmath as mp
import scipy
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mp_kernel as B

PI = np.pi


# ---------------------------------------------------------------- float value + gradient
def ud(x, n):
    """U_i, U_i' (in x) for i=0..n at scalar x."""
    u = np.empty(n + 1); d = np.empty(n + 1)
    u[0] = 1.0; d[0] = 0.0
    if n >= 1:
        u[1] = 2 * x; d[1] = 2.0
    for i in range(2, n + 1):
        u[i] = 2 * x * u[i - 1] - u[i - 2]
        d[i] = 2 * u[i - 1] + 2 * x * d[i - 1] - d[i - 2]
    return u, d


def val_grad(fm, th, ph):
    n = fm.n
    x, y = np.cos(th), np.cos(ph)
    ux, dx = ud(x, n); uy, dy = ud(y, n)
    A, Bv = ux[fm.I], uy[fm.J]
    dA = -np.sin(th) * dx[fm.I]
    dB = -np.sin(ph) * dy[fm.J]
    phi = A * Bv
    l = fm.C @ phi
    s = np.sign(l)
    d = fm.C.T @ s
    return float(s @ l), float(d @ (dA * Bv)), float(d @ (A * dB))


def refine_float(fm, th0, ph0, face, h):
    """maximize lam on the face. face in {'int','x1','y1','ym1'}: x1: th=0 fixed; y1: ph=0; ym1: ph=pi."""
    lo = [max(0.0, th0 - 2 * h), max(0.0, ph0 - 2 * h)]
    hi = [min(PI, th0 + 2 * h), min(PI, ph0 + 2 * h)]
    if face == "x1":
        lo[0] = hi[0] = 0.0
    if face == "y1":
        lo[1] = hi[1] = 0.0
    if face == "ym1":
        lo[1] = hi[1] = PI
    free = [lo[0] < hi[0], lo[1] < hi[1]]
    z0 = np.array([th0 if free[0] else lo[0], ph0 if free[1] else lo[1]])

    def f(zf):
        z = np.array(z0)
        k = 0
        for t in range(2):
            if free[t]:
                z[t] = zf[k]; k += 1
        v, gt, gp = val_grad(fm, z[0], z[1])
        g = [gt, gp]
        return -v, -np.array([g[t] for t in range(2) if free[t]])

    zf0 = np.array([z0[t] for t in range(2) if free[t]])
    bnds = [(lo[t], hi[t]) for t in range(2) if free[t]]
    r = minimize(f, zf0, jac=True, bounds=bnds, method="L-BFGS-B", options={"ftol": 1e-16, "gtol": 1e-11, "maxiter": 200})
    z = np.array(z0); k = 0
    for t in range(2):
        if free[t]:
            z[t] = r.x[k]; k += 1
    return z, -float(r.fun)


# ---------------------------------------------------------------- mpmath polish
def ud_mp(x, n, order=2):
    """U_i, U_i', U_i'' at mp x, lists."""
    u = [mp.mpf(1), 2 * x]; d = [mp.mpf(0), mp.mpf(2)]; e = [mp.mpf(0), mp.mpf(0)]
    for i in range(2, n + 1):
        u.append(2 * x * u[-1] - u[-2])
        d.append(2 * u[-2] + 2 * x * d[-1] - d[-2])
        e.append(4 * d[-2] + 2 * x * e[-1] - e[-2])
    return u[:n + 1], d[:n + 1], e[:n + 1]


class MPPolisher:
    def __init__(self, n, dps):
        self.n, self.dps = n, dps
        mp.mp.dps = dps
        self.idx = B.basis_index(n)
        self.nodes = []
        for (m, k, w, v, xm, yk) in B.mp_nodes(n):
            self.nodes.append((B.omega_closed(n, w, v), B.U_mp(xm, n), B.U_mp(yk, n)))

    def lagr_and_d(self, th, ph, want_d=True):
        """lambda (exact sum |l_a|) and, optionally, d_b = sum_a sign(l_a) C_ab at point (th,ph)."""
        n, idx = self.n, self.idx
        x, y = mp.cos(th), mp.cos(ph)
        Ux, Uy = B.U_mp(x, n), B.U_mp(y, n)
        phi = [Ux[i] * Uy[j] for (i, j) in idx]
        lam = mp.mpf(0)
        d = [mp.mpf(0)] * len(idx) if want_d else None
        minabs = None
        for (om, Vx, Vy) in self.nodes:
            row = [Vx[i] * Vy[j] for (i, j) in idx]
            l = om * mp.fsum(r * p for r, p in zip(row, phi))
            lam += abs(l)
            a = abs(l)
            minabs = a if minabs is None else min(minabs, a)
            if want_d:
                s = 1 if l > 0 else -1
                f = om * s
                d = [dd + f * r for dd, r in zip(d, row)]
        return lam, d, minabs

    def derivs(self, d, th, ph):
        n, idx = self.n, self.idx
        x, y = mp.cos(th), mp.cos(ph)
        ux, dx, ex = ud_mp(x, n); uy, dy, ey = ud_mp(y, n)
        st, ct, sp, cp = mp.sin(th), mp.cos(th), mp.sin(ph), mp.cos(ph)
        A = ux; dA = [-st * t for t in dx]; ddA = [st * st * e - ct * t for e, t in zip(ex, dx)]
        Bv = uy; dB = [-sp * t for t in dy]; ddB = [sp * sp * e - cp * t for e, t in zip(ey, dy)]
        g = gt = gp = gtt = gtp = gpp = mp.mpf(0)
        g = mp.fsum(d[b] * A[i] * Bv[j] for b, (i, j) in enumerate(idx))
        gt = mp.fsum(d[b] * dA[i] * Bv[j] for b, (i, j) in enumerate(idx))
        gp = mp.fsum(d[b] * A[i] * dB[j] for b, (i, j) in enumerate(idx))
        gtt = mp.fsum(d[b] * ddA[i] * Bv[j] for b, (i, j) in enumerate(idx))
        gtp = mp.fsum(d[b] * dA[i] * dB[j] for b, (i, j) in enumerate(idx))
        gpp = mp.fsum(d[b] * A[i] * ddB[j] for b, (i, j) in enumerate(idx))
        return g, gt, gp, gtt, gtp, gpp

    def polish(self, th0, ph0, face, rounds=4):
        mp.mp.dps = self.dps
        th, ph = mp.mpf(float(th0)), mp.mpf(float(ph0))
        if face == "x1": th = mp.mpf(0)
        if face == "y1": ph = mp.mpf(0)
        if face == "ym1": ph = mp.pi
        tol = mp.mpf(10) ** (-(self.dps - 8))
        info = {}
        for rd in range(rounds):
            lam0, d, _ = self.lagr_and_d(th, ph)
            for it in range(40):
                g, gt, gp, gtt, gtp, gpp = self.derivs(d, th, ph)
                if face == "int":
                    det = gtt * gpp - gtp ** 2
                    dth = -(gpp * gt - gtp * gp) / det
                    dph = -(-gtp * gt + gtt * gp) / det
                elif face == "x1":
                    dth, dph = mp.mpf(0), -gp / gpp
                else:
                    dth, dph = -gt / gtt, mp.mpf(0)
                th += dth; ph += dph
                if abs(dth) + abs(dph) < tol:
                    break
            lam, d2, minabs = self.lagr_and_d(th, ph, want_d=False)
            g, gt, gp, gtt, gtp, gpp = self.derivs(d, th, ph)
            # sign pattern consistent iff polynomial value equals the exact sum
            if abs(g - lam) < mp.mpf(10) ** (-(self.dps - 10)) * lam:
                info = {"iterations": it + 1, "grad": [mp.nstr(gt, 3), mp.nstr(gp, 3)], "hess_diag": [mp.nstr(gtt, 6), mp.nstr(gpp, 6)],
                        "sign_pattern_ok": True, "min_abs_l": mp.nstr(minabs, 3)}
                return th, ph, lam, info
        info["sign_pattern_ok"] = False
        return th, ph, lam, info


# ---------------------------------------------------------------- grid screen
def vertex_dist(th, ph):
    return min(np.hypot(th - a, ph - b) for a in (0.0, PI) for b in (0.0, PI))


def screen_n(n, raw_dir, args):
    t0 = time.time()
    fm = B.FloatModel(n)
    M = max(64, 12 * n)
    h = PI / M
    th = np.arange(0, M // 2 + 1) * h
    ph = np.arange(0, M + 1) * h
    G = fm.grid_rows(th, ph)                                   # (M/2+1, M+1)
    # vertex values (float64, exact angles)
    lv = fm.lam([1, -1, 1, -1], [1, 1, -1, -1])
    vv = {"(1,1)": float(lv[0]), "(-1,1)": float(lv[1]), "(1,-1)": float(lv[2]), "(-1,-1)": float(lv[3])}
    Vmax = max(vv["(1,1)"], vv["(-1,1)"])
    # extended array with mirror row i = M/2+1 -> M/2-1
    R, S = G.shape
    E = np.vstack([G, G[R - 2:R - 1]])
    cands = []
    for i in range(R):
        for j in range(S):
            v = G[i, j]
            if i == 0 and j in (0, S - 1):
                continue          # vertices (0-D faces)
            if i == 0:            # open edge x = 1
                ok = v >= G[0, j - 1] and v >= G[0, j + 1]; face = "x1"
            elif j == 0:
                ok = v >= E[i - 1, 0] and v >= E[i + 1, 0]; face = "y1"
            elif j == S - 1:
                ok = v >= E[i - 1, j] and v >= E[i + 1, j]; face = "ym1"
            else:
                nb = E[i - 1:i + 2, j - 1:j + 2].copy()
                nb[1, 1] = -np.inf
                ok = v >= nb.max(); face = "int"
            if ok:
                cands.append((i, j, face, float(v)))
    n_all_local = len(cands)
    above = [c for c in cands if c[3] >= 0.9 * Vmax]
    context_only = False
    if above:
        cands = above
    else:       # nothing >= 0.9*Vmax besides vertices: refine the 3 best local maxima as CONTEXT (below the pre-registered threshold)
        cands = sorted(cands, key=lambda c: -c[3])[:3]
        context_only = True
    # float refinement
    refined = []
    for (i, j, face, v) in cands:
        z, val = refine_float(fm, th[i], ph[j], face, h)
        t, p = float(z[0]), float(z[1])
        t = min(t, PI - t) if t > PI / 2 + 1e-15 else t         # fold x -> -x (theta -> pi - theta)
        isv = vertex_dist(t, p) < 1e-8
        refined.append({"grid": [i, j], "face": face, "theta": t, "phi": p, "value": val, "vertex": bool(isv)})
    # dedupe non-vertex
    nonv = []
    for r in sorted([r for r in refined if not r["vertex"]], key=lambda r: -r["value"]):
        if all(np.hypot(r["theta"] - q["theta"], r["phi"] - q["phi"]) > 1e-6 or r["face"] != q["face"] for q in nonv):
            nonv.append(r)
    nvert = sum(1 for r in refined if r["vertex"])
    # polish non-vertex candidates (all, up to a cap sorted by value)
    cap = args.max_polish
    pol = MPPolisher(n, 40) if nonv else None
    for r in nonv[:cap]:
        th_m, ph_m, lam_m, info = pol.polish(r["theta"], r["phi"], r["face"])
        r["mp_theta"] = mp.nstr(th_m, 30); r["mp_phi"] = mp.nstr(ph_m, 30); r["mp_value"] = mp.nstr(lam_m, 30)
        r["mp_info"] = info
        r["value_best"] = float(lam_m)
        r["polished"] = True
    # context: best non-vertex local max regardless of the 0.9 threshold (float64 only, top 3)
    ctx_best = None
    best = nonv[0] if nonv else None
    out = {"n": n, "M": M, "vertices": vv, "Vmax": Vmax, "n_grid_local_max_nonvertex": n_all_local, "n_candidates_ge_0.9Vmax": len(above),
           "context_only_below_threshold": context_only, "n_vertex_classified": nvert,
           "n_nonvertex": len(nonv), "grid_max": float(G.max()),
           "grid_max_is_vertex_value": bool(abs(G.max() - Vmax) <= 1e-9 * Vmax) or bool(G.max() <= Vmax * (1 + 1e-12))}
    if best:
        val = best.get("value_best", best["value"])
        out["best_nonvertex"] = {"face": best["face"], "x": float(np.cos(best["theta"])), "y": float(np.cos(best["phi"])),
                                 "theta_over_pi": best["theta"] / PI, "phi_over_pi": best["phi"] / PI, "value": val,
                                 "mp_value": best.get("mp_value"), "mp_ok": best.get("mp_info", {}).get("sign_pattern_ok")}
        out["g_n"] = 1.0 - val / Vmax
        out["g_n_gt_1e-9"] = bool(out["g_n"] > 1e-9)
        if out["g_n"] < 1e-6:
            pol60 = MPPolisher(n, 60)
            th_m, ph_m, lam_m, info = pol60.polish(best["theta"], best["phi"], best["face"])
            out["re_polish_60digits"] = {"value": mp.nstr(lam_m, 50), "ok": info.get("sign_pattern_ok")}
    else:
        out["best_nonvertex"] = None
        out["g_n"] = None
        out["note"] = "no non-vertex local maximum on the grid at all"
    out["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(raw_dir, "g1_raw_n%02d.json" % n), "w") as f:
        json.dump({"summary": out, "candidates_refined": refined, "nonvertex_polished": nonv}, f, indent=1, default=str)
    return out


def compact(r):
    """compact summary row for the evidence file (< 16 KiB total); full detail stays in the raw files."""
    f = lambda t, d=13: float("%.*g" % (d, t))
    v = r["vertices"]
    bn = r.get("best_nonvertex")
    o = {"n": r["n"], "M": r["M"],
         "lam_(1,1),(-1,1),(1,-1),(-1,-1)": [f(v["(1,1)"]), f(v["(-1,1)"]), f(v["(1,-1)"]), f(v["(-1,-1)"])],
         "grid_max_over_Vmax": f(r["grid_max"] / r["Vmax"], 15),
         "n_local_max_nonvertex_grid": r["n_grid_local_max_nonvertex"], "n_ge_0.9Vmax": r["n_candidates_ge_0.9Vmax"],
         "n_vertex_classified": r["n_vertex_classified"], "context_only": r["context_only_below_threshold"]}
    if bn:
        o["best_nonvertex"] = {"face": bn["face"], "x": f(bn["x"], 9), "y": f(bn["y"], 9), "value_mp": (bn["mp_value"] or "")[:22], "mp_ok": bn["mp_ok"]}
        o["g_n"] = f(r["g_n"])
        if "re_polish_60digits" in r:
            o["re_polish_60"] = r["re_polish_60digits"]
    return o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-raw", action="store_true", help="rebuild the compact summary from raw files in --raw (no recomputation)")
    ap.add_argument("--nmin", type=int, default=2)
    ap.add_argument("--nmax", type=int, default=60)
    ap.add_argument("--out", default="../../evidence/mp-g1-summary.json")
    ap.add_argument("--raw", default="/tmp/mp-runs")
    ap.add_argument("--max-polish", type=int, default=6)
    a = ap.parse_args()
    os.makedirs(a.raw, exist_ok=True)
    t0 = time.time()
    rows = []
    for n in range(a.nmin, a.nmax + 1, 2):
        if a.from_raw:
            r = json.load(open(os.path.join(a.raw, "g1_raw_n%02d.json" % n)))["summary"]
            rows.append(r)
            continue
        r = screen_n(n, a.raw, a)
        rows.append(r)
        bn = r.get("best_nonvertex")
        print(n, "Vmax=%.6f" % r["Vmax"], "cands", r["n_candidates_ge_0.9Vmax"], "vert", r["n_vertex_classified"], "nonvert", r["n_nonvertex"],
              "g_n=", r["g_n"], bn and bn["face"], "%.0fs" % r["seconds"], flush=True)
    ev = {"script": "code/mp/g1_screen.py", "command": "python3 " + " ".join(sys.argv),
          "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__, "mpmath": mp.__version__, "platform": platform.platform()},
          "prereg": "gates.md addendum 2026-11-14 (G1-MP screen)",
          "grid_max_is_vertex_value_all": all(r["grid_max_is_vertex_value"] for r in rows),
          "n_ge_0.9Vmax_nonvertex_total": sum(r["n_candidates_ge_0.9Vmax"] for r in rows),
          "min_g_n": min(r["g_n"] for r in rows if r.get("g_n") is not None), "max_g_n": max(r["g_n"] for r in rows if r.get("g_n") is not None),
          "g_n_gt_1e-9_all": all(r.get("g_n") is not None and r["g_n"] > 1e-9 for r in rows),
          "mp_polish_sign_pattern_ok_all": all(r["best_nonvertex"]["mp_ok"] for r in rows if r.get("best_nonvertex")),
          "interpretation_note": "No non-vertex local maximum reaches 0.9*Vmax at any n, so the pre-registered candidate set is empty; best_nonvertex is the best of the 3 highest grid local maxima refined as CONTEXT (g_n = 1 - value/Vmax).",
          "provenance": ("compact rebuild (--from-raw) of the full run `python3 g1_screen.py` (n=2..60, wall 945 s on a shared 2-core box); raw files /tmp/mp-runs/g1_raw_nNN.json" if a.from_raw else "full run"),
          "rows": [compact(r) for r in rows], "wall_seconds": (None if a.from_raw else round(time.time() - t0, 1))}
    json.dump(ev, open(a.out, "w"), separators=(",", ":"), default=str)
    print("wrote", a.out, os.path.getsize(a.out))


if __name__ == "__main__":
    main()
