"""Replay D3 whole-cell Bernstein partitions and exact E-P witnesses."""
import argparse
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import time

import d3_edge_common as c


def check_pair(run, identity):
    n, j, k, target = identity
    assert tuple(run[key] for key in ('n', 'j', 'source', 'target')) == identity
    assert run['source_interval'] == list(c.source_interval(n, k))
    assert run['target_mesh'] == str(target)
    assert run['target_cosine_interval'] == list(c.cosine_mesh(n, target))
    threshold = c.lambda_interval(n, j, target)[0]
    assert run['target_lower'] == threshold
    leaves, ancestors = {}, set()
    for row in run['leaves']:
        path = row['path']
        assert isinstance(path, str) and set(path) <= {'0', '1'} and len(path) <= 24
        assert path not in leaves
        leaves[path] = row
    assert leaves and run['pending'] == []
    for path in leaves:
        for i in range(len(path)):
            assert path[:i] not in leaves
            ancestors.add(path[:i])
    stack, reached = [('', c.source_bernstein(n, j, k))], set()
    while stack:
        path, coefficients = stack.pop()
        if path in leaves:
            bound = c.upper(coefficients)
            assert leaves[path] == {'path': path, 'upper': bound}
            assert bound < threshold
            reached.add(path)
        else:
            assert path in ancestors, 'uncovered source interval'
            left, right = c.split(coefficients)
            stack.extend(((path + '1', right), (path + '0', left)))
    assert reached == set(leaves)
    margin = threshold - max(row['upper'] for row in leaves.values())
    assert margin > 0
    return {'n': n, 'j': j, 'source': k, 'target': target,
            'leaves': len(leaves), 'margin_lower_scaled': margin,
            'source_upper_scaled': max(row['upper'] for row in leaves.values()),
            'target_lower_scaled': threshold}


def check(data):
    assert data['format'] == c.FORMAT and data['source_checkpoint'] == c.CHECKPOINT
    assert data['precision'] == c.g.PRECISION and data['scale'] == c.g.S
    assert data['source_sha256'] == c.source_hashes()
    assert data['complete'] is True and data['producer_accepted'] is False
    assert c.arithmetic_controls()
    expected = c.pairs()
    assert len(data['pairs']) == len(expected)
    pairs = [check_pair(run, identity) for run, identity in zip(data['pairs'], expected)]
    witnesses, witness_identities = [], set()
    for row in data['ep_exact_witnesses']:
        phase = F(row['phase'])
        assert phase in c.PHASES
        identity = (row['n'], row['j'], row['source'], row['target'], phase)
        assert identity not in witness_identities
        actual = c.witness(row['n'], row['j'], row['source'], row['target'], phase)
        assert row == actual and actual['reversal_lower'] > 0
        witness_identities.add(identity)
        witnesses.append(actual)
    assert (12, 0, 5, 7, F(-1, 2)) in witness_identities, 'designated E-P witness missing'
    return {'accepted': True, 'arithmetic': 'outward integer intervals; exact rational transforms',
            'verified_claim': 'strict whole-cell E-C at all registered n7,n12 directed pairs',
            'pairs': pairs, 'exact_EP_reversal_witnesses': witnesses,
            'count_n7': sum(r['n'] == 7 for r in pairs), 'count_n12': sum(r['n'] == 12 for r in pairs)}


def controls(data):
    rejected = []
    def reject(label, mutation):
        changed = copy.deepcopy(data)
        mutation(changed)
        try:
            check(changed)
        except (AssertionError, KeyError, ValueError, TypeError):
            rejected.append(label)
        else:
            raise AssertionError('malformed certificate accepted: ' + label)
    reject('missing_pair', lambda d: d['pairs'].pop())
    reject('wrong_pair', lambda d: d['pairs'][0].update(target=2))
    reject('nonedge_index', lambda d: d['pairs'][0].update(j=1))
    reject('missing_leaf', lambda d: d['pairs'][0]['leaves'].pop())
    reject('duplicate_leaf', lambda d: d['pairs'][0]['leaves'].append(copy.deepcopy(d['pairs'][0]['leaves'][0])))
    reject('invalid_path', lambda d: d['pairs'][0]['leaves'][0].update(path='X'))
    reject('forged_upper', lambda d: d['pairs'][0]['leaves'][0].update(upper=0))
    reject('forged_target_lower', lambda d: d['pairs'][0].update(target_lower=d['pairs'][0]['target_lower'] + 1))
    reject('changed_source_interval', lambda d: d['pairs'][0]['source_interval'].__setitem__(0, 0))
    reject('target_sample_outside', lambda d: d['pairs'][0].update(target_mesh='100'))
    reject('changed_source', lambda d: d['source_sha256'].update({'code/gated/d3_edge_common.py': '0' * 64}))
    reject('false_complete', lambda d: d.update(complete=False))
    reject('producer_self_approval', lambda d: d.update(producer_accepted=True))
    reject('missing_designated_EP_witness', lambda d: d.update(ep_exact_witnesses=[
        row for row in d['ep_exact_witnesses']
        if (row['n'], row['j'], row['source'], row['target'], F(row['phase']))
        != (12, 0, 5, 7, F(-1, 2))]))
    reject('duplicate_EP_witness', lambda d: d['ep_exact_witnesses'].append(copy.deepcopy(d['ep_exact_witnesses'][0])))
    reject('nonpositive_EP_reversal', lambda d: d['ep_exact_witnesses'][0].update(reversal_lower=0))
    reject('unregistered_EP_phase', lambda d: d['ep_exact_witnesses'][0].update(phase='100'))
    return {'malformed_cases_rejected': rejected, 'count': len(rejected)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--controls', action='store_true')
    args = parser.parse_args()
    start = time.process_time()
    data = json.loads(args.certificate.read_text())
    result = check(data)
    if args.controls:
        result['malformed_controls'] = controls(data)
    result.update(certificate_sha256=c.digest(args.certificate), checker_sha256=c.digest(__file__),
                  source_sha256=c.source_hashes(), cpu_seconds=time.process_time() - start)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
