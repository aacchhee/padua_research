import json, sys
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
runs = json.load(open('/home/claude/padua_research/topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json'))['runs']
R = {(r['set'], r['degree'], r['rule']): r for r in runs}
def q(r, k): return F(r[k]['exact'])
out = []
for s in ['triangle', 'rotated']:
    for n in range(2, 13):
        b = R[s, n, 'bj']; goods = [R[s, n, 'alt'], R[s, n, 'pivot']]
        KHSb = q(b, 'KHS_squared'); Ub = q(b, 'upper_squared'); Lb = q(b, 'Knode_squared')
        c1 = any(KHSb <= q(g, 'Knode_squared') for g in goods)
        c2 = all(KHSb < 100 * q(g, 'Knode_squared') for g in goods)
        c2sharp = all(Ub < 100 * q(g, 'Knode_squared') for g in goods)
        surv_orig = Lb > 100 * min(q(g, 'KHS_squared') for g in goods)
        surv_sharp = Lb > 100 * min(q(g, 'upper_squared') for g in goods)
        out.append((s, n, 'origDEAD' if (c1 or c2) else '-', 'c1' if c1 else '', 'c2' if c2 else '', 'c2sharp' if c2sharp else '', 'SURV_orig' if surv_orig else '', 'SURV_sharp' if surv_sharp else ''))
for o in out: print(*o)
