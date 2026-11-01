"""L2 reconstruction 01: implicit J-section error e_H and formed-J error e_tau of PD-N?bivariate-lanczos-claude-201 (a)
for BJ + CGS2-all (own run), evaluated in long double; F-defect and theta_LB; product control (tensor 41^2).
Own code.  MEASURED.  Usage: python3 -I rl2_sections.py > logs_L2/sections.log"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rl2_lib as R
import rl2_thmA as TA

LD = R.LD


def implicit_HJ(recs, N, Nc, dtype=LD):
    deg = R.degrees(N)
    TG = np.zeros((N, Nc), dtype=dtype)       # F-section incl. reorth coefficients, column = parent
    Jcol = {}
    for k in range(1, N):
        op, p, S, c, beta = recs[k]
        col = np.zeros(N, dtype=dtype); col[S] = np.asarray(c, dtype=dtype); col[k] = dtype(beta)
        if p < Nc:
            if op == 'Y':
                TG[:, p] = col
            else:
                Jcol[p] = col
    H = np.zeros((N, Nc), dtype=dtype)
    formed = []
    for c in range(Nc):
        if c in Jcol:
            H[:, c] = Jcol[c]; formed.append(c)
        else:
            op, p, S, cc, beta = recs[c]
            Ns = R.Nof(deg[c])
            v = TG[:, :Ns] @ H[:Ns, p] - H[:, S] @ np.asarray(cc, dtype=dtype)
            H[:, c] = v / dtype(beta)
    return H, formed


def main():
    print(f"# rl2_sections.py numpy={np.__version__}", flush=True)
    sq, dk, tr = R.rng11_sets()
    for name, P, nmax in (('rotpi4', R.rotate(sq, np.pi / 4), 24), ('triangle', tr, 20)):
        t0 = time.time()
        x, y = P[:, 0].copy(), P[:, 1].copy()
        w = np.ones(len(x))
        Q, recs = R.recur(x, y, w, nmax, rule='bj', orth='cgs2all', record=True)
        nrm = max(np.abs(x).max(), np.abs(y).max())
        for n in (12, 16, 20, 24):
            if n > nmax:
                continue
            N, Nc = R.Nof(n), R.Nof(n - 1)
            H, formed = implicit_HJ(recs, N, Nc)
            Ql = Q[:, :N].astype(LD)
            G = Ql.T @ Ql
            Lc = TA.chol_ld(G)
            A = Ql.T @ (np.asarray(x, dtype=LD)[:, None] * Ql[:, :Nc])
            Z = TA.fsub(Lc, A)
            S = TA.fsub(Lc[:Nc, :Nc], Z.T).T
            D = np.abs((S - H).astype(np.float64)) / nrm
            eH = float(D.max()); etau = float(D[:, formed].max())
            C = np.asarray(x, dtype=LD)[:, None] * Ql[:, :Nc] - Ql @ H
            K = float(np.abs((Ql.T @ C).astype(np.float64)).max())
            rA = TA.theorem_A(Q, recs, x, y, n)
            print(f"  {name:8s} BJ cgs2all n={n:2d}: loss={rA['loss']:.1e} e_F={rA['lhs'] / nrm:.1e} e_tau={etau:.1e} "
                  f"e_H={eH:.1e} max|K|={K:.1e} max||c_l||={float(np.linalg.norm(C.astype(np.float64), axis=0).max()):.1e}",
                  flush=True)
        Wd = np.linalg.qr(Q)[0]
        dX, dY = R.defects(Wd, x, y, nmax)
        print(f"  {name:8s} F-defect max {dY.max():.1e}, J-defect max {dX.max():.1e}, thetaLB {dX.max() / (2 * np.abs(x).max()):.1e}"
              f" ({time.time() - t0:.0f}s)", flush=True)
    # product control: tensor Chebyshev 41^2, n = 39
    g = np.cos(np.pi * (np.arange(41) + 0.5) / 41)
    P = np.array([(a, b) for a in g for b in g])
    x, y = P[:, 0].copy(), P[:, 1].copy()
    Q = R.recur(x, y, np.ones(len(x)), 39, rule='bj', orth='cgs2all')
    Wd = np.linalg.qr(Q)[0]
    dX, dY = R.defects(Wd, x, y, 39)
    print(f"  tensor41 BJ cgs2all n=39: loss={np.abs(Q.T @ Q - np.eye(Q.shape[1])).max():.1e} "
          f"thetaLB={max(dX.max() / (2 * np.abs(x).max()), dY.max() / (2 * np.abs(y).max())):.1e}", flush=True)
    # tensor: exact S_n reference from the product Chebyshev basis (orthogonal for this node set)
    V = R.vander_product(x, y, np.ones(len(x)), 39, 'cheb')
    print(f"  tensor41 reference kappa(Cheb product, n=39) = {R.kappa(V):.2e}; drift = "
          f"{R.sin_angles_nested(Wd, np.linalg.qr(V)[0], [39])[39]:.1e}", flush=True)


if __name__ == '__main__':
    main()
