"""R06 (MEASURED): consistency defect of the computed coefficient data of the window recurrence.

Imports L1's library tracks/bivariate-lanczos/code/L1/l1_recurrence.py READ-ONLY (recurrence,
node sets, rotate). L1 convention: J = X injects columns (t,0), F = Y is full; within degree t,
column (t,j) <-> x^(t-j) y^j.
For one run to degree nmax+1 and each n <= nmax:
  Hf  = computed F-coefficients (columns of degree <= n, rows truncated to degree <= n)
  Hj  = implicit J-section (L1 PD-T?bivariate-lanczos-claude-104 part 2): computed columns (t,0);
        column (t,j), j >= 1: (T_F Hj e_p - sum_{l in W} h_l Hj e_l) / beta, p = (t-1, j-1)
  comm = max over columns of degree <= n-1 of |[Hf, Hj] e_c|          (K12; ~0 by construction)
  asym = (max|Hf - Hf^T| + max|Hj - Hj^T|) / max(|Hf|, |Hj|)       (consistency defect)
  loss = max|Q^T Q - I| over the first N_n columns
  fwd  = max|H - H_exact| / max|H_exact| with H_exact = Q_e^T (X, Y) Q_e, Q_e from Householder QR of
         the weighted Chebyshev-Vandermonde matrix in the same graded order (R diagonal > 0).
Usage: python3 r06_consistency.py set nmax [win] [orth]
  set in {random, tensor, rot03, rot10, annulus};  win in {block, exact}; orth in {cgs, orth}
"""
import os
import sys
import numpy as np
from numpy.polynomial import chebyshev as Ch

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'L1'))
import l1_recurrence as L1  # noqa: E402  (read-only use of L1's library)

U = 2.0 ** -53


def cheb_vander(x, y, idx):
    cols = []
    for (t, j) in idx:
        a, b = t - j, j
        ca = np.zeros(a + 1); ca[a] = 1
        cb = np.zeros(b + 1); cb[b] = 1
        cols.append(Ch.chebval(x, ca) * Ch.chebval(y, cb))
    return np.array(cols).T


def main():
    which = sys.argv[1]; nmax = int(sys.argv[2])
    win = sys.argv[3] if len(sys.argv) > 3 else 'block'
    orth = sys.argv[4] if len(sys.argv) > 4 else 'cgs'
    if which == 'random':
        P, w = L1.nodes_random(1681, 0)
    elif which == 'tensor':
        P, w = L1.nodes_tensor_cheb(41)
    elif which == 'rot03':
        P, w = L1.nodes_random(1681, 0); P = L1.rotate(P, 0.3)
    elif which == 'rot10':
        P, w = L1.nodes_random(1681, 0); P = L1.rotate(P, 1.0)
    elif which == 'annulus':
        P, w = L1.nodes_annulus_random(3000, 0)
    else:
        raise SystemExit(which)
    x, y = P[:, 0], P[:, 1]
    w = np.asarray(w, float); w = w / w.sum()
    Q, coef, (idx, pos, parent, op, start) = L1.recurrence(x, y, w, nmax + 1, win=win, orth=orth)
    Ntot = len(idx)
    Tf = np.zeros((Ntot, Ntot)); Hj = np.zeros((Ntot, Ntot))
    for k in range(1, Ntot):
        W, h, beta = coef[k]; p = parent[k]
        T = Tf if op[k] == 'F' else Hj
        T[W, p] += h; T[k, p] += beta
    # implicit J columns (t, j), j >= 1, for degree t <= nmax (needs Tf columns of degree <= t)
    for k in range(1, Ntot):
        t, j = idx[k]
        if j == 0 or t > nmax:
            continue
        W, h, beta = coef[k]; p = parent[k]
        v = Tf @ Hj[:, p]
        for ii, l in enumerate(W):
            v -= h[ii] * Hj[:, l]
        Hj[:, k] = v / beta
    Ve = cheb_vander(x, y, idx) * np.sqrt(w)[:, None]
    NQ = start[nmax + 1]
    QeAll, RAll = np.linalg.qr(Ve[:, :NQ]); QeAll = QeAll * np.sign(np.diag(RAll))  # leading columns = QR of leading block
    print(f"set={which} M={len(x)} win={win} orth={orth} nmax={nmax}")
    print(" n    N   loss       asymF      asymJ      asym/u     comm/u     fwdF       fwdJ")
    for n in range(2, nmax + 1):
        N = start[n + 1]
        Hf_n, Hj_n = Tf[:N, :N], Hj[:N, :N]
        scale = max(np.abs(Hf_n).max(), np.abs(Hj_n).max())
        aF = np.abs(Hf_n - Hf_n.T).max() / scale; aJ = np.abs(Hj_n - Hj_n.T).max() / scale
        cols = list(range(start[n]))  # degree <= n-1
        C = (Hf_n @ Hj_n - Hj_n @ Hf_n)[:, cols]
        comm = np.abs(C).max() / scale ** 2
        Qn = Q[:, :N]; loss = np.abs(Qn.T @ Qn - np.eye(N)).max()
        Qe = QeAll[:, :N]
        HeF = Qe.T @ (y[:, None] * Qe); HeJ = Qe.T @ (x[:, None] * Qe)
        fF = np.abs(Hf_n - HeF).max() / np.abs(HeF).max(); fJ = np.abs(Hj_n - HeJ).max() / np.abs(HeJ).max()
        print(f"{n:2d} {N:4d}  {loss:.2e}  {aF:.2e}  {aJ:.2e}  {(aF+aJ)/U:.2e}  {comm/U:.2e}  {fF:.2e}  {fJ:.2e}", flush=True)


if __name__ == '__main__':
    main()
