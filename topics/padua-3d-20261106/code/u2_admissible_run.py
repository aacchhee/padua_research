#!/usr/bin/env python3
"""R2 admissible projected-gradient pilot/holdout; preserves the R1 runner."""
import argparse
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy

import u2_core as core
import u2_admissible as update

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]
PROTOCOL = '86b9e26920272bcb6a9a55b3eaf2d41bd63d2d58'


def compact(value):
    if isinstance(value, float):
        return float(format(value, '.9g'))
    if isinstance(value, list):
        return [compact(x) for x in value]
    if isinstance(value, dict):
        return {k: compact(v) for k, v in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--degrees', nargs='+', type=int, required=True)
    parser.add_argument('--scratch', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.scratch.exists():
        raise RuntimeError('scratch must be a new unique directory')
    args.scratch.mkdir(parents=True)
    sources = [Path(__file__), Path(update.__file__), Path(core.__file__), Path(core.inherited.__file__),
               Path(core.inherited.prev.__file__), Path(core.old.__file__),
               ROOT/'tracks/lattice-unisolvence/code/c3_rank.py', TOP/'code/t4_stacks.py']
    inputs = [TOP/'evidence/t9-r06-qr.json', TOP/'evidence/t9-r06-localdet.json']
    receipt = {'schema': 'u2-admissible-norm-v1', 'status': 'MEASURED lower samples; exact dyadic ranks reported separately',
               'rules_input': '38227202bc6908d5a5a874950145761a8ca4312f',
               'protocol_commit': PROTOCOL, 'command': sys.argv, 'scratch': str(args.scratch),
               'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
               'sources': {str(p.relative_to(ROOT)): core.sha(p) for p in sources},
               'inputs': {str(p.relative_to(ROOT)): core.sha(p) for p in inputs},
               'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')},
               'assessment_seeds': [2026110702, 2026110703], 'requested_degrees': args.degrees,
               'columns': {'conditioning': ['unscaled_kappa2', 'orthonormal_kappa2', 'inverse_residual_inf', 'logabsdet'],
                           'norms': ['train21', 'lobatto41', 'gauss32', 'sobol8192', 'corners', 'fresh_refined'],
                           'errors': ['maxabs', 'rms'],
                           'functions': ['exp(x+y+z)', '1/(1+5r^2)', 'abs(x+y+z)/3', 'cos(3x+2y-z)'],
                           'noise': ['maxabs16trials', 'rms_pooled', 'row_l1_max']},
               'rows': [], 'optimizations': [], 'calibration': [], 'unrun': []}

    def save():
        columns = ['n', 'family', 'N', 'unique', 'eligible', 'conditioning', 'norms',
                   'errors', 'noise', 'refinement_success', 'node_sha256', 'dyadic_ranks',
                   'construction_cpu', 'assessment_cpu']
        packed = dict(receipt)
        packed['row_columns'] = columns
        packed['rows'] = [[row.get(k) for k in columns] for row in receipt['rows']]
        payload = json.dumps(compact(packed), separators=(',', ':'), allow_nan=False)+'\n'
        if len(payload.encode()) >= 16384:
            (args.scratch/'failed-oversize-receipt.json').write_text(payload)
            raise RuntimeError('receipt exceeds 16KiB; preserve raw full output before changing summary')
        args.output.write_text(payload)

    old_qr = json.loads(inputs[0].read_text())['rows']
    old_det = json.loads(inputs[1].read_text())['rows']
    train = np.cos(core.inherited.prev.angular_mesh(21))
    began = time.process_time()
    for index, n in enumerate(args.degrees):
        started = time.process_time()
        qr = core.inherited.prev.qrpoints(n)
        qr_cpu = time.process_time()-started
        started = time.process_time()
        localdet, determinant_trace = core.inherited.exchange(qr.copy(), n)
        det_extra = time.process_time()-started
        started = time.process_time()
        leja = core.inherited.prev.points(n, 'leja')
        leja_cpu = time.process_time()-started
        E = core.old.basis(train, n)
        if n == 2:
            check = core.gradient_check(localdet, n, E)
            receipt['gradient_check'] = check
            (args.scratch/'gradient-check.json').write_text(json.dumps(check)+'\n')
            if check['max_relative_error'] > 1e-4:
                receipt['unrun'] = args.degrees[index:]
                receipt['blocked'] = 'gradient check failed; no candidate optimization executed'
                save()
                return
        candidate, trace = update.optimize(localdet, n, E, args.scratch)
        V = core.old.basis(candidate, n)
        inverse = np.linalg.inv(V)
        if np.linalg.cond(V) >= 1e12 or np.linalg.norm(V@inverse-np.eye(len(V)), np.inf) > 1e-7:
            trace['guard_fallback'] = True
            candidate = localdet.copy()
        else:
            trace['guard_fallback'] = False
        trace.update(n=n, determinant_trace=determinant_trace, qr_cpu=qr_cpu,
                     localdet_extra_cpu=det_extra, candidate_total_cpu=qr_cpu+det_extra+trace['extra_cpu'])
        receipt['optimizations'].append(trace)
        for family, nodes, construction_cpu in (
                ('qr', qr, qr_cpu), ('leja', leja, leja_cpu),
                ('localdet', localdet, qr_cpu+det_extra),
                ('joint_norm', candidate, trace['candidate_total_cpu'])):
            assessed = time.process_time()
            row = core.assess(nodes, n, args.scratch, family)
            row.update(n=n, family=family, construction_cpu=construction_cpu,
                       assessment_cpu=time.process_time()-assessed)
            receipt['rows'].append(row)
            if (family == 'qr' and n in (4, 8)) or (family == 'localdet' and n == 2):
                historic = next(r for r in (old_qr if family == 'qr' else old_det) if r['n'] == n)
                calibration_dir = args.scratch/f'calibration-{family}-n{n}'
                calibration_dir.mkdir()
                calibration_started = time.process_time()
                calibrated = core.inherited.measure(n, family, nodes.copy(), calibration_dir, {})
                receipt['calibration'].append({'n': n, 'family': family,
                    'mesh41_delta': calibrated['mesh41']-historic['mesh41'],
                    'historical_refined_delta': calibrated['local']-historic['local'],
                    'fresh_refined_minus_old_refined': row['norms'][5]-historic['local'],
                    'cpu': time.process_time()-calibration_started,
                    'historical_node_sha256_match': row['node_sha256'] == historic['node_sha256']})
            save()
        ratio = {r['family']: r['norms'][5] for r in receipt['rows'] if r['n'] == n}
        print(json.dumps({'n': n, 'fresh_refined': ratio,
                          'joint_over_localdet': ratio['joint_norm']/ratio['localdet'],
                          'optimization': trace}), flush=True)
    eligible = [n for n in args.degrees if n in (6, 8)]
    receipt['pilot_gate'] = {'eligible_degrees': eligible, 'passes': False,
                            'meaning': 'finite operational gate, no asymptotic or supremum claim'}
    if eligible == [6, 8]:
        rows = {(r['n'], r['family']): r for r in receipt['rows']}
        receipt['pilot_gate']['passes'] = all(
            rows[n, 'joint_norm']['eligible'] and
            rows[n, 'joint_norm']['norms'][5] <= .95*rows[n, 'localdet']['norms'][5] and
            next(t for t in receipt['optimizations'] if t['n'] == n)['extra_cpu'] < 120
            for n in eligible)
    receipt['cpu_total'] = time.process_time()-began
    full = args.scratch/'full-results.json'
    full.write_text(json.dumps(receipt, separators=(',', ':'), allow_nan=False)+'\n')
    inventory = [{'name': str(p.relative_to(args.scratch)), 'bytes': p.stat().st_size, 'sha256': core.sha(p)}
                 for p in sorted(args.scratch.rglob('*')) if p.is_file()]
    manifest = args.scratch/'raw-inventory.json'
    manifest.write_text(json.dumps(inventory, separators=(',', ':'))+'\n')
    receipt['raw_inventory'] = {'path': str(manifest), 'bytes': manifest.stat().st_size, 'sha256': core.sha(manifest)}
    save()


if __name__ == '__main__':
    main()
