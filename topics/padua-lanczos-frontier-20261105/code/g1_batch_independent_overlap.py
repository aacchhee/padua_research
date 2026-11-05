#!/usr/bin/env python3
"""Read-only independent comparison of all88 frozen degree2--12 rows."""
import argparse
import json
import pathlib
import sys
from fractions import Fraction
from g1_batch_independent_compare import FIELDS, RULES, cmp, ident, pinned, require


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--directory', required=True)
    ap.add_argument('--source', required=True)
    ap.add_argument('--old', required=True)
    ap.add_argument('--receipt', required=True)
    a = ap.parse_args()
    old_id = ident(a.old)
    require(old_id['sha256'] == '0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344', 'wrong old input')
    old = {(r['set'], r['rule'], r['degree']): r
           for r in json.loads(pathlib.Path(a.old).read_text())['runs']}
    source = ident(a.source)
    cases = []
    for grid, nodes in [('triangle', 325), ('rotated', 625)]:
        for rule in ('bj', 'mirror', 'alt', 'pivot'):
            path = pathlib.Path(a.directory) / f'{grid}-{rule}-d12.json'
            run = json.loads(path.read_text())
            require(run['result'] == 'EXACT_CASE_COMPLETED' and run['max_degree'] == 12
                    and run['set'] == grid and run['rule'] == rule
                    and run['code_sha256'] == source['sha256'], 'wrong completed case/source')
            require(run['complete_degrees'] == list(range(2, 13))
                    and run['all_source_columns'] == 90 and run['all_original_nodes'] == nodes
                    and run['controls']['every_new_column_exact_Gram_pairings'], 'incomplete coverage')
            artifact = pinned(run['endpoint_file'])
            rows = json.loads(pathlib.Path(artifact['path']).read_text())['runs']
            require([r['degree'] for r in rows] == list(range(2, 13)), 'incomplete/duplicate rows')
            for row in rows:
                degree = row['degree']
                expected = old[grid, rule, degree]
                count = (degree+1)*(degree+2)//2
                require(row['source_count'] == count-1 and row['basis_count'] == count
                        and row['point_count'] == nodes and row['sources'] == 'all', 'bad row coverage')
                for field in ('degree', 'rule', 'set', 'sources', 'source_count',
                              'point_count', 'basis_count', 'pivot_choices'):
                    require(row[field] == expected[field], 'metadata differs: '+field)
                # Legacy sweep omitted tie metadata; frozen independent overlap
                # established this complete degree2--12 tie list separately.
                ties = [[2, 1]] if grid == 'rotated' and rule == 'pivot' else []
                require(row['pivot_ties'] == ties, 'frozen ties differ')
                require(Fraction(row['normal_trace_exact']) == nodes-count, 'incorrect trace')
                vals = [Fraction(row[field]['exact']) for field in FIELDS]
                require(all(v > 0 for v in vals) and vals[0] <= vals[3]
                        and vals[3] == min(vals[1:3]), 'bad endpoint order/minimum')
                for field in FIELDS:
                    require(cmp(row[field]['exact'], expected[field]['exact']) == 0,
                            f'endpoint differs: {grid}/{rule}/{degree}/{field}')
            cases.append(dict(grid=grid, rule=rule, rows=11, receipt=ident(path), endpoints=artifact))
    receipt = dict(status='PASS independent exact all88 old overlap comparison', rules_sha=RULES,
                   code=ident(__file__), comparison_dependency=ident(pathlib.Path(__file__).with_name('g1_batch_independent_compare.py')),
                   source=source, old=old_id, rows=88, rational_endpoint_comparisons=352,
                   command=[sys.executable, '-B', str(pathlib.Path(__file__).resolve()), *sys.argv[1:]],
                   cases=cases, limits='Actual read-only comparison; no scientific rerun or fits.')
    output = pathlib.Path(a.receipt)
    require(not output.exists(), 'refusing to overwrite receipt')
    output.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({'status': receipt['status'], 'rows': 88, 'receipt': ident(output)}))


if __name__ == '__main__':
    main()
