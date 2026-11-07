"""Independent D11, n=16000 only; see SPEC.md, frozen before execution."""
import time
START=time.process_time()
import ast
import hashlib
import json
import platform
import resource
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(9,10))
base=Path(__file__).resolve().parents[2]
dep=base/'code/post_audit_D08_review/check.py'
raw=dep.read_bytes()
expected='37e58bc880259c27cd2282dab48231f11822452d6fd2db876c846d1b9a008485'
assert hashlib.sha256(raw).hexdigest()==expected
names={'rounded','Box','maxbox','atanh_log','scalar_log','log','atan_recip'}
selected=[x for x in ast.parse(raw).body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names]
assert {x.name for x in selected}==names
namespace={'D':D,'F':F,'localcontext':localcontext,'ROUND_FLOOR':ROUND_FLOOR,'ROUND_CEILING':ROUND_CEILING,'PREC':70}
exec(compile(ast.Module(body=selected,type_ignores=[]),str(dep),'exec'),namespace)
Box=namespace['Box']; rounded=namespace['rounded']; log=namespace['log']; maxbox=namespace['maxbox']
namespace['LOG2']=namespace['atanh_log'](Box(2))
aa,ab=namespace['atan_recip'](5,50)
ba,bb=namespace['atan_recip'](239,16)
pl,pu=16*aa-4*bb,16*ab-4*ba
pi=Box(rounded(lambda:D(pl.numerator)/D(pl.denominator),ROUND_FLOOR),rounded(lambda:D(pu.numerator)/D(pu.denominator),ROUND_CEILING))
one=Box(1); n=16000; m=n+1; L=log(n); b=4/pi**2; H=1+L
v={'logN':L}
v['near_ED04']=((52/pi**2+176/(3*pi))*H+7+1/pi)/n+10*one/n**2+20*H/(pi*n**2)
v['near_Eglobal']=((21*one/5)*L+(9*one/4)*log(2*m)+1022*one/15)/m
r=log(5*one/2)+one/18
v['near_Bmesh']=b*(2*L+2*r)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
v['near_dBlog_over_pi']=(3*log(m)+log(2)+2*log(pi)+2)/(2*pi*m)
v['near_B6']=(18+L/2)/n+73*one/n**2
v['near_Ehat']=sum((v[k] for k in ('near_ED04','near_Eglobal','near_Bmesh','near_dBlog_over_pi','near_B6')),Box(0))
delta=pi/8; X=one*m/8
CX=(5+log(X+one/2)/2)/(2*(X-one/2))+(6+log(X+one/2)/2)/(8*(X-one/2)**2)
v['far_mesh']=7*L/(2*m)+2*CX+(8+r)/n+one/(2*n*n)
v['far_rows']=(181+19*L)/n+21600*one/n**2
v['far_collision']=(2*one/m)*(7+(2/pi)*(3+2*log(2*m)))+5*one/(n*n*m)+one/(n*m)
v['far_e4']=v['far_mesh']+v['far_rows']+v['far_collision']
v['far_ED04']=((52/pi**2+704/(3*pi))*H+7+4/pi)/n+10*one/n**2+20*H/(pi*n**2)
v['far_Dpole']=10*one/n**2+20*H/(pi*n**2)
u=one/2; sb=one/2+4/delta; f=log(8)
G=2*u*(1+log((sb+u)/u))
AS=(1+8/delta)/pi; VA=16/(pi*delta); VS=16/delta+6; VV=32/delta+23
JS=maxbox(5,2*sb*f+maxbox(2*u,sb+u)*log(2))
VJ=(16/delta+4*sb)*f+3*G+2*(sb+u)*log(2)+20
WS=VS+JS/pi; VW=VV+VJ/pi
v['far_I_n']=((VA/2+9*AS)*L+VW/2+5*WS+4*VS+(4+5*log(m))/pi)/m
h=pi/m
def W(z): return 7+(2/pi)*(3+2*log(4*pi/z))
v['far_TZ_bv']=(32+6*log(4*m/pi))/(2*m)
v['far_TZ_initial']=(5*one/m)*(7+(2/pi)*(5+2*log(8*one*m/5)))
v['far_TZ_upper']=W(delta-h/2)/m
v['far_TZ_holes']=2*W(2*h)/m
v['far_TZ']=sum((v[k] for k in ('far_TZ_bv','far_TZ_initial','far_TZ_upper','far_TZ_holes')),Box(0))
v['far_UF']=sum((v[k] for k in ('far_ED04','far_e4','far_I_n','far_Dpole','far_TZ')),Box(0))
T=(4*L**2-3*L)/pi**2; A=77*one/96; B=(47*T/192-113*one/72)/2
assert B.lo>0 and T.lo>22
J=27*A**4/(256*B**3)
v.update(T=T,A=A,B=B,near_model_excess_J=J,near_two_error_charge=2*v['near_Ehat'])
v['near_physical_slack']=one/16-2*v['near_Ehat']-J
v['far_model_margin']=191*(T-22)/6144
v['far_physical_slack']=v['far_model_margin']-v['far_UF']-v['near_Ehat']
assert v['near_physical_slack'].lo>D('0.007')
assert v['far_physical_slack'].lo>D('0.19')
# Evidence comparison only, after independently reconstructing every value.
author_path=base/'code/post_audit_D11_onset/budget-16000.json'
author_raw=author_path.read_bytes()
assert hashlib.sha256(author_raw).hexdigest()=='34675d877186c34f16a40c2dc5b2470c27ec2fbb40f62b338c2dd24e96583afb47'
author=json.loads(author_raw)
assert set(v)==set(author['values'])
contained={k:D(author['values'][k][0])<=x.lo<=x.hi<=D(author['values'][k][1]) for k,x in v.items()}
assert all(contained.values())
result={'status':'PASS_INDEPENDENT_D11_N16000','N':n,'values':{k:[str(x.lo),str(x.hi)] for k,x in v.items()},'author_intervals_contain_independent_results':contained,'pi_interval':[str(pi.lo),str(pi.hi)],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_library_sha256':expected,'author_evidence_sha256':hashlib.sha256(author_raw).hexdigest(),'method':'70-digit directed Decimal basic arithmetic; exact rational alternating Machin (50,16); 90 positive atanh log terms plus geometric tail; no Decimal.ln; AST-selected arithmetic definitions only','python':platform.python_version(),'cpu_seconds':time.process_time()-START}
assert result['cpu_seconds']<10
out=base/'evidence/post_audit_D11_onset_review/scalars.json'
out.parent.mkdir(parents=True,exist_ok=True)
assert not out.exists()
content=json.dumps(result,sort_keys=True,indent=2)+'\n'
assert len(content.encode())<16384
out.write_text(content)
print(json.dumps({'status':result['status'],'cpu_seconds':result['cpu_seconds'],'bytes':len(content.encode()),'sha256':hashlib.sha256(content.encode()).hexdigest()}))
