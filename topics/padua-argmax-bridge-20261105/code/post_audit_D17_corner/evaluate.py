"""D17: sole frozen N4096 analytic actual-corner scalar budget."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (4, 5))
import ast
import hashlib
import json
import sys
import time
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from pathlib import Path

assert sys.argv[1:] == ['--run-once']
out = Path(__file__).with_name('budget-4096.json')
assert not out.exists(), 'One-shot receipt exists; no retry authorized'
base = Path(__file__).resolve().parents[2]
dep = base/'code/post_audit_D06_model_budget/evaluate.py'
raw = dep.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413'
wanted = {'directed', 'I', 'ilog', 'imax', 'atan_bounds', 'components'}
defs = [x for x in ast.parse(raw).body if isinstance(x, (ast.FunctionDef, ast.ClassDef)) and x.name in wanted]
assert {x.name for x in defs} == wanted
env = {'D': D, 'localcontext': localcontext, 'ROUND_FLOOR': ROUND_FLOOR,
       'ROUND_CEILING': ROUND_CEILING, 'Q': Q, 'PREC': 50}
exec(compile(ast.Module(body=defs, type_ignores=[]), str(dep), 'exec'), env)
I = env['I']; log = env['ilog']; directed = env['directed']; atan = env['atan_bounds']
al, au = atan(5, 70); bl, bu = atan(239, 20)
pl, pu = 16*al-4*bu, 16*au-4*bl
pi = I(directed(lambda: D(pl.numerator)/D(pl.denominator), ROUND_FLOOR),
       directed(lambda: D(pu.numerator)/D(pu.denominator), ROUND_CEILING))
q_exact = Q(15, 224); d_exact = Q(6211, 7260)
r_exact = Q(22, 7)**4/31104
checks = {'sqrt3': Q(97,56)**2 > 3,
          'axis_loss': (2-Q(97,56))/4 == q_exact,
          'constant_difference': Q(8,3)-Q(4383,2420) == d_exact,
          'pi_square': Q(22,7)**2 < 10,
          'r_small': r_exact < Q(1,300), 'q_lower': q_exact > Q(1,16),
          'quadratic_coefficient': q_exact-r_exact > 0,
          'derivative_at_one': 5*q_exact-Q(119,5)*r_exact > 0,
          'scaled_denominator': 6*72**2 == 31104}
def rational_interval(value):
    return I(value.numerator)/value.denominator
n = 4096; m = n+1; one = I(1); half = one/2
L = log(n); H = 1+L; b = 4/(pi*pi); hr = log(one*5/2)+one/18
origin_D = ((52/(pi*pi))*H+7)/n+10*one/(n*n)+20*H/(pi*n*n)
origin_G = ((28/(pi*pi))*L+one*111/2+23/pi)/m
origin_mesh = b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2)
origin_rows = 14*one/n+71*one/(n*n)
E0 = origin_D+origin_G+origin_mesh+origin_rows
parts = env['components'](n, one, one, one*2, one, one*8, H, pi, log, env['imax'])
UF = parts[-1]
q0 = rational_interval(q_exact); d0 = rational_interval(d_exact); r = rational_interval(r_exact)
T = (4*L*L-3*L)/(pi*pi)
M = (4*L*L+(one*79/5)*L)/(pi*pi)+one*8/3+UF
charge = d0+UF+E0
delta = q0*T-charge
diagonal_loss = 2*q0*T-charge
F = delta-r*M
U = pi*pi/72
radial_coefficient = 36*F/(pi*pi)
vals = {'L': L, 'q0': q0, 'd0': d0, 'r': r, 'T': T, 'U': U,
        'origin_D': origin_D, 'origin_G': origin_G, 'origin_mesh': origin_mesh,
        'origin_rows': origin_rows, 'E0': E0, 'M': M, 'Q': charge,
        'axis_loss_delta': delta, 'diagonal_loss': diagonal_loss,
        'barrier_cost': r*M, 'F': F, 'radial_coefficient': radial_coefficient}
names = ['ED04', 'mesh', 'rows', 'collision', 'e4', 'I_n', 'Dpole',
         'TZ_bv', 'TZ_initial', 'TZ_upper', 'TZ_holes', 'TZ', 'UF']
vals.update({'far_'+k: v for k, v in zip(names, parts)})
usage = resource.getrusage(resource.RUSAGE_SELF)
result = {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
          'checks': checks, 'values': {k: [str(v.a), str(v.b)] for k, v in vals.items()},
          'passed': all(checks.values()) and T.a > 0 and F.a > 0,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'dependency_sha256': hashlib.sha256(raw).hexdigest(),
          'pi_interval': [str(pi.a), str(pi.b)],
          'cpu_seconds_before_receipt': usage.ru_utime+usage.ru_stime,
          'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
with out.open('x') as handle:
    handle.write(json.dumps(result, sort_keys=True, indent=2)+'\n')
print(json.dumps(result, sort_keys=True))
