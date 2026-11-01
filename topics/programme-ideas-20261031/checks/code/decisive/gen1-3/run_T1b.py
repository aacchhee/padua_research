"""Decisive test gen1-3, supplement T1b (written after seeing T1's first rows): which computed basis is
closest to the true space V_24, and which LS error is right?

Scope: S1 (64^2 Chebyshev grid, n = 24, N = 325), classes Ppt and Pbhh, eps_min in {3e-4, 3e-3},
far-first. Methods: LF (double), LF80 (80-bit full reorthogonalisation), R3 (Householder QR of the
unit-column-scaled graded complex basis T_a T_b / pi_t), R3-80 (two-pass Gram-Schmidt of the same graded
basis in 80-bit), L3c (double). Quantities:
  dist(X,Y) = || Q_X - Q_Y (Q_Y^H W Q_X) ||_2 = sin of the largest canonical angle between the two
              computed N-dimensional spaces (both bases orthonormal to ~u);
  LS errors fA, fB on the training grid;
  resorth(f) = max_j |a_j^H W r| / ||r||_W over the unit-norm graded basis columns a_j (double), r = the
              method's LS residual for target f: zero for the true LS residual in V_24 (A spans V_24
              exactly up to rounding in its entries), so it measures how far each computed space is
              from containing the true LS fit's missing directions;
  span24 / span12 as in T1 (corner-spike-dominated in-space tests).
Also the union space test: LS error of f in span(Q_LF) + span(Q_R3) (dimension <= 2N) -- a lower bound
for both methods' true-space error only if both spaces were subspaces of V_24, which they are not; it is
reported as a diagnostic only.
Outputs: T1b.out. MEASURED within this scope only.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orf2d import *

OUT = []


def say(s=""):
    print(s, flush=True)
    OUT.append(s)


def dist(QX, QY, w):
    QX = QX.astype(np.complex128); QY = QY.astype(np.complex128)
    return float(np.linalg.norm(np.sqrt(w)[:, None] * (QX - QY @ (QY.conj().T @ (w[:, None] * QX))), 2))


def graded_gs80(x, y, lines, n, w):
    xl, yl, wl = x.astype(np.longdouble), y.astype(np.longdouble), w.astype(np.longdouble)
    Vx, Vy = cheb_vander(xl, n), cheb_vander(yl, n)
    cols = []
    for t in range(n + 1):
        cols.append(cheb2_block(Vx, Vy, t).astype(np.clongdouble) / pi_vals(xl, yl, lines, t, dtype=np.clongdouble)[:, None])
    A = np.column_stack(cols)
    A = A / np.sqrt(np.real(np.sum(wl[:, None] * np.abs(A) ** 2, axis=0)))
    # plain (unpivoted) two-pass modified Gram-Schmidt, column order = graded order
    M, N = A.shape
    Q = np.empty_like(A)
    for j in range(N):
        v = A[:, j].copy()
        for _ in range(2):
            if j:
                v = v - Q[:, :j] @ (Q[:, :j].conj().T @ (wl * v))
        Q[:, j] = v / np.sqrt(np.real(np.sum(wl * np.abs(v) ** 2)))
    return Q


if __name__ == '__main__':
    T0 = time.perf_counter()
    x, y = cheb_grid(64); w = np.ones(len(x)); wl = w.astype(np.longdouble)
    tg = targets(x, y)
    n = 24
    say("T1b: subspace distances, 80-bit graded Gram-Schmidt reference, residual orthogonality. S1, n = 24.")
    for cls, eps in [('Ppt', 3e-4), ('Pbhh', 3e-4), ('Ppt', 3e-3), ('Pbhh', 3e-3)]:
        lines = make_lines(cls, n, eps, 'far')
        say(f"\n--- {cls}, eps_min = {eps:.0e}, far-first ---")
        t0 = time.perf_counter()
        LF = Lanczos(lines, n, proj=0, con=0, track=False).run(x, y, w)
        L3 = Lanczos(lines, n, proj=2, con=1, track=False).run(x, y, w)
        Ag = eval_basis_graded(x, y, lines, n)
        R3 = QRBasis(Ag, w, 'qr')
        Agd = Ag / np.linalg.norm(Ag, axis=0)
        LF80 = Lanczos(lines, n, proj=0, con=0, dtype=np.clongdouble, track=False).run(x, y, w)
        t1 = time.perf_counter(); Q380 = graded_gs80(x, y, lines, n, w); t380 = time.perf_counter() - t1
        say(f"    (LF80 {LF80.time:.0f} s, R3-80 {t380:.0f} s)")
        bases = {'LF': LF.Q, 'L3c': L3.Q, 'R3': R3.Q, 'LF80': LF80.Q.astype(np.complex128), 'R3-80': Q380.astype(np.complex128)}
        say("    orthogonality defect: " + "  ".join(f"{k}={orth_defect(Q, w):.1e}" for k, Q in bases.items()) +
            f"  (R3-80 in 80-bit: {orth_defect(Q380, wl):.1e}, LF80 in 80-bit: {orth_defect(LF80.Q, wl):.1e})")
        keys = list(bases)
        say("    dist(X,Y) = sin(max canonical angle):")
        for i, a in enumerate(keys):
            say("      " + f"{a:6s}" + "  ".join(f"{b}:{dist(bases[a], bases[b], w):8.1e}" for b in keys if b != a))
        say("    in-space tests span24 / span12:  " + "  ".join(f"{k}: {inspace_test(Q, w, x, y, lines, n, n):.1e}/{inspace_test(Q, w, x, y, lines, n, n//2):.1e}" for k, Q in bases.items()))
        for f_name in ('fA', 'fB'):
            f = tg[f_name]
            row = []
            for k, Q in bases.items():
                err, cq, fit = ls_fit(Q, w, f)
                r = f - fit
                ro = float(np.max(np.abs(Agd.conj().T @ (w * r))) / np.linalg.norm(np.sqrt(w) * r))
                row.append(f"{k}: {err:.3e} (resorth {ro:.1e})")
            # union space LF + R3
            U = np.column_stack([bases['LF'], bases['R3']])
            Uq, _ = np.linalg.qr(np.sqrt(w)[:, None] * U)
            err_u = float(np.linalg.norm(np.sqrt(w) * f - Uq @ (Uq.conj().T @ (np.sqrt(w) * f))) / np.linalg.norm(np.sqrt(w) * f))
            say(f"    {f_name}: " + "  ".join(row) + f"  | union(LF,R3): {err_u:.3e}")
        say(f"    wall {time.perf_counter()-t0:.0f} s")
    say(f"\ntotal wall time {time.perf_counter()-T0:.1f} s")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T1b.out'), 'w') as fh:
        fh.write("\n".join(OUT) + "\n")
