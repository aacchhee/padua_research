#!/usr/bin/env python3
"""Replay unchanged T9 producers in isolated scratch and record missing metadata.

This supplies a new execution record, not retrospectively observed versions
for the historical runs. Original receipts and producer bytes stay intact.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile

TOP = Path(__file__).resolve().parents[1]
RULES = '7afa6a54a4db4652267e38cd48658ba435d20481'


def identity(path):
    b = path.read_bytes()
    return {'path': str(path), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def scientific(data):
    if isinstance(data, dict):
        return {k: scientific(v) for k, v in data.items() if k != 'seconds'}
    if isinstance(data, list):
        return [scientific(v) for v in data]
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    scratch = Path(tempfile.mkdtemp(prefix='padua-3d-r06-legacy-t9-'))
    (scratch / 'code').mkdir()
    (scratch / 'evidence').mkdir()
    (scratch / 'raw').mkdir()
    sources = {name: identity(TOP / 'code' / name) for name in
               ('t9_checks.py', 't9_maxima.py', 't4_stacks.py')}
    old = {name: json.loads((TOP / 'evidence' / name).read_text())
           for name in ('t9-checks.json', 't9-maxima.json')}
    copied = scratch / 'code/t9_checks.py'
    shutil.copyfile(TOP / 'code/t9_checks.py', copied)
    command = [sys.executable, str(copied)]
    completed = subprocess.run(command, capture_output=True, text=True, check=True)
    (scratch / 'checks.stdout').write_text(completed.stdout)
    (scratch / 'checks.stderr').write_text(completed.stderr)

    # Only output destinations are redirected for the unchanged maxima module.
    sys.path.insert(0, str(TOP / 'code'))
    spec = importlib.util.spec_from_file_location('legacy_t9_maxima', TOP / 'code/t9_maxima.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.TOP = scratch
    import numpy as np
    import scipy
    import mpmath as mp
    original_save = np.save

    def redirected_save(path, *values, **kwargs):
        return original_save(scratch / 'raw' / Path(path).name, *values, **kwargs)

    np.save = redirected_save
    try:
        module.main()
    finally:
        np.save = original_save
    equalities = {}
    for name, previous in old.items():
        current = json.loads((scratch / 'evidence' / name).read_text())
        equalities[name] = scientific(current) == scientific(previous)
        if not equalities[name]:
            raise RuntimeError('scientific receipt mismatch: ' + name)
    for name, before in sources.items():
        if identity(TOP / 'code' / name) != before:
            raise RuntimeError('producer source changed during replay')
    out = {
        'schema': 'padua-3d-legacy-t9-metadata-replay-v1', 'rules_sha': RULES,
        'status': 'new execution metadata; original missing metadata is not retroactively reconstructed',
        'command': 'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python ' +
                   str(Path(__file__).relative_to(TOP.parents[1])) + ' --output ' + str(args.output),
        'checker_sha256': identity(Path(__file__))['sha256'],
        'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                     'scipy': scipy.__version__, 'mpmath': mp.__version__},
        'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')},
        'historical_commands': ['python topics/padua-3d-20261106/code/t9_checks.py',
            'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t9_maxima.py'],
        'producer_sources': sources, 'scientific_fields_equal_excluding_seconds': equalities,
        'raw_node_arrays': [identity(p) for p in sorted((scratch / 'raw').glob('*.npy'))],
        'raw_retention': 'regenerate-only; no cold-storage delivery',
        'scratch': str(scratch), 'verdict': 'PASS'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(out, separators=(',', ':')) + '\n'
    if len(encoded.encode()) >= 16384:
        raise RuntimeError('receipt exceeds compact evidence limit')
    args.output.write_text(encoded)
    print(json.dumps({'verdict': 'PASS', 'output': str(args.output),
                      'raw_arrays': len(out['raw_node_arrays'])}))


if __name__ == '__main__':
    main()
