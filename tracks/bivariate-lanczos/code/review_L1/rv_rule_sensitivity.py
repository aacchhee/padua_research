"""Re-application of the pre-registered R01 decision rule (candidates.md, IDEA?...-101) to the developer's raw
JSON records, written independently from the rule text (not from l1_analyze_r01.py), with two sensitivity
variants: (a) u = 2^-53 (unit roundoff, as plan.md / PD-T?...-102 define u) instead of 2^-52; (b) exclusion of
the tensor-grid chain-completion degree n = 40 (the analogue of the developer's post-hoc N = M exclusion).
This is a protocol check on the developer's outputs, not a rerun.
Usage: python3 -I rv_rule_sensitivity.py ../../../../topics/bivariate-lanczos-20261031/directions/L1/logs/r01_*.raw
"""
import sys, json
from collections import defaultdict


def verdict(rows, key, u, excl):
    tau = 1e3 * u
    D = []
    for r in rows:
        if (r['run'], r['n']) in excl or r['N'] >= r['M']:
            continue
        if key not in r:
            continue
        P = u / r[key]; L = r['loss']
        if L >= tau or P >= tau:
            D.append(L / P)
    if not D:
        return 'uninf', None
    ok = all(1 / 3 <= q <= 3 for q in D)
    return ('PRED' if ok else 'fail'), (min(D), max(D))


def main(files):
    runs = defaultdict(list)
    for f in files:
        for line in open(f):
            if line.startswith('JSON '):
                r = json.loads(line[5:])
                if r['method'] in ('bj', 'hl'):
                    runs[(r['run'], r['method'])].append(r)
    for (u, ulab) in ((2.0 ** -52, 'u=2^-52 (developer)'), (2.0 ** -53, 'u=2^-53 (unit roundoff)')):
        for excl, elab in ((set(), 'no tensor exclusion'), ({('tensorcheb41', 40)}, 'tensor n=40 excluded')):
            print(f'## {ulab}; {elab}')
            zpred = []
            k1 = True
            single_fail_z_ok = []
            for (run, meth), rows in sorted(runs.items()):
                v = {o: verdict(rows, 'res_' + o, u, excl) for o in ('x', 'y', 'z')}
                if run.startswith(('random', 'tensorcheb41')) and not run.endswith(('rot0.3', 'rot1.0')):
                    print(f'   {run:24s} {meth}: X {v["x"][0]:5s} {v["x"][1]}  Y {v["y"][0]:5s} {v["y"][1]}  Z {v["z"][0]:5s} {v["z"][1]}')
                if v['z'][0] == 'PRED':
                    zpred.append((run, meth))
                    if not (v['x'][0] == 'PRED' or v['y'][0] == 'PRED'):
                        k1 = False
                if v['z'][0] in ('PRED', 'uninf') and (v['x'][0] == 'fail' or v['y'][0] == 'fail'):
                    single_fail_z_ok.append((run, meth))
            print(f'   runs where Z predicts: {zpred}')
            print(f'   K1 (operational) fires: {bool(zpred) and k1};  single section fails while Z predicts/uninformative: {single_fail_z_ok}')


if __name__ == '__main__':
    main(sys.argv[1:])
