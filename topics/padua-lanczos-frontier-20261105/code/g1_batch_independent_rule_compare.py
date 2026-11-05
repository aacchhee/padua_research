#!/usr/bin/env python3
"""Independent exact comparison for one newly completed remaining rule20."""
import argparse
import json
import pathlib
import sys
import time
from fractions import Fraction
from g1_batch_independent_compare import FIELDS, RULES, cmp, ident, pinned, require
from g1_independent_run import validate

SOURCE = 'b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc'
ENGINE = '49b45df9c2c28e3e63e9b886ff873a744ea0f0a44cd5f51fe2e3a345eec81552'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--rule', choices=('mirror', 'alt', 'pivot'), required=True)
    ap.add_argument('--producer-receipt', required=True)
    ap.add_argument('--native-receipt', required=True)
    ap.add_argument('--producer-source', required=True)
    ap.add_argument('--receipt', required=True)
    a = ap.parse_args()
    start = time.monotonic()
    producer = json.loads(pathlib.Path(a.producer_receipt).read_text())
    native = json.loads(pathlib.Path(a.native_receipt).read_text())
    source = ident(a.producer_source)
    require(source['sha256'] == ENGINE == producer['code_sha256'], 'producer source mismatch')
    require(producer['result'] == 'EXACT_CASE_COMPLETED'
            and producer['set'] == 'rotated' and producer['rule'] == a.rule
            and producer['max_degree'] == 20 and producer['complete_degrees'] == list(range(2, 21))
            and producer['all_original_nodes'] == 625 and producer['all_source_columns'] == 230
            and producer['controls']['every_new_column_exact_Gram_pairings'], 'producer not complete')
    require(native['status'] == 'PASS native exact remaining-rule20; fresh producer comparison pending'
            and native['rule'] == a.rule and native['grid'] == 'rotated'
            and native['completed_degrees'] == list(range(2, 21)) and native['node_count'] == 625
            and native['source_count_at20'] == 230 and native['native_source']['sha256'] == SOURCE,
            'native not complete or wrong source')
    native_source = pinned(native['native_source'])
    producer_endpoint = pinned(producer['endpoint_file'])
    native_endpoint = pinned(native['endpoint_file'])
    p_rows = json.loads(pathlib.Path(producer_endpoint['path']).read_text())['runs']
    n_rows = [json.loads(line) for line in pathlib.Path(native_endpoint['path']).read_text().splitlines()]
    require([r['degree'] for r in p_rows] == list(range(2, 21))
            and [r['degree'] for r in n_rows] == list(range(2, 21)), 'missing/duplicate degree')
    for p, n in zip(p_rows, n_rows):
        validate(n)
        require(n['set'] == 'rotated' and n['rule'] == a.rule, 'wrong native case')
        for field in ('degree', 'set', 'rule', 'sources', 'source_count', 'basis_count',
                      'point_count', 'pivot_choices', 'pivot_ties'):
            require(p[field] == n[field], 'metadata differs: '+field)
        require(cmp(p['normal_trace_exact'], n['normal_trace_exact']) == 0, 'trace differs')
        for field in FIELDS:
            require(cmp(p[field]['exact'], n[field]['exact']) == 0,
                    'endpoint differs at degree%s: %s' % (p['degree'], field))
        values = [Fraction(p[field]['exact']) for field in FIELDS]
        require(all(v > 0 for v in values) and values[0] <= values[3]
                and values[3] == min(values[1:3]), 'producer endpoint order/minimum')
    receipt = dict(status='PASS fresh producer/native exact rotated %s20 comparison' % a.rule,
                   rules_sha=RULES, checker=ident(__file__), producer_source=source,
                   native_source=native_source, producer_receipt=ident(a.producer_receipt),
                   native_receipt=ident(a.native_receipt), producer_endpoints=producer_endpoint,
                   native_endpoints=native_endpoint,
                   dependencies=[ident(pathlib.Path(__file__).with_name(name)) for name in
                                 ('g1_batch_independent_compare.py', 'g1_independent_run.py')],
                   matched_degrees=list(range(2, 21)), rational_endpoint_comparisons=76,
                   all_original_nodes=625, all_source_columns_at_max_degree=230,
                   command=[sys.executable, '-B', str(pathlib.Path(__file__).resolve()), *sys.argv[1:]],
                   wall_seconds=time.monotonic()-start,
                   limits='Actual read-only all19-row exact comparison; no native rerun, fit or asymptotic claim. '
                          'Native has no maximizing witness field.')
    output = pathlib.Path(a.receipt)
    require(not output.exists(), 'refusing to overwrite receipt')
    output.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
