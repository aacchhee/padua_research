"""Independent auditor sanity implementation (Claude Opus 5.5, audit01/A).

MEASURED sanity only: high-precision floating arithmetic (mpmath), not a proof.
Route: Padua points are built from their definition; Lagrange cardinals are obtained
by directly solving the interpolation system in the product-Chebyshev basis
T_a(x)T_b(y), a+b<=n (mpmath LU at high precision). No PD-T101 kernel formula is used
to build them. The formula is only *compared* against the direct solve.

Nothing here writes into the repository; outputs go to the --out directory.
"""
import argparse
import json
import math
import sys
import time
from fractions import Fraction as F
from math import comb

import mpmath as mp
import numpy as np


# ---------------------------------------------------------------- nodes / basis
def padua_nodes(n):
    """(j,k), 0<=j<=n, 0<=k<=n+1, j+k even; x=cos(j pi/n), y=cos(k pi/(n+1))."""
    out = []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                out.append((j, k))
    return out


def modes(n):
    return [(a, b) for a in range(n + 1) for b in range(n + 1 - a)]


def cheb_values_mp(x, deg):
    """T_0..T_deg at x by the three-term recurrence (no trig identity)."""
    t = [mp.mpf(1), x]
    for _ in range(2, deg + 1):
        t.append(2 * x * t[-1] - t[-2])
    return t[:deg + 1]


def direct_cardinals(n):
    """Return nodes, node coordinates, modes, C with L_l = sum_m C[m][l] q_m."""
    nodes = padua_nodes(n)
    md = modes(n)
    assert len(nodes) == len(md) == (n + 1) * (n + 2) // 2
    xs = [mp.cos(j * mp.pi / n) for j, k in nodes]
    ys = [mp.cos(k * mp.pi / (n + 1)) for j, k in nodes]
    V = mp.matrix(len(nodes), len(md))
    for i in range(len(nodes)):
        tx = cheb_values_mp(xs[i], n)
        ty = cheb_values_mp(ys[i], n)
        for m, (a, b) in enumerate(md):
            V[i, m] = tx[a] * ty[b]
    C = mp.inverse(V)  # C[m, l]: column l is cardinal l's Chebyshev coefficients
    # residual of V*C = I
    R = V * C
    res = max(abs(R[i, j] - (1 if i == j else 0)) for i in range(R.rows) for j in range(R.cols))
    return nodes, xs, ys, md, C, res


def formula_coefficients(n, nodes, md):
    """PD-T101 / BDMVX corrected kernel, only for comparison."""
    Cf = mp.matrix(len(md), len(nodes))
    for l, (j, k) in enumerate(nodes):
        w = mp.mpf(2) / (n * (n + 1))
        if j in (0, n):
            w /= 2
        if k in (0, n + 1):
            w /= 2
        for m, (a, b) in enumerate(md):
            h = (1 if a == 0 else 2) * (1 if b == 0 else 2)
            if (a, b) == (n, 0):
                h = 1
            Cf[m, l] = w * h * mp.cos(a * j * mp.pi / n) * mp.cos(b * k * mp.pi / (n + 1))
    return Cf


def wrong_formula_variants(n, nodes, md):
    """Plausible convention errors, to show the comparison is discriminating."""
    out = {}
    for name in ("exceptional_mode_in_y", "no_exceptional_mode", "no_endpoint_halving"):
        Cf = mp.matrix(len(md), len(nodes))
        for l, (j, k) in enumerate(nodes):
            w = mp.mpf(2) / (n * (n + 1))
            if name != "no_endpoint_halving":
                if j in (0, n):
                    w /= 2
                if k in (0, n + 1):
                    w /= 2
            for m, (a, b) in enumerate(md):
                h = (1 if a == 0 else 2) * (1 if b == 0 else 2)
                if name == "exceptional_mode_in_y" and (a, b) == (0, n):
                    h = 1
                if name in ("no_endpoint_halving",) and (a, b) == (n, 0):
                    h = 1
                Cf[m, l] = w * h * mp.cos(a * j * mp.pi / n) * mp.cos(b * k * mp.pi / (n + 1))
        out[name] = Cf
    return out


# ------------------------------------------------------------- power basis
def cheb_int_coeffs(deg):
    """Integer power coefficients of T_0..T_deg, via sympy (independent of the checker)."""
    import sympy as sp
    x = sp.Symbol("x")
    out = []
    for a in range(deg + 1):
        p = sp.Poly(sp.chebyshevt(a, x), x)
        v = [0] * (deg + 1)
        for (e,), c in p.terms():
            v[e] = int(c)
        out.append(v)
    return out


def power_coefficients(n, md, C):
    """P[l][i][j]: coefficient of x^i y^j in cardinal l (mp)."""
    t = cheb_int_coeffs(n)
    N = C.cols
    P = []
    for l in range(N):
        M = [[mp.mpf(0)] * (n + 1) for _ in range(n + 1)]
        for m, (a, b) in enumerate(md):
            c = C[m, l]
            if c == 0:
                continue
            for i in range(a + 1):
                if t[a][i] == 0:
                    continue
                ci = c * t[a][i]
                for j in range(b + 1):
                    if t[b][j]:
                        M[i][j] += ci * t[b][j]
        P.append(M)
    return P


def eval_power(P, x, y):
    n = len(P) - 1
    xp = [x ** i for i in range(n + 1)]
    yp = [y ** j for j in range(n + 1)]
    return sum(P[i][j] * xp[i] * yp[j] for i in range(n + 1) for j in range(n + 1))


def eval_cheb(C, md, l, x, y, n):
    tx = cheb_values_mp(x, n)
    ty = cheb_values_mp(y, n)
    return sum(C[m, l] * tx[a] * ty[b] for m, (a, b) in enumerate(md))


def lebesgue_mp(C, md, n, x, y):
    tx = cheb_values_mp(x, n)
    ty = cheb_values_mp(y, n)
    q = [tx[a] * ty[b] for (a, b) in md]
    tot = mp.mpf(0)
    for l in range(C.cols):
        tot += abs(mp.fsum(C[m, l] * q[m] for m in range(len(md))))
    return tot


# -------------------------------------------- PD-T101 corner identity (3rd route)
def corner_formula(n, cx, cy):
    """lambda_n(c)=sum w_jk |D_n(th_c+th_j, ph_c+ph_k) - T_n(cos th_c)(-1)^j|."""
    thc = mp.mpf(0) if cx == 1 else mp.pi
    phc = mp.mpf(0) if cy == 1 else mp.pi

    def U(m, t):
        s = mp.sin(t)
        if abs(s) < mp.mpf(10) ** (-mp.mp.dps + 10):
            # continuous extension sin(mt)/sin(t) at t in pi Z: m * cos(m t)/cos(t)
            return m * mp.cos(m * t) / mp.cos(t)
        return mp.sin(m * t) / s

    tot = mp.mpf(0)
    for j, k in padua_nodes(n):
        w = mp.mpf(2) / (n * (n + 1))
        if j in (0, n):
            w /= 2
        if k in (0, n + 1):
            w /= 2
        u = thc + j * mp.pi / n
        v = phc + k * mp.pi / (n + 1)
        S = (u + v) / 2
        T = (v - u) / 2
        D = U(n + 1, S) * U(n + 1, T) + U(n, S) * U(n, T)
        tot += w * abs(D - mp.cos(n * thc) * (-1) ** j)
    return tot


# ---------------------------------------------------------- leaf Bernstein replay
def box_of_path(path):
    """Independent geometry: depth d splits x if d even, y if d odd; '0'=lower half."""
    box = [[F(-1), F(1)], [F(-1), F(1)]]
    for d, ch in enumerate(path):
        ax = d % 2
        lo, hi = box[ax]
        mid = (lo + hi) / 2
        box[ax] = [lo, mid] if ch == "0" else [mid, hi]
    return box


def interval_power_to_bernstein(n, lo, hi):
    """Exact matrix M[i][a]: Bernstein coefficient i on [lo,hi] of x^a."""
    h = hi - lo
    M = [[F(0)] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        # x^a = sum_r C(a,r) lo^(a-r) h^r u^r ; u^r = sum_{i>=r} C(i,r)/C(n,r) B_i
        for r in range(a + 1):
            coef = comb(a, r) * lo ** (a - r) * h ** r
            if coef == 0:
                continue
            for i in range(r, n + 1):
                M[i][a] += coef * F(comb(i, r), comb(n, r))
    return M


def to_int_matrix(M):
    den = 1
    for row in M:
        for q in row:
            den = den * q.denominator // math.gcd(den, q.denominator)
    return np.array([[int(q * den) for q in row] for row in M], dtype=object), den


def leaf_coefficient_sums(n, Pint, E, box):
    """Return list of approximate sum_l |b_{l,ik}| (as Fractions scaled) for all (i,k)."""
    Mx, dx = to_int_matrix(interval_power_to_bernstein(n, *box[0]))
    My, dy = to_int_matrix(interval_power_to_bernstein(n, *box[1]))
    N = len(Pint)
    # B_l = Mx P_l My^T
    stack = np.concatenate(Pint, axis=1)  # (n+1) x (N*(n+1))
    left = Mx.dot(stack)                  # (n+1) x (N*(n+1))
    sums = np.zeros((n + 1, n + 1), dtype=object)
    sums[:, :] = 0
    MyT = My.T
    for l in range(N):
        Bl = left[:, l * (n + 1):(l + 1) * (n + 1)].dot(MyT)
        sums = sums + np.vectorize(abs, otypes=[object])(Bl)
    scale = dx * dy * (1 << E)
    return sums, scale


# ---------------------------------------------------------- float grid search
def float_lebesgue_setup(md, C, n):
    N = C.cols
    Ck = np.zeros((N, n + 1, n + 1))
    for l in range(N):
        for m, (a, b) in enumerate(md):
            Ck[l, a, b] = float(C[m, l])
    return Ck


def cheb_T(x, n):
    x = np.clip(x, -1.0, 1.0)
    th = np.arccos(x)
    return np.cos(np.outer(th, np.arange(n + 1)))  # (len(x), n+1)


def lebesgue_grid(Ck, xs, ys):
    n = Ck.shape[1] - 1
    Tx = cheb_T(xs, n)
    Ty = cheb_T(ys, n)
    tot = np.zeros((len(xs), len(ys)))
    for l in range(Ck.shape[0]):
        tot += np.abs(Tx @ Ck[l] @ Ty.T)
    return tot


def lebesgue_point(Ck, x, y):
    n = Ck.shape[1] - 1
    tx = np.cos(np.arange(n + 1) * math.acos(max(-1.0, min(1.0, x))))
    ty = np.cos(np.arange(n + 1) * math.acos(max(-1.0, min(1.0, y))))
    return float(np.sum(np.abs(np.einsum("lab,a,b->l", Ck, tx, ty))))


def grid_search(Ck, n, G=801, refine=40):
    from scipy.optimize import minimize
    xs = np.linspace(-1, 1, G)
    lam = lebesgue_grid(Ck, xs, xs)
    # discrete local maxima (8-neighbour, with boundary handled by padding -inf)
    pad = np.pad(lam, 1, constant_values=-np.inf)
    core = pad[1:-1, 1:-1]
    ismax = np.ones_like(core, dtype=bool)
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            ismax &= core >= pad[1 + dx:G + 1 + dx, 1 + dy:G + 1 + dy]
    idx = np.argwhere(ismax)
    vals = lam[ismax]
    order = np.argsort(-vals)
    cands = []
    for t in order[:refine]:
        i, j = idx[t]
        x0, y0 = xs[i], xs[j]
        res = minimize(lambda z: -lebesgue_point(Ck, z[0], z[1]), [x0, y0],
                       method="Nelder-Mead",
                       options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 4000})
        z = np.clip(res.x, -1, 1)
        cands.append((lebesgue_point(Ck, z[0], z[1]), float(z[0]), float(z[1]), float(vals[t])))
    cands.sort(reverse=True)
    # edges at much finer resolution
    e = np.linspace(-1, 1, 40001)
    edge = {}
    for name, xx, yy in (("y=-1", e, np.array([-1.0])), ("y=+1", e, np.array([1.0])),
                         ("x=-1", np.array([-1.0]), e), ("x=+1", np.array([1.0]), e)):
        v = lebesgue_grid(Ck, xx, yy).ravel()
        k = int(np.argmax(v))
        edge[name] = {"max": float(v[k]), "at": float(e[k])}
    return lam, xs, cands, edge


def second_peak(cands, corners, tol=1e-6):
    for v, x, y, g in cands:
        if all(abs(x - cx) > tol or abs(y - cy) > tol for cx, cy in corners):
            return {"value": v, "x": x, "y": y}
    return None


def per_cardinal_bernstein_int(n, Pint, E, box):
    Mx, dx = to_int_matrix(interval_power_to_bernstein(n, *box[0]))
    My, dy = to_int_matrix(interval_power_to_bernstein(n, *box[1]))
    MyT = My.T
    out = [Mx.dot(Pl).dot(MyT) for Pl in Pint]
    return out, dx * dy * (1 << E), (np.vectorize(abs, otypes=[object])(Mx).dot(
        np.ones((n + 1, n + 1), dtype=object)).dot(np.vectorize(abs, otypes=[object])(My).T))


def containment_on_box(n, Pint, E, box, checker_coeffs, S):
    """Check independent value lies in checker interval [lo,hi]/S for every cardinal/index.

    mine = Bint/scale with |Bint/scale - exact| <= err (rounding of Pint, 0.5 ulp at 2^-E, times
    sum |Mx||My|; mpmath solve error at dps>=90 is far smaller than the 2^-192 grid). Integer test:
    lo*scale - errint <= Bint*S <= hi*scale + errint.
    """
    Bs, scale, absM = per_cardinal_bernstein_int(n, Pint, E, box)
    m = n + 1
    contained = True
    min_slack = None
    max_width = 0
    for l, Bl in enumerate(Bs):
        tab = checker_coeffs[l]
        for i in range(m):
            for k in range(m):
                lo, hi = tab[i * m + k]
                max_width = max(max_width, hi - lo)
                v = int(Bl[i, k]) * S
                # rounding of Pint (<=0.5*absM in Bint units) plus 1e-6 of a 2^-192 unit for the
                # (far smaller, ~1e-19 unit) mpmath solve error
                err = int(absM[i, k]) * S + scale // 10**6
                a, b_ = lo * scale - err, hi * scale + err
                if not (a <= v <= b_):
                    contained = False
                slack = min(v - lo * scale, hi * scale - v)
                slack_units = slack / scale  # in units of 2^-192
                min_slack = slack_units if min_slack is None else min(min_slack, slack_units)
    return {"contained": contained, "min_slack_units": float(min_slack), "max_width_units": max_width}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, nargs="+", required=True)
    ap.add_argument("--dps", type=int, default=90)
    ap.add_argument("--out", required=True)
    ap.add_argument("--grid", type=int, default=801)
    ap.add_argument("--no-grid", action="store_true")
    ap.add_argument("--checker-compare", action="store_true",
                    help="import the repo's finite_general (read-only) and test containment")
    ap.add_argument("--leaf-replay", action="store_true")
    ap.add_argument("--leaf-containment", action="store_true")
    args = ap.parse_args()
    mp.mp.dps = args.dps
    results = {}
    for n in args.n:
        t0 = time.time()
        r = {"n": n, "dps": args.dps}
        nodes, xs, ys, md, C, res = direct_cardinals(n)
        r["direct_solve_residual"] = mp.nstr(res, 5)
        r["nodes"] = len(nodes)
        # partition of unity: sum_l C[m,l] = delta_{m,(0,0)}
        pu = max(abs(mp.fsum(C[m, l] for l in range(C.cols)) - (1 if md[m] == (0, 0) else 0))
                 for m in range(len(md)))
        r["partition_of_unity_defect"] = mp.nstr(pu, 5)
        Cf = formula_coefficients(n, nodes, md)
        r["max_abs_direct_minus_PD_T101_formula"] = mp.nstr(
            max(abs(C[m, l] - Cf[m, l]) for m in range(C.rows) for l in range(C.cols)), 5)
        for name, Cw in wrong_formula_variants(n, nodes, md).items():
            r["max_abs_direct_minus_" + name] = mp.nstr(
                max(abs(C[m, l] - Cw[m, l]) for m in range(C.rows) for l in range(C.cols)), 5)
        # random-point comparison of cardinals (direct vs formula)
        import random
        rng = random.Random(20261102 + n)
        worst = mp.mpf(0)
        for _ in range(25):
            x = mp.mpf(rng.uniform(-1, 1))
            y = mp.mpf(rng.uniform(-1, 1))
            tx = cheb_values_mp(x, n)
            ty = cheb_values_mp(y, n)
            q = [tx[a] * ty[b] for (a, b) in md]
            for l in range(C.cols):
                d1 = mp.fsum(C[m, l] * q[m] for m in range(len(md)))
                d2 = mp.fsum(Cf[m, l] * q[m] for m in range(len(md)))
                worst = max(worst, abs(d1 - d2))
        r["random_point_cardinal_max_diff"] = mp.nstr(worst, 5)
        # corner values by two routes
        corners = {}
        for cx, cy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            v1 = lebesgue_mp(C, md, n, mp.mpf(cx), mp.mpf(cy))
            v2 = corner_formula(n, cx, cy)
            node = any(abs(xs[i] - cx) < 1e-30 and abs(ys[i] - cy) < 1e-30 for i in range(len(nodes)))
            corners[f"({cx},{cy})"] = {"direct": mp.nstr(v1, 30), "PD_T101_corner_identity": mp.nstr(v2, 30),
                                       "diff": mp.nstr(abs(v1 - v2), 5), "is_node": node}
        r["corners"] = corners
        nonnode = [c for c, v in corners.items() if not v["is_node"]]
        r["nonnode_corners"] = nonnode
        Cval = lebesgue_mp(C, md, n, mp.mpf(-1), mp.mpf(-1))
        r["Lambda_c_direct"] = mp.nstr(Cval, 40)
        P = power_coefficients(n, md, C)
        # random point: power-basis vs Chebyshev-basis evaluation of cardinals
        worst = mp.mpf(0)
        for _ in range(5):
            x = mp.mpf(rng.uniform(-1, 1))
            y = mp.mpf(rng.uniform(-1, 1))
            for l in range(0, C.cols, max(1, C.cols // 10)):
                worst = max(worst, abs(eval_power(P[l], x, y) - eval_cheb(C, md, l, x, y, n)))
        r["power_vs_cheb_eval_diff"] = mp.nstr(worst, 5)

        if args.checker_compare:
            sys.path.insert(0, "/home/user/padua_research/topics/padua-argmax-alln-20261101/code/part3")
            sys.dont_write_bytecode = True
            import finite_general as g
            S = g.S
            cards, gnodes, seeds = g.construct(n)
            assert gnodes == nodes, "node order differs"
            worst_out = mp.mpf(0)
            max_width = 0
            contained = True
            for l in range(len(nodes)):
                for i in range(n + 1):
                    for j in range(n + 1):
                        lo, hi = cards[l].get((i, j), (0, 0))
                        max_width = max(max_width, hi - lo)
                        v = P[l][i][j] * S
                        if not (lo - mp.mpf(10) ** (-(args.dps - 70)) <= v <= hi + mp.mpf(10) ** (-(args.dps - 70))):
                            contained = False
                            worst_out = max(worst_out, max(lo - v, v - hi))
            r["checker_power_interval_containment"] = contained
            r["checker_power_interval_max_width"] = float(max_width) / float(S)
            r["checker_power_interval_worst_violation_scaled"] = mp.nstr(worst_out, 5)
            corner_list = ((-1, -1), (1, -1)) if n % 2 == 0 else ((-1, -1), (-1, 1))
            coeffs, meta = g.setup(n)
            th = meta["threshold_interval"]
            r["checker_threshold"] = [mp.nstr(mp.mpf(th[0]) / S, 30), mp.nstr(mp.mpf(th[1]) / S, 30)]
            r["Lambda_c_in_checker_threshold"] = bool(mp.mpf(th[0]) <= Cval * S <= mp.mpf(th[1]))
            r["checker_corners"] = meta["corners"]
            r["checker_corners_match_nonnode"] = sorted(f"({a},{b})" for a, b in meta["corners"]) == sorted(nonnode)
            # root (and optionally all-leaf) Bernstein containment, exact integer comparisons
            E = 320
            Pint = [np.array([[int(mp.nint(P[l][i][j] * (mp.mpf(2) ** E))) for j in range(n + 1)]
                              for i in range(n + 1)], dtype=object) for l in range(len(P))]
            r["checker_root_bernstein_containment"] = containment_on_box(
                n, Pint, E, [[F(-1), F(1)], [F(-1), F(1)]], coeffs, S)
            if args.leaf_containment:
                import gzip
                base = "/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/part3/"
                fname = {12: "finite_n12_pilot.json.gz"}.get(n, f"finite_n{n}_general.json.gz")
                d = json.loads(gzip.decompress(open(base + fname, "rb").read()))
                import finite_bernstein as bb
                summary = {"leaves": 0, "all_contained": True, "worst_slack_units": None, "max_width_units": 0}
                stack = [("", coeffs)]
                leafset = {row["path"] for row in d["leaves"]}
                while stack:
                    p, cf = stack.pop()
                    if p in leafset:
                        res_ = containment_on_box(n, Pint, E, box_of_path(p), cf, S)
                        summary["leaves"] += 1
                        summary["all_contained"] &= res_["contained"]
                        summary["max_width_units"] = max(summary["max_width_units"], res_["max_width_units"])
                        w_ = res_["min_slack_units"]
                        summary["worst_slack_units"] = w_ if summary["worst_slack_units"] is None else min(summary["worst_slack_units"], w_)
                        continue
                    if len(p) > 64:
                        raise AssertionError("path deeper than any leaf")
                    lft, rgt = bb.subdivide(cf, n, len(p) % 2)
                    stack.append((p + "0", lft))
                    stack.append((p + "1", rgt))
                r["checker_leaf_bernstein_containment"] = summary

        if args.leaf_replay:
            import gzip
            base = "/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/part3/"
            fname = {12: "finite_n12_pilot.json.gz"}.get(n, f"finite_n{n}_general.json.gz")
            d = json.loads(gzip.decompress(open(base + fname, "rb").read()))
            Sc = d["scale"]
            E = 320
            Pint = [np.array([[int(mp.nint(P[l][i][j] * (mp.mpf(2) ** E))) for j in range(n + 1)]
                              for i in range(n + 1)], dtype=object) for l in range(len(P))]
            paths = [row["path"] for row in d["leaves"]]
            prefix_free = all(not (p != q and q.startswith(p)) for p in paths for q in paths)
            kraft = sum(F(1, 2 ** len(p)) for p in paths)
            leaf_rows = []
            worst_rel_margin = None
            max_cert_minus_mine = 0.0
            min_cert_minus_mine = None
            all_ok = True
            Cf_ = Cval
            for row in d["leaves"]:
                box = box_of_path(row["path"])
                sums, scale = leaf_coefficient_sums(n, Pint, E, box)
                vals = [[mp.mpf(int(sums[i, k])) / scale for k in range(n + 1)] for i in range(n + 1)]
                if row["kind"] == "bound":
                    mine = max(max(r_) for r_ in vals)
                    vertex_info = None
                else:
                    cx, cy = row["corner"]
                    vi = 0 if box[0][0] == cx else n
                    vk = 0 if box[1][0] == cy else n
                    assert (box[0][0] == cx or box[0][1] == cx) and (box[1][0] == cy or box[1][1] == cy)
                    mine = max(vals[i][k] for i in range(n + 1) for k in range(n + 1) if (i, k) != (vi, vk))
                    vertex_info = {"vertex_index": [vi, vk], "vertex_sum": mp.nstr(vals[vi][vk], 25),
                                   "vertex_minus_Lambda_c": mp.nstr(vals[vi][vk] - Cf_, 5)}
                    # every non-vertex coefficient strictly below; vertex attains Lambda_c
                cert = mp.mpf(row.get("upper", row.get("upper_away_from_vertex"))) / Sc
                diff = cert - mine
                max_cert_minus_mine = max(max_cert_minus_mine, float(diff))
                min_cert_minus_mine = float(diff) if min_cert_minus_mine is None else min(min_cert_minus_mine, float(diff))
                rel = 1 - mine / Cf_
                worst_rel_margin = float(rel) if worst_rel_margin is None else min(worst_rel_margin, float(rel))
                ok = mine < Cf_ and diff >= -mp.mpf(10) ** -60
                all_ok &= bool(ok)
                leaf_rows.append({"path": row["path"], "kind": row["kind"],
                                  "box": [[str(z) for z in box[0]], [str(z) for z in box[1]]],
                                  "independent_max_sum": mp.nstr(mine, 20),
                                  "certificate_upper": mp.nstr(cert, 20),
                                  "cert_minus_independent": mp.nstr(diff, 5),
                                  "corner": row.get("corner"), "vertex": vertex_info})
            corner_set = sorted(tuple(row["corner"]) for row in d["leaves"] if row["kind"] == "corner")
            r["leaf_replay"] = {"certificate": fname, "leaves": len(paths), "prefix_free": prefix_free,
                                "kraft_sum": str(kraft), "all_leaf_predicates_hold_independently": all_ok,
                                "worst_relative_margin": worst_rel_margin,
                                "cert_minus_independent_range": [min_cert_minus_mine, max_cert_minus_mine],
                                "corner_leaves": corner_set, "rows": leaf_rows}

        if not args.no_grid:
            Ck = float_lebesgue_setup(md, C, n)
            lam, gx, cands, edge = grid_search(Ck, n, G=args.grid)
            corner_pts = [(-1.0, -1.0), (1.0, -1.0)] if n % 2 == 0 else [(-1.0, -1.0), (-1.0, 1.0)]
            k = np.unravel_index(np.argmax(lam), lam.shape)
            r["grid"] = {"G": args.grid, "grid_max": float(lam[k]), "grid_argmax": [float(gx[k[0]]), float(gx[k[1]])],
                         "top_refined": [{"value": v, "x": x, "y": y, "grid_value": gv} for v, x, y, gv in cands[:8]],
                         "best_noncorner_refined": second_peak(cands, corner_pts),
                         "edges_40001": edge,
                         "Lambda_c_float": float(Cval)}
            sp_ = r["grid"]["best_noncorner_refined"]
            if sp_:
                r["grid"]["gap_Lambda_c_minus_best_noncorner"] = float(Cval) - sp_["value"]
            # all grid values excluding corner pixels vs corner value
            mask = np.ones_like(lam, dtype=bool)
            for cx, cy in corner_pts:
                i = 0 if cx < 0 else len(gx) - 1
                j = 0 if cy < 0 else len(gx) - 1
                mask[i, j] = False
            r["grid"]["max_off_corner_pixels"] = float(lam[mask].max())
        r["seconds"] = time.time() - t0
        results[n] = r
        print(json.dumps({k: v for k, v in r.items() if k not in ("leaf_replay",)}, default=str)[:3000], flush=True)
        if "leaf_replay" in r:
            lr = r["leaf_replay"]
            print(json.dumps({k: v for k, v in lr.items() if k != "rows"}), flush=True)
        with open(f"{args.out}/indep_n{n}.json", "w") as fh:
            json.dump(r, fh, indent=1, default=str)


if __name__ == "__main__":
    main()
