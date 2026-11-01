"""Decisive test gen1-3, test T2 (K2: approximation payoff) and T2b (BHH tensor space, informative).

Scope: training grid 64x64 Chebyshev (M = 4096), validation grid 97x97 Chebyshev (9409 points, no node in
common), unit weights; n = 24 (N = 325); classes P, Ppt, Pbhh, Pbx, Ldiag, Pdiag, Mpt, Pedge at
eps_min in {3e-4, 3e-3, 3e-2}, far-first ordering; targets fA = sqrt(2-x-y) (BHH f2 translated),
fB = r^{1/2}(1 + sin(3 theta)/2) (adversary's f7), fC = sqrt(1-x)(1 + sin(2y)/2) (edge, informative).
Fit = least squares in the computed basis: LF (full-reorthogonalisation rational Lanczos, double; the
recurrence is re-run at the validation points to evaluate the basis there), with L3c and R1 (Householder
QR of the evaluated basis, coefficients mapped to the validation points through R^{-1}) for comparison.
T2b: BHH's own tensor space (eq. 2.2 of arXiv:2312.13202 in real form) at matched dimension 324:
poles on both edges (N_q = 12 pairs per edge, N_p = 5) and, for fC, on the x-edge only (N_q = 24, N_p = 5),
solved by truncated SVD (1e-12) of the unit-column-scaled partial-fraction basis.
Also convergence in n (8, 12, 16, 20, 24) for P, Ppt, Pbhh, Ldiag, Pdiag.
Outputs: T2.out. Everything MEASURED within this scope only.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orf2d import *

OUT = []


def say(s=""):
    print(s, flush=True)
    OUT.append(s)


def rel(a, b, w):
    return float(np.linalg.norm(np.sqrt(w) * (a - b)) / np.linalg.norm(np.sqrt(w) * b))


def fit_lanczos(L, x, y, w, xv, yv, tg, tgv):
    Qv = L.evaluate(xv, yv)
    out = {}
    for k in tg:
        err, cq, fit = ls_fit(L.Q, w, tg[k])
        fv = np.real(Qv @ cq)
        out[k] = (err, rel(fv, tgv[k], np.ones(len(xv))))
    return out


def fit_qr(R, A, Av, w, tg, tgv):
    out = {}
    for k in tg:
        err, cq, fit = ls_fit(R.Q, w, tg[k])
        fv = np.real(R.evaluate_fit(Av, cq))
        out[k] = (err, rel(fv, tgv[k], np.ones(Av.shape[0])))
    return out


def bhh_basis(x, y, eps, Np, Nq, edges=('x', 'y')):
    Vx, Vy = cheb_vander(x, Np), cheb_vander(y, Np)
    cols = []
    for e in taper(Nq, eps):
        if 'x' in edges:
            qx = (1 - x) ** 2 + e ** 2
            for k in range(Np + 1):
                cols += [Vy[:, k] * (1 - x) / qx, Vy[:, k] / qx]
        if 'y' in edges:
            qy = (1 - y) ** 2 + e ** 2
            for k in range(Np + 1):
                cols += [Vx[:, k] * (1 - y) / qy, Vx[:, k] / qy]
    for a in range(Np + 1):
        for b in range(Np + 1):
            cols.append(Vx[:, a] * Vy[:, b])
    return np.column_stack(cols)


if __name__ == '__main__':
    T0 = time.perf_counter()
    x, y = cheb_grid(64); w = np.ones(len(x))
    xv, yv = cheb_grid(97)
    tg, tgv = targets(x, y), targets(xv, yv)
    n = 24
    say("Decisive test gen1-3: T2 (K2) and T2b. Entries: training-grid error / validation-grid error (relative RMS).")
    say(f"training M = {len(x)}, validation points = {len(xv)}, n = {n}, N = {(n+1)*(n+2)//2}")
    classes = ['P', 'Ppt', 'Pbhh', 'Pbx', 'Ldiag', 'Pdiag', 'Mpt', 'Pedge']
    best = {k: {} for k in tg}          # target -> class -> (best validation error, eps, method)
    table = {}
    for cls in classes:
        for eps in ([3e-3] if cls == 'P' else [3e-4, 3e-3, 3e-2]):
            lines = make_lines(cls, n, eps, 'far')
            LF = Lanczos(lines, n, proj=0, con=0, track=False).run(x, y, w)
            L3c = Lanczos(lines, n, proj=2, con=1, track=False).run(x, y, w)
            sLF = inspace_test(LF.Q, w, x, y, lines, n, n); sL3 = inspace_test(L3c.Q, w, x, y, lines, n, n)
            A, _ = eval_basis_full(x, y, lines, n, real=True)
            Av, _ = eval_basis_full(xv, yv, lines, n, real=True)
            R1 = QRBasis(A, w, 'qr')
            fLF = fit_lanczos(LF, x, y, w, xv, yv, tg, tgv)
            fL3 = fit_lanczos(L3c, x, y, w, xv, yv, tg, tgv)
            fR1 = fit_qr(R1, A, Av, w, tg, tgv)
            table[(cls, eps)] = (fLF, fL3, fR1, sLF, sL3, orth_defect(LF.Q, w), orth_defect(L3c.Q, w))
            say(f"\n{cls:6s} eps={eps:.0e}  span24: LF {sLF:.1e}  L3c {sL3:.1e}   delta: LF {orth_defect(LF.Q, w):.1e}  L3c {orth_defect(L3c.Q, w):.1e}")
            for k in tg:
                say(f"    {k}:  LF {fLF[k][0]:9.2e} / {fLF[k][1]:9.2e}    L3c {fL3[k][0]:9.2e} / {fL3[k][1]:9.2e}    R1 {fR1[k][0]:9.2e} / {fR1[k][1]:9.2e}")
                # headline method: the Lanczos variant with the smaller span error; record its validation error
                head = fLF if sLF <= sL3 else fL3
                cur = best[k].get(cls)
                if cur is None or head[k][1] < cur[0]:
                    best[k][cls] = (head[k][1], eps, 'LF' if sLF <= sL3 else 'L3c', head[k][0])
    # K2 summary
    say("\n=== K2 summary at n = 24 (validation-grid error of the headline Lanczos fit, best eps per class; training error in brackets) ===")
    for k in tg:
        pe = best[k]['P'][0]
        say(f"\n  target {k}: polynomials P: {pe:.2e}  [{best[k]['P'][3]:.2e}]")
        for cls in classes:
            if cls == 'P' or cls not in best[k]:
                continue
            v, eps, meth, tr = best[k][cls]
            say(f"    {cls:6s} best eps={eps:.0e} ({meth}): {v:.2e}  [{tr:.2e}]   gain over P = {pe / v:7.2f}x")
        bc = min((c for c in best[k] if c != 'P'), key=lambda c: best[k][c][0])
        say(f"    -> best pencil class {bc}: gain {pe / best[k][bc][0]:.2f}x over polynomials (validation); training-grid gain {best[k]['P'][3] / best[k][bc][3]:.2f}x")
    # ---------------- T2b: BHH tensor spaces
    say("\n=== T2b: BHH tensor space at matched dimension (truncated SVD 1e-12 of the scaled partial-fraction basis; R1 = QR) ===")
    for lab, edges, Nq, Np in [('BHHxy', ('x', 'y'), 12, 5), ('BHHx', ('x',), 24, 5)]:
        for eps in [3e-4, 3e-3, 3e-2]:
            B = bhh_basis(x, y, eps, Np, Nq, edges); Bv = bhh_basis(xv, yv, eps, Np, Nq, edges)
            R2 = QRBasis(B, w, 'svd', 1e-12); R1 = QRBasis(B, w, 'qr')
            f2 = fit_qr(R2, B, Bv, w, tg, tgv); f1 = fit_qr(R1, B, Bv, w, tg, tgv)
            say(f"  {lab:6s} dim={B.shape[1]} eps={eps:.0e} rank(1e-12)={R2.rank} kappa={R2.cond:.1e}: " +
                "  ".join(f"{k}: SVD {f2[k][0]:.2e}/{f2[k][1]:.2e} QR {f1[k][0]:.2e}/{f1[k][1]:.2e}" for k in tg))
    # ---------------- convergence in n
    say("\n=== convergence in n (validation-grid error of the LF fit; eps as given; far-first) ===")
    for eps in [3e-4, 3e-3, 3e-2]:
        say(f"\n  eps_min = {eps:.0e}")
        say("   class |  n=8 (N=45)        n=12 (N=91)       n=16 (N=153)      n=20 (N=231)      n=24 (N=325)")
        for cls in ['P', 'Ppt', 'Pbhh', 'Ldiag', 'Pdiag']:
            rows = {k: [] for k in tg}
            for nn in (8, 12, 16, 20, 24):
                lines = make_lines(cls, nn, eps, 'far')
                LF = Lanczos(lines, nn, proj=0, con=0, track=False).run(x, y, w)
                f = fit_lanczos(LF, x, y, w, xv, yv, tg, tgv)
                for k in tg:
                    rows[k].append(f[k][1])
            for k in tg:
                say(f"   {cls:5s} {k}: " + "  ".join(f"{v:9.2e}" for v in rows[k]))
    say(f"\ntotal wall time {time.perf_counter()-T0:.1f} s")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T2.out'), 'w') as fh:
        fh.write("\n".join(OUT) + "\n")
