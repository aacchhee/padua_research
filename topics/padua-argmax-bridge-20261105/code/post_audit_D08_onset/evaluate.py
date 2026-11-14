"""D08: two preregistered scalar endpoints; no old main/kernel execution."""
import time
START=time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(9,10))
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
tree=ast.parse(raw)
defs=[node for node in tree.body if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name in wanted]
assert {node.name for node in defs}==wanted
env={'D':D,'localcontext':localcontext,'ROUND_FLOOR':ROUND_FLOOR,'ROUND_CEILING':ROUND_CEILING,'Q':Q,'PREC':50}
exec(compile(ast.Module(body=defs,type_ignores=[]),str(dep),'exec'),env)
I=env['I']; log=env['ilog']; directed=env['directed']; atan=env['atan_bounds']
al,au=atan(5,70); bl,bu=atan(239,20)
pl,pu=16*al-4*bu,16*au-4*bl
pi=I(directed(lambda:D(pl.numerator)/D(pl.denominator),ROUND_FLOOR),
     directed(lambda:D(pu.numerator)/D(pu.denominator),ROUND_CEILING))
n=int(sys.argv[1]); assert n in (40000,50000)
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
far_parts=env['components'](n,one,one,one*2,one,one*8,H,pi,log,env['imax'])
efar=far_parts[-1]
margin=(one*191/6144)*((one*49/121)*L*L-(one*147/484)*L)-(one*123/40-one*4383/2420)
near_gap=one/16-(2*enear+one/500+one/32+one/1000000)
far_gap=margin-efar-enear
def endpoints(value):
    with localcontext() as ctx:
        ctx.prec=50
        return [str(value.a.quantize(D('1e-15'),rounding=ROUND_FLOOR)),
                str(value.b.quantize(D('1e-15'),rounding=ROUND_CEILING))]
values={'logN':L,'near_ED04':ed04,'near_Eglobal':eglobal,'near_Bmesh':bmesh,'near_dBlog_over_pi':logcharge,'near_B6':b6,'near_total':enear,
        'near_1over80_slack':one/80-enear,'near_lambda_gap':near_gap,'far_E_D04':far_parts[0],'far_e4':far_parts[4],
        'far_I_n':far_parts[5],'far_Dpole':far_parts[6],'far_TZ':far_parts[-2],'far_total':efar,'far_model_margin':margin,'far_lambda_gap':far_gap}
c=Q(15,32); k=Q(11,20)
assert Q(20811,1920)-Q(1225,144)-Q(16,9)>k
assert 27*c**4/(256*k**3)<Q(1,32)
assert c*Q(3,8)**6+Q(16,9)*Q(3,8)**8<Q(1,32)
assert Q(1,36*2**45)+Q(1,2*10**9)<Q(1,10**6)
assert Q(8821,3000)+Q(1,63**2)+Q(637,4805)<Q(123,40)
result={'N':n,'status':'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT','values':{k:endpoints(v) for k,v in values.items()},
        'near_pass':(one/80-enear).a>0 and near_gap.a>0,'far_pass':far_gap.a>0,
        'dependency_sha256':hashlib.sha256(raw).hexdigest(),'pi_interval':[str(pi.a),str(pi.b)],
        'exact_fraction_controls':5,'cpu_seconds':time.process_time()-START}
out=Path(__file__).with_name('budget-'+str(n)+'.json')
out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
