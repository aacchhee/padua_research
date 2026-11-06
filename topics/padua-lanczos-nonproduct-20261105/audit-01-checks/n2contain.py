import json, sys
from fractions import Fraction as F
sys.path.insert(0, sys.argv[1]); from n2 import run
E = sys.argv[2]
for fam in ('H24_222', 'D36x9'):
    mine = run(f'{E}/p6-log-endpoints-{fam}.json')
    rec = json.load(open(f'{E}/p6-n2-{fam}.json'))
    comp = json.load(open(f'{E}/p6-compact-n2-{fam}.json'))
    chk = json.load(open(f'{E}/check-scans-compact-{fam}.json'))
    for w, r, c, ch in zip(mine['windows'], rec['windows'], comp['windows'], chk['windows_outward']):
        lo, hi = w['lower'], w['upper']
        print(fam, w['window'], 'compact exact equal:', F(c['lower_exact']) == lo and F(c['upper_exact']) == hi,
              '| 128-bit primary inside mine:', lo <= F(r['lower_exact']) and F(r['upper_exact']) <= hi,
              '| 128-bit checker inside:', lo <= F(r['checker_lower_exact']) and F(r['checker_upper_exact']) <= hi,
              '| astra outward contains mine:', F(ch[0]) <= lo and hi <= F(ch[1]),
              '| width diff primary', float(F(r['lower_exact']) - lo), float(hi - F(r['upper_exact'])))
    # logratio per-degree containment: receipts' 128-bit logratio intervals inside compact-derived ones
    ok = all(mine['y_exact'][int(d)][0] <= F(v[0]) and F(v[1]) <= mine['y_exact'][int(d)][1] for d, v in rec['logratio_outward'].items())
    print(fam, 'per-degree 128-bit logratio intervals inside compact-derived:', ok, sorted(map(int, rec['logratio_outward'])))
