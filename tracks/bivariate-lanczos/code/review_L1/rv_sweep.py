"""Independent reruns for the MEASURED claims of L1 (PD-N?...-101/-102, PD-T?...-107/-109).

Usage (from this directory):  python3 -I rv_sweep.py <part> > <log>
parts:
  loss      loss vs degree (every degree) for BJ (dev, block, cgs), HL (dev, exact, mgs2), two-relation, full
            reference, in float64 and float32, on all node sets; growth fits
  ritz      loss vs u/rho for H_x, H_y, Z on computed span and exact span (selected sets); tensor grid n=34..40
  alt       alternative explanations: within-degree selection rules (dev / mirror / alt / adapt), deeper windows,
            window CGS2, non-product weights on the square, Gaussian clouds, pivot sizes
  M         M-dependence of the growth (square rotated pi/4, disk) for M = 1681, 6724, 26896
Seeds: node_set(..., seed=20261031) (+1..+6 per shape).  Floating point results are MEASURED only.
"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # own review code only
import numpy as np
import rv_core as C

U64 = 2.0 ** -53      # unit roundoff (IEEE double)
U32 = 2.0 ** -24      # unit roundoff (IEEE single)


def fmt(v):
    return ' '.join(f'{a:.1e}' for a in v)


def fit_growth(L, n0, n1):
    """least squares fits of log10 L on [n0, n1]: linear (exponential growth) and quadratic in n"""
    n = np.arange(n0, n1 + 1); y = np.log10(np.maximum(np.asarray(L)[n0:n1 + 1], 1e-300))
    p1 = np.polyfit(n, y, 1); p2 = np.polyfit(n, y, 2)
    r1 = np.sqrt(np.mean((np.polyval(p1, n) - y) ** 2)); r2 = np.sqrt(np.mean((np.polyval(p2, n) - y) ** 2))
    return p1, r1, p2, r2


def part_loss():
    sets = ['square', 'square_rot0.05', 'square_rot0.3', 'square_rotpi4', 'disk', 'triangle', 'triangle_eq',
            'annulus', 'tensor_cheb', 'tensor_cheb_rot0.3', 'gauss', 'gauss_rot0.3']
    nmax = 24
    for name in sets:
        P, w = C.node_set(name)
        x, y = P[:, 0], P[:, 1]
        t0 = time.time()
        res = {}
        for dt, lab in ((np.float64, 'f64'), (np.float32, 'f32')):
            Q, _ = C.window_rec(x, y, w, nmax, 'dev', 'block', 'cgs', dtype=dt); res['bj_' + lab] = C.loss_profile(Q, nmax)
            Q, _ = C.window_rec(x, y, w, nmax, 'dev', 'exact', 'mgs2', dtype=dt); res['hl_' + lab] = C.loss_profile(Q, nmax)
            Q = C.two_relation(x, y, w, nmax, dtype=dt); res['two_' + lab] = C.loss_profile(Q, nmax)
        Q, _ = C.window_rec(x, y, w, nmax, 'dev', 'full', 'cgs', dtype=np.float64); res['fullcgs_f64'] = C.loss_profile(Q, nmax)
        print(f'## {name}  M={len(x)}  ({time.time() - t0:.0f}s)')
        for k, v in res.items():
            print(f'   {k:12s} n=0..{nmax}: {fmt(v)}')
        # float32/float64 ratio at degrees where both are in the linear regime (f32 loss < 1e-2)
        r = [res['bj_f32'][n] / res['bj_f64'][n] for n in range(nmax + 1)]
        ok = [n for n in range(nmax + 1) if res['bj_f32'][n] < 1e-2 and res['bj_f64'][n] > 1e-14]
        print(f'   ratio bj f32/f64 at n in {ok}: {fmt([r[n] for n in ok])}  (u32/u64 = {U32 / U64:.2e})')
        # growth fit on the segment where loss in [1e-13, 1e-2] (f64 BJ)
        L = res['bj_f64']; seg = [n for n in range(nmax + 1) if 1e-13 <= L[n] <= 1e-2]
        if len(seg) >= 5:
            p1, r1, p2, r2 = fit_growth(L, seg[0], seg[-1])
            print(f'   growth fit bj f64 on n={seg[0]}..{seg[-1]}: linear slope {p1[0]:.3f} dec/deg (rms {r1:.2f}); '
                  f'quadratic coef {p2[0]:.4f} dec/deg^2 (rms {r2:.2f}); per-degree increments {fmt(np.diff(np.log10(L[seg[0]:seg[-1]+1])))}')
        print(json.dumps({'set': name, **res}), file=sys.stderr)
        sys.stdout.flush()


def ritz_row(U, x, y, n):
    Nn = C.N_of(n); Un = U[:, :Nn]
    return C.min_ritz(Un, x), C.min_ritz(Un, y), C.min_ritz(Un, x + 1j * y, hermitian=False)


def part_ritz():
    sets = ['square', 'square_rot0.3', 'square_rotpi4', 'disk', 'triangle', 'tensor_cheb', 'gauss_rot0.3']
    for name in sets:
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        nmax = 40 if name == 'tensor_cheb' else 32
        if name == 'tensor_cheb':
            degs = list(range(4, 33, 4)) + list(range(33, 41))
        else:
            degs = list(range(4, nmax + 1, 4))
        Qb, _ = C.window_rec(x, y, w, nmax, 'dev', 'block', 'cgs')
        Qf, _ = C.window_rec(x, y, w, nmax, 'dev', 'full', 'cgs2')
        Lb = C.loss_profile(Qb, nmax)
        Ub, _ = np.linalg.qr(Qb)
        print(f'## {name} M={len(x)}  columns: n loss_bj | computed span: u/rho_X u/rho_Y u/rho_Z | exact span: u/rho_X u/rho_Y u/rho_Z')
        for n in degs:
            if C.N_of(n) > len(x):
                break
            rc = ritz_row(Ub, x, y, n); re = ritz_row(Qf, x, y, n)
            print(f'   n={n:2d} loss={Lb[n]:.1e} | {U64/rc[0]:.1e} {U64/rc[1]:.1e} {U64/rc[2]:.1e} | {U64/re[0]:.1e} {U64/re[1]:.1e} {U64/re[2]:.1e}')
        sys.stdout.flush()


def part_alt():
    nmax = 24
    sets = ['square', 'square_rot0.3', 'square_rotpi4', 'disk', 'triangle']
    print('# A. within-degree selection rule (block window, CGS, float64): loss at n = 8, 12, 16, 20, 24')
    for name in sets:
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        for ch in ('dev', 'mirror', 'alt', 'adapt'):
            Q, _ = C.window_rec(x, y, w, nmax, ch, 'block', 'cgs')
            L = C.loss_profile(Q, nmax)
            print(f'   {name:14s} {ch:7s} {fmt([L[n] for n in (8, 12, 16, 20, 24)])}')
        sys.stdout.flush()
    print('# B. window depth d (degrees t-d..t-1 plus current degree), dev choice, CGS; and window CGS2 (d=2)')
    for name in ('square_rot0.3', 'square_rotpi4', 'disk', 'triangle'):
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        for d in (2, 3, 4, 6, 10):
            Q, _ = C.window_rec(x, y, w, nmax, 'dev', 'block', 'cgs', depth=d)
            L = C.loss_profile(Q, nmax)
            print(f'   {name:14s} depth={d:2d} cgs  {fmt([L[n] for n in (8, 12, 16, 20, 24)])}')
        Q, _ = C.window_rec(x, y, w, nmax, 'dev', 'block', 'cgs2')
        L = C.loss_profile(Q, nmax)
        print(f'   {name:14s} depth= 2 cgs2 {fmt([L[n] for n in (8, 12, 16, 20, 24)])}')
        Q = C.two_relation(x, y, w, nmax, passes=2)
        L = C.loss_profile(Q, nmax)
        print(f'   {name:14s} two-relation (2 passes) {fmt([L[n] for n in (8, 12, 16, 20, 24)])}')
        sys.stdout.flush()
    print('# C. product support with non-product weights exp(c x y) on the square; Gaussian clouds (product measures, rotated)')
    for name in ('square_w1', 'square_w4', 'square_w8', 'gauss', 'gauss_rot0.3', 'gauss_aniso', 'gauss_aniso_rot0.3'):
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        Q, _ = C.window_rec(x, y, w, nmax, 'dev', 'block', 'cgs')
        L = C.loss_profile(Q, nmax)
        print(f'   {name:20s} bj {fmt([L[n] for n in (8, 12, 16, 20, 24)])}')
        sys.stdout.flush()
    print('# D. pivots: min over columns of degree t of beta_k / ||A q_parent|| (BJ run), and exact within-degree coupling '
          'max_{r<j} |h_(t,r)| / beta (full-reorth run), t = 4, 8, 12, 16, 20')
    for name in ('square', 'square_rot0.3', 'square_rotpi4', 'disk', 'triangle', 'tensor_cheb'):
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        Q, rec = C.window_rec(x, y, w, 20, 'dev', 'full', 'cgs2', record=True)
        idx, pos = C.cols(20)
        piv = {}; cpl = {}
        for k in range(1, len(idx)):
            t, j = idx[k]
            op, p, W, h, beta = rec[k]
            a = (x if op == 'X' else y) * Q[:, p]
            piv[t] = min(piv.get(t, 1e9), beta / np.linalg.norm(a))
            cur = [hh for l, hh in zip(W, h) if idx[l][0] == t]
            if cur:
                cpl[t] = max(cpl.get(t, 0.0), float(np.max(np.abs(cur))) / beta)
        print(f'   {name:14s} min beta/||Aq||: {fmt([piv[t] for t in (4, 8, 12, 16, 20)])} | coupling: {fmt([cpl.get(t, 0) for t in (4, 8, 12, 16, 20)])}')
        sys.stdout.flush()


def part_M():
    nmax = 22
    for name in ('square_rotpi4', 'disk', 'square'):
        for M in (1681, 6724, 26896):
            P, w = C.node_set(name, M=M); x, y = P[:, 0], P[:, 1]
            t0 = time.time()
            Q, _ = C.window_rec(x, y, w, nmax, 'dev', 'block', 'cgs')
            L = C.loss_profile(Q, nmax)
            print(f'   {name:14s} M={M:6d} bj loss n=8..22 step 2: {fmt(L[8::2])}  ({time.time() - t0:.0f}s)')
            sys.stdout.flush()


if __name__ == '__main__':
    part = sys.argv[1]
    print(f'# rv_sweep.py {part}  python {sys.version.split()[0]} numpy {np.__version__}  u64={U64:.3e} u32={U32:.3e}')
    {'loss': part_loss, 'ritz': part_ritz, 'alt': part_alt, 'M': part_M}[part]()
