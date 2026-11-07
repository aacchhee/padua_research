#!/usr/bin/env python3
"""Known-method joint sampled-norm descent; all quality values are lower samples."""
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.linalg import svdvals
from scipy.optimize import minimize
from scipy.special import logsumexp
from scipy.stats import qmc

import t9_r06_maxima as inherited

old = inherited.prev.old
exponents = inherited.prev.exponents


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_sha(array):
    return hashlib.sha256(np.asarray(array, dtype='<f8').tobytes()).hexdigest()


def basis_gradient(points, n):
    """Physical-coordinate derivatives of the same unscaled Chebyshev basis."""
    tabs = [np.polynomial.chebyshev.chebvander(points[:, k], n) for k in range(3)]
    ders = []
    for k in range(3):
        d = np.zeros_like(tabs[k])
        if n:
            d[:, 1] = 1
        for a in range(1, n):
            d[:, a+1] = 2*tabs[k][:, a] + 2*points[:, k]*d[:, a] - d[:, a-1]
        ders.append(d)
    aa = np.array(exponents(n))
    return np.array([np.prod([ders[k][:, aa[:, k]] if k == axis else
                             tabs[k][:, aa[:, k]] for k in range(3)], axis=0)
                     for axis in range(3)]).transpose(1, 0, 2)


def smooth_value_gradient(flat, n, E, beta):
    points = np.asarray(flat).reshape(-1, 3)
    V = old.basis(points, n)
    inverse = np.linalg.inv(V)
    C = E @ inverse
    smooth_abs = np.sqrt(C*C + 1e-16)
    sums = smooth_abs.sum(axis=1)
    logz = logsumexp(beta*sums)
    D = np.exp(beta*sums-logz)[:, None] * C/smooth_abs
    matrix_gradient = -(C.T @ D) @ inverse.T
    grad = np.einsum('ik,ijk->ij', matrix_gradient, basis_gradient(points, n))
    return float(logz/beta), grad.ravel(), float(np.abs(C).sum(axis=1).max())


def gradient_check(initial, n, E):
    flat = initial.ravel().copy()
    flat += 1e-3*np.sin(np.arange(len(flat))+1)
    flat = np.clip(flat, -.99, .99)
    initial_max = float(np.abs(E @ np.linalg.inv(old.basis(flat.reshape(-1, 3), n))).sum(axis=1).max())
    beta = 40/initial_max
    f, analytic, _ = smooth_value_gradient(flat, n, E, beta)
    checks = []
    for j in np.linspace(0, len(flat)-1, 10, dtype=int):
        plus, minus = flat.copy(), flat.copy()
        plus[j] += 1e-6
        minus[j] -= 1e-6
        fp = smooth_value_gradient(plus, n, E, beta)[0]
        fm = smooth_value_gradient(minus, n, E, beta)[0]
        numeric = (fp-fm)/2e-6
        error = abs(numeric-analytic[j])/max(1, abs(numeric), abs(analytic[j]))
        checks.append([int(j), float(analytic[j]), float(numeric), float(error)])
    return {'objective': f, 'checks': checks, 'max_relative_error': max(r[3] for r in checks)}


class CpuLimit(Exception):
    pass


def optimize(initial, n, E, raw, cap=120):
    start = time.process_time()
    initial_max = float(np.abs(E @ np.linalg.inv(old.basis(initial, n))).sum(axis=1).max())
    beta = 40/initial_max
    best, bestmax, bestid = initial.copy(), initial_max, -1
    events, trials = [], []

    def objective(flat):
        nonlocal best, bestmax, bestid
        if time.process_time()-start >= cap:
            raise CpuLimit()
        serial = len(events)
        trials.append(flat.copy())
        try:
            f, gradient, maximum = smooth_value_gradient(flat, n, E, beta)
            if not np.isfinite(f) or not np.isfinite(gradient).all():
                raise FloatingPointError('nonfinite objective or gradient')
            improved = maximum < bestmax
            if improved:
                best, bestmax, bestid = flat.reshape(-1, 3).copy(), maximum, serial
            events.append({'evaluation': serial, 'objective': f, 'train_max': maximum,
                           'cpu': time.process_time()-start, 'new_best': bool(improved),
                           'nodes_raw_sha256': array_sha(flat)})
            return f, gradient
        except (np.linalg.LinAlgError, FloatingPointError) as error:
            events.append({'evaluation': serial, 'failure': str(error), 'cpu': time.process_time()-start,
                           'nodes_raw_sha256': array_sha(flat)})
            return 1e100, np.zeros_like(flat)

    try:
        result = minimize(objective, initial.ravel(), jac=True, method='L-BFGS-B',
                          bounds=[(-1, 1)]*initial.size,
                          options={'maxiter': 150, 'maxfun': 1000, 'maxls': 30,
                                   'maxcor': 10, 'ftol': 1e-10, 'gtol': 1e-7})
        termination = {'message': str(result.message), 'success': bool(result.success),
                       'iterations': int(result.nit), 'status': int(result.status)}
    except CpuLimit:
        termination = {'message': '120 process CPU second cap', 'success': False, 'iterations': None,
                       'status': 'cpu_cap'}
    fallback = bestmax >= initial_max*(1-1e-4)
    if fallback:
        best = initial.copy()
    np.savez_compressed(raw/f'n{n}-optimization-trials.npz', coordinates=np.asarray(trials))
    (raw/f'n{n}-optimization-events.json').write_text(json.dumps(events, separators=(',', ':'))+'\n')
    return best, {'beta': beta, 'epsilon': 1e-8, 'initial_train_max': initial_max,
                  'best_train_max': bestmax, 'best_evaluation': bestid, 'evaluations': len(events),
                  'restart_count': 1, 'extra_cpu': time.process_time()-start,
                  'fallback': fallback, 'termination': termination}


def dyadic_rank(points, n, prime):
    aa = exponents(n)
    tabs = []
    for k in range(3):
        coordinate = []
        for x in points[:, k]:
            numerator, denominator = float(x).as_integer_ratio()
            coordinate.append(numerator % prime * pow(denominator, -1, prime) % prime)
        x = np.asarray(coordinate, dtype=np.int64)
        tab = np.ones((len(points), n+1), dtype=np.int64)
        if n:
            tab[:, 1] = x
        for degree in range(1, n):
            tab[:, degree+1] = (2*x*tab[:, degree]-tab[:, degree-1]) % prime
        tabs.append(tab)
    matrix = np.array([((tabs[0][:, a]*tabs[1][:, b]) % prime)*tabs[2][:, c] % prime
                       for a, b, c in aa], dtype=np.int64).T.copy()
    rank = 0
    for column in range(len(aa)):
        found = np.flatnonzero(matrix[rank:, column])
        if not len(found):
            continue
        pivot = rank+int(found[0])
        matrix[[rank, pivot]] = matrix[[pivot, rank]]
        matrix[rank, column:] = matrix[rank, column:]*pow(int(matrix[rank, column]), -1, prime) % prime
        if rank+1 < len(points):
            matrix[rank+1:, column:] = (matrix[rank+1:, column:] -
                matrix[rank+1:, column, None]*matrix[rank, None, column:]) % prime
        rank += 1
        if rank == len(points):
            break
    return rank


def targets(points):
    x, y, z = points.T
    return np.column_stack((np.exp(x+y+z), 1/(1+5*(x*x+y*y+z*z)),
                            np.abs(x+y+z)/3, np.cos(3*x+2*y-z)))


def assess(points, n, raw, family):
    V = old.basis(points, n)
    inverse = np.linalg.inv(V)
    sing = svdvals(V)
    scale = np.array([2**(sum(k > 0 for k in a)/2) for a in exponents(n)])
    ortho = svdvals(V*scale)
    condition, residual = float(sing[0]/sing[-1]), float(np.linalg.norm(V@inverse-np.eye(len(V)), np.inf))
    row = {'conditioning': [condition, float(ortho[0]/ortho[-1]), residual,
                            float(np.linalg.slogdet(V)[1])], 'N': len(points),
           'unique': len(np.unique(points, axis=0)), 'eligible': condition < 1e12 and residual <= 1e-7}
    np.save(raw/f'n{n}-{family}-nodes.npy', points)
    row['node_file'] = f'n{n}-{family}-nodes.npy'
    row['node_sha256'] = sha(raw/row['node_file'])
    row['dyadic_ranks'] = []
    for prime in (1000003, 1000033):
        rank = dyadic_rank(points, n, prime)
        row['dyadic_ranks'].append([prime, rank])
        if rank == len(points):
            break
    if not row['eligible']:
        return row
    maxima = []
    for q in (21, 41):
        _, values = inherited.prev.grid(inverse, n, q)
        maxima.append(float(max(values)))
    axis = np.cos(np.pi*(np.arange(32)+.5)/32)
    gauss = np.array(list(it.product(axis, repeat=3)))
    sobol = 2*qmc.Sobol(3, scramble=True, seed=2026110702).random_base2(13)-1
    corners = np.array(list(it.product([-1., 1.], repeat=3)))
    noise = np.random.default_rng(2026110703+n).choice([-1., 1.], size=(len(points), 16))*1e-6
    function_coefficients, noise_coefficients = inverse@targets(points), inverse@noise
    errors, noisy, eval_details = {}, {}, {}
    gauss_values = None
    for name, cloud in (('gauss', gauss), ('sobol', sobol)):
        all_norms, function_diff, noise_out = [], [], []
        for offset in range(0, len(cloud), 512):
            chunk = cloud[offset:offset+512]
            E = old.basis(chunk, n)
            all_norms.append(np.abs(E@inverse).sum(axis=1))
            function_diff.append(E@function_coefficients-targets(chunk))
            noise_out.append(E@noise_coefficients)
        norms = np.concatenate(all_norms)
        fd, nd = np.vstack(function_diff), np.vstack(noise_out)
        maxima.append(float(norms.max()))
        errors[name] = np.column_stack((np.max(np.abs(fd), axis=0), np.sqrt(np.mean(fd*fd, axis=0)))).tolist()
        noisy[name] = [float(np.abs(nd).max()), float(np.sqrt(np.mean(nd*nd))), float(norms.max())]
        eval_details[name] = {'noise_trial_max': np.max(np.abs(nd), axis=0).tolist(),
                              'noise_trial_rms': np.sqrt(np.mean(nd*nd, axis=0)).tolist()}
        if name == 'gauss':
            gauss_values = norms
    maxima.append(float(np.abs(old.basis(corners, n)@inverse).sum(axis=1).max()))
    ids = np.argsort(gauss_values)[-4:]
    starts = list(np.arccos(np.clip(gauss[ids], -1, 1))) + list(it.product([0, np.pi], repeat=3))
    (refined, _), refinements = inherited.refine(inverse, n, starts)
    maxima.append(float(max(refined, *maxima[2:])))
    row.update(norms=maxima, errors=errors, noise=noisy,
               refinement_success=sum(r['success'] for r in refinements))
    (raw/f'n{n}-{family}-assessment-details.json').write_text(json.dumps(
        {'refinements': refinements, **eval_details}, separators=(',', ':'))+'\n')
    return row
