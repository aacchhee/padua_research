"""Convention-free check of PD-T?bivariate-lanczos-claude-115 (c): is the clustered-checkerboard BJ loss carried by the
rounding of the window dot products, fed back through the recurrence?

Modes (BJ dev rule, block window, one CGS pass, Harris-Simanek checkerboards m = 30, e = 0):
  double        : the whole recurrence in IEEE double (reference loss L)
  dot64         : everything in long double EXCEPT the window inner products, which are computed by an actual
                  IEEE-double BLAS product of the double-rounded vectors (Q_W^T u in float64); no noise model
  noise(sigma)  : everything in long double; each inner product = long-double value + sigma*u*sum_i eps_i q_il u0_i,
                  eps iid N(0,1), u = 2^-53 (plan's unit roundoff), sigma in {1/sqrt(3), 1, 2} (3 seeds, median)
  long double   : everything in long double (floor)
Usage: python3 -I -u rv2_closed_loop.py > logs_L1b/closed_loop.log
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_L1'))
import numpy as np
import rv_core as C
from rv2_checkerboard import checkerboard, gram_defect

ld = np.longdouble
U = 2.0 ** -53


def bj_mode(P, w, nmax, mode, sigma=1.0, seed=0):
    rng = np.random.default_rng(seed)
    idx, pos = C.cols(nmax)
    x = P[:, 0].astype(ld); y = P[:, 1].astype(ld)
    M, N = len(x), len(idx)
    Q = np.zeros((M, N), dtype=ld)
    s = np.sqrt(w.astype(ld)); Q[:, 0] = s / np.sqrt(s @ s)
    for k in range(1, N):
        t, j = idx[k]
        op, par = C.rule('dev', t, j)
        p = pos[par]
        u0 = (x if op == 'X' else y) * Q[:, p]
        W = C.window_list(op, t, j, 'block')
        Qw = Q[:, W]
        if mode == 'dot64':
            h = (Qw.astype(np.float64).T @ u0.astype(np.float64)).astype(ld)
        else:
            h = Qw.T @ u0
            if mode == 'noise':
                eps = rng.standard_normal((M, len(W)))
                h = h + ld(sigma * U) * np.sum(eps * (Qw * u0[:, None]), axis=0)
        r = u0 - Qw @ h
        Q[:, k] = r / np.sqrt(r @ r)
    return Q


def main():
    m, nmax = 30, 24
    degs = (12, 16, 20, 24)
    print(f'# rv2_closed_loop.py numpy {np.__version__}; u = 2^-53; checkerboards m = {m}')
    for fam in ('cubic', 'equi'):
        P, w, _, _ = checkerboard(fam, m)
        Qd, _ = C.window_rec(P[:, 0].astype(float), P[:, 1].astype(float), w.astype(float), nmax, 'dev', 'block', 'cgs')
        L = [gram_defect(Qd.astype(ld), n) for n in degs]
        print(f'## {fam}')
        print('   double BJ loss L(n), n=12,16,20,24:        ' + ' '.join(f'{v:.1e}' for v in L))
        Q = bj_mode(P, w, nmax, 'dot64')
        D = [gram_defect(Q, n) for n in degs]
        print('   dot64 (only dot products in double):       ' + ' '.join(f'{v:.1e}' for v in D) + '   ratio to L: ' + ' '.join(f'{a / b:.2f}' for a, b in zip(D, L)))
        for sig in (1 / np.sqrt(3), 1.0, 2.0):
            Ds = np.median([[gram_defect(bj_mode(P, w, nmax, 'noise', sig, sd), n) for n in degs] for sd in range(3)], axis=0)
            print(f'   noise model sigma={sig:.3f}u (median of 3):     ' + ' '.join(f'{v:.1e}' for v in Ds) + '   ratio to L: ' + ' '.join(f'{a / b:.2f}' for a, b in zip(Ds, L)))
        Q = bj_mode(P, w, nmax, 'ld')
        print('   all long double:                           ' + ' '.join(f'{gram_defect(Q, n):.1e}' for n in degs))
        sys.stdout.flush()


if __name__ == '__main__':
    main()
