"""Exact comparison: committed e1-full-sweep (degree 12) vs orchestrator reruns vs
auditor-independent ind_aggregate outputs; decisive inequalities from rationals."""
import json, sys, os
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
EV = '/home/claude/padua_research/topics/padua-lanczos-drift-20261101/evidence'
RUNS = '/tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/runs'
HERE = os.path.dirname(os.path.abspath(__file__))
sweep = {(r['set'], r['degree'], r['rule']): r for r in json.load(open(f'{EV}/e1-full-sweep.json'))['runs']}
KEYS = ['Knode_squared', 'KHS_squared', 'Urow_squared', 'upper_squared']
MATH = KEYS + ['source_count', 'point_count', 'basis_count', 'normal_trace_exact', 'pivot_choices', 'witness', 'sources', 'degree', 'rule', 'set']
out = {}
# 1. orchestrator reruns vs committed
for tag, (s, r) in {'audit-T24-bj': ('triangle', 'bj'), 'audit-T24-pivot': ('triangle', 'pivot'),
                    'audit-rotQ24-bj': ('rotated', 'bj'), 'audit-rotQ24-alt': ('rotated', 'alt')}.items():
    p = f'{RUNS}/{tag}.json'
    if not os.path.exists(p):
        out[tag] = 'MISSING'; continue
    a = json.load(open(p)); c = sweep[s, 12, r]
    diff = []
    for k in MATH:
        av, cv = a.get(k), c.get(k)
        if k in KEYS:
            if F(av['exact']) != F(cv['exact']) or av['sqrt_rational_interval'] != cv['sqrt_rational_interval']:
                diff.append(k)
        elif av != cv:
            diff.append(k)
    out[tag] = {'identical_math_fields': not diff, 'diff': diff, 'code_sha256': a['code_sha256'], 'python': a['python']}
# 2. independent vs committed
def cmp_ind(s, r, path):
    if not os.path.exists(path):
        return 'MISSING'
    j = json.load(open(path)); c = sweep[s, 12, r]
    res = {'choices_match': j['choices'] == ''.join(c['pivot_choices'])}
    if j['mode'] == 'exact':
        for mk, ck in [('Knode2', 'Knode_squared'), ('KHS2', 'KHS_squared'), ('Urow2', 'Urow_squared')]:
            res[mk + '_exact_equal'] = F(j[mk]) == F(c[ck]['exact'])
        res['witness_match'] = (c['witness']['source'], c['witness']['node']) == tuple(j['witness'])
    else:
        for mk, ck in [('Knode2_ball', 'Knode_squared'), ('KHS2', 'KHS_squared'), ('Urow2_ball', 'Urow_squared')]:
            lo, hi = F(j[mk]['lower']), F(j[mk]['upper'])
            v = F(c[ck]['exact'])
            res[mk + '_contains_committed'] = lo <= v <= hi
            res[mk + '_rel_width'] = float((hi - lo) / v)
        res['witness_match'] = (c['witness']['source'], c['witness']['node']) == tuple(j['witness'])
    return res
for s, r, f in [('triangle', 'bj', 'ind-T24-bj-exact.json'), ('triangle', 'pivot', 'ind-T24-pivot-exact.json'),
                ('triangle', 'alt', 'ind-T24-alt-exact.json'), ('triangle', 'mirror', 'ind-T24-mirror-exact.json'),
                ('rotated', 'bj', 'ind-rot-bj-arb.json'), ('rotated', 'alt', 'ind-rot-alt-arb.json')]:
    out[f'independent {s}/{r}'] = cmp_ind(s, r, f'{HERE}/{f}')
# 3. decisive inequalities from committed rationals
q = lambda s, r, k: F(sweep[s, 12, r][k]['exact'])
LT = q('triangle', 'bj', 'Knode_squared'); UTp = q('triangle', 'pivot', 'upper_squared'); KHSTp = q('triangle', 'pivot', 'KHS_squared')
LR = q('rotated', 'bj', 'Knode_squared'); URa = q('rotated', 'alt', 'upper_squared'); KHSRa = q('rotated', 'alt', 'KHS_squared'); UrowRa = q('rotated', 'alt', 'Urow_squared')
URp = q('rotated', 'pivot', 'upper_squared'); KHSRp = q('rotated', 'pivot', 'KHS_squared')
UTa = q('triangle', 'alt', 'upper_squared')
dec = {
 'T24 upper pivot is KHS (KHS<=Urow)': UTp == KHSTp,
 'T24 best comparator by sharp upper is pivot': UTp < UTa,
 'rot best comparator by sharp upper is alt': URa < URp,
 'rot best comparator by KHS is alt': KHSRa < KHSRp,
 'rot alt upper is Urow': URa == UrowRa,
 'T24 L_BJ^2 > 2e14': LT > 200000000000000,
 'T24 U_pivot^2 < 1.7e8': UTp < 170000000,
 'T24 2e14 > 1000^2*1.7e8': 200000000000000 > 1000**2 * 170000000,
 'T24 ratio^2 > 1126^2 (kappa ratio >1126)': LT > 1126**2 * UTp,
 'T24 ratio^2 < 1127^2': LT < 1127**2 * UTp,
 'rot L_BJ^2 > 8.8e10': LR > 88000000000,
 'rot U_alt^2 < 6.42e8': URa < 642000000,
 'rot 8.8e10 > 11^2*6.42e8': 88000000000 > 121 * 642000000,
 'rot ratio^2 > 100 (sharp)': LR > 100 * URa,
 'rot ratio^2 > 11.72^2': LR * 10000 > 117200**2 // 100 * URa if False else LR * 10000 > 1172**2 * URa,
 'rot ratio^2 < 11.73^2': LR * 10000 < 1173**2 * URa,
 'rot KHS-only ratio^2 < 100 (original INCONCLUSIVE)': LR < 100 * KHSRa,
 'rot KHS-only ratio^2 in (62.16,62.17)': F(6216, 100) * KHSRa < LR < F(6217, 100) * KHSRa,
 'rot sharp ratio^2 in (137.36,137.37)': F(13736, 100) * URa < LR < F(13737, 100) * URa,
 'T24 ratio^2 in (1269287,1269288)': 1269287 * UTp < LT < 1269288 * UTp,
}
out['decisive_from_committed_rationals'] = dec
print(json.dumps(out, indent=1))
