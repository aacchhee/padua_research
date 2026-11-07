#!/usr/bin/env python3
"""Independent P4 checkpoints, selected scores, modern controls and fresh searches."""
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
from scipy.optimize import minimize
from scipy.stats import qmc
import check_pilot as helper
from check_pilot import basis, targets, nodes, integer_risk, identity, relative, check_pin

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def angular_objective(C, n):
    exponents = np.array([(a, b, d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)])
    scale = 2.**(np.sum(exponents > 0, axis=1)/2)
    def value(theta):
        cs = np.cos(exponents*theta)
        phi = scale*cs.prod(axis=1)
        derivative = np.array([-scale*exponents[:, j]*np.sin(exponents[:, j]*theta[j])*
            cs[:, (j+1)%3]*cs[:, (j+2)%3] for j in range(3)])
        card = phi@C
        return -float(abs(card).sum()), -(derivative@C)@np.sign(card)
    return value


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
        rel = Path('tracks/lattice-unisolvence/code')/name if name in ('c3_lebesgue.py', 'c3_rank.py') else TOP.relative_to(ROOT)/'code'/name
        dest = a.scratch/'frozen'/rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(source.read_bytes())
    frozen_topic = a.scratch/'frozen'/TOP.relative_to(ROOT)
    sys.path.insert(0, str(frozen_topic/'code'))
    import pdpr_core as producer
    packed = lzma.decompress(base64.b85decode(receipt['logical_results_base85']))
    assert len(packed) == receipt['logical_results_uncompressed_bytes']
    logical = json.loads(packed)
    expected = {'columns': logical['columns'],
        'rows': [[r.get(k) for k in logical['columns']] for r in details['assessments']],
        'derived_columns': {'M_trace': 'M*trace', 'amp_union': 'max(amp.values())'},
        'paths': [{k: v for k, v in row.items() if k not in ('curve', 'costs_wall', 'candidate_tables', 'numerically_rejected')} for row in details['paths']],
        'degrees': details['degrees'], 'gate': details['gate'], 'unrun': details['unrun']}
    helper.PRECISION = 6
    assert logical == helper.rounded(expected)
    assert receipt['seeds'] == {'chebyshev': '2026112420+n', 'uniform': '2026112430+n', 'refinement_angular_starts': '2026112440+n'}
    errors = dict.fromkeys(('checkpoint_map', 'score_excess', 'trace', 'integer_risk', 'map',
                           'norm', 'variance', 'targets_scaled', 'mse_scaled', 'search_values', 'fresh_gradient'), 0.)
    path_reports = []
    rerun = a.scratch/'n8-rerun'
    rerun.mkdir()
    for path in details['paths']:
        n, M, primary = path['n'], path['M_start'], path['primary_M']
        xx, A = nodes(n), basis(nodes(n), n)
        snapshots = np.load(raw/f'n{n}-A-path.npz')
        last_cpu, checked_cp, score_counts = -1., [], []
        for step, event in enumerate(path['curve']):
            m = event['M']
            ids = snapshots[f'm{m}']
            assert len(set(ids)) == len(ids) == m and np.all(np.diff(ids) > 0)
            if 'deleted_original_index' in event:
                assert np.array_equal(snapshots[f'm{m-1}'], ids[ids != event['deleted_original_index']])
            if 'prefix_checkpoint' in event:
                cp = np.load(event['prefix_checkpoint'])
                assert np.array_equal(cp['ids'], ids) and np.array_equal(cp['nodes'], xx[ids])
                C = np.linalg.pinv(A[ids], rcond=1e-14)
                errors['checkpoint_map'] = max(errors['checkpoint_map'], relative(C, cp['operator']))
                assert event['prefix_complete_cpu'] >= event['cpu'] and event['prefix_complete_cpu'] >= last_cpu
                last_cpu = event['prefix_complete_cpu']
                assert last_cpu <= path['costs_cpu']['complete_construction']
                checked_cp.append(m)
            inspect = n == 8 or step in (0, 1, 15, 16, 31, 32, 127, 128, 213, 214, 215, 310, 311, 312, 407, 408)
            if inspect:
                C = np.linalg.pinv(A[ids], rcond=1e-14)
                trace, risk = float(np.sum(C*C)), integer_risk(C, M)[0]
                errors['trace'] = max(errors['trace'], relative(trace, event['trace']))
                errors['integer_risk'] = max(errors['integer_risk'], relative(risk, event['B_integer_risk']))
                if 'deleted_original_index' in event:
                    h = np.einsum('ij,ji->i', A[ids], C)
                    allowed = 1-h > 1e-10
                    score = np.divide(np.sum(C*C, axis=0), 1-h, out=np.full(m, np.inf), where=allowed)
                    j = int(np.flatnonzero(ids == event['deleted_original_index'])[0])
                    assert allowed[j]
                    excess = max(0., score[j]-score[allowed].min())/max(1., abs(score[allowed].min()))
                    errors['score_excess'] = max(errors['score_excess'], float(excess))
                score_counts.append(m)
        event = next(e for e in path['curve'] if e['M'] == primary)
        check_pin(path['primary_prefix']['checkpoint'])
        assert path['primary_prefix']['cpu'] == event['prefix_complete_cpu']+path['costs_cpu']['node_generation']
        assert path['primary_prefix']['wall'] == event['prefix_complete_wall']+path['costs_wall']['node_generation']
        report = {'n': n, 'primary_M': primary, 'checkpoint_counts_checked': checked_cp,
                  'score_counts_checked': score_counts, 'prefix_cpu_recorded': path['primary_prefix']['cpu'],
                  'whole_path_support_transitions': len(path['curve'])-1}
        if n == 8:
            fresh, states = producer.curve(xx, n, 'A', rerun, time.process_time()+30, checkpoint_maps=True)
            assert len(states) == len(snapshots.files) == 61
            for count, ids in states.items():
                assert np.array_equal(ids, snapshots[f'm{count}'])
            oldpin = next(r for r in details['inputs'] if r['path'].endswith('n8-A-path.npz'))
            original = np.load(oldpin['path'])
            assert set(original.files) == set(snapshots.files)
            assert all(np.array_equal(original[k], snapshots[k]) for k in snapshots.files)
            report['actual_frozen_rerun_and_original_P1_all_ids_equal'] = True
        path_reports.append(report)
    stored_path = TOP/'evidence/u2-degree12-nodes.json'
    assert identity(stored_path)['sha256'] == 'ade51c2e459b2d3161eddab564e1ada2233d2f841b5dd64bf808b2e607f7140f'
    stored = json.loads(stored_path.read_bytes())
    stored_bytes = base64.b85decode(stored['coordinates_base85'])
    assert hashlib.sha256(stored_bytes).hexdigest() == stored['coordinates_sha256']
    stored_nodes = np.frombuffer(stored_bytes, dtype='<f8').reshape(455, 3)
    # Independently follow both historical receipt chains to exact input arrays.
    input_map = {Path(r['path']).name: r for r in details['inputs']}
    c3 = json.loads(Path(input_map['u2c-heldout16.json']['path']).read_bytes())
    c4 = json.loads(Path(input_map['u2c-prefix-control.json']['path']).read_bytes())
    for old in (c3, c4):
        for pin in old['sources']:
            check_pin(pin)
        check_pin(old['raw_inventory'])
    records = json.loads(Path(c3['raw_inventory']['path']).read_bytes())
    direct = next(r for r in records if Path(r['path']).name == 'joint_norm.npy')
    assert direct in c4['inputs']
    assert direct['sha256'] == '8fd4a96a610d73ca104517a2b960b278fe91f40fe6017053bfe3b09c0b3f2428'
    fine = c4['construction']['selected_node_checkpoint']
    assert fine in json.loads(Path(c4['raw_inventory']['path']).read_bytes())
    modern = {}
    for name, pin in (('modernU2', direct), ('fineDetC4', fine)):
        check_pin(pin)
        modern[name] = np.load(pin['path'], allow_pickle=False)
        assert modern[name].shape == (969, 3)
    fresh_rows, checked, search_values_count, fresh_searches_count = [], {}, 0, 0
    gradient_stencils = []
    for row in details['assessments']:
        assert time.process_time()-start < 90, 'review CPU window exhausted'
        assert row['eligible'] and not row.get('assessment_incomplete')
        n, name = row['n'], row['name']
        data = np.load(raw/f'n{n}-{name}-map.npz')
        xx, saved, reps = data['nodes'], data['operator'], data['replicates']
        if name == 'storedU2':
            assert np.array_equal(xx, stored_nodes)
        if name in modern:
            assert np.array_equal(xx, modern[name]), name
        A = basis(xx, n)
        if name == 'Haar-full':
            order = np.array((n, n+1, n+1))
            ix = np.rint(np.arccos(xx)/np.pi*order).astype(int)
            w = np.prod(np.where((ix == 0) | (ix == order), 1, 2), axis=1)/(2*np.prod(order))
            C = np.linalg.pinv(np.sqrt(w[:, None])*A, rcond=1e-14)*np.sqrt(w)[None, :]
        else:
            C = np.linalg.pinv(A, rcond=1e-14)
        errors['map'] = max(errors['map'], relative(C, saved))
        assert np.linalg.norm(C@A-np.eye(A.shape[1]), np.inf) < 1e-8
        risk, _ = integer_risk(C, len(nodes(n)))
        assert reps.dtype.kind == 'i' and reps.min() >= 1 and reps.sum() == len(nodes(n))
        assert relative(np.sum(np.sum(C*C, axis=0)/reps), risk) < 1e-8
        assert relative(risk, row['integer_risk']) < 1e-8
        assert relative(np.sum(C*C), row['trace']) < 1e-8
        coef = C@targets(xx)
        original_amp, original_variance = {}, {}
        primary = math.ceil(1.20*math.comb(n+3, 3))
        critical = name in (f'A-m{primary}', f'restrictedQR-m{primary}', 'globalQR', 'localdet', 'modernU2', 'fineDetC4')
        if critical:
            for side in (21, 41):
                axis = np.cos(np.pi*np.arange(side)/(side-1))
                query = np.array(list(itertools.product(axis, repeat=3)))
                amp, var = 0., 0.
                for off in range(0, len(query), 2048):
                    cards = basis(query[off:off+2048], n)@C
                    amp = max(amp, float(np.max(np.sum(abs(cards), axis=1))))
                    var = max(var, float(np.max(np.sum(cards*cards, axis=1))))
                original_amp[f'mesh{side}'], original_variance[f'mesh{side}'] = amp, var
        fresh = {'n': n, 'name': name, 'M': len(xx), 'integer_risk': risk, 'clouds': {}}
        fresh_top = None
        for key, angular, oldseed, newseed in (('chebyshev', True, 2026112420+n, 2026112620+n),
                                              ('uniform', False, 2026112430+n, 2026112630+n)):
            for is_fresh, seed in ((False, oldseed), (True, newseed)):
                q = qmc.Sobol(3, scramble=True, seed=seed).random_base2(11)
                q = np.cos(np.pi*q) if angular else 2*q-1
                E = basis(q, n)
                cards, error = E@C, E@coef-targets(q)
                values = np.sum(abs(cards), axis=1)
                amp, var = float(values.max()), float(np.max(np.sum(cards*cards, axis=1)))
                rms, maximum = np.sqrt(np.mean(error*error, axis=0)), np.max(abs(error), axis=0)
                if is_fresh:
                    fresh['clouds'][key] = {'amp': amp, 'variance': var, 'rms': rms.tolist()}
                    if angular:
                        fresh_top = np.arccos(q[np.argsort(values)[-4:]])
                else:
                    original_amp[key], original_variance[key] = amp, var
                    for metric, value in (('rms', rms), ('maximum', maximum)):
                        errors['targets_scaled'] = max(errors['targets_scaled'], float(np.max(abs(value-row['function_errors'][key][metric])/np.maximum(1., abs(value)))))
                    if angular:
                        mse = rms[:, None]**2 + risk*np.array([0, 1e-4, .01, .1, 1])[None, :]**2
                        errors['mse_scaled'] = max(errors['mse_scaled'], float(np.max(abs(mse-row['calibrated_MSE'])/np.maximum(1., abs(mse)))))
        for key in original_amp:
            errors['norm'] = max(errors['norm'], relative(original_amp[key], row['amp'][key]))
            errors['variance'] = max(errors['variance'], relative(original_variance[key], row['variance_max'][key]))
        searches = json.loads((raw/f'n{n}-{name}-searches.json').read_bytes())
        assert len(searches) == 28 == row['refinement']['starts']
        starts = [np.arccos(np.clip(x, -1, 1)).tolist() for x in row['mesh41_largest_points']]
        starts += [list(t) for t in itertools.product((0., np.pi), repeat=3)]
        starts += (np.pi*np.random.default_rng(2026112440+n).random((16, 3))).tolist()
        assert [s['initial_arg'] for s in searches] == starts
        for search in searches:
            for pointkey, valuekey in (('initial_arg', 'initial'), ('arg', 'final')):
                actual = float(np.sum(abs(basis(np.cos(np.array(search[pointkey]))[None, :], n)@C)))
                errors['search_values'] = max(errors['search_values'], relative(actual, search[valuekey]))
                search_values_count += 1
        assert row['amp']['local_search'] == max(s[k] for s in searches for k in ('initial', 'final'))
        assert row['amp_union'] == max(row['amp'].values())
        enhanced_norm = max(row['amp_union'], *(x['amp'] for x in fresh['clouds'].values()))
        if critical:
            objective = angular_objective(C, n)
            theta = np.array((.71, 1.13, 2.21))
            _, gradient = objective(theta)
            # The l1 objective is smooth only while every cardinal sign is fixed.
            # An earlier h=1e-6 oracle crossed a modernU2 cardinal zero.
            middle_sign = np.sign(basis(np.cos(theta)[None, :], n)@C)
            for j in range(3):
                for h in (1e-6, 1e-7, 1e-8, 1e-9):
                    plus, minus = theta.copy(), theta.copy()
                    plus[j] += h
                    minus[j] -= h
                    plus_sign = np.sign(basis(np.cos(plus)[None, :], n)@C)
                    minus_sign = np.sign(basis(np.cos(minus)[None, :], n)@C)
                    crossings = int(np.count_nonzero(plus_sign != middle_sign)+np.count_nonzero(minus_sign != middle_sign))
                    numerical = (objective(plus)[0]-objective(minus)[0])/(2*h)
                    error = abs(numerical-gradient[j])/max(1., abs(numerical))
                    gradient_stencils.append({'map': name, 'coordinate': j, 'h': h, 'sign_changes': crossings, 'relative_error': float(error)})
                    if crossings == 0:
                        errors['fresh_gradient'] = max(errors['fresh_gradient'], float(error))
                        break
                else:
                    raise AssertionError(('no sign-stable derivative stencil', name, j))
            starts = list(fresh_top)+list(itertools.product((0., np.pi), repeat=3))
            starts += list(np.pi*np.random.default_rng(2026112640+n).random((16, 3)))
            results = []
            for theta in starts:
                assert time.process_time()-start < 90, 'review CPU window exhausted'
                initial = -objective(theta)[0]
                fit = minimize(objective, theta, jac=True, bounds=[(0, np.pi)]*3, method='L-BFGS-B',
                    options={'maxiter': 200, 'maxfun': 5000, 'ftol': 1e-12, 'gtol': 1e-8})
                final = -objective(fit.x)[0]
                enhanced_norm = max(enhanced_norm, initial, final)
                results.append({'initial': initial, 'final': final, 'success': bool(fit.success), 'arg': fit.x.tolist()})
            fresh['searches'] = results
            fresh_searches_count += len(results)
        fresh['augmented_norm'] = enhanced_norm
        checked[n, name] = {'risk': risk, 'original_norm': row['amp_union'], 'augmented_norm': enhanced_norm}
        fresh_rows.append(fresh)
    gates = []
    for degree in details['degrees']:
        n, d = degree['n'], degree['decisions']['A']
        primary = checked[n, f'A-m{d["M"]}']
        restricted = checked[n, f'restrictedQR-m{d["M"]}']
        controls = {name: checked[n, name] for name in ('globalQR', 'localdet', 'modernU2', 'fineDetC4')}
        result = {'n': n, 'M': d['M'], 'risk_ratio': primary['risk']/restricted['risk'],
                  'original_norm_ratio': primary['original_norm']/restricted['original_norm'],
                  'fresh_augmented_norm_ratio': primary['augmented_norm']/restricted['augmented_norm'],
                  'candidate': primary, 'minimum_controls': controls}
        dominates = {name: control['risk'] <= primary['risk']*(1+1e-10) and control['original_norm'] <= primary['original_norm']*(1+1e-10) for name, control in controls.items()}
        assert dominates == d['minimum_count_dominates']
        result['augmented_minimum_dominance'] = {name: control['risk'] <= primary['risk']*(1+1e-10) and control['augmented_norm'] <= primary['augmented_norm']*(1+1e-10) for name, control in controls.items()}
        passes = d['guards'] and d['reproduction'] and d['site_saving'] >= .1 and d['prefix_cpu'] <= 120 and result['risk_ratio'] <= .95 and result['original_norm_ratio'] <= .95 and not any(dominates.values())
        assert passes == d['passes']
        result['registered_gate_passes'] = bool(passes)
        gates.append(result)
    assert max(v for k, v in errors.items() if k != 'fresh_gradient') < 1e-8, errors
    assert errors['fresh_gradient'] < 1e-5, errors
    assert all(g['registered_gate_passes'] for g in gates) == details['gate']['passes']
    raw_output = a.scratch/'fresh-metrics.json'
    raw_output.write_text(json.dumps(fresh_rows, separators=(',', ':'), allow_nan=False)+'\n')
    result = {'verdict': 'PASS', 'scope': 'Independent finite P4 audit; no timing replication, universal Pareto statement, certified norm or formal Claude approval.',
        'rules_read_sha': 'c7afc444fabab45081b087bdde583d5631a8d1a1', 'command': sys.argv,
        'started_utc': utc, 'ended_utc': datetime.now(timezone.utc).isoformat(), 'actual_cpu': time.process_time()-start,
        'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')},
        'receipt': identity(a.receipt), 'checker': identity(__file__), 'helper': identity(helper.__file__),
        'source_pins': receipt['executed_source_snapshots'], 'raw_inventory': receipt['raw_inventory'],
        'inventory_files_checked': len(inventory), 'inputs': details['inputs'], 'decoded_logical_object_exact': True,
        'paths': path_reports, 'map_count': len(checked), 'original_search_values_checked': search_values_count,
        'fresh_searches': fresh_searches_count, 'fresh_seeds': ['2026112620+n angular', '2026112630+n uniform', '2026112640+n refinement'],
        'maximum_errors': errors, 'gradient_stencils': gradient_stencils, 'prior_checker_failure': {'source_sha256': 'a466a46a58d1e6cc06fcc795b9efc25064c795c49fb90a146221cca4fd3cffd8', 'fixed_h': 1e-6, 'maximum_gradient_error': 0.006151109066968322, 'reason': 'ModernU2 cardinal sign crossing inside central-difference stencil; smaller sign-stable stencil agrees. Other reported-value comparisons passed below3.44e-13; failed run emitted no success receipt.', 'captured_log': identity('/tmp/padua-pruning-review-p4b.log'), 'earlier_session': 'Pre-compaction terminal outcome unavailable; unclaimed. Retry in existing scratch stopped at mkdir before numerical work.'}, 'gate_reconstruction': gates, 'fresh_metrics': identity(raw_output),
        'limits': 'Source/clock-placement and durable prefix contents checked; hardware timings not independently replicated. n16 score stages sampled as listed; no claim of all408 n16 deletions independently rerun. Full original search values are checked, with additional independently implemented searches on consequential maps. Own raw artifacts regeneration-only.'}
    encoded = json.dumps(result, indent=2)+'\n'
    assert len(encoded.encode()) < 16384, len(encoded)
    a.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
