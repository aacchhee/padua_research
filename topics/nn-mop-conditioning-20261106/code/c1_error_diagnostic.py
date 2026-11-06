#!/usr/bin/env python3
"""Compare authenticated C4 spectral errors with C1 condition bounds.

This measures a forward-error diagnostic; it does not establish stability.
"""
import csv
import hashlib
import json
from pathlib import Path
import platform

TOPIC = Path(__file__).resolve().parents[1]
MATRIX = Path('/tmp/nn-mop-conditioning-20261106/c1-matrix-all.json')


def main():
    matrices = json.loads(MATRIX.read_text())['cases']
    inputs = {str(MATRIX): hashlib.sha256(MATRIX.read_bytes()).hexdigest()}
    receipt_path = TOPIC/'c4-comparison-receipt.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['M2'] == receipt['M4'] == 'PASS'
    assert receipt['binary64_input_equality_cases'] == 58
    assert receipt['case_count'] == 116 and not receipt['failures']
    inputs[str(receipt_path)] = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
    cases = []
    u = 2**-53
    for family in ('krawtchouk', 'hahn'):
        for method in ('CORE', 'REORTH', 'KRYL'):
            path = TOPIC/'c4-tables'/f'{family}-{method}.csv'
            inputs[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
            assert inputs[str(path)] == receipt['tables'][path.name]['sha256']
            raw = list(csv.DictReader(path.open()))
            for kind in ('archive_integer', 'shared_normalized'):
                key = 'integer_node_input_lower' if kind == 'archive_integer' else 'normalized_node_input_lower'
                rows = []
                for row in raw:
                    if row['input_kind'] != kind:
                        continue
                    assert row['status'] == 'ok'
                    N = int(row['N'])
                    bounds = matrices[family][str(N)]
                    error = float(row['H_integer'])
                    lo, hi = bounds[key], bounds['upper_both_inputs']
                    rows.append({'N': N, 'H_relative_spectral_error': error,
                                 'condition_times_u_bounds': [lo*u, hi*u],
                                 'error_over_condition_u_bounds': [error/(hi*u), error/(lo*u)]})
                assert [r['N'] for r in rows] == list(range(4, 33))
                cases.append({'family': family, 'method': method, 'input_kind': kind,
                              'count': len(rows),
                              'first_N_lower_condition_u_ge_one': next((r['N'] for r in rows if r['condition_times_u_bounds'][0] >= 1), None),
                              'largest_lower_error_over_condition_u': max(rows, key=lambda r: r['error_over_condition_u_bounds'][0]),
                              'largest_upper_error_over_condition_u': max(rows, key=lambda r: r['error_over_condition_u_bounds'][1]),
                              'N16': next(r for r in rows if r['N'] == 16),
                              'N32': rows[-1]})
    out = {'status': 'MEASURED; first-order capacity diagnostic, not a stability theorem',
           'source_commit': 'b4a04981d42c7cd872957facf5e3995e4096ca67',
           'python': platform.python_version(), 'u': u, 'input_sha256': inputs,
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'cases': cases,
           'limitations': ['Condition bounds are at the exact rational reference input; errors include input rounding and algorithm arithmetic.',
                           'C4 errors are platform-specific and table-rounded; no outward interval or claimed universal constant.',
                           'Once condition*u is large, these local ratios give no finite-epsilon accuracy guarantee.',
                           'No source-paper numerical table value was freshly authenticated by this code.']}
    path = TOPIC/'c1-error-comparison.json'
    path.write_text(json.dumps(out, separators=(',', ':'), sort_keys=True)+'\n')
    print(json.dumps({'path': str(path), 'bytes': path.stat().st_size,
                      'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'error_rows': 348}))


if __name__ == '__main__':
    main()
