"""D37 sole fixed N1024 five-gate endpoint; no phase/native/rootfinder call."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (4, 5))
import ast
import decimal
import hashlib
import json
import sys
import time
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
TOPIC = HERE.parents[1]
HELPER = TOPIC/'code/post_audit_D06_model_budget/evaluate.py'
HELPER_SHA = '9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413'
OUT = ROOT/'local-output/argmax-bridge-20261105/post-audit-D37/budget'


def identity(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def cpu():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_utime+usage.ru_stime


def write_once(path, obj):
    data = (json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode()
    assert len(data) < 16384, 'whole receipt exceeds essential evidence cap'
    with path.open('xb') as stream:
        stream.write(data)


def check_freeze():
    data = (HERE/'FREEZE.json').read_bytes()
    assert len(data) < 16384
    freeze = json.loads(data)
    assert freeze['N'] == 1024 and freeze['CPU_hard'] == 5
    expected = {str(Path(__file__).resolve().relative_to(ROOT)), str(HELPER.relative_to(ROOT))}
    pins = freeze['code_data']
    assert len(pins) == 2 and {row['path'] for row in pins} == expected
    for row in pins:
        assert identity(ROOT/row['path']) == row, 'frozen code changed'
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def endpoint(state):
    raw = HELPER.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == HELPER_SHA
    wanted = {'directed', 'I', 'ilog', 'atan_bounds'}
    nodes = [node for node in ast.parse(raw).body
             if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in wanted]
    assert len(nodes) == 4 and {node.name for node in nodes} == wanted
    env = {'D': D, 'localcontext': localcontext, 'ROUND_FLOOR': ROUND_FLOOR,
           'ROUND_CEILING': ROUND_CEILING, 'Q': Q, 'PREC': 50}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(HELPER), 'exec'), env)
    I, log, directed, atan = [env[key] for key in ('I', 'ilog', 'directed', 'atan_bounds')]

    def sqrt_interval(value):
        value = I.cast(value)
        assert value.a >= 0
        with localcontext() as ctx:
            ctx.prec = 50
            low = value.a.sqrt().next_minus()
            high = value.b.sqrt().next_plus()
        return I(low, high)

    def psi(B, q, k):
        B, q, k = I.cast(B), I.cast(q), I.cast(k)
        assert B.a >= 0 and q.a > 0 and k.a >= 0
        z = (3*B+sqrt_interval(9*B*B+32*q*k))/(8*q)
        return z, (B/4)*z*z*z+(k/2)*z*z

    al, au = atan(5, 70)
    bl, bu = atan(239, 20)
    pl, pu = 16*al-4*bu, 16*au-4*bl
    pi = I(directed(lambda: D(pl.numerator)/D(pl.denominator), ROUND_FLOOR),
           directed(lambda: D(pu.numerator)/D(pu.denominator), ROUND_CEILING))
    n = 1024
    m, one = n+1, I(1)
    half = one/2
    L, H = log(n), 1+log(n)
    b, hr = 4/(pi*pi), log(one*5/2)+one/18
    Dc0 = ((52/(pi*pi))*H+7)/n+10*one/(n*n)+20*H/(pi*n*n)
    KD35 = ((6+16/(3*pi))*H+2/pi)/n
    MA = 1/pi+4/(pi*pi)
    gpar = 1+log(2+8*one*m/(3*pi))
    VB = 23+(3*gpar+14*log(m)+46+2*log(2))/pi
    Qg = (4*one/m)*(7+(2/pi)*(5+2*log(2*m)))
    Gg = (2*L*MA+VB)/(2*m)+6*L*MA/m+Qg+4*log(pi)/(pi*m)+16*one/m
    endpoint_old = (181+19*L)/n+21600*one/(n*n)
    central_old = (12+2*L)/n
    E6old = endpoint_old+central_old
    mesh = (b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n*n-1)
            +b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2))
    W = (3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
    Cnew = Dc0+Gg+E6old+mesh+W
    G0 = ((28/(pi*pi))*L+one*111/2+23/pi)/m
    E0 = Dc0+G0+mesh+14*one/n+71*one/(n*n)
    T = (4*L*L-3*L)/(pi*pi)
    V = T-E0
    CN = 22*one/n+162*one/(n*n)+40*H/(pi*n*n)
    KN = (8*H+one*39*L/2+one*286/3)/n+4*one/(n*n)
    CW = 23*one/n+204*one/(n*n)+40*H/(pi*n*n)
    KW = (8*H+20*L+one*292/3)/n+4*one/(n*n)
    qNx, qNy = one*47*V/192-one*89/72, one*47*V/192-one*23/24
    qBx, qBy = one*47*V/192-one*53/40, one*47*V/192-one*119/120
    qLx, qLy = one*11*V/48-one*53/40, one*11*V/48-one*119/120
    sqrt2 = sqrt_interval(2)
    tail_x = qLx-3*one/(2*sqrt2)-KW
    tail_y = qLy-3*one/(20*sqrt2)-KW
    values = {'L': L, 'H': H, 'b': b, 'hr': hr, 'D': Dc0, 'KD35': KD35,
              'MA': MA, 'gpar': gpar, 'VB': VB, 'Qg': Qg, 'Gg': Gg,
              'endpoint_old': endpoint_old, 'central_old': central_old, 'E6old': E6old,
              'mesh': mesh, 'W': W, 'Cnew': Cnew, 'G0': G0, 'E0': E0,
              'T': T, 'V': V, 'CN': CN, 'KN': KN, 'CW': CW, 'KW': KW,
              'qNx': qNx, 'qNy': qNy, 'qBx': qBx, 'qBy': qBy, 'qLx': qLx, 'qLy': qLy,
              'sqrt2': sqrt2, 'tail_x': tail_x, 'tail_y': tail_y}
    state['stage'] = 'quadratic and monotone-tail domain checks'
    state['partial_values'] = {key: [str(v.a), str(v.b)] for key, v in values.items()}
    domains = {'V_positive': V.a > 0, 'KN_nonnegative': KN.a >= 0, 'KW_nonnegative': KW.a >= 0,
               'CN_nonnegative': CN.a >= 0, 'CW_nonnegative': CW.a >= 0,
               'Cnew_nonnegative': Cnew.a >= 0, 'E0_nonnegative': E0.a >= 0, 'KD35_nonnegative': KD35.a >= 0,
               **{key+'_positive': values[key].a > 0 for key in ('qNx','qNy','qBx','qBy','qLx','qLy')},
               'tail_x_positive': tail_x.a > 0, 'tail_y_positive': tail_y.a > 0}
    state['domains'] = domains
    assert all(domains.values()), 'first fixed1024 quadratic/tail domain failure'
    zNx, pNx = psi(one*77/96, qNx, KN)
    zNy, pNy = psi(one/12, qNy, KN)
    zBx, pBx = psi(one, qBx, KW+half)
    zBy, pBy = psi(one/10, qBy, KW+half)
    zLx, pLx = psi(one, qLx, KW)
    zLy, pLy = psi(one/10, qLy, KW)
    Ex, Ey = one/(2*sqrt2)-qLx/4+KW/2, one/(20*sqrt2)-qLy/4+KW/2
    floor, eta, u1 = one*3/50, half, one*47/384
    Dc, s1 = one*6211/7260, sqrt_interval(one*47/48)
    GN = floor-CN-pNx-pNy
    GB = one/4-CW-pBx-pBy
    GX, GY = -CW-Ex-pLy, -CW-Ey-pLx
    GO = u1*T-Dc-Cnew-KD35*s1-E0
    gates = {'GN': GN, 'GB': GB, 'GX': GX, 'GY': GY, 'GO': GO}
    minimum = I(min(v.a for v in gates.values()), min(v.b for v in gates.values()))
    values.update({'zNx': zNx, 'PsiNx': pNx, 'zNy': zNy, 'PsiNy': pNy,
                   'zBx': zBx, 'PsiBx': pBx, 'zBy': zBy, 'PsiBy': pBy,
                   'zLx': zLx, 'PsiLx': pLx, 'zLy': zLy, 'PsiLy': pLy,
                   'Ex': Ex, 'Ey': Ey, 'floor': floor, 'eta': eta, 'u1': u1, 'Dc': Dc, 's1': s1,
                   **gates, 'minimum_gate': minimum})
    controls = {
        'fixed_1024': n == 2**10,
        'paper_log': 10*Q(69,100) == Q(69,10) and 10*Q(7,10) == 7,
        'paper_T': (4*Q(69,10)**2-3*Q(69,10))/10 == Q(8487,500),
        'near_constant': 4+18 == 22 and 20+142 == 162,
        'wide_constant': 4+19 == 23 and 20+184 == 204,
        'near_K_constant': 10+8+Q(7,3)+75 == Q(286,3),
        'near_K_log': 1+1+Q(35,2) == Q(39,2),
        'wide_K_constant': 10+12+Q(7,3)+73 == Q(292,3),
        'wide_K_log': 1+1+18 == 20,
        'wide_qx': Q(19,24)+Q(8,15) == Q(53,40),
        'wide_qy': Q(19,24)+Q(3,2)*Q(2,15) == Q(119,120),
        'wide_Bx': Q(3,5)+Q(3,4)*Q(8,15) == 1,
        'wide_By': Q(3,4)*Q(2,15) == Q(1,10),
        'fixed_multiplier': Q(1,2)*Q(1,2) == Q(1,4),
        'box_cosine': Q(1,4)-Q(1,192) == Q(47,192),
        'large_cosine': Q(1,4)-Q(1,48) == Q(11,48),
        'floor_nearest': 183*45 < 14336,
        'floor_small_angle': Q(1763685,28114944) > Q(3,50),
        'floor_middle_margin': Q(1617,24200)-Q(1,200)-Q(3,50) == Q(11,6050),
        'floor_middle_losses': Q(2945,628) < Q(19,4) and Q(19,4096) < Q(24,5000)
                               and Q(550,3*n*n) < Q(1,5000),
        'scalar_W_bounds': Q(160,189) < 1 and Q(6400,3969) < Q(5,3)
                           and Q(189440,83349) < Q(7,3) and Q(5701632,1750329) < Q(10,3)
                           and Q(1340866560,183784545) < Q(15,2),
        'scalar_f4': Q(299,16)*Q(8,25) == Q(299,50) and Q(299,50) < 6,
        'scalar_H': Q(93696,312500)+Q(1539,51200) < Q(1,3),
        'central_short_and_shift': Q(5120,9653) < Q(8,15) and Q(1280,9653) < Q(2,15),
        'central_fractional': Q(5760,9653) < Q(3,5),
        'origin_D0': Q(8,3)+Q(1,2)*Q(6,5) < 4,
        'origin_Z': 4+Q(1,64) < 5,
        'old_global_endpoint': 4+3*59 == 181 and 1+3*6 == 19,
        'old_global_six': 181+12 == 193 and 19+2 == 21,
        'outer_root': 8*Q(47,384) == Q(47,48),
        'outer_cosine': Q(1,8)-Q(1,384) == Q(47,384),
        'uniform_Dc': Q(8,3)-Q(4383,2420) == Q(6211,7260),
        'paper_tail_domain': Q(8487,500)-Q(1,4) == Q(4181,250)
                              and Q(30091,12000) > 2 > Q(15,14)+Q(1,3)}
    state['stage'] = 'all five fixed1024 gates completed'
    state['partial_values'] = {key: [str(v.a), str(v.b)] for key, v in values.items()}
    state['controls'] = controls
    return {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
            'domains': domains, 'controls': controls, 'interval_count': len(values),
            'values': state['partial_values'], 'pi_interval': [str(pi.a), str(pi.b)],
            'passed': all(domains.values()) and all(controls.values()) and all(v.a > 0 for v in gates.values()),
            'source': identity(Path(__file__).resolve()), 'helper': identity(HELPER),
            'python': sys.version, 'decimal_library': decimal.__libmpdec_version__,
            'children': 0, 'native_or_phase_calls': 0,
            'scope': 'ONE fixed1024 five-gate sufficient endpoint; all-n proof and independent result review remain separate',
            'completion_requires': 'Observed process exit0 plus passed=true and unchanged published source/freeze'}


def main():
    assert sys.argv[1:] == ['--run-once'], 'only explicit frozen one-shot command'
    OUT.mkdir(parents=True, exist_ok=False)
    state = {'stage': 'exclusive attempt consumed before helper execution'}
    try:
        freeze = check_freeze()
        write_once(OUT/'preregistration.json', {
            'N': 1024, 'CPU_soft': 4, 'CPU_hard': 5, 'children': 0,
            'precision': 50, 'freeze': freeze, 'source': identity(Path(__file__).resolve()),
            'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'no_retry': True})
        result = endpoint(state)
        assert check_freeze() == freeze, 'freeze changed during endpoint'
        result['freeze'] = freeze
        result['cpu_seconds_before_receipt'] = cpu()
        result['utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        assert result['cpu_seconds_before_receipt'] < 5
        write_once(OUT/'budget-1024.json', result)
        if not result['passed']:
            raise ArithmeticError('first fixed1024 gate/control failure; no retry')
        assert check_freeze() == freeze, 'freeze changed before completion'
        print(json.dumps({'N': 1024, 'passed': result['passed'],
                          'gates': {k: result['values'][k] for k in ('GN','GB','GX','GY','GO')},
                          'cpu_seconds_before_receipt': result['cpu_seconds_before_receipt'],
                          'output': str(OUT/'budget-1024.json')}, sort_keys=True), flush=True)
        assert cpu() < 5, 'CPU cap after output; observed exit0 required'
    except BaseException as error:
        write_once(OUT/'first-failure.json', {'N': 1024, 'first_failure': repr(error),
                                             'state': state, 'CPU_checkpoint': cpu(), 'no_retry': True})
        raise


if __name__ == '__main__':
    main()
