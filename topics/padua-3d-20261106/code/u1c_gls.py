#!/usr/bin/env python3
"""Known GLS refit after frozen B637 integer schedules; all outputs MEASURED."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import time
import numpy as np
import scipy
from scipy import linalg as la
import u1_usable as u
import u1c_budget as b

SEEDS = (2026110713, 2026110714)


def main(a):
    assert not a.out.exists()
    a.raw.mkdir(parents=True, exist_ok=False)
    prior = json.loads(a.prior.read_text())
    oldraw = Path(prior['raw']['directory'])
    assert b.identity(oldraw/'inventory.json') == prior['raw']['inventory']
    inventory = json.loads((oldraw/'inventory.json').read_text())
    assert all(b.identity(p['path']) == p for p in inventory), 'prior raw input differs'
    oldrows = json.loads((oldraw/'all-rows.json').read_text())
    assert len(oldrows) == 38 and all(r['eligible'] for r in oldrows)
    assert not prior['whole_run_cap_hit']
    sources = [Path(__file__), Path(b.__file__), Path(u.__file__),
               u.TRACK/'c3_lebesgue.py', u.TRACK/'c3_rank.py', a.prior,
               oldraw/'inventory.json']
    pins = [b.identity(p) for p in sources]
    for p in sources[:5]: shutil.copyfile(p, a.raw/p.name)
    b.dump(a.raw/'prior-input-inventory.json', inventory)
    cpu0, wall0 = time.process_time(), time.perf_counter()
    rows, coefs, newrows = [], [], []
    olddata = []
    for old in oldrows:
        data = dict(np.load(oldraw/f"{old['name']}-n{old['n']}.npz"))
        olddata.append(data)
        row = {k: v for k, v in old.items() if k != 'bias_squared'}
        rows.append(row); coefs.append(data['coefficients'])
    cap = False
    for idx, old in enumerate(oldrows):
        if old['name'] not in ('Haar', 'OLS'): continue
        start = time.process_time()
        data = olddata[idx]
        n, M, N = old['n'], old['M'], old['N']
        r, Cold, x = data['integer_replicates'], data['operator'], data['nodes']
        assert int(r.sum()) == b.BUDGET and int(r.min()) >= 1
        V = u.basis(x, n)
        root = np.sqrt(r)
        Q, R = la.qr(root[:, None]*V, mode='economic', check_finite=False)
        C = la.solve_triangular(R, Q.T*root[None, :], check_finite=False)
        D = Cold-C
        residual = float(la.norm(C @ V-np.eye(N), np.inf))
        covariance = (Cold/r) @ Cold.T-(C/r) @ C.T-(D/r) @ D.T
        covariance_residual = float(la.norm(covariance, np.inf))
        oldrisk = float(np.sum(Cold*Cold/r))
        risk = float(np.sum(C*C/r))
        cpu = time.process_time()-start
        eligible = bool(residual <= 1e-9 and covariance_residual <= 1e-9
                        and risk <= oldrisk+1e-10 and np.isfinite(C).all() and cpu <= 120)
        row = {'name': 'GLSafter'+old['name'], 'n': n, 'M': M, 'N': N,
               'eligible': eligible, 'parent_index': idx,
               'reproduction_inf': residual, 'covariance_identity_inf': covariance_residual,
               'old_risk': oldrisk, 'risk': risk,
               'relative_risk_gain': 1-risk/oldrisk,
               'construction_cpu_seconds': cpu, 'dense_operator_bytes': C.nbytes}
        if eligible:
            coef = C @ b.targets(x)
            np.savez(a.raw/f"{row['name']}-n{n}.npz", nodes=x, operator=C,
                     integer_replicates=r, coefficients=coef)
        else:
            coef = None
            row['disposition'] = 'ineligible, no repair or quality'
        rows.append(row); coefs.append(coef); newrows.append(row)
        print(json.dumps({k: row[k] for k in ('name','n','eligible','relative_risk_gain')}), flush=True)
        if time.process_time()-cpu0 > 600:
            cap = True; break
    construction_cpu = time.process_time()-cpu0
    outcome = None
    if not cap:
        b.SEEDS = SEEDS
        bias = b.assess(rows, coefs, a.raw, cpu0)
        if bias is None:
            cap = True
        else:
            risk = np.array([r['risk'] for r in rows])
            valid = np.array([r['eligible'] for r in rows])
            total = bias[:, :, :, None] + risk[:, None, None, None]*b.SIGMAS[None,None,None,:]**2
            total[~valid] = np.inf
            baseline_min = np.min(total[:38], axis=0)
            baseline_winners = np.argmin(total[:38], axis=0)
            minimum = np.min(total, axis=0)
            winners = np.argmin(total, axis=0)
            gain = 1-minimum/baseline_min
            regret = np.array([[total[winners[0,t,s],1,t,s]/max(minimum[1,t,s],1e-30)-1
                                for s in range(len(b.SIGMAS))] for t in range(len(b.TARGETS))])
            primary, secondary = 5, 7
            gate = bool(max(np.max(gain[1,primary]), np.max(gain[1,secondary])) >= .05
                        and np.max(regret[[primary,secondary]]) <= .05)
            # Parent-map error regressions are retained even if envelope improves.
            worst_parent_increase = np.zeros((2, len(b.TARGETS)))
            best_parent_gain = np.zeros((2, len(b.TARGETS)))
            for k, row in enumerate(newrows):
                if not row['eligible']: continue
                parent = row['parent_index']
                relative = (total[38+k]-total[parent])/np.maximum(total[parent], 1e-24)
                worst_parent_increase = np.maximum(worst_parent_increase, np.max(relative, axis=2))
                best_parent_gain = np.maximum(best_parent_gain, np.max(-relative, axis=2))
            outcome = {'baseline_minimum_mse': baseline_min.tolist(),
                'baseline_winners': baseline_winners.tolist(), 'winners': winners.tolist(),
                'primary_gain_second_cloud': gain[1,primary].tolist(),
                'secondary_gain_second_cloud': gain[1,secondary].tolist(),
                'gain_max_second_cloud_by_target': np.max(gain[1], axis=1).tolist(),
                'regret_max_second_cloud_by_target': np.max(regret, axis=1).tolist(),
                'worst_parent_relative_mse_increase': worst_parent_increase.tolist(),
                'best_parent_relative_mse_gain': best_parent_gain.tolist(),
                'practical_gate': gate}
            b.dump(a.raw/'decisions.json', {**outcome, 'all_bias_squared': bias.tolist(),
                'all_total_mse': [total[i].tolist() if valid[i] else None for i in range(len(rows))],
                'all_envelope_gain': gain.tolist(), 'all_second_cloud_regrets': regret.tolist()})
    b.dump(a.raw/'all-rows.json', rows)
    assert pins == [b.identity(p) for p in sources]
    assert all(b.identity(p['path']) == p for p in inventory), 'prior input changed during run'
    b.dump(a.raw/'inventory.json', [b.identity(p) for p in sorted(a.raw.iterdir())])
    columns = ['name','n','M','N','eligible','parent_index','reproduction_inf','covariance_identity_inf',
               'risk','relative_risk_gain','construction_cpu_seconds','bias_squared']
    receipt = {'status': 'MEASURED developer GLS operational extension, not independent audit',
        'protocol_commit': a.protocol_commit, 'input_receipt': b.identity(a.prior),
        'command': sys.argv, 'executed_utc': datetime.now(timezone.utc).isoformat(),
        'sources': pins, 'seeds': list(SEEDS), 'assessment_count_each': 32768,
        'sigma': b.SIGMAS.tolist(), 'targets_reference': 'input_receipt targets, identical order',
        'baseline_count': 38, 'new_variant_count': len(newrows),
        'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        'construction_cpu_seconds': construction_cpu,
        'total_cpu_seconds': time.process_time()-cpu0, 'total_wall_seconds': time.perf_counter()-wall0,
        'timing_scope': 'Descriptive process-CPU; concurrent untimed workers permitted; no matched-cost claim',
        'whole_run_cap_hit': cap, 'assessment_finished': outcome is not None,
        'columns': columns, 'new_rows': [[r.get(k) for k in columns] for r in newrows],
        'outcome': outcome, 'raw': {'directory': str(a.raw),
            'results': b.identity(a.raw/'all-rows.json'), 'inventory': b.identity(a.raw/'inventory.json'),
            'policy': 'regenerate-only; original full fresh rows and all MSE values retained; no archival delivery'}}
    payload = json.dumps(b.compact(receipt), separators=(',', ':'), allow_nan=False)+'\n'
    assert len(payload.encode()) < 16384, f'receipt {len(payload.encode())} bytes exceeds limit; no splitting'
    a.out.write_text(payload)
    print(json.dumps({'receipt_bytes': len(payload.encode()), 'eligible_new': sum(r['eligible'] for r in newrows),
        'practical_gate': (outcome or {}).get('practical_gate'), 'cpu_seconds': receipt['total_cpu_seconds']}))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prior', type=Path, required=True)
    p.add_argument('--raw', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--protocol-commit', required=True)
    main(p.parse_args())
