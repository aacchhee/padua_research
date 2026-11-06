"""Independent D17 scalar reconstruction; single literal N4096 only."""
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

assert sys.argv[1:] == ['--run-once']
base = Path(__file__).resolve().parents[2]
out = base/'evidence/post_audit_D17_corner_review/scalars.json'
assert not out.exists(), 'No repeat or overwrite authorized'
manifest = json.loads(Path(__file__).with_name('freeze.json').read_text())
for relative, entry in manifest['inputs'].items():
    raw = (base/relative).read_bytes()
    assert len(entry['sha256']) == 64
    assert len(raw) == entry['bytes']
    assert hashlib.sha256(raw).hexdigest() == entry['sha256']
dep = base/'code/post_audit_D08_review/check.py'
raw = dep.read_bytes()
names = {'rounded', 'Box', 'maxbox', 'atanh_log', 'scalar_log', 'log', 'atan_recip'}
selected = [x for x in ast.parse(raw).body if isinstance(x,(ast.FunctionDef, ast.ClassDef)) and x.name in names]
assert len(selected) == len(names) and {x.name for x in selected} == names
ns = dict(D=D, F=F, localcontext=localcontext, ROUND_FLOOR=ROUND_FLOOR, ROUND_CEILING=ROUND_CEILING, PREC=70)
exec(compile(ast.Module(body=selected, type_ignores=[]), str(dep), 'exec'), ns)
Box=ns['Box']; rounded=ns['rounded']; log=ns['log']; maxbox=ns['maxbox']
ns['LOG2']=ns['atanh_log'](Box(2))
al,au=ns['atan_recip'](5,50); bl,bu=ns['atan_recip'](239,16)
pl,pu=16*al-4*bu,16*au-4*bl
pi=Box(rounded(lambda:D(pl.numerator)/D(pl.denominator),ROUND_FLOOR),rounded(lambda:D(pu.numerator)/D(pu.denominator),ROUND_CEILING))
q_exact=F(15,224); d_exact=F(6211,7260); r_exact=F(22,7)**4/31104
checks={
    'sqrt3': F(97,56)**2>3,
    'axis_loss': (2-F(97,56))/4==q_exact,
    'constant_difference': F(8,3)-F(4383,2420)==d_exact,
    'pi_square': F(22,7)**2<10,
    'r_small': r_exact<F(1,300),
    'q_lower': q_exact>F(1,16),
    'quadratic_coefficient': q_exact-r_exact>0,
    'derivative_at_one': 5*q_exact-F(119,5)*r_exact>0,
    'scaled_denominator': 6*72**2==31104,
}
assert all(checks.values())
n=4096; m=n+1; one=Box(1); L=log(n); H=1+L; b=4/pi**2
hr=log(5*one/2)+one/18
v={'L':L,'q0':15*one/224,'d0':6211*one/7260,'r':(22*one/7)**4/31104}
v['T']=(4*L**2-3*L)/pi**2
v['U']=pi**2/72
# ACTUAL origin, not uniform near inputs: p=P=d=0, a=1.
v['origin_D']=(52*H/pi**2+7)/n+(10+20*H/pi)/n**2
v['origin_G']=(28*L/pi**2+111*one/2+23/pi)/m
v['origin_mesh']=b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n**2-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
v['origin_rows']=14*one/n+71*one/n**2
v['E0']=sum((v[k] for k in ('origin_D','origin_G','origin_mesh','origin_rows')),Box(0))
# Complete D05 R=2, cutoff pi/8 error; reconstructed from its formulas.
cutoff=pi/8; X=one*m/8
CX=(5+log(X+one/2)/2)/(2*(X-one/2))+(6+log(X+one/2)/2)/(8*(X-one/2)**2)
v['far_mesh']=7*L/(2*m)+2*CX+(8+hr)/n+one/(2*n**2)
v['far_rows']=(181+19*L)/n+21600*one/n**2
v['far_collision']=(2*one/m)*(7+(2/pi)*(3+2*log(2*m)))+5*one/(n**2*m)+one/(n*m)
v['far_e4']=v['far_mesh']+v['far_rows']+v['far_collision']
v['far_ED04']=((52/pi**2+704/(3*pi))*H+7+4/pi)/n+(10+20*H/pi)/n**2
v['far_Dpole']=(10+20*H/pi)/n**2
u=one/2; sb=one/2+4/cutoff; f=log(8)
entropy=2*u*(1+log((sb+u)/u))
AS=(1+8/cutoff)/pi; VA=16/(pi*cutoff); VS=16/cutoff+6; VV=32/cutoff+23
JS=maxbox(5,2*sb*f+maxbox(2*u,sb+u)*log(2))
VJ=(16/cutoff+4*sb)*f+3*entropy+2*(sb+u)*log(2)+20
WS=VS+JS/pi; VW=VV+VJ/pi
v['far_I_n']=((VA/2+9*AS)*L+VW/2+5*WS+4*VS+(4+5*log(m))/pi)/m
h=pi/m
def envelope(z):
    return 7+(2/pi)*(3+2*log(4*pi/z))
v['far_TZ_bv']=(32+6*log(4*m/pi))/(2*m)
v['far_TZ_initial']=(5*one/m)*(7+(2/pi)*(5+2*log(8*one*m/5)))
v['far_TZ_upper']=envelope(cutoff-h/2)/m
v['far_TZ_holes']=2*envelope(2*h)/m
v['far_TZ']=sum((v[k] for k in ('far_TZ_bv','far_TZ_initial','far_TZ_upper','far_TZ_holes')),Box(0))
v['far_UF']=sum((v[k] for k in ('far_ED04','far_e4','far_I_n','far_Dpole','far_TZ')),Box(0))
v['M']=(4*L**2+79*L/5)/pi**2+8*one/3+v['far_UF']
v['Q']=v['d0']+v['far_UF']+v['E0']
v['axis_loss_delta']=v['q0']*v['T']-v['Q']
v['diagonal_loss']=2*v['q0']*v['T']-v['Q']
v['barrier_cost']=v['r']*v['M']
v['F']=v['axis_loss_delta']-v['barrier_cost']
v['radial_coefficient']=36*v['F']/pi**2
assert v['T'].lo>0 and v['F'].lo>D('0.034801270247317')
assert v['radial_coefficient'].lo>D('0.126939812173742')>D(1)/D(8)
# Author receipt parsed only after independent reconstruction is complete.
author_raw=(base/'code/post_audit_D17_corner/budget-4096.json').read_bytes()
author=json.loads(author_raw)
assert author['N']==n and author['passed'] is True
assert set(v)==set(author['values']) and checks==author['checks']
contained={k:D(author['values'][k][0])<=x.lo<=x.hi<=D(author['values'][k][1]) for k,x in v.items()}
assert all(contained.values())
usage=resource.getrusage(resource.RUSAGE_SELF)
result={'status':'PASS_INDEPENDENT_D17_N4096','N':n,'checks':checks,'values':{k:[str(x.lo),str(x.hi)] for k,x in v.items()},'author_intervals_contain_independent_results':contained,'pi_interval':[str(pi.lo),str(pi.hi)],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'freeze_sha256':hashlib.sha256(Path(__file__).with_name('freeze.json').read_bytes()).hexdigest(),'method':'70-digit directed Decimal basics; rational Machin 50/16 terms; 90-term positive atanh logs with geometric tail; no Decimal.ln or author imports','python':platform.python_version(),'cpu_seconds_through_pre_serialization':usage.ru_utime+usage.ru_stime,'process_cpu_cap_seconds':10,'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
assert result['cpu_seconds_through_pre_serialization']<10
content=json.dumps(result,sort_keys=True,indent=2)+'\n'
assert len(content.encode())<16384
with out.open('x') as handle: handle.write(content)
print(json.dumps({'status':result['status'],'cpu_seconds_through_pre_serialization':result['cpu_seconds_through_pre_serialization'],'bytes':len(content.encode()),'sha256':hashlib.sha256(content.encode()).hexdigest()}))
