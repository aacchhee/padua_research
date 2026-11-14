"""D20: sole frozen N7000 scalar gate for the new global hybrid telescope."""
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
out = Path(__file__).with_name('budget-7000.json')
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
def sqrt_interval(value):
    value = I.cast(value)
    assert value.a >= 0
    with localcontext() as ctx:
        ctx.prec = 50
        low = value.a.sqrt().next_minus()
        high = value.b.sqrt().next_plus()
    return I(low, high)
al, au = atan(5, 70); bl, bu = atan(239, 20)
pl, pu = 16*al-4*bu, 16*au-4*bl
pi = I(directed(lambda: D(pl.numerator)/D(pl.denominator), ROUND_FLOOR),
       directed(lambda: D(pu.numerator)/D(pu.denominator), ROUND_CEILING))
n = 7000; m = n+1; one = I(1); half = one/2
L = log(n); H = 1+L; b = 4/(pi*pi); hr = log(one*5/2)+one/18
Dc = ((52/(pi*pi))*H+7)/n+10*one/(n*n)+20*H/(pi*n*n)
KD = (352*H/(3*pi)+2/pi)/n
MA = 1/pi+4/(pi*pi)
g = 1+log(2+8*one*m/(3*pi))
VB = 23+(3*g+14*log(m)+46+2*log(2))/pi
Qg = (4*one/m)*(7+(2/pi)*(5+2*log(2*m)))
Gg = (2*L*MA+VB)/(2*m)+6*L*MA/m+Qg+4*log(pi)/(pi*m)+16*one/m
endpoint_rows = (181+19*L)/n+21600*one/(n*n)
central_rows = (12+2*L)/n
E6 = endpoint_rows+central_rows
mesh = b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2)
W = (3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
Cnew = Dc+Gg+E6+mesh+W
G0 = ((28/(pi*pi))*L+one*111/2+23/pi)/m
E0 = Dc+G0+mesh+14*one/n+71*one/(n*n)
T = (4*L*L-3*L)/(pi*pi)
u0 = one*191/6144
s0 = sqrt_interval(one*191/768)
phase_charge = KD*s0
far_allowance = Cnew+phase_charge
far_margin = u0*(T-22)
far_gate = far_margin-far_allowance-E0
controls = {'log_domain': 3**8 < n,
            'T_lower': Q(116,5) > 22,
            'endpoint_constant': 4+3*59 == 181,
            'endpoint_log': 1+3*6 == 19,
            'endpoint_inverse_square': 3*200*4*9 == 21600,
            'six_row_constant': 181+12 == 193,
            'six_row_log': 19+2 == 21,
            'central_sine': 1-Q(10,8*33*33) > Q(99,100),
            'central_V': Q(400,99) < Q(9,2),
            'origin_D0': Q(8,3)+Q(1,2)*Q(6,5) < 4,
            'origin_Z': 4+Q(1,2*32) < 5}
vals = {'L': L, 'H': H, 'b': b, 'hr': hr, 'D': Dc, 'KD': KD,
        'MA': MA, 'g': g, 'VB': VB, 'Qg': Qg, 'Gg': Gg,
        'endpoint_rows': endpoint_rows, 'central_rows': central_rows,
        'E6': E6, 'mesh': mesh, 'W': W, 'Cnew': Cnew,
        'G0': G0, 'E0': E0, 'T': T, 'u0': u0, 's0': s0,
        'phase_charge': phase_charge, 'far_allowance': far_allowance,
        'far_margin': far_margin, 'far_gate': far_gate}
usage = resource.getrusage(resource.RUSAGE_SELF)
result = {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
          'controls': controls, 'values': {k: [str(v.a), str(v.b)] for k, v in vals.items()},
          'passed': all(controls.values()) and T.a > 22 and far_gate.a > 0,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'dependency_sha256': hashlib.sha256(raw).hexdigest(),
          'pi_interval': [str(pi.a), str(pi.b)],
          'cpu_seconds_before_receipt': usage.ru_utime+usage.ru_stime,
          'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
with out.open('x') as handle:
    handle.write(json.dumps(result, sort_keys=True, indent=2)+'\n')
print(json.dumps(result, sort_keys=True))
