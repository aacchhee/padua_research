"""Independent D20 N7000 scalar reconstruction; see frozen SPEC."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(9,10))
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

assert sys.argv[1:]==['--run-once']
base=Path(__file__).resolve().parents[2]
outdir=base/'evidence/post_audit_D20_review'
outdir.mkdir(parents=True,exist_ok=True)
out=outdir/'scalars.json'
assert not out.exists(),'No retry or overwrite authorized'
author_raw=(base/'code/post_audit_D20_budget/budget-7000.json').read_bytes()
author_sha=hashlib.sha256(author_raw).hexdigest()
assert author_sha=='5a594e00454c03ed5881194198580b88b67950022efc88f0c7316067a63256a5'
author=json.loads(author_raw)
assert hashlib.sha256((base/'code/post_audit_D20_budget/evaluate.py').read_bytes()).hexdigest()=='7a006bc385ff60840b8c4c0d4d9058d835b279a2f5eb7ac754e5dda7296e5b4c'
assert type(author['N']) is int and author['N']==7000
expected_keys=set('L H b hr D KD MA g VB Qg Gg endpoint_rows central_rows E6 mesh W Cnew G0 E0 T u0 s0 phase_charge far_allowance far_margin far_gate'.split())
assert set(author['values'])==expected_keys
assert all(type(v) is list and len(v)==2 and all(type(x) is str for x in v) for v in author['values'].values())
dep=base/'code/post_audit_D08_review/check.py'
raw=dep.read_bytes(); dep_sha=hashlib.sha256(raw).hexdigest()
assert dep_sha=='37e58bc880259c27cd2282dab48231f11822452d6fd2db876c846d1b9a008485'
identities={'N':7000,'author_receipt_sha256':author_sha,'author_receipt_bytes':len(author_raw),'interval_key_count':len(expected_keys),'interval_keys':sorted(expected_keys),'arithmetic_sha256':dep_sha,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'spec_sha256':hashlib.sha256(Path(__file__).with_name('SPEC.md').read_bytes()).hexdigest(),'checked_before_scalar_arithmetic':True}
with (outdir/'identities.json').open('x') as h: h.write(json.dumps(identities,sort_keys=True,indent=2)+'\n')
names={'rounded','Box','maxbox','atanh_log','scalar_log','log','atan_recip'}
selected=[x for x in ast.parse(raw).body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names]
assert len(selected)==len(names) and {x.name for x in selected}==names
ns=dict(D=D,F=F,localcontext=localcontext,ROUND_FLOOR=ROUND_FLOOR,ROUND_CEILING=ROUND_CEILING,PREC=70)
exec(compile(ast.Module(body=selected,type_ignores=[]),str(dep),'exec'),ns)
Box=ns['Box']; rounded=ns['rounded']; log=ns['log']
ns['LOG2']=ns['atanh_log'](Box(2))
def rational_box(lo,hi=None):
    hi=lo if hi is None else hi
    return Box(rounded(lambda:D(lo.numerator)/D(lo.denominator),ROUND_FLOOR),rounded(lambda:D(hi.numerator)/D(hi.denominator),ROUND_CEILING))
al,au=ns['atan_recip'](5,70); bl,bu=ns['atan_recip'](239,20)
pi=rational_box(16*al-4*bu,16*au-4*bl)
scale=10**80; root=math.isqrt(191*scale*scale//768)
assert 768*root*root<=191*scale*scale<768*(root+1)*(root+1)
n=7000; m=n+1; one=Box(1); L=log(n); H=1+L; b=4/pi**2
v={'L':L,'H':H,'b':b,'hr':log(5*one/2)+one/18}
v['D']=(52*H/pi**2+7)/n+(10+20*H/pi)/n**2
v['KD']=(352*H/3+2)/(pi*n)
v['MA']=one/pi+4/pi**2
v['g']=1+log(2+8*one*m/(3*pi))
v['VB']=23+(3*v['g']+14*log(m)+46+2*log(2))/pi
v['Qg']=(28+(40+16*log(2*m))/pi)/m
# Independently expanded Gg, rather than importing author's component sum.
v['Gg']=(7*v['MA']*L+111*one/2+(63+log(2)+4*log(pi)+7*log(m)+16*log(2*m)+3*v['g']/2)/pi)/m
v['endpoint_rows']=(181+19*L)/n+21600*one/n**2
v['central_rows']=(12+2*L)/n
v['E6']=v['endpoint_rows']+v['central_rows']
v['mesh']=b*(2*L+2*v['hr'])/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
v['W']=(3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
v['Cnew']=v['D']+v['Gg']+v['E6']+v['mesh']+v['W']
v['G0']=(28*L/pi**2+111*one/2+23/pi)/m
v['E0']=v['D']+v['G0']+v['mesh']+14*one/n+71*one/n**2
v['T']=(4*L**2-3*L)/pi**2
v['u0']=191*one/6144; v['s0']=rational_box(F(root,scale),F(root+1,scale))
v['phase_charge']=v['KD']*v['s0']
v['far_allowance']=v['Cnew']+v['phase_charge']
v['far_margin']=v['u0']*(v['T']-22)
v['far_gate']=v['far_margin']-v['far_allowance']-v['E0']
assert set(v)==expected_keys
contained={k:D(author['values'][k][0])<=x.lo<=x.hi<=D(author['values'][k][1]) for k,x in v.items()}
assert all(contained.values()),[k for k,b in contained.items() if not b]
controls={'log_domain':3**8<n,'T_lower':F(116,5)>22,'endpoint_constant':4+3*59==181,'endpoint_log':1+3*6==19,'endpoint_inverse_square':3*200*4*9==21600,'six_row_constant':181+12==193,'six_row_log':19+2==21,'central_sine':1-F(10,8*33*33)>F(99,100),'central_V':F(400,99)<F(9,2),'origin_D0':F(8,3)+F(1,2)*F(6,5)<4,'origin_Z':4+F(1,2*32)<5}
assert controls==author['controls'] and all(controls.values())
assert v['T'].lo>22 and v['far_gate'].lo>D('0.076229903302571')>D(3)/D(40)
assert author['passed'] is True
usage=resource.getrusage(resource.RUSAGE_SELF)
result={'status':'ACCEPT_INDEPENDENT_D20_N7000','N':n,'values':{k:[str(x.lo),str(x.hi)] for k,x in v.items()},'interval_count':len(v),'author_contains_independent':contained,'controls':controls,'control_count':len(controls),'pi_interval':[str(pi.lo),str(pi.hi)],'source_sha256':identities['source_sha256'],'author_receipt_sha256':author_sha,'arithmetic_sha256':dep_sha,'method':'Decimal70 directed basics; exact Machin70/20; atanh90 logs plus tail; integer sqrt80 constant bracket; independently expanded Gg; no author imports or Decimal transcendentals','cpu_seconds_through_pre_serialization':usage.ru_utime+usage.ru_stime,'whole_process_cpu_cap_seconds':10,'python':platform.python_version(),'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
content=json.dumps(result,sort_keys=True,indent=2)+'\n'
assert len(content.encode())<16384
with out.open('x') as h: h.write(content)
print(json.dumps({'status':result['status'],'interval_count':len(v),'control_count':len(controls),'cpu_seconds_through_pre_serialization':result['cpu_seconds_through_pre_serialization'],'bytes':len(content.encode()),'sha256':hashlib.sha256(content.encode()).hexdigest()}))
