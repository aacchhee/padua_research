"""Independent one-shot D31 N2048 scalar verification; see frozen SPEC."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (9, 10))
import ast
import hashlib
import json
import math
import platform
import sys
import time
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path

assert sys.argv[1:] == ['--run-once'] and not sys.flags.optimize
base = Path(__file__).resolve().parents[2]
outdir = base/'evidence/post_audit_D31_review'
outdir.mkdir(parents=True, exist_ok=True)
start = outdir/'identities.json'; out = outdir/'scalars.json'
assert not start.exists() and not out.exists(), 'No retry or overwrite authorized'
freeze = json.loads(Path(__file__).with_name('PREEXEC.json').read_text())
assert freeze['N'] == 2048 and freeze['cpu_cap_seconds'] == 10
identities = {}
for rel, expected in freeze['inputs'].items():
    data = (base/rel).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    assert actual == expected, rel
    identities[rel] = {'sha256': actual, 'bytes': len(data)}
author_raw = (base/'code/post_audit_D31_near/budget-2048.json').read_bytes()
author = json.loads(author_raw)
assert type(author['N']) is int and author['N'] == 2048
assert author['passed'] is True and author['quadratic_domain'] is True and author['first_failure'] is None
keys = set('L H b hr D04 G0 mesh E0 Cnear Kstar Kout Knear T V qx qy Bx By target_budget alpha_discriminant alpha_z alpha_fractional alpha_linear alpha_Psi beta_discriminant beta_z beta_fractional beta_linear beta_Psi total_near_charge near_gate'.split())
assert set(author['values']) == keys
assert all(type(v) is list and len(v) == 2 and all(type(x) is str for x in v) for v in author['values'].values())
identity_receipt = {'N': 2048, 'inputs': identities,
                    'prerelease_report_sha256': '51b572c3ae02adc40efc1acea745848daaa98fcb2583e78ad6e596b1b3ae3ff3',
                    'interval_keys': sorted(keys), 'interval_count': len(keys),
                    'cpu_cap_seconds': 10, 'checked_before_scalar_arithmetic': True}
identity_text = json.dumps(identity_receipt, sort_keys=True, indent=2)+'\n'
with start.open('x') as handle:
    handle.write(identity_text)
dep = base/'code/post_audit_D08_review/check.py'
raw = dep.read_bytes()
names = {'rounded', 'Box', 'atanh_log', 'scalar_log', 'log', 'atan_recip'}
selected = [x for x in ast.parse(raw).body if isinstance(x, (ast.FunctionDef, ast.ClassDef)) and x.name in names]
assert len(selected) == len(names) and {x.name for x in selected} == names
ns = dict(D=D, F=F, localcontext=localcontext, ROUND_FLOOR=ROUND_FLOOR,
          ROUND_CEILING=ROUND_CEILING, PREC=70)
exec(compile(ast.Module(body=selected, type_ignores=[]), str(dep), 'exec'), ns)
Box = ns['Box']; rounded = ns['rounded']; log = ns['log']
ns['LOG2'] = ns['atanh_log'](Box(2))

def rational_box(lo, hi=None):
    hi = lo if hi is None else hi
    return Box(rounded(lambda: D(lo.numerator)/D(lo.denominator), ROUND_FLOOR),
               rounded(lambda: D(hi.numerator)/D(hi.denominator), ROUND_CEILING))

sqrt_records = {}
def integer_sqrt_box(value, label):
    assert value.lo >= 0
    scale = 10**80
    low = F(value.lo); high = F(value.hi)
    rl = math.isqrt(low.numerator*scale*scale//low.denominator)
    rh = math.isqrt(high.numerator*scale*scale//high.denominator)
    low_ok = rl*rl*low.denominator <= low.numerator*scale*scale < (rl+1)*(rl+1)*low.denominator
    high_ok = rh*rh*high.denominator <= high.numerator*scale*scale < (rh+1)*(rh+1)*high.denominator
    assert low_ok and high_ok
    sqrt_records[label] = {'scale': str(scale), 'lower_integer': str(rl),
                           'upper_integer': str(rh+1), 'lower_verified': low_ok,
                           'upper_verified': high_ok}
    return rational_box(F(rl, scale), F(rh+1, scale))

al, au = ns['atan_recip'](5, 70); bl, bu = ns['atan_recip'](239, 20)
pi = rational_box(16*al-4*bu, 16*au-4*bl)
n = 2048; m = n+1; one = Box(1); p2 = pi**2
L = log(n); H = L+1; b = 4/p2
v = {'L': L, 'H': H, 'b': b, 'hr': log(5*one/2)+one/18}
v['D04'] = (52*H/p2+7)/n+(10+20*H/pi)/n**2
v['G0'] = (28*L/p2+111*one/2+23/pi)/m
v['mesh'] = b*(2*L+2*v['hr'])/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
v['E0'] = v['D04']+v['G0']+v['mesh']+(14+71*one/n)/n
v['Cnear'] = (22*one+(162+40*H/pi)/n)/n
v['Kstar'] = ((112/pi+2)*H+2*L+61*one/3)/n+4*one/n**2
v['Kout'] = (35*L/2+75)/n
# Independent full expansion of Kstar+Kout checks both log/constant sums.
v['Knear'] = ((112/pi+43*one/2)*L+112/pi+292*one/3)/n+4*one/n**2
v['T'] = L*(4*L-3)/p2
v['V'] = v['T']-v['E0']
v['qx'] = (141*v['V']-712)/576
v['qy'] = (47*v['V']-184)/192
v['Bx'] = 77*one/96; v['By'] = one/12
v['target_budget'] = rational_box(F(1,32)-F(1,10000))
domain = v['V'].lo > 0 and v['qx'].lo > 0 and v['qy'].lo > 0 and v['Knear'].lo >= 0
if domain:
    for label, B, q in [('alpha', v['Bx'], v['qx']), ('beta', v['By'], v['qy'])]:
        k = v['Knear']
        disc = 9*B**2+32*q*k
        z = (3*B+integer_sqrt_box(disc, label))/(8*q)
        fractional = B*z**3/4
        linear = k*z**2/2
        v[label+'_discriminant'] = disc
        v[label+'_z'] = z
        v[label+'_fractional'] = fractional
        v[label+'_linear'] = linear
        v[label+'_Psi'] = fractional+linear
    v['total_near_charge'] = v['Cnear']+v['alpha_Psi']+v['beta_Psi']
    v['near_gate'] = v['target_budget']-v['total_near_charge']
contained = {k: D(author['values'][k][0]) <= x.lo <= x.hi <= D(author['values'][k][1]) for k, x in v.items()}
controls = {'physical_floor_domain': n >= 160,
            'target_budget': F(1,32)-F(1,10000) == F(623,20000),
            'cosine_coefficient': F(1,4)-F(1,192) == F(47,192),
            'alpha_quadratic': F(19,24)+F(4,9) == F(89,72),
            'beta_quadratic': F(19,24)+F(1,6) == F(23,24),
            'alpha_fractional': F(15,32)+F(1,3) == F(77,96),
            'beta_fractional': F(1,9)*F(3,4) == F(1,12),
            'K_log': 2+F(35,2) == F(39,2),
            'K_constant': F(61,3)+75 == F(286,3),
            'C_inverse': 4+18 == 22, 'C_inverse_square': 20+142 == 162,
            'D_coarse': F(59,n)+F(70,n*n) < F(1,20),
            'G0_coarse': F(1585,18*m) < F(1,20),
            'mesh_coarse': F(19,2*n)+F(14,n*n) < F(1,100),
            'origin_rows_coarse': F(15,n) < F(1,100),
            'qx_domain_lower': F(3229,1152) > 2, 'qy_domain_lower': F(1183,384) > 2}
checks = {'quadratic_domain': domain, 'complete_key_set': set(v) == keys,
          'all_intervals_contained': all(contained.values()),
          'pi_contained': D(author['pi_interval'][0]) <= pi.lo <= pi.hi <= D(author['pi_interval'][1]),
          'controls_agree': controls == author['controls'], 'all_controls_true': all(controls.values()),
          'near_gate_positive': domain and v['near_gate'].lo > 0,
          'near_gate_reported_lower': domain and v['near_gate'].lo > D('0.0001180816847116292'),
          'charge_reported_upper': domain and v['total_near_charge'].hi < D('0.031031918315289'),
          'charge_below_target': domain and v['total_near_charge'].hi < D('0.03115')}
accepted = all(checks.values())
usage = resource.getrusage(resource.RUSAGE_SELF)
result = {'status': 'ACCEPT_INDEPENDENT_D31_N2048' if accepted else 'FAILED_INDEPENDENT_D31_N2048',
          'passed': accepted, 'N': n, 'interval_count': len(v),
          'values': {k: [str(x.lo), str(x.hi)] for k, x in v.items()},
          'author_contains_independent': contained, 'pi_interval': [str(pi.lo), str(pi.hi)],
          'controls': controls, 'control_count': len(controls), 'checks': checks,
          'radical_integer_brackets': sqrt_records,
          'first_failure': next((k for k, ok in checks.items() if not ok), None),
          'source_sha256': identities['code/post_audit_D31_review/check.py']['sha256'],
          'author_receipt_sha256': hashlib.sha256(author_raw).hexdigest(),
          'arithmetic_sha256': hashlib.sha256(raw).hexdigest(),
          'method': 'Decimal70 basics; atanh90 logs/tail; exact Machin70/20; rational endpoint integer-isqrt80 brackets; expanded Knear; no author imports or Decimal transcendentals',
          'cpu_seconds_through_pre_serialization': usage.ru_utime+usage.ru_stime,
          'whole_process_cpu_cap_seconds': 10, 'python': platform.python_version(),
          'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
content = json.dumps(result, sort_keys=True, indent=2)+'\n'
assert len(identity_text.encode())+len(content.encode()) < 16384
with out.open('x') as handle:
    handle.write(content)
print(json.dumps({'status': result['status'], 'interval_count': len(v),
                  'control_count': len(controls), 'checks': checks,
                  'cpu_seconds_through_pre_serialization': result['cpu_seconds_through_pre_serialization'],
                  'bytes': len(content.encode()), 'sha256': hashlib.sha256(content.encode()).hexdigest()}))
assert accepted, 'First failed result preserved; no retry authorized'
