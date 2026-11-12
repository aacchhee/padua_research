import json, subprocess, sys, copy
from fractions import Fraction as Fr
import math
SP = sys.argv[1]
cert = json.load(open(sys.argv[2]))
V = SP + '/a5-D3/verifier/audit5_d3_verify.py'
PY = SP + '/venv/bin/python'
def run(name, c):
    p = SP + '/a5-D3/mut/' + name + '.json'
    json.dump(c, open(p, 'w'))
    r = subprocess.run([PY, '-I', V, p, p + '.out'], capture_output=True, text=True)
    last = (r.stdout.strip().splitlines() or [''])[-1] if r.returncode == 0 else r.stderr.strip().splitlines()[-1]
    print(name, 'exit', r.returncode, last[:90])
m = copy.deepcopy(cert); m['center_numerators'][60] = str(int(m['center_numerators'][60]) + 2**160); run('M1_weight_plus_2^-20', m)
m = copy.deepcopy(cert); m['center_numerators'][6] = str(2**180 - 2**79); run('M2_active_coord_near_1', m)
m = copy.deepcopy(cert); m['center_numerators'][60] = '0'; run('M3_weight_zero', m)
m = copy.deepcopy(cert); m['center_numerators'][3:6] = m['center_numerators'][0:3]; run('M4_duplicate_node', m)
m = copy.deepcopy(cert); m['active'] = m['active'][:-1] + [m['active'][-2]]; run('M5_repeat_active', m)
m = copy.deepcopy(cert); m['radius_bits'] = 99; run('M6_radius', m)
# nonlattice predicate controls on lattice-type rational cosines (Niven values)
def passes(a, b):
    d = (1-a*a)*(1-b*b)
    sq = math.isqrt(d.numerator)**2 == d.numerator and math.isqrt(d.denominator)**2 == d.denominator
    return d > 0 and not sq and (4*a*b).denominator != 1
vals = [Fr(0), Fr(1,2), Fr(-1,2)]
print('Niven-value pairs passing predicate (expect 0):', sum(passes(a,b) for a in vals for b in vals))
