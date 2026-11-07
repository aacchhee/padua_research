"""Independent D27 N1024 scalar reconstruction; frozen SPEC controls scope."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (9, 10))
import ast
import hashlib
import json
import platform
import sys
import time
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path

assert sys.argv[1:] == ['--run-once'] and not sys.flags.optimize
base = Path(__file__).resolve().parents[2]
outdir = base/'evidence/post_audit_D27_review'
outdir.mkdir(parents=True, exist_ok=True)
out = outdir/'scalars.json'
start = outdir/'identities.json'
assert not out.exists() and not start.exists(), 'No retry or overwrite authorized'
freeze = json.loads(Path(__file__).with_name('PREEXEC.json').read_text())
assert freeze['N'] == 1024 and freeze['cpu_cap_seconds'] == 10
observed = {}
for rel, expected in freeze['inputs'].items():
    data = (base/rel).read_bytes()
    got = hashlib.sha256(data).hexdigest()
    assert got == expected, rel
    observed[rel] = {'sha256': got, 'bytes': len(data)}
author_raw = (base/'code/post_audit_D27_corner/budget-1024.json').read_bytes()
author = json.loads(author_raw)
assert type(author['N']) is int and author['N'] == 1024
assert author['passed'] is True
keys = set('L H b hr D04_constant KD MA g VB Qg Gg endpoint_rows central_rows E6 mesh W Cnew G0 E0 T q Paxis_upper constant_gap r U Mmodel Mnew axis_allowance diagonal_allowance delta diagonal_lower criterion F radial_coefficient'.split())
assert set(author['values']) == keys
assert all(type(v) is list and len(v) == 2 and all(type(x) is str for x in v) for v in author['values'].values())
dep = base/'code/post_audit_D08_review/check.py'
raw = dep.read_bytes()
identities = {'N': 1024, 'input_identities': observed,
              'prerelease_report_sha256': '1473ba56312ab3817fa323c66b16caf0a21b3d1e69c3b0bdb6b1d1d692858055',
              'interval_keys': sorted(keys), 'interval_count': len(keys),
              'cpu_cap_seconds': 10, 'checked_before_scalar_arithmetic': True}
identity_text = json.dumps(identities, sort_keys=True, indent=2)+'\n'
with start.open('x') as handle:
    handle.write(identity_text)
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

al, au = ns['atan_recip'](5, 70)
bl, bu = ns['atan_recip'](239, 20)
pi = rational_box(16*al-4*bu, 16*au-4*bl)
n = 1024; m = n+1; one = Box(1); p2 = pi**2
L = log(n); H = 1+L; b = 4/p2
v = {'L': L, 'H': H, 'b': b, 'hr': log(5*one/2)+one/18}
v['D04_constant'] = (52*H/p2+7)/n+(10+20*H/pi)/n**2
v['KD'] = (352*H/3+2)/(pi*n)
v['MA'] = one/pi+4/p2
v['g'] = 1+log(2+8*one*m/(3*pi))
v['VB'] = 23+(3*v['g']+14*log(m)+46+2*log(2))/pi
v['Qg'] = (28+(40+16*log(2*m))/pi)/m
# Independently expanded global quadrature, cross-checking the author's sum.
v['Gg'] = (7*v['MA']*L+111*one/2+(63+log(2)+4*log(pi)+7*log(m)+16*log(2*m)+3*v['g']/2)/pi)/m
v['endpoint_rows'] = (181+19*L)/n+21600*one/n**2
v['central_rows'] = (12+2*L)/n
v['E6'] = (193+21*L)/n+21600*one/n**2
v['mesh'] = b*(2*L+2*v['hr'])/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
v['W'] = (3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
v['Cnew'] = v['D04_constant']+v['Gg']+v['E6']+v['mesh']+v['W']
v['G0'] = (28*L/p2+111*one/2+23/pi)/m
v['E0'] = v['D04_constant']+v['G0']+v['mesh']+(14+71*one/n)/n
v['T'] = L*(4*L-3)/p2
v['q'] = one/7; v['Paxis_upper'] = 5*one/7
v['constant_gap'] = rational_box(F(8, 3)-F(4383, 2420))
rq = F(22, 7)**4/6144
v['r'] = rational_box(rq)
v['U'] = p2/32
v['Mmodel'] = L*(4*L+79*one/5)/p2+8*one/3
v['Mnew'] = v['Mmodel']+v['Cnew']+2*v['KD']
v['axis_allowance'] = v['Cnew']+5*v['KD']/7
v['diagonal_allowance'] = v['Cnew']+10*v['KD']/7
v['delta'] = v['T']/7-v['constant_gap']-v['axis_allowance']-v['E0']
v['diagonal_lower'] = 2*v['T']/7-v['constant_gap']-v['diagonal_allowance']-v['E0']
v['criterion'] = p2**2/6144
# Expanded combined F also checks the monotonicity expression used in proof.
v['F'] = (4*(v['q']-v['r'])*L**2-(3*v['q']+79*v['r']/5)*L)/p2-v['constant_gap']-8*v['r']/3-(1+v['r'])*v['Cnew']-(5*one/7+2*v['r'])*v['KD']-v['E0']
v['radial_coefficient'] = 16*v['F']/p2
assert set(v) == keys
contained = {k: D(author['values'][k][0]) <= x.lo <= x.hi <= D(author['values'][k][1]) for k, x in v.items()}
pi_contained = D(author['pi_interval'][0]) <= pi.lo <= pi.hi <= D(author['pi_interval'][1])
controls = {'axis_sqrt': 2 > F(7,5)**2,
            'axis_u': (1-F(5,7))/2 == F(1,7),
            'constant_gap': F(8,3)-F(4383,2420) == F(6211,7260),
            'square_normalization': 6*32**2 == 6144,
            'r_upper': rq < F(1,60),
            'leading_positive': F(1,7)-rq > 0,
            'derivative_positive': F(5,7)-F(119,5)*rq > 0,
            'derivative_bound': F(5,7)-F(119,300) == F(667,2100),
            'diagonal_charge': 2*F(5,7) == F(10,7),
            'pi_criterion': v['r'].lo > v['criterion'].hi}
checks = {'all_intervals_contained': all(contained.values()),
          'pi_contained': pi_contained, 'controls_agree': controls == author['controls'],
          'all_controls_true': all(controls.values()), 'Mnew_positive': v['Mnew'].lo > 0,
          'T_positive': v['T'].lo > 0, 'F_positive': v['F'].lo > 0,
          'F_reported_lower': v['F'].lo > D('0.1444175412061567'),
          'radial_reported_lower': v['radial_coefficient'].lo > D('0.2341208994'),
          'radial_exceeds_one_eighth': v['radial_coefficient'].lo > D('0.125')}
accepted = all(checks.values())
usage = resource.getrusage(resource.RUSAGE_SELF)
result = {'status': 'ACCEPT_INDEPENDENT_D27_N1024' if accepted else 'FAILED_INDEPENDENT_D27_N1024',
          'N': n, 'passed': accepted, 'interval_count': len(v),
          'values': {k: [str(x.lo), str(x.hi)] for k, x in v.items()},
          'author_contains_independent': contained, 'pi_interval': [str(pi.lo), str(pi.hi)],
          'controls': controls, 'control_count': len(controls), 'checks': checks,
          'source_sha256': observed['code/post_audit_D27_review/check.py']['sha256'],
          'author_receipt_sha256': hashlib.sha256(author_raw).hexdigest(),
          'arithmetic_sha256': hashlib.sha256(raw).hexdigest(),
          'method': 'Decimal70 directed basics; exact Machin70/20; atanh90 logs plus tail; expanded Gg,E6,F; no author code or Decimal transcendentals',
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
assert accepted, 'First failed result retained; no retry authorized'
