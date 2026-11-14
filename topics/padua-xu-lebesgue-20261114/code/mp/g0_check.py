#!/usr/bin/env python3
"""G0 checks for X2 (Morrow-Patterson points), even n = 2..12 plus published Lebesgue constants.

Usage:  python3 g0_check.py --out ../../evidence/mp-g0.json [--nmax 12] [--seed 20261114] [--skip-published]
Path A = mp_exact.py (python-flint arb Vandermonde), Path B = mp_kernel.py (mpmath kernel formula).
"""
import argparse, json, sys, time, platform, os
import numpy as np
import mpmath as mp
import flint, scipy
from flint import arb, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mp_exact as A
import mp_kernel as B

mp.mp.dps = 60
TOL_REL = 1e-30


def ball_dist(a, b):
    """distance from mpf b to arb ball a (0 if inside), as float."""
    mid = mp.mpf(a.mid().str(80, radius=False)) if False else mp.mpf(a.mid().str(100, radius=False).split('+/-')[0])
    r = mp.mpf(float(a.rad()))
    d = abs(mid - b) - r
    return float(max(d, 0))


def check_n(n, pts, prec0=256):
    res = {"n": n}
    for prec in (prec0, 384, 512, 768):
        ctx.prec = prec
        ex = A.ExactMP(n, prec, want_inverse=True)
        if ex.det_nonzero and ex.Vinv is not None:
            break
    N = ex.N
    res["N"] = N
    res["dim_Pi_n"] = (n + 1) * (n + 2) // 2
    res["cardinality_ok"] = (N == res["dim_Pi_n"] and len(A.nodes_ints(n)) == N)
    # distinct nodes
    xs = [(float(x), float(y)) for x, y in zip(ex.xs, ex.ys)]
    res["nodes_distinct"] = len(set((round(a, 12), round(b, 12)) for a, b in xs)) == N
    res["prec_bits"] = ex.prec
    res["det_enclosure"] = ex.det.str(8)
    res["det_excludes_0"] = bool(ex.det_nonzero)
    # l(eta)=delta : V*Vinv contains identity, widths small
    I = ex.V * ex.Vinv
    ok_id, wmax = True, 0.0
    for a in range(N):
        for b in range(N):
            t = I[a, b]
            if not t.contains(1 if a == b else 0):
                ok_id = False
            wmax = max(wmax, float(t.rad()) * 2)
    res["A_delta_contained"] = ok_id
    res["A_delta_max_width"] = wmax
    # Path B: nodes, omega sum-vs-closed, l(eta)=delta
    mp.mp.dps = 60
    nodes = B.mp_nodes(n)
    om_s = [B.omega_sum(n, nd[4], nd[5]) for nd in nodes]
    om_c = [B.omega_closed(n, nd[2], nd[3]) for nd in nodes]
    res["B_omega_sum_vs_closed_maxrel"] = float(max(abs(a - b) / abs(a) for a, b in zip(om_s, om_c)))
    # Beberok closed form vs sum form of K(1,1)
    kr = 0
    for nd in nodes:
        ks = B.kernel_sum_corner(n, nd[2], nd[3])
        kc = B.kernel_corner_closed(n, nd[0], nd[2], nd[3])
        kr = max(kr, abs(ks - kc) / max(abs(ks), mp.mpf(10) ** -20))
    res["B_beberok_closed_vs_sum_maxrel"] = float(kr)
    dmax = 0
    for a, nd in enumerate(nodes):
        ls = B.lagrange_mp(n, nd[4], nd[5], nodes, "closed")
        for b, t in enumerate(ls):
            dmax = max(dmax, abs(t - (1 if a == b else 0)))
    res["B_delta_max_dev"] = float(dmax)
    # Path A vs B at nodes and random points
    P = [(ex.xs[a], ex.ys[a]) for a in range(N)]
    worst_pt = 0.0; worst_lam = 0.0; worst_enc = 0.0
    allp = [("node", p) for p in P]
    for (x, y) in pts:
        allp.append(("rand", (arb(float(x)), arb(float(y)))))
    sym_ok = True
    A_w = 0.0
    for kind, (xa, ya) in allp:
        la = ex.lagrange(xa, ya)
        xb = mp.mpf(xa.mid().str(120, radius=False).split('+/-')[0]) if kind == "node" else mp.mpf(float(xa))
        yb = mp.mpf(ya.mid().str(120, radius=False).split('+/-')[0]) if kind == "node" else mp.mpf(float(ya))
        lb = B.lagrange_mp(n, xb, yb, nodes, "sum")
        # node coordinates: B recomputes cos at 60 digits, A mid has 76+ digits; compare at 1e-30 level
        scale = max(abs(t) for t in lb)
        scale = max(scale, mp.mpf(1))
        diff = max(abs(mp.mpf(la[a].mid().str(100, radius=False).split('+/-')[0]) - lb[a]) for a in range(N))
        worst_pt = max(worst_pt, float(diff / scale))
        lamA = A.lam_from(la)
        lamB = mp.fsum(abs(t) for t in lb)
        worst_lam = max(worst_lam, float(abs(mp.mpf(lamA.mid().str(100, radius=False).split('+/-')[0]) - lamB) / lamB))
        A_w = max(A_w, max(float(t.rad()) for t in la))
    res["AB_max_rel_lagrange_vs_max|l|"] = worst_pt
    res["AB_max_rel_lambda"] = worst_lam
    res["A_max_enclosure_radius"] = A_w
    res["n_points_compared"] = len(allp)
    # symmetry lambda(x,y)=lambda(-x,y) on the random points (Path A enclosures overlap)
    sym_dev = 0.0
    for (x, y) in pts[:50]:
        l1 = A.lam_from(ex.lagrange(arb(float(x)), arb(float(y))))
        l2 = A.lam_from(ex.lagrange(arb(-float(x)), arb(float(y))))
        sym_dev = max(sym_dev, float(abs(l1.mid() - l2.mid())))
        if not l1.overlaps(l2):
            sym_ok = False
    res["sym_x_mirror_overlap_ok_50pts"] = sym_ok
    res["sym_x_mirror_max_dev"] = sym_dev
    # vertices
    ctx.prec = ex.prec
    vl = [A.lam_from(ex.lagrange(arb(sx), arb(sy))) for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1))]
    res["lam_vertices_A_(1,1),(-1,1),(1,-1),(-1,-1)"] = [t.str(20, radius=False) for t in vl]
    lcl = B.lam_corner_closed_mp(n)
    res["B_closed_form_lam(1,1)"] = mp.nstr(lcl, 20)
    res["A_vs_Bclosed_lam(1,1)_absdiff"] = float(abs(mp.mpf(vl[0].mid().str(100, radius=False).split('+/-')[0]) - lcl))
    res["PASS"] = bool(res["cardinality_ok"] and res["nodes_distinct"] and res["det_excludes_0"] and ok_id and wmax < 1e-30
                       and res["B_delta_max_dev"] < 1e-40 and res["AB_max_rel_lagrange_vs_max|l|"] < TOL_REL
                       and res["AB_max_rel_lambda"] < TOL_REL and A_w < 1e-30 and sym_ok
                       and res["B_omega_sum_vs_closed_maxrel"] < 1e-45 and res["B_beberok_closed_vs_sum_maxrel"] < 1e-40)
    return res


def published(deg_list, M_factor=12):
    """Lambda_MP and Lambda_EMP for the CDMV 2005 Table 4 degrees (float64 grid + local refinement)."""
    from scipy.optimize import minimize
    PUB_MP = {34: 649, 48: 1264, 62: 2082, 76: 3102}
    PUB_EMP = {34: 237, 48: 456, 62: 746, 76: 1106}
    out = []
    for n in deg_list:
        t0 = time.time()
        fm = B.FloatModel(n)
        M = max(64, M_factor * n)
        th = np.arange(0, M // 2 + 1) * np.pi / M
        ph = np.arange(0, M + 1) * np.pi / M
        G = fm.grid_rows(th, ph)
        i, j = np.unravel_index(np.argmax(G), G.shape)
        lam11 = float(fm.lam([1.0], [1.0])[0])
        r = {"n": n, "MP_grid_max": float(G.max()), "MP_grid_argmax_angles": [int(i), int(j), M],
             "MP_lam(1,1)": lam11, "MP_Lambda": max(lam11, float(G.max())), "MP_published": PUB_MP[n]}
        r["MP_rounded"] = int(round(r["MP_Lambda"]))
        r["MP_match"] = r["MP_rounded"] == PUB_MP[n]
        al, be = float(np.cos(np.pi / (n + 2))), float(np.cos(np.pi / (n + 3)))
        GE = fm.grid_rows(th, ph, al, be)
        i, j = np.unravel_index(np.argmax(GE), GE.shape)
        lam_e = lambda z: -fm.lam([al * np.cos(z[0])], [be * np.cos(z[1])])[0]
        best = minimize(lam_e, [th[i], ph[j]], bounds=[(0, np.pi), (0, np.pi)], method="L-BFGS-B", options={"ftol": 1e-15, "gtol": 1e-10})
        cand = max(float(GE.max()), -float(best.fun))
        corner = float(fm.lam([al], [be])[0])
        r.update({"EMP_grid_max": float(GE.max()), "EMP_refined_max": cand, "EMP_argmax_angles_refined": [float(best.x[0]), float(best.x[1])],
                  "EMP_vertex_(1,1)_value": corner, "EMP_Lambda": max(cand, corner), "EMP_published": PUB_EMP[n]})
        r["EMP_rounded"] = int(round(r["EMP_Lambda"]))
        r["EMP_match"] = r["EMP_rounded"] == PUB_EMP[n]
        # x-mirror symmetry on random points (float)
        rng = np.random.default_rng(20261114)
        q = rng.uniform(-1, 1, (200, 2))
        r["sym_x_mirror_max_rel_dev_200pts"] = float(np.max(np.abs(fm.lam(q[:, 0], q[:, 1]) - fm.lam(-q[:, 0], q[:, 1])) / fm.lam(q[:, 0], q[:, 1])))
        r["seconds"] = round(time.time() - t0, 1)
        out.append(r)
        print("published n=%d MP %.3f (%d) EMP %.3f (%d) %.0fs" % (n, r["MP_Lambda"], PUB_MP[n], r["EMP_Lambda"], PUB_EMP[n], r["seconds"]), flush=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="../../evidence/mp-g0.json")
    ap.add_argument("--nmax", type=int, default=12)
    ap.add_argument("--seed", type=int, default=20261114)
    ap.add_argument("--skip-published", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    rng = np.random.default_rng(a.seed)
    pts = rng.uniform(-1, 1, (200, 2))
    per_n = []
    for n in range(2, a.nmax + 1, 2):
        r = check_n(n, [tuple(p) for p in pts])
        per_n.append(r)
        print("n=%d PASS=%s" % (n, r["PASS"]), flush=True)
    pub = [] if a.skip_published else published([34, 48, 62, 76])
    ev = {
        "script": "code/mp/g0_check.py", "command": "python3 " + " ".join(sys.argv),
        "seed": a.seed, "rng": "numpy.random.default_rng(seed).uniform(-1,1,(200,2))",
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
                     "mpmath": mp.__version__, "python-flint": flint.__version__, "platform": platform.platform()},
        "tolerances": {"AB_relative": TOL_REL, "path_B_delta": 1e-40, "arb_width": 1e-30},
        "comparison_definition": "AB_max_rel_lagrange_vs_max|l| = max_a |l_a^A(mid) - l_a^B| / max(1, max_a |l_a^B|) over all nodes and 200 random points; AB_max_rel_lambda relative on lambda",
        "per_n": per_n,
        "published": pub,
        "G0_per_n_all_PASS": all(r["PASS"] for r in per_n),
        "G0_published_MP_all_match": (all(r["MP_match"] for r in pub) if pub else None),
        "G0_published_EMP_all_match": (all(r["EMP_match"] for r in pub) if pub else None),
        "wall_seconds": round(time.time() - t0, 1),
    }
    s = json.dumps(ev, indent=1)
    open(a.out, "w").write(s)
    print("wrote", a.out, len(s), "bytes")


if __name__ == "__main__":
    main()
