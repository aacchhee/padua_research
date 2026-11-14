"""Independent D37 N1024 replay: rational integer intervals; one attempt."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (9, 10))
import hashlib
import json
import sys
import time
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PRIMARY = ROOT/'local-output/argmax-bridge-20261105/post-audit-D37/budget/budget-1024.json'
OUT = ROOT/'local-output/argmax-bridge-20261105/post-audit-D37/independent'
SCALE = 10**65
TERMS = 90


def ceildiv(a, b):
    return -((-a)//b)


class Iv:
    def __init__(self, low, high):
        assert isinstance(low, int) and isinstance(high, int) and low <= high
        self.low, self.high = low, high

    @staticmethod
    def cast(value):
        if isinstance(value, Iv):
            return value
        assert isinstance(value, (int, F)), 'no floating mathematical input'
        value = F(value)
        return Iv(value.numerator*SCALE//value.denominator,
                  ceildiv(value.numerator*SCALE, value.denominator))

    def __add__(self, other):
        other = Iv.cast(other)
        return Iv(self.low+other.low, self.high+other.high)

    __radd__ = __add__

    def __neg__(self):
        return Iv(-self.high, -self.low)

    def __sub__(self, other):
        return self+-Iv.cast(other)

    def __rsub__(self, other):
        return Iv.cast(other)+-self

    def __mul__(self, other):
        other = Iv.cast(other)
        products = [x*y for x in (self.low, self.high) for y in (other.low, other.high)]
        return Iv(min(products)//SCALE, ceildiv(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Iv.cast(other)
        assert not other.low <= 0 <= other.high
        pairs = [(x*SCALE, y) for x in (self.low, self.high)
                 for y in (other.low, other.high)]
        return Iv(min(x//y for x, y in pairs), max(ceildiv(x, y) for x, y in pairs))

    def __rtruediv__(self, other):
        return Iv.cast(other)/self

    def __pow__(self, exponent):
        assert exponent == 2
        return self*self

    def strings(self):
        def render(x):
            sign = '-' if x < 0 else ''
            x = abs(x)
            return sign+(str(x//SCALE)+'.'+str(x % SCALE).zfill(65)).rstrip('0').rstrip('.')
        return [render(self.low), render(self.high)]


def R(a, b=1):
    return Iv.cast(F(a, b))


def root(value):
    value = Iv.cast(value)
    assert value.low >= 0
    lo = isqrt(value.low*SCALE)
    hi = isqrt(value.high*SCALE)
    if hi*hi < value.high*SCALE:
        hi += 1
    return Iv(lo, hi)


def atanh_series(numerator, denominator):
    assert 0 <= 3*numerator <= denominator
    z = R(numerator, denominator)
    square = z*z
    power = z
    total = R(0)
    for j in range(TERMS):
        total += power/(2*j+1)
        power *= square
    tail = ceildiv(9*SCALE, 4*(2*TERMS+1)*3**(2*TERMS+1))
    return 2*total+Iv(0, tail)


LN2 = None
LOG_CACHE = {}


def log_point(value):
    global LN2
    assert value > 0
    if value in LOG_CACHE:
        return LOG_CACHE[value]
    if LN2 is None:
        LN2 = atanh_series(1, 3)
    numerator, denominator, exponent = value, SCALE, 0
    while numerator >= 2*denominator:
        denominator *= 2
        exponent += 1
    while numerator < denominator:
        numerator *= 2
        exponent -= 1
    answer = exponent*LN2+atanh_series(numerator-denominator, numerator+denominator)
    LOG_CACHE[value] = answer
    return answer


def log(value):
    value = Iv.cast(value)
    assert value.low > 0
    return Iv(log_point(value.low).low, log_point(value.high).high)


def arctangent(q, count):
    partial = F(0)
    for j in range(count):
        partial += F(1 if j % 2 == 0 else -1, (2*j+1)*q**(2*j+1))
    following = F(1 if count % 2 == 0 else -1, (2*count+1)*q**(2*count+1))
    return min(partial, partial+following), max(partial, partial+following)


def pi_interval():
    a, b = arctangent(5, 100)
    c, d = arctangent(239, 32)
    low, high = 16*a-4*d, 16*b-4*c
    return Iv(Iv.cast(low).low, Iv.cast(high).high)


def psi(B, q, k):
    B, q, k = Iv.cast(B), Iv.cast(q), Iv.cast(k)
    assert B.low >= 0 and q.low > 0 and k.low >= 0
    z = (3*B+root(9*B*B+32*q*k))/(8*q)
    return z, B*z*z*z/4+k*z*z/2


def cpu():
    use = resource.getrusage(resource.RUSAGE_SELF)
    return use.ru_utime+use.ru_stime


def identity(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def save(path, data):
    encoded = (json.dumps(data, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode()
    assert len(encoded) < 16384, 'complete receipt overflow; no pruning or retry'
    with path.open('xb') as stream:
        stream.write(encoded)


def check_pins():
    raw = (HERE/'FREEZE.json').read_bytes()
    frozen = json.loads(raw)
    assert frozen['N'] == 1024 and frozen['scale_digits'] == 65 and frozen['CPU_hard'] == 10
    for record in frozen['code_data']:
        assert identity(ROOT/record['path']) == record
    return hashlib.sha256(raw).hexdigest()


def calculate(state):
    n, m = 1024, 1025
    pi = pi_interval()
    L, lm, l2, lp = log(n), log(m), log(2), log(pi)
    H = 1+L
    b, hr = 4/(pi*pi), log(R(5, 2))+R(1, 18)
    ordinary = 52*H/(pi*pi*n)+R(7, n)+R(10, n*n)+20*H/(pi*n*n)
    kd = (6*H+16*H/(3*pi)+2/pi)/n
    ma = 1/pi+b
    gpar = 1+log(2+8*m/(3*pi))
    vb = 23+(3*gpar+14*lm+46+2*l2)/pi
    qg = (28+8*(5+2*log(2*m))/pi)/m
    gg = (7*ma*L+R(111, 2)+(63+l2+4*lp+7*lm+16*log(2*m)+R(3, 2)*gpar)/pi)/m
    ep = (181+19*L)/n+R(21600, n*n)
    cen = (12+2*L)/n
    e6 = (193+21*L)/n+R(21600, n*n)
    mesh = (2*b*(L+hr)/n+(4+b*L+b/n)/(4*n*n-1)
            +b/(2*n-1)**2+(5+b*(log(n+R(1, 2))+2))/(2*n-1)**2)
    w = (3*lm+l2+2*lp+2)/(pi*m)
    cnew = ordinary+gg+e6+mesh+w
    g0 = (28*L/(pi*pi)+R(111, 2)+23/pi)/m
    e0 = ordinary+g0+mesh+R(14, n)+R(71, n*n)
    T = L*(4*L-3)/(pi*pi)
    V = T-e0
    cn = R(22, n)+R(162, n*n)+40*H/(pi*n*n)
    cw = R(23, n)+R(204, n*n)+40*H/(pi*n*n)
    kn = (R(55, 2)*L+R(310, 3))/n+R(4, n*n)
    kw = (28*L+R(316, 3))/n+R(4, n*n)
    qnx, qny = R(47, 192)*V-R(89, 72), R(47, 192)*V-R(23, 24)
    qbx, qby = R(47, 192)*V-R(53, 40), R(47, 192)*V-R(119, 120)
    qlx, qly = R(11, 48)*V-R(53, 40), R(11, 48)*V-R(119, 120)
    rt2 = root(2)
    tx, ty = qlx-3/(2*rt2)-kw, qly-3/(20*rt2)-kw
    values = dict(L=L, H=H, b=b, hr=hr, D=ordinary, KD35=kd, MA=ma,
                  gpar=gpar, VB=vb, Qg=qg, Gg=gg, endpoint_old=ep,
                  central_old=cen, E6old=e6, mesh=mesh, W=w, Cnew=cnew,
                  G0=g0, E0=e0, T=T, V=V, CN=cn, KN=kn, CW=cw, KW=kw,
                  qNx=qnx, qNy=qny, qBx=qbx, qBy=qby, qLx=qlx, qLy=qly,
                  sqrt2=rt2, tail_x=tx, tail_y=ty)
    domains = {name+'_nonnegative': values[name].low >= 0
               for name in ('CN','KN','CW','KW','Cnew','E0','KD35')}
    domains.update({name+'_positive': values[name].low > 0
                    for name in ('V','qNx','qNy','qBx','qBy','qLx','qLy','tail_x','tail_y')})
    state.update(stage='domain checks', domains=domains,
                 values={k: v.strings() for k, v in values.items()})
    assert len(domains) == 16 and all(domains.values())
    for suffix, B, q, k in (('Nx', F(77,96), qnx, kn), ('Ny', F(1,12), qny, kn),
                           ('Bx', 1, qbx, kw+R(1,2)), ('By', F(1,10), qby, kw+R(1,2)),
                           ('Lx', 1, qlx, kw), ('Ly', F(1,10), qly, kw)):
        z, maximum = psi(B, q, k)
        values['z'+suffix], values['Psi'+suffix] = z, maximum
    ex, ey = 1/(2*rt2)-qlx/4+kw/2, 1/(20*rt2)-qly/4+kw/2
    floor, eta, u1, dc, s1 = R(3,50), R(1,2), R(47,384), R(6211,7260), root(R(47,48))
    gates = {'GN': floor-cn-values['PsiNx']-values['PsiNy'],
             'GB': R(1,4)-cw-values['PsiBx']-values['PsiBy'],
             'GX': -cw-ex-values['PsiLy'], 'GY': -cw-ey-values['PsiLx'],
             'GO': u1*T-dc-cnew-kd*s1-e0}
    values.update(Ex=ex, Ey=ey, floor=floor, eta=eta, u1=u1, Dc=dc, s1=s1, **gates)
    values['minimum_gate'] = Iv(min(v.low for v in gates.values()), min(v.high for v in gates.values()))
    controls = {
        'fixed_1024': n == 2**10,
        'paper_log': 10*F(69,100) == F(69,10) and 10*F(7,10) == 7,
        'paper_T': (4*F(69,10)**2-3*F(69,10))/10 == F(8487,500),
        'near_constant': 4+18 == 22 and 20+142 == 162,
        'wide_constant': 4+19 == 23 and 20+184 == 204,
        'near_K_constant': 10+8+F(7,3)+75 == F(286,3),
        'near_K_log': 1+1+F(35,2) == F(39,2),
        'wide_K_constant': 10+12+F(7,3)+73 == F(292,3),
        'wide_K_log': 1+1+18 == 20,
        'wide_qx': F(19,24)+F(8,15) == F(53,40),
        'wide_qy': F(19,24)+F(3,2)*F(2,15) == F(119,120),
        'wide_Bx': F(3,5)+F(3,4)*F(8,15) == 1,
        'wide_By': F(3,4)*F(2,15) == F(1,10),
        'fixed_multiplier': F(1,2)**2 == F(1,4),
        'box_cosine': F(1,4)-F(1,192) == F(47,192),
        'large_cosine': F(1,4)-F(1,48) == F(11,48),
        'floor_nearest': 183*45 < 14336,
        'floor_small_angle': F(1763685,28114944) > F(3,50),
        'floor_middle_margin': F(1617,24200)-F(1,200)-F(3,50) == F(11,6050),
        'floor_middle_losses': F(2945,628) < F(19,4) and F(19,4096) < F(24,5000)
                               and F(550,3*n*n) < F(1,5000),
        'scalar_W_bounds': F(160,189) < 1 and F(6400,3969) < F(5,3)
                           and F(189440,83349) < F(7,3) and F(5701632,1750329) < F(10,3)
                           and F(1340866560,183784545) < F(15,2),
        'scalar_f4': F(299,16)*F(8,25) == F(299,50) < 6,
        'scalar_H': F(93696,312500)+F(1539,51200) < F(1,3),
        'central_short_and_shift': F(5120,9653) < F(8,15) and F(1280,9653) < F(2,15),
        'central_fractional': F(5760,9653) < F(3,5),
        'origin_D0': F(8,3)+F(1,2)*F(6,5) < 4,
        'origin_Z': 4+F(1,64) < 5,
        'old_global_endpoint': 4+3*59 == 181 and 1+3*6 == 19,
        'old_global_six': 181+12 == 193 and 19+2 == 21,
        'outer_root': 8*F(47,384) == F(47,48),
        'outer_cosine': F(1,8)-F(1,384) == F(47,384),
        'uniform_Dc': F(8,3)-F(4383,2420) == F(6211,7260),
        'paper_tail_domain': F(8487,500)-F(1,4) == F(4181,250)
                              and F(30091,12000) > 2 > F(15,14)+F(1,3)}
    state.update(stage='fresh endpoint complete', values={k: v.strings() for k, v in values.items()}, controls=controls)
    assert len(values) == 59 and len(controls) == 33 and all(controls.values())
    primary = json.loads(PRIMARY.read_bytes())
    assert primary['N'] == n and primary['passed'] is True and primary['interval_count'] == 59
    assert primary['source']['sha256'] == '2f5fa327a1c93063e4602a8cad06779601c89c86dcecc1e89cb4e1fba070d1eb'
    assert primary['freeze']['sha256'] == '4cf0bf3ef7d41eed5b04ceee9ac26426cee84f2c7578b4f8f868b84a9d9f51b5'
    assert set(values) == set(primary['values']) and domains == primary['domains'] and controls == primary['controls']
    def contained(value, pair):
        return F(pair[0]) <= F(value.low,SCALE) <= F(value.high,SCALE) <= F(pair[1])
    comparisons = {name: contained(value, primary['values'][name]) for name, value in values.items()}
    comparisons['pi'] = contained(pi, primary['pi_interval'])
    margins = {'near_1_over_200': gates['GN'].low*200 > SCALE,
               'far_3_over_100': all(gates[name].low*100 > 3*SCALE for name in ('GB','GX','GY','GO')),
               'negative_Ex_Ey': ex.high < 0 and ey.high < 0}
    passed = all(v.low > 0 for v in gates.values()) and all(comparisons.values()) and all(margins.values())
    state.update(stage='primary comparison complete', comparisons=comparisons, margins=margins)
    return {'N': n, 'passed': passed, 'method': 'exact integer intervals at scale10^65; rational series and isqrt',
            'pi_interval': pi.strings(), 'values': state['values'], 'interval_count': len(values),
            'domains': domains, 'controls': controls, 'primary_contains_independent': comparisons,
            'margins': margins, 'primary': identity(PRIMARY), 'source': identity(Path(__file__).resolve()),
            'python': sys.version, 'children': 0, 'native_or_phase_calls': 0,
            'completion_requires': 'observed EXIT0, passed=true, frozen source and primary pins unchanged'}


def main():
    assert sys.argv[1:] == ['--run-once']
    OUT.mkdir(parents=True, exist_ok=False)
    state = {'stage': 'independent attempt consumed; no scientific calculation yet'}
    try:
        freeze = check_pins()
        save(OUT/'preregistration.json', {'N': 1024, 'CPU_soft': 9, 'CPU_hard': 10,
             'scale_digits': 65, 'log_terms': TERMS, 'Machin_terms': [100,32], 'freeze_sha256': freeze,
             'source': identity(Path(__file__).resolve()), 'no_retry': True,
             'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})
        result = calculate(state)
        assert check_pins() == freeze
        result['freeze_sha256'] = freeze
        result['cpu_seconds_before_receipt'] = cpu()
        result['utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        assert result['cpu_seconds_before_receipt'] < 10
        save(OUT/'independent-1024.json', result)
        assert result['passed'], 'first independent scalar/control/comparison/margin failure; no retry'
        assert check_pins() == freeze
        print(json.dumps({'passed': True, 'N': 1024, 'gates': {k: result['values'][k] for k in ('GN','GB','GX','GY','GO')},
              'cpu_seconds_before_receipt': result['cpu_seconds_before_receipt'],
              'output': str(OUT/'independent-1024.json')}, sort_keys=True), flush=True)
        assert cpu() < 10
    except BaseException as error:
        save(OUT/'first-failure.json', {'N': 1024, 'first_failure': repr(error),
             'state': state, 'cpu_checkpoint': cpu(), 'no_retry': True})
        raise


if __name__ == '__main__':
    main()
