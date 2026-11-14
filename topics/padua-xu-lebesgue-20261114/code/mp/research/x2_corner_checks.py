#!/usr/bin/env python3
"""X2 round 2 (corner values of the Morrow-Patterson Lebesgue function): numerical checks.

MEASURED checks only; nothing here is a proof.  Self-contained (mpmath + numpy), no import of other topic code.

Sections (run all by default, or name them):  ident  cstar  decomp  table
  ident  : mpmath (40 digits) checks of the identities of theory/X2-21..X2-23
           (discrete orthonormality, corner kernel, four corner closed forms, lambda(+-1,-1) = n+1,
            band / one-sum / hyperbolic forms of lambda(1,1)), and inclusion in evidence/mp-cmp-certificate.json.
  cstar  : the constant c* of theory/X2-25 by two independent evaluations; antiderivative check;
           scan of |h''| <= 68/15; numerical total variation of hhat' against the bound used in the proof.
  decomp : float64 check of every per-node inequality and every block sum used in the proof of X2-25.
  table  : R_n = lambda_n(1,1) + (n+1) - c*(n+5/2)^2 for a list of even n and the proved bounds.

Usage:  python3 x2_corner_checks.py [sections...] [--out /tmp/x2r2/x2_corner_checks.json]
"""
import sys, json, os, math, time
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(HERE, "..", "..", "..", "evidence", "mp-cmp-certificate.json")
CSTAR_STR = "0.516953653366806272706422282045"   # value produced by section cstar (printed there again)


# ------------------------------------------------------------------ nodes
def nodes_mq(n):
    """MP nodes as (m, q): w = m*pi/(n+2), v = q*pi/(n+3), q = 2k (m odd) or 2k-1 (m even)."""
    out = []
    for m in range(1, n + 2):
        for k in range(1, n // 2 + 2):
            out.append((m, 2 * k if m % 2 else 2 * k - 1))
    return out


def U_list(x, n):
    u = [mp.mpf(1), 2 * x]
    for i in range(2, n + 1):
        u.append(2 * x * u[-1] - u[-2])
    return u[:n + 1]


# ------------------------------------------------------------------ section ident
def sec_ident(res):
    mp.mp.dps = 40
    half = mp.mpf(1) / 2
    out = {}
    # (a) discrete orthonormality (Lemma 0 of X2-21)
    worst = mp.mpf(0)
    for n in (2, 4, 6):
        M = n + 2; N = M * (M + 1)
        idx = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
        nd = nodes_mq(n)
        assert len(nd) == len(idx) == (n + 1) * (n + 2) // 2
        rows = []
        for (m, q) in nd:
            w = mp.pi * m / M; v = mp.pi * q / (M + 1)
            om = 8 * mp.sin(w) ** 2 * mp.sin(v) ** 2 / N
            Ux, Uy = U_list(mp.cos(w), n), U_list(mp.cos(v), n)
            rows.append((om, [Ux[i] * Uy[j] for (i, j) in idx]))
        for a in range(len(idx)):
            for b in range(a, len(idx)):
                s = mp.fsum(om * r[a] * r[b] for (om, r) in rows)
                worst = max(worst, abs(s - (1 if a == b else 0)))
    out["orthonormality_max_err_n2_4_6"] = mp.nstr(worst, 5)

    # (b) corner kernel G_n(x,y) = (1/4)[(F'(x)+F'(y))/(x-y)^2 - 2(F(x)-F(y))/(x-y)^3]
    def G_direct(n, x, y):
        Ux, Uy = U_list(x, n), U_list(y, n)
        return mp.fsum((i + 1) * (j + 1) * Ux[i] * Uy[j] for i in range(n + 1) for j in range(n + 1 - i))

    def G_closed(n, x, y):
        M = n + 2
        T = lambda t, k: mp.cos(k * mp.acos(t))
        Uu = lambda t, k: mp.sin((k + 1) * mp.acos(t)) / mp.sin(mp.acos(t))
        F = lambda t: T(t, M + 1) + T(t, M)
        Fp = lambda t: (M + 1) * Uu(t, M) + M * Uu(t, M - 1)
        return (Fp(x) + Fp(y)) / (4 * (x - y) ** 2) - (F(x) - F(y)) / (2 * (x - y) ** 3)

    rng = np.random.default_rng(20261114)
    worst = mp.mpf(0)
    for n in (2, 3, 4, 7, 10, 15):
        for _ in range(5):
            x, y = [mp.mpf(float(t)) for t in rng.uniform(-0.99, 0.99, 2)]
            d, c = G_direct(n, x, y), G_closed(n, x, y)
            worst = max(worst, abs(d - c) / (1 + abs(d)))
    out["corner_kernel_max_rel_err"] = mp.nstr(worst, 5)

    # (c) closed forms of l_{m,k} at the four vertices, sign pattern, lambda values
    rows = []
    worst = mp.mpf(0)
    cert = {}
    if os.path.exists(CERT):
        for r in json.load(open(CERT))["rows"]:
            cert[r["n"]] = r["lambda"]
    cert_ok = True
    for n in (2, 4, 6, 8, 10, 12, 16, 20, 24, 30):
        M = n + 2; N = M * (M + 1)
        kap = mp.mpf(2 * M + 3) / (2 * M - 1)
        lam = {"11": 0, "m11": 0, "1m": 0, "mm": 0}
        band = mp.mpf(0); signed11 = mp.mpf(0); nband = 0; sign_ok = True
        for (m, q) in nodes_mq(n):
            w = mp.pi * m / M; v = mp.pi * q / (M + 1); x = mp.cos(w); y = mp.cos(v)
            om = 8 * mp.sin(w) ** 2 * mp.sin(v) ** 2 / N
            s = (-1) ** m
            c11 = om * s * ((2 * M + 1) / (4 * (x - y) ** 2) - (2 + x + y) / (2 * (x - y) ** 3))
            cm1 = om * s * ((2 * M + 1) / (4 * (x + y) ** 2) + (2 - x + y) / (2 * (x + y) ** 3))
            c1m = -om * s / (4 * (x + y) ** 2)
            cmm = -om * s / (4 * (x - y) ** 2)
            if n <= 12:   # compare with the defining kernel sums
                worst = max(worst, abs(om * G_direct(n, x, y) - c11), abs(om * G_direct(n, -x, y) - cm1),
                            abs(om * G_direct(n, x, -y) - c1m), abs(om * G_direct(n, -x, -y) - cmm))
            X = (1 + x) / 2; Y = (1 + y) / 2
            cXY = s * 16 * X * (1 - X) * Y * (1 - Y) * ((M - half) * X - (M + 3 * half) * Y) / (N * (X - Y) ** 3)
            u = mp.log(X / Y) / 2
            chyp = s * (mp.mpf(2) / N) * (1 - X) * (1 - Y) * ((2 * M + 1) * mp.sinh(u) - 2 * mp.cosh(u)) / mp.sinh(u) ** 3
            worst = max(worst, abs(c11 - cXY), abs(c11 - chyp))
            inband = (Y < X) and (X < kap * Y)
            sign_ok &= (mp.sign(c11) == (-s if inband else s))
            if inband:
                band += abs(c11); nband += 1
            signed11 += s * c11
            lam["11"] += abs(c11); lam["m11"] += abs(cm1); lam["1m"] += abs(c1m); lam["mm"] += abs(cmm)
        one = mp.mpf(0)   # one-sum formula
        for r in range(1, N):
            Xr = mp.sin(mp.pi * r / (2 * M)) ** 2; Yr = mp.sin(mp.pi * r / (2 * M + 2)) ** 2
            if r % M == 0 or r % (M + 1) == 0:
                continue
            one += abs(Xr * (1 - Xr) * Yr * (1 - Yr) * ((M - half) * Xr - (M + 3 * half) * Yr) / (Xr - Yr) ** 3)
        one = 8 * one / N
        row = {"n": n, "lam11": mp.nstr(lam["11"], 30), "lam(-1,1)-lam11": mp.nstr(lam["m11"] - lam["11"], 3),
               "lam(1,-1)-(n+1)": mp.nstr(lam["1m"] - (n + 1), 3), "lam(-1,-1)-(n+1)": mp.nstr(lam["mm"] - (n + 1), 3),
               "band_formula-lam11": mp.nstr(-(n + 1) + 2 * band - lam["11"], 3),
               "one_sum-lam11": mp.nstr(one - lam["11"], 3),
               "sum_signed+(n+1)": mp.nstr(signed11 + (n + 1), 3), "n_band": nband, "sign_pattern_ok": bool(sign_ok)}
        if n in cert:
            # the path-A enclosures have width ~1e-45, below the 40-digit working precision here:
            # report the distance to the enclosure (0 if inside) and accept <= 1e-33 as agreement
            lo, hi = [mp.mpf(t) for t in cert[n]["(1,1)"]]
            dist = max(lo - lam["11"], lam["11"] - hi, mp.mpf(0))
            lo2, hi2 = [mp.mpf(t) for t in cert[n]["(1,-1)"]]
            row["dist_to_pathA_enclosure_(1,1)"] = mp.nstr(dist, 3)
            row["pathA_(1,-1)_contains_n+1"] = bool(lo2 <= n + 1 <= hi2)
            cert_ok &= bool(dist <= mp.mpf("1e-33")) and row["pathA_(1,-1)_contains_n+1"]
        rows.append(row)
    out["closed_forms_max_abs_err"] = mp.nstr(worst, 5)
    out["rows"] = rows
    out["agrees_with_pathA_certificate_to_1e-33"] = cert_ok
    res["ident"] = out
    print("ident:", json.dumps({k: v for k, v in out.items() if k != "rows"}))
    for r in rows:
        print("  ", r)


# ------------------------------------------------------------------ section cstar
def Phi(t):
    """antiderivative of sin(2t) * d/dt (sin t / t)^2  ( = -htilde )."""
    t = mp.mpf(t)
    return mp.sin(2 * t) * mp.sin(t) ** 2 / t ** 2 + 2 * mp.cos(2 * t) * mp.sin(t) ** 2 / t + 2 * mp.si(2 * t) - 2 * mp.si(4 * t)


def htilde(t):
    t = mp.mpf(t)
    return mp.sin(2 * t) ** 2 * (mp.tan(t) - t) / t ** 3


def root_a(j):
    """root of tan t = t in (j*pi, j*pi+pi/2), j >= 1."""
    x0 = j * mp.pi + mp.pi / 2 - 1 / (j * mp.pi + mp.pi / 2)
    return mp.findroot(lambda t: mp.sin(t) - t * mp.cos(t), x0)


def sec_cstar(res):
    mp.mp.dps = 40
    out = {}
    # series  c* = (4/pi) sum_{j>=0} [Phi(a_j) - Phi(b_j)],  a_0 = 0, b_j = j pi + pi/2
    J = 60
    terms = [-Phi(mp.pi / 2)]
    for j in range(1, J + 1):
        terms.append(Phi(root_a(j)) - Phi(j * mp.pi + mp.pi / 2))
    part = 4 / mp.pi * mp.fsum(terms)
    tail_bound = 2 / (mp.pi ** 6 * mp.mpf(J) ** 4)            # proved tail bound (X2-25, Lemma C)
    # Richardson-free second evaluation: direct quadrature of the positive part on each bump
    quad = mp.quad(htilde, [0, mp.pi / 4, mp.pi / 2])
    for j in range(1, 13):
        quad += mp.quad(htilde, [root_a(j), j * mp.pi + mp.pi / 2])
    quad = 4 / mp.pi * quad
    out["c0_first_bump"] = mp.nstr(4 / mp.pi * terms[0], 30)
    out["c0_closed_form"] = mp.nstr(16 / mp.pi ** 2 - 8 / mp.pi * (mp.si(mp.pi) - mp.si(2 * mp.pi)), 30)
    out["cstar_partial_J60"] = mp.nstr(part, 32)
    out["tail_bound_J60"] = mp.nstr(tail_bound, 5)
    out["cstar_quad_12_bumps"] = mp.nstr(quad, 20)
    out["quad_tail_bound_J12"] = mp.nstr(2 / (mp.pi ** 6 * mp.mpf(12) ** 4), 5)
    # accelerated full value (mp.nsum on the tail) -- reference value used elsewhere in this file
    full = 4 / mp.pi * (terms[0] + mp.nsum(lambda j: Phi(root_a(int(j))) - Phi(int(j) * mp.pi + mp.pi / 2), [1, mp.inf]))
    out["cstar_nsum"] = mp.nstr(full, 32)
    out["cstar_minus_CSTAR_STR"] = mp.nstr(full - mp.mpf(CSTAR_STR), 5)
    out["term_j_times_j^5_over_bound"] = [mp.nstr(4 / mp.pi * terms[j] * j ** 5 / (8 / mp.pi ** 6), 6) for j in (1, 2, 5, 20, 60)]
    # (2/pi) int |htilde| equals c*  (uses int htilde = 0):  Phi(0+) = 0 = Phi(inf)
    out["Phi(1e-10)"] = mp.nstr(Phi(mp.mpf("1e-10")), 5)
    out["Phi(1e6)"] = mp.nstr(Phi(mp.mpf(10) ** 6), 5)
    # antiderivative check  Phi' = -htilde
    worst = mp.mpf(0)
    for t in (0.3, 1.0, 1.4, 2.5, 4.6, 7.9, 20.3):
        worst = max(worst, abs(mp.diff(Phi, t) + htilde(t)))
    out["max|Phi'+htilde|"] = mp.nstr(worst, 5)
    # |htilde''| <= 68/15 (float scan) and numerical TV of hhat' against T2 <= 9.012
    mp.mp.dps = 20
    tt = np.linspace(1e-3, 60.0, 600001)
    A = np.sin(2 * tt) - 0.5 * np.sin(4 * tt); A1 = 2 * np.cos(2 * tt) - 2 * np.cos(4 * tt); A2 = -4 * np.sin(2 * tt) + 8 * np.sin(4 * tt)
    B = (1 - np.cos(4 * tt)) / 2; B1 = 2 * np.sin(4 * tt); B2 = 8 * np.cos(4 * tt)
    h2 = A2 / tt ** 3 - 6 * A1 / tt ** 4 + 12 * A / tt ** 5 - B2 / tt ** 2 + 4 * B1 / tt ** 3 - 6 * B / tt ** 4
    sel = tt > 0.05                      # the explicit formula cancels badly near 0; h''(0) = 8/3
    out["max|h''|_on_[0.05,60]"] = float(np.max(np.abs(h2[sel])))
    out["bound_68/15"] = 68 / 15
    h1 = A1 / tt ** 3 - 3 * A / tt ** 4 - B1 / tt ** 2 + 2 * B / tt ** 3
    h0 = A / tt ** 3 - B / tt ** 2
    pos = h0 > 0
    hp = np.where(pos, h1, 0.0)[sel]
    out["numerical_TV_hhat'_on_[0.05,60]"] = float(np.sum(np.abs(np.diff(hp))))
    out["T2_bound"] = 9.0121
    res["cstar"] = out
    print("cstar:", json.dumps(out, indent=1))


# ------------------------------------------------------------------ section decomp
def decomp(M, cs):
    """All quantities of the proof of X2-25 for one even M = n+2 (float64, exact integer angle numerators)."""
    N = M * (M + 1)
    L = math.log(M)
    pp = np.arange(1, M, dtype=np.int64)[:, None]
    qq = np.arange(1, M + 1, dtype=np.int64)[None, :]
    mask = ((pp - qq) % 2 == 0) & (qq <= pp)
    P = np.broadcast_to(pp, mask.shape)[mask]; Q = np.broadcast_to(qq, mask.shape)[mask]
    r = P * (M + 1) - Q * M                 # b = pi r/(2N)
    s = P * (M + 1) + Q * M                 # 2 mu = pi s/(2N)
    j = (P - Q) // 2
    b = np.pi * r / (2.0 * N); mu = np.pi * s / (4.0 * N)
    t = np.pi * P / (2.0 * M); th = np.pi * Q / (2.0 * M + 2)
    sst = np.sin(t) * np.sin(th); cct = np.cos(t) * np.cos(th)
    sinhu = np.sin(2 * mu) * np.sin(b) / (2 * sst)
    coshu = np.sqrt(1 + sinhu ** 2)
    chi = (2 * coshu - (2 * M + 1) * sinhu) / sinhu ** 3
    term = (2.0 / N) * cct ** 2 * np.maximum(chi, 0)                 # [-A]_+
    S = (M + 0.5) * sinhu
    zp = lambda V: np.maximum(1 - V, 0) / V ** 3
    cM = (M + 0.5) ** 3 / N
    Mcal = 4 * cM * cct ** 2 * zp(S)
    eta = np.pi * (2 * M + 1) / (4.0 * N)
    taut = eta * r
    assert np.allclose(taut, j * np.pi + mu, rtol=0, atol=1e-9)
    Vh = taut / np.tan(mu)
    hhat = 4 * np.cos(mu) ** 4 * zp(Vh)
    Sstar = (1 - (M + 0.5) ** -2) ** -0.5
    eps_c = np.sin(b / 2) ** 2 / np.cos(mu) ** 2; eps_s = np.sin(b / 2) ** 2 / np.sin(mu) ** 2
    tol = 1e-9
    chk = {}
    chk["S>=Vhat"] = bool(np.all(S >= Vh * (1 - 1e-12)))
    chk["S<=Vhat/(1-eps_s)"] = bool(np.all(S <= Vh / (1 - eps_s) * (1 + 1e-12)))
    chk["eps_c<1,eps_s<1"] = bool(np.all(eps_c < 1) and np.all(eps_s < 1))
    chk["cct=cos^2mu(1-eps_c)"] = bool(np.allclose(cct, np.cos(mu) ** 2 * (1 - eps_c), rtol=1e-10, atol=1e-15))
    # upper chain
    e1 = term - Mcal
    e1_bound = (2.0 / M) * np.sin(mu) * np.cos(mu) ** 3 / taut * (taut < Sstar * np.tan(mu))
    chk["0<=e1<=bound"] = bool(np.all(e1 >= -tol) and np.all(e1 <= e1_bound + tol))
    chk["Mcal<=cM*hhat"] = bool(np.all(Mcal <= cM * hhat * (1 + 1e-12) + tol))
    # lower chain
    inb = Vh < 1
    Lc = 8 * cM * np.cos(mu) ** 4 * eps_c * zp(Vh)
    Ls = np.where(inb, 4 * cM * np.cos(mu) ** 4 * 3 * eps_s / ((1 - eps_s) * Vh ** 3), 0.0)
    chk["Mcal>=cM*hhat-Lc-Ls"] = bool(np.all(Mcal >= cM * hhat - Lc - Ls - tol))
    Lc_bound = np.where(taut < np.tan(mu), (2.0 / M) * np.sin(mu) ** 3 / (np.cos(mu) * taut), 0.0)
    Ls_bound = np.where(taut < np.tan(mu), (4.0 / M) * np.sin(mu) * np.cos(mu) / taut, 0.0)
    chk["Lc<=bound"] = bool(np.all(Lc <= Lc_bound + tol)); chk["Ls<=bound"] = bool(np.all(Ls <= Ls_bound + tol))
    chk["eps_s<1/4_on_Vh<1"] = bool(np.all(eps_s[inb] < 0.25))
    # sums and the proved block bounds
    E1 = float(e1.sum()); sLc = float(Lc.sum()); sLs = float(Ls.sum())
    E1_bd = 2.012; Ls_bd = 4.28; Lc_bd = 0.2026 * L * L + 1.0863 * L + 0.5504
    # Riemann part: full grid sum, node sum, missing part
    rr = np.arange(1, 40 * M * M + 1, dtype=np.float64)           # hhat is supported far below eta*r for these r
    tau_all = eta * rr
    jj = np.floor(tau_all / np.pi); mm = tau_all - jj * np.pi
    with np.errstate(divide="ignore", invalid="ignore"):
        h_all = np.where(mm < np.pi / 2, 4 * np.cos(mm) ** 4 * np.maximum(1 - tau_all / np.tan(mm), 0) / (tau_all / np.tan(mm)) ** 3, 0.0)
    h_all = np.nan_to_num(h_all)
    full = float(h_all.sum()); Sfrak = float(hhat.sum()); miss = full - Sfrak
    I = np.pi * cs / 4
    riem_full = full - I / eta
    T2 = 9.0121
    miss_bd = 1.1119 / (M + 1) + 0.4053 * (0.307 + L) / (M + 1) + 0.386 / M ** 3
    lam = -(M - 1) + 2 * float(term.sum())
    R = lam + (M - 1) - cs * (M + 0.5) ** 2
    chk["E1<=2.012"] = E1 <= E1_bd; chk["sumLs<=4.28"] = sLs <= Ls_bd; chk["sumLc<=bound"] = sLc <= Lc_bd
    chk["|riem_full|<=eta*T2/8"] = abs(riem_full) <= eta * T2 / 8 + 1e-7
    chk["0<=miss<=bound"] = (miss >= -1e-9) and (miss <= miss_bd)
    lower = -(0.4053 * L * L + 2.9833 * L + 15.82); upper = 7.66
    chk["lower<=R<=upper"] = (lower <= R <= upper)
    return {"M": M, "n": M - 2, "lam11": lam, "R": R, "proved_lower": lower, "proved_upper": upper,
            "E1": E1, "sum_Lc": sLc, "sum_Lc_bound": Lc_bd, "sum_Ls": sLs,
            "2cM*riem_full": 2 * cM * riem_full, "2cM*eta*T2/8": 2 * cM * eta * T2 / 8,
            "2cM*miss": 2 * cM * miss, "2cM*miss_bound": 2 * cM * miss_bd,
            "max_tau_tilde_in_support_seen": float(taut[hhat > 0].max()), "checks": chk,
            "all_checks": bool(all(chk.values()))}


def sec_decomp(res):
    cs = float(CSTAR_STR)
    rows = []
    for M in (4, 6, 8, 10, 12, 16, 22, 32, 52, 102, 202, 402, 802, 1202):
        d = decomp(M, cs)
        rows.append(d)
        print("decomp M=%d R=%.5f in [%.2f, %.2f]  E1=%.4f  Lc=%.4f(<=%.2f) Ls=%.4f  riem=%.4f(|.|<=%.3f) miss=%.4f(<=%.3f)  all=%s" % (
            M, d["R"], d["proved_lower"], d["proved_upper"], d["E1"], d["sum_Lc"], d["sum_Lc_bound"], d["sum_Ls"],
            d["2cM*riem_full"], d["2cM*eta*T2/8"], d["2cM*miss"], d["2cM*miss_bound"], d["all_checks"]))
        if not d["all_checks"]:
            print("   FAILED:", [k for k, v in d["checks"].items() if not v])
    res["decomp"] = rows


# ------------------------------------------------------------------ section table
def lam11_band(M):
    """lambda_n(1,1) = -(M-1) + 2 * sum over nodes with theta < t of [-A]_+   (float64)."""
    N = M * (M + 1)
    tot = 0.0
    for P in range(1, M):
        Q = np.arange(2 - (P % 2), P + 1, 2, dtype=np.int64)       # q' <= p', same parity
        r = P * (M + 1) - Q * M; s = P * (M + 1) + Q * M
        b = np.pi * r / (2.0 * N); two_mu = np.pi * s / (2.0 * N)
        t = np.pi * P / (2.0 * M); th = np.pi * Q / (2.0 * M + 2)
        X = math.sin(t) ** 2; Y = np.sin(th) ** 2
        D = np.sin(two_mu) * np.sin(b)                               # X - Y
        val = 16 * X * (1 - X) * Y * (1 - Y) * ((M + 1.5) * Y - (M - 0.5) * X) / (N * D ** 3)
        tot += float(np.sum(np.maximum(val, 0.0)))
    return -(M - 1) + 2 * tot


def sec_table(res):
    cs = float(CSTAR_STR)
    rows = []
    for n in (2, 4, 6, 8, 10, 20, 30, 50, 100, 200, 400, 800, 1600, 3200, 6400):
        M = n + 2; L = math.log(M)
        lam = lam11_band(M)
        R = lam + (n + 1) - cs * (n + 2.5) ** 2
        rows.append({"n": n, "lam11": float("%.12g" % lam), "lam/n^2": lam / n ** 2, "lam/dim": lam / ((n + 1) * (n + 2) / 2),
                     "R_n": R, "R_n/log^2(n+2)": R / L ** 2, "proved_lower": -(0.4053 * L * L + 2.9833 * L + 15.82), "proved_upper": 7.66})
        print("table n=%5d lam=%.9g lam/n^2=%.6f lam/dim=%.6f R_n=%.5f R/log^2=%.4f" % (n, lam, lam / n ** 2, rows[-1]["lam/dim"], R, R / L ** 2))
    res["table"] = rows


def main():
    argv = sys.argv[1:]
    out = "/tmp/x2r2/x2_corner_checks.json"
    if "--out" in argv:
        k = argv.index("--out")
        out = argv[k + 1]
        argv = argv[:k] + argv[k + 2:]
    args = [a for a in argv if not a.startswith("--")]
    secs = args or ["ident", "cstar", "decomp", "table"]
    res = {"script": "code/mp/research/x2_corner_checks.py", "command": "python3 " + " ".join(sys.argv),
           "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "mpmath": mp.__version__},
           "label": "MEASURED checks; not proofs"}
    t0 = time.time()
    for sname in secs:
        {"ident": sec_ident, "cstar": sec_cstar, "decomp": sec_decomp, "table": sec_table}[sname](res)
        print("  [%s done, %.1fs]" % (sname, time.time() - t0), flush=True)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1, default=str)
    print("wrote", out)


if __name__ == "__main__":
    main()
