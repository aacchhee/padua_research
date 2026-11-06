#!/usr/bin/env python3
"""Independent exact audit check of P3 (high-mode SH reweighting).

Written by the Claude audit subagent; does not import developer code.
Exact arithmetic in the cyclotomic field Q(zeta), zeta = exp(i*pi/(m+1)),
with s_k = (zeta^k + zeta^-k)/2.  Vectors are function values phi on the
nodes; the reweighted inner product is <phi,psi> = sum_i w_i phi_i psi_i, so
no square roots of weights are needed.  A represented Euclidean source is
f = sqrt(w)*psi with ||f||^2 = <psi,psi>.

Checks per (n, eta):
  T1 positivity / normalization / marginals / a_k = (-1)^(k+1)
  T2 moments: physical monomials x^a y^b equal to eta=0 for a+b<=2n+1,
     some differ at 2n+2 (and record which)
  T3 rank of latent weight matrix (rank 2) and explicit 2x2 minor = 4 eta prod v;
     convex hull of physical nodes (float) has exactly 4 vertices = latent corners
  T4 exact base Gram-Schmidt for BJ and mirror on the REWEIGHTED measure:
     pivots beta^2 = 1/4, columns = U_r(s)U_j(t), sigma^2 formulas
  T5 normal witness e = U_{n+1}(s): <e,x^a y^b>_w = 0 for a+b<=n, <e,e>=1,
     <q_(n+1,0), q_(0,n+1)> = eta
  T6 dual-number full sequential projection (actual perturbed algorithm, exact
     to first order) with BJ witness source psi_(n,0)=e (source norm^2 = 2):
     normal-output Gram is rank one and lambda_max/2 = 2(4^(n+1)-1)/3
  T7 dual-number vs frozen response agreement mod Pi_n for random sources
     (both rules)
  T8 mirror positivity witness at (0,n)
  T9 numeric: frozen impulse responses -> row upper / HS upper for mirror,
     compared with 2 sqrt6 (n+1)^2 (N_n-1); alternating-maximization
     estimates of both capacities (MEASURED, float64)
"""
import argparse, json, math, random, sys, time
from fractions import Fraction
import flint
import numpy as np

Q = flint.fmpq
QP = flint.fmpq_poly


class Field:
    def __init__(self, m):
        self.N = 2 * (m + 1)
        self.phi = QP(flint.fmpz_poly.cyclotomic(self.N).coeffs())
        self.zeta_num = complex(math.cos(math.pi / (m + 1)), math.sin(math.pi / (m + 1)))

    def red(self, p):
        return p % self.phi

    def const(self, c):
        return QP([c])

    def zpow(self, k):
        k %= self.N
        return self.red(QP([0] * k + [1]))

    def is_zero(self, p):
        return self.red(p) == 0

    def as_rational(self, p):
        p = self.red(p)
        if p.degree() <= 0:
            c = p.coeffs()
            return Fraction(0) if not c else Fraction(int(c[0].p), int(c[0].q))
        return None

    def num(self, p):
        p = self.red(p)
        z = self.zeta_num
        acc = 0j
        for c in reversed(p.coeffs()):
            acc = acc * z + float(Fraction(int(c.p), int(c.q)))
        return acc.real


def run_case(n, eta, rng, seconds_numeric):
    m = n + 2
    F = Field(m)
    red = F.red
    half = Q(1, 2)
    eta_q = Q(eta.numerator, eta.denominator)
    res = {"n": n, "eta": str(eta), "m": m, "M": m * m}
    s = [None] + [red((F.zpow(k) + F.zpow(-k)) * half) for k in range(1, m + 1)]

    def U(r, z):
        if r < 0:
            return QP([0])
        a, b = QP([1]), red(2 * z)
        if r == 0:
            return a
        for _ in range(r - 1):
            a, b = b, red(2 * z * b - a)
        return b

    v = [None] + [red(2 * (1 - s[k] * s[k]) * Q(1, m + 1)) for k in range(1, m + 1)]
    a = [None] + [U(n + 1, s[k]) for k in range(1, m + 1)]
    # T1
    t1 = {}
    t1["a_k_signs_exact"] = all(F.as_rational(a[k]) == (-1) ** (k + 1) for k in range(1, m + 1))
    idx = [(k, l) for k in range(1, m + 1) for l in range(1, m + 1)]
    M = len(idx)
    w = [red(v[k] * v[l] * (1 + eta_q * a[k] * a[l])) for (k, l) in idx]
    w0 = [red(v[k] * v[l]) for (k, l) in idx]
    t1["total_mass"] = str(F.as_rational(sum(w, QP([0]))))
    t1["min_weight_float"] = min(F.num(x) for x in w)
    t1["marginal_s_ok"] = all(F.is_zero(sum((w[(k - 1) * m + l - 1] for l in range(1, m + 1)), QP([0])) - v[k]) for k in range(1, m + 1))
    t1["marginal_t_ok"] = all(F.is_zero(sum((w[(k - 1) * m + l - 1] for k in range(1, m + 1)), QP([0])) - v[l]) for l in range(1, m + 1))
    t1["pass"] = t1["a_k_signs_exact"] and t1["total_mass"] == "1" and t1["min_weight_float"] > 0 and t1["marginal_s_ok"] and t1["marginal_t_ok"]
    res["T1"] = t1
    X = [s[k] for (k, l) in idx]
    Y = [red(2 * s[k] + s[l]) for (k, l) in idx]
    # T2 moments: physical monomials
    Xp = [[QP([1])] * M]
    Yp = [[QP([1])] * M]
    for d in range(1, 2 * n + 3):
        Xp.append([red(Xp[-1][i] * X[i]) for i in range(M)])
        Yp.append([red(Yp[-1][i] * Y[i]) for i in range(M)])
    dw = [red(w[i] - w0[i]) for i in range(M)]
    first_bad = None
    bad_at = []
    for d in range(0, 2 * n + 3):
        for b in range(d + 1):
            aa = d - b
            val = red(sum((dw[i] * Xp[aa][i] * Yp[b][i] for i in range(M)), QP([0])))
            if val != 0:
                bad_at.append((aa, b, str(F.as_rational(val)) if F.as_rational(val) is not None else F.num(val)))
                if first_bad is None:
                    first_bad = d
    res["T2"] = {"first_differing_degree": first_bad, "expected": 2 * n + 2,
                 "differing_monomials_at_2n+2": bad_at,
                 "pass": first_bad == 2 * n + 2}
    # T3 rank of latent weight matrix
    Wm = np.array([[F.num(w[(k - 1) * m + l - 1]) for l in range(1, m + 1)] for k in range(1, m + 1)])
    sv = np.linalg.svd(Wm, compute_uv=False)
    # exact minor rows k=1 (a=+1), k'=2 (a=-1), cols 1,2
    minor = red(w[0] * w[m + 1] - w[1] * w[m])
    expect = red(4 * eta_q * v[1] * v[2] * v[1] * v[2])
    # exact rank: all 3x3 minors zero? check rank<=2 exactly via a few 3x3 minors
    def wkl(k, l):
        return w[(k - 1) * m + l - 1]
    three_minors_zero = True
    for (r1, r2, r3) in [(1, 2, 3), (1, 3, 4), (2, 3, m)]:
        for (c1, c2, c3) in [(1, 2, 3), (2, 3, 4), (1, 3, m)]:
            Mx = [[wkl(r, c) for c in (c1, c2, c3)] for r in (r1, r2, r3)]
            det = red(Mx[0][0] * (Mx[1][1] * Mx[2][2] - Mx[1][2] * Mx[2][1])
                      - Mx[0][1] * (Mx[1][0] * Mx[2][2] - Mx[1][2] * Mx[2][0])
                      + Mx[0][2] * (Mx[1][0] * Mx[2][1] - Mx[1][1] * Mx[2][0]))
            three_minors_zero &= (det == 0)
    pts = np.array([[F.num(X[i]), F.num(Y[i])] for i in range(M)])
    hull = convex_hull(pts)
    corners = {(1, 1), (1, m), (m, 1), (m, m)}
    hull_idx = sorted(idx[i] for i in hull)
    res["T3"] = {"minor_equals_4eta_prod_v": F.is_zero(minor - expect),
                 "minor_float": F.num(minor),
                 "singular_values": [float(x) for x in sv[:3]],
                 "sampled_3x3_minors_zero": three_minors_zero,
                 "hull_vertex_count": len(hull), "hull_vertices_latent": hull_idx,
                 "hull_vertices_are_latent_corners": set(hull_idx) == corners}
    res["T3"]["pass"] = (res["T3"]["minor_equals_4eta_prod_v"] and abs(res["T3"]["minor_float"]) > 0
                         and sv[1] > 1e-12 and len(hull) == 4 and set(hull_idx) == corners)

    def ip(p, q):
        return red(sum((w[i] * p[i] * q[i] for i in range(M)), QP([0])))

    # columns
    cols = [(d - j, j) for d in range(n + 1) for j in range(d + 1)]
    pos = {c: i for i, c in enumerate(cols)}
    Us = {r: [U(r, s[k]) for (k, l) in idx] for r in range(n + 2)}
    Ut = {r: [U(r, s[l]) for (k, l) in idx] for r in range(n + 2)}

    def rule_parent(rule, h):
        r, j = h
        if rule == "BJ":
            return ("X", (r - 1, 0)) if j == 0 else ("Y", (r, j - 1))
        return ("X", (r - 1, j)) if r > 0 else ("Y", (0, j - 1))

    # T4 exact base GS (not assuming the U formula)
    t4 = {}
    base = {}
    sig2 = {}
    for rule in ("BJ", "mirror"):
        q = {(0, 0): [QP([1])] * M}
        ok_beta = True
        ok_U = True
        sg = {}
        for h in cols[1:]:
            op, p = rule_parent(rule, h)
            A = X if op == "X" else Y
            raw = [red(A[i] * q[p][i]) for i in range(M)]
            sg[h] = F.as_rational(ip(raw, raw))
            r_ = raw
            for l in cols[:pos[h]]:
                c = ip(q[l], raw)
                r_ = [red(r_[i] - c * q[l][i]) for i in range(M)]
            nn = F.as_rational(ip(r_, r_))
            if nn != Fraction(1, 4):
                ok_beta = False
            q[h] = [red(2 * r_[i]) for i in range(M)]
            target = [red(Us[h[0]][i] * Ut[h[1]][i]) for i in range(M)]
            if any(q[h][i] != target[i] for i in range(M)):
                ok_U = False
        # sigma formula check
        ok_sig = True
        for h in cols[1:]:
            op, (pa, pb) = rule_parent(rule, h)
            if op == "X":
                expct = Fraction(1 + (pa >= 1), 4)
            else:
                expct = 1 + (pa >= 1) + Fraction(1 + (pb >= 1), 4)
            if sg[h] != expct:
                ok_sig = False
        base[rule] = q
        sig2[rule] = sg
        t4[rule] = {"pivots_beta2_quarter": ok_beta, "columns_equal_UrUj": ok_U,
                    "sigma2_formula": ok_sig, "max_sigma2": str(max(sg.values())),
                    "sigma2_(n,0)": str(sg[(n, 0)])}
    # orthonormality through degree n
    qb = base["BJ"]
    orth = all(ip(qb[c1], qb[c2]) == (1 if c1 == c2 else 0) for c1 in cols for c2 in cols)
    t4["orthonormal_through_n"] = orth
    t4["pass"] = orth and all(t4[r]["pivots_beta2_quarter"] and t4[r]["columns_equal_UrUj"] and t4[r]["sigma2_formula"] for r in ("BJ", "mirror"))
    res["T4"] = t4

    # T5 normal witness
    e = Us[n + 1]
    mon_ok = True
    for d in range(n + 1):
        for b in range(d + 1):
            pm = [red(Xp[d - b][i] * Yp[b][i]) for i in range(M)]
            if ip(e, pm) != 0:
                mon_ok = False
    deg_n1 = []
    for b in range(n + 2):
        pm = [red(Xp[n + 1 - b][i] * Yp[b][i]) for i in range(M)]
        deg_n1.append(ip(e, pm) != 0)
    cross = F.as_rational(ip(Us[n + 1], Ut[n + 1]))
    res["T5"] = {"e_orthogonal_to_Pi_n_in_reweighted_ip": mon_ok,
                 "e_norm2": str(F.as_rational(ip(e, e))),
                 "e_not_orthogonal_to_some_degree_n+1_monomial": any(deg_n1),
                 "ip_q(n+1,0)_q(0,n+1)": str(cross),
                 "pass": mon_ok and F.as_rational(ip(e, e)) == 1 and cross == eta}

    # dual-number perturbed run
    def proj_normal(phi):
        out = list(phi)
        for c in cols:
            cc = ip(qb[c], phi)
            out = [red(out[i] - cc * qb[c][i]) for i in range(M)]
        return out

    def dual_run(rule, src):
        """src: dict h -> function-value vector psi_h. Returns derivative columns."""
        qv = {(0, 0): [QP([1])] * M}
        qd = {(0, 0): [QP([0])] * M}
        for h in cols[1:]:
            op, p = rule_parent(rule, h)
            A = X if op == "X" else Y
            rv = [red(A[i] * qv[p][i]) for i in range(M)]
            rd = [red(A[i] * qd[p][i]) for i in range(M)]
            if h in src:
                rd = [red(rd[i] + src[h][i]) for i in range(M)]
            raw_v, raw_d = rv, rd
            for l in cols[:pos[h]]:
                cv = ip(qv[l], raw_v)
                cd = red(ip(qd[l], raw_v) + ip(qv[l], raw_d))
                rv = [red(rv[i] - cv * qv[l][i]) for i in range(M)]
                rd = [red(rd[i] - cv * qd[l][i] - cd * qv[l][i]) for i in range(M)]
            na = F.as_rational(ip(rv, rv))
            assert na == Fraction(1, 4), (rule, h, na)
            nb = red(2 * ip(rv, rd))
            # (na + nb eps)^(-1/2) = 2 - 4 nb eps
            qv[h] = [red(2 * rv[i]) for i in range(M)]
            qd[h] = [red(2 * rd[i] - 4 * nb * rv[i]) for i in range(M)]
        return qd

    def frozen(rule, src):
        Vv = {(0, 0): [QP([0])] * M}
        for h in cols[1:]:
            op, p = rule_parent(rule, h)
            A = X if op == "X" else Y
            qrule = base[rule]
            raw0 = [red(A[i] * qrule[p][i]) for i in range(M)]
            acc = [red(A[i] * Vv[p][i]) for i in range(M)]
            for l in cols[:pos[h]]:
                c = ip(qrule[l], raw0)
                if c != 0:
                    acc = [red(acc[i] - c * Vv[l][i]) for i in range(M)]
            if h in src:
                acc = [red(acc[i] + src[h][i]) for i in range(M)]
            Vv[h] = [red(2 * acc[i]) for i in range(M)]
        return Vv

    def out_gram(cols_d):
        Rn = {h: proj_normal(cols_d[h]) for h in cols[1:]}
        G = [[ip(Rn[h], Rn[g]) for g in cols[1:]] for h in cols[1:]]
        return Rn, G

    # T6 BJ witness via actual perturbed run
    qd = dual_run("BJ", {(n, 0): e})
    Rn, G = out_gram(qd)
    H = len(cols) - 1
    tr = F.as_rational(sum((G[i][i] for i in range(H)), QP([0])))
    rank1 = all(F.is_zero(G[i][i] * G[j][j] - G[i][j] * G[j][i]) for i in range(H) for j in range(H))
    srcnorm2 = Fraction(1) / sig2["BJ"][(n, 0)]
    lam_over_src = tr / srcnorm2 if tr is not None else None
    expect_bj = Fraction(2 * (4 ** (n + 1) - 1), 3)
    # normal part equals full derivative on degree-n columns? (component check)
    res["T6"] = {"G_out_rank_one": rank1, "lambda_max_over_srcnorm2": str(lam_over_src),
                 "expected_2(4^(n+1)-1)/3": str(expect_bj),
                 "pass": rank1 and lam_over_src == expect_bj}

    # T7 dual vs frozen random sources
    t7 = {}
    for rule in ("BJ", "mirror"):
        src = {h: [QP([rng.randint(-3, 3)]) for _ in range(M)] for h in cols[1:]}
        qd = dual_run(rule, src)
        Vv = frozen(rule, src)
        ok = all(all(F.is_zero(x - y) for x, y in zip(proj_normal(qd[h]), proj_normal(Vv[h]))) for h in cols[1:])
        t7[rule] = ok
    t7["pass"] = all(t7.values())
    res["T7"] = t7

    # T8 mirror positivity witness at (0,n)
    qd = dual_run("mirror", {(0, n): e})
    Rn, G = out_gram(qd)
    nz = [cols[1:][i] for i in range(H) if G[i][i] != 0]
    res["T8"] = {"nonzero_output_columns": nz, "value_over_srcnorm2": str(F.as_rational(G[H - 1][H - 1]) * sig2["mirror"][(0, n)]),
                 "expected_4sigma^4/... (=4 sigma^2 * sigma^2/sigma^2)": str(4 * sig2["mirror"][(0, n)]),
                 "pass": nz == [(0, n)] and F.as_rational(G[H - 1][H - 1]) * sig2["mirror"][(0, n)] == 4 * sig2["mirror"][(0, n)]}

    # T9 numeric capacities via impulse responses
    sq = np.sqrt(np.array([F.num(x) for x in w]))
    Qrep = np.array([[F.num(qb[c][i]) for c in cols] for i in range(M)]) * sq[:, None]
    Rrep = np.eye(M) - Qrep @ Qrep.T
    t9 = {"orthonormality_err": float(np.abs(Qrep.T @ Qrep - np.eye(len(cols))).max())}
    for rule in ("BJ", "mirror"):
        # g[k][h][i]
        g = np.zeros((H, H, M))
        for hi, h in enumerate(cols[1:]):
            Vv = frozen(rule, {h: [QP([1])] * M})
            for ki, k in enumerate(cols[1:]):
                g[ki, hi, :] = [F.num(x) for x in Vv[k]]
        s2 = np.array([float(sig2[rule][h]) for h in cols[1:]])
        # Q_i[k,k'] = sum_h s2_h g[k,h,i] g[k',h,i]
        Qi = np.einsum('h,khi,lhi->ikl', s2, g, g)
        row_upper = math.sqrt(max(np.trace(Qi[i]) for i in range(M)))
        lev = np.einsum('ikk->i', Qi)  # sum_h s2 sum_k g^2 at node i
        hs_upper = math.sqrt(float(np.sum(np.diag(Rrep) * lev)))
        best = 0.0
        t0 = time.time()
        trials = 0
        nrng = np.random.default_rng(12345 + n)
        while trials < 40 or (time.time() - t0 < seconds_numeric and trials < 400):
            trials += 1
            c = nrng.standard_normal(H); c /= np.linalg.norm(c)
            val = 0
            for _ in range(300):
                rho = np.einsum('ikl,k,l->i', Qi, c, c)
                Bm = np.sqrt(np.maximum(rho, 0))[:, None] * Rrep * np.sqrt(np.maximum(rho, 0))[None, :]
                lam, vec = np.linalg.eigh(Bm)
                yv = vec[:, -1]
                # y such that sqrt(rho) R ... ; Ry direction: z_i = (R y')_i^2 where y' = R sqrt(rho) yv / norm
                yy = Rrep @ (np.sqrt(np.maximum(rho, 0)) * yv)
                yy /= np.linalg.norm(yy)
                z = (Rrep @ yy) ** 2
                Cm = np.einsum('i,ikl->kl', z, Qi)
                lc, vc = np.linalg.eigh(Cm)
                newval = lc[-1]
                c = vc[:, -1]
                if abs(newval - val) < 1e-13 * max(1, newval):
                    val = newval
                    break
                val = newval
            best = max(best, val)
        t9[rule] = {"capacity_estimate": math.sqrt(best), "row_upper": row_upper,
                    "hs_upper": hs_upper, "trials": trials}
    t9["BJ_lower_claim"] = math.sqrt(2 * (4 ** (n + 1) - 1) / 3)
    Nn = (n + 1) * (n + 2) // 2
    t9["mirror_upper_claim"] = 2 * math.sqrt(6) * (n + 1) ** 2 * (Nn - 1)
    t9["ratio_lower_claim"] = 2 ** n / (2 * math.sqrt(3) * (n + 1) ** 2 * (Nn - 1))
    t9["pass_consistency"] = (t9["BJ"]["capacity_estimate"] >= t9["BJ_lower_claim"] * (1 - 1e-9)
                              and t9["mirror"]["capacity_estimate"] <= t9["mirror_upper_claim"]
                              and t9["mirror"]["row_upper"] <= t9["mirror_upper_claim"])
    res["T9_MEASURED_float64"] = t9
    res["all_exact_pass"] = all(res[k]["pass"] for k in ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"))
    return res


def convex_hull(pts):
    order = sorted(range(len(pts)), key=lambda i: (pts[i][0], pts[i][1]))
    def cross(o, a, b):
        return (pts[a][0] - pts[o][0]) * (pts[b][1] - pts[o][1]) - (pts[a][1] - pts[o][1]) * (pts[b][0] - pts[o][0])
    lower, upper = [], []
    for i in order:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], i) <= 1e-12:
            lower.pop()
        lower.append(i)
    for i in reversed(order):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], i) <= 1e-12:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--degrees", default="2,3,4")
    ap.add_argument("--etas", default="1/2,-1/3")
    ap.add_argument("--seconds", type=float, default=20)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    rng = random.Random(20261106)
    out = {"tool": "p3_audit_check.py (independent, Claude audit subagent)",
           "python": sys.version, "flint": flint.__version__, "numpy": np.__version__, "cases": []}
    for n in [int(x) for x in args.degrees.split(",")]:
        for et in args.etas.split(","):
            eta = Fraction(et)
            t0 = time.time()
            r = run_case(n, eta, rng, args.seconds)
            r["elapsed_s"] = round(time.time() - t0, 2)
            out["cases"].append(r)
            print(json.dumps({"n": n, "eta": et, "all_exact_pass": r["all_exact_pass"],
                              "first_diff_deg": r["T2"]["first_differing_degree"],
                              "BJ_est": r["T9_MEASURED_float64"]["BJ"]["capacity_estimate"],
                              "BJ_lower": r["T9_MEASURED_float64"]["BJ_lower_claim"],
                              "mir_est": r["T9_MEASURED_float64"]["mirror"]["capacity_estimate"],
                              "mir_row_up": r["T9_MEASURED_float64"]["mirror"]["row_upper"],
                              "mir_claim_up": r["T9_MEASURED_float64"]["mirror_upper_claim"],
                              "t": r["elapsed_s"]}), flush=True)
    with open(args.output, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
