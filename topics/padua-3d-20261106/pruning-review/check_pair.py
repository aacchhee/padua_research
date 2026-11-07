#!/usr/bin/env python3
"""Independent P5 exhaustive pair audit, frozen reruns and fresh quality checks."""
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
    assert receipt['seeds'] == {'training': '2026111010+n (unchanged P2)', 'random_pair': '2026112800+n', 'chebyshev': '2026112820+n', 'uniform': '2026112830+n', 'angular_search': '2026112840+n'}
    errors = dict.fromkeys(('candidate_amp', 'candidate_risk', 'block_eigenvalue', 'trace', 'integer_risk', 'map',
                           'norm', 'variance', 'targets_scaled', 'mse_scaled', 'search_values', 'fresh_gradient'), 0.)
    path_reports, expected_nodes = [], {}
    input_map = {Path(p['path']).name: p for p in details['inputs']}
    p2 = json.loads(Path(input_map['pdpr-constrained.json']['path']).read_bytes())
    check_pin(p2['raw_details'])
    previous = json.loads(Path(p2['raw_details']['path']).read_bytes())
    for path in details['paths']:
        n, M = path['n'], path['M_start']
        xx = nodes(n)
        assert len(xx) == M
        A, C = basis(xx, n), np.linalg.pinv(basis(xx, n), rcond=1e-14)
        H = A@C
        axis = np.cos(np.pi*np.linspace(0, 1, 9))
        train = np.vstack((np.array(list(itertools.product(axis, repeat=3))),
            np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=2026111010+n).random_base2(8))))
        E = basis(train, n)
        amp0, risk0 = float(np.max(np.sum(abs(E@C), axis=1))), float(np.sum(C*C))
        assert relative(amp0, path['full_train_amp']) < 1e-12
        assert relative(risk0, path['full_trace']) < 1e-12
        assert relative(1.25*amp0, path['amp_limit']) < 1e-12
        assert relative(1.10*risk0, path['risk_limit']) < 1e-12
        triplets = [t for t in itertools.product(range(n+1), range(n+2), range(n+2)) if len({v%2 for v in t}) == 1]
        index = {t: i for i, t in enumerate(triplets)}
        pairs = [(i, index[n-t[0],t[1],t[2]]) for i,t in enumerate(triplets) if i < index[n-t[0],t[1],t[2]]]
        fixed = [i for i,t in enumerate(triplets) if t[0]*2 == n]
        assert len(pairs) == path['allowed_pair_count'] and len(fixed) == path['fixed_plane_count']
        rows, noise_feasible, amp_feasible = [], 0, 0
        assert [list(p) for p in pairs] == [r['pair'] for r in path['candidate_tables']]
        for pair, reported in zip(pairs, path['candidate_tables']):
            keep = np.array([i for i in range(M) if i not in pair])
            fresh = np.linalg.pinv(A[keep], rcond=1e-14)
            assert np.linalg.norm(fresh@A[keep]-np.eye(A.shape[1]), np.inf) < 1e-8
            eig = float(np.linalg.eigvalsh(np.eye(2)-H[np.ix_(pair, pair)])[0])
            amp = float(np.max(abs(E@fresh).sum(axis=1)))
            risk = integer_risk(fresh, M)[0]
            trace = float(np.sum(fresh*fresh))
            for key, av, bv in [('candidate_amp', amp, reported['train_amp']), ('candidate_risk', risk, reported['integer_risk']),
                                ('trace', trace, reported['trace']), ('block_eigenvalue', eig, reported['block_eigen_min'])]:
                errors[key] = max(errors[key], relative(av,bv))
            noise_ok, amp_ok = risk <= 1.10*risk0, amp <= 1.25*amp0
            feasible = eig > 1e-10 and noise_ok and amp_ok
            reason = 'feasible' if feasible else 'amp_and_noise' if not noise_ok and not amp_ok else 'amp' if not amp_ok else 'noise'
            assert eig > 1e-10 and feasible == reported['feasible'] and reason == reported['reason']
            noise_feasible += int(noise_ok); amp_feasible += int(amp_ok)
            rows.append({'pair':list(pair),'amp':amp,'risk':risk,'feasible':feasible})
        feasible_rows = [r for r in rows if r['feasible']]
        pool = feasible_rows or rows
        best = min(r['amp'] for r in pool)
        chosen = min((r for r in pool if r['amp'] <= best+1e-12*max(1,abs(best))), key=lambda r:r['pair'])
        assert path['pair_feasible_count'] == len(feasible_rows)
        assert chosen['pair'] == path['selected_pair']
        assert path['operational_pair'] == bool(feasible_rows)
        assert path['operational_M'] == M-(2 if feasible_rows else 0)
        assert not path['failures'] and not path['numerically_rejected'] and path['candidate_enumeration_complete']
        keep = np.array([i for i in range(M) if i not in chosen['pair']])
        with np.load(raw/f'n{n}-pair-checkpoint.npz') as cp:
            assert np.array_equal(cp['ids'],keep) and np.array_equal(cp['nodes'],xx[keep])
        expected_nodes[n,'pair' if feasible_rows else 'pair-infeasible-diagnostic'] = xx[keep]
        prior = next(p for p in previous['paths'] if p['n']==n)
        singletons = prior['candidate_tables'][0]['candidates']
        best_singleton = min(r['train_amp'] for r in singletons if r['integer_risk'] <= prior['risk_limit'])
        assert relative(best_singleton, path['best_P2_singleton_training_amp']) < 1e-12
        assert abs((1-chosen['amp']/best_singleton)-path['gain_over_best_singleton_training_amp']) < 1e-12
        for j in chosen['pair']:
            expected_nodes[n,f'singleton-{j}'] = np.delete(xx,j,axis=0)
            c = np.linalg.pinv(np.delete(A,j,axis=0),rcond=1e-14)
            amp, risk = float(np.max(abs(E@c).sum(axis=1))), integer_risk(c,M)[0]
            old = next(r for r in singletons if r['original_index']==j)
            assert relative(amp,old['train_amp']) < 1e-12 and relative(risk,old['integer_risk']) < 1e-12
            assert not (amp<=1.25*amp0 and risk<=1.10*risk0)
        for rule in ('A','D'):
            oldpin = input_map[f'n{n}-{rule}-path.npz']
            with np.load(oldpin['path']) as old:
                expected_nodes[n,f'{rule}-two-singletons'] = xx[old[f'm{M-2}']]
        random_pair = pairs[int(np.random.default_rng(2026112800+n).integers(len(pairs)))]
        assert list(random_pair) == path['random_pair']
        expected_nodes[n,'random-reflection-pair'] = np.delete(xx,random_pair,axis=0)
        rerun_dir = a.scratch/f'n{n}-frozen-rerun'; rerun_dir.mkdir()
        rerun, selected_ids, actual_pairs = producer.screen_pair(xx,n,{'indices':triplets},rerun_dir,time.process_time()+10)
        assert rerun['selected_pair'] == path['selected_pair'] and rerun['operational_pair'] == path['operational_pair']
        assert rerun['pair_feasible_count'] == path['pair_feasible_count'] and np.array_equal(selected_ids,keep)
        assert actual_pairs == pairs
        path_reports.append({'n':n,'fresh_SVD_pairs':len(rows),'noise_feasible':noise_feasible,'amp_feasible':amp_feasible,
            'joint_feasible':len(feasible_rows),'diagnostic_pair':chosen['pair'],'minimum_train_ratio':chosen['amp']/amp0,
            'diagnostic_risk_ratio':chosen['risk']/risk0,'gain_over_best_singleton':1-chosen['amp']/best_singleton,
            'frozen_actual_rerun_same_decision_and_ids':True})
    fresh_rows, checked, search_values_count, fresh_searches_count = [], {}, 0, 0
    gradient_stencils = []
    for row in details['assessments']:
        assert time.process_time()-start < 60, 'review CPU window exhausted'
        assert row['eligible'] and not row.get('assessment_incomplete')
        n, name = row['n'], row['name']
        data = np.load(raw/f'n{n}-{name}-map.npz')
        xx, saved, reps = data['nodes'], data['operator'], data['replicates']
        if (n,name) in expected_nodes:
            assert np.array_equal(xx,expected_nodes[n,name]), name
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
        critical = name in ('OLS-full','pair','pair-infeasible-diagnostic','restrictedQR-two-rows') or name.startswith('singleton-')
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
        for key, angular, oldseed, newseed in (('chebyshev', True, 2026112820+n, 2026113020+n),
                                              ('uniform', False, 2026112830+n, 2026113030+n)):
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
        starts += (np.pi*np.random.default_rng(2026112840+n).random((16, 3))).tolist()
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
            starts += list(np.pi*np.random.default_rng(2026113040+n).random((16, 3)))
            results = []
            for theta in starts:
                assert time.process_time()-start < 60, 'review CPU window exhausted'
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
        n, decision, aliases = degree['n'], degree['decisions']['pair'], degree['aliases']
        for alias, canonical in aliases.items():
            if (n,alias) in expected_nodes:
                actual = np.load(raw/f'n{n}-{canonical}-map.npz')['nodes']
                assert np.array_equal(actual,expected_nodes[n,alias])
        fullname = aliases['OLS-full']
        pairname = aliases['pair' if decision['operational_pair'] else 'pair-infeasible-diagnostic']
        full,pair = checked[n,fullname],checked[n,pairname]
        ratio = pair['original_norm']/full['original_norm']
        fresh_ratio = pair['augmented_norm']/full['augmented_norm']
        assert relative(ratio,decision['heldout_amp_ratio']) < 1e-12
        assert relative(pair['risk']/full['risk'],decision['integer_risk_ratio']) < 1e-12
        assert decision['guards'] and decision['intermediate_barrier']
        passed = decision['operational_pair'] and ratio<=1.30
        assert bool(passed)==decision['passes']
        gates.append({'n':n,'operational_pair':decision['operational_pair'],'registered_gate_passes':bool(passed),
            'original_amp_ratio':ratio,'fresh_augmented_amp_ratio':fresh_ratio,'pair_risk':pair['risk']})
    assert not details['unrun'] and len(gates)==2
    assert max(v for k, v in errors.items() if k != 'fresh_gradient') < 1e-8, errors
    assert errors['fresh_gradient'] < 1e-5, errors
    assert all(g['registered_gate_passes'] for g in gates) == details['gate']['passes']
    raw_output = a.scratch/'fresh-metrics.json'
    raw_output.write_text(json.dumps({'metrics':fresh_rows,'gradient_stencils':gradient_stencils}, separators=(',', ':'), allow_nan=False)+'\n')
    result = {'verdict': 'PASS', 'scope': 'Independent finite P5 reflection-pair screen; no universal block/subset theorem, certified norm or formal Claude approval.',
        'rules_read_sha': 'c7afc444fabab45081b087bdde583d5631a8d1a1', 'command': sys.argv,
        'started_utc': utc, 'ended_utc': datetime.now(timezone.utc).isoformat(), 'actual_cpu': time.process_time()-start,
        'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')},
        'receipt': identity(a.receipt), 'checker': identity(__file__), 'helper': identity(helper.__file__),
        'source_pins': receipt['executed_source_snapshots'], 'raw_inventory': receipt['raw_inventory'],
        'inventory_files_checked': len(inventory), 'inputs': details['inputs'], 'decoded_logical_object_exact': True,
        'paths': path_reports, 'map_count': len(checked), 'original_search_values_checked': search_values_count,
        'fresh_searches': fresh_searches_count, 'fresh_seeds': ['2026113020+n angular', '2026113030+n uniform', '2026113040+n refinement'],
        'maximum_errors': errors, 'gradient_stencils_recorded':len(gradient_stencils),
        'gate_reconstruction': gates, 'fresh_metrics': identity(raw_output),
        'limits': 'All148 fixed initial pairs independently fresh-SVD refactored, plus frozen source screen reruns. All17 distinct maps/18 aliases checked. Original meshes independently rerun only for10 consequential maps; all recorded search values checked and280 fresh refinements added. Timings not replicated. Raw files regeneration-only; no universal impossibility or new research round.'}
    encoded = json.dumps(result, indent=2)+'\n'
    assert len(encoded.encode()) < 16384, len(encoded)
    a.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
