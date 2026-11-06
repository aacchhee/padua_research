"""Independent one-shot D18 N7000 reconstruction; see frozen SPEC."""
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

assert sys.argv[1:] == ['--run-once']
base = Path(__file__).resolve().parents[2]
outdir = base/'evidence/post_audit_D18_review'
outdir.mkdir(parents=True, exist_ok=True)
out = outdir/'scalars.json'
assert not out.exists(), 'No retry/overwrite authorized'
author_path = base/'code/post_audit_D18_budget/budget-7000.json'
author_raw = author_path.read_bytes()
author_sha = hashlib.sha256(author_raw).hexdigest()
assert author_sha == '9547d1015ba30b78d9a789cf62019c36a2ad1eff1d304b9887311428ede90e2a'
author = json.loads(author_raw)
author_code = base/'code/post_audit_D18_budget/evaluate.py'
assert hashlib.sha256(author_code.read_bytes()).hexdigest() == '3b5700fe790240d280f3567dae9e947a38038a1ecadceca77d802a7948c085d4'
expected_keys = set('L T A B J C K E0 near_D near_KD near_G origin_G0 near_mesh near_W fractional_charge linear_charge near_gate u0 s0 S g Af Bf I1 Z1 far_allowance far_margin far_gate base_ED04 base_mesh base_rows base_collision base_e4 base_I0 base_Dpole base_TZ_bv base_TZ_initial base_TZ_upper base_TZ_holes base_TZ0 base_Af'.split())
assert type(author['N']) is int and author['N'] == 7000
assert set(author['values']) == expected_keys
assert all(type(v) is list and len(v) == 2 and all(type(x) is str for x in v) for v in author['values'].values())
dep = base/'code/post_audit_D08_review/check.py'
raw = dep.read_bytes()
expected_dep = '37e58bc880259c27cd2282dab48231f11822452d6fd2db876c846d1b9a008485'
assert hashlib.sha256(raw).hexdigest() == expected_dep
identities = {'N':7000, 'author_receipt_sha256':author_sha, 'author_receipt_bytes':len(author_raw), 'author_interval_key_count':len(expected_keys), 'author_interval_keys':sorted(expected_keys), 'arithmetic_sha256':expected_dep, 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'spec_sha256':hashlib.sha256(Path(__file__).with_name('SPEC.md').read_bytes()).hexdigest(), 'checked_before_scalar_calculation':True}
with (outdir/'identities.json').open('x') as h:
    h.write(json.dumps(identities, sort_keys=True, indent=2)+'\n')
names = {'rounded','Box','maxbox','atanh_log','scalar_log','log','atan_recip'}
selected = [x for x in ast.parse(raw).body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names]
assert len(selected) == len(names) and {x.name for x in selected} == names
ns = dict(D=D,F=F,localcontext=localcontext,ROUND_FLOOR=ROUND_FLOOR,ROUND_CEILING=ROUND_CEILING,PREC=70)
exec(compile(ast.Module(body=selected,type_ignores=[]),str(dep),'exec'),ns)
Box=ns['Box']; rounded=ns['rounded']; log=ns['log']; maxbox=ns['maxbox']
ns['LOG2']=ns['atanh_log'](Box(2))
al,au=ns['atan_recip'](5,70); bl,bu=ns['atan_recip'](239,20)
pl,pu=16*al-4*bu,16*au-4*bl
def rational_box(lo, hi=None):
    hi=lo if hi is None else hi
    return Box(rounded(lambda:D(lo.numerator)/D(lo.denominator),ROUND_FLOOR),rounded(lambda:D(hi.numerator)/D(hi.denominator),ROUND_CEILING))
pi=rational_box(pl,pu)
scale=10**80
root=math.isqrt((191*scale*scale)//768)
assert 768*root*root <= 191*scale*scale < 768*(root+1)*(root+1)
s0=rational_box(F(root,scale),F(root+1,scale))
n=7000; m=n+1; one=Box(1); L=log(n); H=1+L; b=4/pi**2
r=log(5*one/2)+one/18
v={'L':L}
v['near_D']=(52*H/pi**2+7)/n+(10+20*H/pi)/n**2
v['near_KD']=(352*H/3+2)/(pi*n)
v['near_G']=(21*L/5+9*log(2*m)/4+1022*one/15)/m
v['origin_G0']=(28*L/pi**2+111*one/2+23/pi)/m
v['near_mesh']=b*(2*L+2*r)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
v['near_W']=(3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
v['C']=v['near_D']+v['near_G']+v['near_mesh']+14*one/n+71*one/n**2
v['K']=v['near_KD']+v['near_W']+(8+L)/n+4*one/n**2
v['E0']=v['near_D']+v['origin_G0']+v['near_mesh']+14*one/n+71*one/n**2
v['T']=(4*L**2-3*L)/pi**2; v['A']=77*one/96
v['B']=(47*v['T']/192-113*one/72)/2
assert v['B'].lo>0 and v['T'].lo>22
v['J']=27*v['A']**4/(256*v['B']**3)
v['fractional_charge']=64*v['J']/27
v['linear_charge']=v['K']**2/v['B']
v['near_gate']=one/16-v['C']-v['E0']-v['fractional_charge']-v['linear_charge']
X=one*m/8
CX=(5+log(X+one/2)/2)/(2*(X-one/2))+(6+log(X+one/2)/2)/(8*(X-one/2)**2)
v['base_mesh']=7*L/(2*m)+2*CX+(8+r)/n+one/(2*n*n)
v['base_rows']=(181+19*L)/n+21600*one/n**2
v['base_collision']=(2*one/m)*(7+(2/pi)*(3+2*log(2*m)))+5*one/(n*n*m)+one/(n*m)
v['base_e4']=v['base_mesh']+v['base_rows']+v['base_collision']
v['base_ED04']=v['near_D']; v['base_Dpole']=(10+20*H/pi)/n**2
S=one/2+32/pi; f=log(8); V=128/pi+6; VV=256/pi+23
As=(1+64/pi)/pi; VA=128/pi**2
j0=maxbox(5,2*S*f+S*log(2))
VJ0=(128/pi+4*S)*f+2*S*log(2)+20
W0=V+j0/pi; VW0=VV+VJ0/pi
v['base_I0']=((VA/2+9*As)*L+VW0/2+5*W0+4*V)/m
v['base_TZ_bv']=(16+3*log(4*m/pi))/m
v['base_TZ_initial']=35*one/m; v['base_TZ_upper']=7*one/m; v['base_TZ_holes']=14*one/m
v['base_TZ0']=sum((v[k] for k in ('base_TZ_bv','base_TZ_initial','base_TZ_upper','base_TZ_holes')),Box(0))
v['Af']=sum((v[k] for k in ('base_ED04','base_e4','base_I0','base_Dpole','base_TZ0')),Box(0))
v['base_Af']=v['Af']; v['S']=S; v['s0']=s0; v['u0']=191*one/6144
v['g']=1+log(1+2*S/s0)
v['I1']=(3*v['g']/2+3*log(2)+4+5*log(m))/(pi*m)
v['Z1']=(34+10*log(8*one*m/5)+2*log(32*one*m/(m-4))+4*log(2*m))/(pi*m)
v['Bf']=v['near_KD']+v['I1']+v['Z1']
v['far_allowance']=v['Af']+v['Bf']*s0
v['far_margin']=v['u0']*(v['T']-22)
v['far_gate']=v['far_margin']-v['far_allowance']-v['E0']
assert set(v)==expected_keys
contained={k:D(author['values'][k][0])<=x.lo<=x.hi<=D(author['values'][k][1]) for k,x in v.items()}
assert all(contained.values()), [k for k,b in contained.items() if not b]
controls={'fractional_allocation':F(3,4)**-3==F(64,27),'linear_allocation':1/(4*F(1,4))==1,'log_domain':3**8<n,'T_lower':F(116,5)>22,'B_lower':(F(47,192)*F(116,5)-F(113,72))/2>2}
assert controls==author['controls'] and all(controls.values())
obstruction=v['base_I0']+v['base_e4']+v['E0']-v['far_margin']
assert v['near_gate'].lo>D('0.002716177429282')>D(1)/D(400)
assert v['far_gate'].hi<D('-0.099513391604782')
assert obstruction.lo>D('0.045436078373106')
assert author['near_pass'] is True and author['far_pass'] is False and author['passed'] is False
usage=resource.getrusage(resource.RUSAGE_SELF)
result={'status':'ACCEPT_RECONSTRUCTION_NEAR_PASS_FAR_FAIL','N':n,'values':{k:[str(x.lo),str(x.hi)] for k,x in v.items()},'interval_count':len(v),'author_contains_independent':contained,'controls':controls,'control_count':len(controls),'retained_obstruction_interval':[str(obstruction.lo),str(obstruction.hi)],'pi_interval':[str(pi.lo),str(pi.hi)],'source_sha256':identities['source_sha256'],'author_receipt_sha256':author_sha,'arithmetic_sha256':expected_dep,'method':'Decimal70 directed basics; rational Machin70/20; atanh90 plus tail logs; integer sqrt80 bracket; no author imports or Decimal transcendental calls','cpu_seconds_through_pre_serialization':usage.ru_utime+usage.ru_stime,'whole_process_cpu_cap_seconds':10,'python':platform.python_version(),'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
content=json.dumps(result,sort_keys=True,indent=2)+'\n'
assert len(content.encode())<16384
with out.open('x') as h: h.write(content)
print(json.dumps({'status':result['status'],'interval_count':len(v),'control_count':len(controls),'cpu_seconds_through_pre_serialization':result['cpu_seconds_through_pre_serialization'],'bytes':len(content.encode()),'sha256':hashlib.sha256(content.encode()).hexdigest()}))
