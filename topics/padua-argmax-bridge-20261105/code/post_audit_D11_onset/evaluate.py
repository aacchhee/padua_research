"""D11: preregistered16000/conditional20000 scalar budgets only."""
import time
START=time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(4,5))
import ast
import hashlib
import json
import sys
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from pathlib import Path

base=Path(__file__).resolve().parents[2]
dep=base/'code/post_audit_D06_model_budget/evaluate.py'
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413'
wanted={'directed','I','ilog','imax','atan_bounds','components'}
defs=[x for x in ast.parse(raw).body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in wanted]
assert {x.name for x in defs}==wanted
env={'D':D,'localcontext':localcontext,'ROUND_FLOOR':ROUND_FLOOR,'ROUND_CEILING':ROUND_CEILING,'Q':Q,'PREC':50}
exec(compile(ast.Module(body=defs,type_ignores=[]),str(dep),'exec'),env)
I=env['I']; log=env['ilog']; directed=env['directed']; atan=env['atan_bounds']
al,au=atan(5,70); bl,bu=atan(239,20)
pl,pu=16*al-4*bu,16*au-4*bl
pi=I(directed(lambda:D(pl.numerator)/D(pl.denominator),ROUND_FLOOR),
     directed(lambda:D(pu.numerator)/D(pu.denominator),ROUND_CEILING))
n=int(sys.argv[1]); assert n in (16000,20000)
m=n+1; L=log(n); one=I(1); half=one/2
b=4/(pi*pi); H=1+L
ed04=((52/(pi*pi)+352*half/(3*pi))*H+7+1/pi)/n+10*one/(n*n)+20*H/(pi*n*n)
eglobal=((one*21/5)*L+(one*9/4)*log(2*m)+one*1022/15)/m
hr=log(one*5/2)+one/18
bmesh=b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2)
blog=(3*log(m)+log(2)+2*log(pi)+2)/m
logcharge=blog/(2*pi)
b6=(18+half*L)/n+one*73/(n*n)
enear=ed04+eglobal+bmesh+logcharge+b6
parts=env['components'](n,one,one,one*2,one,one*8,H,pi,log,env['imax'])
T=(4*L*L-3*L)/(pi*pi)
A=one*77/96
B=((one*47/192)*T-one*113/72)/2
assert B.a>0
J=(27*A*A*A*A)/(256*B*B*B)
near_slack=one/16-2*enear-J
far_margin=(one*191/6144)*(T-22)
far_slack=far_margin-parts[-1]-enear
values={'logN':L,'T':T,'A':A,'B':B,'near_model_excess_J':J,
        'near_ED04':ed04,'near_Eglobal':eglobal,'near_Bmesh':bmesh,
        'near_dBlog_over_pi':logcharge,'near_B6':b6,'near_Ehat':enear,
        'near_two_error_charge':2*enear,'near_physical_slack':near_slack,
        'far_model_margin':far_margin,'far_physical_slack':far_slack}
names=['ED04','mesh','rows','collision','e4','I_n','Dpole','TZ_bv','TZ_initial','TZ_upper','TZ_holes','TZ','UF']
values.update({'far_'+k:v for k,v in zip(names,parts)})
result={'N':n,'status':'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
        'values':{k:[str(v.a),str(v.b)] for k,v in values.items()},
        'near_pass':near_slack.a>0,'far_pass':T.a>22 and far_slack.a>0,
        'passed':near_slack.a>0 and T.a>22 and far_slack.a>0,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256':hashlib.sha256(raw).hexdigest(),
        'pi_interval':[str(pi.a),str(pi.b)],
        'cpu_seconds':time.process_time()-START}
out=Path(__file__).with_name('budget-'+str(n)+'.json')
out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
