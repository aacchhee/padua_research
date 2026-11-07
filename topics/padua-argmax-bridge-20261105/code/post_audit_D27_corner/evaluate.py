"""D27: sole frozen N1024 scalar gate for the wider analytic corner square."""
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
out = Path(__file__).with_name('budget-1024.json')
assert not out.exists(), 'One-shot receipt exists; no retry authorized'
base = Path(__file__).resolve().parents[2]
dep = base/'code/post_audit_D06_model_budget/evaluate.py'
raw = dep.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413'
wanted = {'directed', 'I', 'ilog', 'atan_bounds'}
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
n = 1024; m = n+1; one = I(1); half = one/2; p2 = pi*pi
L = log(n); H = 1+L; b = 4/p2; hr = log(one*5/2)+one/18
Dc04 = ((52/p2)*H+7)/n+10*one/(n*n)+20*H/(pi*n*n)
KD = (352*H/(3*pi)+2/pi)/n
MA = 1/pi+4/p2
g = 1+log(2+8*one*m/(3*pi))
VB = 23+(3*g+14*log(m)+46+2*log(2))/pi
Qg = (4*one/m)*(7+(2/pi)*(5+2*log(2*m)))
Gg = (2*L*MA+VB)/(2*m)+6*L*MA/m+Qg+4*log(pi)/(pi*m)+16*one/m
endpoint_rows = (181+19*L)/n+21600*one/(n*n)
central_rows = (12+2*L)/n
E6 = endpoint_rows+central_rows
mesh = b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2)
W = (3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
Cnew = Dc04+Gg+E6+mesh+W
G0 = ((28/p2)*L+one*111/2+23/pi)/m
E0 = Dc04+G0+mesh+14*one/n+71*one/(n*n)
T = (4*L*L-3*L)/p2
q = one/7; Paxis = one*5/7; Dc = one*6211/7260
rq = Q(22,7)**4/6144
r = one*rq.numerator/rq.denominator
U = p2/32
Mmodel = (4*L*L+(one*79/5)*L)/p2+one*8/3
Mnew = Mmodel+Cnew+2*KD
axis_allowance = Cnew+Paxis*KD
diagonal_allowance = Cnew+2*Paxis*KD
delta = q*T-Dc-axis_allowance-E0
diagonal_lower = 2*q*T-Dc-diagonal_allowance-E0
criterion = p2*p2/6144
F = delta-r*Mnew
radial = 16*F/p2
controls = {'axis_sqrt': 2 > Q(7,5)**2,
            'axis_u': (1-Q(5,7))/2 == Q(1,7),
            'constant_gap': Q(8,3)-Q(4383,2420) == Q(6211,7260),
            'square_normalization': 6*32**2 == 6144,
            'r_upper': rq < Q(1,60),
            'leading_positive': Q(1,7)-rq > 0,
            'derivative_positive': Q(5,7)-Q(119,5)*rq > 0,
            'derivative_bound': Q(5,7)-Q(119,300) == Q(667,2100),
            'diagonal_charge': 2*Q(5,7) == Q(10,7),
            'pi_criterion': r.a > criterion.b}
vals = {'L': L, 'H': H, 'b': b, 'hr': hr, 'D04_constant': Dc04,
        'KD': KD, 'MA': MA, 'g': g, 'VB': VB, 'Qg': Qg, 'Gg': Gg,
        'endpoint_rows': endpoint_rows, 'central_rows': central_rows,
        'E6': E6, 'mesh': mesh, 'W': W, 'Cnew': Cnew, 'G0': G0,
        'E0': E0, 'T': T, 'q': q, 'Paxis_upper': Paxis,
        'constant_gap': Dc, 'r': r, 'U': U, 'Mmodel': Mmodel,
        'Mnew': Mnew, 'axis_allowance': axis_allowance,
        'diagonal_allowance': diagonal_allowance, 'delta': delta,
        'diagonal_lower': diagonal_lower, 'criterion': criterion,
        'F': F, 'radial_coefficient': radial}
usage = resource.getrusage(resource.RUSAGE_SELF)
result = {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
          'controls': controls, 'values': {k: [str(v.a), str(v.b)] for k, v in vals.items()},
          'passed': all(controls.values()) and Mnew.a > 0 and T.a > 0 and F.a > 0,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'dependency_sha256': hashlib.sha256(raw).hexdigest(),
          'pi_interval': [str(pi.a), str(pi.b)],
          'cpu_seconds_before_receipt': usage.ru_utime+usage.ru_stime,
          'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
with out.open('x') as handle:
    handle.write(json.dumps(result, sort_keys=True, indent=2)+'\n')
print(json.dumps(result, sort_keys=True))
