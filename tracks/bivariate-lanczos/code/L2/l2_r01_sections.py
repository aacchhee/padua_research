"""R01 (b): section accuracy on semi-orthogonal runs (IDEA?bivariate-lanczos-claude-203) and span drift under
full reorthogonalization (IDEA?...-204).  Kill rules in directions/L2/candidates.md (written before this script
was run).  Runs per benchmark: plain BJ ('none'), BJ + CGS2 against all previous columns ('fullcgs2'),
BJ + oracle partial reorthogonalization at sqrt(u) ('oracle').  MEASURED only.
Usage: python3 -I l2_r01_sections.py [bench ...] > logs/r01_sections.log"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C

U, SQRTU, U34 = C.U, C.SQRTU, C.U34


def degrees(nmax):
    if nmax >= 40:
        return [8, 16, 24, 32, 40, nmax]
    st = 4 if nmax >= 28 else 2
    ns = list(range(4, nmax + 1, st))
    if nmax not in ns: ns.append(nmax)
    return ns


def main(names):
    print(f"# l2_r01_sections.py numpy={np.__version__} u=2^-53 sqrt(u)={SQRTU:.2e} u^(3/4)={U34:.2e}", flush=True)
    for name in names:
        t0 = time.time()
        P, w, nmax = C.benchmark(name)
        x, y = P[:, 0].copy(), P[:, 1].copy()
        ns = degrees(nmax)
        print(f"== {name}: M={len(x)} nmax={nmax}", flush=True)
        for mode in ('none', 'fullcgs2', 'oracle'):
            Q, coef, tab, st = C.run(x, y, w, nmax, reorth=mode)
            recs = C.section_errors(Q, coef, tab, x, y, ns)
            dr = C.drift(Q, P, w, ns) if mode != 'oracle' else [None] * len(ns)
            th = {'rot0.3': 0.3, 'rotpi4': np.pi / 4}.get(name, 0.0)
            dr2 = C.drift(Q, P, w, ns, theta=th) if (th and mode != 'oracle') else [None] * len(ns)
            nJ = np.abs(x).max()
            kill = {'F': [], 'tau': [], 'H': []}
            for r, d, d2 in zip(recs, dr, dr2):
                so = r['loss'] <= SQRTU
                line = (f"   {mode:8s} n={r['n']:2d} L={r['loss']:.1e} {'SO' if so else '  '} local={r['local']:.1e} "
                        f"eF={r.get('eF', np.nan):.1e} etau={r.get('etau', np.nan):.1e} eH={r.get('eH', np.nan):.1e} "
                        f"|Cres|={r['cres']:.1e} K={r['K']:.1e} defJ={r['defJ']:.1e} defF={r['defF']:.1e}")
                line += f" thetaLB={r['defJ'] / (2 * nJ):.1e}"
                r['thetaLB'] = r['defJ'] / (2 * nJ)
                if d is not None:
                    line += f" drift={d['drift']:.1e} (ref u*kappa={d['ref_bound']:.1e})"
                    r.update(d)
                if d2 is not None:
                    line += f" drift_unrot={d2['drift']:.1e} (ref {d2['ref_bound']:.1e})"
                    r['drift_unrot'] = d2['drift']; r['ref_unrot'] = d2['ref_bound']
                print(line, flush=True)
                if so:
                    for key, nm in (('eF', 'F'), ('etau', 'tau'), ('eH', 'H')):
                        if r.get(key, 0) > U34:
                            kill[nm].append(r['n'])
                print('JSON ' + json.dumps(dict(bench=name, mode=mode, **r)), flush=True)
            print(f"   {mode:8s} stats {st}; semi-orthogonal degrees with e > u^(3/4): {kill}", flush=True)
        print(f"# {name} done in {time.time() - t0:.1f}s", flush=True)


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else C.BENCH)
