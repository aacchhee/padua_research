#!/usr/bin/env python3
"""Finite AD verification of the analytic Krawtchouk parity witness.

The all-N proof is in theory/conditioning-lower-krawtchouk.md. This script
is a floating diagnostic, not a computer-assisted proof or interval check.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import platform
import time
import mpmath as mp

HERE = Path(__file__).resolve()
AD = HERE.with_name('conditioning.py')
spec = importlib.util.spec_from_file_location('conditioning_ad', AD)
ad = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ad)


def positive_coefficient(n, r):
    if r == 0:
        return Fraction(1)
    return sum((Fraction(comb(n, j)*comb(r-1, j-1))*Fraction(24, 25)**j
                for j in range(1, min(n, r)+1)), Fraction(0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sizes', type=int, nargs='+', default=[2, 3, 4, 6, 8, 12])
    parser.add_argument('--dps', type=int, default=120)
    args = parser.parse_args()
    if min(args.sizes) < 2 or args.dps < 50:
        parser.error('N>=2 and dps>=50 required')
    started = time.monotonic()
    cases = []
    with mp.workdps(args.dps):
        for N in args.sizes:
            M = N-1
            xq, wq = ad.base.inputs(N, 'krawtchouk')
            x, w = ad.seed_inputs(xq, wq)
            field = ad.layers(N, *(ad.marginal(x, row) for row in w))
            scale = max(abs(row['b2'].v) for row in field.values())
            err = mp.mpf(0)
            rows = []
            for n in range(M):
                m = M-n
                q = positive_coefficient(n, m-1)
                predicted = Fraction((-1)**n * 5**(M-1), M)*q
                computed = sum(field[n,m]['b2'].g[2*N+k]
                               *ad.base.convert(wq[1][k], mp.mpf)*(-1)**k
                               for k in range(N))
                expected = mp.mpf(predicted.numerator)/predicted.denominator
                relative = abs(computed-expected)/max(1, abs(expected))
                err = max(err, relative)
                rows.append({'nu': [n,m], 'derivative_exact': str(predicted),
                             'absolute_error': mp.nstr(abs(computed-expected), 8)})
            ident = json.dumps({'nodes': list(map(str,xq)),
                                'weights': [list(map(str,row)) for row in wq]}, sort_keys=True)
            cases.append({'N': N, 'terminal_rows': rows,
                          'max_scaled_derivative_error': mp.nstr(err, 12),
                          'field_scale_error': mp.nstr(abs(scale-mp.mpf(1)/5), 12),
                          'input_sha256': hashlib.sha256(ident.encode()).hexdigest()})
    result = {'status': 'MEASURED; floating AD verification, analytic proof separate',
              'python': platform.python_version(), 'mpmath': mp.__version__,
              'dps': args.dps, 'code_sha256': hashlib.sha256(HERE.read_bytes()).hexdigest(),
              'AD_sha256': hashlib.sha256(AD.read_bytes()).hexdigest(),
              'baseline_sha256': hashlib.sha256(ad.BASE.read_bytes()).hexdigest(),
              'elapsed_seconds': time.monotonic()-started, 'cases': cases}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
