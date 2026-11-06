#!/usr/bin/env python3
"""Check C1 coverage/precision and summarize numerically evaluated bounds."""
import argparse
import csv
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import platform
import re
import sys
import mpmath as mp
import numpy as np
import c1_metrics as c1

TOPIC = Path(__file__).resolve().parents[1]
HISTORICAL = c1.ROOT/'topics/nn-mop-stability-20261105/attempts/D1.md'


def fit(values):
    pairs = [(N, mp.log(v)) for N, v in values.items() if 32 <= N <= 64]
    center = sum(N for N, _ in pairs)/mp.mpf(len(pairs))
    return mp.exp(sum((N-center)*v for N, v in pairs)/sum((N-center)**2 for N, _ in pairs))


def bounded_fit(lower, upper):
    sizes = list(range(32, 65))
    center = mp.mpf(48)
    denominator = sum((N-center)**2 for N in sizes)
    lo = hi = mp.mpf(0)
    for N in sizes:
        coefficient = (N-center)/denominator
        a, b = mp.log(lower[N]), mp.log(upper[N])
        assert a <= b, (N, a, b)
        lo += coefficient*(a if coefficient >= 0 else b)
        hi += coefficient*(b if coefficient >= 0 else a)
    return [float(mp.exp(lo)), float(mp.exp(hi))]


def historical():
    rows = {}
    for line in HISTORICAL.read_text().splitlines():
        match = re.fullmatch(r'\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', line)
        if not match:
            continue
        N = int(match[1])
        vals = []
        for text in match.groups()[1:]:
            rounded = Decimal(text.strip())
            # Envelope for the last displayed place, not an interval proof of
            # the underlying 260-digit floating derivative calculation.
            radius = Decimal(5).scaleb(rounded.as_tuple().exponent-1)
            vals.append(mp.mpf(str(rounded+radius)))
        rows[N] = {'krawtchouk': {'NN': vals[0], 'step': vals[2]},
                   'hahn': {'NN': vals[1], 'step': vals[3]}}
    assert set(rows) == set(range(4, 65))
    return rows


def scientific_floats(obj):
    if isinstance(obj, dict):
        return {k: scientific_floats(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [scientific_floats(v) for v in obj]
    if isinstance(obj, str):
        try:
            return mp.mpf(obj)
        except ValueError:
            return obj
    return obj


def precision_differences(a, b, mode):
    worst = mp.mpf(0)
    for x, y in zip(a['cases'], b['cases']):
        if mode == 'scalar':
            pairs = [(xm['kappa'][metric][model], ym['kappa'][metric][model])
                     for xm, ym in zip(x['marginals'], y['marginals'])
                     for metric in xm['kappa'] for model in xm['kappa'][metric]]
        else:
            pairs = [(x[target][model], y[target][model]) for target in ('NN_gauge_lower', 'step_gauge_lower')
                     for model in x[target]]
        for u, v in pairs:
            u, v = mp.mpf(u), mp.mpf(v)
            worst = max(worst, abs(u-v)/max(abs(v), mp.mpf('1e-200')))
    return worst


def matrix_bounds(N, family, terminal, upper_sl):
    """Authenticated monic integer-node H; paper M=N-1 convention."""
    xq, wq = c1.base.inputs(N, family)
    x = [c1.base.convert(v, mp.mpf) for v in xq]
    w = [[c1.base.convert(v, mp.mpf) for v in row] for row in wq]
    fields, _ = c1.base.layers(N, *(c1.base.marginal(x, row) for row in w))
    step = c1.ad.step_line({nu: {f: c1.ad.Dual(v) for f, v in row.items()} for nu, row in fields.items()}, N)
    d = mp.mpf(N-1)/2
    field_scales = {f: max(abs(row[f].v) for row in step.values()) for f in ('beta', 'gamma', 'delta')}
    H = np.zeros((N, N), dtype=float)
    for k in range(N):
        H[k, k] = float(d*(step[k, 0]['beta'].v+1))
        if k:
            H[k-1, k] = float(d*d*step[k, 0]['gamma'].v)
        if k >= 2:
            H[k-2, k] = float(d**3*step[k, 0]['delta'].v)
        if k+1 < N:
            H[k+1, k] = 1
    norm = np.linalg.norm(H, ord=2)
    common_upper = upper_sl*mp.sqrt(N*sum((d**degree*field_scales[f])**2
                                        for degree, f in enumerate(('beta', 'gamma', 'delta'), 1)))/norm
    node = mp.mpf(terminal['node_numerator'])
    weight = mp.mpf(terminal['weight_numerator'])
    return {'spectral_norm': float(norm),
            'integer_node_input_lower': float((node+d*weight)/norm),
            'normalized_node_input_lower': float(d*(node+weight)/norm),
            'upper_both_inputs': float(common_upper)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--raw-dir', type=Path, default=Path('/tmp/nn-mop-conditioning-20261106'))
    ap.add_argument('--output', type=Path, default=TOPIC/'c1-summary.json')
    ap.add_argument('--grid', type=Path, default=TOPIC/'c1-grid.csv')
    ap.add_argument('--matrix-raw', type=Path, default=Path('/tmp/nn-mop-conditioning-20261106/c1-matrix-all.json'))
    args = ap.parse_args()
    sizes = list(range(4, 65))
    models = ('mixed', 'spacing', 'componentwise_nodes', 'fixed_mass')
    loaded, artifacts, comparisons = {}, [], {}
    with mp.workdps(320):
        old = historical()
        for family in ('krawtchouk', 'hahn'):
            loaded[family] = {}
            for mode in ('scalar', 'terminal'):
                datasets = []
                for dps in (180, 260):
                    path = args.raw_dir/f'c1-{mode}-{family}{dps}.json'
                    payload = path.read_bytes()
                    data = json.loads(payload)
                    assert [r['N'] for r in data['cases']] == sizes
                    assert all(r['family'] == family and r['dps'] == dps for r in data['cases'])
                    assert data['code_sha256'] == hashlib.sha256(Path(c1.__file__).read_bytes()).hexdigest()
                    datasets.append(data)
                    artifacts.append({'path': str(path), 'bytes': len(payload),
                                      'sha256': hashlib.sha256(payload).hexdigest(),
                                      'elapsed_seconds': data['elapsed_seconds']})
                difference = precision_differences(*datasets, mode)
                assert difference < mp.mpf('1e-60'), (family, mode, difference)
                comparisons[family+'_'+mode] = mp.nstr(difference, 9)
                loaded[family][mode] = {r['N']: r for r in datasets[1]['cases']}
        scalars, gauges, matrices, all_matrices = {}, {}, {}, {}
        grid = []
        for family in ('krawtchouk', 'hahn'):
            scalars[family], gauges[family], matrices[family] = {}, {}, {}
            scalar = loaded[family]['scalar']
            terminal = loaded[family]['terminal']
            for marginal in (1, 2):
                result = {}
                for metric in ('monic', 'orthonormal'):
                    result[metric] = {}
                    for model in models:
                        values = {N: mp.mpf(scalar[N]['marginals'][marginal-1]['kappa'][metric][model]) for N in sizes}
                        result[metric][model] = {'fit_ratio32_64': float(fit(values)),
                                                'N4': float(values[4]), 'N32': float(values[32]), 'N64': float(values[64])}
                scalars[family][str(marginal)] = result
            for target, key in (('NN', 'NN_gauge_lower'), ('step', 'step_gauge_lower')):
                lower = {N: mp.mpf(terminal[N][key]['mixed']) for N in sizes}
                upper = {N: old[N][family][target] for N in sizes}
                gauges[family][target] = {'fit_ratio32_64_interval': bounded_fit(lower, upper),
                                         'monic_fit_ratio32_64': float(fit(upper)),
                                         'endpoint_bounds': {str(N): [float(lower[N]), float(upper[N])] for N in (4, 16, 32, 64)},
                                         'variant_fit_intervals': {model: bounded_fit({N: mp.mpf(terminal[N][key][model]) for N in sizes}, upper) for model in models}}
            mats = {N: matrix_bounds(N, family, terminal[N], old[N][family]['step']) for N in sizes}
            all_matrices[family] = mats
            for model in ('integer_node_input_lower', 'normalized_node_input_lower'):
                lo = {N: mp.mpf(mats[N][model]) for N in sizes}
                hi = {N: mp.mpf(mats[N]['upper_both_inputs']) for N in sizes}
                matrices[family][model] = {'fit_ratio32_64_interval': bounded_fit(lo, hi),
                                           'endpoint_bounds': {str(N): [float(lo[N]), float(hi[N])] for N in (4, 16, 32, 64)}}
        for N in sizes:
            row = {'N': N}
            for family, alias in (('krawtchouk', 'K'), ('hahn', 'H')):
                t = loaded[family]['terminal'][N]
                row[alias+'_NN_lower'] = mp.nstr(mp.mpf(t['NN_gauge_lower']['mixed']), 7)
                row[alias+'_SL_lower'] = mp.nstr(mp.mpf(t['step_gauge_lower']['mixed']), 7)
                for m in (1, 2):
                    for metric, code in (('monic', 'mon'), ('orthonormal', 'sym')):
                        value = loaded[family]['scalar'][N]['marginals'][m-1]['kappa'][metric]['mixed']
                        row[f'{alias}{m}_{code}'] = mp.nstr(mp.mpf(value), 7)
            grid.append(row)
        args.matrix_raw.write_text(json.dumps({'status': 'MEASURED; induced box-to-spectral bounds, not exact norm',
                                               'cases': all_matrices}, indent=2, sort_keys=True)+'\n')
        matrix_payload = args.matrix_raw.read_bytes()
        artifacts.append({'path': str(args.matrix_raw), 'bytes': len(matrix_payload),
                          'sha256': hashlib.sha256(matrix_payload).hexdigest()})
        result = {'status': 'MEASURED; analytic bounds evaluated numerically, not outward enclosures',
                  'source_commit': 'b4a04981d42c7cd872957facf5e3995e4096ca67',
                  'coverage': {'sizes': [4, 64], 'all_integer_sizes': 61, 'families': ['krawtchouk', 'hahn'],
                               'precisions': [180, 260], 'scalar_marginals_per_family': 2},
                  'python': platform.python_version(), 'mpmath': mp.__version__, 'numpy': np.__version__,
                  'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'producer_sha256': hashlib.sha256(Path(c1.__file__).read_bytes()).hexdigest(),
                  'precision_max_relative_differences': comparisons,
                  'scalar_controls': scalars, 'gauge_bounds': gauges, 'monic_integer_H_spectral_bounds': matrices,
                  'raw_artifacts': artifacts,
                  'limitations': ['Pointwise lower is one terminal diagonal row; upper is identity gauge from historical full table.',
                                  'Signed OLS interval is for every sequence between pointwise bounds, not a fit of lower envelope alone.',
                                  'No exact gauge optimizer, outward enclosure or all-N Hahn rate.',
                                  'Matrix spectral lower/upper do not compute the exact induced box-to-spectral norm.',
                                  'Raw artifacts are regenerable local working outputs; external cold storage unconfigured.']}
        args.output.write_text(json.dumps(result, separators=(',', ':'), sort_keys=True)+'\n')
        with args.grid.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(grid[0]))
            writer.writeheader()
            writer.writerows(grid)
        print(json.dumps({'summary': str(args.output), 'bytes': args.output.stat().st_size,
                          'grid': str(args.grid), 'grid_bytes': args.grid.stat().st_size,
                          'precision': comparisons, 'gauge_bounds': gauges,
                          'matrix_bounds': matrices}, indent=2))


if __name__ == '__main__':
    main()
