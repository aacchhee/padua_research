#!/usr/bin/env python3
"""Plot recorded finite sampled maxima; this does not estimate asymptotic laws."""
import argparse
import hashlib
import json
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR', '/tmp/padua-lattice-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    degree = list(range(1, 7))
    best = [min(r['sampled_lebesgue'] for r in data['rows']
                if r['n'] == n and r.get('sampled_lebesgue') is not None)
            for n in degree]
    baseline_names = [('lower_discrete_leja', 'Lower set, discrete Leja order'),
                      ('QR_approximate_Fekete_tensor_mesh', 'QR approximate Fekete')]
    plt.rcParams.update({'font.size': 10, 'svg.fonttype': 'none', 'svg.hashsalt': 'padua-lattice'})
    fig, ax = plt.subplots(figsize=(7.4, 4.5), layout='constrained')
    ax.semilogy(degree, best, 'o-', label='Smallest sampled maximum among screened fibers')
    for name, label in baseline_names:
        values = [next(r['sampled_lebesgue'] for r in data['baselines']
                       if r['n'] == n and r['name'] == name) for n in degree]
        ax.semilogy(degree, values, 's--', label=label)
    ax.set(xlabel='Total degree n', ylabel='Sampled Lebesgue maximum (log scale)',
           title='3D Chebyshev tests: finite measurements only', xticks=degree)
    ax.grid(alpha=.25, which='both')
    ax.legend(fontsize=8, loc='upper left')
    fig.text(.5, -.02, '21³ Lobatto test mesh; floating solves. No supremum or growth-law certificate.',
             ha='center', fontsize=8)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, bbox_inches='tight', metadata={'Date': None})
    print(json.dumps({'input_sha256': hashlib.sha256(args.input.read_bytes()).hexdigest(),
                      'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'output_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest(),
                      'output_bytes': args.output.stat().st_size, 'best_sampled': best,
                      'matplotlib': matplotlib.__version__}, sort_keys=True))


if __name__ == '__main__':
    main()
