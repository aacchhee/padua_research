#!/usr/bin/env python3
"""Stable physical-value OLS backward design; finite measurements only."""
from __future__ import annotations
import hashlib
import itertools
import math
import os
import time
from pathlib import Path
import numpy as np
from scipy import linalg as la
from scipy.stats import qmc
import u1_usable as u
import u1c_budget as old_budget

RULES = ('A', 'D', 'random', 'lex')


def identity(path):
    p = Path(path).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def array_sha(x):
    return hashlib.sha256(np.asarray(x, dtype='<f8').tobytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def qr_map(A):
    Q, R = la.qr(A, mode='economic', check_finite=False)
    return Q, R, la.solve_triangular(R, Q.T, check_finite=False)


def validate(A, Q, R, C):
    s = la.svdvals(A, check_finite=False)
    cond = float(s[0]/s[-1]) if s[-1] > 0 else math.inf
    repro = float(la.norm(C@A-np.eye(A.shape[1]), np.inf))
    reconstruction = float(la.norm(Q@R-A, np.inf)/max(1., la.norm(A, np.inf)))
    orth = float(la.norm(Q.T@Q-np.eye(A.shape[1]), np.inf))
    eligible = (np.isfinite(C).all() and s[-1] > 0 and cond < 1e10
                and repro <= 1e-8 and reconstruction <= 1e-10 and orth <= 1e-9)
    return {'eligible': bool(eligible), 'condition2': cond,
            'reproduction_inf': repro, 'qr_relative_inf': reconstruction,
            'orthogonality_inf': orth, 'sigma_min': float(s[-1])}


def integer_risk(C, budget):
    a = np.sum(C*C, axis=0)
    r = np.ones(C.shape[1], dtype=np.int64)
    require(budget >= len(r), 'infeasible integer budget')
    for _ in range(budget-len(r)):
        j = int(np.argmax(a/(r*(r+1))))
        r[j] += 1
    return float(np.sum(a/r)), r


def training(n):
    x = np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=2026110910+n).random_base2(7))
    return np.vstack((x, np.array(list(itertools.product((-1., 1.), repeat=3)))))


def checkpoints(n, M):
    N = math.comb(n+3, 3)
    return sorted({M, N, *(math.ceil(t*N) for t in (1.05, 1.10, 1.20, 1.30)
                           if math.ceil(t*N) <= M)}, reverse=True)


def curve(nodes, n, rule, raw, cap, checkpoint_maps=False):
    """No Gram inverse: stable QR maps supply scores and actual risks each step."""
    started = time.process_time()
    wall_started = time.perf_counter()
    require(len(np.unique(nodes, axis=0)) == len(nodes) and np.isfinite(nodes).all()
            and np.max(abs(nodes)) <= 1., 'invalid starting physical nodes')
    costs = dict.fromkeys(('basis', 'initial_qr', 'score', 'downdate', 'map',
                           'refactor', 'training', 'checkpoint_io'), 0.)
    wall_costs = dict.fromkeys(costs, 0.)
    def timed(name, function):
        t, w = time.process_time(), time.perf_counter()
        value = function()
        costs[name] += time.process_time()-t
        wall_costs[name] += time.perf_counter()-w
        return value
    A0 = timed('basis', lambda: u.basis(nodes, n))
    M, N = A0.shape
    E = timed('training', lambda: u.basis(training(n), n))
    ids = np.arange(M)
    Q, R, C = timed('initial_qr', lambda: qr_map(A0))
    priority = (np.random.default_rng(2026110900+n).permutation(M)
                if rule == 'random' else np.arange(M))
    order = np.argsort(priority) if rule == 'random' else priority
    events, snapshots, failures = [], {}, []
    selected = M
    first_failure = None
    full_risk = float(np.sum(C*C))
    full_train = float(np.max(np.sum(abs(E@C), axis=1)))
    cp = set(checkpoints(n, M))
    for step in range(M-N+1):
        m = len(ids)
        if time.process_time() >= cap:
            failures.append({'M': m, 'failure': 'total CPU cap before complete iteration'})
            break
        verification = {}
        if step and (step % 16 == 0 or m in cp):
            previous = C
            Q, R, C = timed('refactor', lambda: qr_map(A0[ids]))
            delta = float(la.norm(C-previous)/max(1e-300, la.norm(C)))
            riskdelta = abs(float(np.sum(C*C)-np.sum(previous*previous)))/max(1e-300, float(np.sum(C*C)))
            verification = {'refactor_map_relative_error': delta, 'refactor_risk_relative_error': riskdelta}
            if delta > 1e-7 or riskdelta > 1e-7:
                failures.append({'M': m, 'failure': 'map/risk refactor relative error', **verification})
                break
        if not np.isfinite(C).all():
            failures.append({'M': m, 'failure': 'nonfinite physical map'})
            break
        risk = float(np.sum(C*C))
        br, reps = timed('score', lambda: integer_risk(C, M))
        train_amp = timed('training', lambda: float(np.max(np.sum(abs(E@C), axis=1))))
        quality = train_amp <= 1.25*full_train and br <= 1.10*full_risk
        if first_failure is None:
            if quality:
                selected = m
            else:
                first_failure = m
        event = {'M': m, 'trace': risk, 'B_integer_risk': br, 'train_amp': train_amp,
                 'operational_prefix': first_failure is None,
                 'logdet_gram': float(2*np.log(abs(np.diag(R))).sum()),
                 'cpu': time.process_time()-started, **verification}
        events.append(event)
        snapshots[m] = ids.copy()
        if m in cp:
            diagnostics = timed('refactor', lambda: validate(A0[ids], Q, R, C))
            event['validation'] = diagnostics
            if not diagnostics['eligible']:
                failures.append({'M': m, 'failure': 'checkpoint numerical guards', **diagnostics})
                break
            if checkpoint_maps:
                t, w = time.process_time(), time.perf_counter()
                checkpoint = raw/f'n{n}-{rule}-m{m}-checkpoint.npz'
                with checkpoint.open('wb') as handle:
                    np.savez(handle, ids=ids, nodes=nodes[ids], operator=C)
                    handle.flush()
                    os.fsync(handle.fileno())
                costs['checkpoint_io'] += time.process_time()-t
                wall_costs['checkpoint_io'] += time.perf_counter()-w
                event['prefix_checkpoint'] = str(checkpoint)
                event['prefix_complete_cpu'] = time.process_time()-started
                event['prefix_complete_wall'] = time.perf_counter()-wall_started
        if m == N:
            break
        if time.process_time() >= cap:
            failures.append({'M': m, 'failure': 'total CPU cap before deletion'})
            break
        t, score_wall = time.process_time(), time.perf_counter()
        h = np.sum(Q*Q, axis=1)
        admissible = 1-h > 1e-10
        if not admissible.any():
            failures.append({'M': m, 'failure': 'no rank-admissible deletion'})
            break
        if rule in ('A', 'D'):
            scores = (np.divide(np.sum(C*C, axis=0), 1-h, out=np.full(m, np.inf),
                                where=admissible) if rule == 'A' else h)
            best = float(np.min(scores[admissible]))
            tied = np.flatnonzero(admissible & (scores <= best+1e-12*max(1., abs(best))))
            j = int(tied[np.argmin(ids[tied])])
        else:
            candidate = np.flatnonzero(admissible)
            j = int(candidate[np.argmin(order[ids[candidate]])])
        den = float(1-h[j])
        predicted_increment = float(np.sum(C[:, j]**2)/den)
        event.update(deleted_original_index=int(ids[j]), deletion_denominator=den,
                     predicted_trace_increment=predicted_increment)
        costs['score'] += time.process_time()-t
        wall_costs['score'] += time.perf_counter()-score_wall
        Q, R = timed('downdate', lambda: la.qr_delete(Q, R, j, which='row',
                                                     overwrite_qr=False, check_finite=False))
        ids = np.delete(ids, j)
        C = timed('map', lambda: la.solve_triangular(R, Q.T, check_finite=False))
        actual = float(np.sum(C*C))
        err = abs(actual-risk-predicted_increment)/max(1., actual)
        event['trace_update_relative_error'] = err
        if err > 1e-7 or actual < risk-1e-10*max(1., risk):
            failures.append({'M': len(ids), 'failure': 'trace update/monotonicity', 'relative_error': err})
            break
    costs['complete_construction'] = time.process_time()-started
    t, w = time.process_time(), time.perf_counter()
    np.savez(raw/f'n{n}-{rule}-path.npz', **{f'm{k}': v for k, v in snapshots.items()})
    costs['checkpoint_io'] += time.process_time()-t
    wall_costs['checkpoint_io'] += time.perf_counter()-w
    wall_costs['complete_construction'] = time.perf_counter()-wall_started
    costs['complete_construction'] = time.process_time()-started
    return {'rule': rule, 'n': n, 'M_start': M, 'N': N, 'selected_M': selected,
            'first_operational_failure_M': first_failure, 'full_trace': full_risk,
            'full_train_amp': full_train, 'curve': events, 'failures': failures,
            'costs_cpu': costs, 'costs_wall': wall_costs}, snapshots


def heldout(n):
    result = {}
    for side in (21, 41):
        axis = np.cos(np.pi*np.linspace(0, 1, side))
        result[f'mesh{side}'] = np.array(list(itertools.product(axis, repeat=3)))
    result['chebyshev'] = np.cos(np.pi*qmc.Sobol(3, scramble=True,
                                                seed=2026110920+n).random_base2(11))
    result['uniform'] = 2*qmc.Sobol(3, scramble=True, seed=2026110930+n).random_base2(11)-1
    return result


def assess(nodes, n, budget, sets, name, raw, haar=False):
    began = time.process_time()
    wall_began = time.perf_counter()
    physical_valid = (len(np.unique(nodes, axis=0)) == len(nodes)
                      and np.isfinite(nodes).all() and np.max(abs(nodes)) <= 1.)
    require(physical_valid, 'non-distinct or invalid physical assessment nodes')
    A = u.basis(nodes, n)
    Q, R, C = qr_map(A)
    if haar:
        C = u.parity_fit(n, np.eye(len(nodes)))
    check = validate(A, Q, R, C)
    row = {'n': n, 'name': name, 'M': len(nodes), 'N': A.shape[1], **check,
           'node_bytes_sha256': array_sha(nodes)}
    if not check['eligible']:
        row['assessment_cpu'] = time.process_time()-began
        return row
    row['map_setup_cpu'] = time.process_time()-began
    row['trace'] = float(np.sum(C*C))
    row['M_trace'] = len(nodes)*row['trace']
    row['integer_risk'], reps = integer_risk(C, budget)
    row['integer_replicates'] = reps.tolist()
    row['replicate_sum'] = int(reps.sum())
    coef = C@old_budget.targets(nodes)
    row['amp'], row['variance_max'], row['function_errors'] = {}, {}, {}
    best41_points, best41_values = np.empty((0, 3)), np.empty(0)
    for key, x in sets.items():
        amp, variance = 0., 0.
        maxerr, square = np.zeros(12), np.zeros(12)
        for offset in range(0, len(x), 512):
            p = x[offset:offset+512]
            E = u.basis(p, n)
            cards = E@C
            norm_values = np.sum(abs(cards), axis=1)
            amp = max(amp, float(norm_values.max()))
            if key == 'mesh41':
                loc = np.argsort(norm_values)[-4:]
                combined_points = np.vstack((best41_points, p[loc]))
                combined_values = np.concatenate((best41_values, norm_values[loc]))
                take = np.argsort(combined_values)[-4:]
                best41_points, best41_values = combined_points[take], combined_values[take]
            variance = max(variance, float(np.sum(cards*cards, axis=1).max()))
            if key in ('uniform', 'chebyshev'):
                error = E@coef-old_budget.targets(p)
                maxerr = np.maximum(maxerr, np.max(abs(error), axis=0))
                square += np.sum(error*error, axis=0)
        row['amp'][key] = amp
        row['variance_max'][key] = variance
        if key in ('uniform', 'chebyshev'):
            row['function_errors'][key] = {'maximum': maxerr.tolist(),
                                           'rms': np.sqrt(square/len(x)).tolist()}
    row['amp_union'] = max(row['amp'].values())
    row['mesh41_largest_points'] = best41_points.tolist()
    row['dense_operator_bytes'] = C.nbytes
    row['application_multiply_add_flops'] = 2*C.shape[0]*C.shape[1]
    sigmas = np.array([0., 1e-4, .01, .1, 1.])
    row['calibrated_MSE'] = (np.array(row['function_errors']['chebyshev']['rms'])[:, None]**2
                             +row['integer_risk']*sigmas[None, :]**2).tolist()
    np.savez(raw/f'n{n}-{name}-map.npz', nodes=nodes, operator=C, replicates=reps)
    row['assessment_cpu'] = time.process_time()-began
    row['assessment_wall'] = time.perf_counter()-wall_began
    return row


def predicted_deletion(C, hat, i):
    keep = np.arange(C.shape[1]) != i
    return (C+np.outer(C[:, i], hat[i]/(1-hat[i, i])))[:, keep]


def choose_feasible(candidates, excluded=()):
    available = [r for r in candidates if r['feasible'] and r['original_index'] not in excluded]
    if not available:
        return None
    best = min(r['train_amp'] for r in available)
    tied = [r for r in available if r['train_amp'] <= best+1e-12*max(1., abs(best))]
    return min(tied, key=lambda r: r['original_index'])


def deletion_candidates(C, Q, E, ids, budget, amp_limit, risk_limit, cap):
    hat = Q@Q.T
    cards = E@C
    rows = []
    for i in range(len(ids)):
        if time.process_time() >= cap:
            return rows, False
        den = float(1-hat[i, i])
        row = {'local_index': i, 'original_index': int(ids[i]), 'denominator': den,
               'feasible': False}
        if den <= 1e-10:
            row['reason'] = 'rank_denominator'
        else:
            candidate = predicted_deletion(C, hat, i)
            keep = np.arange(len(ids)) != i
            L = (cards+np.outer(cards[:, i], hat[i]/den))[:, keep]
            amp = float(np.max(np.sum(abs(L), axis=1)))
            risk, _ = integer_risk(candidate, budget)
            finite = bool(np.isfinite(candidate).all() and np.isfinite(amp) and np.isfinite(risk))
            row.update(train_amp=amp, integer_risk=risk, trace=float(np.sum(candidate*candidate)),
                       feasible=bool(finite and amp <= amp_limit and risk <= risk_limit))
            row['reason'] = ('feasible' if row['feasible'] else
                             'nonfinite' if not finite else
                             'amp_and_noise' if amp > amp_limit and risk > risk_limit else
                             'amp' if amp > amp_limit else 'noise')
        rows.append(row)
    return rows, True


def dense_training(n):
    axis = np.cos(np.pi*np.linspace(0, 1, 9))
    mesh = np.array(list(itertools.product(axis, repeat=3)))
    extra = np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=2026111010+n).random_base2(8))
    return np.vstack((mesh, extra))


def constrained_curve(nodes, n, raw, cap):
    began, wall = time.process_time(), time.perf_counter()
    A = u.basis(nodes, n)
    E = u.basis(dense_training(n), n)
    M, N = A.shape
    ids = np.arange(M)
    Q, R, C = qr_map(A)
    full_trace = float(np.sum(C*C))
    full_amp = float(np.max(np.sum(abs(E@C), axis=1)))
    amp_limit, risk_limit = 1.25*full_amp, 1.10*full_trace
    events, scores, rejected, snapshots = [], [], [], {}
    failures = []
    stop = None
    selection_cpu, validation_cpu = 0., 0.
    while True:
        if time.process_time() >= cap:
            failures.append({'M': len(ids), 'failure': 'total CPU cap before state'})
            stop = 'cpu_cap'
            break
        t = time.process_time()
        check = validate(A[ids], Q, R, C)
        validation_cpu += time.process_time()-t
        if not check['eligible']:
            failures.append({'M': len(ids), 'failure': 'accepted-state numerical guards', **check})
            stop = 'numerical_failure'
            break
        risk, reps = integer_risk(C, M)
        amp = float(np.max(np.sum(abs(E@C), axis=1)))
        if not events or events[-1]['M'] != len(ids):
            events.append({'M': len(ids), 'trace': float(np.sum(C*C)), 'B_integer_risk': risk,
                           'train_amp': amp, 'validation': check, 'cpu': time.process_time()-began})
        snapshots[len(ids)] = ids.copy()
        if len(ids) == N:
            stop = 'reached_N'
            break
        t = time.process_time()
        candidates, complete = deletion_candidates(C, Q, E, ids, M, amp_limit, risk_limit, cap)
        selection_cpu += time.process_time()-t
        state = {'M': len(ids), 'complete': complete, 'candidates': candidates,
                 'feasible_count': sum(r['feasible'] for r in candidates)}
        scores.append(state)
        if not complete:
            failures.append({'M': len(ids), 'failure': 'CPU cap within candidate enumeration'})
            stop = 'cpu_cap'
            break
        excluded = set()
        accepted = False
        while True:
            choice = choose_feasible(candidates, excluded)
            if choice is None:
                stop = 'no_predicted_feasible_deletion' if not excluded else 'all_predicted_feasible_numerically_rejected'
                break
            if time.process_time() >= cap:
                failures.append({'M': len(ids), 'failure': 'CPU cap before selected QR'})
                stop = 'cpu_cap'
                break
            i = choice['local_index']
            next_ids = np.delete(ids, i)
            t = time.process_time()
            q, r, c = qr_map(A[next_ids])
            guard = validate(A[next_ids], q, r, c)
            predicted = predicted_deletion(C, Q@Q.T, i)
            delta = float(la.norm(c-predicted)/max(1e-300, la.norm(c)))
            fresh_amp = float(np.max(np.sum(abs(E@c), axis=1)))
            fresh_risk, _ = integer_risk(c, M)
            fresh = {'M_after': len(next_ids), 'original_index': choice['original_index'],
                     'map_relative_error': delta, 'train_amp': fresh_amp,
                     'integer_risk': fresh_risk, 'validation': guard}
            validation_cpu += time.process_time()-t
            if time.process_time() >= cap:
                fresh['reason'] = 'cpu_cap_after_fresh_trial'
                rejected.append(fresh)
                failures.append({'M': len(ids), 'failure': 'CPU cap after selected QR'})
                stop = 'cpu_cap'
                break
            passed = (guard['eligible'] and delta <= 1e-7 and fresh_amp <= amp_limit
                      and fresh_risk <= risk_limit)
            if passed:
                state['selected_original_index'] = choice['original_index']
                state['selected_fresh'] = fresh
                events[-1]['deleted_original_index'] = choice['original_index']
                ids, Q, R, C = next_ids, q, r, c
                snapshots[len(ids)] = ids.copy()
                events.append({'M': len(ids), 'trace': float(np.sum(C*C)),
                    'B_integer_risk': fresh_risk, 'train_amp': fresh_amp,
                    'validation': guard, 'cpu': time.process_time()-began})
                accepted = True
                break
            fresh['reason'] = 'selected_fresh_guard_or_constraint_or_cap'
            rejected.append(fresh)
            excluded.add(choice['original_index'])
        if not accepted:
            break
    t = time.process_time()
    np.savez(raw/f'n{n}-L-path.npz', **{f'm{k}': v for k, v in snapshots.items()})
    io_cpu = time.process_time()-t
    return {'rule': 'L', 'n': n, 'M_start': M, 'N': N, 'selected_M': len(ids),
            'full_trace': full_trace, 'full_train_amp': full_amp,
            'amp_limit': amp_limit, 'risk_limit': risk_limit,
            'curve': events, 'candidate_tables': scores, 'numerically_rejected': rejected,
            'candidate_states': len(scores), 'candidate_evaluations': sum(len(s['candidates']) for s in scores),
            'rejected_candidate_count': len(rejected),
            'failures': failures, 'stop': stop,
            'costs_cpu': {'complete_construction': time.process_time()-began,
                          'selection': selection_cpu, 'validation': validation_cpu, 'checkpoint_io': io_cpu},
            'costs_wall': {'complete_construction': time.perf_counter()-wall}}, snapshots


def reflection_pairs(recipe, n):
    keys = [tuple(v) for v in recipe['indices']]
    lookup = {v: i for i, v in enumerate(keys)}
    pairs, fixed = [], []
    for i, key in enumerate(keys):
        j = lookup[(n-key[0], key[1], key[2])]
        if i == j:
            fixed.append(i)
        elif i < j:
            pairs.append((i, j))
    return pairs, fixed


def predicted_block(C, hat, pair):
    J = np.asarray(pair, dtype=int)
    keep = np.ones(C.shape[1], dtype=bool)
    keep[J] = False
    D = np.eye(len(J))-hat[np.ix_(J, J)]
    correction = la.solve(D, hat[J][:, keep], assume_a='sym', check_finite=False)
    return C[:, keep]+C[:, J]@correction, correction, keep


def pair_candidates(C, Q, E, pairs, budget, amp_limit, risk_limit, cap):
    hat, cards = Q@Q.T, E@C
    rows = []
    for pair in pairs:
        if time.process_time() >= cap:
            return rows, False
        J = np.asarray(pair, dtype=int)
        eig = la.eigvalsh(np.eye(2)-hat[np.ix_(J, J)], check_finite=False)
        row = {'pair': list(pair), 'block_eigen_min': float(eig[0]), 'feasible': False}
        if eig[0] <= 1e-10:
            row['reason'] = 'block_rank_eigenvalue'
        else:
            candidate, correction, keep = predicted_block(C, hat, pair)
            L = cards[:, keep]+cards[:, J]@correction
            amp = float(np.max(np.sum(abs(L), axis=1)))
            risk, _ = integer_risk(candidate, budget)
            finite = bool(np.isfinite(candidate).all() and np.isfinite(amp) and np.isfinite(risk))
            row.update(train_amp=amp, integer_risk=risk, trace=float(np.sum(candidate*candidate)),
                       feasible=bool(finite and amp <= amp_limit and risk <= risk_limit))
            row['reason'] = ('feasible' if row['feasible'] else 'nonfinite' if not finite else
                'amp_and_noise' if amp > amp_limit and risk > risk_limit else
                'amp' if amp > amp_limit else 'noise')
        rows.append(row)
    return rows, True


def choose_pair(candidates, excluded=(), feasible_only=True):
    eligible = [r for r in candidates if 'train_amp' in r and np.isfinite(r['train_amp'])
                and all(np.isfinite(r[k]) for k in ('integer_risk', 'trace') if k in r)
                and tuple(r['pair']) not in excluded
                and (r['feasible'] or not feasible_only)]
    if not eligible:
        return None
    best = min(r['train_amp'] for r in eligible)
    tied = [r for r in eligible if r['train_amp'] <= best+1e-12*max(1., abs(best))]
    return min(tied, key=lambda r: tuple(r['pair']))


def screen_pair(nodes, n, recipe, raw, cap):
    began, wall = time.process_time(), time.perf_counter()
    A = u.basis(nodes, n)
    E = u.basis(dense_training(n), n)
    Q, R, C = qr_map(A)
    M, N = A.shape
    initial = validate(A, Q, R, C)
    pairs, fixed = reflection_pairs(recipe, n)
    require(len(pairs) == (48 if n == 6 else 100) and len(fixed) == (16 if n == 6 else 25),
            'reflection pair/fixed-plane count mismatch')
    amp0 = float(np.max(np.sum(abs(E@C), axis=1)))
    risk0 = float(np.sum(C*C))
    amp_limit, risk_limit = 1.25*amp0, 1.10*risk0
    candidates, complete = pair_candidates(C, Q, E, pairs, M, amp_limit, risk_limit, cap)
    excluded, rejected, failures = set(), [], []
    selected, next_ids, fresh = None, None, None
    operational = False
    if not initial['eligible']:
        failures.append({'failure': 'initial numerical guards', **initial})
    elif not complete:
        failures.append({'failure': 'CPU cap within pair enumeration'})
    else:
        while True:
            selected = choose_pair(candidates, excluded)
            if selected is None:
                break
            if time.process_time() >= cap:
                failures.append({'failure': 'CPU cap before feasible pair QR'})
                break
            ids = np.delete(np.arange(M), selected['pair'])
            q, r, c = qr_map(A[ids])
            guard = validate(A[ids], q, r, c)
            predicted, _, _ = predicted_block(C, Q@Q.T, selected['pair'])
            delta = float(la.norm(c-predicted)/max(1e-300, la.norm(c)))
            amp = float(np.max(np.sum(abs(E@c), axis=1)))
            risk, _ = integer_risk(c, M)
            fresh = {'pair': selected['pair'], 'map_relative_error': delta, 'train_amp': amp,
                     'integer_risk': risk, 'trace': float(np.sum(c*c)), 'validation': guard}
            if time.process_time() >= cap:
                rejected.append({**fresh, 'reason': 'cpu_cap_after_fresh_pair'})
                failures.append({'failure': 'CPU cap after feasible pair QR'})
                break
            if guard['eligible'] and delta <= 1e-7 and amp <= amp_limit and risk <= risk_limit:
                next_ids = ids
                operational = True
                break
            rejected.append({**fresh, 'reason': 'fresh_guard_or_constraint'})
            excluded.add(tuple(selected['pair']))
    # A failed strict gate still receives a labeled best-rank-admissible diagnostic.
    if not operational and complete and time.process_time() < cap:
        selected = choose_pair(candidates, feasible_only=False)
        if selected is not None:
            next_ids = np.delete(np.arange(M), selected['pair'])
            q, r, c = qr_map(A[next_ids])
            guard = validate(A[next_ids], q, r, c)
            predicted, _, _ = predicted_block(C, Q@Q.T, selected['pair'])
            fresh = {'pair': selected['pair'], 'map_relative_error': float(la.norm(c-predicted)/la.norm(c)),
                'train_amp': float(np.max(np.sum(abs(E@c), axis=1))),
                'integer_risk': integer_risk(c, M)[0], 'trace': float(np.sum(c*c)), 'validation': guard}
    if next_ids is not None:
        with (raw/f'n{n}-pair-checkpoint.npz').open('wb') as handle:
            np.savez(handle, ids=next_ids, nodes=nodes[next_ids])
            handle.flush()
            os.fsync(handle.fileno())
    row = {'rule': 'pair', 'n': n, 'M_start': M, 'N': N, 'selected_M': M-2 if next_ids is not None else M,
        'operational_M': M-2 if operational else M, 'operational_pair': operational,
        'initial_validation': initial, 'full_trace': risk0, 'full_train_amp': amp0,
        'amp_limit': amp_limit, 'risk_limit': risk_limit, 'fixed_plane_count': len(fixed),
        'allowed_pair_count': len(pairs), 'pair_feasible_count': sum(r['feasible'] for r in candidates),
        'candidate_tables': candidates, 'candidate_enumeration_complete': complete,
        'numerically_rejected': rejected, 'rejected_candidate_count': len(rejected),
        'selected_pair': None if selected is None else selected['pair'], 'selected_fresh': fresh,
        'failures': failures, 'costs_cpu': {'complete_construction': time.process_time()-began},
        'costs_wall': {'complete_construction': time.perf_counter()-wall}}
    return row, next_ids, pairs
