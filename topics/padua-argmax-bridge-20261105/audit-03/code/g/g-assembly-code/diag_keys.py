import json, sys
from fractions import Fraction as Fr
from flint import arb, fmpq, ctx
import direct_sum_validate as D, phase_rational_indep as PRI
ctx.prec = 300
for path in sys.argv[1:]:
    d = json.load(open(path)); n = int(d['n'])
    for a, b, h in d['S_upper_rows']:
        val = D.S_direct(n, Fr(a), Fr(b)); nat = PRI.hexfr(h)
        natb = arb(fmpq(nat.numerator, nat.denominator))
        if not (natb >= val):
            print(path.split('/')[-1], n, (a, b), 'native', float(nat), 'direct', val, 'native-direct.mid', float(nat) - float(val.mid()))
