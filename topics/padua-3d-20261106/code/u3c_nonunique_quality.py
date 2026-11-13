#!/usr/bin/env python3
"""Complete, prospectively frozen n7 nonunique-support quality diagnostic."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import tempfile
import time

import numpy as np
import scipy
import sympy as sp
from sympy.polys.matrices import DomainMatrix

import u3_constructions as inherited

PIN = '97c323bfae15cf3c76f40802c3ebabedceeb0c60'
TOP = Path(__file__).resolve().parents[1]
PAIRS = ((13,98),(13,142),(16,93),(16,147),(17,28),(17,212),
         (26,37),(26,203),(28,223),(37,214),(44,113),(44,127),
         (66,85),(66,155),(76,99),(76,141),(85,174),(93,224),
         (98,227),(99,164),(113,196),(127,196),(141,164),(142,227),
         (147,224),(155,174),(203,214),(212,223))


def digest(path):
    path = Path(path)
    return {'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'bytes': path.stat().st_size}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        if os.environ.get(name) != '1':
            raise ValueError(f'{name}=1 is required before interpreter startup')
    started, cpu_started = time.monotonic(), time.process_time()
    source_receipt = TOP / 'interim-audit-01/evidence/ia3-blocks.json'
    original = json.loads(source_receipt.read_text())
    cases = [r for r in original['rows'] if r['n'] == 7]
    assert tuple(tuple(r['z'][1:]) for r in cases) == PAIRS
    assert len(PAIRS) == len(set(PAIRS)) == 28
    rawdir = Path(tempfile.mkdtemp(prefix='padua-u3c-nonunique-'))
    sources = [Path(__file__).resolve(), Path(inherited.__file__).resolve()]
    source_records = []
    for path in sources:
        snapshot = rawdir / path.name
        shutil.copyfile(path, snapshot)
        source_records.append(digest(path) | {'snapshot': str(snapshot)})
    (rawdir / 'input-block-receipt.json').write_bytes(source_receipt.read_bytes())

    # Count/rank/inverse checks for the full frozen domain precede all quality.
    validated = []
    for row in cases:
        z = row['z']
        cs = [inherited.cyclic_half(120, *z[1:])]
        cert = inherited.certify(7, cs)
        assert cert['full_rank'] and cert['count'] == 120
        A = DomainMatrix.from_Matrix(sp.Matrix(inherited.exact_C(7, z).tolist())).convert_to(sp.QQ)
        rational_inverse = A.inv()
        assert (A * rational_inverse).to_Matrix() == sp.eye(120)
        inv = rational_inverse.to_Matrix() * 8
        entry_sum = sum(abs(x) for x in inv)
        inverse_inf = max(sum(abs(inv[i,j]) for j in range(120)) for i in range(120))
        assert entry_sum == sp.Rational(row['S'])
        assert inverse_inf == sp.Rational(row['inverse_inf'])
        validated.append({'z': z, 'components': cs, 'certificate': cert,
                          'S': str(entry_sum), 'inverse_inf': str(inverse_inf)})
    print('All 28 exact count/rank/inverse checks passed; quality follows.', flush=True)
    controls = inherited.controls(7)
    rows = []
    for row in validated:
        quality = inherited.quality(7, row['components'])
        values = [quality[str(m)]['sampled_lebesgue'] for m in (21,41)]
        accepted = all(value is not None for value in values)
        ratios = {name: [values[k] / controls[name][str(m)]['sampled_lebesgue']
                        for k,m in enumerate((21,41))] if accepted else None
                  for name in ('QR','Leja')}
        q = max(ratios['QR']) if accepted else None
        result = row | {'quality': quality, 'ratios': ratios, 'q': q,
                        'gate_pass': accepted and q <= 1}
        rows.append(result)
        print(json.dumps({'z': row['z'], 'values': values, 'q': q}), flush=True)
    rawfile = rawdir / 'all-candidates.json'
    rawfile.write_text(json.dumps({'controls': controls, 'rows': rows}, separators=(',',':'))+'\n')
    assert all(digest(p)['sha256'] == rec['sha256'] for p,rec in zip(sources,source_records))
    valid = [r for r in rows if r['q'] is not None]
    summary = {
        'pin': PIN, 'command': sys.argv, 'code': source_records,
        'input': digest(source_receipt),
        'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                     'scipy': scipy.__version__, 'sympy': sp.__version__},
        'threads': {k: os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        'seed': None, 'scope': {'n':7, 'N':120, 'frozen_cases':28, 'completed':len(rows)},
        'exact_checks': {'count_rank_inverse_pass':len(validated), 'two_actual_node_primes':True,
                         'primes_omega':[[c['p'],c['omega']] for c in validated[0]['certificate']['checks']]},
        'controls': controls,
        'row_columns': ['b','c','condition2','residual_inf','L21','L41','q','Leja21_ratio','Leja41_ratio','gate_pass','det_prime1','det_prime2'],
        'rows': [[*r['z'][1:], r['quality']['41']['condition2'],
                  r['quality']['41'].get('node_residual_inf'),
                  r['quality']['21']['sampled_lebesgue'],r['quality']['41']['sampled_lebesgue'],
                  r['q'],*(r['ratios']['Leja'] or [None,None]),r['gate_pass'],
                  *[c['det'] for c in r['certificate']['checks']]] for r in rows],
        'result': {'passes':sum(r['gate_pass'] for r in rows),
                   'min_q':min(r['q'] for r in valid) if valid else None,
                   'max_q':max(r['q'] for r in valid) if valid else None,
                   'all_validation_pass':len(valid)==28,
                   'decision':'eligible for separately registered structural continuation' if any(r['gate_pass'] for r in rows)
                              else 'stop this complete degree7 nonunique half-shift quality route'},
        'raw':digest(rawfile) | {'retention':'local regenerate-only; no cold-storage delivery'},
        'seconds':time.monotonic()-started, 'cpu_seconds':time.process_time()-cpu_started,
    }
    encoded = json.dumps(summary, separators=(',',':'), allow_nan=False)+'\n'
    assert len(encoded.encode()) < 16384
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(encoded)
    print(json.dumps({'receipt':str(args.receipt),'result':summary['result']}), flush=True)


if __name__ == '__main__':
    main()
