"""Decisive test gen1-3, tests T1 (K1: conditioned-solver payoff) and T3 (K3: windowed recurrence).

Scope S1: 64x64 Chebyshev grid (M = 4096), unit weights, n = 24 (N = 325), classes Ppt (target fB) and
Pbhh (target fA); eps_min in {3e-4 (primary), 3e-3, 3e-2}; orderings far (primary) / near.
Scope S2: M = 400 uniform random nodes, n = 22 (N = 276), seeds 1, 2; primary eps_min.
Methods: L3 = adversary's three-block projection-only window (pre-registered; algebraically wrong, see
the .md), L3c = project two blocks + constrain with the third (corrected window, found during this
test), L4c = project three + constrain one, LF = full reorthogonalisation, R1/R2/R3 = QR / truncated
SVD / graded QR of the evaluated basis; LF80, L3c80 = 80-bit versions.
Outputs: T1_T3.out. Everything MEASURED within this scope only.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orf2d import *

OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def method_report(lab, Q, w, x, y, lines, n, tg, tref=None, tm=None, extra=""):
    e24 = inspace_test(Q, w, x, y, lines, n, n)
    e12 = inspace_test(Q, w, x, y, lines, n, n // 2)
    dlt = orth_defect(Q, w.astype(np.longdouble) if Q.dtype in (np.clongdouble,) else w)
    errs = {k: ls_fit(Q, w.astype(np.longdouble) if Q.dtype == np.clongdouble else w, f.astype(np.longdouble) if Q.dtype == np.clongdouble else f)[0] for k, f in tg.items()}
    cols = f"{lab:7s} delta={dlt:8.1e}  span24={e24:8.1e}  span12={e12:8.1e}  " + "  ".join(f"{k}={v:9.3e}" for k, v in errs.items())
    if tm is not None:
        cols += f"  t={tm:6.2f}s"
    say("    " + cols + ("  " + extra if extra else ""))
    return dict(delta=dlt, span24=e24, span12=e12, errs=errs, time=tm)


def run_scope(x, y, w, n, classes, eps_list, orders, targets_on, do80=True, label=""):
    M = len(x)
    say(f"\n=== scope {label}: M = {M}, n = {n}, N = {(n+1)*(n+2)//2} ===")
    for cls in classes:
        for eps in eps_list:
            for order in orders:
                lines = make_lines(cls, n, eps, order)
                tg = targets_on
                say(f"\n--- class {cls}, eps_min = {eps:.0e}, order = {order} ---")
                res = {}
                # Lanczos variants (double)
                for (p, c, fd, lab) in [(3, 0, True, 'L3'), (2, 1, False, 'L3c'), (3, 1, False, 'L4c'), (0, 0, False, 'LF')]:
                    L = Lanczos(lines, n, proj=p, con=c, fixed_dims=fd).run(x, y, w)
                    gN = min((g[0] for g in L.gapN if not np.isnan(g[0])), default=np.nan)
                    gR = min(g[0] for g in L.gapR)
                    dd = L.defect
                    growth = "defect/deg: " + " ".join(f"{dd[i]:.0e}" for i in range(1, len(dd), 3))
                    res[lab] = method_report(lab, L.Q, w, x, y, lines, n, tg, tm=L.time,
                                             extra=f"minsvN={gN:.1e} minkeptR={gR:.1e} dims(last)={L.dims[-1]}")
                    say(f"            {growth}")
                # evaluated-basis baselines
                A, pin = eval_basis_full(x, y, lines, n, real=True)
                t0 = time.perf_counter(); R1 = QRBasis(A, w, 'qr'); t1 = time.perf_counter() - t0
                res['R1'] = method_report('R1', R1.Q, w, x, y, lines, n, tg, tm=t1)
                t0 = time.perf_counter(); R2 = QRBasis(A, w, 'svd', 1e-12); t2 = time.perf_counter() - t0
                res['R2'] = method_report('R2', R2.Q, w, x, y, lines, n, tg, tm=t2, extra=f"rank={R2.rank}/{A.shape[1]} kappa={R2.cond:.1e}")
                Ag = eval_basis_graded(x, y, lines, n)
                t0 = time.perf_counter(); R3 = QRBasis(Ag, w, 'qr'); t3 = time.perf_counter() - t0
                res['R3'] = method_report('R3', R3.Q, w, x, y, lines, n, tg, tm=t3, extra=f"kappa_graded={QRBasis(Ag, w, 'svd').cond:.1e}")
                if do80 and eps == eps_list[0] and order == orders[0]:
                    L80 = Lanczos(lines, n, proj=0, con=0, dtype=np.clongdouble, track=False).run(x, y, w)
                    res['LF80'] = method_report('LF80', L80.Q, w, x, y, lines, n, tg, tm=L80.time)
                    L380 = Lanczos(lines, n, proj=2, con=1, dtype=np.clongdouble).run(x, y, w)
                    dd = L380.defect
                    res['L3c80'] = method_report('L3c80', L380.Q, w, x, y, lines, n, tg, tm=L380.time,
                                                 extra="defect/deg: " + " ".join(f"{dd[i]:.0e}" for i in range(1, len(dd), 3)))
                    # K1 summary line
                    ref = res['LF80']['errs']
                    bestL = min(('L3c', 'L4c', 'LF'), key=lambda k: res[k]['span24'])
                    bestR = min(('R1', 'R2', 'R3'), key=lambda k: res[k]['span24'])
                    say(f"    K1 data: best L = {bestL} (span24 {res[bestL]['span24']:.1e}), best R = {bestR} (span24 {res[bestR]['span24']:.1e}); "
                        f"ratio R/L = {res[bestR]['span24']/max(res[bestL]['span24'],1e-300):.1e}; LS vs LF80: " +
                        ", ".join(f"{k}: L={res[bestL]['errs'][k]/ref[k]:.3f}x R1={res['R1']['errs'][k]/ref[k]:.3f}x R2={res['R2']['errs'][k]/ref[k]:.3f}x R3={res['R3']['errs'][k]/ref[k]:.3f}x" for k in ref))
    return


if __name__ == '__main__':
    T0 = time.perf_counter()
    say("Decisive test gen1-3: T1 (K1) and T3 (K3). numpy " + np.__version__)
    say("delta = max|Q^H W Q - I|; span24 = max rel. residual of 5 random g in V_24 (p/pi_24); span12 = same for g = p/pi_12;")
    say("fA, fB = training-grid relative RMS LS error; minsvN = smallest nonzero singular value of the constraint matrix over all steps;")
    say("minkeptR = smallest kept relative singular value of the projected candidates; dims(last) = (rank of remainder, rank of constraint, block dim).")
    # ---------------- S1
    x, y = cheb_grid(64)
    w = np.ones(len(x))
    tg = targets(x, y)
    tgAB = {'fA': tg['fA'], 'fB': tg['fB']}
    n = 24
    # polynomial control first
    say("\n=== S1 polynomial control (class P, n = 24) ===")
    lines = make_lines('P', n, 3e-4)
    for (p, c, fd, lab) in [(3, 0, True, 'L3'), (2, 1, False, 'L3c'), (0, 0, False, 'LF')]:
        L = Lanczos(lines, n, proj=p, con=c, fixed_dims=fd).run(x, y, w)
        method_report(lab, L.Q, w, x, y, lines, n, tgAB, tm=L.time)
    A, _ = eval_basis_full(x, y, lines, n)
    R1 = QRBasis(A, w, 'qr'); method_report('R1', R1.Q, w, x, y, lines, n, tgAB, tm=R1.time)
    # primary classes, all eps, both orders
    run_scope(x, y, w, n, ['Ppt', 'Pbhh'], [3e-4, 3e-3, 3e-2], ['far', 'near'], tgAB, do80=True, label="S1 (64^2 Chebyshev grid)")
    # ---------------- S2
    for seed in (1, 2):
        xr, yr = random_nodes(400, seed)
        wr = np.ones(400)
        tgr = targets(xr, yr)
        run_scope(xr, yr, wr, 22, ['Ppt', 'Pbhh'], [3e-4], ['far', 'near'], {'fA': tgr['fA'], 'fB': tgr['fB']}, do80=True, label=f"S2 (400 random nodes, seed {seed})")
    say(f"\ntotal wall time {time.perf_counter()-T0:.1f} s")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T1_T3.out'), 'w') as fh:
        fh.write("\n".join(OUT) + "\n")
