"""R02: selection rules vs the space channel (IDEA?bivariate-lanczos-claude-207; kill rule in candidates.md written
before this script was run).  For each benchmark and selection rule: (A) fullcgs2 -> defects, theta_LB, reference
drift; (B) two-pass window, no reorthogonalization -> loss, local level, defects.  Control: two-relation block
recurrence (2 passes).  MEASURED only.  Usage: python3 -I l2_r02_selection.py [bench ...] > logs/r02_selection.raw"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C

U, SQRTU = C.U, C.SQRTU
SETS = ['rot0.3', 'rotpi4', 'disk', 'triangle', 'lshape', 'annulus', 'square', 'tensor41', 'cb_cubic']
SELS = ['dev', 'mirror', 'alt', 'adapt']


def refs(name, P, w, ns):
    out = {}
    th = {'rot0.3': 0.3, 'rotpi4': np.pi / 4}.get(name)
    for n in ns:
        if th is not None:
            Uref, kap = C.cheb_reference(P, w, n, theta=th)
        elif name == 'triangle':
            Uref, kap = C.koornwinder_reference(P, w, n)
        else:
            Uref, kap = C.cheb_reference(P, w, n)
        out[n] = (Uref, kap)
    return out


def main(names):
    print(f"# l2_r02_selection.py numpy={np.__version__} u=2^-53", flush=True)
    for name in names:
        t0 = time.time()
        P, w, nmax = C.benchmark(name)
        x, y = P[:, 0].copy(), P[:, 1].copy()
        nX, nY = np.abs(x).max(), np.abs(y).max()
        st = 4 if nmax > 24 else 2
        ns = [n for n in range(4, nmax + 1, st)]
        if nmax not in ns: ns.append(nmax)
        R = refs(name, P, w, ns)
        print(f"== {name}: M={len(x)} nmax={nmax}; reference u*kappa: " +
              " ".join(f"{n}:{U * R[n][1]:.0e}" for n in ns), flush=True)
        runs = [(s, 'fullcgs2') for s in SELS] + [(s, 'w2') for s in SELS] + [('tworel2', 'tworel')]
        for sel, mode in runs:
            if mode == 'tworel':
                Q = C.two_relation(x, y, w, nmax, passes=2)
            else:
                Q, info, stt = C.run_sel(x, y, w, nmax, sel=sel, orth='cgs2w',
                                         reorth=('fullcgs2' if mode == 'fullcgs2' else 'none'))
            dX, dY, L, mu = C.defects(Q, x, y, nmax)
            line = []
            for n in ns:
                lb = max(dX[:n].max() / (2 * nX), dY[:n].max() / (2 * nY))
                dr = C.drift_ref(Q, R[n][0], n)
                rec = dict(bench=name, sel=sel, mode=mode, n=n, loss=float(L[n]), local=float(mu[n]),
                           dX=float(dX[:n].max()), dY=float(dY[:n].max()), thetaLB=float(lb), drift=dr,
                           ref=float(U * R[n][1]))
                print('JSON ' + json.dumps(rec), flush=True)
                line.append(f"{n}:L{L[n]:.0e}/lb{lb:.0e}/dr{dr:.0e}")
            print(f"   {sel:7s} {mode:8s} " + " ".join(line), flush=True)
        print(f"# {name} done in {time.time() - t0:.1f}s", flush=True)


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else SETS)
