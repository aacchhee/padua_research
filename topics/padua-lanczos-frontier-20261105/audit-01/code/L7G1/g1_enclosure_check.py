import sys, json; sys.path.insert(0, sys.argv[1]); sys.set_int_max_str_digits(0)
from flint import fmpq, arb, ctx
ctx.prec = 600
rep = json.load(open(sys.argv[2]))['grids']['triangle']
def Fq(s):
    a, b = (s.split('/') + ['1'])[:2]; return fmpq(int(a), int(b))
def inside(iv, x): return bool(x > arb(Fq(iv[0]))) and bool(x < arb(Fq(iv[1])))
ok = bad = 0
for rec, lo, hi in zip(rep['ratio_recipes'], rep['log_endpoint_enclosures']['lower'], rep['log_endpoint_enclosures']['upper']):
    for q, iv in ((rec['lower_q'], lo), (rec['upper_q'], hi)):
        v = arb(Fq(q)).log()/2
        if inside(iv, v): ok += 1
        else: bad += 1; print('NOT INSIDE', rec['degree'], iv)
print('log endpoint enclosures containing rigorous arb (1/2)log q:', ok, 'failures', bad)
# rule-curve fits: recompute from rows
import pathlib
DEG = list(range(2, 21)); cnt = [0, 0]
for r in ['bj', 'mirror', 'alt', 'pivot']:
    rows = json.load(open(pathlib.Path(sys.argv[3])/f'full-{r}'/'endpoints.json'))['runs']
    L = [arb(Fq(x['Knode_squared']['exact'])).log()/2 for x in rows]; U = [arb(Fq(x['upper_squared']['exact'])).log()/2 for x in rows]
    M = [(a+b)/2 for a, b in zip(L, U)]
    for kind in ['E', 'P']:
        xs = [arb(d) if kind == 'E' else arb(d+1).log() for d in DEG]
        for name, ys in (('lower', L), ('upper', U), ('midpoint', M)):
            xb = sum(xs, arb(0))/19; yb = sum(ys, arb(0))/19; D = sum(((x-xb)**2 for x in xs), arb(0))
            sl = sum(((x-xb)*y for x, y in zip(xs, ys)), arb(0))/D; ic = yb - sl*xb
            f = rep['rule_descriptive_fits'][r][name][kind]
            for iv, v in ((f['slope'], sl), (f['intercept'], ic)):
                cnt[0 if inside(iv, v) else 1] += 1
print('rule-curve OLS slope/intercept intervals containing my arb values:', cnt[0], 'failures', cnt[1])
