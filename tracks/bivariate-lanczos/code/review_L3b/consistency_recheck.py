"""Reviewer (L3 reconstruction 02): independent re-implementation of the R06 measurements
(PD-T?...-314/315) with an adversarial split of the computed data.

Own code (no developer or L1 import): BJ recurrence (block window = all columns of degrees t-2..t
computed before k; one classical Gram-Schmidt pass), node set as described in R06 (numpy
default_rng(0) uniform 1681 points in [-1,1]^2, optionally rotated by 0.3 rad), uniform weights.
Ordering: within degree t, (t,0..t) <-> x^(t-j) y^j; (t,0) = X (t-1,0); (t,j) = Y (t-1,j-1).

Per n it reports
  loss, asymmetry of H_F (all entries / excluding block-window EXTRA positions), asym_J, comm (K12),
  forward errors against TWO references (A: Householder QR of the weighted Chebyshev-Vandermonde
  matrix; B: the same graded recurrence with full double reorthogonalisation), and their difference
  (reference floor);
  the first-order weight-only fit of the computed partial data e (as in R06/K15):
     rho_all     = min ||Jac eta - e|| / ||e||           over all partial entries (= R06's rho),
     frac_extra  = ||e_extra|| / ||e||                    (EXTRA = F-coefficients of the block window
                   outside the exact support: rows (t-2, r), r < j-2, of the F-product creating (t,j));
                   these are structural zeros of EVERY consistent section pair, so rho_all >= frac_extra;
     rho_noextra = the same fit on the entries of the exact pattern only;
     max|eta|/w_min of each minimiser.
Usage: python3 -I consistency_recheck.py set nmin nmax      (set in {rot03, random})
"""
import sys
import numpy as np
from numpy.polynomial import chebyshev as Ch

U = 2.0 ** -53


def nodes(which):
    rng = np.random.default_rng(0)
    P = rng.uniform(-1, 1, (1681, 2))
    if which == 'rot03':
        c, s = np.cos(0.3), np.sin(0.3)
        P = np.column_stack([c * P[:, 0] - s * P[:, 1], s * P[:, 0] + c * P[:, 1]])
    return P[:, 0].copy(), P[:, 1].copy()


def tables(nmax):
    idx = [(t, j) for t in range(nmax + 1) for j in range(t + 1)]
    pos = {k: i for i, k in enumerate(idx)}
    start = [t * (t + 1) // 2 for t in range(nmax + 2)]
    return idx, pos, start


def bj(x, y, w, nmax, full_reorth=False, dtype=float):
    idx, pos, start = tables(nmax)
    M, N = len(x), len(idx)
    x = np.asarray(x, dtype); y = np.asarray(y, dtype); w = np.asarray(w, dtype)
    Q = np.zeros((M, N), dtype); sw = np.sqrt(w); Q[:, 0] = sw / np.sqrt(np.sum(sw * sw))
    rec = [None] * N
    for k in range(1, N):
        t, j = idx[k]
        if j == 0:
            p, op = pos[(t - 1, 0)], 'J'; v = x * Q[:, p]
        else:
            p, op = pos[(t - 1, j - 1)], 'F'; v = y * Q[:, p]
        W = list(range(start[max(t - 2, 0)], k)) if not full_reorth else list(range(k))
        h = Q[:, W].T @ v; v = v - Q[:, W] @ h
        if full_reorth:
            h2 = Q[:, W].T @ v; v = v - Q[:, W] @ h2; h = h + h2
        beta = np.sqrt(np.sum(v * v)); Q[:, k] = v / beta
        # extra = window positions outside the exact support (F-products, block t-2 below index j-2)
        extra = [l for l in W if (op == 'F' and idx[l][0] == t - 2 and idx[l][1] < j - 2)] if not full_reorth else []
        rec[k] = (op, p, W, h, beta, set(extra))
    return Q, rec, idx, pos, start


def assemble(rec, idx, nmax):
    N = len(idx)
    Tf = np.zeros((N, N)); Hj = np.zeros((N, N))
    for k in range(1, N):
        op, p, W, h, beta, _ = rec[k]
        T = Tf if op == 'F' else Hj
        T[W, p] += h; T[k, p] += beta
    for k in range(1, N):     # implicit J-completion (L1 PD-T?...-104 part 2), own code
        t, j = idx[k]
        if j == 0 or t > nmax:
            continue
        op, p, W, h, beta, _ = rec[k]
        v = Tf @ Hj[:, p] - Hj[:, W] @ h
        Hj[:, k] = v / beta
    return Tf, Hj


def cheb_vander(x, y, idx):
    cols = []
    for (t, j) in idx:
        a, b = t - j, j
        ca = np.zeros(a + 1); ca[a] = 1; cb = np.zeros(b + 1); cb[b] = 1
        cols.append(Ch.chebval(x, ca) * Ch.chebval(y, cb))
    return np.array(cols).T


def main():
    which, nmin, nmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    x, y = nodes(which); M = len(x); w = np.ones(M) / M
    Q, rec, idx, pos, start = bj(x, y, w, nmax + 1)
    Tf, Hj = assemble(rec, idx, nmax)
    QB, *_ = bj(x, y, w, nmax + 1, full_reorth=True)
    QC, *_ = bj(x, y, w, nmax + 1, full_reorth=True, dtype=np.longdouble)
    xl, yl = np.asarray(x, np.longdouble), np.asarray(y, np.longdouble)
    NQ = start[nmax + 1]
    V = cheb_vander(x, y, idx[:NQ]) * np.sqrt(w)[:, None]
    QA, R = np.linalg.qr(V); QA = QA * np.sign(np.diag(R))
    print(f"consistency_recheck set={which} M={M} BJ block window CGS (own implementation); nmin={nmin} nmax={nmax}")
    print(" n    N  loss      asymF     asymF_noX asymJ     comm/u   fwdF_A    fwdJ_A    refAB     |  rho_all  frac_extra rho_noextra  max|eta|/wmin(all,noX)  E")
    for n in range(nmin, nmax + 1):
        N = start[n + 1]
        Hf_n, Hj_n = Tf[:N, :N], Hj[:N, :N]
        sc = max(np.abs(Hf_n).max(), np.abs(Hj_n).max())
        mask = np.ones((N, N), bool)
        for k in range(1, len(idx)):
            op, p, W, h, beta, ex = rec[k]
            if p < N:
                for l in ex:
                    if l < N:
                        mask[l, p] = False; mask[p, l] = False
        AF = np.abs(Hf_n - Hf_n.T)
        aF, aFnx = AF.max() / sc, AF[mask].max() / sc
        aJ = np.abs(Hj_n - Hj_n.T).max() / sc
        C = (Hf_n @ Hj_n - Hj_n @ Hf_n)[:, :start[n]]
        comm = np.abs(C).max() / sc ** 2
        loss = np.abs(Q[:, :N].T @ Q[:, :N] - np.eye(N)).max()
        QAn, QBn = QA[:, :N], QB[:, :N]
        HFA, HJA = QAn.T @ (y[:, None] * QAn), QAn.T @ (x[:, None] * QAn)
        HFB, HJB = QBn.T @ (y[:, None] * QBn), QBn.T @ (x[:, None] * QBn)
        fF = np.abs(Hf_n - HFA).max() / np.abs(HFA).max(); fJ = np.abs(Hj_n - HJA).max() / np.abs(HJA).max()
        refAB = max(np.abs(HFA - HFB).max(), np.abs(HJA - HJB).max())
        QCn = QC[:, :N]
        HFC = np.asarray(QCn.T @ (yl[:, None] * QCn), float); HJC = np.asarray(QCn.T @ (xl[:, None] * QCn), float)
        refAC = max(np.abs(HFA - HFC).max(), np.abs(HJA - HJC).max())
        fFC = np.abs(Hf_n - HFC).max() / np.abs(HFC).max(); fJC = np.abs(Hj_n - HJC).max() / np.abs(HJC).max()
        # partial computed entries (as R06): F-coefficients of columns of degree <= n with rows <= n
        # (window incl. extras, and beta), J computed columns (t,0), t <= n-1, rows <= n
        ent = []
        for k in range(1, len(idx)):
            op, p, W, h, beta, ex = rec[k]
            if p >= N:
                continue
            if op == 'J' and idx[p][0] > n - 1:
                continue
            for l, hv in zip(W, h):
                if l < N:
                    ent.append((op, l, p, hv, l in ex))
            if k < N:
                ent.append((op, k, p, beta, False))
        isF = np.array([e[0] == 'F' for e in ent]); rr = np.array([e[1] for e in ent]); cc = np.array([e[2] for e in ent])
        isX = np.array([e[4] for e in ent])
        val = np.array([e[3] for e in ent])
        ref = np.where(isF, HFA[rr, cc], HJA[rr, cc])
        e = val - ref
        Jac = np.zeros((len(ent), M))
        for i in range(M):
            qi = QAn[i, :]
            K = np.outer(qi, qi) / w[i]
            S = np.triu(K, 1) + np.diag(np.diag(K)) / 2
            dF = y[i] * K - S.T @ HFA - HFA @ S
            dJ = x[i] * K - S.T @ HJA - HJA @ S
            Jac[:, i] = np.where(isF, dF[rr, cc], dJ[rr, cc])
        eta, *_ = np.linalg.lstsq(Jac, e, rcond=None)
        rho_all = np.linalg.norm(Jac @ eta - e) / np.linalg.norm(e)
        fx = np.linalg.norm(e[isX]) / np.linalg.norm(e)
        ne = ~isX
        eta2, *_ = np.linalg.lstsq(Jac[ne], e[ne], rcond=None)
        rho_nx = np.linalg.norm(Jac[ne] @ eta2 - e[ne]) / np.linalg.norm(e[ne])
        # same fits against the long-double reference C (Jacobian from C's basis)
        refC = np.where(isF, HFC[rr, cc], HJC[rr, cc]); eC = val - refC
        QCd = np.asarray(QCn, float)
        JacC = np.zeros((len(ent), M))
        for i in range(M):
            qi = QCd[i, :]
            K = np.outer(qi, qi) / w[i]
            S = np.triu(K, 1) + np.diag(np.diag(K)) / 2
            dF = y[i] * K - S.T @ HFC - HFC @ S
            dJ = x[i] * K - S.T @ HJC - HJC @ S
            JacC[:, i] = np.where(isF, dF[rr, cc], dJ[rr, cc])
        etaC, *_ = np.linalg.lstsq(JacC, eC, rcond=None)
        rhoC = np.linalg.norm(JacC @ etaC - eC) / np.linalg.norm(eC)
        etaC2, *_ = np.linalg.lstsq(JacC[ne], eC[ne], rcond=None)
        rhoC_nx = np.linalg.norm(JacC[ne] @ etaC2 - eC[ne]) / np.linalg.norm(eC[ne])
        print(f"{n:2d} {N:4d}  {loss:.2e}  {aF:.2e}  {aFnx:.2e}  {aJ:.2e}  {comm/U:6.1f}  {fF:.2e}  {fJ:.2e}  {refAB:.1e}   |  {rho_all:.3f}    {fx:.3f}     {rho_nx:.3f}      "
              f"{np.abs(eta).max()/w.min():.1e}, {np.abs(eta2).max()/w.min():.1e}   {len(ent)}", flush=True)
        print(f"   long-double reference C: |A-C| = {refAC:.1e}; fwdF_C = {fFC:.2e}, fwdJ_C = {fJC:.2e}; |e_C|_2/|e_A|_2 = {np.linalg.norm(eC)/np.linalg.norm(e):.3f}; "
              f"rho_all(C) = {rhoC:.3f}, frac_extra(C) = {np.linalg.norm(eC[isX])/np.linalg.norm(eC):.3f}, rho_noextra(C) = {rhoC_nx:.3f}, max|eta|/wmin = {np.abs(etaC).max()/w.min():.1e}", flush=True)


if __name__ == '__main__':
    main()
