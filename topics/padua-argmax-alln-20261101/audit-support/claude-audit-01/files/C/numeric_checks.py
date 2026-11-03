"""Auditor's independent MEASURED (float64 / mpmath) checks for theorems 07, 08, 10, 12, 13.

Nothing here is a proof.  Independent implementation:
  * cardinals by direct Vandermonde inversion in the Chebyshev tensor basis;
  * kernel G_n by the rhombus cosine sum with corrected (n,0) mode, cross-validated
    against both the divided-difference form of PD-T185 and the Vandermonde cardinals.
"""
import json
import math
import sys
import time
import numpy as np
import mpmath as mp

PI = math.pi
rng = np.random.default_rng(20261102)


# ---------------------------------------------------------------- basics
def nodes(n):
    m = n + 1
    return [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]


def weights(n):
    m = n + 1
    w = {}
    for j, k in nodes(n):
        e = .5 if j in (0, n) else 1.
        f = .5 if k in (0, m) else 1.
        w[(j, k)] = 2 * e * f / (n * m)
    return w


def cheb(x, N):
    x = np.asarray(x, float)
    out = np.empty((N + 1,) + x.shape)
    out[0] = 1.
    if N >= 1:
        out[1] = x
    for p in range(2, N + 1):
        out[p] = 2 * x * out[p - 1] - out[p - 2]
    return out


def vandermonde_cardinals(n):
    """Return coefficient matrix A (basis x nodes) with L_B = sum_pq A[pq,B] T_p T_q."""
    m = n + 1
    nd = nodes(n)
    basis = [(p, q) for p in range(n + 1) for q in range(n + 1 - p)]
    xs = np.array([math.cos(j * PI / n) for j, k in nd])
    ys = np.array([math.cos(k * PI / m) for j, k in nd])
    TX, TY = cheb(xs, n), cheb(ys, n)
    V = np.array([[TX[p, i] * TY[q, i] for (p, q) in basis] for i in range(len(nd))])
    A = np.linalg.inv(V)
    return nd, basis, A, np.linalg.cond(V)


def cardinals_at(n, card, x, y):
    nd, basis, A, _ = card
    TX, TY = cheb(np.atleast_1d(x), n), cheb(np.atleast_1d(y), n)
    phi = np.array([TX[p] * TY[q] for (p, q) in basis])     # basis x points
    return A.T @ phi                                         # nodes x points


def coef_matrix(n):
    h = np.where(np.arange(n + 1) == 0, 1., 2.)
    C = np.outer(h, h) * ((np.arange(n + 1)[:, None] + np.arange(n + 1)[None, :]) <= n)
    C[n, 0] = 1.
    return C


def G_rhombus(n, u, v, C=None):
    """Corrected kernel at angle arrays u, v (same shape)."""
    if C is None:
        C = coef_matrix(n)
    a = np.arange(n + 1)
    u = np.atleast_1d(u).ravel()
    v = np.atleast_1d(v).ravel()
    return np.einsum('ip,pq,iq->i', np.cos(np.outer(u, a)), C, np.cos(np.outer(v, a)))


def G_divdiff(n, u, v):
    """PD-T185 form: (P(cos v)-P(cos u))/(cos v-cos u) - cos(n u), P=T_{n+1}+T_n (mpmath)."""
    x, y = mp.cos(u), mp.cos(v)
    P = lambda z: mp.chebyt(n + 1, z) + mp.chebyt(n, z)
    if abs(y - x) < mp.mpf(10) ** (-30):
        dP = mp.diff(P, x)
        D = dP
    else:
        D = (P(y) - P(x)) / (y - x)
    return D - mp.cos(n * u)


def lam_kernel(n, th, ph, C=None):
    """lambda, S (majorant) via four-copy kernel identity of theorem 01."""
    m = n + 1
    nd = nodes(n)
    w = weights(n)
    J = np.array([j for j, k in nd])
    K = np.array([k for j, k in nd])
    W = np.array([w[b] for b in nd])
    Gs = []
    for s in (1, -1):
        for t in (1, -1):
            Gs.append(G_rhombus(n, th + s * J * PI / n, ph + t * K * PI / m, C))
    Gs = np.array(Gs)
    lam = float((W * np.abs(Gs.sum(0)) / 4).sum())
    S = float((W * np.abs(Gs).sum(0) / 4).sum())
    # projected defects
    Gpp, Gpm, Gmp, Gmm = Gs        # (sigma,eta) = (+,+),(+,-),(-,+),(-,-)
    Qv = float((W * (np.abs(Gpp) + np.abs(Gpm) - np.abs(Gpp + Gpm)
                     + np.abs(Gmp) + np.abs(Gmm) - np.abs(Gmp + Gmm)) / 4).sum())
    Qh = float((W * (np.abs(Gpp) + np.abs(Gmp) - np.abs(Gpp + Gmp)
                     + np.abs(Gpm) + np.abs(Gmm) - np.abs(Gpm + Gmm)) / 4).sum())
    return lam, S, Qv, Qh


# ---------------------------------------------------------------- section A
def check_kernel_identity():
    out = []
    for n in (2, 3, 4, 5, 8, 11, 16):
        card = vandermonde_cardinals(n)
        m = n + 1
        C = coef_matrix(n)
        # rhombus vs divided difference at random angles (incl. a collision)
        err_dd = 0.
        for _ in range(20):
            u, v = rng.uniform(0, 2 * PI, 2)
            g1 = G_rhombus(n, u, v, C)[0]
            g2 = float(G_divdiff(n, mp.mpf(u), mp.mpf(v)))
            err_dd = max(err_dd, abs(g1 - g2))
        u = 2 * PI / 7
        g1 = G_rhombus(n, u, u, C)[0]
        g2 = float(G_divdiff(n, mp.mpf(u), mp.mpf(u)))
        err_dd = max(err_dd, abs(g1 - g2))
        # lambda via Vandermonde cardinals vs kernel identity
        err_lam = 0.
        for _ in range(25):
            th, ph = rng.uniform(0, PI, 2)
            Lv = cardinals_at(n, card, math.cos(th), math.cos(ph))[:, 0]
            lv = float(np.abs(Lv).sum())
            lk, S, Qv, Qh = lam_kernel(n, th, ph, C)
            err_lam = max(err_lam, abs(lv - lk))
        out.append({'n': n, 'vandermonde_cond': float(card[3]), 'rhombus_vs_divdiff': err_dd,
                    'lambda_vandermonde_vs_kernel': err_lam})
    return out


# ---------------------------------------------------------------- section B (theorem 13 parts 4)
def lobatto_functional(nmax=14):
    mp.mp.dps = 50
    out = []
    worst = 0
    for n in range(2, nmax + 1):
        t = [mp.cos(i * mp.pi / n) for i in range(n + 1)]
        for r in range(1, n + 1):
            tot = mp.mpf(0)
            for i in range(n + 1):
                # derivative of ell_i at -1 via polynomial coefficients
                roots = [t[l] for l in range(n + 1) if l != i]
                den = mp.fprod([t[i] - z for z in roots])
                # coefficients of prod (x - z) in powers of (x+1)
                coeffs = [mp.mpf(1)]
                for z in roots:
                    c = 1 + z    # x - z = (x+1) - (1+z)
                    new = [mp.mpf(0)] * (len(coeffs) + 1)
                    for p, a in enumerate(coeffs):
                        new[p + 1] += a
                        new[p] -= c * a
                    coeffs = new
                der = coeffs[r] * mp.factorial(r) / den if r < len(coeffs) else mp.mpf(0)
                sgn_exp = (-1) ** (n + r + i)
                if der == 0 or (1 if der > 0 else -1) != sgn_exp:
                    worst = max(worst, 1)
                    out.append({'n': n, 'r': r, 'i': i, 'sign_fail': True})
                tot += abs(der)
            # T_n^{(r)}(1) exact product
            Tr = mp.mpf(1)
            for p in range(1, r + 1):
                Tr *= (n * n - (p - 1) ** 2) / mp.mpf(2 * p - 1)
            rel = abs(tot - Tr) / Tr
            if rel > mp.mpf(10) ** -30 or Tr > mp.mpf(n) ** (2 * r):
                out.append({'n': n, 'r': r, 'sum': float(tot), 'Tn_r_1': float(Tr), 'fail': True})
                worst = max(worst, 1)
    return {'checked_n': [2, nmax], 'failures': out, 'pass': worst == 0}


def endpoint_derivative_sums(nlist=(4, 6, 7, 10, 13)):
    """(6): sum_B |d^r_x d^s_y L_B(c)| <= n^{2r+2s} Lambda_c  (Lambda_c<=Lambda_n, stronger)."""
    out = []
    for n in nlist:
        card = vandermonde_cardinals(n)
        nd, basis, A, _ = card
        Lc = float(np.abs(cardinals_at(n, card, -1., -1.)).sum())
        def dT(p, r):   # d^r/dx^r T_p at x=-1
            if r > p:
                return 0.
            val = 1.
            for i in range(r):
                val *= (p * p - i * i) / (2 * i + 1)
            return (-1) ** (p + r) * val
        worst = 0.
        for r in range(0, 4):
            for s in range(0, 4 - r):
                if r + s < 1:
                    continue
                vec = np.array([dT(p, r) * dT(q, s) for (p, q) in basis])
                tot = float(np.abs(A.T @ vec).sum())
                ratio = tot / (n ** (2 * (r + s)) * Lc)
                worst = max(worst, ratio)
        out.append({'n': n, 'Lambda_c': Lc, 'max_ratio_sum_over_n^(2r+2s)Lc': worst})
    return out


def aggregate_taylor(nlist=(3, 4, 6, 9, 12, 16)):
    out = []
    for n in nlist:
        card = vandermonde_cardinals(n)
        nd, basis, A, _ = card
        m = n + 1
        L0 = cardinals_at(n, card, -1., -1.)[:, 0]
        eps = 1e-7
        # exact gradients via Chebyshev derivative at -1
        def dT1(p):
            return 0. if p == 0 else (-1) ** (p + 1) * p * p
        gx = A.T @ np.array([dT1(p) * (-1) ** q for (p, q) in basis])
        gy = A.T @ np.array([(-1) ** p * dT1(q) for (p, q) in basis])
        zero = np.zeros(len(nd), bool)
        for i, (j, k) in enumerate(nd):
            zero[i] = (k == 0 and j > 0)
        Lc = float(np.abs(L0).sum())
        An = float((np.sign(L0[~zero]) * gx[~zero]).sum() + np.abs(gx[zero]).sum())
        Bn = float((np.sign(L0[~zero]) * gy[~zero]).sum() + np.abs(gy[zero]).sum())
        W = float(((gx[~zero] ** 2 + gy[~zero] ** 2) / np.abs(L0[~zero])).sum())
        worst_margin = math.inf
        worst_lin = -math.inf
        for _ in range(400):
            Hs = 10 ** rng.uniform(-6, 0) / n ** 2
            tt = rng.uniform(0, 1)
            hx, hy = tt * Hs, (1 - tt) * Hs
            Lh = cardinals_at(n, card, -1. + hx, -1. + hy)[:, 0]
            lam = float(np.abs(Lh).sum())
            H = hx + hy
            rhs = Lc + An * hx + Bn * hy + W / 2 * H * H + Lc * (math.expm1(n * n * H) - n * n * H)
            worst_margin = min(worst_margin, rhs - lam)
        # one-sided directional derivative check (linearity incl. zero cardinals)
        lin_err = 0.
        for tt in (0., .25, .5, .75, 1.):
            hh = 1e-9
            Lh = cardinals_at(n, card, -1. + tt * hh, -1. + (1 - tt) * hh)[:, 0]
            fd = (float(np.abs(Lh).sum()) - Lc) / hh
            lin_err = max(lin_err, abs(fd - (tt * An + (1 - tt) * Bn)) / max(1, abs(An)))
        out.append({'n': n, 'Lambda_c': Lc, 'A_n': An, 'B_n': Bn, 'W_n': W,
                    'min_rhs_minus_lambda_(Lambda_n->Lambda_c, stronger)': worst_margin,
                    'directional_derivative_linearity_rel_err': lin_err})
    return out


# ---------------------------------------------------------------- section C (theorem 12)
def theorem12(nlist=(2, 3, 4, 5, 6, 7, 8, 11, 12, 20)):
    out = []
    for n in nlist:
        m = n + 1
        C = coef_matrix(n)
        alphas = [0., .05, -.05, .2, -.2, .4, -.4]
        # add collision phases alpha = pi*(n*r - j*m)/m with |.|<=2/5
        for r in range(1, m):
            for j in range(2 * n):
                if (j + r) % 2 == 1:
                    a = PI * (n * r - j * m) / m
                    if 0 < abs(a) <= .4 and len(alphas) < 12:
                        alphas.append(a)
        res = {'n': n, 'alphas': len(alphas), 'max_signed_row_err': 0., 'max_R0_err': 0.,
               'max_Rm_formula5_err': 0., 'Rm_bound6_ok': True, 'max_S_identity7_err': 0.,
               'max_sign_interval3_err': 0., 'collisions_seen': 0, 'max_collision_value_err': 0.,
               'max_cot_rep2_err': 0.}
        for alpha in alphas:
            a = (1 + math.cos(alpha)) / 2
            Ssum = 0.
            Z = 0.
            for r in range(2 * m):
                delta = (1 - r) % 2
                ks = np.arange(n)
                u = (delta * PI + alpha) / n + 2 * ks * PI / n
                v = r * PI / m
                F = (-1) ** delta * G_rhombus(n, u, np.full(n, v), C) / 2
                T = F.sum()
                R = np.abs(F).sum()
                Ssum += R
                if r == 0:
                    res['max_signed_row_err'] = max(res['max_signed_row_err'], abs(T + n * (m - a)))
                    res['max_R0_err'] = max(res['max_R0_err'], abs(R - n * (m - a)))
                else:
                    res['max_signed_row_err'] = max(res['max_signed_row_err'], abs(T - n * a))
                    Z += np.clip(-F, 0, None).sum()
                if r == m:
                    sig = abs(alpha)
                    if sig == 0:
                        Rm = float(n)
                    else:
                        Rm = n * a + math.sin(sig) * sum(1 / math.tan((k * PI - sig / 2) / n) for k in range(1, n // 2 + 1))
                        Hn = sum(1 / k for k in range(1, n // 2 + 1))
                        if not (-1e-12 <= R - n * a <= n * sig * Hn / (PI - .2) + 1e-12):
                            res['Rm_bound6_ok'] = False
                    res['max_Rm_formula5_err'] = max(res['max_Rm_formula5_err'], abs(R - Rm))
                if r not in (0, m):
                    rs = min(r, 2 * m - r)
                    vf = rs * PI / m
                    sig = abs(alpha)
                    usig = (delta * PI + sig) / n + 2 * ks * PI / n
                    Fs = (-1) ** delta * G_rhombus(n, usig, np.full(n, v), C) / 2
                    Av = (math.sin(sig) - 2 * a / math.tan(vf / 2)) / 4
                    Bv = (math.sin(sig) + 2 * a / math.tan(vf / 2)) / 4
                    coll = np.abs(np.cos(usig) - math.cos(vf)) < 1e-9
                    rep = np.where(coll, (n + math.cos(vf)) / 2,
                                   Av / np.tan((usig - vf) / 2) + Bv / np.tan((usig + vf) / 2))
                    res['max_cot_rep2_err'] = max(res['max_cot_rep2_err'], float(np.max(np.abs(rep - Fs))))
                    if coll.any():
                        res['collisions_seen'] += int(coll.sum())
                        res['max_collision_value_err'] = max(res['max_collision_value_err'],
                                                             float(np.max(np.abs(Fs[coll] - (n + math.cos(vf)) / 2))))
                    # sign-interval formula (3)
                    if sig == 0:
                        I = None
                    else:
                        q = (1 + math.cos(vf)) / math.tan(sig / 2)
                        I = None if q >= 1 else (math.asin(q), PI - math.asin(q))
                    Dn = (usig > vf) & (usig < 2 * PI - vf)
                    In = np.zeros(n, bool) if I is None else (usig > I[0]) & (usig < I[1])
                    E = (Dn != In) & ~coll
                    R3 = n * a - 2 * Av * (1 / np.tan((usig[E] - vf) / 2)).sum() - 2 * Bv * (1 / np.tan((usig[E] + vf) / 2)).sum()
                    res['max_sign_interval3_err'] = max(res['max_sign_interval3_err'], abs(R3 - np.abs(Fs).sum()))
            S7 = 1 + 2 * n / m * a + 2 / (n * m) * Z
            res['max_S_identity7_err'] = max(res['max_S_identity7_err'], abs(Ssum / (n * m) - S7))
        out.append(res)
    return out


# ---------------------------------------------------------------- section D (theorems 08, 10)
def defect_checks(nlist=(48, 49, 64, 65)):
    out = []
    for n in nlist:
        m = n + 1
        C = coef_matrix(n)
        res = {'n': n, 'min_Delta_noncorner_s1to4': math.inf, 'min_Q_thin_lines': math.inf,
               'min_Qv_adaptive': math.inf, 'min_Qh_adaptive': math.inf, 'points': 0,
               'min_Delta_at_nonnode_corner_centres': math.inf}
        phases = []
        for ang in np.linspace(0, 2 * PI, 9)[:-1]:
            rho = 1 / 64
            c, s = math.cos(ang), math.sin(ang)
            sc = abs(c) + abs(s)
            phases.append((rho * c / sc, rho * s / sc))
        phases.append((0., 0.))
        centres = []
        for s_ in (1, 2, 3, 4):
            for J in (0, 1, n // 2, n - 1, n):
                for K in (s_, m - s_):
                    if (J + K) % 2 == 1:
                        centres.append(('V', J, K))
            for K in (0, 1, m // 2, m - 1, m):
                for J in (s_, n - s_):
                    if (J + K) % 2 == 1:
                        centres.append(('H', J, K))
        for kind, J, K in centres:
            for al, be in phases:
                th, ph = (J * PI + al) / n, (K * PI + be) / m
                if not (0 <= th <= PI and 0 <= ph <= PI):
                    continue
                lam, S, Qv, Qh = lam_kernel(n, th, ph, C)
                res['points'] += 1
                res['min_Delta_noncorner_s1to4'] = min(res['min_Delta_noncorner_s1to4'], S - lam)
                q = Qv if (kind == 'V' and 1 <= K <= m - 1) else Qh
                res['min_Q_thin_lines'] = min(res['min_Q_thin_lines'], q)
        # adaptive block (V),(H): rho<=1/8, endpoint distance >= 4pi/n
        for _ in range(60):
            rho = rng.uniform(0, 1 / 8)
            ang = rng.uniform(0, 2 * PI)
            sc = abs(math.cos(ang)) + abs(math.sin(ang))
            al, be = rho * math.cos(ang) / sc, rho * math.sin(ang) / sc
            J = int(rng.integers(0, n + 1))
            K = int(rng.integers(0, m + 1))
            if (J + K) % 2 == 0:
                K = K - 1 if K > 0 else 1
            th, ph = (J * PI + al) / n, (K * PI + be) / m
            if not (0 <= th <= PI and 0 <= ph <= PI):
                continue
            lam, S, Qv, Qh = lam_kernel(n, th, ph, C)
            if min(ph, PI - ph) >= 4 * PI / n:
                res['min_Qv_adaptive'] = min(res['min_Qv_adaptive'], Qv)
            if min(th, PI - th) >= 4 * PI / n:
                res['min_Qh_adaptive'] = min(res['min_Qh_adaptive'], Qh)
        # extreme endpoint distance exactly 4pi/n
        for th in (4 * PI / n, PI - 4 * PI / n):
            for ph in (0., PI / 3, PI):
                lam, S, Qv, Qh = lam_kernel(n, th, ph, C)
                res['min_Qh_adaptive'] = min(res['min_Qh_adaptive'], Qh)
                lam, S, Qv, Qh = lam_kernel(n, ph, th, C)
                res['min_Qv_adaptive'] = min(res['min_Qv_adaptive'], Qv)
        # contrast: Delta at the nonnode corner centres is small (no defect claimed there)
        for J, K in ((n, m), (n, 0) if n % 2 == 1 else (0, m)):
            for al, be in phases:
                th, ph = (J * PI - abs(al)) / n if J else abs(al) / n, (K * PI - abs(be)) / m if K else abs(be) / m
                lam, S, Qv, Qh = lam_kernel(n, th, ph, C)
                res['min_Delta_at_nonnode_corner_centres'] = min(res['min_Delta_at_nonnode_corner_centres'], S - lam)
        res['bounds'] = {'Delta_thm10': 1 / 4096, 'thin_lines': 1 / 3328, 'adaptive': 1 / 1536}
        out.append(res)
    return out


# ---------------------------------------------------------------- section E (theorem 07 sub-lemmas)
def theorem07_sublemmas(nlist=(2, 3, 4, 5, 7, 10, 16, 33, 64)):
    out = []
    for n in nlist:
        m = n + 1
        C = coef_matrix(n)
        res = {'n': n, 'min_b_over_d/2m': math.inf, 'min_t_over_L/4m': math.inf,
               'max_sin_over_3b': 0., 'min_B_F_over_n': math.inf, 'min_B_F0_over_n': math.inf,
               'max_B_grad_over_n': 0., 'max_B_factorisation_err': 0., 'max_S_minus_Q_bound': -math.inf}
        Lc = None
        for trial in range(12):
            rho = 1 / 64 * (1 if trial < 8 else rng.uniform(0, 1))
            ang = rng.uniform(0, 2 * PI) if trial >= 4 else trial * PI / 2 + PI / 4
            sc = abs(math.cos(ang)) + abs(math.sin(ang))
            al, be = rho * math.cos(ang) / sc, rho * math.sin(ang) / sc
            for j in range(n + 1):
                for r in range(m + 1):
                    if (j + r) % 2 == 0:
                        continue
                    inB = (r == j + 1 and j >= 2 * n / 3)
                    u, v = (j * PI + al) / n, (r * PI + be) / m
                    if not inB:
                        L = abs(j - r)
                        d = min(j + r, 2 * n + 1 - j - r)
                        b = math.sin((u + v) / 2)
                        t = abs(math.sin((u - v) / 2))
                        res['min_b_over_d/2m'] = min(res['min_b_over_d/2m'], b / (d / (2 * m)))
                        res['min_t_over_L/4m'] = min(res['min_t_over_L/4m'], t / (L / (4 * m)))
                        res['max_sin_over_3b'] = max(res['max_sin_over_3b'], max(abs(math.sin(u)), abs(math.sin(v))) / (3 * b))
                    else:
                        F = (-1) ** j * (G_rhombus(n, u, v, C)[0]) / 2
                        F0 = (-1) ** j * (G_rhombus(n, j * PI / n, r * PI / m, C)[0]) / 2
                        res['min_B_F_over_n'] = min(res['min_B_F_over_n'], F / n)
                        res['min_B_F0_over_n'] = min(res['min_B_F0_over_n'], F0 / n)
                        e = 1e-6
                        Fa = (-1) ** j * (G_rhombus(n, u + e / n, v, C)[0] - G_rhombus(n, u - e / n, v, C)[0]) / (4 * e)
                        Fb = (-1) ** j * (G_rhombus(n, u, v + e / m, C)[0] - G_rhombus(n, u, v - e / m, C)[0]) / (4 * e)
                        res['max_B_grad_over_n'] = max(res['max_B_grad_over_n'], max(abs(Fa), abs(Fb)) / n)
                        # factorisation D_n=(-1)^n{V_n(X)U_m(T)+U_n(X)V_n(T)}
                        h = n - j
                        xB, yB = (h * PI - al) / n, (h * PI - be) / m
                        XB, TB = (xB + yB) / 2, (xB - yB) / 2
                        U = lambda k, z: sum(math.cos(l * z) for l in range(1 - k, k, 2))
                        Vn = lambda z: math.cos((2 * n + 1) * z / 2) / math.cos(z / 2)
                        Dn = (-1) ** n * (Vn(XB) * U(m, TB) + U(n, XB) * Vn(TB))
                        Gd = Dn - math.cos(n * u)
                        res['max_B_factorisation_err'] = max(res['max_B_factorisation_err'],
                                                             abs(Gd - G_rhombus(n, u, v, C)[0]))
            # the envelope (Q) itself on this phase
            if Lc is None:
                Lc = S_primitive(n, 0., 0., C)
            Sv = S_primitive(n, al, be, C)
            a = (math.cos(al) + math.cos(be)) / 2
            bound = a * Lc + 242000 * rho ** 2 * math.log(m) + 2048 * rho ** 1.5 + 640 * rho * (1 + math.log(m)) / n
            res['max_S_minus_Q_bound'] = max(res['max_S_minus_Q_bound'], Sv - bound)
            res['max_(S-aLc)'] = max(res.get('max_(S-aLc)', -math.inf), Sv - a * Lc)
        res['thresholds'] = {'b': 1, 't': 1, 'sin': 1, 'B_F_lower': 2 / (3 * PI ** 2), 'B_F0_lower': 4 / (3 * PI ** 2), 'B_grad_upper': 3}
        out.append(res)
    return out


def S_primitive(n, al, be, C):
    m = n + 1
    tot = 0.
    for j in range(2 * n):
        rs = np.array([r for r in range(2 * m) if (j + r) % 2 == 1])
        u = np.full(len(rs), (j * PI + al) / n)
        v = (rs * PI + be) / m
        tot += np.abs(G_rhombus(n, u, v, C)).sum() / 2
    return tot / (n * m)


if __name__ == '__main__':
    sections = sys.argv[1:] or ['A', 'B', 'C', 'D', 'E']
    out = {'kind': 'auditor independent MEASURED float64/mpmath checks; not proofs',
           'numpy': np.__version__, 'mpmath': mp.__version__, 'seed': 20261102}
    for sname in sections:
        t0 = time.time()
        if sname == 'A':
            out['A_kernel_identity'] = check_kernel_identity()
        elif sname == 'B':
            out['B_lobatto_functional'] = lobatto_functional()
            out['B_endpoint_derivative_sums'] = endpoint_derivative_sums()
            out['B_aggregate_taylor'] = aggregate_taylor()
        elif sname == 'C':
            out['C_theorem12_rows'] = theorem12()
        elif sname == 'D':
            out['D_defects_08_10'] = defect_checks()
        elif sname == 'E':
            out['E_theorem07_sublemmas'] = theorem07_sublemmas()
        out[f'seconds_{sname}'] = round(time.time() - t0, 1)
        print(f'section {sname} done {out[f"seconds_{sname}"]}s', file=sys.stderr, flush=True)
    print(json.dumps(out, indent=1, default=float))
