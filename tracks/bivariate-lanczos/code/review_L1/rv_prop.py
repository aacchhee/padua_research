"""Exact-coefficient node propagator L*(z) (PD-T?...-104/-108) built independently, and its inverse norm.

Exact window coefficients are taken from a long-double run with full CGS2 orthogonalisation (coefficients on the
exact window only; off-window coefficients of that run are ~1e-19).  For every node z_i the lower-triangular
L*(z_i) has rows  L[k,k] = beta_k,  L[k,l] = h_l (l in exact window W_k),  L[k,p(k)] = h_p - a_k(z_i).
Reported per degree n: u * median_i ||L*(z_i)^{-1}||_2 and u * max_i (leading N_n block; float64 inverse),
validated at 3 nodes by mpmath (30 digits), and compared with the measured BJ loss.

Usage: python3 -I -u rv_prop.py > logs_L1/prop.log
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import mpmath as mp
import rv_core as C

U = 2.0 ** -53


def exact_coeffs(x, y, w, nmax, choice='dev'):
    ld = np.longdouble
    Q, rec = C.window_rec(x, y, w, nmax, choice, 'full', 'cgs2', dtype=ld, record=True)
    idx, pos = C.cols(nmax)
    rows = []
    for k in range(1, len(idx)):
        t, j = idx[k]
        op, p, W, h, beta = rec[k]
        Wex = C.window_list(op, t, j, 'exact')
        hmap = dict(zip(W, h))
        rows.append((k, op, p, [(l, float(hmap[l])) for l in Wex], float(beta)))
    return rows, idx


def build_L(rows, N, z):
    L = np.zeros((N, N)); L[0, 0] = 1.0
    for (k, op, p, hw, beta) in rows:
        if k >= N:
            break
        L[k, k] = beta
        for l, hl in hw:
            L[k, l] += hl
        L[k, p] -= (z[0] if op == 'X' else z[1])
    return L


def mp_inv_norm(L, Nn):
    mp.mp.dps = 30
    A = mp.matrix(L[:Nn, :Nn].tolist())
    # forward substitution for the inverse of a lower triangular matrix
    Inv = mp.matrix(Nn, Nn)
    for c in range(Nn):
        for r in range(c, Nn):
            s = mp.mpf(1) if r == c else mp.mpf(0)
            for k in range(c, r):
                s -= A[r, k] * Inv[k, c]
            Inv[r, c] = s / A[r, r]
    # 2-norm via largest singular value of a float copy is enough after mp inverse; use Frobenius for mp-level check
    fro = mp.sqrt(sum(Inv[i, j] ** 2 for i in range(Nn) for j in range(Nn)))
    return float(fro)


def main():
    print(f'# rv_prop.py python {sys.version.split()[0]} numpy {np.__version__} mpmath {mp.__version__}')
    nmax = 20
    degs = (4, 8, 12, 16, 20)
    for name in ('square', 'square_rot0.3', 'square_rotpi4', 'disk', 'triangle', 'tensor_cheb', 'gauss_rot0.3'):
        t0 = time.time()
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        rows, idx = exact_coeffs(x, y, w, nmax)
        N = C.N_of(nmax)
        Qb, _ = C.window_rec(x, y, w, nmax, 'dev', 'block', 'cgs')
        Lb = C.loss_profile(Qb, nmax)
        norms = np.zeros((len(x), len(degs))); fros = np.zeros((len(x), len(degs)))
        for i in range(len(x)):
            Lz = build_L(rows, N, (x[i], y[i]))
            Inv = np.linalg.inv(Lz)
            for c, n in enumerate(degs):
                Nn = C.N_of(n)
                B = Inv[:Nn, :Nn]
                norms[i, c] = np.linalg.norm(B, 2); fros[i, c] = np.linalg.norm(B, 'fro')
        imax = int(np.argmax(norms[:, -1]))
        print(f'## {name} M={len(x)} ({time.time() - t0:.0f}s)')
        print('   n          : ' + ' '.join(f'{n:8d}' for n in degs))
        print('   BJ loss    : ' + ' '.join(f'{Lb[n]:8.1e}' for n in degs))
        print('   u*med||L^-1||: ' + ' '.join(f'{U * np.median(norms[:, c]):8.1e}' for c in range(len(degs))))
        print('   u*max||L^-1||: ' + ' '.join(f'{U * np.max(norms[:, c]):8.1e}' for c in range(len(degs))))
        print(f'   argmax node at n={degs[-1]}: z = ({x[imax]:+.3f}, {y[imax]:+.3f}), |z| = {np.hypot(x[imax], y[imax]):.3f}')
        # where are the large propagators: correlation with distance to the support boundary is reported as quantiles
        q = np.quantile(norms[:, -1], [0.1, 0.5, 0.9, 1.0])
        print(f'   ||L^-1|| quantiles at n={degs[-1]} (10/50/90/100%): {q[0]:.1e} {q[1]:.1e} {q[2]:.1e} {q[3]:.1e}')
        # mpmath validation at 3 nodes for n = 16
        Nn = C.N_of(16)
        for i in (0, imax, len(x) // 2):
            Lz = build_L(rows, N, (x[i], y[i]))
            f64 = fros[i, degs.index(16)]
            fm = mp_inv_norm(Lz, Nn)
            print(f'   mp check node {i:5d}: ||L^-1||_F (n=16) float64 {f64:.6e}  mpmath(30) {fm:.6e}  rel diff {abs(f64 - fm) / fm:.1e}')
        sys.stdout.flush()


if __name__ == '__main__':
    main()
