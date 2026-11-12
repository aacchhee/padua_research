#!/usr/bin/env python3
"""Supplemental D4 rerun and independent exact arithmetic cross-checks."""
import argparse, base64, hashlib, importlib.util, json, math, os, platform, sys, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

TOP = Path(__file__).resolve().parents[1]
CODE = TOP / 'code/fd4_certify.py'
PIN = '7e1ff950b5d26338fb0cd9bbbdd7d4bb605001cd4f274c628b5dd28926fa8750'

def identity(p):
    return {'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}

assert identity(CODE)['sha256'] == PIN
spec = importlib.util.spec_from_file_location('producer', CODE)
producer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(producer)

def load_nodes(path):
    data = json.loads(path.read_text())
    raw = base64.b85decode(data['coordinates_base85'])
    assert hashlib.sha256(raw).hexdigest() == data['coordinates_sha256']
    return np.frombuffer(raw, dtype='<f8').reshape(-1, 3).copy()

def exact_basis(point, n):
    tables = []
    for value in point:
        t = [F(1), F(float(value))]
        for k in range(1, n):
            t.append(2 * F(float(value)) * t[-1] - t[-2])
        tables.append(t)
    return [tables[0][a] * tables[1][b] * tables[2][c]
            for a in range(n + 1) for b in range(n + 1 - a) for c in range(n + 1 - a - b)]

def atan_interval(q, terms=80):
    partial = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(terms)), F(0))
    term = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(partial, partial+term), max(partial, partial+term)

def pi_interval():
    a, b = atan_interval(5)
    c, d = atan_interval(239)
    return 16*a - 4*d, 16*b - 4*c

def cosine_interval(lo, hi):
    # Taylor at midpoint; alternating tail after term 70 and |cos'| <= 1.
    x = (lo+hi)/2
    term = total = F(1)
    for k in range(1, 71):
        term *= -x*x / ((2*k-1)*(2*k))
        total += term
    error = abs(term*x*x/(141*142)) + (hi-lo)/2
    return total-error, total+error

def independent_mesh_check(n, m):
    plo, phi = pi_interval()
    grid, delta, cm = producer.mesh(n, m)
    scalars = grid[::(m*n+1)**2, 0]
    largest = F(0)
    for j, value in enumerate(scalars):
        lo, hi = cosine_interval(plo*j/(m*n), phi*j/(m*n))
        error = max(abs(F(float(value))-lo), abs(F(float(value))-hi))
        assert error <= delta
        largest = max(largest, error)
    lo, hi = cosine_interval(plo/(2*m), phi/(2*m))
    assert lo > 0 and cm >= 1/lo
    assert scalars[0] == 1 and scalars[-1] == -1
    return {'scalar_coordinates_checked': len(scalars),
            'method': 'Exact Machin atan alternating bounds (80 terms), cosine Taylor (71 terms), Lipschitz remainder',
            'coordinate_error_upper_display': float(largest),
            'delta_proved_by_exact_comparison': str(delta),
            'cm_upper_verified_without_mpmath': str(cm)}

def arithmetic_check(x, n, m, result):
    started = time.monotonic()
    N = len(x)
    A = producer.integer(producer.basis(x, n))
    W = producer.integer(np.linalg.inv(producer.basis(x, n)))
    bound = producer.beta(n)
    worst = F(0)
    for point, row in zip(x, A):
        for expected, actual in zip(exact_basis(point, n), row):
            err = abs(expected - F(int(actual), producer.S))
            assert err <= bound
            worst = max(worst, err)
    rows = list(range(N)) if n == 4 else sorted({0, 1, N//4, N//2, 3*N//4, N-2, N-1})
    product = producer.mul(A, W)
    for i in rows:
        for j in range(N):
            exact = sum(int(A[i, k])*int(W[k, j]) for k in range(N))
            assert exact == int(product[i, j])
    # Independent integer row sums, subtraction, and Fraction bound assembly.
    w = F(max(sum(abs(int(v)) for v in row) for row in W), producer.S)
    r0 = F(max(sum(abs((producer.S**2 if i == j else 0)-int(product[i, j]))
                       for j in range(N)) for i in range(N)), producer.S**2)
    rho = r0 + N*bound*w
    assert str(w) == result['inverse_norm_fraction']
    assert str(r0) == result['residual_quantized_fraction']
    assert str(rho) == result['rho_fraction']
    arg = np.array([result['mesh_arg_dyadic']])
    p = producer.integer(producer.basis(arg, n))[0]
    independent_max = sum(abs(sum(int(p[k])*int(W[k, j]) for k in range(N))) for j in range(N))
    assert independent_max == result['mesh_max_integer']
    grid, delta, cm = producer.mesh(n, m)
    error = N*(bound+n*n*delta)*w
    mid = F(independent_max, producer.S**2)
    assert str(max(F(0), mid-error)/(1+rho)) == result['lower_fraction']
    assert str(cm*(mid+error)/(1-rho)) == result['upper_fraction']
    return {'exact_fraction_node_basis_entries': N*N, 'maximum_node_error_display': float(worst),
            'beta_fraction': str(bound), 'bigint_residual_product_rows': rows,
            'bigint_residual_product_entries': len(rows)*N,
            'bigint_mesh_arg_product_entries': N,
            'fraction_final_endpoints_match': True,
            'independent_mesh': independent_mesh_check(n, m),
            'seconds': time.monotonic()-started}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--family', choices=['qr', 'payload12'], required=True)
    ap.add_argument('--degrees', nargs='+', type=int, required=True)
    ap.add_argument('--m', type=int, required=True)
    ap.add_argument('--arithmetic', nargs='*', type=int, default=[])
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    receipt = {'schema': 'fdq-supplemental-certificate-check-v1', 'command': sys.argv,
               'source': identity(Path(__file__)), 'producer_source': identity(CODE),
               'python': platform.python_version(), 'numpy': np.__version__,
               'threads': {key: os.getenv(key) for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')},
               'rows': []}
    for n in args.degrees:
        path = TOP/'evidence'/('u2-degree12-nodes.json' if args.family == 'payload12' else f'fd4-qr-n{n}-nodes.json')
        x = load_nodes(path)
        assert len(x) == math.comb(n+3, 3) and len(np.unique(x, axis=0)) == len(x) and np.max(abs(x)) <= 1
        result = producer.certificate(x, n, args.m, 120)
        assert result['status'].startswith('CERTIFIED_'), result
        row = {'n': n, 'm': args.m, 'family': args.family, 'input': identity(path), 'certificate': result}
        if n in args.arithmetic:
            row['arithmetic_crosscheck'] = arithmetic_check(x, n, args.m, result)
        producer_path = TOP/'evidence'/(f'fd4-payload-m{args.m}.json' if args.family == 'payload12' else 'fd4-qr.json')
        source = json.loads(producer_path.read_text())
        expected = next(r['certificate'] for r in source['rows'] if r['n'] == n)
        keys = [k for k in result if k not in ('seconds', 'status')]
        assert all(result[k] == expected[k] for k in keys), n
        row['producer_receipt'] = identity(producer_path)
        row['all_non_timing_certificate_fields_equal'] = True
        receipt['rows'].append(row)
        encoded = json.dumps(receipt, separators=(',', ':'))+'\n'
        assert len(encoded.encode()) <= 32768
        args.output.write_text(encoded)
        print(json.dumps({'n': n, 'm': args.m, 'seconds': result['seconds'], 'interval': result['interval_display'],
                          'arithmetic_seconds': row.get('arithmetic_crosscheck', {}).get('seconds')}), flush=True)

if __name__ == '__main__':
    main()
