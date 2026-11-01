"""R02: PRO-2D = two-pass window + omega-triggered partial reorthogonalization (BJ ordering), IDEA?bivariate-
lanczos-claude-208 (kill rule in candidates.md, written before this script was run).  Trigger: sign-matched
estimate E1D crossing sqrt(u); reorthogonalize against {|omega~| > u^(3/4)} (two CGS passes) + window pass; next
column likewise.  Reports L(n), e_F at semi-orthogonal degrees, reorthogonalization dot products vs fullcgs2.
MEASURED only.  Usage: python3 -I l2_r02_pro.py [bench ...] > logs/r02_pro.raw"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C

U, SQRTU, U34 = C.U, C.SQRTU, C.U34


def main(names):
    print(f"# l2_r02_pro.py numpy={np.__version__} u=2^-53", flush=True)
    for name in names:
        t0 = time.time()
        P, w, nmax = C.benchmark(name)
        x, y = P[:, 0].copy(), P[:, 1].copy()
        est = C.OmegaEst(nmax, mode='sign', jmeasure=JMEAS)
        Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs2w', reorth='est', est=est)
        L = C.loss_by_degree(Q, nmax)
        ns = sorted(set(list(range(4, nmax + 1, 4)) + [nmax]))
        recs = C.section_errors(Q, coef, tab, x, y, ns)
        N = Q.shape[1]
        full = N * (N - 1)          # fullcgs2: 2k dot products for column k
        kill_L = [n for n in range(nmax + 1) if L[n] > 10 * SQRTU]
        kill_F = [r['n'] for r in recs if r['loss'] <= SQRTU and r.get('eF', 0) > U34]
        print(f"== {name}: M={len(x)} nmax={nmax} N={N}: reorth columns {st['n_reorth']}, vectors {st['reorth_vectors']}, "
              f"window dots {st['dots_window']}, reorth dots {st['dots_reorth']} = {st['dots_reorth'] / full:.3f} of fullcgs2 "
              f"({full}); measured dots {st['dots_measure']}; (reorth+measure)/fullcgs2 = {(st['dots_reorth'] + st['dots_measure']) / full:.3f}; "
              f"total (window+reorth+measure)/fullcgs2 = {(st['dots_window'] + st['dots_reorth'] + st['dots_measure']) / full:.3f}", flush=True)
        print("   L(n): " + " ".join(f"{n}:{L[n]:.1e}" for n in ns), flush=True)
        print("   eF/etau/eH/defJ: " + " ".join(f"{r['n']}:{r.get('eF', np.nan):.0e}/{r.get('etau', np.nan):.0e}/"
                                               f"{r.get('eH', np.nan):.0e}/{r['defJ']:.0e}" for r in recs), flush=True)
        print(f"   kill L>10sqrt(u): {kill_L}; kill eF>u^3/4 at SO: {kill_F}; time {time.time() - t0:.1f}s", flush=True)
        print('JSON ' + json.dumps(dict(bench=name, L=L.tolist(), stats=st, full=full, recs=recs,
                                         kill_L=kill_L, kill_F=kill_F)), flush=True)


JMEAS = False
if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--jmeasure':
        JMEAS = True; args = args[1:]
    print(f"# trigger: {'E2D (J-rows measured)' if JMEAS else 'E1D (rounding-only)'}", flush=True)
    main(args if args else C.BENCH)
