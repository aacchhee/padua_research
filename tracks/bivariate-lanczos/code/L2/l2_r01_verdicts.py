"""R01 verdicts: applies the pre-registered rules of directions/L2/candidates.md mechanically to the JSON lines of
logs/r01_omega.raw, r01_omega_e3.raw, r01_sections.raw, r01_sections_w2.raw.  Usage (from the L2 log dir):
python3 -I l2_r01_verdicts.py <logdir> > <logdir>/r01_verdicts.txt"""
import sys, os, json
import numpy as np

U = 2.0 ** -53
SQRTU, U34 = U ** 0.5, U ** 0.75


def rows(path):
    import gzip
    if not os.path.exists(path) and os.path.exists(path + '.gz'):
        f = gzip.open(path + '.gz', 'rt')
    else:
        f = open(path)
    return [json.loads(l[5:]) for l in f if l.startswith('JSON')]


def main(d):
    print("# R01 verdicts (u = 2^-53); rules: candidates.md (IDEA?...-201..206)")
    om = rows(os.path.join(d, 'r01_omega.raw')) + rows(os.path.join(d, 'r01_omega_e3.raw'))
    print("\n## IDEA-201/202/205: frozen kill rule U = max_D L/E > 10 kills; O = max_D E/L (tracking)")
    ests = sorted(set(r['est'] for r in om))
    benches = []
    for r in om:
        if r['bench'] not in benches:
            benches.append(r['bench'])
    print("bench      " + " ".join(f"{e:>17s}" for e in ests))
    worst = {e: (0.0, 0.0) for e in ests}
    for b in benches:
        cells = []
        for e in ests:
            rr = [r for r in om if r['bench'] == b and r['est'] == e]
            if not rr:
                cells.append(f"{'-':>17s}"); continue
            r = rr[-1]
            if r['U'] is None:
                cells.append(f"{'uninformative':>17s}")
            else:
                cells.append(f"U={r['U']:5.2f} O={r['O']:7.1e}")
                worst[e] = (max(worst[e][0], r['U']), max(worst[e][1], r['O']))
        print(f"{b:10s} " + " ".join(cells))
    for e in ests:
        print(f"  {e}: max U = {worst[e][0]:.3g} -> {'KILLED' if worst[e][0] > 10 else 'survives frozen kill test'}; "
              f"max O = {worst[e][1]:.2e}")
    sec = rows(os.path.join(d, 'r01_sections.raw')) + rows(os.path.join(d, 'r01_sections_w2.raw'))
    print("\n## IDEA-203 (frozen 2nd clause): semi-orthogonal (L <= sqrt u) degrees with e > u^(3/4), per section type")
    modes = []
    for r in sec:
        if r['mode'] not in modes:
            modes.append(r['mode'])
    kill_any = {'eF': [], 'etau': [], 'eH': []}
    for m in modes:
        for b in benches:
            rr = [r for r in sec if r['bench'] == b and r['mode'] == m and r['loss'] <= SQRTU]
            if not rr:
                continue
            fails = {k: [r['n'] for r in rr if r.get(k, 0) > U34] for k in ('eF', 'etau', 'eH')}
            mx = {k: max(r.get(k, 0) for r in rr) for k in ('eF', 'etau', 'eH')}
            mu = max(r['local'] for r in rr)
            for k in fails:
                if fails[k]:
                    kill_any[k].append(f"{b}/{m}")
            print(f"{m:9s} {b:9s} SO-degrees {rr[0]['n']}..{rr[-1]['n']}: max eF={mx['eF']:.1e} etau={mx['etau']:.1e} "
                  f"eH={mx['eH']:.1e} local={mu:.1e}  fails: eF{fails['eF']} etau{fails['etau']} eH{fails['eH']}")
    for k, v in kill_any.items():
        print(f"  {k}: {'KILLED on ' + ', '.join(v) if v else 'survives'}")
    print("\n## IDEA-206 (two-pass window): P1 local <= 1e3 u at SO degrees (w2_none); P2 eF <= u^(3/4) at SO degrees (w2_oracle)")
    for m, key, thr in (('w2_none', 'local', 1e3 * U), ('w2_oracle', 'eF', U34), ('w2_oracle', 'eH', U34)):
        bad = [(r['bench'], r['n'], r[key]) for r in sec if r['mode'] == m and r['loss'] <= SQRTU and r.get(key, 0) > thr]
        print(f"  {m} {key} > {thr:.1e}: {bad if bad else 'none'}")
    print("\n## IDEA-204 (drift under fullcgs2): pre-registered rule (box Chebyshev reference) and amendments")
    for r in [r for r in sec if r['mode'] == 'fullcgs2']:
        pre = (r.get('drift', 0) > SQRTU and r.get('ref_bound', 1) < 1e-11)
        lb = r['thetaLB'] > SQRTU
        un = (r.get('drift_unrot') is not None and r['drift_unrot'] > SQRTU and r['ref_unrot'] < 1e-11)
        if r['n'] % 4 == 0 or pre or lb or un:
            s = (f"  {r['bench']:9s} n={r['n']:2d} L={r['loss']:.1e} drift={r.get('drift', np.nan):.1e} "
                 f"(u*kappa={r.get('ref_bound', np.nan):.1e})")
            if r.get('drift_unrot') is not None:
                s += f" drift_unrot={r['drift_unrot']:.1e} (u*kappa={r['ref_unrot']:.1e})"
            s += f" thetaLB={r['thetaLB']:.1e}  pre-rule:{'KILL' if pre else '-'} LB:{'KILL' if lb else '-'} unrot:{'KILL' if un else '-'}"
            print(s)


if __name__ == '__main__':
    main(sys.argv[1])
