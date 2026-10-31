"""R06 (MEASURED): linearised weight-only backward fit of the COMPUTED partial coefficient data.

Overdetermined case (M >= dim Pi_{2n+1}): the tangent space of the consistent-section manifold at
Phi(mu) is spanned by node-weight perturbations, so the best consistent fit near Phi(mu) is, to first
order, min_eta || Jac eta - e ||, e = computed - exact partial entries, Jac = d(partial entries)/d(eta).
Derivative of sections wrt weights (orthonormal basis Q of the weighted graded space, R diag > 0):
 D = diag(eta/w), K = Q^T D Q, S = strict_upper(K) + diag(K)/2, dQ = D Q/2 - Q S,
 dH_A = Q^T D A Q - S^T H_A - H_A S   (A = X or Y diagonal).
Partial entries: every computed F-coefficient (window rows incl. block-window extras, and beta) of
the columns of degree <= n with rows of degree <= n, and the computed J-columns (t,0), t <= n-1
(rows of degree <= n).  Reports, per n: loss, ||e|| (forward error of the partial data, max-norm),
rho = ||Jac eta* - e||_2 / ||e||_2, the residual in max-norm, and max|eta*|/min(w).
Imports L1's library read-only.
Usage: python3 r06_weight_fit.py set nmin nmax
"""
import os
import sys
import numpy as np
from numpy.polynomial import chebyshev as Ch

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'L1'))
import l1_recurrence as L1  # noqa: E402
from r06_consistency import cheb_vander  # noqa: E402


def main():
    which, nmin, nmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    if which == 'random':
        P, w = L1.nodes_random(1681, 0)
    elif which == 'rot03':
        P, w = L1.nodes_random(1681, 0); P = L1.rotate(P, 0.3)
    else:
        raise SystemExit(which)
    x, y = P[:, 0], P[:, 1]
    w = np.asarray(w, float); w = w / w.sum()
    M = len(x)
    Q, coef, (idx, pos, parent, op, start) = L1.recurrence(x, y, w, nmax + 1, win='block', orth='cgs')
    Ve = cheb_vander(x, y, idx) * np.sqrt(w)[:, None]
    NQ = start[nmax + 1]
    QeAll, R = np.linalg.qr(Ve[:, :NQ]); QeAll = QeAll * np.sign(np.diag(R))
    print(f"set={which} M={M} weight-only linearised fit; D(2n+1) must be <= M (overdetermined)")
    print(" n    N  D2n+1  loss      |e|max    rho(2)   resid_max  max|eta|/w_min")
    for n in range(nmin, nmax + 1):
        N = start[n + 1]; D = (2 * n + 2) * (2 * n + 3) // 2
        Qe = QeAll[:, :N]
        HF = Qe.T @ (y[:, None] * Qe); HJ = Qe.T @ (x[:, None] * Qe)
        entries = []  # (matrix 'F'/'J', row, col, computed value)
        for k in range(1, start[n + 2] if n + 2 < len(start) else len(idx)):
            if k >= len(idx):
                break
            t, j = idx[k]
            Wk, h, beta = coef[k]; p = parent[k]
            if p >= N:
                continue
            if op[k] == 'F':
                for l, hv in zip(Wk, h):
                    if l < N:
                        entries.append(('F', l, p, hv))
                if k < N:
                    entries.append(('F', k, p, beta))
            else:
                if idx[p][0] > n - 1:
                    continue
                for l, hv in zip(Wk, h):
                    if l < N:
                        entries.append(('J', l, p, hv))
                if k < N:
                    entries.append(('J', k, p, beta))
        E = len(entries)
        e = np.array([v - (HF[r, c] if m == 'F' else HJ[r, c]) for (m, r, c, v) in entries])
        Jac = np.zeros((E, M))
        rows_F = np.array([r for (m, r, c, v) in entries]); cols_F = np.array([c for (m, r, c, v) in entries])
        isF = np.array([m == 'F' for (m, r, c, v) in entries])
        for i in range(M):
            qi = Qe[i, :]
            K = np.outer(qi, qi) / w[i]
            S = np.triu(K, 1) + np.diag(np.diag(K)) / 2
            dF = y[i] * K - S.T @ HF - HF @ S
            dJ = x[i] * K - S.T @ HJ - HJ @ S
            Jac[:, i] = np.where(isF, dF[rows_F, cols_F], dJ[rows_F, cols_F])
        eta, *_ = np.linalg.lstsq(Jac, e, rcond=None)
        r = Jac @ eta - e
        rho = np.linalg.norm(r) / np.linalg.norm(e)
        # bounded fit: positive weights within a factor 2 (|eta_i| <= w_i/2), linearisation valid
        from scipy.optimize import lsq_linear
        sc = np.linalg.norm(e)
        bl = lsq_linear(Jac / sc, e / sc, bounds=(-w / 2, w / 2), lsmr_tol='auto', max_iter=2000)
        rho_pos = np.linalg.norm(Jac @ bl.x - e) / np.linalg.norm(e)
        loss = np.abs(Q[:, :N].T @ Q[:, :N] - np.eye(N)).max()
        print(f"{n:2d} {N:4d} {D:5d}  {loss:.2e}  {np.abs(e).max():.2e}  {rho:.3f}    {np.abs(r).max():.2e}   "
              f"{np.abs(eta).max()/w.min():.2e}   rho_pos(|eta|<=w/2)={rho_pos:.3f}   [{E} entries]", flush=True)


if __name__ == '__main__':
    main()
