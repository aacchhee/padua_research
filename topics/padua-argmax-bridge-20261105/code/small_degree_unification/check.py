#!/usr/bin/env python3
"""Unchanged strict checker with an honestly identified metadata-only kernel fix."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = ROOT / 'topics/padua-argmax-effective-20261103/code/native_checker'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise RuntimeError('No receipt overwrite')
    frozen = json.loads((HERE / 'METADATA-FREEZE.json').read_text())
    for row in frozen['sources']:
        path = ROOT / row['path']
        if digest(path) != row['sha256'] or path.stat().st_size != row['bytes']:
            raise RuntimeError('Source identity mismatch: ' + row['path'])
    spec = importlib.util.spec_from_file_location('unchanged_strict_checker', BASE / 'check.py')
    strict = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(strict)
    started = time.monotonic()
    # The actual input is passed untouched to the original strict check.
    result = strict.check(strict.load(args.certificate), args.binary)
    result.update(format='padua-native-independent-check-v1',
                  certificate_sha256=digest(args.certificate),
                  checker_sha256=digest(BASE / 'check.py'),
                  driver_sha256=digest(Path(__file__)),
                  kernel_sha256=digest(HERE / 'metadata_kernel.cpp'),
                  baseline_kernel_sha256=digest(BASE / 'kernel.cpp'),
                  binary_sha256=digest(args.binary),
                  seconds=time.monotonic() - started)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
