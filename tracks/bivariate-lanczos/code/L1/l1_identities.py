"""R02 checks: (1) growing-block Paige identity for the full operator F (PD-T?...-103), evaluated on F-Ritz pairs
and on the joint min-residual Ritz vector; (2) commutator-residual recursion for the injecting operator J
(PD-T?...-104): Hhat_J built from computed coefficients, C_res = J Qhat - Qhat Hhat_J, recursion residual;
(3) joint (complex-symmetric, bilinear) identity for N = J + iF with the commutator residual as error term.
All identities are exact algebra; the script checks them at rounding level and reports the sizes of the terms.
MEASURED only.  Usage: python3 -I l1_identities.py > logs/r02_identities.log
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L

Nof = lambda n: (n + 1) * (n + 2) // 2


def coef_matrices(coef, tab, nq):
    """T_F (N_nq x N_{nq-1}) of computed F-coefficients by parent column; tau (J-columns (t,0))."""
    idx, pos, parent, op, start = tab
    Nb = Nof(nq)
    TF = np.zeros((Nb, Nof(nq - 1)))
    TJ = {}
    for k in range(1, Nb):
        W, h, beta = coef[k]
        p = parent[k]
        col = np.zeros(Nb); col[W] = h; col[k] = beta
        if op[k] == 'F':
            TF[:, p] = col
        else:
            TJ[p] = col
    return TF, TJ


def hhat_J(TF, TJ, coef, tab, nq):
    """Implicit J-section from computed coefficients (PD-T?...-101 part 5 applied to computed data):
    columns up to degree nq-1; column (t,0) = computed tau_t; (t,j) = (TF Hj[(t-1,j-1)] - sum h_l Hj[l]) / beta."""
    idx, pos, parent, op, start = tab
    Nb = Nof(nq); Ncols = Nof(nq - 1)
    H = np.zeros((Nb, Ncols), dtype=TF.dtype)
    for p in range(Ncols):
        t, j = idx[p]
        if j == 0:
            H[:, p] = TJ[p]
        else:
            W, h, beta = coef[p]
            pp = parent[p]
            v = TF[:, :Nof(t)] @ H[:Nof(t), pp]          # H[:, pp] supported on degree <= t
            for hl, l in zip(h, W):
                v = v - hl * H[:, l]
            H[:, p] = v / beta
    return H


def j_support_mask(tab, nq):
    """Exact-arithmetic support of the J-columns (PD-T?...-101 part 3): rows (t-1, i>=j), block t, (t+1, r<=j)."""
    idx, pos, parent, op, start = tab
    Nb = Nof(nq); Nc = Nof(nq - 1)
    Mk = np.zeros((Nb, Nc), dtype=bool)
    for p in range(Nc):
        t, j = idx[p]
        for l in range(Nb):
            tl, i = idx[l]
            if (tl == t - 1 and i >= j) or tl == t or (tl == t + 1 and i <= j):
                Mk[l, p] = True
    return Mk


def identity_report(Qh, A, Tfull, n, svecs, name):
    """A: diagonal entries (real or complex) of a (complex) symmetric diagonal operator;
    Tfull: N_n x N_{n-1} coefficient matrix with A Q_{n-1} = Q_n Tfull + E.
    For each s in svecs (coefficient vectors in the coordinates of Q_{n-1}), report
    lhs = s^T c B s, the bound pieces, |B s|, |Q_new^T y|, and the controlled fraction."""
    m = Nof(n - 1); Nn = Nof(n)
    Qo, Qn = Qh[:, :m], Qh[:, m:Nn]
    T, B = Tfull[:m, :m], Tfull[m:Nn, :m]
    E = A[:, None] * Qo - Qh[:, :Nn] @ Tfull
    C = Qo.T @ Qo; c = Qo.T @ Qn
    G = C - np.eye(m)
    S = (T + T.T) / 2; K = (T - T.T) / 2
    # exact identity (*): C T + c B + Qo^T E - (T^T C + B^T c^T + E^T Qo) = 0
    lhs_star = C @ T + c @ B + Qo.T @ E - (T.T @ C + B.T @ c.T + E.T @ Qo)
    star = float(np.abs(lhs_star).max())
    Dg = np.diag(np.diag(G)); R = np.triu(G, 1)
    X = R @ S - S @ R
    Phi = E.T @ Qo - Qo.T @ E - 2 * K - G @ K - K @ G
    low = lambda Mx: np.tril(Mx, -1); up = lambda Mx: np.triu(Mx, 1); dg = lambda Mx: np.diag(np.diag(Mx))
    cB = c @ B
    Omega = low(X) + low(X).T + dg(X) - up(Dg @ S - S @ Dg) + up(B.T @ c.T) + np.tril(cB) + up(Phi)
    Omega_loc = Omega - up(Phi)
    nOm = np.linalg.norm(Omega, 2); nOml = np.linalg.norm(Omega_loc, 2); nPhi = np.linalg.norm(up(Phi), 2)
    nE = np.linalg.norm(E, 2); nK = np.linalg.norm(K, 2); nR = np.linalg.norm(R, 2)
    print(f"  [{name}] n={n}: identity(*) resid {star:.1e}; |Omega|={nOm:.1e} (local {nOml:.1e}, up(Phi) {nPhi:.1e}); "
          f"|E|={nE:.1e} |K|={nK:.1e} |R|={nR:.1e}")
    out = []
    for lab, s, theta in svecs:
        s = s / np.linalg.norm(s)
        rho = S @ s - theta * s
        lhs = s @ (cB @ s)
        rhs = s @ (Omega @ s) - s @ ((R - R.T) @ rho)
        Bs = B @ s
        y_new = Qn.T @ (Qo @ s)
        nb = np.linalg.norm(Bs); ny = np.linalg.norm(y_new)
        ctrl = abs(y_new @ (Bs / nb)) if nb > 0 else 0.0   # bilinear, as in the identity
        out.append((lab, abs(lhs), abs(lhs - rhs), np.linalg.norm(rho), nb, ny, ctrl))
        print(f"     {lab:22s} |s^T cB s|={abs(lhs):.1e} (identity err {abs(lhs - rhs):.1e}) |rho|={np.linalg.norm(rho):.1e} "
              f"|Bs|={nb:.1e} |Qnew^T y|={ny:.1e} |<Qnew^T y, Bs/|Bs|>|={ctrl:.1e} frac={ctrl / max(ny, 1e-300):.2f} "
              f"bound (|Om|+2|R||rho|)/|Bs|={(nOm + 2 * nR * np.linalg.norm(rho)) / max(nb, 1e-300):.1e}")
    return out


def run(name, P, w, nmax, ns, win='exact', orth='cgs'):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    nq = nmax + 1
    Q, coef, tab = L.recurrence(x, y, w, nq, win=win, orth=orth)
    TF, TJ = coef_matrices(coef, tab, nq)
    HJ = hhat_J(TF, TJ, coef, tab, nq)
    Jmask = j_support_mask(tab, nq)
    print(f"== {name} M={len(x)} win={win} orth={orth}; max |Hhat_J| outside exact J-support: "
          f"{np.abs(np.where(Jmask, 0.0, HJ)).max():.1e}")
    # commutator residual and recursion check
    m = Nof(nq - 1)
    Cres = x[:, None] * Q[:, :m] - Q @ HJ
    U, _ = np.linalg.qr(Q)
    for n in ns:
        Nm = Nof(n - 1); Nn = Nof(n)
        Un = U[:, :Nn]
        D = x[:, None] * U[:, :Nm] - Un @ (Un.T @ (x[:, None] * U[:, :Nm]))
        G = Q[:, :Nn].T @ Q[:, :Nn]
        print(f"  n={n}: loss={np.abs(G - np.eye(Nn)).max():.1e}  max|c_k| (commutator residual, deg<=n-1)="
              f"{np.linalg.norm(Cres[:, :Nm], axis=0).max():.1e}  defect_x={np.linalg.norm(D, axis=0).max():.1e}")
    # recursion residual (exact identity) on all columns of degree <= nmax-1
    idx, pos, parent, op, start = tab
    # The recursion is an exact identity between the stored double-precision quantities; evaluate both sides
    # in long double so that the evaluation error (~1e-19) is far below the u-sized terms being compared.
    LD = np.longdouble
    TJl = {k: v.astype(LD) for k, v in TJ.items()}
    coefl = [None] + [(W, np.asarray(h, dtype=LD), LD(b)) for (W, h, b) in coef[1:]]
    Ql, TFl, xl, yl = Q.astype(LD), TF.astype(LD), x.astype(LD), y.astype(LD)
    HJl = hhat_J(TFl, TJl, coefl, tab, nq)       # implicit section rebuilt in long double from the same data
    Cl = xl[:, None] * Ql[:, :m] - Ql @ HJl
    EF = yl[:, None] * Ql[:, :Nof(nq - 1)] - Ql @ TFl
    worst = 0.0
    for k in range(1, Nof(nmax - 1)):
        t, j = idx[k]
        if j == 0:
            continue
        W, h, beta = coef[k]; p = parent[k]
        hl = np.asarray(h, dtype=LD); bl = LD(beta)
        f = yl * Ql[:, p] - Ql[:, W] @ hl - bl * Ql[:, k]
        lhs = bl * Cl[:, k]
        rhs = yl * Cl[:, p] - Cl[:, W] @ hl + EF[:, :Nof(t)] @ HJl[:Nof(t), p] - xl * f
        worst = max(worst, float(np.linalg.norm(lhs - rhs) / max(np.linalg.norm(lhs), 1e-300)))
    print(f"  commutator-residual recursion (long-double evaluation): max relative residual {worst:.1e}")
    # Paige identities at selected degrees
    zN = x + 1j * y
    for n in ns:
        Nm = Nof(n - 1)
        Um = U[:, :Nm]
        # F-Ritz pairs of the symmetrized computed section, smallest |B s|
        T = TF[:Nm, :Nm]; S = (T + T.T) / 2
        th, V = np.linalg.eigh(S)
        Bv = TF[Nm:Nof(n), :Nm] @ V
        order = np.argsort(np.linalg.norm(Bv, axis=0))
        svecs = [(f"F-Ritz #{r}", V[:, order[r]], th[order[r]]) for r in range(2)]
        # joint min-residual Ritz vector, expressed in Qhat coordinates (Qhat s = U s_U)
        rz, thz, Sz = L.ritz_min(Um, zN, False, want_vec=True)
        sU = Sz[:, 0]
        sQ = np.linalg.lstsq(Q[:, :Nm], Um @ sU, rcond=None)[0]
        sQ = sQ * np.exp(-0.5j * np.angle(np.sum(sQ ** 2)))   # remove the free phase, then take the real part
        sr = sQ.real
        svecs_real = svecs + [("joint-min (phase-fixed Re)", sr, (sr @ (S @ sr)) / (sr @ sr))]
        identity_report(Q, y, TF[:Nof(n), :Nm], n, svecs_real, 'F=Y')
        # joint identity: N = J + iF with T_N = P(HJ) + i TF, error = Cres + Q(HJ - P(HJ)) + i E_F (bilinear)
        HJm = np.where(Jmask, HJ, 0.0)
        TN = HJm[:Nof(n), :Nm] + 1j * TF[:Nof(n), :Nm]
        TNs = TN[:Nm, :Nm]; SN = (TNs + TNs.T) / 2
        thN, VN = np.linalg.eig(SN)
        BN = TN[Nof(n - 1):Nof(n), :]
        ordN = np.argsort(np.linalg.norm(BN @ VN, axis=0) / np.linalg.norm(VN, axis=0))
        sv = [(f"Z-Ritz #{r}", VN[:, ordN[r]], thN[ordN[r]]) for r in range(2)]
        identity_report(Q.astype(complex), zN, TN, n, sv, 'N=J+iF')


if __name__ == '__main__':
    print(f"# l1_identities.py numpy={np.__version__}")
    P, w = L.nodes_random(1681, 0)
    run('random1681_s0 (product-like support)', P, w, 40, [24, 32, 40])
    P, w = L.nodes_random(1681, 0)
    run('random1681_s0 rotated 0.3 (non-product support)', L.rotate(P, 0.3), w, 24, [12, 16, 20])
    P, w = L.nodes_tensor_cheb(41)
    run('tensorcheb41', P, w, 39, [24, 32, 39])


def omega_sources(name, P, w, nmax, win='exact', orth='cgs', check_ld=True):
    """Exact 2D omega-recurrence (PD-T?...-106): for every new column k (parent p, operator A) and every old l,
    beta_k w_lk = sum_r (T_A)_{rl} w_rp + (E_A e_l)^T q_p - sum_{l' in W_k} h_l' w_ll' - q_l^T f_k,
    T_A = T_F (F-products) or Hhat_J (J-products), E_A = E_F or C_res.  Reports, per degree of k, the largest
    source term |(E_A e_l)^T q_p| over l outside the window, separately for F- and J-products, the largest
    |w_lk| (loss), and the identity residual (long-double evaluation)."""
    x, y = P[:, 0].copy(), P[:, 1].copy()
    nq = nmax + 1
    Q, coef, tab = L.recurrence(x, y, w, nq, win=win, orth=orth)
    idx, pos, parent, op, start = tab
    TF, TJ = coef_matrices(coef, tab, nq)
    LD = np.longdouble
    TJl = {k: v.astype(LD) for k, v in TJ.items()}
    coefl = [None] + [(W, np.asarray(h, dtype=LD), LD(b)) for (W, h, b) in coef[1:]]
    Ql, TFl, xl, yl = Q.astype(LD), TF.astype(LD), x.astype(LD), y.astype(LD)
    HJl = hhat_J(TFl, TJl, coefl, tab, nq)
    m = Nof(nq - 1)
    EF = yl[:, None] * Ql[:, :m] - Ql @ TFl
    CR = xl[:, None] * Ql[:, :m] - Ql @ HJl
    Om = Ql.T @ Ql
    print(f"== omega-recurrence sources: {name} M={len(x)} win={win} orth={orth}")
    rows = {}
    for k in range(1, Nof(nmax)):
        t, j = idx[k]
        if t < 3:
            continue
        W, h, beta = coefl[k]; p = parent[k]
        lo = min(W) if W else k
        old = np.arange(0, lo)
        if op[k] == 'F':
            TA, EA, a = TFl, EF, yl
        else:
            TA, EA, a = HJl, CR, xl
        f = a * Ql[:, p] - Ql[:, W] @ h - beta * Ql[:, k]
        src = EA[:, old].T @ Ql[:, p]
        if check_ld:
            lhs = beta * Om[old, k]
            rhs = TA[:, old].T @ Om[:TA.shape[0], p] + src - Om[np.ix_(old, W)] @ h - Ql[:, old].T @ f
            res = float(np.abs(lhs - rhs).max())
        else:
            res = float('nan')
        r = rows.setdefault(t, dict(srcF=0.0, srcJ=0.0, lossF=0.0, lossJ=0.0, ampF=0.0, ampJ=0.0, res=0.0))
        key = 'F' if op[k] == 'F' else 'J'
        amp = TA[:, old].T @ Om[:TA.shape[0], p] - Om[np.ix_(old, W)] @ h      # recursion (propagation) term
        r['src' + key] = max(r['src' + key], float(np.abs(src).max()))
        r['loss' + key] = max(r['loss' + key], float(np.abs(Om[old, k]).max()))
        r['amp' + key] = max(r['amp' + key], float(np.abs(amp).max() / beta))
        r['res'] = max(r['res'], res)
    for t in sorted(rows):
        r = rows[t]
        print(f"   deg {t:2d}: loss(l outside window) F-cols {r['lossF']:.1e} J-col {r['lossJ']:.1e} | propagation term/beta "
              f"F {r['ampF']:.1e} J {r['ampJ']:.1e} | source F {r['srcF']:.1e} J(commutator) {r['srcJ']:.1e} | "
              f"identity residual {r['res']:.1e}", flush=True)
