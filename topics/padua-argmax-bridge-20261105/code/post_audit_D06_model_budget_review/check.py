"""Independent scalar review; <=10 CPU seconds, no native/kernel imports."""
import time
START = time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU, (9, 10))
import contextlib
import csv
import hashlib
import io
import json
import runpy
import tempfile
from decimal import Decimal, localcontext, ROUND_UP
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'post_audit_D06_model_budget'
checks = {}
def passed(name, count=1):
    checks[name] = checks.get(name, 0) + count

before = hashlib.sha256((AUTHOR/'evidence.csv').read_bytes()).hexdigest()
with tempfile.TemporaryDirectory(prefix='d06-budget-review-') as tmp:
    fresh = Path(tmp)/'evaluate.py'
    fresh.write_bytes((AUTHOR/'evaluate.py').read_bytes())
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        api = runpy.run_path(str(fresh))
    replay_meta = json.loads(capture.getvalue())
    replay = (Path(tmp)/'evidence.csv').read_bytes()
    assert replay == (AUTHOR/'evidence.csv').read_bytes()
    passed('byte_identical_fresh_replay')

# Exact primitive checks, deliberately with hostile ambient Decimal context.
I, ilog = api['I'], api['ilog']
with localcontext() as ctx:
    ctx.prec = 7
    ctx.rounding = ROUND_UP
    for alo, ahi, blo, bhi in [('-1.2','2.3','0.01','7'),
                               ('1e-30','3.1','-9','-0.2'),
                               ('-17','-0.01','2','3.7')]:
        a, b = I(alo,ahi), I(blo,bhi)
        for op, fn in [(lambda:a+b, lambda x,y:x+y),
                       (lambda:a-b, lambda x,y:x-y),
                       (lambda:a*b, lambda x,y:x*y),
                       (lambda:a/b, lambda x,y:x/y)]:
            exact = [fn(Q(x),Q(y)) for x in (alo,ahi) for y in (blo,bhi)]
            out = op()
            assert Q(out.a) <= min(exact) <= max(exact) <= Q(out.b)
            passed('exact_interval_primitive')
    zero_log = ilog(1)
    assert zero_log.a <= 0 <= zero_log.b
    passed('log_one')

def log_small(q):
    z = (q-1)/(q+1)
    assert 0 <= z <= Q(1,3)
    s = sum((2*z**(2*k+1)/(2*k+1) for k in range(80)), Q(0))
    tail = 2*z**161/(161*(1-z*z))
    return s, s+tail

two_lo, two_hi = log_small(Q(2))
def exact_log(q):
    e = 0
    while q >= 2:
        q /= 2
        e += 1
    while q < 1:
        q *= 2
        e -= 1
    lo, hi = log_small(q)
    return (lo+min(e*two_lo,e*two_hi), hi+max(e*two_lo,e*two_hi))

for s in ['0.5','1.5','2','32','512','4096','10000','100000']:
    lo, hi = exact_log(Q(s))
    with localcontext() as ctx:
        ctx.prec = 7
        ctx.rounding = ROUND_UP
        got = ilog(I(s))
    assert Q(got.a) <= lo <= hi <= Q(got.b)
    passed('exact_log_series_containment')

assert Q(11,4)**9 < 10000 and Q(11,4)**8 < 4096 and Q(11,4)**3 < 32
assert Q(352,10000)>Q(1,32) and Q(333,4096)>Q(1,16)
assert Q(1305,20002)>Q(1,16)
passed('analytic_rational_thresholds', 6)

# Independent formula implementation, with R=2 and delta=pi/8 simplified.
# Floating comparisons here are controls, not proof of enclosure arithmetic.
mp.mp.dps = 160
M = mp.mpf
def parameters(label):
    if label == 'uniform':
        return list(map(M, [1,1,2,1,8]))
    if label == 'midpoint':
        return list(map(M, [0,1,2,0,1]))
    alpha,beta = {'zero':(M(0),M(0)), 'quarter':(M(1)/4,M(1)/4),
                  'axis':(M(69)/50,M(0)), 'diag145':(M(29)/20,M(29)/20)}[label]
    p,q = mp.sin(alpha),mp.sin(beta)
    def phi(t):
        t = t % 1
        if t == 0:
            return M(1)
        return mp.sin(mp.pi*t)/mp.pi*(-mp.psi(0,t)-mp.psi(0,1-t)-2*mp.log(mp.pi))
    U = abs(mp.cos((alpha+beta)/2)*phi(M(1)/2+(alpha-beta)/(2*mp.pi))
            +mp.cos((alpha-beta)/2)*phi(M(1)/2+(alpha+beta)/(2*mp.pi)))
    return [(mp.cos(alpha)+mp.cos(beta))/2,p,p+q,max(q-p,M(0)),U]

def independent(n,label):
    a,p,P,d,U = parameters(label)
    pi,L,m = mp.pi,mp.log(n),M(n+1)
    H = 1+L if label == 'uniform' else mp.psi(0,n+1)+mp.euler
    ed = (52*a/pi**2+352*P/(3*pi))*H/n+(7*a+2*P/pi)/n+10/M(n)**2+20*a*H/(pi*n*n)
    X=m/8
    cx=(5+mp.log(X+M(1)/2)/2)/(2*X-1)+(6+mp.log(X+M(1)/2)/2)/(8*(X-M(1)/2)**2)
    mesh=7*L/(2*m)+2*cx+(8+mp.log(M(5)/2)+M(1)/18)/n+M(1)/(2*n*n)
    rows=(181+19*L)/n+M(21600)/(n*n)
    collision=2/m*(7+2/pi*(3+2*mp.log(2*m)))+M(5)/(n*n*m)+1/(n*m)
    e4=mesh+rows+collision
    u=p/2; sb=M(1)/2+32*a/pi
    G=2*u*(1+mp.log1p(sb/u)) if u else M(0)
    vstar=16*U/pi+6; vv=32*U/pi+23
    jstar=max(M(5),2*sb*mp.log(8)+max(2*u,sb+u)*mp.log(2))
    vj=(128*a/pi+4*sb)*mp.log(8)+3*G+2*(sb+u)*mp.log(2)+20
    interior=((9/pi+640*a/pi**2)*L+(vv+vj/pi)/2
              +5*(vstar+jstar/pi)+4*vstar+d/pi*(4+5*mp.log(m)))/m
    dpole=M(10)/(n*n)+20*a*(1+L)/(pi*n*n)
    bv=(32+6*mp.log(4*m/pi))/(2*m)
    initial=5/m*(7+P/pi*(5+2*mp.log(8*m/5)))
    upper=(7+P/pi*(3+2*mp.log(32*m/(m-4))))/m
    holes=2/m*(7+P/pi*(3+2*mp.log(2*m)))
    tz=bv+initial+upper+holes
    return [ed,mesh,rows,collision,e4,interior,dpole,bv,initial,upper,holes,tz,ed+e4+interior+dpole+tz]

csvrows=list(csv.reader(io.StringIO(replay.decode())))
assert len(csvrows)==49
uniform = {}
for row in csvrows[1:]:
    kind,label,n = row[:3]
    n=int(n)
    reference=independent(n,label)
    if kind=='MEASURED':
        for printed,ref in zip(row[3:],reference):
            assert printed == mp.nstr(ref,12), (label,n,printed,mp.nstr(ref,12))
            passed('independent_measured_component')
    else:
        for printed,ref in zip(row[3:],reference):
            assert M(printed)>=ref and M(printed)-ref<M('1.0001e-12')
            passed('independent_uniform_component_control')
        uniform[n]=row[-1]

# Check Machin alternation endpoint order and Decimal conversion exactly.
assert api['pl'] < api['pu']
assert Q(api['PI'].a) <= api['pl'] < api['pu'] <= Q(api['PI'].b)
passed('exact_machin_decimal_conversion')
assert before == hashlib.sha256((AUTHOR/'evidence.csv').read_bytes()).hexdigest()
passed('original_evidence_unchanged')
receipt = {'status':'PASS','checks':checks,'cpu_seconds':time.process_time()-START,
           'author_replay_cpu_seconds':replay_meta['cpu_seconds'],
           'author_script_sha256':hashlib.sha256((AUTHOR/'evaluate.py').read_bytes()).hexdigest(),
           'replay_csv_sha256':hashlib.sha256(replay).hexdigest(),
           'review_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'uniform_totals':uniform,'precision_control_digits':160,
           'scope':'scalar formula/source controls only; no native/kernel/board/quadrature/degree extension'}
(HERE/'receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(receipt,sort_keys=True))
