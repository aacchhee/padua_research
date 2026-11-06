#!/usr/bin/env python3
"""Plot existing CC measurements and registered fits; perform no fit or solve."""
import argparse
import json
import math
import os
import re
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/sharp-matplotlib')
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

TOPIC = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=TOPIC / 'figures/cc-extrapolation.svg')
    parser.add_argument('--preview', type=Path, default=Path('/tmp/sharp-S4/cc-extrapolation.png'))
    args = parser.parse_args()
    rows = json.loads((TOPIC / 'evidence/S4-essential-cc.json').read_text())['rows']
    fits = json.loads((TOPIC / 'evidence/S4-k1-fit.json').read_text())['results']
    plt.rcParams.update({'svg.fonttype': 'none', 'svg.hashsalt': 'sharp-cc-v1',
                         'font.size': 9, 'font.sans-serif': ['DejaVu Sans'], 'axes.spines.top': False,
                         'axes.spines.right': False, 'path.simplify': True})
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    colors = {'even': '#1565a8', 'odd': '#b44b13'}
    for parity, marker in [('even', 'o'), ('odd', 's')]:
        subset = [row for row in rows if row[0] % 2 == (parity == 'odd')]
        ax.plot([1 / math.log(row[0]) for row in subset],
                [math.log(row[0])**2 * row[1] for row in subset],
                linestyle='none', marker=marker, markersize=3.5,
                markerfacecolor='none', markeredgewidth=0.8, color=colors[parity],
                label=f'{parity} N: measured rows')
    for parity in ('even', 'odd'):
        for label, name, style in [('A', 'A_j8_to14', '-'), ('B', 'B_j15_to20', '--')]:
            window = fits[parity]['windows'][name]
            c, a, b = window['coefficients']
            end = 1 / math.log(min(window['Ns']))
            xs = [end * index / 24 for index in range(25)]
            ys = [c if x == 0 else c - a * x * math.log(x) + b * x for x in xs]
            ax.plot(xs, ys, style, linewidth=1.1, color=colors[parity],
                    label=f'{parity} {label}: c={c:.5f} (MEASURED)')
    bound = math.pi**4 / 8
    ax.axhline(bound, color='#555555', linewidth=1, linestyle=(0, (5, 3)),
               label='PROVED limsup bound: pi^4/8')
    ax.set(xlim=(0, 0.225), ylim=(3.8, 13.8), xlabel='1 / log N',
           ylabel='(log N)^2 lambda_min', title='CC finite-window extrapolation')
    ax.set_xticks([0, 0.05, 0.10, 0.15, 0.20])
    ax.set_yticks([4, 6, 8, 10, 12, 14])
    ax.legend(loc='lower left', frameon=False, fontsize=7.5)
    fig.text(0.14, 0.025, 'Registered A/B curves only; intercepts are extrapolations. '
             'The limsup bound is asymptotic, not pointwise in N.', fontsize=7.5)
    fig.subplots_adjust(left=0.11, bottom=0.15, right=0.98, top=0.90)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.preview.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={'Date': None})
    # Compact rendering syntax only: keep text as text and all plotted values.
    svg = args.output.read_text()
    svg = re.sub(r'\s+id="(?:figure|axes|patch|matplotlib.axis|xtick|ytick|line2d|text|legend)_[^"]+"', '', svg)
    svg = re.sub(r' transform="rotate\(-0 [^"]*\)"', '', svg)
    def compact_coordinates(match):
        value = re.sub(r'-?\d+\.\d+',
                       lambda number: f'{float(number.group()):.3f}'.rstrip('0').rstrip('.'),
                       match.group(2))
        value = re.sub(r'\s+', ' ', value).strip()
        return f'{match.group(1)}="{value}"'
    svg = re.sub(r'(d|x|y|transform)="([^"]*)"', compact_coordinates, svg)
    svg = re.sub(r'>\s+<', '><', svg)
    args.output.write_text(svg + '\n')
    fig.savefig(args.preview, dpi=140)
    plt.close(fig)
    size = args.output.stat().st_size
    print(f'{args.output}: {size} bytes; preview: {args.preview}')
    if size >= 16 * 1024:
        raise SystemExit('SVG exceeds the 16 KiB committed-evidence limit; keep local only')


if __name__ == '__main__':
    main()
