"""Independent D08 scalar audit: directed basics, rational pi, series logs.

No author evaluator is imported. Natural logs use positive atanh series:
log(y)=2 sum_{j=0}^{K-1} t^(2j+1)/(2j+1)+tail, t=(y-1)/(y+1),
0<=tail<=2 t^(2K+1)/((2K+1)(1-t*t)). Reduce by powers of two
to 1<=y<=2; K=90. Integer/Fraction operations are exact; Decimal
basic operations use explicit outward contexts at 70 digits.
"""
import hashlib
import json
import platform
import resource
import time
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (17, 18))
START = time.process_time()
PREC = 70


def rounded(op, direction):
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = direction
        return op()


class Box:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = self.lo if hi is None else D(hi)
        assert self.lo <= self.hi

    @staticmethod
    def box(x):
        return x if isinstance(x, Box) else Box(x)

    def __add__(self, other):
        q = self.box(other)
        return Box(rounded(lambda: self.lo + q.lo, ROUND_FLOOR),
                   rounded(lambda: self.hi + q.hi, ROUND_CEILING))

    __radd__ = __add__

    def __neg__(self):
        return Box(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -self.box(other)

    def __rsub__(self, other):
        return self.box(other) + -self

    def __mul__(self, other):
        q = self.box(other)
        pairs = [(x, y) for x in (self.lo, self.hi) for y in (q.lo, q.hi)]
        return Box(min(rounded(lambda: x*y, ROUND_FLOOR) for x, y in pairs),
                   max(rounded(lambda: x*y, ROUND_CEILING) for x, y in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        q = self.box(other)
        assert q.lo*q.hi > 0
        pairs = [(x, y) for x in (self.lo, self.hi) for y in (q.lo, q.hi)]
        return Box(min(rounded(lambda: x/y, ROUND_FLOOR) for x, y in pairs),
                   max(rounded(lambda: x/y, ROUND_CEILING) for x, y in pairs))

    def __rtruediv__(self, other):
        return self.box(other)/self

    def __pow__(self, k):
        assert isinstance(k, int) and k >= 0
        acc = Box(1)
        for _ in range(k):
            acc = acc*self
        return acc


def maxbox(*args):
    xs = [Box.box(x) for x in args]
    return Box(max(x.lo for x in xs), max(x.hi for x in xs))


def atanh_log(y):
    assert y.lo >= 1 and y.hi <= 2
    t = (y-1)/(y+1)
    t2 = t*t
    power, total = t, Box(0)
    for j in range(90):
        total = total + power/(2*j+1)
        power = power*t2
    upper_tail = 2*power/(181*(1-t2))
    return 2*total + Box(0, upper_tail.hi)


LOG2 = atanh_log(Box(2))


def scalar_log(x):
    assert x > 0
    # The dyadic scaling is exact as a rational. Directed conversion
    # then encloses its value and keeps the series argument in [1,2].
    y, k = F(x), 0
    while y < 1:
        y *= 2
        k -= 1
    while y > 2:
        y /= 2
        k += 1
    z = Box(rounded(lambda: D(y.numerator)/D(y.denominator), ROUND_FLOOR),
            rounded(lambda: D(y.numerator)/D(y.denominator), ROUND_CEILING))
    return atanh_log(z) + k*LOG2


def log(x):
    q = Box.box(x)
    return Box(scalar_log(q.lo).lo, scalar_log(q.hi).hi)


def atan_recip(q, count):
    part = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(count)), F(0))
    following = F((-1)**count, (2*count+1)*q**(2*count+1))
    return min(part, part+following), max(part, part+following)


aa, ab = atan_recip(5, 40)
ba, bb = atan_recip(239, 12)
pl, pu = 16*aa-4*bb, 16*ab-4*ba
pi = Box(rounded(lambda: D(pl.numerator)/D(pl.denominator), ROUND_FLOOR),
         rounded(lambda: D(pu.numerator)/D(pu.denominator), ROUND_CEILING))
one = Box(1)


def evaluate(n):
    m, L, b = n+1, log(n), 4/(pi*pi)
    H = 1+L
    near_d = ((52/(pi*pi)+176/(3*pi))*H+7+1/pi)/n+10*one/n**2+20*H/(pi*n**2)
    near_g = ((21*one/5)*L+(9*one/4)*log(2*m)+1022*one/15)/m
    r = log(5*one/2)+one/18
    near_m = b*(2*L+2*r)/n+(4+b*(L+one/n))/(4*n*n-1)+b/(2*n-1)**2
    near_m += (5+b*(log(n+one/2)+2))/(4*(n-one/2)**2)
    near_log = (3*log(m)+log(2)+2*log(pi)+2)/(2*pi*m)
    near_6 = (18+L/2)/n+73*one/n**2
    near = near_d+near_g+near_m+near_log+near_6

    delta, x = pi/8, one*m/8
    hr = log(5*one/2)+one/18
    cx = (5+log(x+one/2)/2)/(2*(x-one/2))
    cx += (6+log(x+one/2)/2)/(8*(x-one/2)**2)
    mesh = 7*L/(2*m)+2*cx+(8+hr)/n+one/(2*n*n)
    rows = (181+19*L)/n+21600*one/n**2
    collision = (2*one/m)*(7+(2/pi)*(3+2*log(2*m)))+5*one/(n*n*m)+one/(n*m)
    e4 = mesh+rows+collision
    far_d = ((52/(pi*pi)+704/(3*pi))*H+7+4/pi)/n+10*one/n**2+20*H/(pi*n**2)
    pole = 10*one/n**2+20*H/(pi*n**2)
    u, sb, f = one/2, one/2+4/delta, log(8)
    entropy = 2*u*(1+log((sb+u)/u))
    astar, va = (1+8/delta)/pi, 16/(pi*delta)
    vstar, vv = 16/delta+6, 32/delta+23
    jstar = maxbox(5, 2*sb*f+maxbox(2*u, sb+u)*log(2))
    vj = (16/delta+4*sb)*f+3*entropy+2*(sb+u)*log(2)+20
    wstar, vw = vstar+jstar/pi, vv+vj/pi
    interior = ((va/2+9*astar)*L+vw/2+5*wstar+4*vstar+(4+5*log(m))/pi)/m
    h = pi/m
    def W(z):
        return 7+(2/pi)*(3+2*log(4*pi/z))
    tz = (32+6*log(4*m/pi))/(2*m)
    tz += (5*one/m)*(7+(2/pi)*(5+2*log(8*one*m/5)))
    tz += W(delta-h/2)/m+2*W(2*h)/m
    far = far_d+e4+interior+pole+tz
    margin = (191*one/6144)*((49*one/121)*L*L-(147*one/484)*L)-(123*one/40-4383*one/2420)
    return {'near_ED04':near_d, 'near_Eglobal':near_g, 'near_Bmesh':near_m,
            'near_dBlog_over_pi':near_log, 'near_B6':near_6, 'near_total':near,
            'far_E_D04':far_d, 'far_e4':e4, 'far_I_n':interior,
            'far_Dpole':pole, 'far_TZ':tz, 'far_total':far,
            'far_model_margin':margin, 'far_lambda_gap':margin-far-near,
            'near_1over80_slack':one/80-near,
            'near_lambda_gap':one/16-(2*near+one/500+one/32+one/1000000)}


c, k = F(15,32), F(11,20)
controls = {
    'alpha_quadratic_slack':F(20811,1920)-F(1225,144)-F(16,9)-k,
    'alpha_large_slack':F(1,32)-27*c**4/(256*k**3),
    'alpha_small_slack':F(1,32)-c*F(3,8)**6-F(16,9)*F(3,8)**8,
    'beta_slack':F(1,10**6)-F(1,36*2**45)-F(1,2*10**9),
    'constant_slack':F(123,40)-F(8821,3000)-F(1,63**2)-F(637,4805),
    'beta_quadratic_slack':F(20811,1920)-F(395,48)-F(5,2),
    'eta_slack':F(1,1000)-F(12989329736187619160983471,38345245772322816000000000000),
    'near_uniform_gap_slack':F(1,16)-F(1,40)-F(1,500)-F(1,32)-F(1,1000000)-F(1,250),
}
assert all(x>0 for x in controls.values())
base = Path(__file__).resolve().parents[2]
comparisons = {}
output = {}
for n in (40000,50000):
    values = evaluate(n)
    author = json.loads((base/'code/post_audit_D08_onset'/f'budget-{n}.json').read_text())
    comparisons[n] = all(D(author['values'][key][0]) <= val.lo <= val.hi <= D(author['values'][key][1])
                         for key, val in values.items())
    assert comparisons[n]
    assert values['near_1over80_slack'].lo > 0
    assert values['near_lambda_gap'].lo > D('0.004')
    if n == 40000:
        assert values['far_lambda_gap'].hi < 0
    else:
        assert values['far_lambda_gap'].lo > D('0.0367')
    output[n] = {key:[str(val.lo),str(val.hi)] for key,val in values.items()}
result = {'status':'PASS_INDEPENDENT_SERIES_INTERVAL_RECONSTRUCTION',
          'trusted_arithmetic':'Python integer/Fraction exact; Decimal basic arithmetic directed at 70 digits',
          'log_method':'90 positive atanh terms, analytic geometric tail, dyadic reduction; no Decimal.ln',
          'pi_method':'exact alternating Machin bounds: atan(1/5) 40 terms, atan(1/239) 12 terms',
          'pi_interval':[str(pi.lo),str(pi.hi)], 'values':output,
          'author_outward_intervals_contain_independent_results':comparisons,
          'exact_positive_slacks':{k:str(v) for k,v in controls.items()},
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'python':platform.python_version(), 'cpu_seconds':time.process_time()-START}
dest = base/'evidence/post_audit_D08_review/scalars.json'
dest.parent.mkdir(parents=True,exist_ok=True)
assert not dest.exists(), 'fresh evidence only; choose a new run path'
dest.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'status':result['status'], 'cpu_seconds':result['cpu_seconds'],
                  'output':str(dest), 'bytes':dest.stat().st_size,
                  'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
