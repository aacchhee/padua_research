"""One independent D33 endpoint, under the accompanying frozen SPEC."""
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
OUT = BASE/'evidence/post_audit_D33_review'
PRIMARY = ROOT/'local-output/argmax-bridge-20261105/post-audit-D33/budget/budget-2048.json'
DEP = BASE/'code/post_audit_D08_review/check.py'
PINS = {
    PRIMARY: '5e2610b0e6226f055a474bff84936bcdd1e88317e75b1671363ed20c717ba875',
    BASE/'code/post_audit_D33_budget/evaluate.py': '54eea39070b022bce6571d1418184a94be9e4b2603dc6e7aac6ae5f1146188c5',
    BASE/'code/post_audit_D33_budget/FREEZE.json': '00af3dca1096971c276fe3726948f7b07c71869b324fa583459c715b5915d425',
    BASE/'code/post_audit_D33_budget/SPEC.md': 'b3ba13a1a848e2a2ec55428da742b6cd1d909a989b3e4ddbe6fea20cc94ba24d',
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
    assert len(author_raw)==7389
    author = json.loads(author_raw)
    assert type(author['N']) is int and author['N']==2048 and author['passed'] is True
    keys = set('L H b hr D KD MA g VB Qg Gg endpoint_rows central_rows E6old mesh W Cbase Cnew G0 E0 T A Kinner u0 ueta s0 seta inner_coefficient outer_coefficient inner_row_charge inner_phase_charge inner_allowance inner_margin Fin outer_phase_charge outer_allowance outer_margin Fout minimum_gate'.split())
    control_keys = set('sole_fixed_case paper_log_lower paper_T_lower T_minus_both_coefficients inner_root_square outer_root_square outer_cosine_lower wide_Dh_gaps wide_reciprocal_sum wide_displacement wide_H_error wide_sine_error wide_central_weight wide_six_row_constant inner_Young_determinant inner_constant11 endpoint_constant endpoint_log endpoint_inverse_square six_row_constant six_row_log central_sine central_V origin_D0 origin_Z'.split())
    assert set(author['values'])==keys and set(author['controls'])==control_keys
    assert all(type(v) is bool for v in author['controls'].values())
    assert all(type(v) is list and len(v)==2 and all(type(x) is str for x in v) for v in author['values'].values())
    identities = {'N':2048,'checked_before_scalar_arithmetic':True,
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
    def sqrt_rational(p,q):
        scale = 10**80
        root = math.isqrt(p*scale*scale//q)
        assert q*root*root <= p*scale*scale < q*(root+1)*(root+1)
        return rational_box(F(root,scale),F(root+1,scale))
    n=2048; m=n+1; one=Box(1); L=log(n); H=1+L; b=4/pi**2
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
    v['E6old']=(193+21*L)/n+21600*one/n**2
    v['mesh']=b*(2*L+2*v['hr'])/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2+(5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
    v['W']=(3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
    v['Cbase']=v['D']+v['Gg']+v['mesh']+v['W']
    v['Cnew']=v['Cbase']+v['E6old']
    v['G0']=(28*L/pi**2+111*one/2+23/pi)/m
    v['E0']=v['D']+v['G0']+v['mesh']+14*one/n+71*one/n**2
    v['T']=(4*L**2-3*L)/pi**2
    v['A']=14*one/n+90*one/n**2
    v['Kinner']=v['KD']+(10+L)/n+4*one/n**2
    v['u0']=191*one/6144
    v['ueta']=2277*one/32768
    v['s0']=sqrt_rational(191,768)
    v['seta']=sqrt_rational(2277,4096)
    v['inner_coefficient']=Box(11)
    v['outer_coefficient']=25*one/2
    v['inner_row_charge']=v['A']*(1-v['u0'])
    v['inner_phase_charge']=v['Kinner']*v['s0']
    v['inner_allowance']=v['Cbase']+v['inner_row_charge']+v['inner_phase_charge']
    v['inner_margin']=v['u0']*(v['T']-11)
    # Independent expansion retains the a=1-u term and all origin charges.
    v['Fin']=v['u0']*(v['T']-11+v['A'])-v['Cbase']-v['A']-v['inner_phase_charge']-v['E0']
    v['outer_phase_charge']=v['KD']*v['seta']
    v['outer_allowance']=v['Cnew']+v['outer_phase_charge']
    v['outer_margin']=v['ueta']*(v['T']-25*one/2)
    v['Fout']=v['outer_margin']-v['Cbase']-v['E6old']-v['outer_phase_charge']-v['E0']
    v['minimum_gate']=Box(min(v['Fin'].lo,v['Fout'].lo),min(v['Fin'].hi,v['Fout'].hi))
    assert set(v)==keys
    contained={k:D(author['values'][k][0])<=x.lo<=x.hi<=D(author['values'][k][1]) for k,x in v.items()}
    assert all(contained.values()),[k for k,b in contained.items() if not b]
    assert D(author['pi_interval'][0])<=pi.lo<=pi.hi<=D(author['pi_interval'][1])
    controls={
        'sole_fixed_case':n==2**11,
        'paper_log_lower':11*F(69,100)==F(759,100) and F(759,100)>7,
        'paper_T_lower':(4*F(759,100)**2-3*F(759,100))/10==F(129789,6250),
        'T_minus_both_coefficients':F(129789,6250)>F(25,2)>11,
        'inner_root_square':8*F(191,6144)==F(191,768),
        'outer_root_square':8*F(2277,32768)==F(2277,4096),
        'outer_cosine_lower':F(9,128)-F(81,98304)==F(2277,32768),
        'wide_Dh_gaps':F(19,8)-F(7,33)>F(17,8),
        'wide_reciprocal_sum':F(64,289)*(2+F(2,3))==F(512,867),
        'wide_displacement':F(3584,2907)<F(5,4),
        'wide_H_error':F(77824,867)<90,
        'wide_sine_error':F(358400,42483)<9,
        'wide_central_weight':F(51200,11781)<F(9,2),
        'wide_six_row_constant':4+10==14 and 9+1==10,
        'inner_Young_determinant':F(1,5)*F(7,5)-F(21,40)**2==F(7,1600),
        'inner_constant11':F(729,280)<11*F(61,256),
        'endpoint_constant':4+3*59==181,'endpoint_log':1+3*6==19,
        'endpoint_inverse_square':3*200*4*9==21600,
        'six_row_constant':181+12==193,'six_row_log':19+2==21,
        'central_sine':1-F(10,8*33*33)>F(99,100),
        'central_V':F(400,99)<F(9,2),
        'origin_D0':F(8,3)+F(1,2)*F(6,5)<4,'origin_Z':4+F(1,2*32)<5}
    assert set(controls)==control_keys and controls==author['controls'] and all(controls.values())
    assert F(v['T'].lo)>F(25,2)
    assert F(v['Fin'].lo)>F(3,100) and F(v['Fout'].lo)>F(3,100)
    for path,digest in PINS.items():
        assert sha(path)==digest
    assert {str(p.relative_to(ROOT)):sha(p) for p in (Path(__file__).resolve(),HERE/'SPEC.md')}==own
    result={'status':'ACCEPT_INDEPENDENT_D33_N2048','N':n,
        'values':{k:[str(x.lo),str(x.hi)] for k,x in v.items()},'interval_count':len(v),
        'author_contains_independent':contained,'pi_contained':True,
        'controls':controls,'control_count':len(controls),'pi_interval':[str(pi.lo),str(pi.hi)],
        'own_pins':own,'primary_receipt_sha256':PINS[PRIMARY],'arithmetic_sha256':PINS[DEP],
        'method':'Decimal70 directed basics; exact Machin70/20; atanh90 logs with tail; integer sqrt80 brackets; independently expanded Gg, Fin and Fout; no author imports or Decimal transcendentals',
        'cpu_seconds_through_pre_serialization':cpu(),'whole_process_CPU_cap':10,
        'children':0,'native_or_phase_calls':0,'python':platform.python_version(),
        'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        'completion_requires':'Observed EXIT0; CPU checkpoint is not exact exit CPU'}
    receipt=write_once('scalars.json',result)
    print(json.dumps({'status':result['status'],'interval_count':len(v),'control_count':len(controls),
        'Fin':result['values']['Fin'],'Fout':result['values']['Fout'],'cpu_seconds_through_pre_serialization':result['cpu_seconds_through_pre_serialization'],**receipt}),flush=True)
    assert cpu()<10

if __name__=='__main__':
    assert sys.argv[1:]==['--run-once']
    OUT.mkdir(parents=True,exist_ok=False)
    try:
        run()
    except BaseException as error:
        write_once('first-failure.json',{'first_failure':repr(error),'CPU_checkpoint':cpu(),'retry':False})
        raise
