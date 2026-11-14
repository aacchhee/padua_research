#!/usr/bin/env python3
"""X2 round 3: numerical checks (float64 / mpmath; MEASURED support only, no certificate).

Sections (run all by default, or name them on the command line):
  transl   translation formula (theory/X2-34): K_n(P,z_a) against (i) the four-term diamond-kernel formula,
           (ii) the box average of Gt = (1/4) d_alpha d_beta D_M (mpmath quad, n = 2 only), mpmath 30 digits, n = 2,4,6;
           also the rotated product form of D_M.
  farfield far-field bounds of theory/X2-33 against lambda_n on angle grids (float64), n in {10, 40, 100, 200}.
  dlimit   heuristic limit constant d = (8/pi) int_band k2 against D_x/M^4, D_y/M^4 (certified values are read
           from /tmp/x2r3/fv_band_*.json if present).
  shift    shifted-lattice sums Xi(a1,a2) (theory/X2-34) at M = 62, 102, 202 against the heuristic limit
           |cos(M(a1+a2)/2)| * J(-M(a1-a2)/2); exhibits shifts with Xi(a) > Xi(0) (theory/X2-N35).
  jensen   the averaged bound B(xi,ze) = E|cos phibar| J(psi) against L_top (heuristic profile of X2-28) and lambda_n/M^2.
  ucoef    Chebyshev-U coefficients of the edge restrictions of P = sum_a sgn(l_a(1,1)) l_a, even n <= 120.
Usage: python3 x2r3_checks.py [sections] [--out /tmp/x2r3/x2r3_checks.json]
"""
import sys, json, os, time
import numpy as np
import mpmath as mp

CSTAR = 0.516953653366806


# ------------------------------------------------------------------ common (float64)
def node_arrays(M):
    p = np.arange(1, M)[:, None] * np.ones((1, M), dtype=int)
    q = np.arange(1, M + 1)[None, :] * np.ones((M - 1, 1), dtype=int)
    mask = ((p + q) % 2 == 1)
    return p[mask], q[mask]


def Ft(g, M):
    return np.cos((M + 1) * g) + np.cos(M * g)


def dFt(g, M):
    return -(M + 1) * np.sin((M + 1) * g) - M * np.sin(M * g)


def Gt(al, be, M):
    """Gt(alpha,beta) = (1/4) d_alpha d_beta D_M(alpha,beta) = sum_{k,l>=1,k+l<=M} k l sin(k alpha) sin(l beta) (closed form)."""
    XmY = -2 * np.sin((al + be) / 2) * np.sin((al - be) / 2)        # cos al - cos be
    return 0.25 * ((-dFt(al, M) * np.sin(be) - dFt(be, M) * np.sin(al)) / XmY ** 2
                   - 2 * np.sin(al) * np.sin(be) * (Ft(al, M) - Ft(be, M)) / XmY ** 3)


def lam_angles(n, th1, th2):
    """lambda_n(cos th1, cos th2), four-term formula (X2-28 Lemma K)."""
    M = n + 2; N = M * (M + 1)
    p, q = node_arrays(M)
    w = np.pi * p / M; v = np.pi * q / (M + 1)
    tot = np.zeros(w.shape)
    for s1 in (1, -1):
        for s2 in (1, -1):
            al = th1 - s1 * w; be = th2 - s2 * v
            tot += s1 * s2 * (Ft(al, M) - Ft(be, M)) / (np.cos(al) - np.cos(be))
    return float(np.abs(np.sin(w) * np.sin(v) / (2 * N * np.sin(th1) * np.sin(th2)) * tot).sum())


def Xi(M, a1, a2):
    """Xi(a1,a2) = (8/N) sum_a sin w_a sin v_a |Gt(w_a+a1, v_a+a2)|;  Xi(0,0) = lambda_n(1,1)."""
    N = M * (M + 1)
    p, q = node_arrays(M)
    w = np.pi * p / M; v = np.pi * q / (M + 1)
    return float(8.0 / N * (np.sin(w) * np.sin(v) * np.abs(Gt(w + a1, v + a2, M))).sum())


def kappa(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    small = np.abs(x) < 1e-3
    out[small] = 1 / 3 - x[small] ** 2 / 30
    xl = x[~small]
    out[~small] = np.abs(np.sin(xl) - xl * np.cos(xl)) / np.abs(xl) ** 3
    return out


_Jcache = {}


def Jfun(psi, mmax=400, h=0.001):
    """J(psi) = (4/pi) int_S |sin 2tau sin tau| kappa(tau+psi) dtau, S = U_j (j pi, j pi + pi/2); pi-periodic."""
    psi = float(np.mod(psi + np.pi / 2, np.pi) - np.pi / 2)
    key = round(psi / 1e-4)
    if key in _Jcache:
        return _Jcache[key]
    y = np.arange(h / 2, np.pi / 2, h)
    W = 2 * np.sin(y) ** 2 * np.cos(y)
    tot = np.zeros_like(y)
    for m in range(-mmax, mmax + 1):
        tot += kappa(y + psi + m * np.pi)
    tot += 2 * np.abs(np.cos(y + psi)) / (np.pi ** 2 * mmax)      # tail of sum_m |cos|/(m pi)^2
    val = float(4 / np.pi * np.sum(W * tot) * h)
    _Jcache[key] = val
    return val


def Ltop(xi, ze, T=400.0, h=0.005):
    sinc = lambda x: np.sinc(x / np.pi)
    tau = np.arange(h / 2, T, h)
    a = (xi + ze) / 2; b = (xi - ze) / 2
    if abs(a * a - b * b) < 1e-12:
        a += 1e-6
    G = np.cos(a) * (sinc(tau + b) + sinc(tau - b)) - np.cos(b) * (sinc(tau + a) + sinc(tau - a))
    return float(2 / np.pi * np.sum(np.abs(2 * np.sin(tau) ** 2 * np.cos(tau) * G / (a * a - b * b))) * h)


# ------------------------------------------------------------------ sections
def sec_transl():
    mp.mp.dps = 30
    res = {}
    def U_list(x, n):
        u = [mp.mpf(1), 2 * x]
        for i in range(2, n + 1): u.append(2 * x * u[-1] - u[-2])
        return u[:n + 1]
    def D(al, be, M):
        return mp.fsum(mp.cos(k * al + l * be) for k in range(-M, M + 1) for l in range(-(M - abs(k)), M - abs(k) + 1))
    def Gtm(al, be, M):
        return mp.fsum(k * l * mp.sin(k * al) * mp.sin(l * be) for k in range(1, M) for l in range(1, M - k + 1))
    e1 = e2 = e3 = mp.mpf(0)
    for n in (2, 4, 6):
        M = n + 2
        for (t1, t2) in ((mp.mpf('0.3'), mp.mpf('1.1')), (mp.mpf('2.0'), mp.mpf('0.7'))):
            for p in range(1, M):
                for q in range(1, M + 1):
                    if (p + q) % 2 == 0: continue
                    w = mp.pi * p / M; v = mp.pi * q / (M + 1)
                    a, b, c, d = U_list(mp.cos(t1), n), U_list(mp.cos(t2), n), U_list(mp.cos(w), n), U_list(mp.cos(v), n)
                    K = mp.fsum(a[i] * c[i] * b[j] * d[j] for i in range(n + 1) for j in range(n + 1 - i))
                    four = mp.fsum(s1 * s2 * D(t1 - s1 * w, t2 - s2 * v, M) for s1 in (1, -1) for s2 in (1, -1)) / (16 * mp.sin(t1) * mp.sin(w) * mp.sin(t2) * mp.sin(v))
                    e1 = max(e1, abs(K - four))
                    if n == 2:
                        box = mp.quad(lambda al, be: Gtm(al, be, M), [w - t1, w + t1], [v - t2, v + t2]) / (4 * mp.sin(t1) * mp.sin(w) * mp.sin(t2) * mp.sin(v))
                        e2 = max(e2, abs(K - box))
        for (al, be) in ((mp.mpf('0.37'), mp.mpf('1.9')), (mp.mpf('-2.2'), mp.mpf('0.45'))):
            u = (al + be) / 2; vv = (al - be) / 2
            rot = (mp.sin((M + 1) * u) * mp.sin((M + 1) * vv) + mp.sin(M * u) * mp.sin(M * vv)) / (mp.sin(u) * mp.sin(vv))
            e3 = max(e3, abs(D(al, be, M) - rot))
            e3 = max(e3, abs(Gtm(al, be, M) - mp.mpf(Gt(float(al), float(be), M))) * mp.mpf('1e-14'))   # float closed form, scaled
    res["four_term_diamond_formula_max_err"] = mp.nstr(e1, 5)
    res["box_average_formula_max_err_(quad)"] = mp.nstr(e2, 5)
    res["rotated_product_form_max_err"] = mp.nstr(e3, 5)
    # closed form Gt (float) vs double sum
    errG = 0.0
    for M in (4, 8, 12):
        for (al, be) in ((0.37, 1.9), (2.2, 0.45), (1.0, 1.3)):
            ds = sum(k * l * np.sin(k * al) * np.sin(l * be) for k in range(1, M) for l in range(1, M - k + 1))
            errG = max(errG, abs(ds - Gt(np.array(al), np.array(be), M)) / (1 + abs(ds)))
    res["Gt_closed_form_vs_double_sum_rel_err"] = errG
    # Xi(0,0) = lambda(1,1)
    res["Xi(0,0)_minus_lam11_n=20"] = Xi(22, 0.0, 0.0) - 236.90095327527381
    return res


def sec_farfield():
    rows = []
    ok = True
    for n in (10, 40, 100, 200):
        M = n + 2; L = np.log(M)
        Cab = (1 + 1 / M) * (2 + L) * (5 + 2 * L)
        Cb = (np.pi / 2) * (2 * M + 1) * Cab
        worst_a = 0.0; worst_b = 0.0
        g = np.linspace(0.02, np.pi - 0.02, 41 if n <= 100 else 25)
        for t1 in g:
            for t2 in g:
                lam = lam_angles(n, t1, t2)
                ba = Cab / (np.sin(t1) * np.sin(t2)); bb = Cb / max(np.sin(t1), np.sin(t2))
                worst_a = max(worst_a, lam / ba); worst_b = max(worst_b, lam / bb)
        ok = ok and worst_a <= 1 and worst_b <= 1
        rows.append({"n": n, "max lambda/bound_(a)": worst_a, "max lambda/bound_(b)": worst_b,
                     "theta_loc = C_FF/(cstar n^2)": Cb / (CSTAR * n * n)})
    return {"rows": rows, "bounds_hold_on_grid": ok}


def sec_dlimit():
    # d = (8/pi) int over band {h~ > 0} of k2,  k2 = sin^2(tau) cos(tau) m4(tau)/24,
    # m4 = 8[-cos/t^2 + 3 sin/t^3 + 6 cos/t^4 - 6 sin/t^5]
    mp.mp.dps = 25
    def m4(t): return 8 * (-mp.cos(t) / t ** 2 + 3 * mp.sin(t) / t ** 3 + 6 * mp.cos(t) / t ** 4 - 6 * mp.sin(t) / t ** 5)
    def k2(t): return mp.sin(t) ** 2 * mp.cos(t) * m4(t) / 24
    tot = mp.quad(k2, [0, mp.pi / 4, mp.pi / 2])
    terms = [tot]
    for j in range(1, 60):
        a = mp.findroot(lambda t: mp.sin(t) - t * mp.cos(t), j * mp.pi + mp.pi / 2 - 1 / (j * mp.pi))
        terms.append(mp.quad(k2, [a, j * mp.pi + mp.pi / 2]))
    d = 8 / mp.pi * mp.fsum(terms)
    res = {"d_band_integral_(60_bumps;_terms_decay_like_j^-5)": mp.nstr(d, 12), "first_bump_share": mp.nstr(8 / mp.pi * terms[0], 12),
           "last_term": mp.nstr(8 / mp.pi * terms[-1], 5)}
    try:
        import glob
        f = sorted(glob.glob("/tmp/x2r3/fv_band_*.json"))[-1]
        rows = json.load(open(f))["rows"]
        res["certified_D_over_M4_(n,Dx,Dy)"] = [(r["n"], r["Dx_over_M4_lower"], r["Dy_over_M4_lower"]) for r in rows if r["n"] in (10, 100, 1000, rows[-1]["n"])]
    except Exception as ex:
        res["certified_values"] = "not found: %s" % ex
    return res


def sec_shift():
    rows = []
    for M in (62, 102, 202):
        lam = Xi(M, 0.0, 0.0)
        for (f1, f2) in ((0.0, 0.0), (0.9, -0.9), (-0.9, 0.9), (1.8, 0.0), (0.0, 1.8), (0.6, 0.6), (-0.6, 0.6), (np.pi, np.pi), (np.pi, 0.0), (0.0, np.pi)):
            a1 = f1 / M; a2 = f2 / M
            xi = Xi(M, a1, a2)
            heur = abs(np.cos((f1 + f2) / 2)) * Jfun(-(f1 - f2) / 2)
            rows.append({"M": M, "M*a1": f1, "M*a2": f2, "Xi/M^2": xi / M ** 2, "heuristic": heur, "Xi/Xi(0)": xi / lam})
    # scan psi at M = 202: Xi(psi/M*(-1), psi/M) ... direction a1 = -a2
    scan = []
    M = 202
    for s in np.linspace(-1.5, 1.5, 13):
        scan.append((round(float(s), 3), Xi(M, s / M, -s / M) / M ** 2, Jfun(-s)))
    best = max(rows, key=lambda r: r["Xi/Xi(0)"])
    return {"rows": rows, "scan_M202_(s, Xi(s/M,-s/M)/M^2, J(-s))": scan, "max_Xi_over_Xi0": best,
            "Jmax_on_grid": max(Jfun(x) for x in np.linspace(-np.pi / 2, np.pi / 2, 181)),
            "Jmin_on_grid": min(Jfun(x) for x in np.linspace(-np.pi / 2, np.pi / 2, 181)), "J(0)": Jfun(0.0)}


def sec_jensen():
    # B(xi,ze) = E_{u,u' in [-1,1]} |cos((u xi + u' ze)/2)| J((u xi - u' ze)/2)   (heuristic limit of the averaged bound)
    def B(xi, ze, m=40):
        g, wts = np.polynomial.legendre.leggauss(m)
        tot = 0.0
        if ze == 0.0:
            for u, wu in zip(g, wts):
                tot += wu * abs(np.cos(u * xi / 2)) * Jfun(u * xi / 2)
            return tot / 2
        for u, wu in zip(g, wts):
            for up, wup in zip(g, wts):
                tot += wu * wup * abs(np.cos((u * xi + up * ze) / 2)) * Jfun((u * xi - up * ze) / 2)
        return tot / 4
    rows = []
    for (xi, ze) in ((0.25, 0.0), (0.5, 0.5), (1.0, 0.0), (1.0, 1.0), (2.0, 0.0), (2.0, 2.0), (4.0, 0.0), (3.0, 1.0), (8.0, 0.0), (6.0, 6.0), (16.0, 0.0)):
        n = 200; M = n + 2
        lam = lam_angles(n, max(xi, 1e-3) / M, max(ze, 1e-3) / M) / M ** 2
        rows.append({"xi": xi, "ze": ze, "B": B(xi, ze, m=24 if ze else 80), "Ltop": Ltop(max(xi, 1e-3), max(ze, 1e-3)), "lam_200/M^2": lam})
    return {"rows": rows, "B_lt_cstar_all": all(r["B"] < CSTAR for r in rows), "B_ge_Ltop_all": all(r["B"] >= r["Ltop"] - 2e-3 for r in rows)}


def sec_ucoef():
    def U_all(x, n):
        u = np.empty((n + 1,) + x.shape); u[0] = 1.0
        if n >= 1: u[1] = 2 * x
        for i in range(2, n + 1): u[i] = 2 * x * u[i - 1] - u[i - 2]
        return u
    bad = []
    sample = {}
    for n in range(2, 122, 2):
        M = n + 2; N = M * (M + 1)
        p, q = node_arrays(M)
        w = np.pi * p / M; v = np.pi * q / (M + 1)
        x = np.cos(w); y = np.cos(v)
        om = 8 * np.sin(w) ** 2 * np.sin(v) ** 2 / N
        Ux = U_all(x, n); Uy = U_all(y, n)
        j1 = np.arange(n + 1) + 1.0
        cumy = np.cumsum(j1[:, None] * Uy, axis=0); cumx = np.cumsum(j1[:, None] * Ux, axis=0)
        K = sum(j1[i] * Ux[i] * cumy[n - i] for i in range(n + 1))
        s = np.sign(om * K)
        c = np.array([(s * om * Ux[i] * cumy[n - i]).sum() for i in range(n + 1)])
        cp = np.array([(s * om * Uy[j] * cumx[n - j]).sum() for j in range(n + 1)])
        bx = c.copy(); bx[n] += 1.0; bx /= 2            # b_i = (c_i + delta_{in})/2
        by = cp.copy(); by[0] += n + 1.0; by /= 2       # b'_j = (c'_j + (n+1) delta_{j0})/2
        if bx.min() <= 0 or by.min() <= 0:
            bad.append(n)
        if n in (10, 40, 120):
            sample[n] = {"min b_i": float(bx.min()), "min b'_j": float(by.min()), "c_n": float(c[n]), "c'_0": float(cp[0]), "c_0": float(c[0]), "c'_1": float(cp[1])}
    return {"even n <= 120 with some band coefficient <= 0": bad, "samples": sample}


def main():
    secs = [a for a in sys.argv[1:] if not a.startswith("--") and not a.startswith("/")]
    allsecs = {"transl": sec_transl, "farfield": sec_farfield, "dlimit": sec_dlimit, "shift": sec_shift, "jensen": sec_jensen, "ucoef": sec_ucoef}
    if not secs:
        secs = list(allsecs)
    out = "/tmp/x2r3/x2r3_checks.json"
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    res = {"script": "code/mp/research/x2r3_checks.py", "label": "MEASURED (float64/mpmath); not certificates"}
    for s in secs:
        t0 = time.time()
        res[s] = allsecs[s]()
        res[s]["wall_seconds"] = round(time.time() - t0, 1)
        print("==", s); print(json.dumps(res[s], indent=1, default=str))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1, default=str)
    print("wrote", out)


if __name__ == "__main__":
    main()
