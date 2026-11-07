"""D16: sole frozen N10000 directed scalar sufficient-budget call."""
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
out = Path(__file__).with_name('budget-10000.json')
assert not out.exists(), 'One-shot receipt already exists; no retry authorized'
base = Path(__file__).resolve().parents[2]
dep = base / 'code/post_audit_D06_model_budget/evaluate.py'
raw = dep.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413'
wanted = {'directed', 'I', 'ilog', 'imax', 'atan_bounds', 'components'}
defs = [x for x in ast.parse(raw).body
        if isinstance(x, (ast.FunctionDef, ast.ClassDef)) and x.name in wanted]
assert {x.name for x in defs} == wanted
env = {'D': D, 'localcontext': localcontext, 'ROUND_FLOOR': ROUND_FLOOR,
       'ROUND_CEILING': ROUND_CEILING, 'Q': Q, 'PREC': 50}
exec(compile(ast.Module(body=defs, type_ignores=[]), str(dep), 'exec'), env)
I = env['I']; log = env['ilog']; directed = env['directed']; atan = env['atan_bounds']
al, au = atan(5, 70); bl, bu = atan(239, 20)
pl, pu = 16*al-4*bu, 16*au-4*bl
pi = I(directed(lambda: D(pl.numerator)/D(pl.denominator), ROUND_FLOOR),
       directed(lambda: D(pu.numerator)/D(pu.denominator), ROUND_CEILING))
n = 10000; m = n+1; one = I(1); half = one/2; L = log(n); H = 1+L
b = 4/(pi*pi); r = log(one*5/2)+one/18
Dc = ((52/(pi*pi))*H+7)/n+10*one/(n*n)+20*H/(pi*n*n)
KD = (352*H/(3*pi)+2/pi)/n
G = ((one*21/5)*L+(one*9/4)*log(2*m)+one*1022/15)/m
G0 = ((28/(pi*pi))*L+one*111/2+23/pi)/m
M = b*(2*L+2*r)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2)
W = (3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
C = Dc+G+M+14*one/n+71*one/(n*n)
K = KD+W+(8+L)/n+4*one/(n*n)
E0 = Dc+G0+M+14*one/n+71*one/(n*n)
T = (4*L*L-3*L)/(pi*pi); A = one*77/96
B = ((one*47/192)*T-one*113/72)/2
assert B.a > 0
J = (27*A*A*A*A)/(256*B*B*B)
linear_charge = K*K/(2*B)
near_slack = one/16-C-E0-8*J-linear_charge
parts = env['components'](n, one, one, one*2, one, one*8, H, pi, log, env['imax'])
far_margin = (one*191/6144)*(T-22)
far_slack = far_margin-parts[-1]-E0
vals = {'L': L, 'T': T, 'A': A, 'B': B, 'D': Dc, 'KD': KD,
        'G': G, 'G0': G0, 'M': M, 'W': W, 'C': C, 'K': K, 'E0': E0,
        'J': J, 'eight_J': 8*J, 'linear_charge': linear_charge,
        'near_slack': near_slack, 'far_margin': far_margin, 'far_slack': far_slack}
names = ['ED04', 'mesh', 'rows', 'collision', 'e4', 'I_n', 'Dpole',
         'TZ_bv', 'TZ_initial', 'TZ_upper', 'TZ_holes', 'TZ', 'UF']
vals.update({'far_'+k: v for k, v in zip(names, parts)})
usage = resource.getrusage(resource.RUSAGE_SELF)
result = {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
          'values': {k: [str(v.a), str(v.b)] for k, v in vals.items()},
          'near_pass': near_slack.a > 0, 'far_pass': T.a > 22 and far_slack.a > 0,
          'passed': near_slack.a > 0 and T.a > 22 and far_slack.a > 0,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'dependency_sha256': hashlib.sha256(raw).hexdigest(),
          'pi_interval': [str(pi.a), str(pi.b)],
          'cpu_seconds_including_startup': usage.ru_utime+usage.ru_stime,
          'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
with out.open('x') as handle:
    handle.write(json.dumps(result, sort_keys=True, indent=2)+'\n')
print(json.dumps(result, sort_keys=True))
