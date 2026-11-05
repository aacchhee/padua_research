#!/usr/bin/env python3
"""Developer sanity checks for N5's analytic lemma; not a proof checker."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import time

import mpmath as mp


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def w_primitive(x):
    # Symmetry removes the removable endpoint from the numerical expression.
    t = min(x, mp.pi - x)
    return mp.log(mp.sinc(t) / (mp.pi - t))


def w_prime(x):
    # Differentiate the pole-deleted series (theorem (7)). The convergent
    # reciprocal-square sums are evaluated as trigamma functions by mpmath.
    z = x / mp.pi
    return -(mp.polygamma(1, 1 + z) + mp.polygamma(1, 2 - z)) / mp.pi**2


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = 110
    start = time.process_time()
    topic = Path(__file__).resolve().parents[1]
    theorem = topic / "theory/N5-partial-cotangent.md"
    gate = topic / "novelty-gate-N5.md"
    source = Path(__file__).resolve()

    # Exact quartic check of the sign/coefficient in (10)-(11), h=1.
    quartic_functional = Fraction(1, 1920) - Fraction(1, 576)
    assert quartic_functional == -Fraction(7, 5760)
    assert 5 * 19456 * 50**5 < 4 * 81 * 157**5

    rows = []
    offsets = ["1e-30", "0.142857142857142857142857142857", "0.5",
               "0.875", "0.999999999999999999999999999999"]
    for n in (2, 3, 7, 33, 128):
        h = mp.pi / n
        blocks = sorted({(0, 0), (n - 1, n - 1), (0, n - 1),
                         (0, n // 2), (n // 2, n - 1),
                         (n // 3, 2 * n // 3)})
        for offset in offsets:
            delta = mp.mpf(offset)
            for a, b in blocks:
                count = b - a + 1
                left, right = h * (a + delta - mp.mpf("0.5")), h * (b + delta + mp.mpf("0.5"))
                direct = mp.fsum(mp.cot(h * (i + delta)) for i in range(a, b + 1))
                pole = mp.fsum(1 / (i + delta) - 1 / (n - i - delta)
                               for i in range(a, b + 1)) / h
                integral = (w_primitive(right) - w_primitive(left)) / h
                derivative = -h * (w_prime(right) - w_prime(left)) / 24
                corrected = pole + integral + derivative
                bound = mp.mpf(7) * count * h**4 / 7200
                error = abs(direct - corrected)
                ratio = error / bound
                rows.append({"n": n, "delta": offset, "a": a, "b": b,
                             "absolute_error": mp.nstr(error, 30),
                             "analytic_bound": mp.nstr(bound, 30),
                             "error_over_bound": mp.nstr(ratio, 30)})
                assert ratio < 1, rows[-1]

    worst = max(rows, key=lambda row: mp.mpf(row["error_over_bound"]))
    summary = {"kind": "MEASURED developer sanity verification; analytic proof independent",
               "rules_read_sha": "98d6c00d8a474cf97602c9cfdea631a837191ac0",
               "python": platform.python_version(), "mpmath": mp.__version__,
               "decimal_digits": mp.mp.dps,
               "sources": {str(p.relative_to(topic)): sha(p) for p in (source, theorem, gate)},
               "cases": len(rows), "degrees": [2, 3, 7, 33, 128],
               "offsets": offsets, "all_within_analytic_bound": True,
               "max_error_over_bound": worst["error_over_bound"], "worst_case": worst,
               "exact_quartic_functional": str(quartic_functional),
               "rational_derivative_constant_comparison": True,
               "cpu_seconds": time.process_time() - start,
               "independent_review": "PENDING; this execution is by developer"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"summary": summary, "cases": rows}, indent=2) + "\n")
    summary["bulk_output"] = {"path": str(args.output), "bytes": args.output.stat().st_size,
                              "sha256": sha(args.output)}
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"cases": len(rows), "max_error_over_bound": worst["error_over_bound"],
                      "receipt": str(args.receipt), "status": "MEASURED verification passed"}))


if __name__ == "__main__":
    run()
