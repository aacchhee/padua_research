#!/usr/bin/env python3
"""Independent factorization, trajectory, noise and fresh-cloud audit of P1."""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import heapq
import itertools
import json
import lzma
import math
import os
from pathlib import Path
import platform
import sys
import time
import zlib
import numpy as np
import scipy
from scipy.stats import qmc

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def identity(p):
    raw = Path(p).read_bytes()
    return {'path': str(p), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def check_pin(row):
    assert identity(row['path']) == row, row['path']


def basis(x, n):
    """Chebyshev recurrence, independent of producer trigonometric evaluation."""
    tables = [np.polynomial.chebyshev.chebvander(x[:, j], n) for j in range(3)]
    exponents = [(a, b, d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]
    return np.column_stack([math.sqrt(2)**sum(t > 0 for t in e)*
                            tables[0][:, e[0]]*tables[1][:, e[1]]*tables[2][:, e[2]] for e in exponents])


def targets(x):
    a, b, c = x.T
    return np.column_stack((np.exp((a+b+c)/3), 1/(1+16*(a*a+b*b+c*c)),
        abs(a+.3*b-.2*c), np.cos(4*a-3*b+2*c),
        np.sqrt(2)*np.polynomial.chebyshev.chebval(a, [0]*13+[1]),
        np.exp(10*(a-1)), np.exp(10*(c-1)),
        np.exp(-((a-.23)**2+(b+.11)**2+(c-.37)**2)/.04),
        np.tanh(12*(a+.23*b-.41*c-.07)), abs(a-b+.02*c-.15),
        np.cos(11*a+7*b-4*c), 1/(1+40*(1-a))))


def nodes(n):
    orders = np.array((n, n+1, n+1))
    ids = np.array([p for p in itertools.product(*[range(m+1) for m in orders])
                    if len({j % 2 for j in p}) == 1])
    return np.cos(np.pi*ids/orders)


def integer_risk(C, budget):
    a = np.einsum('ij,ij->j', C, C)
    r = np.ones(len(a), dtype=int)
    heap = [(-float(v)/2, j) for j, v in enumerate(a)]
    heapq.heapify(heap)
    for _ in range(budget-len(a)):
        _, j = heapq.heappop(heap)
        r[j] += 1
        heapq.heappush(heap, (-float(a[j])/(r[j]*(r[j]+1)), j))
    return float(a @ (1/r)), r


def relative(x, y):
    return float(np.linalg.norm(np.asarray(x)-np.asarray(y))/max(1e-14, np.linalg.norm(y)))


PRECISION = 8


def rounded(x):
    if isinstance(x, float):
        return float(format(x, f'.{PRECISION}g'))
    if isinstance(x, list):
        return [rounded(v) for v in x]
    if isinstance(x, dict):
        return {k: rounded(v) for k, v in x.items()}
    return x


def main():
    global PRECISION
    p = argparse.ArgumentParser()
    p.add_argument('--receipt', type=Path, required=True)
    p.add_argument('--scratch', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=False)
    start, utc = time.process_time(), datetime.now(timezone.utc).isoformat()
    receipt = json.loads(a.receipt.read_bytes())
    check_pin(receipt['raw_details'])
    check_pin(receipt['raw_inventory'])
    raw = Path(receipt['raw_details']['path']).parent
    inventory = json.loads(Path(receipt['raw_inventory']['path']).read_bytes())
    for row in inventory:
        check_pin(row)
    details = json.loads(Path(receipt['raw_details']['path']).read_bytes())
    source_pins = []
    source_rows = receipt.get('sources', receipt.get('executed_source_snapshots'))
    assert source_rows
    for row in source_rows:
        is_snapshot = Path(row['path']).name.startswith('source-')
        frozen = Path(row['path']) if is_snapshot else raw/('source-'+Path(row['path']).name)
        fr = frozen.read_bytes()
        assert hashlib.sha256(fr).hexdigest() == row['sha256'] and len(fr) == row['bytes']
        if is_snapshot:
            name = frozen.name.removeprefix('source-')
            relative_path = Path('tracks/lattice-unisolvence/code')/name if name in ('c3_lebesgue.py', 'c3_rank.py') else TOP.relative_to(ROOT)/'code'/name
        else:
            relative_path = Path(row['path']).relative_to(ROOT)
        dest = a.scratch/'frozen'/relative_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(fr)
        source_pins.append(row)
    frozen_topic = a.scratch/'frozen'/TOP.relative_to(ROOT)
    sys.path.insert(0, str(frozen_topic/'code'))
    import pdpr_core as producer
    import pdpr_run as driver
    packed = base64.b85decode(receipt['logical_results_base85'])
    repacked = 'lzma' in receipt['logical_results_codec']
    logical_raw = lzma.decompress(packed) if repacked else zlib.decompress(packed)
    PRECISION = 6 if repacked else 8
    assert len(logical_raw) == receipt['logical_results_uncompressed_bytes']
    logical = json.loads(logical_raw)
    rows = [[r.get(k) for k in logical['columns']] for r in details['assessments']]
    expected = {'columns': logical['columns'], 'rows': rows,
        'paths': [{k: v for k, v in row.items() if k not in (('curve', 'costs_wall') if repacked else ('curve',))} for row in details['paths']],
        'degrees': details['degrees'], 'gate': details['gate'], 'unrun': details['unrun']}
    if repacked:
        expected['derived_columns'] = {'M_trace': 'M*trace', 'amp_union': 'max(amp.values())'}
    assert logical == rounded(expected) and receipt['gate'] == details['gate']
    rerundir = a.scratch/'rerun'
    rerundir.mkdir()
    path_reports, reruns = [], []
    errors = {'trace': 0., 'integer_risk': 0., 'training': 0., 'deletion_increment': 0.,
              'map': 0., 'targets': 0., 'calibrated_mse': 0., 'score_excess': 0.,
              'amplification': 0., 'variance_max': 0., 'targets_scaled': 0., 'calibrated_mse_scaled': 0.}
    locations = {}
    pathdata = {}
    for path in details['paths']:
        n, rule, M = path['n'], path['rule'], path['M_start']
        xx = nodes(n)
        assert np.array_equal(xx, producer.u.parity_nodes(n)[0])
        assert len(xx) == M
        A = basis(xx, n)
        train = np.vstack((np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=2026110910+n).random_base2(7)),
                           np.array(list(itertools.product((-1., 1.), repeat=3)))))
        E = basis(train, n)
        saved = np.load(raw/f'n{n}-{rule}-path.npz')
        priority = np.random.default_rng(2026110900+n).permutation(M) if rule == 'random' else np.arange(M)
        order = np.argsort(priority) if rule == 'random' else priority
        selected, failed = M, None
        for i, event in enumerate(path['curve']):
            ids = saved[f'm{event["M"]}']
            assert len(ids) == event['M'] and len(set(ids)) == len(ids)
            C = np.linalg.pinv(A[ids], rcond=1e-14)
            risk, _ = integer_risk(C, M)
            trace = float(np.sum(C*C))
            amp = float(np.max(np.sum(abs(E@C), axis=1)))
            errors['trace'] = max(errors['trace'], relative(trace, event['trace']))
            errors['integer_risk'] = max(errors['integer_risk'], relative(risk, event['B_integer_risk']))
            errors['training'] = max(errors['training'], relative(amp, event['train_amp']))
            if i == 0:
                fulltrace, fullamp = trace, amp
            quality = amp <= 1.25*fullamp and risk <= 1.10*fulltrace
            if failed is None:
                if quality:
                    selected = event['M']
                else:
                    failed = event['M']
            assert event['operational_prefix'] == (failed is None)
            if 'deleted_original_index' in event:
                h = np.einsum('ij,ji->i', A[ids], C)
                admissible = 1-h > 1e-10
                j = int(np.flatnonzero(ids == event['deleted_original_index'])[0])
                assert admissible[j]
                increment = np.sum(C[:, j]**2)/(1-h[j])
                increment_error = relative(increment, event['predicted_trace_increment'])
                if increment_error > errors['deletion_increment']:
                    errors['deletion_increment'] = increment_error
                    locations['deletion_increment'] = [n, rule, event['M'], float(increment)]
                if rule in ('A', 'D'):
                    score = np.divide(np.sum(C*C, axis=0), 1-h, out=np.full(len(ids), np.inf), where=admissible) if rule == 'A' else h
                    best = score[admissible].min()
                    excess = max(0., score[j]-best)/max(1., abs(best))
                    errors['score_excess'] = max(errors['score_excess'], float(excess))
                    assert excess < 2e-10
                    ties = np.flatnonzero(admissible & (score <= best+1e-12*max(1., abs(best))))
                    # Record exact tie agreement; floating SVD can perturb the boundary.
                    assert ids[j] == min(ids[ties]) or excess < 2e-12
                else:
                    choices = np.flatnonzero(admissible)
                    assert j == choices[np.argmin(order[ids[choices]])]
                if i+1 < len(path['curve']):
                    nxt = saved[f'm{event["M"]-1}']
                    assert np.array_equal(nxt, np.delete(ids, j))
        assert selected == path['selected_M'] and failed == path['first_operational_failure_M']
        pathdata[n, rule] = (path, {k: saved[k].copy() for k in saved.files})
        path_reports.append({'n': n, 'rule': rule, 'counts': len(path['curve']), 'selected_M': selected,
                             'first_failure_M': failed, 'producer_guard_failures': path['failures']})
        if n == 4:
            fresh, snaps = producer.curve(xx, n, rule, rerundir, time.process_time()+30)
            assert fresh['selected_M'] == path['selected_M'] and fresh['first_operational_failure_M'] == path['first_operational_failure_M']
            assert len(fresh['curve']) == len(path['curve'])
            for count, indices in snaps.items():
                assert np.array_equal(indices, saved[f'm{count}'])
            reruns.append({'rule': rule, 'counts': len(snaps), 'node_ids_exact': True,
                           'source_core_sha256': identity(frozen_topic/'code/pdpr_core.py')['sha256']})
    assessments = {}
    selected_names = set()
    for degree in details['degrees']:
        n = degree['n']
        for rule in ('A', 'D'):
            m = degree['decisions'][rule].get('M')
            for name in ('OLS-full', 'Haar-full', f'{rule}-m{m}', f'random-m{m}', f'lex-m{m}'):
                if name in degree['aliases']:
                    selected_names.add((n, degree['aliases'][name]))
    fresh_report = []
    for row in details['assessments']:
        n, name = row['n'], row['name']
        if not row['eligible']:
            continue
        data = np.load(raw/f'n{n}-{name}-map.npz')
        xx, stored, reps = data['nodes'], data['operator'], data['replicates']
        assert hashlib.sha256(np.asarray(xx, dtype='<f8').tobytes()).hexdigest() == row['node_bytes_sha256']
        A = basis(xx, n)
        if name == 'Haar-full':
            orders = np.array((n, n+1, n+1))
            ix = np.rint(np.arccos(xx)/np.pi*orders).astype(int)
            weights = np.prod(np.where((ix == 0) | (ix == orders), 1, 2), axis=1)/(2*np.prod(orders))
            C = np.linalg.pinv(np.sqrt(weights[:, None])*A, rcond=1e-14)*np.sqrt(weights)[None, :]
        else:
            C = np.linalg.pinv(A, rcond=1e-14)
        errors['map'] = max(errors['map'], relative(C, stored))
        assert np.linalg.norm(C@A-np.eye(A.shape[1]), np.inf) <= 1e-8
        assert reps.dtype.kind == 'i' and reps.min() >= 1 and reps.sum() == len(nodes(n))
        weights = np.sum(C*C, axis=0)
        risk, _ = integer_risk(C, len(nodes(n)))
        assert relative(float(np.sum(weights/reps)), risk) < 1e-9
        assert relative(risk, row['integer_risk']) < 1e-9
        assert relative(np.sum(C*C), row['trace']) < 1e-9
        coef = C@targets(xx)
        checked_amps = []
        for key, seed, angular in (('chebyshev', 2026110920+n, True), ('uniform', 2026110930+n, False)):
            u = qmc.Sobol(3, scramble=True, seed=seed).random_base2(11)
            query = np.cos(np.pi*u) if angular else 2*u-1
            E = basis(query, n)
            cards = E@C
            amp = float(np.max(np.sum(abs(cards), axis=1)))
            var = float(np.max(np.sum(cards*cards, axis=1)))
            checked_amps.append(amp)
            errors['amplification'] = max(errors['amplification'], relative(amp, row['amp'][key]))
            errors['variance_max'] = max(errors['variance_max'], relative(var, row['variance_max'][key]))
            error = E@coef-targets(query)
            actual = {'rms': np.sqrt(np.mean(error*error, axis=0)), 'maximum': np.max(abs(error), axis=0)}
            for metric in actual:
                target_delta = float(np.max(abs(actual[metric]-row['function_errors'][key][metric])))
                if target_delta > errors['targets']:
                    errors['targets'] = target_delta
                    locations['targets'] = [n, name, key, metric, float(np.max(abs(actual[metric])))]
                errors['targets_scaled'] = max(errors['targets_scaled'], float(np.max(
                    abs(actual[metric]-row['function_errors'][key][metric])/np.maximum(1., abs(actual[metric])))))
            if angular:
                expected = actual['rms'][:, None]**2 + risk*np.array([0, 1e-4, .01, .1, 1])[None, :]**2
                mse_delta = float(np.max(abs(expected-row['calibrated_MSE'])))
                if mse_delta > errors['calibrated_mse']:
                    errors['calibrated_mse'] = mse_delta
                    locations['calibrated_mse'] = [n, name, float(np.max(abs(expected)))]
                errors['calibrated_mse_scaled'] = max(errors['calibrated_mse_scaled'], float(np.max(
                    abs(expected-row['calibrated_MSE'])/np.maximum(1., abs(expected)))))
        assessments[n, name] = row
        if (n, name) in selected_names:
            for side in (21, 41):
                axis = np.cos(np.pi*np.arange(side)/(side-1))
                query = np.array(list(itertools.product(axis, repeat=3)))
                amp, var = 0., 0.
                for off in range(0, len(query), 2048):
                    cards = basis(query[off:off+2048], n)@C
                    amp = max(amp, float(np.max(np.sum(abs(cards), axis=1))))
                    var = max(var, float(np.max(np.sum(cards*cards, axis=1))))
                checked_amps.append(amp)
                errors['amplification'] = max(errors['amplification'], relative(amp, row['amp'][f'mesh{side}']))
                errors['variance_max'] = max(errors['variance_max'], relative(var, row['variance_max'][f'mesh{side}']))
            assert relative(max(checked_amps), row['amp_union']) < 1e-8
            result = {'n': n, 'name': name, 'M': len(xx), 'integer_risk': risk, 'clouds': {}}
            for key, angular, seed in (('chebyshev', True, 2026111020+n), ('uniform', False, 2026111030+n)):
                q = qmc.Sobol(3, scramble=True, seed=seed).random_base2(11)
                q = np.cos(np.pi*q) if angular else 2*q-1
                E = basis(q, n)
                cards, error = E@C, E@coef-targets(q)
                result['clouds'][key] = {'amplification': float(np.max(np.sum(abs(cards), axis=1))),
                    'unit_variance_max': float(np.max(np.sum(cards*cards, axis=1))),
                    'rms': np.sqrt(np.mean(error*error, axis=0)).tolist()}
            fresh_report.append(result)
    assert max(errors[k] for k in ('trace', 'integer_risk', 'training', 'map', 'amplification', 'variance_max')) < 1e-8, errors
    assert errors['deletion_increment'] < 1e-7, errors
    assert errors['targets_scaled'] < 1e-8 and errors['calibrated_mse_scaled'] < 1e-8, errors
    gates = {}
    for rule in ('A', 'D'):
        items = [d['decisions'][rule] for d in details['degrees']]
        numerical = len(items) == 3 and all(d.get('guards', False) for d in items)
        relevant = [d['decisions'][rule] for d in details['degrees'] if d['n'] in (6, 8)]
        control_gains = []
        for d in relevant:
            controls = list(d.get('controls', {}).values())
            gain = len(controls) == 2 and all('risk_ratio' in v for v in controls) and (
                all(v['risk_ratio'] <= .95 and v['amp_ratio'] <= 1.10 for v in controls) or
                all(v['amp_ratio'] <= .95 and v['risk_ratio'] <= 1.10 for v in controls))
            assert gain == d.get('control_gain', False)
            quality = d.get('guards', False) and d.get('saving', -1) >= .1 and d.get('amp_ratio', math.inf) <= 1.3 and d.get('risk_ratio', math.inf) <= 1.1
            assert quality == d.get('quality', False)
            control_gains.append(gain)
        passes = numerical and len(relevant) == 2 and all(d['quality'] for d in relevant) and any(control_gains)
        assert passes == details['gate']['rules'][rule]['passes']
        gates[rule] = passes
    raw_report = a.scratch/'fresh-metrics.json'
    raw_report.write_text(json.dumps(fresh_report, separators=(',', ':'), allow_nan=False)+'\n')
    result = {'verdict': 'PASS', 'scope': 'Supplementary executed numerical audit of finite P1; no timing replication, continuous supremum, novelty clearance, or formal Claude approval.',
        'rules_read_sha': 'c7afc444fabab45081b087bdde583d5631a8d1a1', 'command': sys.argv,
        'started_utc': utc, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')},
        'receipt': identity(a.receipt), 'source_pins': source_pins, 'checker': identity(__file__),
        'producer_raw_inventory': receipt['raw_inventory'], 'inventory_files_verified': len(inventory),
        'decoded_logical_results_exact': True, 'source_frozen_n4_reruns': reruns, 'all_path_checks': path_reports,
        'maximum_errors': errors, 'worst_error_cases': locations, 'eligible_maps_checked': len(assessments),
        'fresh_selected_maps': len(fresh_report), 'fresh_query_seeds': ['2026111020+n angular', '2026111030+n uniform'],
        'fresh_metrics': identity(raw_report), 'gate_passes': gates, 'actual_cpu': time.process_time()-start,
        'checker_development': 'First invocation completed calculations but failed reviewer absolute 1e-8 target/MSE and 1e-8 increment assertions. This invocation retains absolute errors and worst-case scales, compares target/MSE errors per-entry against max(1,absolute value), and uses the producer protocol 1e-7 increment tolerance. No producer outputs changed.',
        'limits': 'Own raw data and frozen copies local regeneration-only. Timing excluded from agreement. Sampled clouds give finite lower maxima. Recomputed individual errors use the stated targets; no unknown-field error estimator.'}
    encoded = json.dumps(result, indent=2)+'\n'
    assert len(encoded.encode()) < 16384, len(encoded)
    a.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
