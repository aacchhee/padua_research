"""R07 (IDEA?bivariate-lanczos-claude-119): a-priori loss estimate on checkerboards from exact data only:
E(n) = median over seeds of D(c* + delta), delta_{k,l} = u sum_i eps_i xi*_{i,l} (a xi*_p)_i on the off-pattern
window entries (eps iid N(0,1)); compared with the BJ block-CGS loss L(n).  MEASURED only.
Usage: python3 -I l1_r07_termwise_predictor.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C
import l1_r06_coefficient_channel as K
import l1_r06_gain_identity as G
import l1_r07_offpattern_anatomy as A

LD = np.longdouble
EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2


def run(name, X, Y, nmax=24, seeds=(0, 1, 2)):
    P, w, wx, wy = C.checkerboard(X, Y); x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, cbj, tab = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    idx, pos, parent, op, start = tab; N = Q.shape[1]
    Gm = Q.T @ Q; loss = {n: float(np.abs(Gm[:Nof(n), :Nof(n)] - np.eye(Nof(n))).max()) for n in (8, 12, 16, 20, 24)}
    ax, bx = K.jacobi_1d_ld(X, wx, nmax); ay, by = K.jacobi_1d_ld(Y, wy, nmax)
    cst = K.ref_coefs(ax, bx, ay, by, tab); masks = K.pattern_mask(tab, N)
    Xi = G.build_xi(cst, x, y, w, tab, N); xl, yl = x.astype(LD), y.astype(LD)
    res = []
    for sd in seeds:
        rng = np.random.default_rng(100 + sd); off = [None] * N
        for k in range(1, N):
            W = cst[k][0]; p = parent[k]; al = xl if op[k] == 'J' else yl
            prod = Xi[:, W].T * (al * Xi[:, p])[None, :]
            off[k] = LD(EPS) * np.sum(rng.standard_normal(prod.shape).astype(LD) * prod, axis=1)
        res.append(K.xi_from(A.with_off(cst, masks, off, N), x, y, w, tab, N))
    est = {n: float(np.median([r[n] for r in res])) for n in res[0]}
    floor = K.xi_from(cst, x, y, w, tab, N)
    print(f"== {name} (M={len(x)}, weights {w.min():.1e}..{w.max():.1e})", flush=True)
    for lab, d in [('BJ loss L(n)', loss), ('estimate E(n)', est), ('D(c*) floor', floor)]:
        print(f"   {lab:14s} " + " ".join(f"n{n}:{v:.2e}" for n, v in d.items()), flush=True)
    print("   ratio E/L     " + " ".join(f"n{n}:{est[n] / loss[n]:.2f}" for n in loss), flush=True)
    return loss, est


if __name__ == '__main__':
    print(f"# l1_r07_termwise_predictor.py numpy={np.__version__}")
    out = {}
    for name, m, f in [('quadratic clustering s|s|, m=30', 30, lambda s: s * np.abs(s)),
                       ('quartic clustering s|s|^3, m=30', 30, lambda s: s * np.abs(s) ** 3),
                       ('cubic clustering s|s|^2, m=36', 36, lambda s: s * np.abs(s) ** 2),
                       ('Chebyshev-Lobatto, m=30', 30, None)]:
        if f is None:
            X, Y = np.cos(np.pi * np.arange(m + 1) / m), np.cos(np.pi * np.arange(m + 2) / (m + 1))
        else:
            X, Y = f(np.linspace(-1, 1, m + 1)), f(np.linspace(-1, 1, m + 2))
        out[name] = run(name, X, Y)
    verdicts = []
    for name, (loss, est) in out.items():
        if loss[20] >= 1e-13:
            r = [est[n] / loss[n] for n in (16, 20)]
            v = 'killed' if any(x < 0.01 or x > 100 for x in r) else ('survives' if all(0.1 <= x <= 10 for x in r) else 'inconclusive')
        else:
            v = 'survives' if est[20] < 1e-12 else ('killed' if est[20] >= 1e-11 else 'inconclusive')
        verdicts.append(v); print(f"   verdict on {name}: {v}")
    order = {'survives': 0, 'inconclusive': 1, 'killed': 2}
    print(f"# overall (worst over sets): {max(verdicts, key=order.get)}")
