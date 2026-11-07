#!/usr/bin/env python3
"""Stable physical-value OLS backward design; finite measurements only."""
from __future__ import annotations
import hashlib
import itertools
import math
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


def curve(nodes, n, rule, raw, cap):
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
    for key, x in sets.items():
        amp, variance = 0., 0.
        maxerr, square = np.zeros(12), np.zeros(12)
        for offset in range(0, len(x), 512):
            p = x[offset:offset+512]
            E = u.basis(p, n)
            cards = E@C
            amp = max(amp, float(np.sum(abs(cards), axis=1).max()))
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
    sigmas = np.array([0., 1e-4, .01, .1, 1.])
    row['calibrated_MSE'] = (np.array(row['function_errors']['chebyshev']['rms'])[:, None]**2
                             +row['integer_risk']*sigmas[None, :]**2).tolist()
    np.savez(raw/f'n{n}-{name}-map.npz', nodes=nodes, operator=C, replicates=reps)
    row['assessment_cpu'] = time.process_time()-began
    row['assessment_wall'] = time.perf_counter()-wall_began
    return row
