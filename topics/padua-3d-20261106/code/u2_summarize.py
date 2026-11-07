#!/usr/bin/env python3
"""Summarize the already registered U2 pilot/degree-transfer gates and traces."""
import argparse
import json
from pathlib import Path
import sys
import u2_core as core


def summarize(receipt_path):
    packed = json.loads(receipt_path.read_text())
    raw = Path(packed['scratch'])
    full_path = raw/'full-results.json'
    full = json.loads(full_path.read_text())
    target = [6, 8] if full['requested_degrees'] == [2, 4, 6, 8] else [10, 12]
    rows = {(r['n'], r['family']): r for r in full['rows']}
    result = {'receipt': str(receipt_path), 'receipt_sha256': core.sha(receipt_path),
              'full_results': {'path': str(full_path), 'bytes': full_path.stat().st_size,
                               'sha256': core.sha(full_path)},
              'scope': 'reused pilot assessment' if target == [6, 8] else 'previously unseen degree holdout',
              'target_degrees': target, 'cases': [], 'passes': False}
    for optimization in full['optimizations']:
        n = optimization['n']
        path = raw/f'n{n}-optimization-events.json'
        events = json.loads(path.read_text())
        trials = [r for r in events if 'rho' in r]
        accepted = [r for r in trials if r['accepted']]
        invariant = all(r['step_max'] <= r['delta']*(1+1e-12)+1e-15 and
                        r['new_separation'] >= .75*r['old_separation']*(1-1e-12)
                        for r in trials)
        inverse_guard = all(r['rho'] <= .5 for r in accepted)
        armijo = all(r['objective'] <= r['armijo_rhs'] for r in accepted)
        local, candidate = rows[n, 'localdet'], rows[n, 'joint_norm']
        result['cases'].append({'n': n, 'N': candidate['N'],
            'fresh_localdet': local['norms'][5], 'fresh_candidate': candidate['norms'][5],
            'ratio': candidate['norms'][5]/local['norms'][5],
            'extra_cpu': optimization['extra_cpu'], 'total_construction_cpu': optimization['candidate_total_cpu'],
            'eligible': candidate['eligible'], 'fallback': optimization['fallback'],
            'dyadic_ranks': candidate['dyadic_ranks'], 'accepted_steps': len(accepted),
            'termination': optimization['termination'], 'geometry_pass': invariant,
            'inverse_guard_pass': inverse_guard, 'armijo_pass': armijo,
            'max_accepted_rho': max((r['rho'] for r in accepted), default=None),
            'minimum_separation_ratio': min((r['pair_separation_ratio'] for r in trials), default=None),
            'events': {'path': str(path), 'bytes': path.stat().st_size, 'sha256': core.sha(path)}})
    all_guarded = all(r['eligible'] and r['extra_cpu'] < 120 and r['geometry_pass'] and
                      r['inverse_guard_pass'] and r['armijo_pass'] for r in result['cases'])
    target_rows = [r for r in result['cases'] if r['n'] in target]
    result['passes'] = all_guarded and len(target_rows) == 2 and all(r['ratio'] <= .95 for r in target_rows)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = {'status': 'MEASURED registered finite gate/trace summary; no exact inverse enclosure',
              'command': sys.argv, 'source_sha256': core.sha(__file__),
              'core_sha256': core.sha(core.__file__),
              'gate_definition': '>=5% fresh refined improvement at both target degrees; all cases guards and extraCPU<120',
              'batches': [summarize(p) for p in args.inputs]}
    args.output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    assert args.output.stat().st_size < 16384
    print(json.dumps({'gates': [[r['target_degrees'], r['passes']] for r in result['batches']],
                      'bytes': args.output.stat().st_size, 'sha256': core.sha(args.output)}))


if __name__ == '__main__':
    main()
