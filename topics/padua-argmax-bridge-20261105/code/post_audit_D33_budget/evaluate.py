"""D33 sole fixed N2048 pair of D30 far gates; no near/phase/native calls."""
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
OUT = ROOT/'local-output/argmax-bridge-20261105/post-audit-D33/budget'


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
    assert freeze['N'] == 2048 and freeze['CPU_hard'] == 5
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
    n = 2048
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
    Cbase = Dc+Gg+mesh+W
    Cnew = Cbase+E6  # OLD GLOBAL six-row charge belongs to the OUTER case.
    G0 = ((28/(pi*pi))*L+one*111/2+23/pi)/m
    E0 = Dc+G0+mesh+14*one/n+71*one/(n*n)
    T = (4*L*L-3*L)/(pi*pi)
    A = 14*one/n+90*one/(n*n)
    Kinner = KD+(10+L)/n+4*one/(n*n)
    u0, ueta = one*191/6144, one*2277/32768
    s0, seta = sqrt_interval(one*191/768), sqrt_interval(one*2277/4096)
    inner_coefficient, outer_coefficient = I(11), one*25/2
    inner_row_charge = A*(1-u0)
    inner_phase_charge = Kinner*s0
    inner_allowance = Cbase+inner_row_charge+inner_phase_charge
    inner_margin = u0*(T-inner_coefficient)
    Fin = inner_margin-inner_allowance-E0
    outer_phase_charge = KD*seta
    outer_allowance = Cnew+outer_phase_charge
    outer_margin = ueta*(T-outer_coefficient)
    Fout = outer_margin-outer_allowance-E0
    minimum_gate = I(min(Fin.a,Fout.a),min(Fin.b,Fout.b))
    controls = {
        'sole_fixed_case': n == 2**11,
        'paper_log_lower': 11*Q(69,100) == Q(759,100) and Q(759,100) > 7,
        'paper_T_lower': (4*Q(759,100)**2-3*Q(759,100))/10 == Q(129789,6250),
        'T_minus_both_coefficients': Q(129789,6250) > Q(25,2) > 11,
        'inner_root_square': 8*Q(191,6144) == Q(191,768),
        'outer_root_square': 8*Q(2277,32768) == Q(2277,4096),
        'outer_cosine_lower': Q(9,128)-Q(81,98304) == Q(2277,32768),
        'wide_Dh_gaps': Q(19,8)-Q(7,33) > Q(17,8),
        'wide_reciprocal_sum': Q(64,289)*(2+Q(2,3)) == Q(512,867),
        'wide_displacement': Q(3584,2907) < Q(5,4),
        'wide_H_error': Q(77824,867) < 90,
        'wide_sine_error': Q(358400,42483) < 9,
        'wide_central_weight': Q(51200,11781) < Q(9,2),
        'wide_six_row_constant': 4+10 == 14 and 9+1 == 10,
        'inner_Young_determinant': Q(1,5)*Q(7,5)-Q(21,40)**2 == Q(7,1600),
        'inner_constant11': Q(729,280) < 11*Q(61,256),
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
              'E6old': E6, 'mesh': mesh, 'W': W, 'Cbase': Cbase, 'Cnew': Cnew,
              'G0': G0, 'E0': E0, 'T': T, 'A': A, 'Kinner': Kinner,
              'u0': u0, 'ueta': ueta, 's0': s0, 'seta': seta,
              'inner_coefficient': inner_coefficient, 'outer_coefficient': outer_coefficient,
              'inner_row_charge': inner_row_charge, 'inner_phase_charge': inner_phase_charge,
              'inner_allowance': inner_allowance, 'inner_margin': inner_margin, 'Fin': Fin,
              'outer_phase_charge': outer_phase_charge, 'outer_allowance': outer_allowance,
              'outer_margin': outer_margin, 'Fout': Fout, 'minimum_gate': minimum_gate}
    return {'N': n, 'status': 'DIRECTED_INTERVAL_UNDER_DECIMAL_CONTRACT',
            'controls': controls,
            'values': {key: [str(value.a), str(value.b)] for key, value in values.items()},
            'pi_interval': [str(pi.a), str(pi.b)],
            'passed': all(controls.values()) and T.a > D('12.5') and Fin.a > 0 and Fout.a > 0,
            'source': identity(Path(__file__).resolve()), 'helper': identity(HELPER),
            'python': sys.version, 'decimal_library': decimal.__libmpdec_version__,
            'children': 0, 'native_or_phase_calls': 0,
            'scope': 'Sole fixed2048 pair of FAR gates; all-n review and independent D31 NEAR result remain separate',
            'completion_requires': 'Observed process exit0 as well as passed=true and unchanged published freeze'}


def main():
    assert sys.argv[1:] == ['--run-once'], 'only frozen explicit one-shot command'
    OUT.mkdir(parents=True, exist_ok=False)  # Permanent one-attempt lock, including failure.
    try:
        freeze = check_freeze()
        write_once(OUT/'preregistration.json', {
            'N': 2048, 'CPU_soft': 4, 'CPU_hard': 5, 'children': 0,
            'precision': 50, 'freeze': freeze, 'source': identity(Path(__file__).resolve()),
            'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'no_retry': True})
        result = endpoint()
        assert check_freeze() == freeze, 'freeze changed during endpoint'
        result['freeze'] = freeze
        result['cpu_seconds_before_receipt'] = cpu()
        result['utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        assert result['cpu_seconds_before_receipt'] < 5
        write_once(OUT/'budget-2048.json', result)
        if not result['passed']:
            raise ArithmeticError('first fixed2048 gate/control failure; no retry')
        assert check_freeze() == freeze, 'freeze changed before completion'
        print(json.dumps({'N': result['N'], 'passed': result['passed'],
                          'Fin': result['values']['Fin'], 'Fout': result['values']['Fout'],
                          'cpu_seconds_before_receipt': result['cpu_seconds_before_receipt'],
                          'output': str(OUT/'budget-2048.json')}, sort_keys=True), flush=True)
        assert cpu() < 5, 'CPU cap after output; exit0 required'
    except BaseException as error:
        write_once(OUT/'first-failure.json', {
            'N': 2048, 'first_failure': repr(error), 'CPU_checkpoint': cpu(),
            'no_retry': True, 'scope': 'Failed primary; retained directory consumes sole attempt'})
        raise


if __name__ == '__main__':
    main()
