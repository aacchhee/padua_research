#!/usr/bin/env python3
"""Freeze fixed-configuration projection inputs and witnesses for audit M3.

This writes a new reference run, not a recovery of missing historical /tmp
bytes. It never selects/re-tunes sizes, methods, precision or optimizer rules.
Third-party source is not used. The checker reads the committed data without
regenerating its own comparison target.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import backward_projection as dev

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def build():
    rows = []
    for family in ('krawtchouk', 'hahn'):
        for N in (4, 8):
            for method in ('c4', 'lu', 'nodeqr'):
                raw, _ = dev.c4.compute(N, family) if method == 'c4' else dev.native.compute(N, family, method)
                fit = dev.fit(raw, N, family, dps=160)
                stored = [dict(nu=list(nu), **{f: float(raw[nu][f]).hex() for f in dev.FIELDS})
                          for nu in sorted(raw)]
                metrics = {k: fit[k] for k in ('input_mixed_sup', 'input_in_units_u',
                    'full_coefficient_correction', 'correction_in_units_u', 'coefficient_SPD_norm',
                    'returned_witness_scaled_stationarity', 'returned_witness_stationarity_dps',
                    'exact_normality_systems_checked', 'fields')}
                rows.append(dict(N=N, family=family, method=method, raw_coefficients=stored,
                    raw_sha256=digest(stored), rational_input=fit['rational_input'],
                    rational_input_sha256=fit['rational_input_sha256'], metrics=metrics))
    paths = [Path(__file__), HERE/'backward_projection.py', HERE/'conditioning.py',
             HERE/'native_mixed.py', HERE/'backward_joint.py', dev.native.BASE]
    return dict(format='padua-projection-reference-v1', source_commit='4e87fc0a771fc13c6d5791f0f4c2e746e4eb9a71',
        provenance='Fixed-config response run on 2026-11-06. Original Nov5 /tmp witnesses are absent; these bytes are a newly pinned reference, not recovered historic artifacts.',
        platform=dict(python=platform.python_version(), numpy=dev.native.np.__version__,
                      scipy=dev.native.scipy.__version__, mpmath=dev.mp.__version__,
                      system=platform.platform(), machine=platform.machine()),
        source_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        configuration=dict(sizes=[4, 8], families=['krawtchouk', 'hahn'],
                           methods=['c4', 'lu', 'nodeqr'], dps=160, maxiter=10),
        cases=rows, cases_sha256=digest(rows))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError('Refusing to replace an existing reference: ' + str(args.output))
    result = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(dict(path=str(args.output), cases=len(result['cases']),
                         sha256=hashlib.sha256(args.output.read_bytes()).hexdigest(),
                         cases_sha256=result['cases_sha256']), sort_keys=True))


if __name__ == '__main__':
    main()
