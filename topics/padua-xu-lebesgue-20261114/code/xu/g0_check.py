#!/usr/bin/env python3
"""G0 checks for X1 (Xu interpolation), gates.md G0.  Writes evidence/xu-g0.json.

Usage:  python3 code/xu/g0_check.py [--nmax 12] [--npts 200] [--out evidence/xu-g0.json] [--skip-lambda]
Checks per n = 1..nmax (both parities):
  C1 cardinality = dimension, det enclosure excludes 0 (path A, 256 bit arb)
  C2 l_xi(eta)=delta: path A (V*V^-1 enclosure contains identity) and path B (1e-40, mpmath dps 60)
  C3 path A vs path B at all nodes and at npts seeded random points (+4 vertices) to 1e-30
  C4 path B orthonormal-sum form vs compact D_n form (first 20 random points)
  C5 Lemma S invariances (path B, mpmath 30 digits)
Global:
  C6 Lambda vs BCDMV Table 7 (n=34,48,62,76 -> 10,12,13,14): vertex value (closed form + generic path B at n=34)
     and uniform-grid maximum from the float64 screen kernel.
"""
import sys, os, json, time, argparse, platform
import numpy as np
import mpmath as mp
import flint
from flint import arb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import xu_kernel as K
from xu_exact import XuExact

SEED = 20261114


def rnd_points(npts):
    rng = np.random.default_rng(SEED)
    return [(float(a), float(b)) for a, b in rng.uniform(0, np.pi, size=(npts, 2))]


def group_elems():
    # (swap, flipx, flipy): apply flips first, then swap
    out = []
    for sw in (0, 1):
        for fx in (0, 1):
            for fy in (0, 1):
                out.append((sw, fx, fy))
    return out


def apply_g(g, th, ph, pi):
    sw, fx, fy = g
    a = pi - th if fx else th
    b = pi - ph if fy else ph
    return (b, a) if sw else (a, b)


def check_n(n, pts, prec=256):
    res = {"n": n}
    t0 = time.time()
    mp.mp.dps = 60
    A = XuExact(n, prec)
    res["N"] = A.N
    res["dim"] = A.dim
    res["cardinality_eq_dim"] = bool(A.square)
    res["det_excludes_0"] = bool(A.det_nonzero)
    res["log10_abs_det_mid"] = round(float(mp.log10(abs(mp.mpf(A.det.mid().str(40, radius=False)))))) if A.det_nonzero else None
    res["pass_C1"] = bool(A.square and A.det_nonzero)
    ok, mr = A.interpolation_check()
    res["A_VVinv_contains_identity"] = bool(ok)
    res["A_VVinv_max_radius"] = float("%.3g" % mr)
    res["A_Vinv_max_width"] = float("%.3g" % A.inverse_max_width())
    # path B at nodes
    nodes = K.nodes(n)
    worstB_delta = mp.mpf(0)
    worstAB_nodes = mp.mpf(0)
    for idx, (r, s) in enumerate(nodes):
        th = (mp.pi * r / n, mp.pi * s / n)
        ell = K.ell_all(n, th, "D")
        for jdx, nd in enumerate(nodes):
            dlt = 1 if nd == (r, s) else 0
            worstB_delta = max(worstB_delta, abs(ell[nd] - dlt))
    res["B_max_delta_error_at_nodes"] = float("%.3g" % worstB_delta)
    res["pass_C2_A"] = bool(ok and mr < 1e-30)
    res["pass_C2_B"] = bool(worstB_delta <= mp.mpf(10) ** -40)
    # A vs B at random points
    maxabs = mp.mpf(0)
    maxrel = mp.mpf(0)
    maxlamrel = mp.mpf(0)
    maxwidthA = 0.0
    maxD_orth = mp.mpf(0)
    for ip, (a, b) in enumerate(pts):
        thA = (arb(a), arb(b))
        ellA = A.ell(thA)
        lamA = sum((abs(v) for v in ellA), arb(0))
        thB = (mp.mpf(a), mp.mpf(b))
        ellB = K.ell_all(n, thB, "D")
        lamB = mp.mpf(0)
        for (nd, v) in zip(nodes, ellA):
            mid = mp.mpf(v.mid().str(70, radius=False))
            maxwidthA = max(maxwidthA, float(v.rad()))
            d = abs(mid - ellB[nd])
            maxabs = max(maxabs, d)
            if abs(mid) > 1e-3:
                maxrel = max(maxrel, d / abs(mid))
            lamB += abs(ellB[nd])
        lamAm = mp.mpf(lamA.mid().str(70, radius=False))
        maxlamrel = max(maxlamrel, abs(lamAm - lamB) / lamAm)
        if ip < 20:
            ellO = K.ell_all(n, thB, "orth")
            for nd in nodes:
                maxD_orth = max(maxD_orth, abs(ellO[nd] - ellB[nd]))
    res["AB_random_points"] = len(pts)
    res["AB_max_abs_diff_ell"] = float("%.3g" % maxabs)
    res["AB_max_rel_diff_ell(|l|>1e-3)"] = float("%.3g" % maxrel)
    res["AB_max_rel_diff_lambda"] = float("%.3g" % maxlamrel)
    res["A_max_enclosure_radius_ell"] = float("%.3g" % maxwidthA)
    res["pass_C3"] = bool(maxabs < 1e-30 and maxrel < 1e-30 and maxlamrel < 1e-30 and maxwidthA < 1e-30)
    res["orth_vs_D_max_abs_diff(20pts)"] = float("%.3g" % maxD_orth)
    res["pass_C4"] = bool(maxD_orth < 1e-30)
    # vertices: A, B generic, B closed form
    vv = {}
    vmax = mp.mpf(0)
    for v in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        th = (mp.pi * v[0], mp.pi * v[1])
        lb = K.lebesgue(n, th, "D")
        lc = K.vertex_value(n, v)
        la = A.lam((arb.pi() * v[0], arb.pi() * v[1]))
        lam_mid = mp.mpf(la.mid().str(70, radius=False))
        vmax = max(vmax, abs(lb - lc), abs(lb - lam_mid))
        vv["%d%d" % v] = mp.nstr(lb, 20)
    res["vertex_lambda(key=flags for angle pi in x,y)"] = vv if n < 4 else {k: vv[k] for k in ("00", "01")}
    res["vertex_A_B_closedform_max_diff"] = float("%.3g" % vmax)
    res["pass_C3v"] = bool(vmax < 1e-30)
    # Lemma S
    mp.mp.dps = 30
    prs = rnd_points(6)
    dev = {}
    for g in group_elems():
        mx = mp.mpf(0)
        for (a, b) in prs:
            th0 = (mp.mpf(a), mp.mpf(b))
            th1 = apply_g(g, th0[0], th0[1], mp.pi)
            mx = max(mx, abs(K.lebesgue(n, th0) - K.lebesgue(n, th1)))
        dev["swap%d_flipx%d_flipy%d" % g] = float(mx)
    # node-set invariance (index form)
    nodeset = set(nodes)
    def img(g, rs):
        sw, fx, fy = g
        r, s = rs
        r2 = n - r if fx else r
        s2 = n - s if fy else s
        return (s2, r2) if sw else (r2, s2)
    inv_nodes = {"swap%d_flipx%d_flipy%d" % g: all(img(g, x) in nodeset for x in nodes) for g in group_elems()}
    if n % 2 == 0:
        expected = set(dev.keys())
    else:
        expected = {"swap0_flipx0_flipy0", "swap1_flipx0_flipy0", "swap0_flipx1_flipy1", "swap1_flipx1_flipy1"}
    inv_ok = all(dev[k] < 1e-25 for k in expected)
    # for odd n the remaining elements are NOT symmetries (report, informational; n=1 degenerate possible)
    non_sym_observed = {k: dev[k] > 1e-6 for k in dev if k not in expected}
    # keys swap{0,1}_flipx{0,1}_flipy{0,1} abbreviated to s,x,y bits, e.g. "101" = swap, no flipx, flipy
    short = lambda k: k.replace("swap", "").replace("_flipx", "").replace("_flipy", "")
    res["LemmaS_max_dev"] = {short(k): float("%.2g" % v) for k, v in dev.items()}
    res["LemmaS_node_set_invariant_elements"] = sorted(short(k) for k, v in inv_nodes.items() if v)
    res["LemmaS_other_elements_noninvariant(dev>1e-6)"] = bool(all(non_sym_observed.values())) if non_sym_observed else None
    res["pass_C5"] = bool(inv_ok and all(inv_nodes[k] for k in expected))
    res["seconds"] = round(time.time() - t0, 1)
    res["PASS"] = bool(res["pass_C1"] and res["pass_C2_A"] and res["pass_C2_B"] and res["pass_C3"] and res["pass_C3v"]
                       and res["pass_C4"] and res["pass_C5"])
    return res


def lambda_published_check():
    pub = {34: 10, 48: 12, 62: 13, 76: 14}
    out = {}
    mp.mp.dps = 30
    for n, p in pub.items():
        t0 = time.time()
        vv = {"%d%d" % v: K.vertex_value(n, v) for v in [(0, 0), (0, 1), (1, 0), (1, 1)]}
        lam_v = vv["00"]
        # grid maximum with the float screen kernel on quadrant (n even: full dihedral symmetry)
        M = 12 * n
        X = K.XuFloat(n)
        h = np.arange(0, M // 2 + 1) * np.pi / M
        G = X.grid(h, h)
        i, j = np.unravel_index(np.argmax(G), G.shape)
        d = {
            "published_rounded": p,
            "vertex_value_closed_form": mp.nstr(lam_v, 15),
            "round_vertex": int(mp.nint(lam_v)),
            "four_vertices_equal": bool(max(abs(vv[k] - lam_v) for k in vv) < 1e-25),
            "grid_M": M,
            "grid_max_float64": float(G[i, j]),
            "grid_argmax_angles/pi": [float(h[i] / np.pi), float(h[j] / np.pi)],
            "grid_max_minus_vertex": float(G[i, j] - float(lam_v)),
            "round_grid_max": int(round(G[i, j])),
            "seconds": round(time.time() - t0, 1),
        }
        if n == 34:
            gen = K.lebesgue(n, (mp.mpf(0), mp.mpf(0)), "D")
            d["generic_pathB_vertex_n34_diff_vs_closed_form"] = float(abs(gen - lam_v))
        d["PASS"] = bool(d["round_vertex"] == p and d["round_grid_max"] == p and d["four_vertices_equal"]
                         and d["grid_max_minus_vertex"] <= 1e-9)
        out[str(n)] = d
    # reader reproduction table (reader's own script, not a published number)
    reader = {2: 2.0000, 4: 3.4142, 6: 4.4285, 8: 5.2304, 10: 5.8992, 20: 8.2356, 34: 10.2881, 48: 11.7445,
              62: 12.8877, 76: 13.8351, 100: 15.1653}
    rd = {str(n): bool(abs(float(K.vertex_value(n, (0, 0))) - v) < 5.1e-5) for n, v in reader.items()}
    out["reader_table_consistency(4 decimals)"] = rd
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=12)
    ap.add_argument("--npts", type=int, default=200)
    ap.add_argument("--out", default=os.path.join(HERE, "..", "..", "evidence", "xu-g0.json"))
    ap.add_argument("--skip-lambda", action="store_true")
    a = ap.parse_args()
    pts = rnd_points(a.npts)
    ev = {
        "LemmaS_note": "even n: all 8 elements invariant expected; odd n: expected invariant = swap, central reflection (keys 000,100,011,111 as swap/flipx/flipy bits); other elements reported as noninvariant",
        "what": "G0 checks, X1 Xu interpolation (gates.md G0)",
        "seed": SEED,
        "command": " ".join(sys.argv),
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "mpmath": mp.__version__,
                     "python-flint": flint.__version__, "arb_prec_bits": 256, "mp_dps": 60},
        "random_points": "np.random.default_rng(%d).uniform(0,pi,(%d,2)) angles (theta,phi), x=(cos th, cos phi)" % (SEED, a.npts),
        "per_n": [],
    }
    t0 = time.time()
    for n in range(1, a.nmax + 1):
        r = check_n(n, pts)
        ev["per_n"].append(r)
        print("n=%d N=%d PASS=%s (%.1fs)" % (n, r["N"], r["PASS"], r["seconds"]), flush=True)
    ev["per_n_PASS_all"] = all(r["PASS"] for r in ev["per_n"])
    ev["per_check_PASS"] = {k: all(r[k] for r in ev["per_n"]) for k in
                            ["pass_C1", "pass_C2_A", "pass_C2_B", "pass_C3", "pass_C3v", "pass_C4", "pass_C5"]}
    if not a.skip_lambda:
        ev["lambda_vs_published"] = lambda_published_check()
        ev["pass_C6_lambda"] = all(v["PASS"] for k, v in ev["lambda_vs_published"].items() if k.isdigit()) and \
            all(ev["lambda_vs_published"]["reader_table_consistency(4 decimals)"].values())
    ev["G0_PASS"] = bool(ev["per_n_PASS_all"] and ev.get("pass_C6_lambda", False))
    ev["total_seconds"] = round(time.time() - t0, 1)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    s = json.dumps(ev, indent=None, separators=(",", ":"))
    open(a.out, "w").write(s)
    print("G0_PASS =", ev["G0_PASS"], "bytes", len(s), "->", a.out)


if __name__ == "__main__":
    main()
