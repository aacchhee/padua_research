"""D26 sole prospective N4096 scalar gate; no phase or native oracle."""
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
OUT = ROOT/'local-output/argmax-bridge-20261105/post-audit-D26/budget'


def identity(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def cpu():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_utime+usage.ru_stime


def write_once(path, obj):
    data = (json.dumps(obj, sort_keys=True, indent=2, allow_nan=False)+'\n').encode()
    assert len(data) < 16384, 'whole receipt exceeds essential evidence cap'
    with path.open('xb') as stream:
        stream.write(data)


def check_freeze():
    freeze_path = HERE/'FREEZE.json'
    raw = freeze_path.read_bytes()
    assert len(raw) < 16384
    freeze = json.loads(raw)
    assert freeze['N'] == 4096 and freeze['CPU_hard'] == 5
    expected = {str(Path(__file__).resolve().relative_to(ROOT)),
                str(HELPER.relative_to(ROOT))}
    pins = freeze['code_data']
    assert len(pins) == 2 and {row['path'] for row in pins} == expected
    for row in pins:
        assert identity(ROOT/row['path']) == row, 'frozen code changed'
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def endpoint():
    raw = HELPER.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == HELPER_SHA
    wanted = {'directed', 'I', 'ilog', 'atan_bounds'}
    defs = [node for node in ast.parse(raw).body
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in wanted]
    assert len(defs) == 4 and {node.name for node in defs} == wanted
    env = {'D': D, 'localcontext': localcontext, 'ROUND_FLOOR': ROUND_FLOOR,
           'ROUND_CEILING': ROUND_CEILING, 'Q': Q, 'PREC': 50}
    exec(compile(ast.Module(body=defs, type_ignores=[]), str(HELPER), 'exec'), env)
    I, log, directed, atan = [env[key] for key in ('I', 'ilog', 'directed', 'atan_bounds')]

    def sqrt_interval(value):
        value = I.cast(value)
        assert value.a >= 0
        with localcontext() as ctx:
            ctx.prec = 50
            low = value.a.sqrt().next_minus()
            high = value.b.sqrt().next_plus()
        return I(low, high)

    al, au = atan(5, 70)
    bl, bu = atan(239, 20)
    pl, pu = 16*al-4*bu, 16*au-4*bl
    pi = I(directed(lambda: D(pl.numerator)/D(pl.denominator), ROUND_FLOOR),
           directed(lambda: D(pu.numerator)/D(pu.denominator), ROUND_CEILING))
    n = 4096
    m, one = n+1, I(1)
    half = one/2
    L = log(n)
    H, b, hr = 1+L, 4/(pi*pi), log(one*5/2)+one/18
    Dc = ((52/(pi*pi))*H+7)/n+10*one/(n*n)+20*H/(pi*n*n)
    KD = (352*H/(3*pi)+2/pi)/n
    MA = 1/pi+4/(pi*pi)
    g = 1+log(2+8*one*m/(3*pi))
    VB = 23+(3*g+14*log(m)+46+2*log(2))/pi
    Qg = (4*one/m)*(7+(2/pi)*(5+2*log(2*m)))
    Gg = (2*L*MA+VB)/(2*m)+6*L*MA/m+Qg+4*log(pi)/(pi*m)+16*one/m
    endpoint_rows = (181+19*L)/n+21600*one/(n*n)
    central_rows = (12+2*L)/n
    E6 = endpoint_rows+central_rows
    mesh = (b*(2*L+2*hr)/n+(4+b*(L+one/n))/(4*n*n-1)
            +b/(2*n-1)**2+(5+b*(log(n+half)+2))/(4*(n-half)**2))
    W = (3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
    Cnew = Dc+Gg+E6+mesh+W
    G0 = ((28/(pi*pi))*L+one*111/2+23/pi)/m
    E0 = Dc+G0+mesh+14*one/n+71*one/(n*n)
    T = (4*L*L-3*L)/(pi*pi)
    u0, s0, far_coefficient = one*191/6144, sqrt_interval(one*191/768), one*25/2
    phase_charge = KD*s0
    far_allowance = Cnew+phase_charge
    far_margin = u0*(T-far_coefficient)
    far_gate = far_margin-far_allowance-E0
    controls = {
        'sole_natural_barrier': n == 2**12,
        'paper_log_lower': 12*Q(69,100) == Q(207,25) and Q(207,25) > 8,
        'paper_T_lower': (4*Q(207,25)**2-3*Q(207,25))/10 == Q(155871,6250),
        'T_minus_new_coefficient': Q(155871,6250) > Q(25,2),
        'D24_inner_strip': Q(59,20) < Q(25,2)*Q(61,256),
        'D24_outer_region': Q(6211,7260) < Q(25,2)*Q(2277,32768),
        'endpoint_constant': 4+3*59 == 181,
        'endpoint_log': 1+3*6 == 19,
        'endpoint_inverse_square': 3*200*4*9 == 21600,
        'six_row_constant': 181+12 == 193,
        'six_row_log': 19+2 == 21,
        'central_sine': 1-Q(10,8*33*33) > Q(99,100),
        'central_V': Q(400,99) < Q(9,2),
        'origin_D0': Q(8,3)+Q(1,2)*Q(6,5) < 4,
        'origin_Z': 4+Q(1,2*32) < 5}
    values = {'L': L, 'H': H, 'b': b, 'hr': hr, 'D': Dc, 'KD': KD,
              'MA': MA, 'g': g, 'VB': VB, 'Qg': Qg, 'Gg': Gg,
              'endpoint_rows': endpoint_rows, 'central_rows': central_rows,
              'E6': E6, 'mesh': mesh, 'W': W, 'Cnew': Cnew,
              'G0': G0, 'E0': E0, 'T': T, 'u0': u0, 's0': s0,
              'far_coefficient': far_coefficient, 'phase_charge': phase_charge,
              'far_allowance': far_allowance, 'far_margin': far_margin,
              'far_gate': far_gate}
    return {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
            'controls': controls,
            'values': {key: [str(value.a), str(value.b)] for key, value in values.items()},
            'pi_interval': [str(pi.a), str(pi.b)],
            'passed': all(controls.values()) and T.a > D('12.5') and far_gate.a > 0,
            'source': identity(Path(__file__).resolve()), 'helper': identity(HELPER),
            'python': sys.version, 'decimal_library': decimal.__libmpdec_version__,
            'children': 0, 'native_or_phase_calls': 0,
            'scope': 'Sole fixed4096 scalar gate; all-n mathematics and independent fresh review remain separate',
            'completion_requires': 'Observed process exit0 as well as passed=true and unchanged published freeze'}


def main():
    assert sys.argv[1:] == ['--run-once'], 'only frozen explicit one-shot command'
    OUT.mkdir(parents=True, exist_ok=False)  # Permanent one-attempt lock, including failure.
    try:
        freeze = check_freeze()
        write_once(OUT/'preregistration.json', {
            'N': 4096, 'CPU_soft': 4, 'CPU_hard': 5, 'children': 0,
            'precision': 50, 'freeze': freeze, 'source': identity(Path(__file__).resolve()),
            'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'no_retry': True})
        result = endpoint()
        assert check_freeze() == freeze, 'freeze changed during endpoint'
        result['freeze'] = freeze
        result['cpu_seconds_before_receipt'] = cpu()
        result['utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        assert result['cpu_seconds_before_receipt'] < 5
        write_once(OUT/'budget-4096.json', result)
        if not result['passed']:
            raise ArithmeticError('first fixed4096 gate/control failure; no retry')
        assert check_freeze() == freeze, 'freeze changed before completion'
        print(json.dumps({'N': result['N'], 'passed': result['passed'],
                          'far_gate': result['values']['far_gate'],
                          'cpu_seconds_before_receipt': result['cpu_seconds_before_receipt'],
                          'output': str(OUT/'budget-4096.json')}, sort_keys=True), flush=True)
        assert cpu() < 5, 'CPU cap after output; exit0 required'
    except BaseException as error:
        write_once(OUT/'first-failure.json', {
            'N': 4096, 'first_failure': repr(error), 'CPU_checkpoint': cpu(),
            'no_retry': True, 'scope': 'Failed primary; retained directory consumes sole attempt'})
        raise


if __name__ == '__main__':
    main()
