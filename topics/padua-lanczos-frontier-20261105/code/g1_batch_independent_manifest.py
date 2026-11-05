#!/usr/bin/env python3
"""Build full eight-case fit manifest only after all exact case acceptances.
No logarithms, regressions, scientific reruns or endpoint transformations.
"""
import argparse
import json
import pathlib
import sys
from g1_batch_independent_compare import ident, pinned, require

RULES = ('bj', 'mirror', 'alt', 'pivot')
FROZEN = '19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    topic = pathlib.Path(args.topic)
    prior_path = topic/'evidence/g1-independent-triangle20-comparison.json'
    prior = json.loads(prior_path.read_text())
    require(prior['status'] == 'PASS exact independent/producer T24 degree2–20 all4rules identities'
            and prior['row_count'] == 76, 'missing original T24 acceptance')
    # Read and validate every acceptance before creating any manifest/receipt.
    rotated = {}
    for rule in RULES:
        path = topic/f'evidence/g1-batch-independent-{rule}20.json'
        receipt = json.loads(path.read_text())
        expected_status = 'PASS fresh producer/native exact BJ20 comparison' if rule == 'bj' else \
                          f'PASS fresh producer/native exact rotated {rule}20 comparison'
        require(receipt['status'] == expected_status
                and receipt['matched_degrees'] == list(range(2, 21))
                and receipt['rational_endpoint_comparisons'] == 76
                and receipt['all_original_nodes'] == 625
                and receipt['all_source_columns_at_max_degree'] == 230,
                'incomplete rotated acceptance: '+rule)
        require(receipt['producer_source']['sha256'] == '49b45df9c2c28e3e63e9b886ff873a744ea0f0a44cd5f51fe2e3a345eec81552'
                and receipt['native_source']['sha256'] == 'b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc',
                'unexpected rotated source identity')
        rotated[rule] = dict(grid='rotated', rule=rule,
                             endpoints=pinned(receipt['producer_endpoints']),
                             independent_endpoints=pinned(receipt['native_endpoints']),
                             acceptance_receipt=ident(path))
    triangle = []
    for rule in RULES:
        comparisons = [c for c in prior['comparisons']
                       if c['rows'] == [['triangle', rule, degree] for degree in range(2, 21)]]
        require(len(comparisons) == 1, 'missing/duplicate prior T24 case: '+rule)
        comparison = comparisons[0]
        require(comparison['status'] == 'PASS exact independent/producer row identities'
                and len(comparison['inputs']) == 2, 'invalid prior T24 comparison')
        native, producer = comparison['inputs']
        require(native['path'].endswith('.jsonl') and producer['path'].endswith('/endpoints.json'),
                'unexpected original canonical endpoint identities')
        triangle.append((rule, comparison, pinned(producer), pinned(native)))
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    cases = []
    for rule, comparison, producer, native in triangle:
        receipt = dict(status='PASS derived T24 case identity link to prior actual exact acceptance; no new rerun',
                       grid='triangle', rule=rule, degrees=list(range(2, 21)),
                       endpoints=producer, independent_endpoints=native,
                       prior_actual_acceptance=ident(prior_path),
                       prior_case_comparison=comparison,
                       derivation_code=ident(__file__),
                       limits='Identity-only derivation from retained actual comparison; no new scientific execution.')
        path = out/f'triangle-{rule}-acceptance-link.json'
        path.write_text(json.dumps(receipt, indent=2)+'\n')
        cases.append(dict(grid='triangle', rule=rule, endpoints=producer,
                          independent_endpoints=native, acceptance_receipt=ident(path)))
    cases.extend(rotated[rule] for rule in RULES)
    manifest = dict(schema='g1-fit-input-v1',
                    source_metric='PD-T137 aggregate all-source spectral normal output',
                    tie_convention='X wins exact ties', frozen_source_sha256=FROZEN,
                    cases=cases, full_row_count=152,
                    provenance=dict(builder=ident(__file__), prior_T24_actual_acceptance=ident(prior_path)),
                    fit_execution='NOT RUN; root must inspect full acceptance and issue START before any real fit')
    path = out/'manifest.json'
    path.write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(dict(status='PASS built full eight-case acceptance manifest; real fits NOT RUN',
                          manifest=ident(path), cases=8, rows=152), indent=2))


if __name__ == '__main__':
    main()
