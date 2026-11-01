#!/usr/bin/env python3
"""Numerical census (SUPPORTING EVIDENCE, NOT PROOF) of strict local maxima of the
Padua Lebesgue function lambda_n = sum_i |L_i| on the closed square, n=3..8.

claude-audit-01 sub-auditor; imports no repository code.

Nodes (cos(j pi/n), cos(k pi/(n+1))), j+k even (repo convention).  Cardinals by
the closed-form kernel formula (verified numerically against the cardinal
conditions and against a numpy Vandermonde solve).

Method, in theta-coordinates x=cos(t1), y=cos(t2), t in [0,pi]^2, where
F(t)=lambda(cos t1, cos t2) is even about t=0 and t=pi, so open-edge maxima of
lambda become ordinary maxima of F (edges are not special) and corners are
handled separately:
  1. uniform (M+1)^2 theta grid; lambda and the full 45-bit sign mask per point;
  2. seeds = grid points not exceeded by any 8-neighbour WITH THE SAME MASK
     (reflection padding).  Every sign-region component contains a seed, so
     twin maxima separated by a crease (different masks) are seeded separately;
  3. from every seed, Newton on grad_t G_s = 0 for the seed's fixed mask s
     (G_s = P_s o cos), step-limited; accept iff converged, Hessian of G_s
     negative definite, and sign(L_i(p)) = s_i for all i (so lambda = P_s near p);
     min |L_i(p)| is recorded to flag crease-adjacent cases;
  4. independent non-smooth check: Nelder-Mead on F itself from every FULL discrete
     local max of lambda; every NM limit must coincide with an accepted point or a
     corner, otherwise it is reported as UNMATCHED;
  5. corners: exact node test, and for non-node corners all active masks need
     strictly negative inward partials;
  6. dedupe, classify interior / open edge / corner, and compare the global max.
"""
import argparse, json, sys, time
import numpy as np
from scipy.optimize import minimize


def nodes(n):
    out = []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                out.append((j, k))
    return out


def cardinal_cheb(n):
    """C[i, a, b]: L_i(x,y) = sum_{a+b<=n} C[i,a,b] T_a(x) T_b(y)."""
    nd = nodes(n)
    C = np.zeros((len(nd), n + 1, n + 1))
    for i, (j, k) in enumerate(nd):
        tx, ty = j * np.pi / n, k * np.pi / (n + 1)
        on_x, on_y = j in (0, n), k in (0, n + 1)
        w = (0.5 if (on_x and on_y) else (1.0 if (on_x or on_y) else 2.0)) / (n * (n + 1))
        for a in range(n + 1):
            for b in range(n + 1 - a):
                fa = 1.0 if a == 0 else 2.0
                fb = 1.0 if b == 0 else 2.0
                v = fa * fb * np.cos(a * tx) * np.cos(b * ty)
                if a == n and b == 0:
                    v -= np.cos(n * tx)
                C[i, a, b] = w * v
    return nd, C


def check_cardinals(n, nd, C):
    th = np.array([[j * np.pi / n, k * np.pi / (n + 1)] for j, k in nd])
    A = np.arange(n + 1)
    Tx = np.cos(np.outer(th[:, 0], A)); Ty = np.cos(np.outer(th[:, 1], A))
    Lnodes = np.einsum('iab,ha,hb->ih', C, Tx, Ty)
    err_id = np.abs(Lnodes - np.eye(len(nd))).max()
    # Vandermonde cross-check in Chebyshev basis
    idx = [(a, b) for a in range(n + 1) for b in range(n + 1 - a)]
    V = np.array([[Tx[h, a] * Ty[h, b] for (a, b) in idx] for h in range(len(nd))])
    coef = np.linalg.solve(V, np.eye(len(nd)))  # columns = cardinals
    Cv = np.zeros_like(C)
    for q, (a, b) in enumerate(idx):
        Cv[:, a, b] = coef[q, :]
    err_v = np.abs(Cv - C).max()
    return float(err_id), float(err_v), float(np.linalg.cond(V))


def grid_eval(C, t1, t2, chunk=400):
    n = C.shape[1] - 1
    A = np.arange(n + 1)
    Tx = np.cos(np.outer(A, t1)); Ty = np.cos(np.outer(A, t2))
    N = C.shape[0]
    lam = np.zeros((len(t1), len(t2)))
    mask = np.zeros((len(t1), len(t2)), dtype=np.int64)
    minabs = np.full((len(t1), len(t2)), np.inf)
    for i in range(N):
        L = Tx.T @ C[i] @ Ty
        lam += np.abs(L)
        mask |= (L > 0).astype(np.int64) << i
        np.minimum(minabs, np.abs(L), out=minabs)
    return lam, mask, minabs


def seeds_restricted(lam, mask, full=False):
    P = np.pad(lam, 1, mode='reflect'); Q = np.pad(mask, 1, mode='reflect')
    M1, M2 = lam.shape
    ok = np.ones_like(lam, dtype=bool)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            nb = P[1 + di:1 + di + M1, 1 + dj:1 + dj + M2]
            if full:
                ok &= ~(nb > lam)
            else:
                nm = Q[1 + di:1 + di + M1, 1 + dj:1 + dj + M2]
                ok &= ~((nm == mask) & (nb > lam))
    return np.argwhere(ok)


def signs_from_mask(m, N):
    return np.where((m[:, None] >> np.arange(N)[None, :]) & 1, 1.0, -1.0)


def G_derivs(c, th):
    """c: (K, n+1, n+1) Chebyshev coeffs; th: (K,2).  Returns G, grad, Hess in theta."""
    n = c.shape[1] - 1
    A = np.arange(n + 1)
    ca, sa = np.cos(th[:, 0:1] * A), np.sin(th[:, 0:1] * A)
    cb, sb = np.cos(th[:, 1:2] * A), np.sin(th[:, 1:2] * A)
    G = np.einsum('kab,ka,kb->k', c, ca, cb)
    g1 = np.einsum('kab,ka,kb->k', c, -A * sa, cb)
    g2 = np.einsum('kab,ka,kb->k', c, ca, -A * sb)
    h11 = np.einsum('kab,ka,kb->k', c, -A ** 2 * ca, cb)
    h12 = np.einsum('kab,ka,kb->k', c, A * sa, A * sb)
    h22 = np.einsum('kab,ka,kb->k', c, ca, -A ** 2 * cb)
    return G, np.stack([g1, g2], 1), np.stack([np.stack([h11, h12], 1), np.stack([h12, h22], 1)], 1)


def cardinals_at(C, th):
    n = C.shape[1] - 1
    A = np.arange(n + 1)
    ca, cb = np.cos(th[:, 0:1] * A), np.cos(th[:, 1:2] * A)
    return np.einsum('iab,ka,kb->ki', C, ca, cb)


def fold(th):
    return np.arccos(np.clip(np.cos(th), -1, 1))


def newton(c, th0, iters=60, maxstep=0.02):
    th = th0.copy()
    for _ in range(iters):
        _, g, H = G_derivs(c, th)
        det = H[:, 0, 0] * H[:, 1, 1] - H[:, 0, 1] ** 2
        det = np.where(np.abs(det) < 1e-300, 1e-300, det)
        d1 = (H[:, 1, 1] * g[:, 0] - H[:, 0, 1] * g[:, 1]) / det
        d2 = (-H[:, 0, 1] * g[:, 0] + H[:, 0, 0] * g[:, 1]) / det
        step = np.stack([d1, d2], 1)
        nrm = np.abs(step).max(1, keepdims=True)
        nrm = np.where(np.isfinite(nrm), nrm, 1e300)
        step = np.where(np.isfinite(step), step, 0.0)
        step = np.where(nrm > maxstep, step * (maxstep / np.maximum(nrm, 1e-300)), step)
        th = th - step
    th = fold(th)
    G, g, H = G_derivs(c, th)
    return th, G, g, H


def census(n, M, nm_max=4000):
    t0 = time.time()
    nd, C = cardinal_cheb(n)
    N = len(nd)
    err_id, err_v, condV = check_cardinals(n, nd, C)
    t = np.linspace(0, np.pi, M + 1)
    lam, mask, minabs = grid_eval(C, t, t)
    seeds = seeds_restricted(lam, mask)
    th0 = np.stack([t[seeds[:, 0]], t[seeds[:, 1]]], 1)
    s = signs_from_mask(mask[seeds[:, 0], seeds[:, 1]], N)
    c = np.einsum('ki,iab->kab', s, C)
    th, G, g, H = newton(c, th0)
    gnorm = np.abs(g).max(1)
    negdef = (H[:, 0, 0] < 0) & (H[:, 0, 0] * H[:, 1, 1] - H[:, 0, 1] ** 2 > 0)
    Lp = cardinals_at(C, th)
    consistent = np.all(s * Lp > 0, axis=1)
    minL = np.abs(Lp).min(1)
    lam_p = np.abs(Lp).sum(1)
    sin1, sin2 = np.sin(th[:, 0]), np.sin(th[:, 1])
    corner_like = (np.abs(sin1) < 1e-7) & (np.abs(sin2) < 1e-7)
    # an edge critical point of G has sin=0 in one coordinate; Hessian there is the
    # theta-Hessian (normal entry = -cos(t)*P_x etc.), negative definite <=> strict
    acc = (gnorm < 1e-9) & negdef & ~corner_like
    # sign consistency, allowing (numerically) zero cardinals: every active mask
    # (both signs at each near-zero cardinal) must satisfy stationarity (theta-grad=0)
    # and theta-Hessian negative definite; otherwise rejected.
    zero_tol = 1e-9
    crease_info = []
    for q in np.nonzero(acc)[0]:
        Z = np.nonzero(np.abs(Lp[q]) < zero_tol)[0]
        nz = np.abs(Lp[q]) >= zero_tol
        if not np.all((s[q] * Lp[q] > 0) | ~nz):
            acc[q] = False
            continue
        if len(Z) == 0:
            continue
        if len(Z) > 12:
            acc[q] = False; crease_info.append({'theta': th[q].tolist(), 'zeros': len(Z), 'ok': False})
            continue
        ok = True
        for bits in range(1 << len(Z)):
            sq = s[q].copy()
            for u, zi in enumerate(Z):
                sq[zi] = 1.0 if (bits >> u) & 1 else -1.0
            cq = np.einsum('i,iab->ab', sq, C)[None]
            _, gq, Hq = G_derivs(cq, th[q][None])
            okq = (np.abs(gq).max() < 1e-8) and (Hq[0, 0, 0] < 0) and \
                (Hq[0, 0, 0] * Hq[0, 1, 1] - Hq[0, 0, 1] ** 2 > 0)
            ok &= bool(okq)
        crease_info.append({'x': float(np.cos(th[q, 0])), 'y': float(np.cos(th[q, 1])),
                            'zero_cardinals': Z.tolist(), 'all_active_masks_ok': ok})
        if not ok:
            acc[q] = False
    pts = []
    for q in np.nonzero(acc)[0]:
        x, y = np.cos(th[q, 0]), np.cos(th[q, 1])
        cls = 'interior'
        if abs(sin1[q]) < 1e-7 or abs(sin2[q]) < 1e-7:
            cls = 'edge'
        pts.append((x, y, cls, float(lam_p[q]), float(minL[q]), int(mask[seeds[q, 0], seeds[q, 1]])))
    # dedupe
    uniq = []
    for p in sorted(pts, key=lambda r: -r[3]):
        if not any(abs(p[0] - u[0]) < 1e-8 and abs(p[1] - u[1]) < 1e-8 for u in uniq):
            uniq.append(p)
    # corners
    corners = []
    for (x0, y0) in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        j = 0 if x0 == 1 else n; k = 0 if y0 == 1 else n + 1
        is_node = (j + k) % 2 == 0
        thc = np.array([[0.0 if x0 == 1 else np.pi, 0.0 if y0 == 1 else np.pi]])
        Lc = cardinals_at(C, thc)[0]
        lamc = float(np.abs(Lc).sum())
        strict = False
        if not is_node:
            zero = np.abs(Lc) < 1e-12
            # inward partials: d/dx at x0 inward direction -x0; T_a'(1)=a^2, T_a'(-1)=(-1)^(a+1) a^2
            A = np.arange(n + 1)
            Tx0 = np.cos(A * thc[0, 0]); Ty0 = np.cos(A * thc[0, 1])
            dTx = (A ** 2) * (1.0 if x0 == 1 else (-1.0) ** (A + 1))
            dTy = (A ** 2) * (1.0 if y0 == 1 else (-1.0) ** (A + 1))
            base = np.sign(Lc)
            zs = np.nonzero(zero)[0]
            strict = True
            for bits in range(1 << len(zs)):
                sc = base.copy()
                for u, zi in enumerate(zs):
                    sc[zi] = 1 if (bits >> u) & 1 else -1
                cc = np.einsum('i,iab->ab', sc, C)
                px = dTx @ cc @ Ty0
                py = Tx0 @ cc @ dTy
                inx, iny = -x0 * px, -y0 * py
                strict &= (inx < 0) and (iny < 0)
            strict = bool(strict)
        corners.append({'corner': [x0, y0], 'is_node': is_node, 'lambda': lamc,
                        'strict_local_max': (not is_node) and strict})
    # non-smooth independent check: Nelder-Mead on F from full discrete local maxima
    fseeds = seeds_restricted(lam, mask, full=True)
    if len(fseeds) > nm_max:
        fseeds = fseeds[np.argsort(-lam[fseeds[:, 0], fseeds[:, 1]])[:nm_max]]

    def negF(v):
        Lv = cardinals_at(C, np.array([v]))[0]
        return -np.abs(Lv).sum()
    unmatched = []
    for (a, b) in fseeds:
        r = minimize(negF, [t[a], t[b]], method='Nelder-Mead',
                     options={'xatol': 1e-12, 'fatol': 1e-15, 'maxiter': 4000,
                              'initial_simplex': [[t[a], t[b]], [t[a] + 1e-4, t[b]], [t[a], t[b] + 1e-4]]})
        v = fold(np.array(r.x))
        x, y = np.cos(v[0]), np.cos(v[1])
        hit = any(abs(x - u[0]) < 1e-5 and abs(y - u[1]) < 1e-5 for u in uniq) or \
            any(abs(x - cc['corner'][0]) < 1e-5 and abs(y - cc['corner'][1]) < 1e-5 for cc in corners)
        if not hit:
            unmatched.append([float(x), float(y), float(-r.fun)])
    # dedupe unmatched
    um = []
    for p in unmatched:
        if not any(abs(p[0] - u[0]) < 1e-4 and abs(p[1] - u[1]) < 1e-4 for u in um):
            um.append(p)
    n_int = sum(1 for p in uniq if p[2] == 'interior')
    n_edge = sum(1 for p in uniq if p[2] == 'edge')
    n_cor = sum(1 for cc in corners if cc['strict_local_max'])
    gmax_pt = max([p[3] for p in uniq] + [0])
    gmax_corner = max(cc['lambda'] for cc in corners)
    out = {'n': n, 'M': M, 'nodes': N, 'cardinal_identity_maxerr': err_id,
           'formula_vs_vandermonde_maxerr': err_v, 'cheb_vandermonde_cond': condV,
           'grid_lambda_max': float(lam.max()), 'grid_lambda_min': float(lam.min()),
           'n_seeds': int(len(seeds)), 'n_accepted_raw': int(acc.sum()),
           'interior': n_int, 'open_edge': n_edge, 'non_node_corner': n_cor,
           'closed_total': n_int + n_edge + n_cor,
           'min_abs_cardinal_at_accepted': min([p[4] for p in uniq]) if uniq else None,
           'corners': corners, 'max_noncorner_lambda': gmax_pt, 'max_corner_lambda': gmax_corner,
           'global_max_at_corners': bool(gmax_corner > gmax_pt),
           'nm_seeds': int(len(fseeds)), 'nm_unmatched': um,
           'zero_cardinal_cases': [dict(t) for t in {json.dumps(c, sort_keys=True): c for c in crease_info}.values()][:50],
           'points': [{'x': p[0], 'y': p[1], 'class': p[2], 'lambda': p[3], 'min_abs_L': p[4],
                       'mask': str(p[5])} for p in uniq],
           'seconds': time.time() - t0}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, nargs='+', default=[3, 4, 5, 6, 7, 8])
    ap.add_argument('--M', type=int, nargs='+', default=[1600])
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    res = []
    for n in args.n:
        for M in args.M:
            r = census(n, M)
            res.append(r)
            print(json.dumps({k: v for k, v in r.items() if k not in ('points', 'corners')}), flush=True)
    json.dump({'tool': 'claude-audit-01 numerical census (not proof)', 'numpy': np.__version__,
               'python': sys.version.split()[0], 'results': res}, open(args.output, 'w'), indent=1)


if __name__ == '__main__':
    main()
