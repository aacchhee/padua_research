#!/usr/bin/env python3
"""Independent focused U1-M1 review; finite checks, no research round."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import types
import warnings

import numpy as np
import scipy

REPO = Path(__file__).resolve().parents[3]
TOPIC = REPO / 'topics/padua-3d-20261106'
BASE = '97c323bfae15cf3c76f40802c3ebabedceeb0c60'
SOURCE = TOPIC / 'code/u1_usable.py'
SEED = 20261107113


def ident(p):
    p = p.resolve()
    b = p.read_bytes()
    return {'path': str(p.relative_to(REPO)), 'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest()}


def cosine_basis(points, n):
    angles = np.arccos(np.clip(points, -1, 1))
    return np.column_stack([
        np.prod(np.cos(angles * [a, b, d-a-b]), axis=1)
        * 2**(sum(v > 0 for v in (a, b, d-a-b))/2)
        for d in range(n+1) for a in range(d+1) for b in range(d-a+1)])


def outcome(module, n, values, equal):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        try:
            result = module.parity_fit(n, values, equal)
            out = {'result_shape': list(result.shape),
                   'all_finite': bool(np.isfinite(result).all())}
        except Exception as e:
            out = {'exception': type(e).__name__, 'message': str(e)}
    out['warnings'] = [str(w.message) for w in caught]
    return out


def main(args):
    began = datetime.now(timezone.utc).isoformat()
    args.raw.mkdir(parents=True, exist_ok=False)
    files = [SOURCE, TOPIC/'code/u1c_api_check.py', TOPIC/'evidence/u1c-api.json',
             REPO/'tracks/lattice-unisolvence/code/c3_lebesgue.py',
             REPO/'tracks/lattice-unisolvence/code/c3_rank.py', Path(__file__).resolve()]
    before = [ident(p) for p in files]
    baseline = subprocess.check_output(['git', 'show', f'{BASE}:{SOURCE.relative_to(REPO)}'], cwd=REPO)
    (args.raw/'baseline-u1_usable.py').write_bytes(baseline)
    for i, p in enumerate(files):
        (args.raw/f'{i}-{p.name}').write_bytes(p.read_bytes())
    old = types.ModuleType('u1_original')
    old.__file__ = str(SOURCE)
    exec(compile(baseline, str(SOURCE), 'exec'), old.__dict__)
    spec = importlib.util.spec_from_file_location('u1_candidate', SOURCE)
    new = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(new)
    producer = json.loads((TOPIC/'evidence/u1c-api.json').read_text())
    for source in producer['sources']:
        p = Path(source['path'])
        assert ident(p)['sha256'] == source['sha256']
        assert p.stat().st_size == source['bytes']
    rng = np.random.default_rng(SEED)
    query = rng.uniform(-1, 1, (61, 3))
    rows = []
    for n in (1, 2, 3, 5, 9):
        for equal in (False, True):
            x, _, _ = new.parity_nodes(n, equal)
            M = len(x)
            V = cosine_basis(x, n)
            E = cosine_basis(query, n)
            N = V.shape[1]
            coefficients = rng.normal(size=(N, 3))
            coefficients[:, 2] = 0
            coefficients[-1, 2] = 1  # highest x mode in the stated ordering
            values = V @ coefficients
            full = float(np.linalg.norm(new.parity_fit(n, V, equal)-np.eye(N), np.inf))
            assert full < 1e-10
            prediction = float(np.max(abs(E @ new.parity_fit(n, values, equal)-E @ coefficients)))
            assert prediction < 1e-10
            top = float(np.max(abs(new.parity_fit(n, values[:, 2], equal)-coefficients[:, 2])))
            assert top < 1e-10
            base_values = rng.normal(size=(M, 6))
            readonly = base_values[:, 0].copy()
            readonly.flags.writeable = False
            variants = [
                ('vector', values[:, 0], (N,)), ('column', values[:, :1], (N, 1)),
                ('multiple', values, (N, 3)), ('vector_list', values[:, 0].tolist(), (N,)),
                ('matrix_list', values.tolist(), (N, 3)),
                ('complex_vector', values[:, 0]*(1+2j), (N,)),
                ('complex_matrix', values*(2-3j), (N, 3)),
                ('float32', values.astype(np.float32), (N, 3)),
                ('complex64', (values*(1+1j)).astype(np.complex64), (N, 3)),
                ('integer', np.arange(M), (N,)), ('boolean', np.arange(M)%2 == 0, (N,)),
                ('noncontiguous', base_values[:, ::2], (N, 3)),
                ('readonly', readonly, (N,)), ('empty_channels', np.empty((M, 0)), (N, 0))]
            valid = []
            for label, data, shape in variants:
                copy = np.asarray(data).copy()
                a, b = old.parity_fit(n, data, equal), new.parity_fit(n, data, equal)
                assert a.shape == b.shape == shape
                assert a.dtype == b.dtype
                assert a.tobytes() == b.tobytes(), (n, equal, label)
                assert np.array_equal(data, copy)
                valid.append(label)
            invalid = [
                ('scalar', 2.), ('one_value', [2.]), ('one_row', [[2., 3.]]),
                ('empty_vector', []), ('short_vector', np.zeros(M-1)),
                ('long_vector', np.zeros(M+1)), ('short_matrix', np.zeros((M-1, 2))),
                ('long_matrix', np.zeros((M+1, 2))), ('transposed', values.T),
                ('rank3', np.zeros((M, 1, 1))), ('rank4', np.zeros((M, 1, 1, 1)))]
            rejected = []
            for label, data in invalid:
                try:
                    new.parity_fit(n, data, equal)
                except ValueError as e:
                    assert 'values must' in str(e)
                    rejected.append(label)
                else:
                    raise AssertionError((n, equal, label))
            rows.append({'n': n, 'equal': equal, 'M': M, 'N': N,
                         'cosine_basis_reproduction_inf': full,
                         'prediction_max_error': prediction, 'top_coefficient_max_error': top,
                         'bitwise_baseline_equal_paths': valid, 'rejected': rejected})
    # Exhibit the originally silent broadcast independently, at the reported n4.
    original_failure = {}
    for label, data in [('one_value', [2.]), ('one_row', [[2., 3.]])]:
        original_failure[label] = {'before': outcome(old, 4, data, False),
                                   'after': outcome(new, 4, data, False)}
    # Degree-domain behavior is inherited and outside this shape-only repair.
    domain = []
    for n, data in [(0, [1.]), (-1, [1.]), (1.5, [1.]), (True, np.ones(5))]:
        for equal in (False, True):
            a, b = outcome(old, n, data, equal), outcome(new, n, data, equal)
            domain.append({'n_repr': repr(n), 'equal': equal, 'before': a, 'after': b})
    after = [ident(p) for p in files]
    assert before == after, 'source or evidence mutated during check'
    receipt = {'status': 'MEASURED independent supplementary API shape review; zero research rounds',
               'rules_and_baseline_commit': BASE, 'command': sys.argv,
               'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
               'seed': SEED, 'query_points': 61,
               'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                               'scipy': scipy.__version__, 'platform': platform.platform(),
                               'threads': {k: os.environ.get(k) for k in
                                           ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')}},
               'sources_unchanged_before_after': before,
               'baseline_source': {'bytes': len(baseline), 'sha256': hashlib.sha256(baseline).hexdigest()},
               'producer_receipt_source_pins_match': True,
               'rows': rows, 'original_failure': original_failure,
               'degree_domain_observations': domain,
               'counts': {'grid_cases': len(rows), 'bitwise_valid_cases': sum(len(r['bitwise_baseline_equal_paths']) for r in rows),
                          'shape_rejections': sum(len(r['rejected']) for r in rows)},
               'raw': str(args.raw), 'retention': 'regenerate-only snapshots; no cold archive delivery',
               'limits': 'Finite floating tests, no general theorem; original 24-case science replay is separate; formal Claude review pending.'}
    payload = json.dumps(receipt, separators=(',', ':'), allow_nan=False)+'\n'
    assert len(payload.encode()) < 16384
    args.out.write_text(payload)
    print(json.dumps({'counts': receipt['counts'], 'maximum_reproduction_residual': max(r['cosine_basis_reproduction_inf'] for r in rows),
                      'maximum_prediction_error': max(r['prediction_max_error'] for r in rows),
                      'receipt': ident(args.out)}))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--raw', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    main(p.parse_args())
