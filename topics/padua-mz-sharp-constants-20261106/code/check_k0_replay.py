#!/usr/bin/env python3
"""Independent K0 execution: fixed finite scope, no fit or proof claim."""
import argparse
import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time

import mpmath as mp
import numpy as np
import scipy
from scipy.sparse.linalg import eigsh

ROOT = Path(__file__).resolve().parents[3]
TOPIC = 'topics/padua-mz-sharp-constants-20261106/'
PIN = '2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861'
EXPECTED = {
    TOPIC+'code/S4_k0_replay.py': '707d8d925d34c09846ac454a7482be2efc8563b33dd0e5e9ad2a16842d605285',
    'topics/mz-constants/sources/padua_mz_inputs/code/cc_mz_large.py': 'df392b043fad81395ce6e07258a438bbd5fc609fc83fc51fa03314b885ac5af9',
    'tracks/mz-constants/code/mz2d_spectra.py': '623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76',
    'topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py': 'f246b7a436fa9e6133153a87fd5af887d80f6fb0ab12dc2208fbd9ade223c241',
    'topics/padua-mz-2d-frontier-20261105/evidence/g1-minimum-only.json': '82ada412cd2886c6c569431bbb77bf4d786f96bfc8190554d5fe2e8b95d12b00',
    TOPIC+'evidence/S4-k0-cc.json': '5a2eae3b33636c71e2296d1cf5ccac9e8cb46fef42c044bf3933da7428f7638d',
    TOPIC+'evidence/S4-k0-padua.json': 'aa22868fa079ec8b5760a06a35f1ed9657ab9cfd535c69e18bd08774b74bbf9f',
    TOPIC+'evidence/S4-k0-carrier.json': 'f925c919725dbbd3fb57097bd3a58c03687e655725d633c71af00b7d4d1e157c',
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    tick = time.monotonic()
    for path, expected in EXPECTED.items():
        if digest(ROOT/path) != expected:
            raise RuntimeError('Input hash mismatch: '+path)
    report = {
        'status': 'MEASURED', 'rigorous_enclosures': False,
        'role': 'independent supplementary checker',
        'requested_model': 'gpt-6-astra high; runtime model/effort metadata unexposed',
        'source_and_rules_pin': PIN,
        'command': [sys.executable]+sys.argv,
        'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'python': sys.version, 'numpy': np.__version__, 'scipy': scipy.__version__,
        'mpmath': mp.__version__, 'platform': platform.platform(),
        'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        'checker_sha256': digest(__file__), 'input_sha256': EXPECTED,
        'independence': 'Separately executed; same imported numerical algorithms; changed Padua seed and 90-digit carrier moment evaluation.',
        'seed': 20261106, 'tolerance': 2e-11, 'ncv': 40, 'maxiter': 20000,
        'cc': [], 'carrier': [], 'padua': [],
    }

    def save():
        report['seconds'] = time.monotonic()-tick
        report['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')

    replay = load_module(TOPIC+'code/S4_k0_replay.py', 'independent_k0')
    cc = load_module(replay.SOURCES[0], 'independent_cc')
    cc_ref = json.loads((ROOT/(TOPIC+'evidence/S4-k0-cc.json')).read_text())
    for old in cc_ref['results']:
        N = old['N']
        pair = [cc.extremes(N, N-1, parity) for parity in (0, 1)]
        lo, hi = min(p[0] for p in pair), max(p[1] for p in pair)
        err = max(abs(lo/old['reference'][0]-1), abs(hi/old['reference'][1]-1))
        report['cc'].append(dict(N=N, minimum=float(lo), maximum=float(hi),
                                 maximum_relative_error=float(err), pass_1e10=bool(err <= 1e-10)))
    save()
    mp.mp.dps = 90
    carrier_ref = json.loads((ROOT/(TOPIC+'evidence/S4-k0-carrier.json')).read_text())
    limit = mp.mpf(carrier_ref['limit'])
    for m in (512, 1024, 2048, 4096):
        r, s, h = m//4, m//5, m//2
        # This pre-computation bound checks int64 safety before convolution.
        bound = max((2*r+1)*(r+1)**2, (2*s+1)*(s+1)**2)
        assert bound < 2**63
        mass = replay.finite_mass(r, h)*replay.finite_mass(s)
        quad = replay.quad_mass(r, h)*replay.quad_mass(s)
        old = next(v for v in carrier_ref['results'] if v['m'] == m)
        err = float(abs(mp.mpf(quad)/mass-1))
        report['carrier'].append(dict(m=m, finite_norm_squared_90digit=mp.nstr(mass, 65),
            gauss_norm_squared=quad, quadrature_relative_error=err,
            developer_norm_relative_difference=float(abs(mass/mp.mpf(old['finite_norm_squared_75digit'])-1)),
            relative_difference_from_limit=float(mass/limit-1),
            int64_preconvolution_bound=bound, pass_1e10=bool(err <= 1e-10)))
    save()
    padua = load_module(replay.SOURCES[2], 'independent_padua')
    reference = json.loads((ROOT/replay.SOURCES[3]).read_text())
    for m in (800, 1000):
        start = time.monotonic()
        op = padua.PaduaOperator(m, m-1)
        rng = np.random.default_rng(report['seed'])
        _, vecs = eigsh(op, k=1, which='SA', v0=rng.standard_normal(op.shape[0]),
                        tol=report['tolerance'], ncv=report['ncv'], maxiter=report['maxiter'])
        vec = vecs[:, 0]
        vec /= np.linalg.norm(vec)
        av = op@vec
        value = float(vec@av)
        old = next(v for v in reference['results'] if v['m'] == m)['minimum']
        err = abs(value/old-1)
        row = dict(m=m, n=m-1, dimension=op.shape[0], minimum=value, reference=old,
                   relative_error=err, pass_1e10=bool(err <= 1e-10),
                   residual_2_float=float(np.linalg.norm(av-value*vec)),
                   matvecs=op.calls, seconds=time.monotonic()-start)
        report['padua'].append(row)
        save()
        print(json.dumps(row), flush=True)
    report['all_finite_comparisons_pass'] = all(row['pass_1e10'] for key in ('cc','carrier','padua') for row in report[key])
    report['inputs_unchanged_at_end'] = all(digest(ROOT/p) == h for p,h in EXPECTED.items())
    save()
    if not report['all_finite_comparisons_pass'] or not report['inputs_unchanged_at_end']:
        raise RuntimeError('Check failed; see output receipt')


if __name__ == '__main__':
    main()
