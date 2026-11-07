#!/usr/bin/env python3
"""P2 independent exhaustive candidate replay and terminal-map assessment."""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import itertools
import json
import lzma
import math
import os
from pathlib import Path
import platform
import sys
import time
import numpy as np
import scipy
from scipy.stats import qmc
import check_pilot as helper
from check_pilot import basis, targets, nodes, integer_risk, identity, relative, check_pin

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--receipt', type=Path, required=True)
    p.add_argument('--scratch', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=False)
    start, utc = time.process_time(), datetime.now(timezone.utc).isoformat()
    receipt = json.loads(a.receipt.read_bytes())
    for key in ('raw_details', 'raw_inventory'):
        check_pin(receipt[key])
    raw = Path(receipt['raw_details']['path']).parent
    inventory = json.loads(Path(receipt['raw_inventory']['path']).read_bytes())
    for row in inventory:
        check_pin(row)
    details = json.loads(Path(receipt['raw_details']['path']).read_bytes())
    for row in details['inputs']:
        check_pin(row)
    for row in receipt['executed_source_snapshots']:
        check_pin(row)
        source = Path(row['path'])
        name = source.name.removeprefix('source-')
        location = Path('tracks/lattice-unisolvence/code')/name if name in ('c3_lebesgue.py', 'c3_rank.py') else TOP.relative_to(ROOT)/'code'/name
        target = a.scratch/'frozen'/location
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    frozen_topic = a.scratch/'frozen'/TOP.relative_to(ROOT)
    sys.path.insert(0, str(frozen_topic/'code'))
    import pdpr_core as producer
    logical_raw = lzma.decompress(base64.b85decode(receipt['logical_results_base85']))
    assert len(logical_raw) == receipt['logical_results_uncompressed_bytes']
    logical = json.loads(logical_raw)
    expected = {'columns': logical['columns'],
        'rows': [[r.get(k) for k in logical['columns']] for r in details['assessments']],
        'derived_columns': {'M_trace': 'M*trace', 'amp_union': 'max(amp.values())'},
        'paths': [{k: v for k, v in r.items() if k not in ('curve', 'costs_wall', 'candidate_tables', 'numerically_rejected')} for r in details['paths']],
        'degrees': details['degrees'], 'gate': details['gate'], 'unrun': details['unrun']}
    helper.PRECISION = 6
    assert logical == helper.rounded(expected)
    assert receipt['seeds']['chebyshev'] == '2026111520+n' and receipt['seeds']['uniform'] == '2026111530+n'
    assert receipt['producer_utc']['started_utc'] < receipt['producer_utc']['ended_utc']
    errors = dict.fromkeys(('candidate_amp', 'candidate_risk', 'candidate_trace', 'fresh_terminal_amp',
                           'fresh_terminal_risk', 'map', 'assessed_amp', 'assessed_variance', 'target_scaled', 'mse_scaled'), 0.)
    summaries, fresh_checks, reruns = [], [], []
    rerundir = a.scratch/'rerun'
    rerundir.mkdir()
    for path in details['paths']:
        n, M = path['n'], path['M_start']
        xx, A = nodes(n), basis(nodes(n), n)
        axis = np.cos(np.pi*np.arange(9)/8)
        tx = np.vstack((np.array(list(itertools.product(axis, repeat=3))),
            np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=2026111010+n).random_base2(8))))
        E = basis(tx, n)
        saved = np.load(raw/f'n{n}-L-path.npz')
        full = np.linalg.pinv(A, rcond=1e-14)
        amp_limit = 1.25*float(np.max(np.sum(abs(E@full), axis=1)))
        risk_limit = 1.10*float(np.sum(full*full))
        candidate_count = 0
        feasibility_margins = []
        for state in path['candidate_tables']:
            ids = saved[f'm{state["M"]}']
            current = A[ids]
            C = np.linalg.pinv(current, rcond=1e-14)
            H, L = current@C, E@C
            records = state['candidates']
            assert state['complete'] and len(records) == len(ids)
            accepted = []
            for record in records:
                i = record['local_index']
                assert record['original_index'] == ids[i]
                den = 1-H[i, i]
                if den <= 1e-10:
                    assert not record['feasible'] and record['reason'] == 'rank_denominator'
                    continue
                keep = np.arange(len(ids)) != i
                cp = C[:, keep] + C[:, i, None]*(H[i, keep]/den)[None, :]
                lp = L[:, keep] + L[:, i, None]*(H[i, keep]/den)[None, :]
                amp = float(np.max(np.sum(abs(lp), axis=1)))
                risk, _ = integer_risk(cp, M)
                trace = float(np.sum(cp*cp))
                for key, value, recorded in (('candidate_amp', amp, record['train_amp']),
                                             ('candidate_risk', risk, record['integer_risk']),
                                             ('candidate_trace', trace, record['trace'])):
                    errors[key] = max(errors[key], relative(value, recorded))
                feasible = amp <= amp_limit and risk <= risk_limit
                assert feasible == record['feasible'], (n, len(ids), i)
                reason = 'feasible' if feasible else ('amp_and_noise' if amp > amp_limit and risk > risk_limit else 'amp' if amp > amp_limit else 'noise')
                assert reason == record['reason']
                feasibility_margins.extend((abs(amp-amp_limit)/amp_limit, abs(risk-risk_limit)/risk_limit))
                candidate_count += 1
                if feasible:
                    accepted.append((amp, int(ids[i])))
                if state['M'] == path['selected_M']:
                    # Full fresh SVD for every terminal deletion, independent of
                    # either producer's or reviewer's cardinal update shortcut.
                    fresh = np.linalg.pinv(current[keep], rcond=1e-14)
                    freshamp = float(np.max(np.sum(abs(E@fresh), axis=1)))
                    freshrisk, _ = integer_risk(fresh, M)
                    errors['fresh_terminal_amp'] = max(errors['fresh_terminal_amp'], relative(freshamp, amp))
                    errors['fresh_terminal_risk'] = max(errors['fresh_terminal_risk'], relative(freshrisk, risk))
                    assert (freshamp <= amp_limit and freshrisk <= risk_limit) == feasible
                    fresh_checks.append([n, int(ids[i]), feasible])
            assert len(accepted) == state['feasible_count']
            if 'selected_original_index' in state:
                excluded = {r['original_index'] for r in path['numerically_rejected'] if r['M_after'] == state['M']-1}
                candidates = [(v, i) for v, i in accepted if i not in excluded]
                best = min(v for v, i in candidates)
                chosen = min(i for v, i in candidates if v <= best+1e-12*max(1., abs(best)))
                assert chosen == state['selected_original_index']
                assert np.array_equal(saved[f'm{state["M"]-1}'], ids[ids != chosen])
            elif path['stop'] == 'no_predicted_feasible_deletion':
                assert not accepted
        fresh, snapshots = producer.constrained_curve(xx, n, rerundir, time.process_time()+180)
        assert fresh['selected_M'] == path['selected_M'] and fresh['stop'] == path['stop']
        for count, indices in snapshots.items():
            assert np.array_equal(indices, saved[f'm{count}'])
        reruns.append({'n': n, 'count_states': len(snapshots), 'exact_node_ids': True, 'stop': fresh['stop']})
        summaries.append({'n': n, 'terminal_M': path['selected_M'], 'states': len(path['curve']),
            'candidate_rows_checked': candidate_count, 'stop': path['stop'],
            'numerical_rejections': len(path['numerically_rejected']), 'failures': path['failures'],
            'minimum_relative_constraint_margin': min(feasibility_margins)})
    fresh_rows, checked = [], {}
    for row in details['assessments']:
        if not row['eligible']:
            continue
        n, name = row['n'], row['name']
        data = np.load(raw/f'n{n}-{name}-map.npz')
        xx, stored, reps = data['nodes'], data['operator'], data['replicates']
        assert hashlib.sha256(np.asarray(xx, dtype='<f8').tobytes()).hexdigest() == row['node_bytes_sha256']
        A = basis(xx, n)
        if name == 'Haar-full':
            order = np.array((n, n+1, n+1))
            ix = np.rint(np.arccos(xx)/np.pi*order).astype(int)
            w = np.prod(np.where((ix == 0) | (ix == order), 1, 2), axis=1)/(2*np.prod(order))
            C = np.linalg.pinv(np.sqrt(w[:, None])*A, rcond=1e-14)*np.sqrt(w)[None, :]
        else:
            C = np.linalg.pinv(A, rcond=1e-14)
        errors['map'] = max(errors['map'], relative(C, stored))
        assert np.linalg.norm(C@A-np.eye(A.shape[1]), np.inf) < 1e-8
        risk, _ = integer_risk(C, len(nodes(n)))
        assert reps.min() >= 1 and reps.sum() == len(nodes(n)) and reps.dtype.kind == 'i'
        assert relative(np.sum(np.sum(C*C, axis=0)/reps), risk) < 1e-8
        assert relative(risk, row['integer_risk']) < 1e-8
        coef = C@targets(xx)
        measured_amp, measured_var = {}, {}
        for side in (21, 41):
            axis = np.cos(np.pi*np.arange(side)/(side-1))
            query = np.array(list(itertools.product(axis, repeat=3)))
            amp, var = 0., 0.
            for off in range(0, len(query), 2048):
                card = basis(query[off:off+2048], n)@C
                amp = max(amp, float(np.max(np.sum(abs(card), axis=1))))
                var = max(var, float(np.max(np.sum(card*card, axis=1))))
            measured_amp[f'mesh{side}'], measured_var[f'mesh{side}'] = amp, var
        fresh = {'n': n, 'name': name, 'M': len(xx), 'integer_risk': risk, 'clouds': {}}
        for key, angular, originalseed, newseed in (('chebyshev', True, 2026111520+n, 2026111720+n),
                                                   ('uniform', False, 2026111530+n, 2026111730+n)):
            for is_fresh, seed in ((False, originalseed), (True, newseed)):
                q = qmc.Sobol(3, scramble=True, seed=seed).random_base2(11)
                q = np.cos(np.pi*q) if angular else 2*q-1
                E = basis(q, n)
                card, error = E@C, E@coef-targets(q)
                amp = float(np.max(np.sum(abs(card), axis=1)))
                var = float(np.max(np.sum(card*card, axis=1)))
                rms, maximum = np.sqrt(np.mean(error*error, axis=0)), np.max(abs(error), axis=0)
                if is_fresh:
                    fresh['clouds'][key] = {'amp': amp, 'variance': var, 'rms': rms.tolist()}
                else:
                    measured_amp[key], measured_var[key] = amp, var
                    for metric, value in (('rms', rms), ('maximum', maximum)):
                        delta = abs(value-row['function_errors'][key][metric])/np.maximum(1., abs(value))
                        errors['target_scaled'] = max(errors['target_scaled'], float(delta.max()))
                    if angular:
                        mse = rms[:, None]**2 + risk*np.array([0, 1e-4, .01, .1, 1])[None, :]**2
                        errors['mse_scaled'] = max(errors['mse_scaled'], float(np.max(abs(mse-row['calibrated_MSE'])/np.maximum(1., abs(mse)))))
        for key in measured_amp:
            errors['assessed_amp'] = max(errors['assessed_amp'], relative(measured_amp[key], row['amp'][key]))
            errors['assessed_variance'] = max(errors['assessed_variance'], relative(measured_var[key], row['variance_max'][key]))
        assert relative(max(measured_amp.values()), row['amp_union']) < 1e-8
        checked[n, name] = {'amp': max(measured_amp.values()), 'risk': risk, 'M': len(xx)}
        fresh_rows.append(fresh)
    decisions = []
    for degree in details['degrees']:
        n, d = degree['n'], degree['decisions']['L']
        def lookup(name):
            return checked[n, degree['aliases'][name]]
        full, terminal = lookup('OLS-full'), lookup(f'L-m{d["M"]}')
        risk_ratio, amp_ratio = terminal['risk']/full['risk'], terminal['amp']/full['amp']
        saving = 1-terminal['M']/degree['M_start']
        controls = [lookup(f'{rule}-m{d["M"]}') for rule in ('random', 'lex')]
        control_gain = (all(terminal['risk']/r['risk'] <= .95 and terminal['amp']/r['amp'] <= 1.10 for r in controls)
                        or all(terminal['amp']/r['amp'] <= .95 and terminal['risk']/r['risk'] <= 1.10 for r in controls))
        quality = d['guards'] and saving >= .1 and amp_ratio <= 1.3 and risk_ratio <= 1.1
        assert quality == d['quality'] and control_gain == d['control_gain']
        decisions.append({'n': n, 'M': terminal['M'], 'saving': saving, 'amp_ratio': amp_ratio,
                          'risk_ratio': risk_ratio, 'quality': quality, 'control_gain': control_gain})
    passes = len(decisions) == 2 and all(d['quality'] for d in decisions) and any(d['control_gain'] for d in decisions) and not details['unrun'] and details['timing']['actual_cpu'] <= 600
    assert passes == details['gate']['passes']
    assert max(errors.values()) < 1e-8, errors
    metrics = a.scratch/'fresh-metrics.json'
    metrics.write_text(json.dumps(fresh_rows, separators=(',', ':'), allow_nan=False)+'\n')
    result = {'verdict': 'PASS', 'scope': 'Independent finite P2 numerical audit, zero research rounds; no continuous theorem, novelty clearance or formal Claude approval.',
        'rules_read_sha': 'c7afc444fabab45081b087bdde583d5631a8d1a1', 'command': sys.argv,
        'started_utc': utc, 'ended_utc': datetime.now(timezone.utc).isoformat(), 'actual_cpu': time.process_time()-start,
        'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')},
        'receipt': identity(a.receipt), 'checker': identity(__file__), 'helper': identity(helper.__file__),
        'producer_source_pins': receipt['executed_source_snapshots'], 'raw_inventory': receipt['raw_inventory'],
        'raw_inventory_files_checked': len(inventory), 'decoded_logical_object_exact': True,
        'path_summaries': summaries, 'actual_frozen_reruns': reruns,
        'terminal_all_candidate_fresh_SVD_count': len(fresh_checks), 'maximum_errors': errors,
        'assessed_maps': len(checked), 'fresh_query_count_per_measure': 2048,
        'fresh_seeds': ['2026111720+n angular', '2026111730+n uniform'],
        'fresh_metrics': identity(metrics), 'decisions': decisions, 'gate_passes': bool(passes),
        'limits': 'All candidate feasibility claims refer to this finite floating path and frozen thresholds. Actual producer timings not independently replicated. Own raw output/source snapshots local regeneration-only.'}
    encoded = json.dumps(result, indent=2)+'\n'
    assert len(encoded.encode()) < 16384
    a.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
