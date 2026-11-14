#!/usr/bin/env python3
"""C4C numerical checks (MEASURED; double precision, finite random/grid scope)
of finite-row statements in companion comparison-unified.tex L1990-4020.
Rows are built from the regular-sample identity of L1557-1560 (checked
against its rational form) with C_+-(v) from uc:row-profile."""
import numpy as np
rng = np.random.default_rng(4020)
worst = {}


def upd(k, v):
    worst[k] = max(worst.get(k, -np.inf), float(v))


def setup(n, x, y):
    m = n + 1
    rho = x + y
    ce, cd = np.cos(rho / 2), np.cos((x - y) / 2)
    return dict(n=n, m=m, x=x, y=y, a=ce * cd, ce=ce, cd=cd, p=np.sin(x), q=np.sin(y),
                L=np.log(n), H=np.sum(1.0 / np.arange(1, n + 1)))


def row_vals(S, r):
    n, m, x, y, a, p, q = (S[k] for k in "n m x y a p q".split())
    v = (r * np.pi + y) / m
    dl = (1 - r) % 2
    u = (dl * np.pi + x + 2 * np.pi * np.arange(n)) / n
    Cm = (p - q - 2 * a / np.tan(v / 2)) / 4
    Cp = (p + q + 2 * a / np.tan(v / 2)) / 4
    val = Cm / np.tan((u - v) / 2) + Cp / np.tan((u + v) / 2)
    rat = (a * (1 + np.cos(v)) - (p / 2) * np.sin(u) + (q / 2) * np.sin(v)) / (np.cos(u) - np.cos(v))
    return val, rat, v


def sinc(t):
    return np.sinc(t / np.pi)


def tau(t):
    t = np.asarray(t, float)
    out = np.ones_like(t)
    nz = np.abs(t) > 1e-12
    out[nz] = t[nz] / np.tan(t[nz])
    return out


def ell(S, r, b):
    a, x = S["a"], S["x"]
    w = r * np.pi + b
    js = np.arange(-r + 1, r, 2)
    return np.sin(b) / w + 8 * a * np.sum(1 / (w ** 2 - (js * np.pi + x) ** 2))


charts = {(1, +1): 1, (1, -1): -1, (2, -1): -2}  # (r, sign of b) -> actual row offset


def actual_row_index(S, r, sb):
    m = S["m"]
    return r if sb > 0 else 2 * m - r


def sinc_row(S, r, b):
    n, m, x = S["n"], S["m"], S["x"]
    mu = n / m
    w = r * np.pi + b
    v = w / m
    par = (1 - r) % 2
    start = -n if (-n - par) % 2 == 0 else -n + 1
    js = np.arange(start, n + 2, 2)
    js = js[(js * np.pi + x) / n < np.pi]
    js = js[(js * np.pi + x) / n >= -np.pi]
    z = js * np.pi + x
    u = z / n
    ce, cd = np.cos((x + b) / 2), np.cos((x - b) / 2)
    sm = np.where(((r - js - 1) // 2) % 2 == 0, 1.0, -1.0)
    spp = np.where(((js + r - 1) // 2) % 2 == 0, 1.0, -1.0)
    F = (ce * sm * sinc((z - mu * w) / 2) * tau((u - v) / 2)
         + cd * spp * sinc((z + mu * w) / 2) * tau((u + v) / 2)) / (2 * m * np.sin(w / (2 * m)))
    return js, z, F


def e_formula(S, r, b, P):
    n, m, x, a, p = S["n"], S["m"], S["x"], S["a"], S["p"]
    mu = n / m
    w = r * np.pi + b
    v = w / m
    tot = -a / m + np.sin(b) / w * (tau(np.array([v / 2]))[0] - 1)
    for j in P:
        z = j * np.pi + x
        u = z / n
        Dh = mu ** 2 * w ** 2 - z ** 2
        Dp = w ** 2 - z ** 2
        K = sinc((abs(u) + v) / 2) * sinc((abs(u) - v) / 2)
        Hh = (1 + np.cos(v)) / (2 * K)
        g = -p * np.sin(u) + np.sin(b) * np.sin(v)
        tot += 8 * a * (mu / Dh - 1 / Dp) + 8 * mu * a * (Hh - 1) / Dh + 2 * mu * g / (Dh * K)
    return tot


Pos = {(1, 1): [0], (1, -1): [0], (2, -1): [-1, 1]}

for n in (32, 33, 47, 64, 160, 161, 512):
    for trial in range(120):
        # full triangle interior
        x = rng.uniform(0, np.pi)
        y = rng.uniform(0, np.pi - x)
        if trial % 3 == 0:  # concentrate near rho<=1
            x = rng.uniform(0, 1); y = rng.uniform(0, 1 - x)
        S = setup(n, x, y)
        n_, m = S["n"], S["m"]
        rho = x + y
        # rational form vs cot form
        for r in (0, 1, 2, m - 1, m, 2 * m - 2, 2 * m - 1, 5):
            val, rat, _ = row_vals(S, r)
            upd("cot form vs rational form (rel)", np.max(np.abs(val - rat) / (1 + np.abs(rat))))
        # signed sums and sinc-row agreement for the three charts
        for (r, sb) in ((1, 1), (1, -1), (2, -1)):
            b = sb * y
            w = r * np.pi + b
            idx = actual_row_index(S, r, sb)
            val, _, v_act = row_vals(S, idx)
            js, z, F = sinc_row(S, r, b)
            upd("sinc-row multiset vs actual row (sorted, max abs)",
                np.max(np.abs(np.sort(F) - np.sort(val / (n_ * m)))))
            signed = val.sum() / (n_ * m)
            pred = S["a"] / m - np.sin(b) / w * tau(np.array([w / (2 * m)]))[0]
            upd("signed row sum a/m - sin b tau/w (abs err)", abs(signed - pred))
            # positive samples and e_r on rho<=1
            if rho <= 1:
                pos = js[F > 0]
                upd("positive set != expected (count)", 0 if sorted(pos.tolist()) == Pos[(r, sb)] else 1)
                e_act = np.abs(val).sum() / (n_ * m) - ell(S, r, b)
                upd("e_r identity (abs err)", abs(e_act - e_formula(S, r, b, Pos[(r, sb)])))
        # closest row
        val0, _, v0 = row_vals(S, 0)
        R0 = np.abs(val0).sum() / (n_ * m)
        sg0 = val0.sum() / (n_ * m)
        upd("closest signed = a/m - sinc y tau(y/2m)", abs(sg0 - (S["a"] / m - sinc(y) * tau(np.array([y / (2 * m)]))[0])))
        bound0 = (2 + S["H"] / np.pi) / m + np.pi ** 2 / (24 * m ** 2)
        upd("closest |R0/(nm)-sinc y| / bound", abs(R0 - sinc(y)) / bound0)
        if rho <= 1:
            upd("closest row positive count on rho<=1 (after sign reversal: count of val0>0)", np.sum(val0 > 0))
        # J_end - C2 absolute bound
        Jend = (np.abs(row_vals(S, 0)[0]).sum() + np.abs(row_vals(S, 1)[0]).sum()
                + np.abs(row_vals(S, 2 * m - 1)[0]).sum() + np.abs(row_vals(S, 2 * m - 2)[0]).sum()) / (n_ * m)
        C2 = sinc(y) + ell(S, 1, y) + ell(S, 1, -y) + ell(S, 2, -y)
        bJ = (9 + 21 * S["a"] + ((1 + 48 * S["p"]) * S["H"] + 24 * S["q"]) / np.pi) / n_ + (317 + 5 / 12) / n_ ** 2
        upd("|J_end - C2| / bound (full triangle)", abs(Jend - C2) / bJ)
        # central rows
        for r in (m - 1, m):
            Rr = np.abs(row_vals(S, r)[0]).sum()
            upd("central R_r/n / (L+6)", (Rr / n_) / (S["L"] + 6))
        Jc = (np.abs(row_vals(S, m - 1)[0]).sum() + np.abs(row_vals(S, m)[0]).sum()) / (n_ * m)
        upd("J_cen / ((12+2L)/n)", Jc / ((12 + 2 * S["L"]) / n_))

# origin-sample constants (L2860-2863) for n in [32, 2e4]
for n in list(range(32, 400)) + [512, 1000, 5000, 20000]:
    m = n + 1; mu = n / m
    sD = 0; mxH = 0; mnK = 9
    for (w, z) in ((np.pi, 0), (np.pi, 0), (2 * np.pi, np.pi), (2 * np.pi, -np.pi)):
        u, v = z / n, w / m
        K = sinc((abs(u) + v) / 2) * sinc((abs(u) - v) / 2)
        Hh = (1 + np.cos(v)) / (2 * K)
        Dh = mu ** 2 * w ** 2 - z ** 2
        sD += 1 / Dh; mxH = max(mxH, abs(Hh - 1) * n * n); mnK = min(mnK, K)
    upd("origin: max n^2|H_h-1| / 19", mxH / 19)
    upd("origin: (49/50)/min K", (49 / 50) / mnK)
    upd("origin: sum D_h^-1 / (25/54)", sD / (25 / 54))

# wide-domain constants (L3349-3359, 3386-3391)
for n in (32, 33, 64, 160, 512):
    m = n + 1; mu = n / m
    for trial in range(400):
        x = rng.uniform(0, 1); y = rng.uniform(0, 1 - x); rho = x + y
        if rho == 0:
            continue
        P = np.sin(x) + np.sin(y)
        sumD = 0
        for (r, sb, j) in ((1, 1, 0), (1, -1, 0), (2, -1, -1), (2, -1, 1)):
            def quant(lam):
                xx, yy = lam * x, lam * y
                b = sb * yy
                w = r * np.pi + b; v = w / m; z = j * np.pi + xx; u = z / n
                K = sinc((abs(u) + v) / 2) * sinc((abs(u) - v) / 2)
                Hh = (1 + np.cos(v)) / (2 * K)
                Dh = mu ** 2 * w ** 2 - z ** 2
                g = -np.sin(xx) * np.sin(u) + np.sin(b) * np.sin(v)
                prods = [1 / ((mu * w - z) * (w - z)), 1 / ((mu * w + z) * (w + z))]
                ks = [r - j, r + j]
                return K, Hh, Dh, g, prods, ks, w, z
            K, Hh, Dh, g, prods, ks, w, z = quant(1.0)
            eps = 1e-6
            K2, Hh2, Dh2, g2, prods2, _, _, _ = quant(1 - eps)
            dH = abs(Hh - Hh2) / eps
            dDi = abs(1 / Dh - 1 / Dh2) / eps
            upd("wide: K>=49/50 ratio (49/50)/K", (49 / 50) / K)
            upd("wide: n^2|H_h-1|/19", n * n * abs(Hh - 1) / 19)
            upd("wide: |dH_h/dlam|/(5 rho/n^2)", dH / (5 * rho / n ** 2))
            upd("wide: |d(1/Dh)|/((20/19) rho/Dh)", dDi / ((20 / 19) * rho / Dh))
            upd("wide: |g_j|/(7P/n)", abs(g) / (7 * P / n))
            for pr, pr2, k in zip(prods, prods2, ks):
                upd("wide: product derivative/((25760/104329) rho/k^3)", (abs(pr - pr2) / eps) / ((25760 / 104329) * rho / k ** 3))
            upd("wide: w-z>=(17/8)k", max((17 / 8) * ks[0] - (w - z), (17 / 8) * ks[1] - (w + z)))
            upd("wide: mu w-z>=(19/10)k", max((19 / 10) * ks[0] - (mu * w - z), (19 / 10) * ks[1] - (mu * w + z)))
            sumD += 1 / Dh
        upd("wide: sum D_h^-1/(800/1083)", sumD / (800 / 1083))
        # central-row coefficient errors (L3484-3497)
        ce, cd = np.cos(rho / 2), np.cos((x - y) / 2); a = ce * cd
        c = np.cos(y / (2 * m))
        upd("row m: |A+B-a|/(a rho^2/6)", abs((ce + cd) / (2 * c) - a) / (a * rho ** 2 / 6))
        c1, c0 = np.cos((np.pi - y) / (2 * m)), np.cos(np.pi / (2 * m))
        A, B, A0 = ce / (2 * c1), cd / (2 * c1), 1 / (2 * c0)
        bnd = a * rho ** 2 / 13 + a * y / m ** 2
        upd("row m-1: |A-aA0|/bound", abs(A - a * A0) / bnd)
        upd("row m-1: |B-aB0|/bound", abs(B - a * A0) / bnd)
        upd("(c_e+c_d)/(2c) <= 8a/(7c)", ((ce + cd) / 2) / (8 * a / 7))
        upd("2a-P>=17/32 (17/32-(2a-P))", 17 / 32 - (2 * a - P))

for k in sorted(worst):
    print(f"{k:70s} {worst[k]: .4e}")
