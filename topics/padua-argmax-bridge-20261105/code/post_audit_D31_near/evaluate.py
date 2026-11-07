"""D31: sole frozen N2048 exact-radical near-budget calculation."""
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
out = Path(__file__).with_name('budget-2048.json')
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
def psi(B, q, k):
    discriminant = 9*B*B+32*q*k
    z = (3*B+sqrt_interval(discriminant))/(8*q)
    fractional = B*z*z*z/4
    linear = k*z*z/2
    return discriminant, z, fractional, linear, fractional+linear
al, au = atan(5, 70); bl, bu = atan(239, 20)
pl, pu = 16*al-4*bu, 16*au-4*bl
pi = I(directed(lambda: D(pl.numerator)/D(pl.denominator), ROUND_FLOOR),
       directed(lambda: D(pu.numerator)/D(pu.denominator), ROUND_CEILING))
n = 2048; m = n+1; one = I(1); half = one/2; p2 = pi*pi
L = log(n); H = 1+L; b = 4/p2; hr = log(one*5/2)+one/18
D04 = ((52/p2)*H+7)/n+10*one/(n*n)+20*H/(pi*n*n)
G0 = ((28/p2)*L+one*111/2+23/pi)/m
mesh = b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2)
E0 = D04+G0+mesh+14*one/n+71*one/(n*n)
Cnear = 22*one/n+162*one/(n*n)+40*H/(pi*n*n)
Kstar = ((112/pi+2)*H+2*L+one*61/3)/n+4*one/(n*n)
Kout = ((one*35/2)*L+75)/n
Knear = Kstar+Kout
T = (4*L*L-3*L)/p2
V = T-E0
qx = (one*47/192)*V-one*89/72
qy = (one*47/192)*V-one*23/24
Bx = one*77/96; By = one/12
target = one/32-one/10000
controls = {'physical_floor_domain': n >= 160,
            'target_budget': Q(1,32)-Q(1,10000) == Q(623,20000),
            'cosine_coefficient': Q(1,4)-Q(1,192) == Q(47,192),
            'alpha_quadratic': Q(19,24)+Q(4,9) == Q(89,72),
            'beta_quadratic': Q(19,24)+Q(1,6) == Q(23,24),
            'alpha_fractional': Q(15,32)+Q(1,3) == Q(77,96),
            'beta_fractional': Q(1,9)*Q(3,4) == Q(1,12),
            'K_log': 2+Q(35,2) == Q(39,2),
            'K_constant': Q(61,3)+75 == Q(286,3),
            'C_inverse': 4+18 == 22,
            'C_inverse_square': 20+142 == 162,
            'D_coarse': Q(59,n)+Q(70,n*n) < Q(1,20),
            'G0_coarse': Q(1585,18*m) < Q(1,20),
            'mesh_coarse': Q(19,2*n)+Q(14,n*n) < Q(1,100),
            'origin_rows_coarse': Q(15,n) < Q(1,100),
            'qx_domain_lower': Q(3229,1152) > 2,
            'qy_domain_lower': Q(1183,384) > 2}
vals = {'L': L, 'H': H, 'b': b, 'hr': hr, 'D04': D04, 'G0': G0,
        'mesh': mesh, 'E0': E0, 'Cnear': Cnear, 'Kstar': Kstar,
        'Kout': Kout, 'Knear': Knear, 'T': T, 'V': V,
        'qx': qx, 'qy': qy, 'Bx': Bx, 'By': By, 'target_budget': target}
domain = V.a > 0 and qx.a > 0 and qy.a > 0 and Knear.a >= 0
gate = None
if domain:
    px = psi(Bx, qx, Knear)
    py = psi(By, qy, Knear)
    names = ['discriminant', 'z', 'fractional', 'linear', 'Psi']
    vals.update({'alpha_'+key: value for key, value in zip(names, px)})
    vals.update({'beta_'+key: value for key, value in zip(names, py)})
    total = Cnear+px[-1]+py[-1]
    gate = target-total
    vals.update({'total_near_charge': total, 'near_gate': gate})
first_failure = ('exact_controls' if not all(controls.values()) else
                 'quadratic_domain' if not domain else
                 'near_gate_not_positive' if gate.a <= 0 else None)
usage = resource.getrusage(resource.RUSAGE_SELF)
result = {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
          'controls': controls, 'quadratic_domain': domain,
          'values': {key: [str(value.a), str(value.b)] for key, value in vals.items()},
          'passed': first_failure is None, 'first_failure': first_failure,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'dependency_sha256': hashlib.sha256(raw).hexdigest(),
          'pi_interval': [str(pi.a), str(pi.b)],
          'cpu_seconds_before_receipt': usage.ru_utime+usage.ru_stime,
          'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
with out.open('x') as handle:
    handle.write(json.dumps(result, sort_keys=True, indent=2)+'\n')
print(json.dumps(result, sort_keys=True))
