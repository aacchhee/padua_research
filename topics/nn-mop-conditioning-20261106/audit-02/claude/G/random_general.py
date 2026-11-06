import sys, os, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import gauge_exact as G
random.seed(20261106)
R = G.Num('fr')
summary = []
for trial in range(12):
    N = random.choice([3, 4, 5])
    M = N - 1
    xs = sorted(set(Fr(random.randint(-60, 60), 60) for _ in range(4 * N)))
    xs = sorted(random.sample(xs, N))
    w = [[Fr(random.randint(1, 40), random.randint(1, 9)) for _ in range(N)] for _ in range(2)]
    G.inputs = lambda fam, MM, xs=xs, w=w: (xs, w)
    try:
        res = G.analyse('random', N, R)
    except ZeroDivisionError:
        summary.append((trial, N, 'non-normal'))
        continue
    for c in res['cases']:
        # formula (2) must hold at all tested t; attainment iff dominance
        assert c['formula2_ok'], (trial, c['model'])
        if c['dominance']:
            assert c['attain_equal'], (trial, c['model'])
    summary.append((trial, N, [(c['model'][:4], c['fixed_mass'], c['dominance'], c['attain_equal'], '%.3g' % float(c['K']), ['%.3g' % float(x) for x in c['r']]) for c in res['cases'] if c['model'] in ('mixed',)]))
for s in summary: print(s)
