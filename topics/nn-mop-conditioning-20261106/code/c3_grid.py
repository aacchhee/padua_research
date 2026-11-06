#!/usr/bin/env python3
"""Frozen C3 grid: MEASURED field errors, never a stability theorem.

Reuse native_mixed.compute(method='lu') and the predecessor C4 140/220-dps
references and errors function. The denominator is the displayed seven-digit
PD-T434 NN/mixed condition number, not a newly evaluated condition number.
"""
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import platform
import sys
import time
import warnings

import mpmath as mp
import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[3]
PRE = ROOT / 'topics/nn-mop-stability-20261105'
NATIVE = PRE / 'code/native_mixed.py'
TABLE = PRE / 'attempts/D1.md'
SIZES = list(range(4, 33))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_native():
    spec = importlib.util.spec_from_file_location('frozen_native_c3', NATIVE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def table_values():
    # Read column headers as a guard against swapping family columns.
    lines = TABLE.read_text().splitlines()
    assert '| N | NN Krawtchouk | NN Hahn | SL Krawtchouk | SL Hahn |' in lines
    data = {}
    for line in lines:
        parts = [q.strip() for q in line.split('|')]
        if len(parts) == 7 and parts[1].isdigit():
            n = int(parts[1])
            if n in SIZES:
                assert n not in data
                data[n] = dict(zip(('krawtchouk', 'hahn'), parts[2:4]))
    assert sorted(data) == SIZES
    return data


def coeff_hash(coeff):
    # Canonical serialization fixes the reference identity without a large
    # committed coefficient archive. mp.nstr uses 220 significant digits.
    payload = [[list(nu), [mp.nstr(mp.mpf(row[k]), 220)
                          for k in ('a1', 'a2', 'b1', 'b2')]]
               for nu, row in sorted(coeff.items())]
    return hashlib.sha256(json.dumps(payload, separators=(',', ':')).encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sizes', type=int, nargs='+', default=SIZES)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--raw', type=Path, required=True)
    args = ap.parse_args()
    if len(set(args.sizes)) != len(args.sizes) or any(n not in SIZES for n in args.sizes):
        ap.error('sizes must be distinct integers in 4..32')
    start = time.monotonic()
    native = load_native()
    c4 = native.c4
    kappas = table_values()
    rows, rawrows = [], []
    with mp.workdps(220):
        for family in ('krawtchouk', 'hahn'):
            for N in args.sizes:
                x, w = c4.inputs(N, family)
                ident = json.dumps(dict(nodes=list(map(str, x)),
                    weights=[list(map(str, r)) for r in w]), sort_keys=True)
                row = dict(N=N, family=family,
                    input_sha256=hashlib.sha256(ident.encode()).hexdigest(),
                    kappa_display=kappas[N][family])
                kappa_u = mp.mpf(kappas[N][family]) * mp.mpf(2)**-53
                row['kappa_u'] = float(kappa_u)
                row['first_order_informative'] = bool(kappa_u < 1)
                rawrow = dict(N=N, family=family)
                try:
                    ref, _ = c4.compute(N, family, 220)
                    lower, _ = c4.compute(N, family, 140)
                    conv, _ = c4.errors(lower, ref)
                    row.update(reference_agreement=float(conv),
                               reference_sha256=coeff_hash(ref))
                    if not mp.isfinite(conv) or conv >= mp.mpf('1e-60'):
                        raise ArithmeticError('140/220-dps agreement failed')
                    if N == 4:
                        check = c4.exact_check(N, family, ref)
                        row['exact_N4_check'] = check
                        if not check['passed']:
                            raise ArithmeticError('exact N4 reference check failed')
                    for name, solver in [('A-LU', lambda: native.compute(N, family, 'lu')),
                                         ('C4', lambda: c4.compute(N, family)),
                                         ('A-QR', lambda: native.compute(N, family, 'qr')),
                                         ('B-nodeqr', lambda: native.compute(N, family, 'nodeqr'))]:
                        try:
                            with warnings.catch_warnings(record=True) as caught:
                                warnings.simplefilter('always')
                                got, diag = solver()
                            E, fields = c4.errors(got, ref)
                            if not mp.isfinite(E):
                                raise ArithmeticError('nonfinite field error')
                            row[name] = dict(status='completed', E=float(E),
                                E_over_kappa_u=float(E / kappa_u), fields=fields,
                                warnings=[str(z.message) for z in caught], **diag)
                            rawrow[name] = dict(coefficient_sha256=coeff_hash(got),
                                coefficients=[[list(nu), r] for nu, r in sorted(got.items())])
                        except (ArithmeticError, ValueError, np.linalg.LinAlgError) as exc:
                            row[name] = dict(status='breakdown', reason=str(exc))
                except (ArithmeticError, ValueError, np.linalg.LinAlgError) as exc:
                    row['reference_failure'] = str(exc)
                rows.append(row)
                rawrow['measurement'] = row
                rawrows.append(rawrow)
                print(f"{family} N={N}: " + ', '.join(
                    f"{z} {row.get(z, {}).get('status', 'not-run')}" for z in ('A-LU', 'C4', 'A-QR', 'B-nodeqr')),
                    file=sys.stderr, flush=True)
    # Raw floats are the actual binary64 coefficients; JSON's round-trip decimal
    # representation preserves those values. Reference identity is a digest only.
    config = io.StringIO()
    with contextlib.redirect_stdout(config):
        np.show_config()
    args.raw.write_text(json.dumps(dict(cases=rawrows, numpy_build_config=config.getvalue()), sort_keys=True, allow_nan=False))
    compact = []
    def short(value):
        return float(format(value, '.9g'))
    for row in rows:
        q = dict(N=row['N'], family=row['family'], kappa=row['kappa_display'])
        for key, ekey, rkey in [('A-LU','E','ratio'), ('C4','c4E','c4ratio')]:
            z = row.get(key, {})
            if z.get('status') == 'completed':
                q[ekey], q[rkey] = short(z['E']), short(z['E_over_kappa_u'])
            else:
                q[key] = z
        q['lu_warnings'] = row.get('A-LU', {}).get('lu_ill_conditioning_warnings')
        if 'reference_failure' in row:
            q['reference_failure'] = row['reference_failure']
        compact.append(q)
    result = dict(status='MEASURED frozen finite grid; no stability theorem',
        rules_sha='b4a04981d42c7cd872957facf5e3995e4096ca67',
        platform=platform.platform(), machine=platform.machine(),
        python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
        mpmath=mp.__version__, float_mantissa_bits=sys.float_info.mant_dig,
        u='2^-53', argv=sys.argv[1:], elapsed_seconds=time.monotonic()-start,
        thread_environment={k: os.environ.get(k) for k in
            ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')},
        blas_config_location='raw.numpy_build_config',
        producer_sha256=sha(Path(__file__)), native_sha256=sha(NATIVE),
        baseline_sha256=sha(native.BASE), table_source=str(TABLE.relative_to(ROOT)),
        table_values_sha256=hashlib.sha256(json.dumps(kappas, sort_keys=True).encode()).hexdigest(),
        exact_checker_sha256=sha(ROOT / 'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py'),
        denominator='PD-T434 committed NN/mixed table rounded to seven significant digits',
        metric='max over a1,a2,b1,b2 of sup absolute error / reference field sup; structural zeros included',
        reference='same frozen C4 graph at 220 dps; compare 140 dps <1e-60; N4 exact Fraction moment check',
        reference_digest='sorted sites, fields a1,a2,b1,b2, mp.nstr(value,220), compact JSON SHA256',
        limitations=['Rounded kappa introduces about 5e-7 relative uncertainty in ratios.',
            'Reference precision agreement is not an interval certificate or independent algorithm.',
            'Large kappa*u makes ratio alone uninformative; no constant C or theorem inferred.',
            'A-LU counts its caught LinAlgWarning internally; count is retained separately.',
            'No timing comparison; platform/BLAS dependent; raw temporary archive is regenerable.'],
        reference_max_agreement=max(r.get('reference_agreement', 0) for r in rows),
        exact_N4_checks={r['family']:r['exact_N4_check'] for r in rows if 'exact_N4_check' in r},
        extra_methods={key: dict(
            completed=sum(r.get(key, {}).get('status') == 'completed' for r in rows),
            max_ratio=max((r[key]['E_over_kappa_u'] for r in rows if r.get(key, {}).get('status') == 'completed'), default=None),
            breakdowns=[dict(N=r['N'], family=r['family'], detail=r.get(key, {})) for r in rows if r.get(key, {}).get('status') != 'completed'])
            for key in ('A-QR', 'B-nodeqr')},
        summary_precision='E and ratios rounded to nine significant digits; full precision and diagnostics in raw.cases[].measurement',
        raw=dict(path=str(args.raw), bytes=args.raw.stat().st_size, sha256=sha(args.raw)), cases=compact)
    args.output.write_text(json.dumps(result, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n')
    assert args.output.stat().st_size < 16384, 'summary exceeds evidence size limit'
    print(json.dumps(dict(output=str(args.output), bytes=args.output.stat().st_size,
                          sha256=sha(args.output))))


if __name__ == '__main__':
    main()
