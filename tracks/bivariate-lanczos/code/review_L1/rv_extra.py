"""Extra independent checks for the L1 review.
 (i)  complex windowed (N, N*) recurrence (HL SIMAX 2002 Algorithm 1 as described in PD-N?...-102 and re-derived
      here: N* applied to the first vector of each cycle, N to the others; window of the N-product of (k-1, s-1):
      cycle k-2 from index s-1, cycle k-1, cycle k up to s-1; window of the N*-product: cycles k-2, k-1), with
      CGS, ORTH (MGS + conditional second pass) and full orthogonalisation; loss = max|Q^H Q - I|.
 (ii) Ritz residuals vs loss for BJ and the two-relation recurrence on the Gaussian cloud and on the square with
      weights exp(8xy).
 (iii) T-102 part 1: measured local errors f_k = A q_p - Q_W h - beta q_k (evaluated in long double from a double
      BJ run) against the first-order bound [(w+2)(1 + kappa sqrt(w) mu) + 1] u ||A|| mu.
Usage: python3 -I -u rv_extra.py > logs_L1/extra.log
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rv_core as C

U = 2.0 ** -53


def simax(x, y, w, nmax, orth='orth', win='listing'):
    z = x + 1j * y
    idx, pos = C.cols(nmax)
    M, N = len(z), len(idx)
    Q = np.zeros((M, N), dtype=complex)
    s0 = np.sqrt(w).astype(complex); Q[:, 0] = s0 / np.linalg.norm(s0)
    for k in range(1, N):
        t, s = idx[k]
        if s == 0:
            u = np.conj(z) * Q[:, pos[(t - 1, 0)]]
            W = list(range(C.start_of(max(t - 2, 0)), k))
        else:
            u = z * Q[:, pos[(t - 1, s - 1)]]
            lo = C.start_of(t - 2) + (s - 1) if t >= 2 else 0
            W = list(range(lo, k))
        if win == 'full':
            W = list(range(0, k))
        Qw = Q[:, W]
        if orth == 'cgs':
            u = u - Qw @ (Qw.conj().T @ u)
        else:
            n0 = np.linalg.norm(u)
            for _ in range(2):
                for i in range(Qw.shape[1]):
                    u = u - (np.vdot(Qw[:, i], u)) * Qw[:, i]
                n1 = np.linalg.norm(u)
                if n1 > 0.707 * n0:
                    break
                n0 = n1
        Q[:, k] = u / np.linalg.norm(u)
    return Q


def closs(Q, n):
    Nn = C.N_of(n); G = Q[:, :Nn].conj().T @ Q[:, :Nn]
    return float(np.max(np.abs(G - np.eye(Nn))))


def part_simax():
    print('# (i) complex windowed (N, N*) recurrence: loss at n = 4, 8, 12, 16, 20, 24')
    for name in ('square', 'tensor_cheb', 'square_rot0.3', 'disk'):
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        for orth, win in (('orth', 'listing'), ('cgs', 'listing'), ('orth', 'full')):
            Q = simax(x, y, w, 24, orth, win)
            print(f'   {name:14s} {orth:4s} {win:8s} ' + ' '.join(f'{closs(Q, n):.1e}' for n in (4, 8, 12, 16, 20, 24)))
        sys.stdout.flush()


def part_ritz_extra():
    print('# (ii) loss vs u/rho (exact span) for BJ and two-relation; n, loss_bj, loss_two, u/rho_X, u/rho_Y, u/rho_Z')
    for name in ('gauss', 'square_w8', 'square_w4'):
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        Qb, _ = C.window_rec(x, y, w, 28, 'dev', 'block', 'cgs'); Lb = C.loss_profile(Qb, 28)
        Qt = C.two_relation(x, y, w, 28); Lt = C.loss_profile(Qt, 28)
        Qf, _ = C.window_rec(x, y, w, 28, 'dev', 'full', 'cgs2')
        for n in (8, 12, 16, 20, 24, 28):
            Un = Qf[:, :C.N_of(n)]
            r = (C.min_ritz(Un, x), C.min_ritz(Un, y), C.min_ritz(Un, x + 1j * y, hermitian=False))
            print(f'   {name:10s} n={n:2d} bj={Lb[n]:.1e} two={Lt[n]:.1e} | {U / r[0]:.1e} {U / r[1]:.1e} {U / r[2]:.1e}')
        sys.stdout.flush()


def part_local_errors():
    print('# (iii) T-102 part 1: max_k ||f_k|| / (u ||A|| mu) measured vs first-order constant (BJ, block window, CGS)')
    ld = np.longdouble
    for name in ('square', 'square_rotpi4', 'triangle'):
        P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
        Q, rec = C.window_rec(x, y, w, 20, 'dev', 'block', 'cgs', record=True)
        idx, _ = C.cols(20)
        worst_ratio = 0.0; worst_meas = 0.0
        mu = float(np.max(np.linalg.norm(Q, axis=0)))
        for k in range(1, len(idx)):
            op, p, W, h, beta = rec[k]
            a = (x if op == 'X' else y)
            f = a.astype(ld) * Q[:, p].astype(ld) - Q[:, W].astype(ld) @ h.astype(ld) - ld(beta) * Q[:, k].astype(ld)
            nf = float(np.sqrt(np.sum(f * f)))
            normA = float(np.max(np.abs(a)))
            wk = len(W); kap = float(np.linalg.norm(Q[:, W], 2)) if wk else 0.0
            bound = ((wk + 2) * (1 + kap * np.sqrt(wk) * mu) + 1) * U * normA * mu
            worst_ratio = max(worst_ratio, nf / bound)
            worst_meas = max(worst_meas, nf / (U * normA * mu))
        print(f'   {name:14s} max ||f_k||/(u||A||mu) = {worst_meas:.2f};  max ||f_k|| / bound = {worst_ratio:.3f} (must be <= 1)')
        sys.stdout.flush()


if __name__ == '__main__':
    print(f'# rv_extra.py python {sys.version.split()[0]} numpy {np.__version__}')
    part_simax()
    part_ritz_extra()
    part_local_errors()
