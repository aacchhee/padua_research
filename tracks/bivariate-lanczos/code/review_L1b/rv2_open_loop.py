"""Convention-free open-loop estimate for IDEA?bivariate-lanczos-claude-119 / PD-N?...-104 (c): add to the exact
product-type coefficients c* the ACTUAL IEEE-double rounding error of the window dot products of the exact vectors
(rho_kl = fl64(xi*_l^T (a xi*_p)) - long-double value), on off-pattern entries only (as in IDEA-119's model) and on all
window entries, and compare E(n) = D(c* + rho) with the double BJ loss L(n). No noise model, no u convention.
Usage: python3 -I -u rv2_open_loop.py > logs_L1b/open_loop.log
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_L1'))
import numpy as np
import rv_core as C
import rv2_checkerboard as CB

ld = np.longdouble


def abscissae(fam, npts):
    s = np.linspace(-1, 1, npts, dtype=ld)
    return {'quad': s * np.abs(s), 'cubic': s ** 3, 'quart': s * np.abs(s) ** 3,
            'lobatto': -np.cos(np.pi * np.arange(npts, dtype=ld) / (npts - 1))}[fam]


CB.abscissae = abscissae      # extend the family list (own module)


def main():
    nmax = 24; degs = (12, 16, 20, 24)
    print(f'# rv2_open_loop.py numpy {np.__version__}; open loop with actual double dot-product rounding on exact vectors')
    for fam, m in (('quad', 30), ('cubic', 30), ('quart', 30), ('cubic', 36), ('lobatto', 30)):
        P, w, (xs, a), (ys, b) = CB.checkerboard(fam, m)
        x64, y64, w64 = P[:, 0].astype(float), P[:, 1].astype(float), w.astype(float)
        Q, rec = C.window_rec(x64, y64, w64, nmax, 'dev', 'block', 'cgs', record=True)
        L = [CB.gram_defect(Q.astype(ld), n) for n in degs]
        idx, pos = C.cols(nmax)
        ax, bx = CB.jacobi(xs, a, m); ay, by = CB.jacobi(ys, b, m + 1)
        cstar = CB.product_coeffs(rec, idx, pos, ax, bx, ay, by)
        Xs = CB.xi_map(P, w, rec, cstar, nmax)
        X = P[:, 0].astype(ld); Y = P[:, 1].astype(ld)
        c_off = [None]; c_all = [None]
        for k in range(1, len(idx)):
            op, p, W, _, _ = rec[k]
            u0 = (X if op == 'X' else Y) * Xs[:, p]
            exact = Xs[:, W].T @ u0
            fl = (Xs[:, W].astype(np.float64).T @ u0.astype(np.float64)).astype(ld)
            rho = fl - exact
            mask = np.array([CB.on_pattern(k, l, idx) for l in W], dtype=bool)
            hs, bs = cstar[k]
            c_off.append((hs + np.where(mask, 0, rho), bs))
            c_all.append((hs + rho, bs))
        Eoff = [CB.gram_defect(CB.xi_map(P, w, rec, c_off, nmax), n) for n in degs]
        Eall = [CB.gram_defect(CB.xi_map(P, w, rec, c_all, nmax), n) for n in degs]
        print(f'## {fam} m={m}')
        print('   double BJ loss L(n), n=12,16,20,24:          ' + ' '.join(f'{v:.1e}' for v in L))
        print('   open loop, actual rounding, off-pattern only: ' + ' '.join(f'{v:.1e}' for v in Eoff) + '   E/L: ' + ' '.join(f'{e / l:.2f}' for e, l in zip(Eoff, L)))
        print('   open loop, actual rounding, all entries:      ' + ' '.join(f'{v:.1e}' for v in Eall) + '   E/L: ' + ' '.join(f'{e / l:.2f}' for e, l in zip(Eall, L)))
        sys.stdout.flush()


if __name__ == '__main__':
    main()
