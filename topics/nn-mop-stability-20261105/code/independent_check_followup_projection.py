#!/usr/bin/env python3
"""Exact moment checks against committed projection data, never /tmp replay.

The frozen target arrays and rational witnesses are inputs. No call to the
fit producer creates the comparison target. Exact moments, objectives and
N4 gradients use the separate defining-system implementation.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
from independent_check_moments import direct, inputs, FIELDS

HERE = Path(__file__).resolve().parent
REFERENCE = HERE.parent/'evidence/projection-reference.json'
REFERENCE_SHA256 = '37c3c060ad42cad679a78f256d9a5bdf5c129ed338cc8dcda9afbae6a5fef23f'


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def near(a, b):
    require(abs(a-b) <= 1e-12*max(abs(a), abs(b), 1e-100), 'reported metric mismatch')


def case(record):
    N, family, method = record['N'], record['family'], record['method']
    stored, witness = record['raw_coefficients'], record['rational_input']
    require(digest(stored) == record['raw_sha256'], 'raw array identity mismatch')
    require(digest(witness) == record['rational_input_sha256'], 'witness identity mismatch')
    raw = {tuple(row['nu']): {f: Q(float.fromhex(row[f])) for f in FIELDS} for row in stored}
    expected = {(n, k-n) for k in range(N) for n in range(k+1)}
    require(len(stored) == len(expected) and set(raw) == expected, 'raw triangle coverage mismatch')
    x = list(map(Q, witness['nodes']))
    w = [list(map(Q, row)) for row in witness['normalized_weights']]
    require(len(x) == N and len(w) == 2 and all(len(row) == N for row in w), 'input dimensions')
    require(all(x[i] < x[i+1] for i in range(N-1)), 'nodes not ordered')
    require(all(a > 0 for row in w for a in row) and all(sum(row) == 1 for row in w), 'mass/positivity')
    gradient_check = N == 4
    c, jac = direct(x, w, gradient_check)
    x0, w0 = inputs(N, family)
    w0 = [[a/sum(row) for a in row] for row in w0]
    truth, _ = direct(x0, w0, False)
    scale = {f: max(abs(row[f]) for row in truth.values()) for f in FIELDS}
    residual, chart = [], []
    for nu in c:
        for f in FIELDS:
            residual.append((raw[nu][f]-c[nu][f])/scale[f])
            if gradient_check:
                g = jac[nu][f]
                row = [a/scale[f] for a in g[:N]]
                for s in range(2):
                    avg = sum(w[s][i]*g[(s+1)*N+i] for i in range(N))
                    row.extend(w[s][i]*(g[(s+1)*N+i]-avg)/scale[f] for i in range(N-1))
                chart.append(row)
    cost = sum(a*a for a in residual)
    data = max(max(abs(a-b) for a, b in zip(x, x0)),
               max(abs(a-b)/b for row, old in zip(w, w0) for a, b in zip(row, old)))
    correction = max(map(abs, residual))
    metrics = record['metrics']
    near(float(data), metrics['input_mixed_sup'])
    near(float(correction), metrics['full_coefficient_correction'])
    for f in FIELDS:
        value = max(abs(raw[nu][f]-c[nu][f]) for nu in c)/scale[f]
        near(float(value), metrics['fields'][f])
    with mp.workdps(180):
        spd = mp.sqrt(mp.mpf(cost.numerator)/cost.denominator)
        near(float(spd), metrics['coefficient_SPD_norm'])
        stationarity = None
        if gradient_check:
            gradient = [sum(row[k]*a for row, a in zip(chart, residual)) for k in range(3*N-2)]
            frob2 = sum(a*a for row in chart for a in row)
            stationary2 = sum(a*a for a in gradient)/(cost*frob2)
            require(stationary2 < Q(1, 10**100), 'rounded N4 witness stationarity bound')
            stationarity = mp.sqrt(mp.mpf(stationary2.numerator)/stationary2.denominator)
            near(float(stationarity), metrics['returned_witness_scaled_stationarity'])
    return dict(N=N, family=family, method=method, full_array_entries=4*len(c),
        exact_normality_systems=(N+1)*(N+2)//2-1, positive_ordered_normalized=True,
        committed_witness_sha256=record['rational_input_sha256'], committed_raw_sha256=record['raw_sha256'],
        exact_moment_rebuild=True, N4_exact_gradient_checked=gradient_check,
        stationarity_float=float(stationarity) if stationarity is not None else None,
        input_units_u=float(data*2**53), correction_units_u=float(correction*2**53), SPD_norm=float(spd),
        exact_squared_SPD_hex_sha256=hashlib.sha256((hex(cost.numerator)+'/'+hex(cost.denominator)).encode()).hexdigest())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--reference', type=Path, default=REFERENCE)
    args = ap.parse_args()
    payload = args.reference.read_bytes()
    require(hashlib.sha256(payload).hexdigest() == REFERENCE_SHA256, 'committed reference SHA-256 mismatch')
    reference = json.loads(payload)
    require(reference['format'] == 'padua-projection-reference-v1', 'reference format')
    require(digest(reference['cases']) == reference['cases_sha256'], 'case payload identity')
    ids = [(r['family'], r['N'], r['method']) for r in reference['cases']]
    expected = [(f, N, m) for f in ('krawtchouk', 'hahn') for N in (4, 8) for m in ('c4', 'lu', 'nodeqr')]
    require(ids == expected, '12-case reference coverage/order mismatch')
    results = [case(row) for row in reference['cases']]
    print(json.dumps(dict(status='PASS', python=platform.python_version(), mpmath=mp.__version__,
        reference_sha256=REFERENCE_SHA256, reference_platform=reference['platform'],
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        independent_moment_code_sha256=hashlib.sha256((HERE/'independent_check_moments.py').read_bytes()).hexdigest(),
        scope='committed identities and independent exact reconstruction; no fit reproduction or global nearest certification',
        cases=results), indent=2, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
