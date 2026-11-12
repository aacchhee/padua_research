#!/usr/bin/env python3
"""Known fixed-map degree/replication choices at B637; all outputs MEASURED."""
from __future__ import annotations
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import shutil
import sys
import time

import numpy as np
import scipy
from scipy import linalg as la
from scipy.stats import qmc
import u1_usable as u

TOP = Path(__file__).resolve().parents[1]
BUDGET = 637
SEEDS = (2026110711, 2026110712)
SIGMAS = np.array([0., 1e-5, 1e-4, 1e-3, .01, .1, 1.])
TARGETS = list(u.FUNCTIONS) + [
    'sqrt(2)T13(x)', 'exp(10*(x-1))', 'exp(10*(z-1))',
    'exp(-((x-.23)^2+(y+.11)^2+(z-.37)^2)/.04)',
    'tanh(12*(x+.23*y-.41*z-.07))', 'abs(x-y+.02*z-.15)',
    'cos(11*x+7*y-4*z)', '1/(1+40*(1-x))']


def identity(p):
    p = Path(p).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def dump(p, obj):
    Path(p).write_text(json.dumps(obj, separators=(',', ':'), allow_nan=False)+'\n')


def targets(x):
    a, b, c = x.T
    return np.column_stack((u.targets(x), np.sqrt(2)*np.cos(13*np.arccos(a)),
        np.exp(10*(a-1)), np.exp(10*(c-1)),
        np.exp(-((a-.23)**2+(b+.11)**2+(c-.37)**2)/.04),
        np.tanh(12*(a+.23*b-.41*c-.07)), np.abs(a-b+.02*c-.15),
        np.cos(11*a+7*b-4*c), 1/(1+40*(1-a))))


def allocation(a, budget):
    r = np.ones(len(a), dtype=np.int64)
    assert budget >= len(r)
    for _ in range(budget-len(r)):
        j = int(np.argmax(a/(r*(r+1))))
        r[j] += 1
    return float(np.sum(a/r)), r


def allocation_check():
    checks = 0
    for a in (np.array([.1, 1., 7.]), np.array([2., 2., 2.]), np.array([0., .2, 1.])):
        for budget in range(3, 10):
            risk, r = allocation(a, budget)
            brute = min(float(np.sum(a/np.array(s))) for s in
                        itertools.product(range(1, budget+1), repeat=3) if sum(s) == budget)
            assert abs(risk-brute) < 1e-12 and sum(r) == budget and min(r) >= 1
            checks += 1
    return checks


def build(n, name, raw):
    cpu0, wall0 = time.process_time(), time.perf_counter()
    if name in ('Haar', 'OLS'):
        x, w, recipe = u.parity_nodes(n)
    elif name == 'storedU2':
        p = json.loads((TOP/'evidence/u2-degree12-nodes.json').read_text())
        data = base64.b85decode(p['coordinates_base85'])
        assert hashlib.sha256(data).hexdigest() == p['coordinates_sha256']
        x = np.frombuffer(data, dtype='<f8').reshape(p['N'], 3).copy()
        assert p['n'] == n
        w = np.ones(len(x))/len(x)
        recipe = {'stored_payload': identity(TOP/'evidence/u2-degree12-nodes.json')}
    else:
        x, w, recipe = u.select_nodes(n, 'globalQR')
    M, N = len(x), math.comb(n+3, 3)
    V = u.basis(x, n)
    if name == 'Haar':
        C = u.parity_fit(n, np.eye(M))
    elif M == N:
        C = la.solve(V, np.eye(N), check_finite=False)
    else:
        Q, R = la.qr(V, mode='economic', check_finite=False)
        C = la.solve_triangular(R, Q.T, check_finite=False)
    residual = float(la.norm(C @ V-np.eye(N), np.inf))
    singular = la.svdvals(V, check_finite=False)
    elapsed_cpu = time.process_time()-cpu0
    eligible = bool(M <= BUDGET and np.isfinite(C).all() and residual <= 1e-9
                    and singular[-1] > 0 and elapsed_cpu <= 120)
    row = {'name': name, 'n': n, 'M': M, 'N': N, 'eligible': eligible,
           'reproduction_inf': residual, 'condition2': float(singular[0]/singular[-1]),
           'construction_cpu_seconds': elapsed_cpu,
           'construction_wall_seconds': time.perf_counter()-wall0,
           'dense_operator_bytes': C.nbytes}
    key = f'{name}-n{n}'
    if not eligible:
        row['disposition'] = 'ineligible; retained without repair/quality'
        dump(raw/f'{key}-ineligible.json', row)
        return row, None
    risk, r = allocation(np.sum(C*C, axis=0), BUDGET)
    coef = C @ targets(x)
    row.update(risk=risk, replicate_min=int(r.min()), replicate_max=int(r.max()),
               allocation_budget=int(r.sum()))
    np.savez(raw/f'{key}.npz', nodes=x, weights=w, operator=C,
             integer_replicates=r, coefficients=coef)
    dump(raw/f'{key}-recipe.json', recipe)
    return row, coef


def assess(rows, coefficients, raw, cpu_start):
    clouds = [np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=s).random_base2(15))
              for s in SEEDS]
    np.savez(raw/'assessment.npz', first=clouds[0], second=clouds[1])
    result = np.zeros((len(rows), 2, len(TARGETS)))
    for k, points in enumerate(clouds):
        for start in range(0, len(points), 512):
            if time.process_time()-cpu_start > 600:
                np.save(raw/'partial-assessment-sums.npy', result)
                return None
            x = points[start:start+512]
            truth = targets(x)
            for n in sorted(set(r['n'] for r in rows if r['eligible'])):
                ids = [i for i, r in enumerate(rows) if r['n'] == n and r['eligible']]
                E = u.basis(x, n)
                coefs = np.hstack([coefficients[i] for i in ids])
                predicted = E @ coefs
                for j, idx in enumerate(ids):
                    error = predicted[:, j*len(TARGETS):(j+1)*len(TARGETS)]-truth
                    result[idx, k] += np.sum(error*error, axis=0)/len(points)
            if time.process_time()-cpu_start > 600:
                np.save(raw/'partial-assessment-sums.npy', result)
                return None
    for i, row in enumerate(rows):
        if row['eligible']:
            row['bias_squared'] = result[i].tolist()
    return result


def decisions(rows, bias):
    valid = np.array([r['eligible'] for r in rows])
    risk = np.array([r.get('risk', 0.) for r in rows])
    total = bias[:, :, :, None] + risk[:, None, None, None]*SIGMAS[None, None, None, :]**2
    total[~valid] = np.inf
    winners = np.argmin(total, axis=0)  # cloud, target, sigma
    minimum = np.min(total, axis=0)
    regret = np.empty((len(TARGETS), len(SIGMAS)))
    for t in range(len(TARGETS)):
        for s in range(len(SIGMAS)):
            regret[t, s] = total[winners[0, t, s], 1, t, s]/max(minimum[1, t, s], 1e-30)-1
    baseline = next(i for i, r in enumerate(rows) if r['name'] == 'Haar' and r['n'] == 12)
    primary = 5
    primary_gain = 1-minimum[1, primary]/total[baseline, 1, primary]
    primary_winners = winners[:, primary]
    # Both deterministic and noisy models must be represented; at least one
    # different primary winner and a robust material gain over fixed Haar12.
    gate = bool(len(set(primary_winners[0])) > 1 and np.max(primary_gain) >= .05
                and np.max(regret[primary]) <= .05)
    return {'winners': winners.tolist(), 'first_cloud_choice_second_cloud_regret': regret.tolist(),
            'maximum_second_cloud_regret_by_target': np.max(regret, axis=1).tolist(),
            'primary_gain_over_Haar12_second_cloud': primary_gain.tolist(),
            'primary_practical_gate': gate,
            'total_mse': [total[i].tolist() if valid[i] else None for i in range(len(rows))]}


def compact(obj):
    if isinstance(obj, float): return float(format(obj, '.6g'))
    if isinstance(obj, list): return [compact(x) for x in obj]
    if isinstance(obj, dict): return {k: compact(v) for k, v in obj.items()}
    return obj


def main(a):
    assert not a.out.exists()
    a.raw.mkdir(parents=True, exist_ok=False)
    source_paths = [Path(__file__), Path(u.__file__), u.TRACK/'c3_lebesgue.py',
                    u.TRACK/'c3_rank.py', TOP/'evidence/u2-degree12-nodes.json']
    pins = [identity(p) for p in source_paths]
    for p in source_paths[:4]: shutil.copyfile(p, a.raw/p.name)
    cpu0, wall0 = time.process_time(), time.perf_counter()
    checks = allocation_check()
    rows, coefficients = [], []
    cap = False
    for n in range(1, 14):
        names = (['Haar', 'OLS'] if n <= 12 else []) + ['QR'] + (['storedU2'] if n == 12 else [])
        for name in names:
            row, coef = build(n, name, a.raw)
            rows.append(row); coefficients.append(coef)
            print(json.dumps({k: row.get(k) for k in ('name','n','M','eligible','risk')}), flush=True)
            if time.process_time()-cpu0 > 600:
                cap = True; break
        if cap: break
    construction_cpu = time.process_time()-cpu0
    # Maps are all frozen before either assessment cloud is consulted.
    outcome = None
    if not cap:
        bias = assess(rows, coefficients, a.raw, cpu0)
        if bias is None:
            cap = True
        else:
            outcome = decisions(rows, bias)
            dump(a.raw/'all-decisions.json', outcome)
    dump(a.raw/'all-rows.json', rows)
    dump(a.raw/'inventory.json', [identity(p) for p in sorted(a.raw.iterdir())])
    assert pins == [identity(p) for p in source_paths], 'source/data changed during execution'
    columns = ['name','n','M','N','eligible','reproduction_inf','condition2','risk',
               'replicate_min','replicate_max','construction_cpu_seconds','dense_operator_bytes','bias_squared']
    receipt = {'status': 'MEASURED developer operational decision, not independent audit',
        'input_commit': '97c323bfae15cf3c76f40802c3ebabedceeb0c60',
        'protocol_commit': a.protocol_commit, 'command': sys.argv,
        'executed_utc': datetime.now(timezone.utc).isoformat(), 'sources': pins,
        'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        'assumed_budget': BUDGET, 'noise': 'independent mean-zero equal per-observation variance sigma^2; fixed original map after averaging',
        'sigma': SIGMAS.tolist(), 'targets': TARGETS, 'seeds': list(SEEDS),
        'assessment_count_each': 32768, 'allocation_bruteforce_checks': checks,
        'construction_cpu_seconds': construction_cpu,
        'total_cpu_seconds': time.process_time()-cpu0, 'total_wall_seconds': time.perf_counter()-wall0,
        'whole_run_cap_hit': cap, 'assessment_finished': outcome is not None, 'columns': columns,
        'rows': [[r.get(k) for k in columns] for r in rows],
        'outcome': {k: v for k, v in (outcome or {}).items() if k not in ('total_mse', 'first_cloud_choice_second_cloud_regret')},
        'raw': {'directory': str(a.raw), 'results': identity(a.raw/'all-rows.json'),
                'inventory': identity(a.raw/'inventory.json'),
                'policy': 'regenerate-only; no archival delivery'}}
    payload = json.dumps(compact(receipt), separators=(',', ':'), allow_nan=False)+'\n'
    if len(payload.encode()) >= 16384:
        raise RuntimeError(f'receipt {len(payload.encode())} bytes exceeds limit; no split/omission')
    a.out.write_text(payload)
    print(json.dumps({'receipt_bytes': len(payload.encode()),
        'eligible': sum(r['eligible'] for r in rows),
        'primary_practical_gate': (outcome or {}).get('primary_practical_gate'),
        'seconds': receipt['total_cpu_seconds']}), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--raw', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--protocol-commit', required=True)
    main(p.parse_args())
