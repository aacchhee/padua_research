"""One independent D26 endpoint, under the accompanying frozen SPEC."""
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

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
ROOT = BASE.parents[1]
OUT = BASE/'evidence/post_audit_D26_review'
PRIMARY = ROOT/'local-output/argmax-bridge-20261105/post-audit-D26/budget/budget-4096.json'
DEP = BASE/'code/post_audit_D08_review/check.py'
PINS = {
    PRIMARY: '132c03cbda7a2bd10f4f962a5a67ea373941b9ee4fca53c48ea765db0a95e408',
    BASE/'code/post_audit_D26_budget/evaluate.py': '57d94154dd577fc8fa79a0e24d689bfdc51b4ccee28156a69109f375106ee173',
    BASE/'code/post_audit_D26_budget/FREEZE.json': '42271abd32c5b9222ea4748130aceb11d451d02c5421191fcdd2ed76ad409612',
    BASE/'code/post_audit_D26_budget/SPEC.md': '8ae9876b60aa7433fd0f883d53947240833726fa3927dc8bbb5521006abc56c9',
    DEP: '37e58bc880259c27cd2282dab48231f11822452d6fd2db876c846d1b9a008485',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def cpu():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_utime+usage.ru_stime

def write_once(name, value):
    data = (json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode()
    assert len(data)<16384
    with (OUT/name).open('xb') as stream:
        stream.write(data)
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def run():
    for path, digest in PINS.items():
        assert sha(path)==digest, str(path)
    own = {str(p.relative_to(ROOT)):sha(p) for p in (Path(__file__).resolve(), HERE/'SPEC.md')}
    author_raw = PRIMARY.read_bytes()
    assert len(author_raw)==5498
    author = json.loads(author_raw)
    assert type(author['N']) is int and author['N']==4096 and author['passed'] is True
    keys = set('L H b hr D KD MA g VB Qg Gg endpoint_rows central_rows E6 mesh W Cnew G0 E0 T u0 s0 far_coefficient phase_charge far_allowance far_margin far_gate'.split())
    control_keys = set('sole_natural_barrier paper_log_lower paper_T_lower T_minus_new_coefficient D24_inner_strip D24_outer_region endpoint_constant endpoint_log endpoint_inverse_square six_row_constant six_row_log central_sine central_V origin_D0 origin_Z'.split())
    assert set(author['values'])==keys and set(author['controls'])==control_keys
    assert all(type(v) is bool for v in author['controls'].values())
    assert all(type(v) is list and len(v)==2 and all(type(x) is str for x in v) for v in author['values'].values())
    identities = {'N':4096,'checked_before_scalar_arithmetic':True,
        'primary_receipt_sha256':PINS[PRIMARY],'primary_receipt_bytes':len(author_raw),
        'interval_keys':sorted(keys),'interval_count':len(keys),
        'control_keys':sorted(control_keys),'control_count':len(control_keys),
        'input_pins':{str(p.relative_to(ROOT)):h for p,h in PINS.items()},'own_pins':own}
    write_once('identities.json',identities)
    names = {'rounded','Box','maxbox','atanh_log','scalar_log','log','atan_recip'}
    definitions = [node for node in ast.parse(DEP.read_bytes()).body
        if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name in names]
    assert len(definitions)==len(names) and {x.name for x in definitions}==names
    ns = dict(D=D,F=F,localcontext=localcontext,ROUND_FLOOR=ROUND_FLOOR,ROUND_CEILING=ROUND_CEILING,PREC=70)
    exec(compile(ast.Module(body=definitions,type_ignores=[]),str(DEP),'exec'),ns)
    Box, rounded, log = ns['Box'], ns['rounded'], ns['log']
    ns['LOG2'] = ns['atanh_log'](Box(2))
    def rational_box(lo,hi=None):
        hi = lo if hi is None else hi
        return Box(rounded(lambda:D(lo.numerator)/D(lo.denominator),ROUND_FLOOR),
                   rounded(lambda:D(hi.numerator)/D(hi.denominator),ROUND_CEILING))
    al,au = ns['atan_recip'](5,70)
    bl,bu = ns['atan_recip'](239,20)
    pi = rational_box(16*al-4*bu,16*au-4*bl)
    scale = 10**80
    root = math.isqrt(191*scale*scale//768)
    assert 768*root*root<=191*scale*scale<768*(root+1)*(root+1)
    n=4096; m=n+1; one=Box(1); L=log(n); H=1+L; b=4/pi**2
    v={'L':L,'H':H,'b':b,'hr':log(5*one/2)+one/18}
    v['D']=(52*H/pi**2+7)/n+(10+20*H/pi)/n**2
    v['KD']=(352*H/3+2)/(pi*n)
    v['MA']=one/pi+4/pi**2
    v['g']=1+log(2+8*one*m/(3*pi))
    v['VB']=23+(3*v['g']+14*log(m)+46+2*log(2))/pi
    v['Qg']=(28+(40+16*log(2*m))/pi)/m
    # Independent expansion of the full global quadrature charge.
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
    v['u0']=191*one/6144
    v['s0']=rational_box(F(root,scale),F(root+1,scale))
    v['far_coefficient']=25*one/2
    v['phase_charge']=v['KD']*v['s0']
    v['far_allowance']=v['Cnew']+v['phase_charge']
    v['far_margin']=v['u0']*(v['T']-v['far_coefficient'])
    v['far_gate']=v['far_margin']-v['far_allowance']-v['E0']
    assert set(v)==keys
    contained={k:D(author['values'][k][0])<=x.lo<=x.hi<=D(author['values'][k][1]) for k,x in v.items()}
    assert all(contained.values()),[k for k,b in contained.items() if not b]
    assert D(author['pi_interval'][0])<=pi.lo<=pi.hi<=D(author['pi_interval'][1])
    controls={
        'sole_natural_barrier':n==2**12,
        'paper_log_lower':12*F(69,100)==F(207,25) and F(207,25)>8,
        'paper_T_lower':(4*F(207,25)**2-3*F(207,25))/10==F(155871,6250),
        'T_minus_new_coefficient':F(155871,6250)>F(25,2),
        'D24_inner_strip':F(59,20)<F(25,2)*F(61,256),
        'D24_outer_region':F(6211,7260)<F(25,2)*F(2277,32768),
        'endpoint_constant':4+3*59==181,'endpoint_log':1+3*6==19,
        'endpoint_inverse_square':3*200*4*9==21600,
        'six_row_constant':181+12==193,'six_row_log':19+2==21,
        'central_sine':1-F(10,8*33*33)>F(99,100),
        'central_V':F(400,99)<F(9,2),
        'origin_D0':F(8,3)+F(1,2)*F(6,5)<4,'origin_Z':4+F(1,2*32)<5}
    assert set(controls)==control_keys and controls==author['controls'] and all(controls.values())
    assert F(v['T'].lo)>F(25,2)
    assert F(v['far_gate'].lo)>F('0.1671480439691848334')>F(1,6)
    for path,digest in PINS.items():
        assert sha(path)==digest
    assert {str(p.relative_to(ROOT)):sha(p) for p in (Path(__file__).resolve(),HERE/'SPEC.md')}==own
    result={'status':'ACCEPT_INDEPENDENT_D26_N4096','N':n,
        'values':{k:[str(x.lo),str(x.hi)] for k,x in v.items()},'interval_count':len(v),
        'author_contains_independent':contained,'pi_contained':True,
        'controls':controls,'control_count':len(controls),'pi_interval':[str(pi.lo),str(pi.hi)],
        'own_pins':own,'primary_receipt_sha256':PINS[PRIMARY],'arithmetic_sha256':PINS[DEP],
        'method':'Decimal70 directed basics; exact Machin70/20; atanh90 logs with tail; integer sqrt80 bracket; independently expanded Gg; no author imports or Decimal transcendentals',
        'cpu_seconds_through_pre_serialization':cpu(),'whole_process_CPU_cap':10,
        'children':0,'native_or_phase_calls':0,'python':platform.python_version(),
        'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        'completion_requires':'Observed EXIT0; CPU checkpoint is not exact exit CPU'}
    receipt=write_once('scalars.json',result)
    print(json.dumps({'status':result['status'],'interval_count':len(v),'control_count':len(controls),
        'far_gate':result['values']['far_gate'],'cpu_seconds_through_pre_serialization':result['cpu_seconds_through_pre_serialization'],**receipt}),flush=True)
    assert cpu()<10

if __name__=='__main__':
    assert sys.argv[1:]==['--run-once']
    OUT.mkdir(parents=True,exist_ok=False)
    try:
        run()
    except BaseException as error:
        write_once('first-failure.json',{'first_failure':repr(error),'CPU_checkpoint':cpu(),'retry':False})
        raise
