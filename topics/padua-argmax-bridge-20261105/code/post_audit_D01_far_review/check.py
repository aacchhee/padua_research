#!/usr/bin/env python3
"""Focused independent D01 check; every numerical conclusion is MEASURED.

Two n=512 cases only. Reuse the hash-verified native artifact; independently
sum the original finite polynomial and separate cotangent norms in long
double. This is not a fresh native build or an interval proof.
"""
import resource
import time

START = time.process_time()
WALL = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (38, 38))
import ctypes
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys
import mpmath as mp
import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
ROOT = HERE.parents[3]
RAW = ROOT / 'local-output/argmax-bridge-20261105/post-audit-D01/far-review-01'
OUT = TOPIC / 'evidence/d01-review-far.json'
assert not OUT.exists(), 'Preserve previous review execution'
RAW.mkdir(parents=True, exist_ok=False)


def identity(p):
    p = Path(p).resolve()
    data = p.read_bytes()
    return dict(path=str(p), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def verify(record):
    assert identity(record['path']) == record, record['path']


prior_path = TOPIC / 'evidence/d01-far.json'
prior = json.loads(prior_path.read_text())
manifest = json.loads(Path(prior['raw_manifest']['path']).read_text())
verify(prior['raw_manifest'])
verify(prior['binary'])
for record in prior['sources']:
    verify(record)
for key in ['source_snapshot', 'preprocessed_translation_unit', 'instrumentation']:
    verify(manifest[key])
for record in manifest['frozen_inputs'] + manifest['actual_loaded_before']:
    verify(record)

# Reconstruct and byte-compare the assignment-only instrumentation.
point_path = TOPIC / 'code/cheap_rows_C11/point.cpp'
partial_path = TOPIC / 'code/cheap_rows_C11/partial.cpp'
generated = point_path.read_text().replace(
    '#include "partial.cpp"',
    '#include "' + str(partial_path) + '"\nstatic std::vector<B>* d01_capture=nullptr;')
changes = [
    ('total=total+absolute(finiteF(n,r,k,af,bf));stats.retained++;',
     'total=total+absolute(finiteF(n,r,k,af,bf));if(d01_capture)(*d01_capture)[r]=(*d01_capture)[r]+absolute(finiteF(n,r,k,af,bf));stats.retained++;'),
    ('total=total+row;', 'total=total+row;if(d01_capture)(*d01_capture)[r]=row;')]
for old, new in changes:
    assert generated.count(old) == 1
    generated = generated.replace(old, new)
assert generated == Path(manifest['instrumentation']['path']).read_text()

model_path = TOPIC / 'code/post_audit_D01_far/model.py'
spec = importlib.util.spec_from_file_location('reviewed_model', model_path)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
lib = ctypes.CDLL(prior['binary']['path'])
ptr = ctypes.POINTER(ctypes.c_double)
rows = lib.d01_rows
rows.argtypes = [ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ptr, ptr]
poles = lib.d01_poles
poles.argtypes = [ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ptr,
                  ctypes.POINTER(ctypes.c_int)]
point = lib.c07_point
point.argtypes = [ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p, ptr,
                  ctypes.POINTER(ctypes.c_long)]

LD = np.longdouble
PI = np.arccos(LD(-1))


def ldq(q):
    return LD(str(q.numerator)) / LD(str(q.denominator))


def sinc(x):
    result = np.ones_like(x)
    np.divide(np.sin(x), x, out=result, where=x != 0)
    return result


def ratio(turn, degree):
    turns = np.floor(turn + LD('.5')).astype(np.int64)
    reduced = PI * (turn - turns)
    sign = 1 - 2 * ((turns * (degree - 1)) % 2)
    return degree * sign * sinc(degree * reduced) / sinc(reduced)


def direct(n, af, bf):
    m = n + 1
    alpha, beta = PI * ldq(af), PI * ldq(bf)
    p, q = np.sin(alpha), np.sin(beta)
    a = LD(0) if af + bf == 1 else (np.cos(alpha) + np.cos(beta)) / 2
    all_rows = np.zeros(2*m, dtype=LD)
    all_poles = np.zeros(2*m, dtype=LD)
    kinds = np.zeros(2*m, dtype=np.int32)
    for r in range(2*m):
        parity = (1-r) % 2
        vf = (Fraction(r) + bf) / m
        sigma = (parity + af) / 2
        ym, yp = sigma - n*vf/2, sigma + n*vf/2
        collision = ym.denominator == 1 or yp.denominator == 1
        kinds[r] = 1 if r < 64 or r >= 2*m-64 else 2 if collision else 3 if r in [m-1, m] else 0
        u = (2*np.arange(n, dtype=LD) + parity + ldq(af)) / n
        v = ldq(vf)
        plus, minus = (u+v)/2, (u-v)/2
        kernel = ratio(plus, m)*ratio(minus, m) + ratio(plus, n)*ratio(minus, n) - np.cos(PI*n*u)
        all_rows[r] = np.sum(np.abs(kernel), dtype=LD) / (2*n*m)
        if kinds[r] == 0:
            cv = 1/np.tan(PI*v/2)
            c, d = (p-q-2*a*cv)/4, (p+q+2*a*cv)/4
            norms = []
            for y in [ym, yp]:
                t = y - (y.numerator // y.denominator)
                norms.append(np.sum(np.abs(1/np.tan(PI*(np.arange(n, dtype=LD)+ldq(t))/n)), dtype=LD))
            all_poles[r] = (abs(c)*norms[0]+abs(d)*norms[1])/(n*m)
    return all_rows, all_poles, kinds


results = []
for phase in [2, 3]:
    start = time.process_time()
    old = next(x for x in prior['results'] if x['n'] == 512 and x['phase'] == phase)
    n, m = 512, 513
    af, bf = Fraction(old['alpha_pi']), Fraction(old['beta_pi'])
    astr, bstr = str(af).encode(), str(bf).encode()
    actual = np.zeros((2*m, 2))
    finite_poles = np.zeros_like(actual)
    total = np.zeros(2)
    kinds = np.zeros(2*m, dtype=np.int32)
    assert rows(n, astr, bstr, actual.ctypes.data_as(ptr), total.ctypes.data_as(ptr)) == 0
    assert poles(n, astr, bstr, finite_poles.ctypes.data_as(ptr), kinds.ctypes.data_as(ctypes.POINTER(ctypes.c_int))) == 0
    plain, counts = np.zeros(3), np.zeros(6, dtype=np.int64)
    assert point(n, astr, bstr, plain.ctypes.data_as(ptr), counts.ctypes.data_as(ctypes.POINTER(ctypes.c_long))) == 0
    assert np.array_equal(total, plain[:2])
    dr, dp, dk = direct(n, af, bf)
    assert np.array_equal(dk, kinds)
    row_mid = actual.astype(LD).mean(axis=1)
    pole_mid = finite_poles.astype(LD).mean(axis=1)
    row_error = float(np.max(abs(dr-row_mid)))
    pole_error = float(np.max(abs(dp-pole_mid)))
    assert row_error < 1e-10 and pole_error < 1e-10
    assert total.tolist() == old['S']
    alpha, beta = float(af)*math.pi, float(bf)*math.pi
    pr = model.profile(alpha, beta, math.log(n), af+bf == 1, eps=3e-12)
    L = math.log(n)
    ordinary = np.where(kinds == 0)[0]
    vv = (ordinary + float(bf))*math.pi/m
    assert min(np.minimum(vv, 2*math.pi-vv)) > .01
    aval = np.array([model.A(v, pr) for v in vv])
    bval = np.array([model.B(v, alpha, beta, pr) for v in vv])
    cancellation = np.array([model.old.J(pr['p']/2, abs(pr['q']/2+pr['a']/math.tan(v/2)), min(v, abs(v-math.pi), 2*math.pi-v))/math.pi for v in vv])
    # Reconstruct the telescope using independent direct finite sums.
    cc = dict(endpoint_actual_minus_sinc=float(sum(dr[kinds == 1]))-pr['endpoint_rows'],
              mesh=-(pr['B0']*L**2+pr['b_end']*L+pr['mesh_constant']),
              collision=float(sum(dr[kinds == 2])), central=float(sum(dr[kinds == 3])),
              ordinary_interior_quadrature=math.fsum(aval*L+bval)/m-(pr['integral_A']*L+pr['integral']),
              E=float(sum(dr[ordinary]-dp[ordinary]))-math.fsum(cancellation)/m,
              D=float(sum(dp[ordinary]))-math.fsum(aval*L+bval-cancellation)/m, Q=0.)
    diff = float(sum(dr))-pr['value']
    closure = math.fsum(cc.values())-diff
    assert abs(closure) < 2e-12
    max_component_error = max(abs(cc[k]-old['components'][k]) for k in cc)
    assert max_component_error < 1e-9
    np.savez(RAW/f'n512-p{phase}.npz', actual=actual, native_poles=finite_poles,
             direct_rows=dr, direct_poles=dp, kinds=kinds)
    results.append(dict(n=n, phase=phase, alpha_pi=str(af), beta_pi=str(bf),
        S_native=total.tolist(), S_direct=float(sum(dr)),
        direct_vs_native_total=float(sum(dr)-sum(total.astype(LD))/2),
        max_direct_vs_native_row=row_error, max_direct_vs_native_pole=pole_error,
        native_row_radius_max=float(np.max(actual[:, 1]-actual[:, 0])/2),
        native_pole_radius_max=float(np.max(finite_poles[:, 1]-finite_poles[:, 0])/2),
        matched_unchanged_point_total=True, exact_rational_classification_matches=True,
        class_counts={str(k): int(np.sum(kinds == k)) for k in range(4)},
        endpoint_ordinary_rows=0, n1_strip_admissible=False,
        tighter_model=pr['value'], model_constant=pr['constant'],
        quadrature_warnings=pr['warnings'], components_direct=cc,
        max_component_difference_from_author=max_component_error,
        telescope_closure=closure, S_minus_M=diff, cpu_seconds=time.process_time()-start))

mp.mp.dps = 60
eps = mp.mpf(1)/(200*mp.pi)
cr = (2/mp.pi)*mp.fsum(1/(mp.mpf(k)+mp.mpf('.5')) for k in range(64))
mesh = (2/mp.pi)*(mp.log(mp.mpf('.01')/mp.pi)-mp.digamma(mp.mpf('64.5')))
integral = 2/mp.pi*mp.quad(lambda t: -mp.digamma(t)-mp.digamma(1-t)-2*mp.log(mp.pi), [eps, mp.mpf('.1'), mp.mpf('.5')])
constant = cr+mesh+integral
gamma_constant = 2/mp.pi*(mp.euler+mp.log(8/mp.pi))
bias_series = 4/mp.pi*((mp.euler-mp.log(mp.pi))*eps+mp.fsum(mp.zeta(2*k+1)*eps**(2*k+1)/(2*k+1) for k in range(1, 12)))
assert abs(gamma_constant-constant-bias_series) < mp.mpf('1e-55')
N = 512*513
xx = (np.arange(N, dtype=LD)+LD('.5'))*PI/(2*N)
exact_sum_measured = np.sum(1/np.tan(xx), dtype=LD)/N
leading = 2/mp.pi*(mp.log(N)+mp.euler+mp.log(8/mp.pi))
finite_error = mp.mpf(str(exact_sum_measured))-leading
remainder_bound = mp.mpf(1)/(4*N*N)
assert abs(finite_error) < remainder_bound
midpoint_control = dict(bias=str(bias_series), R_cancel_residual=str(cr+mesh-(2/mp.pi)*(-mp.digamma(mp.mpf('.5'))+mp.log(mp.mpf('.01')/mp.pi))),
    integral_constant=str(constant), high_precision_series_difference=str(gamma_constant-constant-bias_series),
    n=512, N=N, finite_cotangent_sum=str(exact_sum_measured), finite_error=str(finite_error), finite_remainder_bound=str(remainder_bound),
    author_asymptotic_oracle_discrepancy=next(x for x in prior['results'] if x['n']==512 and x['phase']==3)['boundary_oracle_discrepancy'])

# Independent high precision Stieltjes constants check the EM tail formula.
g_controls = []
af = Fraction(next(x for x in prior['results'] if x['n']==512 and x['phase']==2)['beta_pi'])
for tq in [af, 1-af]:
    t = mp.mpf(tq.numerator)/tq.denominator
    x, lx = 64+t, mp.log(64+t)
    em = -lx**2/2+lx/(2*x)+mp.fsum(mp.bernoulli(2*j)/(2*j)*(lx-mp.harmonic(2*j-1))/x**(2*j) for j in range(1, 7))
    true = mp.stieltjes(1, x)
    C = mp.fsum(math.comb(12, k)*abs(mp.bernoulli(k)) for k in range(13))
    bound = C*x**(-12)*((lx+mp.harmonic(12))/12+mp.mpf(1)/144)
    assert abs(em-true) < bound
    binary, binary_bound = model.g_R(float(tq))
    g_controls.append(dict(t=str(tq), high_precision_EM_error=str(em-true), remainder_bound=str(bound),
        binary64_error=str(mp.mpf(binary)-true), binary64_bound=binary_bound))

loaded_paths = {str(Path(line.split()[-1]).resolve()) for line in Path('/proc/self/maps').read_text().splitlines() if line.split()[-1].startswith('/')}
loaded = []
for record in manifest['actual_loaded_before']:
    assert str(Path(record['path']).resolve()) in loaded_paths
    verify(record)
    loaded.append(record)

receipt = dict(status='MEASURED', role='distinct supplementary review; formal Claude audit separate',
    rules_input_head='e6549177fe48c7fea8436cece8a04b411dc544e1',
    requested_model_effort='gpt-6-astra xhigh; serving model/effort metadata not independently exposed',
    command='python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_far_review/check.py',
    source=identity(__file__), author_receipt=identity(prior_path), native_binary=prior['binary'],
    source_controls=dict(assignment_only_instrumentation_matches=True, source_snapshot_and_preprocessed_TU_hashes_verified=True,
                         native_loaded_closure=loaded, independently_rebuilt=False),
    versions=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, mpmath=mp.__version__,
                  longdouble_epsilon=str(np.finfo(LD).eps)),
    results=results, midpoint=midpoint_control, g_R=g_controls,
    raw=[identity(p) for p in sorted(RAW.glob('*.npz'))],
    cpu_seconds=time.process_time()-START, wall_seconds=time.monotonic()-WALL,
    cpu_scope='Current Python process from before imports; no build or child process. 38 CPU-second process limit; review authorization 40 CPU seconds.',
    limitation='Native artifact reused after hash and loaded-closure checks. Long-double finite sums and mpmath/Scipy calculations are diagnostics, not enclosures. Two even n512 cases only; no new odd-degree or collision execution; full Python package trees not pinned.')
OUT.write_text(json.dumps(receipt, indent=2, allow_nan=False)+'\n')
assert OUT.stat().st_size < 16384
print(json.dumps(dict(output=identity(OUT), cpu_seconds=time.process_time()-START,
                     cases=[(r['n'], r['phase']) for r in results],
                     max_component_difference=max(r['max_component_difference_from_author'] for r in results))))
