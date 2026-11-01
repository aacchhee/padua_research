"""R03: correctly rounded / long-double window dot products vs the coefficient channel (IDEA?bivariate-lanczos-
claude-210; kill rules in candidates.md written before this script was run).  BJ block window, one CGS pass,
dots in {'double', 'exact', 'ld'}; reports L(n), theta_LB; plus PRO-2D-J with exact dots on the cubic checkerboard.
MEASURED only.  Usage: python3 -I l2_r03_dots.py > logs/r03_dots.raw"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C

U, SQRTU = C.U, C.SQRTU
SETS = ['cb_quad', 'cb_cubic', 'cb_quart', 'cb_cubic36', 'cb_cheb', 'rotpi4', 'triangle', 'tensor41']


def main(names):
    print(f"# l2_r03_dots.py numpy={np.__version__} u=2^-53", flush=True)
    for name in names:
        t0 = time.time()
        P, w, nmax = C.benchmark(name)
        x, y = P[:, 0].copy(), P[:, 1].copy()
        nmax = min(nmax, 24 if name in ('rotpi4',) else (20 if name == 'triangle' else nmax))
        print(f"== {name}: M={len(x)} nmax={nmax}", flush=True)
        for dots in ('double', 'exact', 'ld'):
            Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs', dots=dots)
            dX, dY, L, mu = C.defects(Q, x, y, nmax)
            lb = [max(dX[:n].max() / (2 * np.abs(x).max()), dY[:n].max() / (2 * np.abs(y).max())) if n else 0.0
                  for n in range(nmax + 1)]
            print(f"   {dots:6s} L: " + " ".join(f"{n}:{L[n]:.1e}" for n in range(8, nmax + 1, 4)) +
                  f" | {nmax}:{L[nmax]:.1e}  thetaLB({nmax})={lb[nmax]:.1e}", flush=True)
            print('JSON ' + json.dumps(dict(bench=name, dots=dots, L=L.tolist(), thetaLB=lb, local=mu.tolist())),
                  flush=True)
        if name == 'cb_cubic':
            for dots in ('double', 'exact'):
                est = C.OmegaEst(nmax, mode='sign', jmeasure=True)
                Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs2w', reorth='est', est=est, dots=dots)
                L = C.loss_by_degree(Q, nmax)
                print(f"   PRO-2D-J dots={dots}: L: " + " ".join(f"{n}:{L[n]:.1e}" for n in range(16, nmax + 1, 2))
                      + f" reorth cols {st['n_reorth']}", flush=True)
                print('JSON ' + json.dumps(dict(bench=name, dots=dots, pro=True, L=L.tolist(), stats=st)), flush=True)
        print(f"# {name} done in {time.time() - t0:.1f}s", flush=True)


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else SETS)
