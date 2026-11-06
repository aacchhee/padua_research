"""Independent signed-OLS slope interval from compact integer/scale log tables (exact Fractions)."""
import json, sys
from fractions import Fraction as F
from itertools import product
RULES = ('bj', 'mirror', 'alt', 'pivot')
def run(path):
    t = json.load(open(path)); sc = t['scale']
    assert t['columns'] == ['degree', 'rule', 'logL_lower', 'logL_upper', 'logU_lower', 'logU_upper']
    tab = {}
    for d, r, a, b, c, e in t['rows']:
        assert (d, r) not in tab and a <= b and c <= e and a <= e  # L<=U consistency of outward bounds
        tab[d, r] = (F(a, sc), F(b, sc), F(c, sc), F(e, sc))
    degs = sorted({d for d, _ in tab})
    assert all((d, r) in tab for d in degs for r in RULES), 'missing row'
    y = {}
    for d in degs:
        lo = tab[d, 'bj'][0] - min(tab[d, r][3] for r in RULES)
        hi = tab[d, 'bj'][3] - min(tab[d, r][0] for r in RULES)
        y[d] = (lo, hi)
    out = {'table': path, 'degrees': [degs[0], degs[-1]], 'rows': len(t['rows'])}
    wins = []
    for w in ((8, 12), (12, 16)):
        ds = list(range(w[0], w[1] + 1)); m = F(sum(ds), len(ds)); sxx = sum((d - m) ** 2 for d in ds)
        c = {d: (d - m) / sxx for d in ds}
        lo = sum(c[d] * (y[d][0] if c[d] > 0 else y[d][1]) for d in ds)
        hi = sum(c[d] * (y[d][1] if c[d] > 0 else y[d][0]) for d in ds)
        # brute-force all 32 corners as cross-check
        vals = [sum(c[d] * y[d][k] for d, k in zip(ds, ks)) for ks in product((0, 1), repeat=len(ds))]
        assert min(vals) == lo and max(vals) == hi
        verdict = 'PASS-side' if lo > F(1, 10) else ('KILL-side' if hi < F(2, 100) else 'neither')
        wins.append({'window': w, 'lower': lo, 'upper': hi, 'lower_f': float(lo), 'upper_f': float(hi), 'side': verdict})
    out['windows'] = wins
    sides = [x['side'] for x in wins]
    out['verdict'] = 'PASS' if all(s == 'PASS-side' for s in sides) else ('KILL/redirect' if all(s == 'KILL-side' for s in sides) else 'INCONCLUSIVE')
    # whole-window 8..16 slope (handoff 01 wording) as supplementary
    ds = list(range(8, 17)); m = F(sum(ds), len(ds)); sxx = sum((d - m) ** 2 for d in ds)
    c = {d: (d - m) / sxx for d in ds}
    out['full_8_16'] = (float(sum(c[d] * (y[d][0] if c[d] > 0 else y[d][1]) for d in ds)), float(sum(c[d] * (y[d][1] if c[d] > 0 else y[d][0]) for d in ds)))
    out['y'] = {d: (float(y[d][0]), float(y[d][1])) for d in range(8, 17)}
    out['y_exact'] = {d: (y[d][0], y[d][1]) for d in range(8, 17)}
    return out
if __name__ == '__main__':
    for p in sys.argv[1:]:
        o = run(p)
        print('==', p.split('/')[-1], o['rows'], 'rows, degrees', o['degrees'])
        for w in o['windows']:
            print('  ', w['window'], 'lower', w['lower'], '=', w['lower_f'], '; upper', w['upper'], '=', w['upper_f'], w['side'])
        print('   verdict', o['verdict'], '; full 8-16 slope interval', o['full_8_16'])
        print('   y intervals', {d: tuple(round(v, 4) for v in iv) for d, iv in o['y'].items()})
