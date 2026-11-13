#!/usr/bin/env python3
"""Independent synthetic block deletion versus fresh SVD, no science supports."""
from datetime import datetime, timezone
import itertools
import json
import os
from pathlib import Path
import platform
import sys
import time
import numpy as np
import scipy
import check_pilot as own

TOP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOP/'code'))
import pdpr_core as producer


def main():
    start, utc = time.process_time(), datetime.now(timezone.utc).isoformat()
    expected = {'pdpr_core.py': '12456d1aaa82abc242e9bd3463791be622116abb820b213058e1074f00d3f13a',
                'pdpr_run.py': '9a0b42e8e1b150f4554fa3908163cfce064897869bb68bc52e5c5240ce14f92c',
                'pdpr_collect.py': '3117045003ab41b37b34f737edd4983ebc91f890d5076661a2955531bef32baf'}
    sources = [own.identity(TOP/'code'/name) for name in expected]
    assert all(p['sha256'] == expected[Path(p['path']).name] for p in sources)
    rng = np.random.default_rng(202611070579)
    errors = dict.fromkeys(('map', 'cardinal', 'risk', 'trace', 'amp'), 0.)
    total, rejected, classifications = 0, 0, {True: 0, False: 0}
    for m, n in ((9, 4), (13, 7), (6, 6)):
        A, E = rng.normal(size=(m, n)), rng.normal(size=(23, n))
        Q = np.linalg.qr(A, mode='reduced')[0]
        C = np.linalg.pinv(A)
        H, L = Q@Q.T, E@C
        pairs = list(itertools.combinations(range(m), 2))
        amp_limit, risk_limit = float(np.max(abs(L).sum(axis=1)))*1.15, float(np.sum(C*C))*1.10
        rows, complete = producer.pair_candidates(C, Q, E, pairs, m, amp_limit, risk_limit, time.process_time()+1)
        assert complete and len(rows) == len(pairs)
        for row, pair in zip(rows, pairs):
            keep = np.array([i for i in range(m) if i not in pair])
            assert row['pair'] == list(pair)
            if np.linalg.matrix_rank(A[keep]) < n:
                assert not row['feasible'] and row['reason'] == 'block_rank_eigenvalue'
                rejected += 1
                continue
            fresh = np.linalg.pinv(A[keep])
            predicted, correction, mask = producer.predicted_block(C, H, pair)
            assert np.array_equal(np.flatnonzero(mask), keep)
            raw_cards = L[:, keep]+L[:, pair]@correction
            risk = own.integer_risk(fresh, m)[0]
            amp, trace = float(np.max(abs(E@fresh).sum(axis=1))), float(np.sum(fresh*fresh))
            for key, a, b in [('map', predicted, fresh), ('cardinal', raw_cards, E@fresh),
                              ('risk', risk, row['integer_risk']), ('amp', amp, row['train_amp']),
                              ('trace', trace, row['trace'])]:
                errors[key] = max(errors[key], own.relative(a, b))
            feasible = amp <= amp_limit and risk <= risk_limit
            assert row['feasible'] == feasible
            classifications[feasible] += 1
            total += 1
        stopped, complete = producer.pair_candidates(C, Q, E, pairs, m, amp_limit, risk_limit, -1)
        assert not complete and stopped == []
    assert max(errors.values()) < 1e-10
    def row(pair, amp, feasible, risk=1., trace=1.):
        return {'pair': list(pair), 'train_amp': amp, 'feasible': feasible, 'integer_risk': risk, 'trace': trace}
    rows = [row((0, 1), .1, False), row((2, 3), 2., True), row((1, 4), 2.+1e-13, True), row((0, 2), float('nan'), False)]
    assert producer.choose_pair(rows)['pair'] == [1, 4]
    assert producer.choose_pair(rows, excluded={(1, 4)})['pair'] == [2, 3]
    assert producer.choose_pair(rows, feasible_only=False)['pair'] == [0, 1]
    assert producer.choose_pair([rows[0], rows[-1]]) is None
    assert producer.choose_pair([rows[-1]], feasible_only=False) is None
    assert producer.choose_pair([row((0, 1), 1., True, float('inf'))]) is None
    assert producer.choose_pair([row((0, 1), 1., True, trace=float('nan'))]) is None
    assert time.process_time()-start < 2
    out = {'verdict': 'PASS', 'command': sys.argv, 'started_utc': utc,
           'ended_utc': datetime.now(timezone.utc).isoformat(), 'actual_cpu': time.process_time()-start,
           'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
           'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
           'checker': own.identity(__file__), 'helper': own.identity(own.__file__), 'producer_sources': sources,
           'random_seed': 202611070579, 'fresh_SVD_block_comparisons': total, 'rank_rejections': rejected,
           'classification_counts': {str(k): v for k, v in classifications.items()}, 'maximum_relative_errors': errors,
           'ordering_branches': 7, 'cap_stops': 3,
           'scope': 'Synthetic finite preflight only: no parity candidate generation or research round. Actual singleton dense-training comparison, operational-vs-diagnostic labeling, all-controls/cap gate and provenance inspected in frozen driver.',
           'limits': 'No scientific P5 outcome or universal guarantee; formal Claude audit pending.'}
    target = Path(sys.argv[1]); target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: out[k] for k in ('verdict', 'actual_cpu', 'fresh_SVD_block_comparisons', 'rank_rejections', 'maximum_relative_errors')}))


if __name__ == '__main__':
    main()
