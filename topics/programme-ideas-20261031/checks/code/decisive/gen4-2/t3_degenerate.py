"""Decisive test gen4-2, T3: certificates for the degenerate points of lambda_n in Chebyshev angles, where the generic
box certificates of t3_certify.py cannot terminate:
  (1) corners z (both angles in {0, pi}): every L_B is even in both u = th - z1 and v = ph - z2, so
      L_B(x) = L_B(z) + q_B(u,v) + R_B,  q_B = (c_B u^2 + e_B v^2)/2,  |R_B| <= n^4 M_B (|u|+|v|)^4 / 24,
      grad L_B(x) = (c_B u, e_B v) + R',   |R'_i| <= n^4 M_B (|u|+|v|)^3 / 6
      (all odd-order derivatives vanish at z; Bernstein bounds the 4th derivatives by n^4 M_B).
      Z = {B : the sign of L_B is not constant on the disc}, s_B = sgn L_B(z) for the others.
      (D-max) C1 = sum_clear s_B c_B + sum_Z |c_B| < 0 and C2 (with e) < 0, with the remainder margins: z is a strict local max
              and every x != z in the disc has D^+ lambda > 0 towards z  -> exactly one local max in the disc.
      (D-min) g(alpha) = sum_Z |q_B| + sum_clear s_B q_B on the unit circle has a positive minimum (exact: piecewise linear
              in cos 2 alpha): every x != z has D^+ lambda > 0 away from z -> no local max in the disc.
  (2) edge nodes z (one angle in {0, pi}; normal coordinate u, tangential v): L_B(x) = a_B v + (c_B u^2 + e_B v^2)/2 + R_B,
      |R_B| <= n^3 M_B rho^3/6, rho = |u|+|v|; d_v L_B(x) = a_B + e_B v + R (|R| <= n^3 M_B rho^2/2); d_u L_B(x) = c_B u + R.
      A local max at x needs D^+ lambda <= 0 along +-e_v and e_u (u > 0 w.l.o.g. by evenness). With sigma the sign pattern
      at x: D_{+-e_v}^+ lambda >= +-F1(sigma) - E1, F1 = sum_{B != z} sigma_B a_B + a_z;  D_{e_u}^+ lambda >= u F2(sigma) - E2',
      F2 = sum_{B != z} sigma_B c_B + c_z (L_z > 0 near z). Realisable patterns: regime I (|v| >= W u^2): sigma_B = sgn(a_B v);
      regime II (|v| <= W u^2, w = v/u^2): sigma_B = sgn(a_B) sgn(w + kappa_B), kappa_B = c_B/(2 a_B), up to the ambiguity
      windows |w + kappa_B| <= eta_B where B may have either sign (treated with the worst sign in each inequality).
      The disc is certified free of local maxima if in regime I: gap_I(+-) - E1 > 0, and in regime II for every w:
      |F1^clear(w)| - sum_amb |a_B| - E1 > 0  or  |F2^clear(w)| - sum_amb |c_B| - E2 > 0,
      where the second alternative uses that a local max at a point off the creases is a critical point of the local
      polynomial (so d_u p_sigma = u F2 + ... = 0 is necessary) and every zero of every L_B in the punctured disc is regular
      (checked: |a_B| exceeds the remainder of d_v L_B, or else |c_B| exceeds the remainder of d_u L_B / u).
All quantities are evaluated at the node; the sets and minima are computed exactly (finite breakpoints).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01.
"""
import numpy as np


def _minimise_piecewise_linear(A, Bv, signs_fixed, Z):
    """min over t in [-1,1] of sum_{B in Z} |A_B + B_B t| + sum_{B not in Z} s_B (A_B + B_B t)  (exact)."""
    def val(t):
        return np.sum(np.abs(A[Z] + Bv[Z] * t)) + np.sum(signs_fixed * (A[~Z] + Bv[~Z] * t))
    cands = [-1.0, 1.0]
    with np.errstate(divide='ignore', invalid='ignore'):
        tb = -A[Z] / Bv[Z]
    cands += [float(t) for t in tb if np.isfinite(t) and -1 < t < 1]
    return min(val(t) for t in cands)


def corner_certificate(C, z, rho_list=(2e-3, 1e-3, 5e-4, 2e-4, 1e-4, 5e-5, 2e-5, 1e-5)):
    """Returns dict(kind in {'max','min',None}, rho0, details) for the corner z = (z1, z2) (angles)."""
    n = C.n; d = C.f.cardinals([z[0]], [z[1]], derivs=2)
    L = d['L'][0]; c = d['Ltt'][0]; e = d['Lpp'][0]
    g1 = np.max(np.abs(d['Lt'][0])); g2 = np.max(np.abs(d['Lp'][0])); mixed = np.max(np.abs(d['Ltp'][0]))
    n4M = n ** 4 * C.MB; n4Mtot = float(np.sum(n4M))
    lam = float(np.sum(np.abs(L)))
    for rho0 in rho_list:
        # sign constancy of L_B on the 1-norm disc of radius rho0: |L_B(z)| > max|q_B| + max|R_B|
        bound = 0.5 * (np.abs(c) + np.abs(e)) * rho0 ** 2 + n4M * rho0 ** 4 / 24
        Z = np.abs(L) <= bound
        s = np.sign(L[~Z])
        C1 = np.sum(s * c[~Z]) + np.sum(np.abs(c[Z])); C2 = np.sum(s * e[~Z]) + np.sum(np.abs(e[Z]))
        rem = n4Mtot * rho0 ** 2 / 6
        if max(C1, C2) / 2 + rem < 0 and abs(max(C1, C2)) / np.sqrt(2) > n4Mtot * rho0 ** 2 / 3:
            return dict(kind='max', rho0=rho0, lam=lam, C1=float(C1), C2=float(C2), nZ=int(Z.sum()), evenness_err=float(max(g1, g2, mixed)),
                        margin=float(min(-(max(C1, C2) / 2 + rem), abs(max(C1, C2)) / np.sqrt(2) - n4Mtot * rho0 ** 2 / 3)))
        # (D-min): g(alpha) = sum_Z |q_B| + sum_clear s_B q_B, q_B = A_B + B_B cos 2alpha, A = (c+e)/4, B = (c-e)/4
        A = (c + e) / 4; Bq = (c - e) / 4
        gmin = _minimise_piecewise_linear(A, Bq, s, Z)
        if gmin > 0.45 * n4Mtot * rho0 ** 2:
            return dict(kind='min', rho0=rho0, lam=lam, gmin=float(gmin), nZ=int(Z.sum()), evenness_err=float(max(g1, g2, mixed)),
                        margin=float(gmin - 0.45 * n4Mtot * rho0 ** 2))
    return dict(kind=None, rho0=None, lam=lam, nZ=int(Z.sum()), evenness_err=float(max(g1, g2, mixed)))


def edge_node_certificate(C, z, nu, rho_list=(8e-3, 5e-3, 3e-3, 2e-3, 1.5e-3, 1e-3, 5e-4, 2e-4, 1e-4, 5e-5, 2e-5, 1e-5), W_factor=2.0):
    """Edge node z (angles) with normal coordinate index nu (0: theta, 1: phi). Third-order Taylor data at z are exact
    (remainders bounded by Bernstein n^4 M_B); evenness in u kills all terms odd in u. Returns dict(ok, rho0, details)."""
    n = C.n; d = C.f.cardinals([z[0]], [z[1]], derivs=3)
    L = d['L'][0]
    q = int(np.argmin(np.abs(L - 1)))                       # the node's own index
    if nu == 0:
        a = d['Lp'][0]; c = d['Ltt'][0]; e = d['Lpp'][0]; dn = d['Lt'][0]; mix = d['Ltp'][0]
        Tuuv = d['Lttp'][0]; Tvvv = d['Lppp'][0]; Tuuu = d['Lttt'][0]; Tuvv = d['Ltpp'][0]
    else:
        a = d['Lt'][0]; c = d['Lpp'][0]; e = d['Ltt'][0]; dn = d['Lp'][0]; mix = d['Ltp'][0]
        Tuuv = d['Ltpp'][0]; Tvvv = d['Lttt'][0]; Tuuu = d['Lppp'][0]; Tuvv = d['Lttp'][0]
    even_err = float(max(np.max(np.abs(dn)), np.max(np.abs(mix)), np.max(np.abs(Tuuu)), np.max(np.abs(Tuvv))))
    n4M = n ** 4 * C.MB; n4Mtot = float(np.sum(n4M))
    others = np.ones(C.N, bool); others[q] = False
    a_o, c_o, e_o, n4M_o = a[others], c[others], e[others], n4M[others]
    Tuuv_o, Tvvv_o = Tuuv[others], Tvvv[others]
    a_z, c_z, e_z = a[q], c[q], e[q]
    for rho0 in rho_list:
        # remainder of d_v L_B beyond a_B: |e_B| rho + (|T_uuv| + |T_vvv|) rho^2/2 + n^4 M_B rho^3/6   (all B)
        rem_v = np.abs(e) * rho0 + 0.5 * (np.abs(Tuuv) + np.abs(Tvvv)) * rho0 ** 2 + n4M * rho0 ** 3 / 6
        E1 = float(np.sum(rem_v))
        # which B != z have a certainly non-vanishing tangential derivative on the disc (regular zeros)
        reg = np.abs(a_o) > rem_v[others]
        # for the others ("small-a"): need |c_B| > |T_uuv| W u^2 + n^4 M_B u^2 (1+Wu)^3/6 (regular zeros off the edge) - checked below with W
        small = ~reg
        with np.errstate(divide='ignore', invalid='ignore'):
            kappa = np.where(small, 0.0, c_o / (2 * a_o))
        W = W_factor * (np.max(np.abs(kappa[reg])) if np.any(reg) else 1.0) + 1.0
        th0 = rho0
        if np.any(small):
            if not np.all(np.abs(c_o[small]) > np.abs(Tuuv_o[small]) * W * th0 ** 2 + n4M_o[small] * th0 ** 2 * (1 + W * th0) ** 3 / 6):
                continue
        # L_z > 0 on the disc
        if 1 - abs(a_z) * rho0 - 0.5 * (abs(c_z) + abs(e_z)) * rho0 ** 2 - (abs(Tuuv[q]) + abs(Tvvv[q])) * rho0 ** 3 / 2 - n4M[q] * rho0 ** 4 / 24 <= 0:
            continue
        # regime I (|v| >= W u^2): clear B satisfy |a_B| > |c_B|/(2W) + |e_B| rho0/2 + (|T_uuv| + |T_vvv|/3) rho0^2/2 + T4_B/|v|
        T4ratio = n4M_o * (np.sqrt(rho0 / W) + rho0) ** 4 / (24 * rho0)
        thrI = np.abs(c_o) / (2 * W) + 0.5 * np.abs(e_o) * rho0 + 0.5 * (np.abs(Tuuv_o) + np.abs(Tvvv_o) / 3) * rho0 ** 2 + T4ratio
        clearI = reg & (np.abs(a_o) > thrI)
        gapI = np.sum(np.abs(a_o[clearI])) - np.sum(np.abs(a_o[~clearI])) - abs(a_z)
        if gapI - E1 <= 0:
            continue
        # regime II (|v| <= W u^2, w = v/u^2): ambiguity windows and the normal-derivative remainder (both O(u^2))
        eta_num = 0.5 * np.abs(e_o) * W ** 2 * th0 ** 2 + 0.5 * np.abs(Tuuv_o) * W * th0 ** 2 + np.abs(Tvvv_o) * W ** 3 * th0 ** 4 / 6 + n4M_o * th0 ** 2 * (1 + W * th0) ** 4 / 24
        eta = np.where(small, np.inf, eta_num / np.where(small, 1.0, np.abs(a_o)))
        E2 = float(W * th0 ** 2 * np.sum(np.abs(Tuuv)) + n4Mtot * th0 ** 2 * (1 + W * th0) ** 3 / 6)
        pts = np.concatenate([[-W, W], (-kappa[reg] - eta[reg]), (-kappa[reg] + eta[reg])])
        pts = np.sort(pts[(pts >= -W) & (pts <= W)]); pts = np.concatenate([[-W], pts, [W]])
        worst = np.inf; okII = True
        for w0, w1 in zip(pts[:-1], pts[1:]):
            if w1 - w0 <= 0:
                continue
            w = 0.5 * (w0 + w1)
            amb = small | (np.abs(w + kappa) <= eta)
            sig = np.sign(a_o) * np.sign(w + kappa)
            F1 = np.sum(sig[~amb] * a_o[~amb]) + a_z; F2 = np.sum(sig[~amb] * c_o[~amb]) + c_z
            Sa = np.sum(np.abs(a_o[amb])); Sc = np.sum(np.abs(c_o[amb]))
            m = max(abs(F1) - Sa - E1, abs(F2) - Sc - E2)
            worst = min(worst, m)
            if m <= 0:
                okII = False
                break
        if okII:
            return dict(ok=True, rho0=rho0, W=float(W), E1=E1, E2=E2, gapI=float(gapI), marginII=float(worst),
                        n_clearI=int(clearI.sum()), n_small=int(small.sum()), evenness_err=even_err)
    return dict(ok=False, rho0=None, W=float(W) if 'W' in dir() else None, evenness_err=even_err)


def degenerate_points(C):
    """All degenerate points of the extended function meeting the domain: the 4 corners and the edge nodes (own images)."""
    corners = []
    for z in ((0.0, 0.0), (0.0, np.pi), (np.pi, 0.0), (np.pi, np.pi)):
        corners.append((np.array(z), corner_certificate(C, z)))
    edges = []
    thB, phB = C.f.thB, C.f.phB
    for q in range(C.N):
        on_t = min(thB[q], abs(np.pi - thB[q])) < 1e-12; on_p = min(phB[q], abs(np.pi - phB[q])) < 1e-12
        if on_t and on_p:
            continue                                      # corner node: handled by the corner certificate
        if on_t:
            edges.append((np.array([thB[q], phB[q]]), edge_node_certificate(C, (thB[q], phB[q]), 0)))
        elif on_p:
            edges.append((np.array([thB[q], phB[q]]), edge_node_certificate(C, (thB[q], phB[q]), 1)))
    return corners, edges
