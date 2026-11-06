"""Independent D16 reconstruction; N10000 only. See frozen SPEC.md."""
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
out = base/'evidence/post_audit_D16_budget_review/scalars.json'
assert not out.exists(), 'No retry or overwrite authorized'
dep = base/'code/post_audit_D08_review/check.py'
raw = dep.read_bytes()
expected = '37e58bc880259c27cd2282dab48231f11822452d6fd2db876c846d1b9a008485'
assert len(expected) == 64 and hashlib.sha256(raw).hexdigest() == expected
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
n=10000; m=n+1; one=Box(1); L=log(n); H=1+L; b=4/pi**2
r=log(one*5/2)+one/18
v={'L':L}
# D04 constant and coefficient of P<=rho, kept separate.
v['D']=(52*H/pi**2+7)/n+(10+20*H/pi)/n**2
v['KD']=(352*H/3+2)/(pi*n)
v['G']=(21*L/5+9*log(2*m)/4+1022*one/15)/m
# Actual p=q=P=d=0 in D07 E_global: VA/2 + 6 MA = 28/pi^2.
v['G0']=(28*L/pi**2+(23+46/pi)/2+28+16)/m
v['M']=b*(2*L+2*r)/n+(4+b*(L+one/n))/(4*n**2-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
v['W']=(3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
v['C']=v['D']+v['G']+v['M']+14*one/n+71*one/n**2
v['K']=v['KD']+v['W']+(8+L)/n+4*one/n**2
v['E0']=v['D']+v['G0']+v['M']+14*one/n+71*one/n**2
T=(4*L**2-3*L)/pi**2; A=77*one/96; B=(47*T/192-113*one/72)/2
assert T.lo>22 and B.lo>0
J=27*A**4/(256*B**3)
v.update(T=T,A=A,B=B,J=J,eight_J=8*J,linear_charge=v['K']**2/(2*B))
v['near_slack']=one/16-v['C']-v['E0']-v['eight_J']-v['linear_charge']
# Full D05 R=2, delta=pi/8 allowance, independently restated.
delta=pi/8; X=one*m/8
CX=(5+log(X+one/2)/2)/(2*(X-one/2))+(6+log(X+one/2)/2)/(8*(X-one/2)**2)
v['far_mesh']=7*L/(2*m)+2*CX+(8+r)/n+one/(2*n*n)
v['far_rows']=(181+19*L)/n+21600*one/n**2
v['far_collision']=(2*one/m)*(7+(2/pi)*(3+2*log(2*m)))+5*one/(n*n*m)+one/(n*m)
v['far_e4']=v['far_mesh']+v['far_rows']+v['far_collision']
v['far_ED04']=((52/pi**2+704/(3*pi))*H+7+4/pi)/n+(10+20*H/pi)/n**2
v['far_Dpole']=(10+20*H/pi)/n**2
u=one/2; sb=one/2+4/delta; f=log(8)
entropy=2*u*(1+log((sb+u)/u))
AS=(1+8/delta)/pi; VA=16/(pi*delta); VS=16/delta+6; VV=32/delta+23
JS=maxbox(5,2*sb*f+maxbox(2*u,sb+u)*log(2))
VJ=(16/delta+4*sb)*f+3*entropy+2*(sb+u)*log(2)+20
WS=VS+JS/pi; VW=VV+VJ/pi
v['far_I_n']=((VA/2+9*AS)*L+VW/2+5*WS+4*VS+(4+5*log(m))/pi)/m
h=pi/m
def envelope(z):
    return 7+(2/pi)*(3+2*log(4*pi/z))
v['far_TZ_bv']=(32+6*log(4*m/pi))/(2*m)
v['far_TZ_initial']=(5*one/m)*(7+(2/pi)*(5+2*log(8*one*m/5)))
v['far_TZ_upper']=envelope(delta-h/2)/m
v['far_TZ_holes']=2*envelope(2*h)/m
v['far_TZ']=sum((v[k] for k in ('far_TZ_bv','far_TZ_initial','far_TZ_upper','far_TZ_holes')),Box(0))
v['far_UF']=sum((v[k] for k in ('far_ED04','far_e4','far_I_n','far_Dpole','far_TZ')),Box(0))
v['far_margin']=191*(T-22)/6144
v['far_slack']=v['far_margin']-v['far_UF']-v['E0']
assert v['near_slack'].lo>D('0.011867625153962')
assert v['far_slack'].lo>D('0.002676038916455')
# Read author evidence only after every independent scalar is reconstructed.
author_path=base/'code/post_audit_D16_budget/budget-10000.json'
author_raw=author_path.read_bytes()
assert hashlib.sha256(author_raw).hexdigest()=='84c64165a325d8df8f4b413a388717feb4a5316730d038aade2ac1696b9915bc'
author=json.loads(author_raw)
assert set(v)==set(author['values']) and author['N']==10000
contained={k:D(author['values'][k][0])<=x.lo<=x.hi<=D(author['values'][k][1]) for k,x in v.items()}
assert all(contained.values())
usage=resource.getrusage(resource.RUSAGE_SELF)
result={'status':'PASS_INDEPENDENT_D16_N10000','N':n,'values':{k:[str(x.lo),str(x.hi)] for k,x in v.items()},'author_intervals_contain_independent_results':contained,'pi_interval':[str(pi.lo),str(pi.hi)],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_library_sha256':expected,'author_evidence_sha256':hashlib.sha256(author_raw).hexdigest(),'method':'70-digit directed Decimal basics; rational Machin 50/16 terms; 90-term positive atanh logs plus analytic geometric tail; no Decimal.ln or author imports','python':platform.python_version(),'cpu_seconds_through_pre_serialization':usage.ru_utime+usage.ru_stime,'process_cpu_cap_seconds':10,'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
assert result['cpu_seconds_through_pre_serialization']<10
content=json.dumps(result,sort_keys=True,indent=2)+'\n'
assert len(content.encode())<16384
with out.open('x') as handle: handle.write(content)
print(json.dumps({'status':result['status'],'cpu_seconds_through_pre_serialization':result['cpu_seconds_through_pre_serialization'],'bytes':len(content.encode()),'sha256':hashlib.sha256(content.encode()).hexdigest()}))
