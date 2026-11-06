#!/usr/bin/env python3
"""Render explicit D1 JSON inputs; artifacts and a hash manifest go to outputdir.

No data discovery, fallback, fitting, or missing-row interpolation is performed.
The optional Krawtchouk analytic lower envelope is the maximum of equations
(1), (2), and (13) in the explicitly hashed theory source. Rendering uses binary64;
it adds no proof or certification to the underlying numerical measurements.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
import tempfile
from pathlib import Path
import platform
import sys

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'nn-mop-matplotlib-cache'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter

SAMPLED = [4, 8, 12, 16, 24, 32, 48, 64]


def identity(path):
    return dict(path=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def read_cases(path, family):
    data = json.loads(path.read_text())
    cases = data['cases']
    if not cases:
        raise ValueError(f'{path}: no cases')
    rows = {}
    for case in cases:
        n = case['N']
        if not isinstance(n, int) or n < 2 or n in rows:
            raise ValueError(f'{path}: invalid/duplicate size {n}')
        if case['family'] != family:
            raise ValueError(f'{path}: expected family {family}, got {case["family"]}')
        values = [float(case[key]['mixed']['kappa']) for key in ['NN', 'step_line']]
        if not all(math.isfinite(v) and v > 0 for v in values):
            raise ValueError(f'{path}: nonpositive/nonfinite kappa at N={n}')
        rows[n] = values
    sizes = sorted(rows)
    return sizes, [[rows[n][j] for n in sizes] for j in range(2)], data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--krawtchouk', type=Path, required=True)
    parser.add_argument('--hahn', type=Path, required=True)
    parser.add_argument('--outputdir', type=Path, required=True)
    parser.add_argument('--grid-label', choices=['sampled8sizes', 'fullgrid61', 'custom'], required=True)
    parser.add_argument('--bound-source', type=Path)
    parser.add_argument('--bound-sha256')
    args = parser.parse_args()
    if bool(args.bound_source) != bool(args.bound_sha256):
        parser.error('--bound-source and --bound-sha256 must be supplied together')
    bound_identity = None
    if args.bound_source:
        bound_identity = identity(args.bound_source)
        if bound_identity['sha256'] != args.bound_sha256:
            raise ValueError('lower-bound source hash differs from explicit frozen hash')
        text = args.bound_source.read_text()
        if any(formula not in text for formula in ['5^(N−1)/(N−1)', '(4 sqrt(6))^(N−1)', '(5+2 sqrt(6))^(N−2)']):
            raise ValueError('bound source does not contain the specified two formulas')
    inputs = {}
    tables = {}
    for family in ['krawtchouk', 'hahn']:
        path = getattr(args, family)
        sizes, values, data = read_cases(path, family)
        tables[family] = (sizes, values)
        inputs[family] = identity(path)
        inputs[family]['producer_code_sha256'] = data.get('code_sha256')
        inputs[family]['precision_dps'] = sorted(set(c['dps'] for c in data['cases']))
    sizes = tables['krawtchouk'][0]
    if sizes != tables['hahn'][0]:
        raise ValueError('the two explicit input files have different size grids')
    if args.grid_label == 'sampled8sizes' and sizes != SAMPLED:
        raise ValueError('sampled8sizes requires exactly N=4,8,12,16,24,32,48,64')
    if args.grid_label == 'fullgrid61' and sizes != list(range(4, 65)):
        raise ValueError('fullgrid61 requires every integer N=4,...,64')

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'svg.fonttype': 'none', 'pdf.fonttype': 42})
    fig, axes = plt.subplots(1, 2, figsize=(8.3, 4.2), sharex=True, sharey=True)
    for ax, family in zip(axes, ['krawtchouk', 'hahn']):
        grid, values = tables[family]
        marker = 'o' if len(grid) <= 12 else None
        ax.semilogy(grid, values[0], color='#175e95', marker=marker,
                    markersize=3.7, linewidth=1.6, label='NN triangle')
        ax.semilogy(grid, values[1], color='#ba542d', marker='s' if marker else None,
                    markersize=3.4, linewidth=1.4, label='Monic step-line')
        if family == 'krawtchouk' and bound_identity:
            bound_grid = list(range(min(grid), max(grid) + 1))
            bounds = [max(5.0**(n-1)/(n-1),
                          (4*math.sqrt(6))**(n-1)/(4*(n-1)*(n-2)),
                          5*((5+2*math.sqrt(6))**(n-2)+(5-2*math.sqrt(6))**(n-2))/(2*(n-1)**2))
                      for n in bound_grid]
            ax.semilogy(bound_grid, bounds, color='#323232', linestyle='--',
                        linewidth=1.35, label='Analytic NN lower bound')
        ax.set_title('Krawtchouk' if family == 'krawtchouk' else 'Hahn', loc='left')
        ax.set_xlabel('Number of common support nodes, N')
        ax.set_xticks([4, 16, 32, 48, 64])
        ax.grid(axis='y', which='major', color='#dedede', linewidth=.55)
        ax.yaxis.set_major_locator(LogLocator(base=10, numticks=8))
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.legend(loc='upper left', frameon=False, fontsize=8)
    axes[0].set_ylabel(r'Induced derivative condition number, $\kappa$ (log scale)')
    caption = {'sampled8sizes': 'Sampled 8 sizes: N = 4, 8, 12, 16, 24, 32, 48, 64.',
               'fullgrid61': 'Every integer size N = 4,...,64.',
               'custom': 'Explicit supplied size grid: ' + ', '.join(map(str, sizes)) + '.'}[args.grid_label]
    footer = (caption + '\nMixed input: unit-scale nodes and relative weights; relative field-sup output norms.'
              '\nNumerical derivative norms; precision convergence is not certification. Lines connect measurements.')
    if bound_identity:
        footer += '\nDashed: analytic Krawtchouk lower envelope, equations (1), (2), (13); mandatory audit pending.'
    fig.suptitle('Sensitivity of nearest-neighbour and monic step-line coefficients', x=.08, ha='left', fontsize=11)
    fig.subplots_adjust(left=.085, right=.985, top=.855, bottom=.31, wspace=.12)
    fig.text(.085, .025, footer, fontsize=7.2, va='bottom', linespacing=1.5)
    args.outputdir.mkdir(parents=True, exist_ok=True)
    stem = 'conditioning-' + args.grid_label
    outputs = []
    for ext in ['png', 'pdf', 'svg']:
        path = args.outputdir / (stem + '.' + ext)
        fig.savefig(path, dpi=220, facecolor='white')
        outputs.append(identity(path))
    plt.close(fig)
    manifest = dict(status='rendering of existing measured data; no new scientific claim',
                    created_utc=datetime.now(timezone.utc).isoformat(), argv=sys.argv[1:],
                    code=identity(Path(__file__)), inputs=inputs,
                    lower_bound_source=bound_identity, output=outputs,
                    grid_label=args.grid_label, sizes=sizes, caption=caption,
                    bound_formulas=['5^(N-1)/(N-1)', '(4sqrt(6))^(N-1)/[4(N-1)(N-2)]',
                                    '5*((5+2sqrt(6))^(N-2)+(5-2sqrt(6))^(N-2))/[2(N-1)^2]'] if bound_identity else [],
                    versions=dict(python=platform.python_version(), matplotlib=matplotlib.__version__),
                    metric='mixed input; NN four relative field sup norms; monic step-line three relative field sup norms',
                    numerical_note='Connecting measured points does not establish values between samples; no fit is plotted.')
    manifest_path = args.outputdir / (stem + '-manifest.json')
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
    print(json.dumps(dict(manifest=str(manifest_path.resolve()), outputs=outputs), indent=2))


if __name__ == '__main__':
    main()
