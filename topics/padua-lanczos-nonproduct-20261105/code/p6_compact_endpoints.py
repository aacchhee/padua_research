#!/usr/bin/env python3
"""Commit-size outward log tables after complete exact two-path scans only."""
import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path
from p6_rows import compare, validate

CODE = Path(__file__).resolve().parent
OLD = CODE.parents[1]/'padua-lanczos-frontier-20261105/code'
sys.path.insert(0, str(OLD))
import g1_fit as primary
import g1_fit_independent as secondary

RULES = ('bj', 'mirror', 'alt', 'pivot')


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def floor(q):
    return q.numerator//q.denominator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scan-receipt', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    info = json.loads(args.scan_receipt.read_text())
    assert info['status'] == 'PASS exact two-path weighted finite scan', 'requires full accepted two-path scan'
    assert info['max_degree'] == 16 and len(info['runs']) == 8
    family, count = info['family'], info['input']['point_count']
    assert family in ('H24_222', 'D36x9')
    rows, provenance = {}, []
    for run in info['runs']:
        assert run['status'].startswith('PASS')
        key = run['backend'], run['rule']
        assert key not in rows
        endpoint = run['output']
        assert identity(endpoint['path']) == endpoint
        values = [json.loads(x) for x in Path(endpoint['path']).read_text().splitlines()]
        assert [r['degree'] for r in values] == list(range(2, 17))
        for row in values:
            validate(row, family, count)
        rows[key] = values
        scientific = [{k: v for k, v in row.items() if k != 'elapsed_seconds'} for row in values]
        digest = hashlib.sha256(json.dumps(scientific, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        source_hash = run.get('source_sha256') or info['backends'][run['backend']]['source']['sha256']
        if 'source_catalog' in info:
            source = info['source_catalog'][source_hash]
        else:
            source = info['backends'][run['backend']]['source']
        assert identity(source['path']) == source and source['sha256'] == source_hash
        provenance.append({'backend': key[0], 'rule': key[1], 'endpoint_file': endpoint,
                           'scientific_rows_sha256': digest, 'source_sha256': source_hash})
    assert set(rows) == {(b, r) for b in ('producer', 'checker') for r in RULES}
    for rule in RULES:
        for a, b in zip(rows['producer', rule], rows['checker', rule]):
            compare(a, b, family, count)
            assert {k: v for k, v in a.items() if k != 'elapsed_seconds'} == {k: v for k, v in b.items() if k != 'elapsed_seconds'}
    scale, table = 10**15, []
    for degree in range(2, 17):
        for rule in RULES:
            row = rows['producer', rule][degree-2]
            limits = []
            for field in ('Knode_squared', 'upper_squared'):
                a = primary.logq(row[field]['exact'], 128)
                b = secondary.logq(row[field]['exact'], 128)
                assert max(a.a, b.lo) <= min(a.b, b.hi)
                lo, hi = min(a.a, b.lo)/2, max(a.b, b.hi)/2
                limits.extend([floor(lo*scale), -floor(-hi*scale)])
            table.append([degree, rule, *limits])
    result = {'schema': 'p6-compact-log-endpoints-v1', 'family': family,
              'scale': scale, 'point_count': count, 'degree_range': [2, 16], 'sources': 'all',
              'columns': ['degree', 'rule', 'logL_lower', 'logL_upper', 'logU_lower', 'logU_upper'],
              'meaning': 'integer/scale bounds natural log(L_squared)/2 and log(upper_squared)/2; lower=floor,upper=ceil; endpoint intervals, not true capacities',
              'model': 'P4-02 relative raw-product aggregate Hilbert inputs; spectral normal output; every source1..N_s-1 and original node',
              'source_scan_receipt': identity(args.scan_receipt),
              'native_input_sha256': info['input']['native_input_sha256'],
              'case_provenance': provenance, 'log_codes': [identity(OLD/'g1_fit.py'), identity(OLD/'g1_fit_independent.py')],
              'log_enclosure_agreement': 'PASS both128-bit exact rational routines on all120 endpoint logarithms',
              'generator': identity(__file__), 'row_guard': identity(CODE/'p6_rows.py'),
              'command': [sys.executable, '-B', *sys.argv], 'python': platform.python_version(),
              'generation_seconds': time.monotonic()-start, 'rows': table,
              'verification_limit': 'Standalone integer N2 replay needs only this table. Rechecking original endpoint/log generation requires the linked raw exact rows or their regeneration.'}
    encoded = json.dumps(result, separators=(',', ':'))+'\n'
    assert len(encoded.encode()) < 16384, 'compact table exceeds small-evidence cap'
    args.output.write_text(encoded)
    print(json.dumps({'family': family, 'rows': len(table), 'bytes': len(encoded.encode()),
                      'generation_seconds': result['generation_seconds'], 'status': 'PASS outward compact table'}))


if __name__ == '__main__':
    main()
