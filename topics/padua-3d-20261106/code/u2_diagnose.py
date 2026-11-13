#!/usr/bin/env python3
"""Inspect preserved U2 trials; no optimization, node selection or tuning."""
import argparse
import json
from pathlib import Path
import sys
import numpy as np
import u2_core as core


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--failed-raw', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = {'status': 'MEASURED frozen-iterate diagnosis; no optimization',
              'command': sys.argv, 'source_sha256': core.sha(__file__),
              'core_sha256': core.sha(core.__file__), 'raw': str(args.raw),
              'inputs': {}, 'rows': [], 'failed_execution': {}}
    full = args.raw/'full-results.json'
    data = json.loads(full.read_text())
    result['inputs'][str(full)] = core.sha(full)
    for n in (2, 6, 8):
        eventfile = args.raw/f'n{n}-optimization-events.json'
        trialfile = args.raw/f'n{n}-optimization-trials.npz'
        result['inputs'][str(eventfile)] = core.sha(eventfile)
        result['inputs'][str(trialfile)] = core.sha(trialfile)
        events = json.loads(eventfile.read_text())
        trials = np.load(trialfile)['coordinates']
        E = core.old.basis(np.cos(core.inherited.prev.angular_mesh(21)), n)
        beta = 40/events[0]['train_max']
        rows = []
        for i, flat in enumerate(trials):
            points = flat.reshape(-1, 3)
            singular = np.linalg.svd(core.old.basis(points, n), compute_uv=False)
            distances = np.linalg.norm(points[:, None, :]-points[None, :, :], axis=2)
            np.fill_diagonal(distances, np.inf)
            row = {**events[i], 'step_max': float(np.max(np.abs(flat-trials[0]))),
                   'unique': len(np.unique(points, axis=0)),
                   'minimum_pair_distance': float(distances.min()),
                   'condition2': float(singular[0]/singular[-1]),
                   'bounds_active': int(np.sum(np.abs(flat) >= 1-1e-14))}
            try:
                _, gradient, _ = core.smooth_value_gradient(flat, n, E, beta)
                projected = flat-np.clip(flat-gradient, -1, 1)
                row.update(gradient_inf=float(np.max(np.abs(gradient))),
                           projected_gradient_inf=float(np.max(np.abs(projected))))
            except np.linalg.LinAlgError as error:
                row['gradient_exception'] = str(error)
            rows.append(row)
        termination = next(r['termination'] for r in data['optimizations'] if r['n'] == n)
        result['rows'].append({'n': n, 'termination': termination, 'trials': rows})
    failed = args.failed_raw/'failed-oversize-receipt.json'
    prior = json.loads(failed.read_text())
    result['failed_execution'] = {'reason': '16689-byte receipt exceeded 16384-byte guard',
        'path': str(failed), 'bytes': failed.stat().st_size, 'sha256': core.sha(failed),
        'completed_assessments': len(prior['rows']), 'requested_assessments': 16,
        'command': prior['command'], 'frozen_sources': {
            p.name: {'path': str(p), 'bytes': p.stat().st_size, 'sha256': core.sha(p)}
            for p in args.failed_raw.glob('failed-source-*')},
        'repair': 'serialization only: packed row arrays and nine significant display digits; mathematical core unchanged'}
    args.output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    assert args.output.stat().st_size < 16384
    print(json.dumps({'output': str(args.output), 'bytes': args.output.stat().st_size,
                      'rows': len(result['rows']), 'sha256': core.sha(args.output)}))


if __name__ == '__main__':
    main()
