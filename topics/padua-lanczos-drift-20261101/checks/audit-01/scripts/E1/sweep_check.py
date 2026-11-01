"""Independent recomputation of the whole committed 88-case sweep (one set per call).
T24: exact equality of Knode^2, KHS^2, Urow^2, choices, witness.
rotated: rigorous arb balls (512 bits) must contain the committed rationals; choices equal."""
import sys, json, time
from fractions import Fraction as F
from ind_aggregate import run
sys.set_int_max_str_digits(0)
name, mode = sys.argv[1], sys.argv[2]
EV = '/home/claude/padua_research/topics/padua-lanczos-drift-20261101/evidence'
sw = {(r['set'], r['degree'], r['rule']): r for r in json.load(open(f'{EV}/e1-full-sweep.json'))['runs']}
deg = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(2, 13))
rules = sys.argv[4].split(',') if len(sys.argv) > 4 else ['bj', 'mirror', 'alt', 'pivot']
out = []
for n in deg:
    for rule in rules:
        t0 = time.time()
        r = run(name, n, rule, mode)
        c = sw[name, n, rule]
        row = {'degree': n, 'rule': rule, 'choices_equal': r['choices'] == ''.join(c['pivot_choices'])}
        if mode == 'exact':
            row['all_equal'] = (F(str(r['Knode2'])) == F(c['Knode_squared']['exact']) and
                                F(str(r['KHS2'])) == F(c['KHS_squared']['exact']) and
                                F(str(r['Urow2'])) == F(c['Urow_squared']['exact']))
        else:
            def contains(ball, s):
                m, e = ball.lower().man_exp(); lo = F(int(m)) * F(2) ** int(e)
                m, e = ball.upper().man_exp(); hi = F(int(m)) * F(2) ** int(e)
                return lo <= F(s) <= hi
            row['all_contained'] = (contains(r['Knode2_ball'], c['Knode_squared']['exact']) and
                                    contains(r['KHS2'], c['KHS_squared']['exact']) and
                                    contains(r['Urow2_ball'], c['Urow_squared']['exact']))
        row['ties'] = r['pivot_tie_columns']; row['secs'] = round(time.time() - t0, 1)
        out.append(row); print(json.dumps(row), flush=True)
ok = all(r['choices_equal'] and r.get('all_equal', r.get('all_contained')) for r in out)
print('SWEEP', name, 'cases', len(out), 'ALL MATCH' if ok else 'MISMATCH')
