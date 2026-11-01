"""R02 cost / M-scaling driver (also the driver for the M = 1e6 Runs needed on syvert0/1/2).

For each node set and M: wall time, dot-product counts, loss L(nmax), reference-free drift bound theta_LB(nmax)
and reference drift at nmax, for the methods
  bj1      BJ, one CGS window pass                      (L1 baseline)
  bj2w     BJ, two-pass window                          (IDEA?...-206)
  proJ     BJ, two-pass window + omega-triggered partial reorthogonalization, J-rows measured (IDEA?...-209)
  adapt2w  adaptive selection (reconstruction 01), two-pass window, no reorthogonalization (IDEA?...-207)
  fullcgs2 BJ, CGS2 against all previous columns         (V+A-type, O(M N^2))
  tworel2  two-relation block recurrence, 2 passes      (control)
Node sets: 'rotpi4' (uniform square rotated by pi/4, rng seed 11) and 'triangle' (uniform on the triangle
x, y >= -1, x + y <= 0, rng seed 12; vectorised rejection), unit weights.  MEASURED only.

Usage: python3 -I l2_r02_cost.py --sets rotpi4,triangle --M 1681,10000,100000 [--n24 24 --n20 20]
       [--methods bj1,bj2w,proJ,adapt2w,fullcgs2,tworel2] [--noref] > out.jsonl
Environment knobs: OMP_NUM_THREADS / OPENBLAS_NUM_THREADS (record them).  Memory ~ 6 * M * N * 8 bytes peak.
"""
import sys, os, json, time, argparse, platform
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C


def nodes(name, M):
    if name == 'rotpi4':
        P = np.random.default_rng(11).uniform(-1, 1, (M, 2))
        return C.L1.rotate(P, np.pi / 4)
    if name == 'triangle':
        rng = np.random.default_rng(12)
        out = np.zeros((0, 2))
        while len(out) < M:
            Z = rng.uniform(0, 1, (2 * M, 2))
            out = np.vstack([out, Z[Z.sum(axis=1) <= 1]])
        return 2 * out[:M] - 1
    raise ValueError(name)


def method(name, x, y, w, nmax):
    t0 = time.perf_counter()
    st = {}
    if name == 'bj1':
        Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs')
    elif name == 'bj2w':
        Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs2w')
    elif name == 'proJ':
        est = C.OmegaEst(nmax, mode='sign', jmeasure=True)
        Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs2w', reorth='est', est=est)
    elif name == 'adapt2w':
        Q, info, st = C.run_sel(x, y, w, nmax, sel='adapt', orth='cgs2w')
    elif name == 'fullcgs2':
        Q, coef, tab, st = C.run(x, y, w, nmax, reorth='fullcgs2')
    elif name == 'tworel2':
        Q = C.two_relation(x, y, w, nmax, passes=2)
    else:
        raise ValueError(name)
    return Q, st, time.perf_counter() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sets', default='rotpi4,triangle')
    ap.add_argument('--M', default='1681,10000,100000')
    ap.add_argument('--methods', default='bj1,bj2w,proJ,adapt2w,fullcgs2,tworel2')
    ap.add_argument('--nrot', type=int, default=24)
    ap.add_argument('--ntri', type=int, default=20)
    ap.add_argument('--noref', action='store_true')
    a = ap.parse_args()
    env = dict(python=platform.python_version(), numpy=np.__version__, machine=platform.node(),
               threads=os.environ.get('OMP_NUM_THREADS'), blas_threads=os.environ.get('OPENBLAS_NUM_THREADS'))
    print('# ' + json.dumps(env), flush=True)
    for sname in a.sets.split(','):
        nmax = a.nrot if sname == 'rotpi4' else a.ntri
        for M in [int(v) for v in a.M.split(',')]:
            P = nodes(sname, M); x, y = P[:, 0].copy(), P[:, 1].copy(); w = np.ones(M)
            Uref = kap = None
            if not a.noref:
                t0 = time.perf_counter()
                if sname == 'rotpi4':
                    Uref, kap = C.cheb_reference(P, w, nmax, theta=np.pi / 4)
                else:
                    Uref, kap = C.koornwinder_reference(P, w, nmax)
                tref = time.perf_counter() - t0
            for mname in a.methods.split(','):
                Q, st, tm = method(mname, x, y, w, nmax)
                dX, dY, L, mu = C.defects(Q, x, y, nmax)
                lb = max(dX.max() / (2 * np.abs(x).max()), dY.max() / (2 * np.abs(y).max()))
                rec = dict(set=sname, M=M, n=nmax, N=Q.shape[1], method=mname, time=tm, loss=float(L[nmax]),
                           local=float(mu[nmax]), thetaLB=float(lb), stats=st)
                if Uref is not None:
                    rec['drift'] = C.drift_ref(Q, Uref, nmax); rec['ref'] = float(C.U * kap)
                print(json.dumps(rec), flush=True)
                del Q


if __name__ == '__main__':
    main()
