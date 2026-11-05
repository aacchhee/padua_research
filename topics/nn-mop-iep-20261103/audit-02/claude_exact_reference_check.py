#!/usr/bin/env python3
"""Claude audit-02 check: exact ground truth versus the C4 pilot's mpmath reference.

Extends the developer's N=4 exact cross-check to larger N. Ground truth comes from
the auditor's exact Fraction moment solver (audit-01/claude_layer_recursion_check.py,
ground_truth). Inputs and the 220-digit reference come from code/c4_float_baseline.py.
Prints, per case, the fieldwise sup-relative distance of the reference and of the
binary64 run from the exact values. Requires mpmath. MEASURED evidence only.
"""
import hashlib
import importlib.util
import json
import platform
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def main():
    base, base_sha = load('c4', 'code/c4_float_baseline.py')
    aud, aud_sha = load('aud', 'audit-01/claude_layer_recursion_check.py')
    sizes = [int(a) for a in sys.argv[1:]] or [8, 12, 16]
    rows = []
    with mp.workdps(220):
        for fam in ('krawtchouk', 'hahn'):
            for N in sizes:
                x, w = base.inputs(N, fam)
                _, truth = aud.ground_truth(x, w)
                exact = {nu: {k: mp.mpf(v.numerator) / v.denominator for k, v in r.items()}
                         for nu, r in truth.items()}
                ref, _ = base.compute(N, fam, 220)
                dbl, _ = base.compute(N, fam)
                e_ref, _ = base.errors(ref, exact)
                e_dbl, _ = base.errors(dbl, exact)
                rows.append(dict(family=fam, N=N, ref_vs_exact=float(e_ref),
                                 double_vs_exact=float(e_dbl)))
                assert e_ref < mp.mpf('1e-100'), (fam, N, e_ref)
    print(json.dumps(dict(status='MEASURED auditor exact-reference check', python=platform.python_version(),
                          mpmath=mp.__version__, baseline_sha256=base_sha, auditor_checker_sha256=aud_sha,
                          code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                          cases=rows, all_passed=True), indent=1, sort_keys=True))


if __name__ == '__main__':
    main()
