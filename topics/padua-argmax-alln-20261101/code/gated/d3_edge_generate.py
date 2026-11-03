"""Produce bounded whole-cell E-C certificates and separate MEASURED E-P screen."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import time

import d3_edge_common as c


def certify_pair(identity, deadline):
    n, j, k, target = identity
    lower = c.lambda_interval(n, j, target)[0]
    leaves, pending = [], []
    stack = [('', c.source_bernstein(n, j, k))]
    while stack:
        path, coefficients = stack.pop()
        bound = c.upper(coefficients)
        if bound < lower:
            leaves.append({'path': path, 'upper': bound})
        elif len(path) >= 24 or len(leaves) + len(stack) >= 4095 or time.process_time() > deadline:
            pending.append(path)
        else:
            left, right = c.split(coefficients)
            stack.extend(((path + '1', right), (path + '0', left)))
    return {'n': n, 'j': j, 'source': k, 'target': target,
            'source_interval': list(c.source_interval(n, k)),
            'target_mesh': str(target), 'target_cosine_interval': list(c.cosine_mesh(n, target)),
            'target_lower': lower, 'leaves': leaves, 'pending': pending}


def ep_screen():
    sys.path.insert(0, str(c.TOPIC / 'code/part3'))
    from tests_common import Edge
    import numpy as np
    cache = {n: Edge(n) for n in c.DEGREES}
    rows, exact_witnesses = [], []
    for n, j, k, target in c.pairs():
        edge = cache[n]
        name = 'v+' if j == 0 else 'v-'
        for phase in c.PHASES:
            source = edge.one(name, float(k + phase) * np.pi / (n + 1))
            destination = edge.one(name, float(target + phase) * np.pi / (n + 1))
            difference = destination - source
            rows.append({'n': n, 'j': j, 'source': k, 'target': target, 'phase': str(phase),
                         'source_value': source, 'target_value': destination,
                         'target_minus_source': difference, 'measured_reversal': difference < -1e-6})
            if difference < -1e-6:
                exact = c.witness(n, j, k, target, phase)
                assert exact['reversal_lower'] > 0
                exact_witnesses.append(exact)
    return {'status': 'MEASURED', 'arithmetic': 'float64', 'samples': rows,
            'reversal_count': sum(r['measured_reversal'] for r in rows)}, exact_witnesses


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--ep-output', type=Path, required=True)
    args = parser.parse_args()
    started_cpu, started_wall = time.process_time(), time.monotonic()
    assert c.arithmetic_controls()
    ep, witnesses = ep_screen()
    runs = []
    for identity in c.pairs():
        run = certify_pair(identity, started_cpu + 180.)
        runs.append(run)
        print(json.dumps({'pair': identity, 'leaves': len(run['leaves']),
                          'pending': len(run['pending']),
                          'target_lower_approx': run['target_lower'] / c.g.S,
                          'source_upper_approx': max(r['upper'] for r in run['leaves']) / c.g.S,
                          'margin_lower_approx': (run['target_lower'] - max(r['upper'] for r in run['leaves'])) / c.g.S}), flush=True)
    result = {'format': c.FORMAT, 'source_checkpoint': c.CHECKPOINT,
              'precision': c.g.PRECISION, 'scale': c.g.S, 'source_sha256': c.source_hashes(),
              'preregistration_note_sha256': c.digest(c.TOPIC / 'gated/d3/r01-finite.md'),
              'pairs': runs, 'ep_exact_witnesses': witnesses,
              'complete': all(not r['pending'] for r in runs),
              'producer_accepted': False,
              'cpu_seconds': time.process_time() - started_cpu,
              'wall_seconds': time.monotonic() - started_wall}
    ep.update(source_checkpoint=c.CHECKPOINT, source_sha256=c.source_hashes(),
              exact_witness_count=len(witnesses))
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    args.ep_output.write_text(json.dumps(ep, indent=2) + '\n')
    print(json.dumps({'complete': result['complete'], 'cpu_seconds': result['cpu_seconds'],
                      'wall_seconds': result['wall_seconds'], 'ep_reversals': ep['reversal_count'],
                      'ep_exact_witnesses': len(witnesses)}), flush=True)


if __name__ == '__main__':
    main()
