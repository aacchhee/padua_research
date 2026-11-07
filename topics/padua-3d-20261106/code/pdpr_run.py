#!/usr/bin/env python3
"""P1 prospective parity-grid backward design pilot; numerical evidence only."""
from __future__ import annotations
import argparse
import base64
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import sys
import time
import zlib
import numpy as np
import scipy
from scipy import linalg as la
import pdpr_core as core
import t9_r06_maxima as old_det

TOP = Path(__file__).resolve().parents[1]


def dump(path, x):
    Path(path).write_text(json.dumps(x, separators=(',', ':'), allow_nan=False)+'\n')


def compact(x):
    if isinstance(x, float):
        return float(format(x, '.8g'))
    if isinstance(x, list):
        return [compact(v) for v in x]
    if isinstance(x, dict):
        return {k: compact(v) for k, v in x.items()}
    return x


def control_gate(controls):
    values = list(controls.values())
    return (len(values) == 2 and all('risk_ratio' in r and 'amp_ratio' in r for r in values)
            and ((all(r['risk_ratio'] <= .95 for r in values)
                  and all(r['amp_ratio'] <= 1.10 for r in values))
                 or (all(r['amp_ratio'] <= .95 for r in values)
                     and all(r['risk_ratio'] <= 1.10 for r in values))))


def numerical_gate(degrees, rule):
    return (len(degrees) == 3 and {r['n'] for r in degrees} == {4, 6, 8}
            and all(r['decisions'][rule].get('guards', False) for r in degrees))


def retained_rule(gates):
    eligible = [r for r in ('A', 'D') if gates[r]['passes']]
    if not eligible:
        return None
    if len(eligible) == 1:
        return eligible[0]
    a, d = (gates[r]['worst_risk_ratio'] for r in ('A', 'D'))
    return 'A' if abs(a-d) <= 1e-8 or a < d else 'D'


def engineering(raw):
    rng = np.random.default_rng(2026110901)
    checks = []
    for m, n in ((9, 3), (10, 6), (7, 6)):
        A = rng.normal(size=(m, n))
        Q, R, C = core.qr_map(A)
        for j in range(m):
            h = float(Q[j]@Q[j])
            pred = float(np.sum(C*C)+np.sum(C[:, j]**2)/(1-h))
            q, r = la.qr_delete(Q, R, j, which='row', check_finite=False)
            c = la.solve_triangular(r, q.T)
            freshq, freshr, fresh = core.qr_map(np.delete(A, j, axis=0))
            err = float(la.norm(c-fresh)/max(1., la.norm(fresh)))
            traceerr = abs(float(np.sum(c*c))-pred)/max(1., pred)
            core.require(err < 1e-10 and traceerr < 1e-10, 'synthetic deletion mismatch')
            diag = core.validate(np.delete(A, j, axis=0), q, r, c)
            core.require(diag['eligible'], 'synthetic QR guard failure')
            checks.append([m, n, j, err, traceerr])
    # Exhaustive small integer allocation, independent of polynomial design.
    import itertools
    allocation_checks = []
    for values in ((.1, 1., 7.), (2., 2., 2.), (0., .2, 1.)):
        C = np.diag(np.sqrt(values))
        for budget in range(3, 10):
            risk, reps = core.integer_risk(C, budget)
            brute = min(sum(a/r for a, r in zip(values, rs)) for rs in
                        itertools.product(range(1, budget+1), repeat=3) if sum(rs) == budget)
            core.require(abs(risk-brute) < 1e-12, 'integer allocation mismatch')
            allocation_checks.append([list(values), budget, risk, reps.tolist()])
    branch_cases = [({'random': {'risk_ratio': .94, 'amp_ratio': 1.05},
                       'lex': {'risk_ratio': 1.05, 'amp_ratio': .94}}, False),
                    ({'random': {'risk_ratio': .94, 'amp_ratio': 1.05},
                       'lex': {'risk_ratio': .93, 'amp_ratio': 1.10}}, True),
                    ({'random': {'risk_ratio': 1.10, 'amp_ratio': .94},
                       'lex': {'risk_ratio': 1.05, 'amp_ratio': .93}}, True),
                    ({'random': {'risk_ratio': .94, 'amp_ratio': 1.11},
                       'lex': {'risk_ratio': .93, 'amp_ratio': 1.05}}, False),
                    ({'random': {'unavailable': True}, 'lex': {'unavailable': True}}, False)]
    for controls, expected in branch_cases:
        core.require(control_gate(controls) == expected, 'common-metric control gate mismatch')
    tie_cases = [(1.01, 1.01-5e-9, 'A'), (1.01, 1.01-2e-8, 'D'),
                 (1.01-2e-8, 1.01, 'A')]
    for av, dv, expected in tie_cases:
        core.require(retained_rule({'A': {'passes': True, 'worst_risk_ratio': av},
                                    'D': {'passes': True, 'worst_risk_ratio': dv}}) == expected,
                     'explicit tie-to-A branch mismatch')
    numerical_cases = []
    for flags, expected in (([True, True, True], True), ([False, True, True], False),
                            ([True, False, True], False), ([True, True], False)):
        deg = [{'n': n, 'decisions': {'A': {'guards': flag}}} for n, flag in zip((4, 6, 8), flags)]
        core.require(numerical_gate(deg, 'A') == expected, 'all-degree numerical gate mismatch')
        numerical_cases.append([flags, expected])
    cardinal_cases = []
    rng = np.random.default_rng(2026111001)
    for m, n in ((9, 3), (10, 6), (7, 6)):
        A = rng.normal(size=(m, n))
        E = rng.normal(size=(13, n))
        Q, R, C = core.qr_map(A)
        hat = Q@Q.T
        amp_limit = 1.25*float(np.max(np.sum(abs(E@C), axis=1)))
        risk_limit = 1.10*float(np.sum(C*C))
        candidates, completed = core.deletion_candidates(C, Q, E, np.arange(m), m,
            amp_limit, risk_limit, time.process_time()+30)
        core.require(completed and len(candidates) == m, 'synthetic candidate census incomplete')
        for i, row in enumerate(candidates):
            q, r, fresh = core.qr_map(np.delete(A, i, axis=0))
            predicted = core.predicted_deletion(C, hat, i)
            relative = float(la.norm(fresh-predicted)/la.norm(fresh))
            amp = float(np.max(np.sum(abs(E@fresh), axis=1)))
            risk, reps = core.integer_risk(fresh, m)
            core.require(relative <= 1e-10 and abs(amp-row['train_amp']) <= 1e-10*max(1., amp)
                         and abs(risk-row['integer_risk']) <= 1e-10*max(1., risk),
                         'raw cardinal candidate formula mismatch')
            core.require(row['feasible'] == (amp <= amp_limit and risk <= risk_limit),
                         'exhaustive feasible classification mismatch')
            cardinal_cases.append([m, n, i, relative, row['feasible']])
    # Lowest amp violates noise; a different row remains feasible and must win.
    selection_branches = [([{'original_index': 0, 'train_amp': 1., 'feasible': False},
                            {'original_index': 1, 'train_amp': 2., 'feasible': True}], 1),
                          ([{'original_index': 4, 'train_amp': 2., 'feasible': True},
                            {'original_index': 2, 'train_amp': 2.+1e-13, 'feasible': True}], 2),
                          ([{'original_index': 0, 'train_amp': 1., 'feasible': False}], None)]
    for rows, expected in selection_branches:
        choice = core.choose_feasible(rows)
        core.require((None if choice is None else choice['original_index']) == expected,
                     'feasibility-before-objective selection mismatch')
    # Synthetic duplicate-row design, mocked CPU clock; no polynomial grid.
    cap_cases = []
    saved_basis, saved_training, saved_clock = core.u.basis, core.dense_training, core.time.process_time
    nodes = np.column_stack((np.arange(6), np.zeros((6, 2))))
    design = np.array([[1., 0.]]*3+[[0., 1.]]*3)
    query = np.column_stack((1000+np.arange(2), np.zeros((2, 2))))
    def synthetic_basis(points, n):
        ids = np.asarray(points)[:, 0].astype(int)
        return np.eye(2)[ids-1000] if np.all(ids >= 1000) else design[ids]
    try:
        core.u.basis = synthetic_basis
        core.dense_training = lambda n: query
        for limit in range(5, 181, 5):
            tick = [0]
            def mocked_cpu():
                tick[0] += 1
                return float(tick[0])
            core.time.process_time = mocked_cpu
            directory = raw/f'mocked-cap-{limit}'
            directory.mkdir()
            path, states = core.constrained_curve(nodes, 0, directory, float(limit))
            if states:
                core.require(path['selected_M'] in states, 'cap returned unrecorded accepted support')
                core.require(any(e['M'] == path['selected_M'] for e in path['curve']),
                             'cap terminal missing fresh verified curve state')
            cap_rejections = [r for r in path['numerically_rejected'] if r.get('reason') == 'cpu_cap_after_fresh_trial']
            if cap_rejections:
                core.require(path['stop'] == 'cpu_cap', 'post-trial cap mislabeled numerical exhaustion')
            cap_cases.append([limit, path['selected_M'], sorted(states), path['stop'], len(cap_rejections)])
    finally:
        core.u.basis, core.dense_training, core.time.process_time = saved_basis, saved_training, saved_clock
    core.require(any(len(r[2]) > 1 and r[3] == 'cpu_cap' for r in cap_cases), 'accepted-then-cap branch unexercised')
    core.require(any(r[4] for r in cap_cases), 'post-trial-cap branch unexercised')
    checkpoint_checks = []
    saved_basis, saved_training = core.u.basis, core.training
    synthetic_nodes = np.column_stack((np.linspace(-1, 1, 6), np.zeros((6, 2))))
    def checkpoint_basis(points, n):
        x = np.asarray(points)[:, 0]
        return np.eye(2)[x.astype(int)-1000] if np.all(x >= 1000) else design[np.rint((x+1)*2.5).astype(int)]
    try:
        core.u.basis = checkpoint_basis
        core.training = lambda n: query
        dirs = [raw/'checkpoint-on', raw/'checkpoint-off']
        for directory in dirs:
            directory.mkdir()
        on, on_states = core.curve(synthetic_nodes, 0, 'A', dirs[0], time.process_time()+30, checkpoint_maps=True)
        off, off_states = core.curve(synthetic_nodes, 0, 'A', dirs[1], time.process_time()+30)
        core.require(not on['failures'] and not off['failures'], 'checkpoint synthetic path guard failure')
        core.require(on_states.keys() == off_states.keys() and
                     all(np.array_equal(on_states[m], off_states[m]) for m in on_states),
                     'durable checkpoint changed deletion arithmetic')
        for event in on['curve']:
            if 'prefix_checkpoint' in event:
                with np.load(event['prefix_checkpoint'], allow_pickle=False) as data:
                    core.require(np.array_equal(data['ids'], on_states[event['M']]), 'checkpoint IDs mismatch')
                    error = float(la.norm(data['operator']@design[data['ids']]-np.eye(2), np.inf))
                core.require(error <= 1e-10 and event['prefix_complete_cpu'] <= on['costs_cpu']['complete_construction'],
                             'checkpoint map/prefix cost mismatch')
                checkpoint_checks.append([event['M'], error, event['prefix_complete_cpu']])
    finally:
        core.u.basis, core.training = saved_basis, saved_training
    gradient_checks = []
    random = np.random.default_rng(2026111901)
    n = 2
    scale = np.array([2.**(sum(v > 0 for v in aa)/2) for aa in core.u.exponents(n)])
    rectangular = random.normal(size=(len(scale), 13))
    for theta in random.uniform(.2, 2.9, size=(3, 3)):
        value, gradient = old_det.prev.basis_angle(theta, n, True)
        cards = (value*scale)@rectangular
        direct = core.u.basis(np.cos(theta)[None, :], n)[0]@rectangular
        core.require(np.max(abs(cards-direct)) < 1e-12, 'rectangular physical/angular basis scaling mismatch')
        analytic = (gradient*scale)@rectangular@np.sign(cards)
        for axis in range(3):
            plus, minus = theta.copy(), theta.copy()
            plus[axis] += 1e-6
            minus[axis] -= 1e-6
            fp = np.sum(abs((old_det.prev.basis_angle(plus, n)*scale)@rectangular))
            fm = np.sum(abs((old_det.prev.basis_angle(minus, n)*scale)@rectangular))
            numerical = float((fp-fm)/2e-6)
            err = abs(numerical-analytic[axis])/max(1., abs(numerical))
            core.require(err <= 1e-7, 'rectangular angular norm gradient mismatch')
            gradient_checks.append([axis, float(err)])
    return {'synthetic_deletions': checks, 'integer_allocations': allocation_checks,
            'control_gate_branch_cases': branch_cases, 'tie_branch_cases': tie_cases,
            'all_degree_gate_cases': numerical_cases, 'cardinal_candidate_checks': cardinal_cases,
            'feasibility_selection_branches': selection_branches, 'mocked_cap_cases': cap_cases,
            'durable_checkpoint_checks': checkpoint_checks, 'rectangular_gradient_checks': gradient_checks, 'passes': True}


def run_pilot(a):
    began_cpu = time.process_time()
    began_wall = time.perf_counter()
    absolute_cap = began_cpu+900
    details = {'paths': [], 'assessments': [], 'degrees': [], 'unrun': []}
    sources = [Path(__file__), Path(core.__file__), Path(core.u.__file__),
               Path(core.old_budget.__file__), Path(old_det.__file__),
               Path(old_det.prev.__file__), Path(old_det.prev.old.__file__),
               TOP/'code/t4_stacks.py', TOP.parents[1]/'tracks/lattice-unisolvence/code/c3_rank.py']
    sourcepins = [core.identity(p) for p in sources]
    for p in sources:
        (a.scratch/('source-'+p.name)).write_bytes(p.read_bytes())
    for n in (4, 6, 8):
        if time.process_time() >= absolute_cap:
            details['unrun'].append({'degree': n, 'stage': 'entire degree'})
            continue
        t, generation_wall = time.process_time(), time.perf_counter()
        nodes, _, recipe = core.u.parity_nodes(n)
        generation_cpu = time.process_time()-t
        generation_wall = time.perf_counter()-generation_wall
        dump(a.scratch/f'n{n}-recipe.json', recipe)
        paths, snapshots = {}, {}
        for rule in core.RULES:
            if time.process_time() >= absolute_cap:
                details['unrun'].append({'degree': n, 'stage': 'path', 'rule': rule})
                continue
            row, snaps = core.curve(nodes, n, rule, a.scratch, absolute_cap)
            row['costs_cpu']['node_generation'] = generation_cpu
            row['costs_cpu']['complete_construction'] += generation_cpu
            row['costs_wall']['node_generation'] = generation_wall
            row['costs_wall']['complete_construction'] += generation_wall
            paths[rule], snapshots[rule] = row, snaps
            details['paths'].append(row)
            print(json.dumps({'stage': 'path', 'n': n, 'rule': rule,
                              'selected_M': row['selected_M'], 'failures': row['failures'],
                              'cpu': row['costs_cpu']['complete_construction']}), flush=True)
        t = time.process_time()
        sets = core.heldout(n)
        query_setup_cpu = time.process_time()-t
        assessed, aliases = {}, {}
        def assess(name, x, haar=False):
            key = (core.array_sha(x), haar)
            if key in assessed:
                aliases[name] = assessed[key]['name']
                return assessed[key]
            if time.process_time() >= absolute_cap:
                details['unrun'].append({'degree': n, 'stage': 'assessment', 'name': name})
                return None
            row = core.assess(x, n, len(nodes), sets, name, a.scratch, haar=haar)
            assessed[key] = row
            aliases[name] = name
            details['assessments'].append(row)
            return row
        full = assess('OLS-full', nodes)
        assess('Haar-full', nodes, haar=True)
        for rule, path in paths.items():
            counts = set(core.checkpoints(n, len(nodes))) | {path['selected_M']}
            for m in sorted(counts, reverse=True):
                if m in snapshots[rule]:
                    assess(f'{rule}-m{m}', nodes[snapshots[rule][m]])
        # Same-count random/lex controls at each optimized rule's selected count.
        for rule in ('A', 'D'):
            if rule not in paths:
                continue
            m = paths[rule]['selected_M']
            for control in ('random', 'lex'):
                if control in snapshots and m in snapshots[control]:
                    assess(f'{control}-m{m}', nodes[snapshots[control][m]])
        t = time.process_time()
        if time.process_time() >= absolute_cap:
            details['unrun'].append({'degree': n, 'stage': 'restrictedQR construction'})
            break
        restricted_wall = time.perf_counter()
        piv = la.qr(old_det.prev.old.basis(nodes, n).T, pivoting=True,
                    mode='economic', check_finite=False)[2]
        restricted_cpu = time.process_time()-t+generation_cpu
        restricted_wall = time.perf_counter()-restricted_wall+generation_wall
        counts = set(core.checkpoints(n, len(nodes))) | {p['selected_M'] for p in paths.values()}
        for m in sorted(counts, reverse=True):
            assess(f'restrictedQR-m{m}', nodes[piv[:m]])
        if time.process_time() < absolute_cap:
            t, global_wall = time.process_time(), time.perf_counter()
            global_nodes = old_det.prev.qrpoints(n)
            global_cpu = time.process_time()-t
            global_wall = time.perf_counter()-global_wall
            global_row = assess('globalQR', global_nodes)
            if global_row is not None:
                global_row['construction_cpu'] = global_cpu
                global_row['construction_wall'] = global_wall
            if time.process_time() < absolute_cap:
                t, local_wall = time.process_time(), time.perf_counter()
                local_nodes, trace = old_det.exchange(global_nodes.copy(), n)
                local_cpu = time.process_time()-t
                local_wall = time.perf_counter()-local_wall
                local_row = assess('localdet', local_nodes)
                if local_row is not None:
                    local_row['construction_cpu'] = global_cpu+local_cpu
                    local_row['construction_wall'] = global_wall+local_wall
                    local_row['determinant_trace'] = trace
        if full is not None and full['eligible']:
            for row in assessed.values():
                if row['eligible']:
                    row['target_regressions_to_full'] = {}
                    for measure in ('uniform', 'chebyshev'):
                        report = {}
                        for metric in ('rms', 'maximum'):
                            values = np.array(row['function_errors'][measure][metric])
                            ref = np.array(full['function_errors'][measure][metric])
                            ratio = values/np.maximum(ref, 1e-14)
                            report[metric] = {'worse_count': int(np.sum(values > 1.01*ref+1e-14)),
                                              'worst_ratio_above_floor': float(np.max(ratio))}
                        row['target_regressions_to_full'][measure] = report
        byname = {r['name']: r for r in assessed.values()}
        def lookup(name):
            return byname.get(aliases.get(name))
        decisions = {}
        for rule in ('A', 'D'):
            path = paths.get(rule)
            row = lookup(f'{rule}-m{path["selected_M"]}') if path else None
            decision = {'complete': row is not None and full is not None}
            if row is not None and full is not None:
                m = path['selected_M']
                checkpoint_rows = [lookup(name) for name in aliases if name.startswith(rule+'-m')]
                guards = (row['eligible'] and not path['failures'] and bool(checkpoint_rows)
                          and all(r is not None and r['eligible'] for r in checkpoint_rows))
                if row['eligible'] and full['eligible']:
                    decision.update(M=m, saving=1-m/len(nodes),
                        amp_ratio=row['amp_union']/full['amp_union'],
                        risk_ratio=row['integer_risk']/full['integer_risk'],
                        guards=bool(guards), controls={})
                    for control in ('random', 'lex'):
                        c = lookup(f'{control}-m{m}')
                        if c and c['eligible']:
                            decision['controls'][control] = {
                                'risk_ratio': row['integer_risk']/c['integer_risk'],
                                'amp_ratio': row['amp_union']/c['amp_union']}
                        else:
                            decision['controls'][control] = {'unavailable': True}
                    decision['control_gain'] = control_gate(decision['controls'])
                    decision['quality'] = bool(guards and decision['saving'] >= .10
                        and decision['amp_ratio'] <= 1.30 and decision['risk_ratio'] <= 1.10)
                    decision['function_error_ratio_to_full'] = {
                        measure: [float(v/max(w, 1e-14)) for v, w in zip(
                            row['function_errors'][measure]['rms'], full['function_errors'][measure]['rms'])]
                        for measure in ('uniform', 'chebyshev')}
            decisions[rule] = decision
        details['degrees'].append({'n': n, 'M_start': len(nodes),
            'restrictedQR_construction_cpu': restricted_cpu, 'restrictedQR_construction_wall': restricted_wall,
            'node_generation_cpu': generation_cpu, 'node_generation_wall': generation_wall,
            'query_setup_cpu': query_setup_cpu,
            'aliases': aliases, 'decisions': decisions})
        print(json.dumps({'stage': 'degree', 'n': n, 'decisions': decisions}), flush=True)
        dump(a.scratch/'partial-details.json', details)
    gates = {}
    for rule in ('A', 'D'):
        d = [r['decisions'][rule] for r in details['degrees'] if r['n'] in (6, 8)]
        numerical = numerical_gate(details['degrees'], rule)
        passes = (numerical and len(d) == 2 and all(x.get('quality', False) for x in d)
                  and any(x.get('control_gain', False) for x in d))
        gates[rule] = {'passes': passes, 'all_degree_numerical_guards': numerical,
                      'worst_risk_ratio': max((x.get('risk_ratio', 1e100) for x in d), default=1e100)}
    selected = retained_rule(gates)
    details['gate'] = {'rules': gates, 'selected_rule': selected,
                       'passes': selected is not None and not details['unrun']
                       and time.process_time()-began_cpu <= 900}
    details['timing'] = {'actual_cpu': time.process_time()-began_cpu,
                         'wall': time.perf_counter()-began_wall,
                         'allowance_cpu': 900}
    core.require(sourcepins == [core.identity(p) for p in sources], 'executed sources changed')
    dump(a.scratch/'details.json', details)
    inventory = [core.identity(p) for p in sorted(a.scratch.rglob('*')) if p.is_file()]
    dump(a.scratch/'inventory.json', inventory)
    return details, sourcepins


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--round', choices=('pilot', 'engineering', 'constrained', 'frontier'), required=True)
    p.add_argument('--protocol-commit')
    p.add_argument('--reference', type=Path)
    p.add_argument('--scratch', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=False)
    started = datetime.now(timezone.utc).isoformat()
    if a.round == 'frontier':
        core.require(bool(a.protocol_commit) and a.reference is not None, 'P3requires protocol/P1reference')
        run_frontier(a)
        return
    if a.round == 'constrained':
        core.require(bool(a.protocol_commit) and a.reference is not None, 'P2requires published protocol and P1reference')
        run_constrained(a)
        return
    if a.round == 'engineering':
        result = engineering(a.scratch)
        receipt = {'status': 'Engineering verification only; zero research rounds',
                   'command': sys.argv, 'result': result,
                   'sources': [core.identity(__file__), core.identity(core.__file__)]}
    else:
        core.require(bool(a.protocol_commit), 'published protocol commit required')
        details, sources = run_pilot(a)
        columns = ['n', 'name', 'M', 'eligible', 'condition2', 'reproduction_inf',
                   'trace', 'M_trace', 'integer_risk', 'amp_union', 'amp', 'variance_max',
                   'map_setup_cpu', 'assessment_cpu', 'target_regressions_to_full']
        logical = {'columns': columns,
                   'rows': [[row.get(k) for k in columns] for row in details['assessments']],
                   'paths': [{k: v for k, v in r.items() if k != 'curve'} for r in details['paths']],
                   'degrees': details['degrees'], 'gate': details['gate'], 'unrun': details['unrun']}
        payload = json.dumps(compact(logical), separators=(',', ':'), allow_nan=False).encode()
        receipt = {'status': 'MEASURED finite pilot; lower amplification samples',
            'round': 'P1', 'input_head': '6d894d50efd8167c5b10f3d5b0da4d8cf214b681',
            'protocol_commit': a.protocol_commit, 'command': sys.argv, 'sources': sources,
            'timing': details['timing'], 'gate': details['gate'],
            'logical_results_codec': 'UTF8 JSON -> zlib.compress(level9) -> ASCII base85; entire result object, unsplit',
            'logical_results_base85': base64.b85encode(zlib.compress(payload, 9)).decode(),
            'logical_results_uncompressed_bytes': len(payload),
            'raw_details': core.identity(a.scratch/'details.json'),
            'raw_inventory': core.identity(a.scratch/'inventory.json'),
            'raw_policy': 'unique local regeneration-only; full curves/functions/maps/recipes retained, no archive delivery',
            'target_functions': list(core.old_budget.TARGETS),
            'seeds': {'random': '2026110900+n', 'training': '2026110910+n',
                      'chebyshev': '2026110920+n', 'uniform': '2026110930+n'},
            'scope': 'Unweighted physical OLS; iid equal single-observation variance; fixed-map integer repeats at B=Mstart; orthonormal product-Chebyshev output. Haar baseline separate. No generic user noise/measure/cost facts.'}
    receipt.update(started_utc=started, ended_utc=datetime.now(timezone.utc).isoformat(),
        versions={'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        threads={k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')})
    text = json.dumps(receipt, separators=(',', ':'), allow_nan=False)+'\n'
    core.require(len(text.encode()) < 16384, f'compact receipt size {len(text.encode())} exceeds limit')
    a.output.write_text(text)
    print(json.dumps({'stage': 'complete', 'bytes': len(text.encode()),
                      'output': str(a.output), 'gate': receipt.get('gate')}), flush=True)





def run_constrained(a):
    import pdpr_collect as collector
    from types import SimpleNamespace
    began, wall = time.process_time(), time.perf_counter()
    metadata = {'started_utc': datetime.now(timezone.utc).isoformat(),
                'command': sys.argv, 'seeds': {'training': '2026111010+n',
                    'chebyshev': '2026111520+n', 'uniform': '2026111530+n'},
                'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')}}
    dump(a.scratch/'run-metadata.json', metadata)
    cap = began+600
    sources = [Path(__file__), Path(core.__file__), Path(collector.__file__), Path(core.u.__file__),
               Path(core.old_budget.__file__), Path(old_det.__file__), Path(old_det.prev.__file__),
               Path(old_det.prev.old.__file__), TOP/'code/t4_stacks.py',
               TOP.parents[1]/'tracks/lattice-unisolvence/code/c3_rank.py']
    sourcepins = [core.identity(p) for p in sources]
    for p in sources:
        (a.scratch/('source-'+p.name)).write_bytes(p.read_bytes())
    reference = json.loads(a.reference.read_text())
    for key in ('raw_details', 'raw_inventory'):
        core.require(core.identity(reference[key]['path']) == reference[key], 'P1reference identity mismatch')
    ref_inventory = json.loads(Path(reference['raw_inventory']['path']).read_text())
    for item in ref_inventory:
        core.require(core.identity(item['path']) == item, 'P1raw input identity mismatch')
    prior = json.loads(Path(reference['raw_details']['path']).read_text())
    refraw = Path(reference['raw_details']['path']).parent
    details = {'paths': [], 'assessments': [], 'degrees': [], 'unrun': [],
               'inputs': [core.identity(a.reference), reference['raw_details'], reference['raw_inventory']]}
    for n in (6, 8):
        if time.process_time() >= cap:
            details['unrun'].append({'n': n, 'stage': 'degree'})
            continue
        t, w = time.process_time(), time.perf_counter()
        nodes, _, recipe = core.u.parity_nodes(n)
        generation = {'cpu': time.process_time()-t, 'wall': time.perf_counter()-w}
        dump(a.scratch/f'n{n}-recipe.json', recipe)
        path, snaps = core.constrained_curve(nodes, n, a.scratch, cap)
        path['costs_cpu']['node_generation'] = generation['cpu']
        path['costs_cpu']['complete_construction'] += generation['cpu']
        path['costs_wall']['node_generation'] = generation['wall']
        path['costs_wall']['complete_construction'] += generation['wall']
        details['paths'].append(path)
        print(json.dumps({'stage': 'constrained_path', 'n': n, 'M': path['selected_M'],
                          'stop': path['stop'], 'cpu': path['costs_cpu']['complete_construction'],
                          'failures': path['failures']}), flush=True)
        if time.process_time() >= cap:
            details['unrun'].append({'n': n, 'stage': 'assessment'})
            continue
        # Standard nested meshes; new independent query seeds at same sizes.
        sets = core.heldout(n)
        from scipy.stats import qmc
        sets['chebyshev'] = np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=2026111520+n).random_base2(11))
        sets['uniform'] = 2*qmc.Sobol(3, scramble=True, seed=2026111530+n).random_base2(11)-1
        assessed, aliases = {}, {}
        def assess(name, x, haar=False):
            key = (core.array_sha(x), haar)
            if key in assessed:
                aliases[name] = assessed[key]['name']
                return assessed[key]
            if time.process_time() >= cap:
                details['unrun'].append({'n': n, 'stage': 'assessment', 'name': name})
                return None
            row = core.assess(x, n, len(nodes), sets, name, a.scratch, haar=haar)
            assessed[key] = row
            aliases[name] = name
            details['assessments'].append(row)
            return row
        full = assess('OLS-full', nodes)
        assess('Haar-full', nodes, haar=True)
        m = path['selected_M']
        counts = {k for k in core.checkpoints(n, len(nodes)) if k in snaps} | {m}
        for count in sorted(counts, reverse=True):
            if count in snaps:
                assess(f'L-m{count}', nodes[snaps[count]])
        for rule in core.RULES:
            source = refraw/f'n{n}-{rule}-path.npz'
            details['inputs'].append(core.identity(source))
            with np.load(source, allow_pickle=False) as data:
                if f'm{m}' in data:
                    row = assess(f'{rule}-m{m}', nodes[data[f'm{m}']])
                    if row is not None:
                        oldpath = next(p for p in prior['paths'] if p['n'] == n and p['rule'] == rule)
                        row['historical_P1_path_construction_cpu'] = oldpath['costs_cpu']['complete_construction']
                else:
                    details['unrun'].append({'n': n, 'stage': 'missing mandatory control count', 'rule': rule, 'M': m})
        costs = {}
        if time.process_time() < cap:
            t, w = time.process_time(), time.perf_counter()
            piv = la.qr(old_det.prev.old.basis(nodes, n).T, pivoting=True,
                        mode='economic', check_finite=False)[2]
            costs['restrictedQR'] = {'cpu': time.process_time()-t+generation['cpu'],
                                      'wall': time.perf_counter()-w+generation['wall']}
            for count in sorted(counts, reverse=True):
                assess(f'restrictedQR-m{count}', nodes[piv[:count]])
        else:
            details['unrun'].append({'n': n, 'stage': 'restrictedQR'})
        if time.process_time() < cap:
            t, w = time.process_time(), time.perf_counter()
            qrpoints = old_det.prev.qrpoints(n)
            costs['globalQR'] = {'cpu': time.process_time()-t, 'wall': time.perf_counter()-w}
            assess('globalQR', qrpoints)
            if time.process_time() < cap:
                t, w = time.process_time(), time.perf_counter()
                local, trace = old_det.exchange(qrpoints.copy(), n)
                costs['localdet'] = {'cpu': time.process_time()-t+costs['globalQR']['cpu'],
                                    'wall': time.perf_counter()-w+costs['globalQR']['wall'],
                                    'trace': trace}
                assess('localdet', local)
            else:
                details['unrun'].append({'n': n, 'stage': 'localdet'})
        else:
            details['unrun'].append({'n': n, 'stage': 'globalQR/localdet'})
        byname = {r['name']: r for r in assessed.values()}
        def lookup(name):
            return byname.get(aliases.get(name))
        if full and full['eligible']:
            for row in assessed.values():
                if row['eligible']:
                    row['target_regressions_to_full'] = {}
                    for measure in ('uniform', 'chebyshev'):
                        report = {}
                        for metric in ('rms', 'maximum'):
                            vals = np.array(row['function_errors'][measure][metric])
                            ref = np.array(full['function_errors'][measure][metric])
                            report[metric] = {'worse_count': int(np.sum(vals > 1.01*ref+1e-14)),
                                'worst_ratio_above_floor': float(np.max(vals/np.maximum(ref, 1e-14)))}
                        row['target_regressions_to_full'][measure] = report
        terminal = lookup(f'L-m{m}')
        decision = {'complete': terminal is not None and full is not None,
                    'stop': path['stop'], 'M': m, 'saving': 1-m/len(nodes)}
        if terminal and full and terminal['eligible'] and full['eligible']:
            retained = [lookup(name) for name in aliases if name.startswith('L-m')]
            decision.update(guards=bool(not path['failures'] and retained
                and all(row is not None and row['eligible'] for row in retained)),
                amp_ratio=terminal['amp_union']/full['amp_union'],
                risk_ratio=terminal['integer_risk']/full['integer_risk'], controls={})
            for control in ('random', 'lex'):
                row = lookup(f'{control}-m{m}')
                decision['controls'][control] = ({'risk_ratio': terminal['integer_risk']/row['integer_risk'],
                    'amp_ratio': terminal['amp_union']/row['amp_union']} if row and row['eligible'] else {'unavailable': True})
            decision['control_gain'] = control_gate(decision['controls'])
            decision['quality'] = bool(decision['guards'] and decision['saving'] >= .10
                and decision['amp_ratio'] <= 1.30 and decision['risk_ratio'] <= 1.10)
        details['degrees'].append({'n': n, 'M_start': len(nodes), 'aliases': aliases,
                                  'decisions': {'L': decision}, 'comparator_costs': costs})
        print(json.dumps({'stage': 'constrained_degree', 'n': n, 'decision': decision}), flush=True)
        dump(a.scratch/'partial-details.json', details)
    d = [x['decisions']['L'] for x in details['degrees']]
    passes = (len(d) == 2 and all(x.get('quality', False) for x in d)
              and any(x.get('control_gain', False) for x in d) and not details['unrun']
              and time.process_time()-began <= 600)
    details['gate'] = {'rules': {'L': {'passes': bool(passes)}},
                       'selected_rule': 'L' if passes else None, 'passes': bool(passes)}
    details['timing'] = {'actual_cpu': time.process_time()-began, 'wall': time.perf_counter()-wall,
                         'allowance_cpu': 600}
    core.require(sourcepins == [core.identity(p) for p in sources], 'P2executed source changed')
    metadata['ended_utc'] = datetime.now(timezone.utc).isoformat()
    dump(a.scratch/'run-metadata.json', metadata)
    dump(a.scratch/'details.json', details)
    dump(a.scratch/'inventory.json', [core.identity(p) for p in sorted(a.scratch.rglob('*')) if p.is_file()])
    collector.collect(SimpleNamespace(scratch=a.scratch, protocol_commit=a.protocol_commit,
        output=a.output, original_command=None, round='P2'))





def frontier_assess(nodes, n, budget, sets, name, raw, cap, haar=False):
    began, wall = time.process_time(), time.perf_counter()
    row = core.assess(nodes, n, budget, sets, name, raw, haar=haar)
    if not row['eligible']:
        return row
    if time.process_time() >= cap:
        row['assessment_incomplete'] = 'cap_before_refinement'
        return row
    with np.load(raw/f'n{n}-{name}-map.npz', allow_pickle=False) as data:
        C = data['operator']
    scale = np.array([2.**(sum(v > 0 for v in alpha)/2) for alpha in core.u.exponents(n)])
    starts = [np.arccos(np.clip(x, -1, 1)) for x in row['mesh41_largest_points']]
    starts.extend(np.array(list(__import__('itertools').product((0., np.pi), repeat=3))))
    starts.extend(np.pi*np.random.default_rng(2026111940+n).random((16, 3)))
    t = time.process_time()
    (value, where), searches = old_det.refine(scale[:, None]*C, n, starts)
    row['amp']['local_search'] = float(value)
    row['amp_union'] = max(row['amp'].values())
    row['refinement'] = {'starts': len(searches), 'successes': sum(s['success'] for s in searches),
                         'cpu': time.process_time()-t, 'angular_arg': np.asarray(where).tolist()}
    dump(raw/f'n{n}-{name}-searches.json', searches)
    # Direct application cost is separate from factorization/validation/search.
    Y = core.old_budget.targets(nodes)
    samples = []
    for _ in range(5):
        t = time.process_time()
        C@Y
        samples.append(time.process_time()-t)
    row['application_12_rhs_median_cpu'] = float(np.median(samples))
    row['assessment_cpu'] = time.process_time()-began
    row['assessment_wall'] = time.perf_counter()-wall
    return row


def target_regressions(rows, full):
    if not full or not full['eligible']:
        return
    for row in rows:
        if row['eligible']:
            row['target_regressions_to_full'] = {}
            for measure in ('uniform', 'chebyshev'):
                report = {}
                for metric in ('rms', 'maximum'):
                    vals = np.array(row['function_errors'][measure][metric])
                    ref = np.array(full['function_errors'][measure][metric])
                    report[metric] = {'worse_count': int(np.sum(vals > 1.01*ref+1e-14)),
                        'worst_ratio_above_floor': float(np.max(vals/np.maximum(ref, 1e-14)))}
                row['target_regressions_to_full'][measure] = report


def run_frontier(a):
    import math
    import itertools
    import pdpr_collect as collector
    from scipy.stats import qmc
    from types import SimpleNamespace
    began, wall = time.process_time(), time.perf_counter()
    cap = began+900
    metadata = {'started_utc': datetime.now(timezone.utc).isoformat(), 'command': sys.argv,
                'seeds': {'chebyshev': '2026111920+n', 'uniform': '2026111930+n',
                          'refinement_angular_starts': '2026111940+n'},
                'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')}}
    dump(a.scratch/'run-metadata.json', metadata)
    sources = [Path(__file__), Path(core.__file__), Path(collector.__file__), Path(core.u.__file__),
        Path(core.old_budget.__file__), Path(old_det.__file__), Path(old_det.prev.__file__),
        Path(old_det.prev.old.__file__), TOP/'code/t4_stacks.py',
        TOP.parents[1]/'tracks/lattice-unisolvence/code/c3_rank.py']
    pins = [core.identity(p) for p in sources]
    for p in sources:
        (a.scratch/('source-'+p.name)).write_bytes(p.read_bytes())
    ref = json.loads(a.reference.read_text())
    for key in ('raw_details', 'raw_inventory'):
        core.require(core.identity(ref[key]['path']) == ref[key], 'P1reference changed')
    refraw = Path(ref['raw_details']['path']).parent
    path8 = refraw/'n8-A-path.npz'
    inv = json.loads(Path(ref['raw_inventory']['path']).read_text())
    expected8 = next(r for r in inv if r['path'] == str(path8))
    core.require(core.identity(path8) == expected8, 'P1n8path input changed')
    stored = TOP/'evidence/u2-degree12-nodes.json'
    details = {'paths': [], 'assessments': [], 'degrees': [], 'unrun': [],
        'inputs': [core.identity(a.reference), ref['raw_details'], ref['raw_inventory'],
                   core.identity(path8), core.identity(stored)]}
    for n in (8, 12):
        if time.process_time() >= cap:
            details['unrun'].append({'n': n, 'stage': 'degree'})
            continue
        t, w = time.process_time(), time.perf_counter()
        nodes, _, recipe = core.u.parity_nodes(n)
        generation = {'cpu': time.process_time()-t, 'wall': time.perf_counter()-w}
        dump(a.scratch/f'n{n}-recipe.json', recipe)
        N, primary = math.comb(n+3, 3), math.ceil(1.20*math.comb(n+3, 3))
        path, snapshots = core.curve(nodes, n, 'A', a.scratch, cap, checkpoint_maps=True)
        path['old_strict_prefix_M'] = path['selected_M']
        path['primary_M'] = primary
        path['costs_cpu']['node_generation'] = generation['cpu']
        path['costs_cpu']['complete_construction'] += generation['cpu']
        path['costs_wall']['node_generation'] = generation['wall']
        path['costs_wall']['complete_construction'] += generation['wall']
        event = next((e for e in path['curve'] if e['M'] == primary), None)
        if event and 'prefix_complete_cpu' in event:
            path['primary_prefix'] = {'M': primary, 'cpu': event['prefix_complete_cpu']+generation['cpu'],
                'wall': event['prefix_complete_wall']+generation['wall'],
                'checkpoint': core.identity(event['prefix_checkpoint'])}
        reproduction = {'required': n == 8, 'passes': n != 8}
        if n == 8:
            with np.load(path8, allow_pickle=False) as old:
                mismatch = [m for m, ids in snapshots.items() if f'm{m}' not in old
                            or not np.array_equal(ids, old[f'm{m}'])]
                reproduction.update(passes=not mismatch and len(snapshots) == len(old.files),
                                    compared_counts=len(snapshots), mismatched_counts=mismatch)
        path['P1_reproduction'] = reproduction
        details['paths'].append(path)
        print(json.dumps({'stage': 'frontier_path', 'n': n, 'primary_M': primary,
            'prefix': path.get('primary_prefix'), 'reproduction': reproduction,
            'failures': path['failures'], 'full_diagnostic_cpu': path['costs_cpu']['complete_construction']}), flush=True)
        sets = core.heldout(n)
        sets['chebyshev'] = np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=2026111920+n).random_base2(11))
        sets['uniform'] = 2*qmc.Sobol(3, scramble=True, seed=2026111930+n).random_base2(11)-1
        assessed, aliases = {}, {}
        def assess(name, x, haar=False):
            key = (core.array_sha(x), haar)
            if key in assessed:
                aliases[name] = assessed[key]['name']
                return assessed[key]
            if time.process_time() >= cap:
                details['unrun'].append({'n': n, 'stage': 'assessment', 'name': name})
                return None
            row = frontier_assess(x, n, len(nodes), sets, name, a.scratch, cap, haar)
            assessed[key] = row
            aliases[name] = name
            details['assessments'].append(row)
            if row.get('assessment_incomplete'):
                details['unrun'].append({'n': n, 'stage': row['assessment_incomplete'], 'name': name})
            print(json.dumps({'stage': 'frontier_assessment', 'n': n, 'name': name,
                              'M': row['M'], 'norm': row.get('amp_union'), 'risk': row.get('integer_risk')}), flush=True)
            return row
        full = assess('OLS-full', nodes)
        assess('Haar-full', nodes, True)
        counts = {len(nodes), primary, math.ceil(1.10*N), N}
        for m in sorted(counts, reverse=True):
            if m in snapshots:
                assess(f'A-m{m}', nodes[snapshots[m]])
            else:
                details['unrun'].append({'n': n, 'stage': 'missing path checkpoint', 'M': m})
        costs = {}
        if time.process_time() < cap:
            t, w = time.process_time(), time.perf_counter()
            piv = la.qr(old_det.prev.old.basis(nodes, n).T, pivoting=True,
                        mode='economic', check_finite=False)[2]
            costs['restrictedQR'] = {'cpu': time.process_time()-t+generation['cpu'],
                                    'wall': time.perf_counter()-w+generation['wall']}
            for m in sorted(counts, reverse=True):
                assess(f'restrictedQR-m{m}', nodes[piv[:m]])
        else:
            details['unrun'].append({'n': n, 'stage': 'restrictedQR construction'})
        if time.process_time() < cap:
            t, w = time.process_time(), time.perf_counter()
            qrnodes = old_det.prev.qrpoints(n)
            costs['globalQR'] = {'cpu': time.process_time()-t, 'wall': time.perf_counter()-w}
            assess('globalQR', qrnodes)
            if time.process_time() < cap:
                t, w = time.process_time(), time.perf_counter()
                local, trace = old_det.exchange(qrnodes.copy(), n)
                costs['localdet'] = {'cpu': time.process_time()-t+costs['globalQR']['cpu'],
                                    'wall': time.perf_counter()-w+costs['globalQR']['wall'], 'trace': trace}
                assess('localdet', local)
            else:
                details['unrun'].append({'n': n, 'stage': 'localdet construction'})
        else:
            details['unrun'].append({'n': n, 'stage': 'globalQR/localdet construction'})
        if n == 12 and time.process_time() < cap:
            t, w = time.process_time(), time.perf_counter()
            record = json.loads(stored.read_text())
            raw = base64.b85decode(record['coordinates_base85'])
            core.require(core.hashlib.sha256(raw).hexdigest() == record['coordinates_sha256'], 'storedU2coordinate hash')
            storednodes = np.frombuffer(raw, dtype='<f8').reshape(record['N'], 3).copy()
            core.require(record['n'] == n and record['N'] == N, 'storedU2degree/count')
            costs['storedU2_load'] = {'cpu': time.process_time()-t, 'wall': time.perf_counter()-w,
                'offline_construction': 'Existing stored455artifact; original optimizer cost in usable2.md, not rerun'}
            assess('storedU2', storednodes)
        elif n == 12:
            details['unrun'].append({'n': n, 'stage': 'storedU2'})
        target_regressions(assessed.values(), full)
        byname = {r['name']: r for r in assessed.values()}
        def lookup(name):
            return byname.get(aliases.get(name))
        candidate, restricted = lookup(f'A-m{primary}'), lookup(f'restrictedQR-m{primary}')
        decision = {'M': primary, 'site_saving': 1-primary/len(nodes),
                    'reproduction': reproduction['passes'], 'complete': candidate is not None and restricted is not None,
                    'prefix_cpu': path.get('primary_prefix', {}).get('cpu')}
        if candidate and restricted and candidate['eligible'] and restricted['eligible']:
            required_names = ['globalQR', 'localdet']+(['storedU2'] if n == 12 else [])
            controls = {k: lookup(k) for k in required_names}
            valid_controls = all(r is not None and r['eligible'] for r in controls.values())
            dominance = {name: bool(row['integer_risk'] <= candidate['integer_risk']*(1+1e-10)
                and row['amp_union'] <= candidate['amp_union']*(1+1e-10))
                for name, row in controls.items() if row is not None and row['eligible']}
            ratios = {'risk': candidate['integer_risk']/restricted['integer_risk'],
                      'amp': candidate['amp_union']/restricted['amp_union']}
            decision.update(guards=bool(not path['failures'] and all(r['eligible'] for r in assessed.values())),
                restricted_ratios=ratios, minimum_count_dominates=dominance,
                nondominated=valid_controls and not any(dominance.values()),
                old_full_grid_ratios={'risk': candidate['integer_risk']/full['integer_risk'],
                                      'amp': candidate['amp_union']/full['amp_union']})
            decision['passes'] = bool(decision['guards'] and decision['reproduction']
                and decision['site_saving'] >= .10 and decision['prefix_cpu'] is not None
                and decision['prefix_cpu'] <= 120 and ratios['risk'] <= .95 and ratios['amp'] <= .95
                and decision['nondominated'])
        details['degrees'].append({'n': n, 'M_start': len(nodes), 'aliases': aliases,
                                   'decisions': {'A': decision}, 'comparator_costs': costs})
        print(json.dumps({'stage': 'frontier_degree', 'n': n, 'decision': decision}), flush=True)
        dump(a.scratch/'partial-details.json', details)
    ds = [r['decisions']['A'] for r in details['degrees']]
    passes = len(ds) == 2 and all(r.get('passes', False) for r in ds) and not details['unrun'] and time.process_time()-began <= 900
    details['gate'] = {'rules': {'A': {'passes': bool(passes)}},
                       'selected_rule': 'A' if passes else None, 'passes': bool(passes)}
    details['timing'] = {'actual_cpu': time.process_time()-began, 'wall': time.perf_counter()-wall, 'allowance_cpu': 900}
    core.require(pins == [core.identity(p) for p in sources], 'P3executed sources changed')
    metadata['ended_utc'] = datetime.now(timezone.utc).isoformat()
    dump(a.scratch/'run-metadata.json', metadata)
    dump(a.scratch/'details.json', details)
    dump(a.scratch/'inventory.json', [core.identity(p) for p in sorted(a.scratch.rglob('*')) if p.is_file()])
    collector.collect(SimpleNamespace(scratch=a.scratch, protocol_commit=a.protocol_commit,
        output=a.output, original_command=None, round='P3'))


if __name__ == '__main__':
    main()
