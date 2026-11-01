"""R07 (IDEA?bivariate-lanczos-claude-118): anatomy of the BJ off-pattern coefficient errors on checkerboards.
Split h_off = phi + rho (phi = long-double inner product of the stored double vectors, rho = rounding of the
double dot product); nonlinear long-double Gram defects D(c* + delta) with delta on the off-pattern entries only:
phi, rho, independent term-wise rounding model, |h| with random signs.  Descriptive: sizes on the largest-gain
entries (gains from PD-T?...-114).  MEASURED only.  Usage: python3 -I l1_r07_offpattern_anatomy.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
import l1_r06_coefficient_channel as K
import l1_r06_gain_identity as G

LD = np.longdouble
EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2


def with_off(cst, masks, off, N):
    """c* with the off-pattern entries replaced by off[k] (arrays over the window)"""
    out = [None] * N
    for k in range(1, N):
        W, h, beta = cst[k]
        out[k] = (W, np.where(masks[k], np.asarray(h, dtype=LD), np.asarray(off[k], dtype=LD)), beta)
    return out


def run(name, X, Y, nmax=24, seeds=(0, 1, 2), ngain=20, top=100):
    P, w, wx, wy = C.checkerboard(X, Y); x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, cbj, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    idx, pos, parent, op, start = tab; N = Q.shape[1]
    Gm = Q.T @ Q; loss = {n: float(np.abs(Gm[:Nof(n), :Nof(n)] - np.eye(Nof(n))).max()) for n in (8, 12, 16, 20, 24)}
    ax, bx = K.jacobi_1d_ld(X, wx, nmax); ay, by = K.jacobi_1d_ld(Y, wy, nmax)
    cst = K.ref_coefs(ax, bx, ay, by, tab); masks = K.pattern_mask(tab, N)
    Xi = G.build_xi(cst, x, y, w, tab, N); xl, yl = x.astype(LD), y.astype(LD)
    hbj, phi, rho, s_abs, s_two = [None] * N, [None] * N, [None] * N, [None] * N, [None] * N
    term = {sd: [None] * N for sd in seeds}; sign = {sd: [None] * N for sd in seeds}
    rngs_t = {sd: np.random.default_rng(100 + sd) for sd in seeds}; rngs_s = {sd: np.random.default_rng(200 + sd) for sd in seeds}
    for k in range(1, N):
        W, h, beta = cbj[k]; p = parent[k]; a = x if op[k] == 'J' else y
        u0 = a * Q[:, p]                                      # as in l1_recurrence.recurrence (double)
        hbj[k] = np.asarray(h, dtype=LD)
        phi[k] = Q[:, W].astype(LD).T @ u0.astype(LD); rho[k] = hbj[k] - phi[k]
        al = xl if op[k] == 'J' else yl
        prod = Xi[:, W].T * (al * Xi[:, p])[None, :]          # (|W|, M): xi*_l (a xi*_p) term-wise
        s_abs[k] = np.sum(np.abs(prod), axis=1); s_two[k] = np.sqrt(np.sum(prod * prod, axis=1))
        for sd in seeds:
            E = rngs_t[sd].standard_normal(prod.shape).astype(LD)
            term[sd][k] = LD(EPS) * np.sum(E * prod, axis=1)
            sign[sd][k] = np.abs(hbj[k]) * np.where(rngs_s[sd].random(len(W)) < 0.5, -1, 1).astype(LD)
    rows = [('BJ loss L(n)', loss),
            ('D(c* + h_BJ off)', K.xi_from(with_off(cst, masks, hbj, N), x, y, w, tab, N)),
            ('D(c* + phi off)  [feedback part]', K.xi_from(with_off(cst, masks, phi, N), x, y, w, tab, N)),
            ('D(c* + rho off)  [rounding part]', K.xi_from(with_off(cst, masks, rho, N), x, y, w, tab, N))]
    for lab, dd in [('D(c* + term-wise rounding model), median', term), ('D(c* + |h_BJ| random signs), median', sign)]:
        res = [K.xi_from(with_off(cst, masks, dd[sd], N), x, y, w, tab, N) for sd in seeds]
        rows.append((lab, {n: float(np.median([r[n] for r in res])) for n in res[0]}))
    offv = lambda arr: np.concatenate([np.abs(np.asarray(arr[k], dtype=float))[~masks[k]] for k in range(1, N)])
    print(f"== {name} (M={len(x)}): max off-pattern |h_BJ| {offv(hbj).max():.1e}, |phi| {offv(phi).max():.1e}, "
          f"|rho| {offv(rho).max():.1e}", flush=True)
    for lab, d in rows:
        print(f"   {lab:42s} " + " ".join(f"n{n}:{v:.2e}" for n, v in d.items()), flush=True)
    # descriptive: largest-gain off-pattern entries (gains at degree <= ngain, PD-T?...-114 formula)
    uni = (G.univ(X, ax, bx, nmax), G.univ(Y, ay, by, nmax), wx, wy, X, Y, ax, bx, ay, by)
    ent = []
    for k in range(1, Nof(ngain)):
        W = cst[k][0]
        for ii, l in enumerate(W):
            if masks[k][ii]:
                continue
            A = G.formula_A(k, l, tab, ngain, *uni); gn = float(np.abs((A + A.T).astype(float)).max())
            ent.append((gn, k, ii))
    ent.sort(reverse=True); sel = ent[:top]
    def med(arr, scale=1.0):
        return float(np.median([abs(float(arr[k][ii])) * scale for (_, k, ii) in sel]))
    gmed = float(np.median([g for (g, _, _) in sel]))
    print(f"   top-{top} gain entries (n<={ngain}): median gain {gmed:.1e}; medians |h_BJ| {med(hbj):.1e}, |phi| {med(phi):.1e}, "
          f"|rho| {med(rho):.1e}, u*s {med(s_abs, EPS):.1e}, u*s2 {med(s_two, EPS):.1e}", flush=True)
    for lab, arr in [('h_BJ', hbj), ('phi', phi), ('rho', rho)]:
        c = sorted((g * abs(float(arr[k][ii])) for (g, k, ii) in ent), reverse=True)
        print(f"   gain*|{lab}| over all off-pattern entries: largest {c[0]:.1e}, 10th {c[9]:.1e}, 100th {c[99]:.1e}", flush=True)
    c = sorted((g * EPS * float(s_two[k][ii]) for (g, k, ii) in ent), reverse=True)
    print(f"   gain*u*s2 over all off-pattern entries:  largest {c[0]:.1e}, 10th {c[9]:.1e}, 100th {c[99]:.1e}", flush=True)


if __name__ == '__main__':
    print(f"# l1_r07_offpattern_anatomy.py numpy={np.__version__}")
    m = 30
    s1, s2 = np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)
    run('cubic-clustered checkerboard m=30', s1 * np.abs(s1) ** 2, s2 * np.abs(s2) ** 2)
    run('equispaced checkerboard m=30 (control, descriptive)', s1, s2)
