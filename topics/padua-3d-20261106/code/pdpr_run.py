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
    return {'synthetic_deletions': checks, 'integer_allocations': allocation_checks,
            'control_gate_branch_cases': branch_cases, 'tie_branch_cases': tie_cases,
            'all_degree_gate_cases': numerical_cases, 'passes': True}


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
    p.add_argument('--round', choices=('pilot', 'engineering'), required=True)
    p.add_argument('--protocol-commit')
    p.add_argument('--scratch', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=False)
    started = datetime.now(timezone.utc).isoformat()
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


if __name__ == '__main__':
    main()
