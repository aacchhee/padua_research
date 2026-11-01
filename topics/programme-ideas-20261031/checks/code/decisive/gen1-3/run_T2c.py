"""Decisive test gen1-3, supplement T2c (POST HOC, not pre-registered; written after T2 showed training/
validation gaps of 1e3..1e18 for poles at or near the Chebyshev-grid resolution).

Question: does the approximation payoff of the pencil classes over polynomials survive when the sampling
is lightning-style, i.e. exponentially clustered towards the corner singularity (BHH / HHT practice),
so that the least-squares fit controls the approximant near the poles?

Training set: 64^2 Chebyshev grid plus 25 x 9 polar points about the corner (1,1), radii geometric from
0.7 down to 1e-5, 9 angles inside the square. Validation set: 97^2 Chebyshev grid plus 24 x 11 polar
points at the geometric midpoints of the training radii (disjoint). Unit weights. Errors: relative RMS
and relative max over the validation set; training relative RMS. Classes P, Ppt, Pbhh, Ldiag, Pdiag,
Mpt (far-first) at eps_min in {3e-5, 3e-4, 3e-3, 3e-2}, n = 16 and 24, LF (full reorthogonalisation)
fit; BHH tensor space (dimension 324) by truncated SVD for reference. Targets fA, fB, fC.
Outputs: T2c.out. MEASURED within this scope only.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orf2d import *
from run_T2 import bhh_basis

OUT = []


def say(s=""):
    print(s, flush=True)
    OUT.append(s)


def polar_points(radii, nang):
    phis = (np.arange(nang) + 0.5) * (np.pi / 2) / nang
    R, PH = np.meshgrid(radii, phis)
    return (1 - R * np.cos(PH)).ravel(), (1 - R * np.sin(PH)).ravel()


if __name__ == '__main__':
    T0 = time.perf_counter()
    K = 25
    rho = (1e-5 / 0.7) ** (1 / (K - 1))
    r_tr = 0.7 * rho ** np.arange(K)
    r_va = 0.7 * rho ** (np.arange(K - 1) + 0.5)
    xg, yg = cheb_grid(64); xc, yc = polar_points(r_tr, 9)
    x, y = np.concatenate([xg, xc]), np.concatenate([yg, yc]); w = np.ones(len(x))
    xvg, yvg = cheb_grid(97); xvc, yvc = polar_points(r_va, 11)
    xv, yv = np.concatenate([xvg, xvc]), np.concatenate([yvg, yvc])
    tg, tgv = targets(x, y), targets(xv, yv)
    say(f"T2c (post hoc): clustered sampling. training M = {len(x)} ({len(xg)} grid + {len(xc)} polar, r >= {r_tr.min():.0e}); validation {len(xv)} points")
    say("entries: training relRMS / validation relRMS / validation relMAX")
    best = {}
    for n in (16, 24):
        say(f"\n=== n = {n}, N = {(n+1)*(n+2)//2} ===")
        for cls in ['P', 'Ppt', 'Pbhh', 'Ldiag', 'Pdiag', 'Mpt']:
            for eps in ([3e-3] if cls == 'P' else [3e-5, 3e-4, 3e-3, 3e-2]):
                lines = make_lines(cls, n, eps, 'far')
                LF = Lanczos(lines, n, proj=0, con=0, track=False).run(x, y, w)
                Qv = LF.evaluate(xv, yv)
                row = []
                for k in tg:
                    err, cq, fit = ls_fit(LF.Q, w, tg[k])
                    fv = np.real(Qv @ cq)
                    e2 = float(np.linalg.norm(fv - tgv[k]) / np.linalg.norm(tgv[k]))
                    einf = float(np.max(np.abs(fv - tgv[k])) / np.max(np.abs(tgv[k])))
                    row.append(f"{k}: {err:.1e}/{e2:.1e}/{einf:.1e}")
                    key = (n, k, cls)
                    if key not in best or e2 < best[key][0]:
                        best[key] = (e2, eps, einf)
                say(f"  {cls:6s} eps={eps:.0e} span24={inspace_test(LF.Q, w, x, y, lines, n, n):.0e} delta={orth_defect(LF.Q, w):.0e}  " + "  ".join(row))
        # BHH tensor reference at n = 24 only (dimension 324)
        if n == 24:
            for eps in [3e-5, 3e-4, 3e-3, 3e-2]:
                B = bhh_basis(x, y, eps, 5, 12); Bv = bhh_basis(xv, yv, eps, 5, 12)
                R2 = QRBasis(B, w, 'svd', 1e-12)
                row = []
                for k in tg:
                    err, cq, fit = ls_fit(R2.Q, w, tg[k])
                    fv = np.real(R2.evaluate_fit(Bv, cq))
                    e2 = float(np.linalg.norm(fv - tgv[k]) / np.linalg.norm(tgv[k]))
                    einf = float(np.max(np.abs(fv - tgv[k])) / np.max(np.abs(tgv[k])))
                    row.append(f"{k}: {err:.1e}/{e2:.1e}/{einf:.1e}")
                say(f"  BHHxy  eps={eps:.0e} rank={R2.rank}/{B.shape[1]}  " + "  ".join(row))
        say(f"\n  summary n = {n}: best validation relRMS per class (eps), gain over P:")
        for k in tg:
            pe = best[(n, k, 'P')][0]
            parts = []
            for cls in ['Ppt', 'Pbhh', 'Ldiag', 'Pdiag', 'Mpt']:
                e2, eps, einf = best[(n, k, cls)]
                parts.append(f"{cls} {e2:.1e} ({eps:.0e}) x{pe/e2:.1f}")
            say(f"    {k}: P {pe:.1e} | " + "; ".join(parts))
    say(f"\ntotal wall time {time.perf_counter()-T0:.1f} s")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T2c.out'), 'w') as fh:
        fh.write("\n".join(OUT) + "\n")
