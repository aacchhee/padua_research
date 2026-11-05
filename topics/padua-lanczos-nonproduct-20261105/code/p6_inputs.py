#!/usr/bin/env python3
"""Validate rational positive node data; this is not N1 family admission."""
import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path


def prepare(spec):
    assert set(spec) >= {'family', 'admission', 'points'}
    assert re.fullmatch(r'[A-Za-z0-9_-]+', spec['family'])
    assert isinstance(spec['admission'], str) and spec['admission']
    points = []
    for row in spec['points']:
        assert len(row) == 3 and all(isinstance(x, str) for x in row)
        x, y, w = map(Fraction, row)
        assert w > 0
        points.append((x, y, w))
    assert points and len({(x, y) for x, y, _ in points}) == len(points)
    data = (str(len(points)) + '\n' + ''.join(' '.join(map(str, p)) + '\n' for p in points)).encode()
    return data, {'family': spec['family'], 'admission': spec['admission'],
                  'point_count': len(points), 'weight_sum': str(sum(p[2] for p in points)),
                  'native_input_bytes': len(data), 'native_input_sha256': hashlib.sha256(data).hexdigest(),
                  'parameters': spec.get('parameters', {}),
                  'model': 'positive finite measure; weighted Euclidean aggregate source norm'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', type=Path, required=True)
    parser.add_argument('--native-input', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    source = args.spec.read_bytes()
    data, receipt = prepare(json.loads(source))
    args.native_input.write_bytes(data)
    receipt.update(spec_path=str(args.spec), spec_sha256=hashlib.sha256(source).hexdigest(),
                   native_input_path=str(args.native_input),
                   code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   status='PASS exact rational data validation; N1 proof remains separate')
    args.receipt.write_text(json.dumps(receipt, indent=2)+'\n')


if __name__ == '__main__':
    main()
