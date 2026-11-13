#!/usr/bin/env python3
"""Known projected-gradient variant with explicit finite-step safeguards."""
import json
import math
import time
import numpy as np
import u2_core as core


def separation(points):
    distances = np.linalg.norm(points[:, None, :]-points[None, :, :], axis=2)
    np.fill_diagonal(distances, np.inf)
    return float(distances.min())


def optimize(initial, n, E, raw, cap=120):
    started = time.process_time()
    current = initial.ravel().copy()
    initial_max = float(np.abs(E @ np.linalg.inv(core.old.basis(initial, n))).sum(axis=1).max())
    beta = 40/initial_max
    value, gradient, maximum = core.smooth_value_gradient(current, n, E, beta)
    best, bestmax, bestid = initial.copy(), initial_max, -1
    accepted = 0
    objective_evaluations = 1
    rejected_guard = rejected_armijo = 0
    events = [{'evaluation': 0, 'objective': value, 'train_max': maximum,
               'accepted': True, 'iteration': 0, 'cpu': time.process_time()-started,
               'nodes_raw_sha256': core.array_sha(current)}]
    trials = [current.copy()]
    termination = {'message': '200 accepted-step limit', 'success': False,
                   'iterations': 0, 'status': 'iteration_cap'}
    while accepted < 200:
        if time.process_time()-started >= cap:
            termination.update(message='120 process CPU second cap', status='cpu_cap')
            break
        projected = np.clip(current-gradient, -1, 1)-current
        projected_norm = float(np.max(np.abs(projected)))
        if projected_norm < 1e-7:
            termination.update(message='projected gradient tolerance', success=True, status='gtol')
            break
        points = current.reshape(-1, 3)
        old_separation = separation(points)
        delta = old_separation/(8*math.sqrt(3))
        direction = projected*min(1., delta/projected_norm)
        slope = float(gradient@direction)
        V = core.old.basis(points, n)
        inverse = np.linalg.inv(V)
        step_accepted = False
        for backtrack in range(25):
            if time.process_time()-started >= cap:
                termination.update(message='120 process CPU second cap', status='cpu_cap')
                break
            alpha = 2.**(-backtrack)
            trial = current+alpha*direction
            trial_points = trial.reshape(-1, 3)
            Vtrial = core.old.basis(trial_points, n)
            rho = float(np.linalg.norm((Vtrial-V)@inverse, np.inf))
            serial = len(events)
            trials.append(trial.copy())
            trial_separation = separation(trial_points)
            displacement = float(np.max(np.abs(trial-current)))
            event = {'evaluation': serial, 'iteration': accepted+1, 'backtrack': backtrack,
                     'alpha': alpha, 'rho': rho, 'step_max': displacement, 'delta': delta,
                     'old_separation': old_separation, 'new_separation': trial_separation,
                     'pair_separation_ratio': trial_separation/old_separation,
                     'accepted': False, 'nodes_raw_sha256': core.array_sha(trial)}
            if displacement > delta*(1+1e-12)+1e-15 or trial_separation < .75*old_separation*(1-1e-12):
                raise RuntimeError('declared geometric invariant violated')
            if not np.isfinite(rho) or rho > .5:
                rejected_guard += 1
                event.update(reason='neumann_guard', cpu=time.process_time()-started)
                events.append(event)
                continue
            try:
                trial_value, trial_gradient, trial_maximum = core.smooth_value_gradient(trial, n, E, beta)
                objective_evaluations += 1
                if not np.isfinite(trial_value) or not np.isfinite(trial_gradient).all():
                    raise FloatingPointError('nonfinite objective or gradient')
            except (np.linalg.LinAlgError, FloatingPointError) as error:
                event.update(reason='inverse_or_nonfinite', failure=str(error), cpu=time.process_time()-started)
                rejected_guard += 1
                events.append(event)
                continue
            armijo = value+1e-4*alpha*slope
            event.update(objective=trial_value, train_max=trial_maximum, armijo_rhs=armijo,
                         cpu=time.process_time()-started)
            if trial_value > armijo:
                event['reason'] = 'armijo'
                rejected_armijo += 1
                events.append(event)
                continue
            event.update(accepted=True, reason='accepted')
            events.append(event)
            decrease = (value-trial_value)/max(1, abs(value))
            current, value, gradient = trial, trial_value, trial_gradient
            accepted += 1
            step_accepted = True
            if trial_maximum < bestmax:
                best, bestmax, bestid = trial_points.copy(), trial_maximum, serial
            if decrease <= 1e-10:
                termination.update(message='relative accepted function reduction', success=True, status='ftol')
            break
        if termination['status'] in ('cpu_cap', 'ftol'):
            break
        if not step_accepted:
            termination.update(message='25 backtracks failed', status='backtrack_cap')
            break
    termination['iterations'] = accepted
    fallback = bestmax >= initial_max*(1-1e-4)
    if fallback:
        best = initial.copy()
    np.savez_compressed(raw/f'n{n}-optimization-trials.npz', coordinates=np.asarray(trials))
    (raw/f'n{n}-optimization-events.json').write_text(json.dumps(events, separators=(',', ':'))+'\n')
    return best, {'method': 'admissible_projected_gradient', 'beta': beta, 'epsilon': 1e-8,
                  'initial_train_max': initial_max, 'best_train_max': bestmax,
                  'best_evaluation': bestid, 'evaluations': len(events),
                  'objective_evaluations': objective_evaluations, 'rejected_guard': rejected_guard,
                  'rejected_armijo': rejected_armijo, 'restart_count': 1,
                  'extra_cpu': time.process_time()-started, 'fallback': fallback,
                  'termination': termination}
