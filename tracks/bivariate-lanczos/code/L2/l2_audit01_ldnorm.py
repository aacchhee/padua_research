"""Response to Codex audit-01, finding L2-F5: the R03 'ld' variant of l2_core.run (dots='ld') performs the
product, the window dot products and the update in x87 long double but casts the residual to float64 BEFORE the
normalisation, so beta and q are computed in double.  This script (new; l2_core.py is not modified) re-implements
that branch for the R03 setting (BJ block window, ONE CGS pass, no reorthogonalisation) with two normalisation
options and compares them:

  'ld'  : as l2_core.run(dots='ld'):  r = fl64(r_LD);  beta = sqrt(r.r) in double;  q = r / beta in double
  'ldn' : normalisation in long double: beta_LD = sqrt(r_LD.r_LD), q = fl64(r_LD / beta_LD) (one final rounding to
          the stored double vector); column 0 likewise (v_LD / ||v_LD||, one rounding)

Control: the re-implemented 'ld' must reproduce l2_core.run(dots='ld') bit for bit (checked and printed).
Also printed: the 'double' baseline (l2_core.run, dots='double').  Vectors are stored in double in every variant.
MEASURED only (floating point).  Usage (from this directory):
    python3 -I l2_audit01_ldnorm.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_ldnorm.raw
"""
import sys, os, json, time, platform
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C

U, SQRTU = C.U, C.SQRTU
SETS = ['cb_quad', 'cb_cubic', 'cb_quart', 'cb_cubic36', 'cb_cheb', 'rotpi4', 'triangle', 'tensor41']
LD = np.longdouble


def run_ld(x, y, w, nmax, norm='ld'):
    """BJ block window, one CGS pass, step in long double; norm in {'ld' (normalise in double, as l2_core),
    'ldn' (normalise in long double)}.  Returns Q (float64)."""
    tab = C.tables(nmax)
    idx, pos, parent, op, start = tab
    N = len(idx)
    x = np.asarray(x, dtype=np.float64); y = np.asarray(y, dtype=np.float64)
    M = len(x)
    Q = np.zeros((M, N), dtype=np.float64)
    v = np.sqrt(np.asarray(w, dtype=np.float64))
    if norm == 'ldn':
        vL = v.astype(LD)
        Q[:, 0] = (vL / np.sqrt(vL @ vL)).astype(np.float64)
    else:
        Q[:, 0] = v / np.sqrt(v @ v)
    xL, yL = x.astype(LD), y.astype(LD)
    for k in range(1, N):
        t, j = idx[k]
        p = parent[k]
        lo = start[max(t - 2, 0)]
        W = np.arange(lo, k)                                   # block window
        Qw = Q[:, W]
        QwL = Qw.astype(LD)
        aL = (xL if op[k] == 'J' else yL) * Q[:, p].astype(LD)
        hL = QwL.T @ aL
        rL = aL - QwL @ hL
        if norm == 'ldn':
            betaL = np.sqrt(rL @ rL)
            Q[:, k] = (rL / betaL).astype(np.float64)
        else:
            r = rL.astype(np.float64)                          # l2_core: "normalisation then in double"
            beta = float(np.sqrt(r @ r))
            Q[:, k] = r / beta
    return Q


def lb_of(dX, dY, x, y, nmax):
    return [max(dX[:n].max() / (2 * np.abs(x).max()), dY[:n].max() / (2 * np.abs(y).max())) if n else 0.0
            for n in range(nmax + 1)]


def main(names):
    print(f"# l2_audit01_ldnorm.py python={platform.python_version()} numpy={np.__version__} "
          f"longdouble eps={np.finfo(LD).eps!r} u=2^-53", flush=True)
    for name in names:
        t0 = time.time()
        P, w, nmax = C.benchmark(name)
        x, y = P[:, 0].copy(), P[:, 1].copy()
        nmax = min(nmax, 24 if name in ('rotpi4',) else (20 if name == 'triangle' else nmax))
        print(f"== {name}: M={len(x)} nmax={nmax}", flush=True)
        Qd, _, _, _ = C.run(x, y, w, nmax, orth='cgs', dots='double')
        Qc, _, _, _ = C.run(x, y, w, nmax, orth='cgs', dots='ld')
        Qld = run_ld(x, y, w, nmax, norm='ld')
        Qldn = run_ld(x, y, w, nmax, norm='ldn')
        same = bool(np.array_equal(Qc, Qld))
        print(f"   control: re-implemented 'ld' == l2_core.run(dots='ld') bitwise: {same}; "
              f"max|diff| = {float(np.abs(Qc - Qld).max()):.1e}", flush=True)
        res = {}
        for lab, Q in (('double', Qd), ('ld', Qld), ('ldn', Qldn)):
            dX, dY, L, mu = C.defects(Q, x, y, nmax)
            lb = lb_of(dX, dY, x, y, nmax)
            res[lab] = (L, lb)
            print(f"   {lab:6s} L: " + " ".join(f"{n}:{L[n]:.2e}" for n in range(8, nmax + 1, 4)) +
                  f" | {nmax}:{L[nmax]:.2e}  thetaLB({nmax})={lb[nmax]:.2e}", flush=True)
            print('JSON ' + json.dumps(dict(bench=name, variant=lab, L=L.tolist(), thetaLB=lb, local=mu.tolist(),
                                            control_bitwise=same)), flush=True)
        degs = (16, 20) if name == 'triangle' else (20, 24)
        degs = tuple(d for d in degs if d <= nmax)
        Ld, Lld, Lldn = res['double'][0], res['ld'][0], res['ldn'][0]
        print("   ratios double/variant: " + " ".join(
            f"n={d}: ld {Ld[d] / Lld[d]:.2f}, ldn {Ld[d] / Lldn[d]:.2f}" for d in degs) +
            f"; thetaLB({nmax}) double/ld/ldn = {res['double'][1][nmax]:.2e}/{res['ld'][1][nmax]:.2e}/"
            f"{res['ldn'][1][nmax]:.2e}", flush=True)
        print(f"# {name} done in {time.time() - t0:.1f}s", flush=True)


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else SETS)
