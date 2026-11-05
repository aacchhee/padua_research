#!/usr/bin/env python3
"""Read-only independent BJ20 endpoint comparison; no producer math imports."""
import argparse
import hashlib
import json
import pathlib
import platform
import sys
import time
from fractions import Fraction

sys.set_int_max_str_digits(1000000)
RULES = '9825d184517db81d0aad8542fbd6639f2164b803'
NATIVE = 'b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc'
ENDPOINT = '0f7c1475a0484aa0905bcdfddf938b4ea2154f58322228e17bb7a91955ca3cf7'
FIELDS = ('Knode_squared', 'KHS_squared', 'Urow_squared', 'upper_squared')


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def ident(path):
    p = pathlib.Path(path)
    b = p.read_bytes()
    return dict(path=str(p.resolve()), bytes=len(b), sha256=hashlib.sha256(b).hexdigest())


def pinned(record, path=None):
    actual = ident(record['path'] if path is None else path)
    require(actual['sha256'] == record['sha256'] and actual['bytes'] == record['bytes'],
            'artifact identity mismatch: ' + actual['path'])
    return actual


def cmp(a, b):
    a, b = Fraction(a), Fraction(b)
    left, right = a.numerator * b.denominator, b.numerator * a.denominator
    return (left > right) - (left < right)


def validate(row, native):
    s = row['degree']
    count = (s + 1) * (s + 2) // 2
    require(type(s) is int and 2 <= s <= 20, 'invalid degree')
    require(row['set'] == 'rotated' and row['rule'] == 'bj', 'wrong case')
    require(row['sources'] == 'all' and row['source_count'] == count - 1
            and row['basis_count'] == count and row['point_count'] == 625,
            'incomplete source/node/basis coverage')
    require(len(row['pivot_choices']) == count - 1
            and set(row['pivot_choices']) <= {'X', 'Y'} and row['pivot_ties'] == [],
            'invalid choices or ties')
    require(Fraction(row['normal_trace_exact']) == 625 - count, 'incorrect trace')
    if native:
        require(row['exact_gram_pairs_checked'] >= count * (count - 1) // 2,
                'missing native Gram checks')
    values = [Fraction(row[field]['exact']) for field in FIELDS]
    require(all(v > 0 for v in values) and values[0] <= values[3]
            and values[3] == min(values[1:3]), 'invalid endpoint ordering/minimum')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--producer-receipt', required=True)
    ap.add_argument('--producer-source', required=True)
    ap.add_argument('--native-receipt', required=True)
    ap.add_argument('--receipt', required=True)
    ap.add_argument('--degree', type=int, choices=(14, 20), default=20)
    a = ap.parse_args()
    start = time.monotonic()
    prod = json.loads(pathlib.Path(a.producer_receipt).read_text())
    native = json.loads(pathlib.Path(a.native_receipt).read_text())
    require(prod['result'] == 'EXACT_CASE_COMPLETED' and prod['max_degree'] == a.degree
            and prod['set'] == 'rotated' and prod['rule'] == 'bj',
            'producer case did not complete')
    source = ident(a.producer_source)
    require(source['sha256'] == prod['code_sha256'], 'producer source mismatch')
    require(prod['complete_degrees'] == list(range(2, a.degree + 1))
            and prod['all_original_nodes'] == 625 and prod['all_source_columns'] == (a.degree+1)*(a.degree+2)//2-1,
            'producer completion coverage mismatch')
    require(prod['controls']['every_new_column_exact_Gram_pairings'],
            'producer missing Gram check declaration')
    require(native['status'] == 'PASS native exact BJ20 pilot; fresh producer comparison pending'
            and native['native_source']['sha256'] == NATIVE
            and native['endpoint_file']['sha256'] == ENDPOINT
            and native['completed_degrees'] == list(range(2, 21)), 'unrecognized native run')
    native_source = pinned(native['native_source'])
    producer_endpoint = pinned(prod['endpoint_file'])
    native_endpoint = pinned(native['endpoint_file'])
    p_rows = json.loads(pathlib.Path(producer_endpoint['path']).read_text())['runs']
    n_rows = [json.loads(line) for line in pathlib.Path(native_endpoint['path']).read_text().splitlines()]
    require([r['degree'] for r in p_rows] == list(range(2, a.degree + 1))
            and [r['degree'] for r in n_rows] == list(range(2, 21)), 'missing or duplicate rows')
    for p, n in zip(p_rows, n_rows):
        validate(p, False)
        validate(n, True)
        for field in ('degree', 'set', 'rule', 'sources', 'source_count', 'basis_count',
                      'point_count', 'pivot_choices', 'pivot_ties'):
            require(p[field] == n[field], 'metadata differs: ' + field)
        require(cmp(p['normal_trace_exact'], n['normal_trace_exact']) == 0, 'traces differ')
        for field in FIELDS:
            require(cmp(p[field]['exact'], n[field]['exact']) == 0,
                    'endpoint differs at degree %s: %s' % (p['degree'], field))
    receipt = dict(status='PASS fresh producer/native exact BJ%s comparison' % a.degree, rules_sha=RULES,
                   checker=ident(__file__), python=platform.python_version(),
                   producer_source=source, native_source=native_source,
                   producer_receipt=ident(a.producer_receipt), native_receipt=ident(a.native_receipt),
                   producer_endpoints=producer_endpoint, native_endpoints=native_endpoint,
                   command=[sys.executable, '-B', str(pathlib.Path(__file__).resolve()), *sys.argv[1:]],
                   matched_degrees=list(range(2, a.degree + 1)), rational_endpoint_comparisons=4*(a.degree-1),
                   all_original_nodes=625, all_source_columns_at_max_degree=(a.degree+1)*(a.degree+2)//2-1,
                   metadata=['choices', 'ties', 'source/node/basis counts', 'normal trace'],
                   wall_seconds=time.monotonic() - start,
                   limits='Read-only comparison actually executed; native run reused, not rerun. '
                          'No fit, remaining-rule execution or asymptotic claim. Native emits no '
                          'maximizing witness, so witness identity is outside this comparison.')
    output = pathlib.Path(a.receipt)
    require(not output.exists(), 'refusing to overwrite receipt')
    output.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
