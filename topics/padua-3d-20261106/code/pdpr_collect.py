#!/usr/bin/env python3
"""Administrative compact receipt from an already completed, unchanged pilot.

This program performs no candidate generation, fitting or assessment. Exact
full-precision results and original executed source bytes remain in raw files.
"""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
import os
from pathlib import Path
import platform
import sys
import numpy as np
import scipy


def identity(path):
    p = Path(path).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def compact(x):
    if isinstance(x, float):
        return float(format(x, '.6g'))
    if isinstance(x, list):
        return [compact(v) for v in x]
    if isinstance(x, dict):
        return {k: compact(v) for k, v in x.items()}
    return x


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scratch', type=Path, required=True)
    p.add_argument('--protocol-commit', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--original-command')
    p.add_argument('--round', default='P1')
    a = p.parse_args()
    collect(a)


def collect(a):
    inventory = json.loads((a.scratch/'inventory.json').read_text())
    for item in inventory:
        if identity(item['path']) != item:
            raise ArithmeticError('completed pilot raw identity changed: '+item['path'])
    details = json.loads((a.scratch/'details.json').read_text())
    columns = ['n', 'name', 'M', 'eligible', 'condition2', 'reproduction_inf',
               'trace', 'integer_risk', 'amp', 'variance_max', 'target_regressions_to_full']
    logical = {'columns': columns,
               'rows': [[r.get(k) for k in columns] for r in details['assessments']],
               'derived_columns': {'M_trace': 'M*trace', 'amp_union': 'max(amp.values())'},
               'paths': [{k: v for k, v in r.items() if k not in ('curve', 'costs_wall', 'candidate_tables', 'numerically_rejected')}
                         for r in details['paths']],
               'degrees': details['degrees'], 'gate': details['gate'], 'unrun': details['unrun']}
    payload = json.dumps(compact(logical), separators=(',', ':'), allow_nan=False).encode()
    packed = lzma.compress(payload, format=lzma.FORMAT_XZ, preset=9)
    if lzma.decompress(packed) != payload:
        raise ArithmeticError('receipt codec roundtrip mismatch')
    sources = [identity(p) for p in sorted(a.scratch.glob('source-*'))]
    metadata_path = a.scratch/'run-metadata.json'
    metadata = json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
    # Producer versions/threads are those of the recorded command and unchanged
    # same-session interpreter. The collector reports its versions separately.
    receipt = {'schema': 'pdpr-compact-v2',
        'status': 'MEASURED complete finite pruning; lower amplification samples',
        'round': a.round, 'input_head': '6d894d50efd8167c5b10f3d5b0da4d8cf214b681',
        'protocol_commit': a.protocol_commit, 'producer_command': a.original_command or metadata.get('command'),
        'producer_utc': {k: metadata.get(k) for k in ('started_utc', 'ended_utc')},
        'executed_source_snapshots': sources, 'collector': identity(__file__),
        'collector_command': metadata.get('collector_command', sys.argv), 'collected_utc': datetime.now(timezone.utc).isoformat(),
        'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')},
        'timing': details['timing'], 'gate': details['gate'],
        'logical_results_codec': 'ASCII base85 -> lzma.decompress(FORMAT_XZ) -> UTF8 JSON; entire unsplit object',
        'logical_results_base85': base64.b85encode(packed).decode(),
        'logical_results_uncompressed_bytes': len(payload),
        'summary_precision': 'six significant digits; all gate decisions use original full-precision raw values; M_trace and amp_union derived as documented',
        'raw_details': identity(a.scratch/'details.json'),
        'inputs': details.get('inputs', []),
        'raw_inventory': identity(a.scratch/'inventory.json'),
        'raw_policy': 'unique local regeneration-only; all full-precision curves/functions/maps/recipes/CPU+wall phases retained; no archive delivery',
        'serialization_note': 'Summary-only packing; fullprecision raw unchanged. P1serialization deviation documented in pruning-results.md. No executed-source relabel.',
        'seeds': metadata.get('seeds', {'random': '2026110900+n', 'training': '2026110910+n',
                  'chebyshev': '2026110920+n', 'uniform': '2026110930+n'}),
        'scope': 'Unweighted physical OLS; iid equal variance; fixed-map integer repeats B=Mstart; product-Chebyshev prediction measure. Haar separately labeled. Every12-target/measure/sigma table is fullprecision raw.'}
    text = json.dumps(receipt, separators=(',', ':'), allow_nan=False)+'\n'
    if len(text.encode()) >= 16384:
        raise ArithmeticError('compact receipt too large: '+str(len(text.encode())))
    a.output.write_text(text)
    print(json.dumps({'output': str(a.output), 'bytes': len(text.encode()),
                      'sha256': identity(a.output)['sha256'], 'gate': details['gate']}))


if __name__ == '__main__':
    main()
