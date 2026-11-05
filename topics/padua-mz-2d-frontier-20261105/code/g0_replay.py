#!/usr/bin/env python3
"""G0 adapter: execute frozen independent checker at m10 without repository writes."""
import argparse
import hashlib
import importlib.util
import json
import platform
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source = ROOT / 'tracks/mz-constants/code/mz2d_independent_check.py'
    spec = importlib.util.spec_from_file_location('frozen_independent', source)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    start = time.monotonic()
    result = {'command': sys.argv, 'python': sys.version,
              'platform': platform.platform(), 'sympy': checker.sp.__version__,
              'python_flint': checker.p.flint.__version__,
              'checker_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'scope': 'Frozen checker functions; no modification to frozen sources or outputs.',
              'region_checks': checker.region_checks()}
    print('region checks passed; start exact cyclotomic nodal m10', flush=True)
    result['nodal_m10'] = checker.nodal_check(10)
    result['seconds'] = time.monotonic() - start
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS', args.output, flush=True)


if __name__ == '__main__':
    main()
