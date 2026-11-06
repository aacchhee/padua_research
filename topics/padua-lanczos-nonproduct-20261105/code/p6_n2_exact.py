#!/usr/bin/env python3
"""Certified new-plan N2 screen after complete two-path weighted scans."""
import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from p6_rows import compare, FIELDS
from p6_n2_compact import interval_slope

ROOT = Path(__file__).resolve().parents[3]
OLD = ROOT/'topics/padua-lanczos-frontier-20261105/code'
sys.path.insert(0, str(OLD))
import g1_fit as logs
import g1_fit_independent as independent_logs


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def verdict(windows):
    if all(lo > Q(1, 10) for lo, hi in windows):
        return 'PASS measured exponential screen'
    if all(hi < Q(1, 50) for lo, hi in windows):
        return 'REDIRECT polynomial-bound question'
    return 'INCONCLUSIVE'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scan-receipt', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    receipt = json.loads(args.scan_receipt.read_text())
    assert receipt['status'] == 'PASS exact two-path weighted finite scan'
    assert receipt['max_degree'] >= 16
    family, count = receipt['family'], receipt['input']['point_count']
    rows = {}
    for run in receipt['runs']:
        assert run['status'].startswith('PASS')
        path = Path(run['output']['path'])
        assert identity(path) == run['output']
        values = [json.loads(x) for x in path.read_text().splitlines()]
        assert [r['degree'] for r in values] == list(range(2, receipt['max_degree']+1))
        rows[run['backend'], run['rule']] = values
    assert set(rows) == {(b, r) for b in ('producer', 'checker') for r in ('bj', 'mirror', 'alt', 'pivot')}
    for rule in ('bj', 'mirror', 'alt', 'pivot'):
        for a, b in zip(rows['producer', rule], rows['checker', rule]):
            compare(a, b, family, count)
    endpoint = {(rule, r['degree']): (Q(r[FIELDS[0]]['exact']), Q(r[FIELDS[-1]]['exact']))
                for (backend, rule), values in rows.items() if backend == 'producer' for r in values}
    inputs, primary, checked = {}, {}, {}
    for degree in range(8, 17):
        bounds = [endpoint[rule, degree] for rule in ('bj', 'mirror', 'alt', 'pivot')]
        lower = endpoint['bj', degree][0]/min(hi for lo, hi in bounds)
        upper = endpoint['bj', degree][1]/min(lo for lo, hi in bounds)
        assert 0 < lower <= upper
        inputs[degree] = {'lower_squared_ratio': str(lower), 'upper_squared_ratio': str(upper)}
        a, b = logs.logq(lower, 128), logs.logq(upper, 128)
        c, d = independent_logs.logq(lower, 128), independent_logs.logq(upper, 128)
        assert max(a.a, c.lo) <= min(a.b, c.hi)
        assert max(b.a, d.lo) <= min(b.b, d.hi)
        primary[degree], checked[degree] = (a.a/2, b.b/2), (c.lo/2, d.hi/2)
    windows, primary_slopes, checked_slopes = [], [], []
    for start, end in ((8, 12), (12, 16)):
        lo, hi = interval_slope([(s, *primary[s]) for s in range(start, end+1)])
        # Separate OLS computation: enumerate all corners with exact
        # unnormalized centered integer coefficients, using other log path.
        corners = [sum(coef*checked[s][pick] for s, coef, pick in
                       zip(range(start, end+1), (-2, -1, 0, 1, 2), choice))/10
                   for choice in itertools.product((0, 1), repeat=5)]
        clo, chi = min(corners), max(corners)
        assert max(lo, clo) <= min(hi, chi)
        primary_slopes.append((lo, hi)); checked_slopes.append((clo, chi))
        windows.append({'degrees': [start, end], 'lower_exact': str(lo), 'upper_exact': str(hi),
                        'checker_lower_exact': str(clo), 'checker_upper_exact': str(chi),
                        'decimal_display': [float(lo), float(hi)],
                        'checker': 'PASS separate rational logs and all32 OLS corners'})
    assert verdict(primary_slopes) == verdict(checked_slopes)
    result = {'status': 'PASS exact outward logs and two-path OLS screen', 'family': family,
              'N2_verdict': verdict(primary_slopes), 'scan_receipt': identity(args.scan_receipt),
              'code': identity(__file__), 'log_producer': identity(OLD/'g1_fit.py'),
              'log_checker': identity(OLD/'g1_fit_independent.py'),
              'slope_helper': identity(Path(__file__).with_name('p6_n2_compact.py')),
              'command': [sys.executable, '-B', *sys.argv], 'precision_fractional_bits': 128,
              'comparator_rules': ['bj', 'mirror', 'alt', 'pivot'], 'windows': windows,
              'logratio_outward': {str(s): [str(a), str(b)] for s, (a, b) in primary.items()},
              'scope': 'MEASURED finite endpoint-interval screen; no true-capacity equality or asymptotic rate',
              'verification_limit': 'Separate algorithms executed by same worker; distinct-agent rerun/audit remains separate.'}
    # Huge endpoint ratios remain recoverable from pinned scan rows; do not
    # duplicate their large rational strings in the short result receipt.
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'family': family, 'N2_verdict': result['N2_verdict'], 'windows': windows}, indent=2))


if __name__ == '__main__':
    main()
