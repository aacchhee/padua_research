#!/usr/bin/env python3
"""Independent finite validation; no fits, extrapolation or rigorous enclosures."""
import argparse
import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.sparse.linalg import eigsh

ROOT = Path(__file__).resolve().parents[3]
TOPIC = 'topics/padua-mz-sharp-constants-20261106/'
PIN = '2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861'
EXPECTED = {
    TOPIC+'code/S4_structured.py': '40e9ffc00edbf8ff9009cfa133646a69815f8423ad8baf4bdd23a69ae604bd8d',
    'topics/mz-constants/sources/padua_mz_inputs/code/cc_mz_large.py': 'df392b043fad81395ce6e07258a438bbd5fc609fc83fc51fa03314b885ac5af9',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def mu(k):
    # Independent scalar moment formula, avoiding the producer helper.
    return 0.0 if int(k) % 2 else 2.0/(1-int(k)**2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    for path, expected in EXPECTED.items():
        assert sha(ROOT/path) == expected, path
    source = module(TOPIC+'code/S4_structured.py', 'checked_structured')
    cc = module('topics/mz-constants/sources/padua_mz_inputs/code/cc_mz_large.py', 'checked_dense')
    started = time.monotonic()
    report = dict(status='MEASURED', rigorous_enclosures=False,
        source_and_rules_pin=PIN, scan_preregistration_commit='e2652c3',
        role='independent supplementary checker',
        requested_model='gpt-6-astra high; actual runtime metadata unexposed',
        command=[sys.executable]+sys.argv, checker_sha256=sha(__file__), input_sha256=EXPECTED,
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        python=sys.version, numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform(),
        threads={k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        seed=20261107, tolerance=2e-12, ncv=40, maxiter=3000,
        guards=dict(dense_relative=1e-10, sparse_quadratic_relative=1e-10,
                    inverse_residual=1e-9, constraint=1e-9, symmetry=1e-10), results=[])

    def save():
        report['seconds'] = time.monotonic()-started
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')

    for N in (101, 1281, 8192, 8193):
        tick = time.monotonic()
        op = source.ContinuousOverCC(N)
        rng = np.random.default_rng(report['seed']+N)
        row = dict(N=N, n=N-1, weight_sum=float(op.w.sum()),
                   minimum_weight=float(op.w.min()), results={})
        u, v = rng.standard_normal((2, N+1))
        row['symmetry_relative_error'] = float(abs(u@(op@v)-v@(op@u))/(np.linalg.norm(u)*np.linalg.norm(v)))
        row['artificial_unit_eigenvector_residual'] = float(np.linalg.norm(op@op.h-op.h))
        # A separated implementation of p on the CC grid and its integral:
        # 32 nonzero Chebyshev modes, all of degree <=N-1.
        indices = np.unique(np.r_[0, N-1, rng.choice(np.arange(1,N-1), 30, replace=False)])
        coeff = rng.standard_normal(len(indices))
        theta = np.pi*np.arange(N+1)/N
        values = np.cos(theta[:, None]*indices[None, :])@coeff
        z = op.sw*values
        exact_moment_quadratic = sum(coeff[i]*coeff[j]*(mu(a+b)+mu(abs(a-b)))/2
                                    for i,a in enumerate(indices) for j,b in enumerate(indices))
        measured_quadratic = float(z@(op@z))
        row['sparse_polynomial_quadratic_relative_error'] = abs(measured_quadratic/exact_moment_quadratic-1)
        row['sparse_polynomial_constraint_relative'] = float(abs(op.h@z)/np.linalg.norm(z))
        row['sparse_polynomial_modes'] = len(indices)
        for name, which in (('minimum','LA'), ('maximum','SA')):
            before = op.calls
            _, vectors = eigsh(op, k=1, which=which, v0=rng.standard_normal(N+1),
                               tol=report['tolerance'], ncv=report['ncv'], maxiter=report['maxiter'])
            vector = vectors[:,0]
            av = op@vector
            eigenvalue = float(vector@av)
            row['results'][name] = dict(eigenvalue=1/eigenvalue,
                inverse_eigenvalue=eigenvalue,
                inverse_residual_2_float=float(np.linalg.norm(av-eigenvalue*vector)),
                constraint_residual_float=float(abs(op.h@vector)), matvecs=op.calls-before)
        if N <= 1281:
            dense = [cc.extremes(N,N-1,p) for p in (0,1)]
            row['dense_reference'] = [float(min(p[0] for p in dense)),float(max(p[1] for p in dense))]
            row['dense_maximum_relative_error'] = max(abs(row['results'][name]['eigenvalue']/reference-1)
                for name, reference in zip(('minimum','maximum'), row['dense_reference']))
        checks = [row['symmetry_relative_error'] <= 1e-10,
                  row['sparse_polynomial_quadratic_relative_error'] <= 1e-10,
                  row.get('dense_maximum_relative_error',0) <= 1e-10]
        checks += [r[key] <= 1e-9 for r in row['results'].values()
                   for key in ('inverse_residual_2_float','constraint_residual_float')]
        row['pass'] = all(checks)
        row['seconds'] = time.monotonic()-tick
        report['results'].append(row)
        save()
        print(json.dumps(row), flush=True)
    report['all_pass'] = all(row['pass'] for row in report['results'])
    report['inputs_unchanged_at_end'] = all(sha(ROOT/path) == expected for path, expected in EXPECTED.items())
    save()
    if not report['all_pass'] or not report['inputs_unchanged_at_end']:
        raise RuntimeError('Independent check failed')


if __name__ == '__main__':
    main()
