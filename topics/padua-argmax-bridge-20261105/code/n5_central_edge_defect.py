#!/usr/bin/env python3
"""Small developer normalization diagnostics; not an ordering certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform
import time

import mpmath as mp


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def weighted_chebyshev(x, n):
    values = [mp.mpf(1), x]
    for _ in range(2, n + 1):
        values.append(2 * x * values[-1] - values[-2])
    return [values[0]] + [2 * value for value in values[1:]]


def prefix(values):
    result, total = [], mp.mpf(0)
    for value in values:
        total += value
        result.append(total)
    return result


def finite_d(first, second_prefix):
    n = len(first) - 1
    return mp.fsum(first[p] * second_prefix[n - p] for p in range(n + 1))


def c_exact(r):
    return Q(1, 5) - 5 * r / 16 - r * r / 20


def evaluate(n, endpoint, phase):
    m, s = n + 1, mp.mpf(phase)
    q = min((q for q in range(m + 1) if endpoint**n * (-1)**q == -1),
            key=lambda q: (abs(2 * q - m), q))
    phi = (q * mp.pi + s) / m
    assert 11 * mp.pi / 24 <= phi <= 13 * mp.pi / 24
    r = abs(s)
    c = mp.mpf(1) / 5 - 5 * r / 16 - r * r / 20
    bound = c * (1 - mp.mpf(8) / n) * (1 - mp.mpf(8) / m) / 32
    first = [weighted_chebyshev(mp.cos(j * mp.pi / n), n) for j in range(n + 1)]
    second = {}
    for k in range(m + 1):
        for sign in (-1, 1):
            v = phi + sign * k * mp.pi / m
            second[k, sign] = prefix(weighted_chebyshev(mp.cos(v), n))
    lam, primitive, defect = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    selected_rows, selected_pairs = {}, 0
    worst_quotient_error = mp.mpf(0)
    smallest_numerator = mp.inf
    for j in range(n + 1):
        reflected = j if endpoint == 1 else n - j
        u = reflected * mp.pi / n
        tau = endpoint**n * (-1)**j
        for k in range(m + 1):
            if (j + k) % 2:
                continue
            halves = [(tau * finite_d(first[reflected], second[k, sign]) - 1) / 2
                      for sign in (1, -1)]
            factor = (mp.mpf(1) / 2 if j in (0, n) else mp.mpf(1))
            factor *= (mp.mpf(1) / 2 if k in (0, m) else 1)
            weight = 2 * factor / (n * m)
            pair_sum = abs(halves[0] + halves[1])
            abs_sum = abs(halves[0]) + abs(halves[1])
            lam += weight * pair_sum
            primitive += weight * abs_sum
            defect += weight * (abs_sum - pair_sum)
            b = k * mp.pi / m
            if mp.pi / 8 <= b <= mp.pi / 4 and phi - mp.pi / 8 < u < phi + mp.pi / 8:
                selected_rows[k] = selected_rows.get(k, 0) + 1
                selected_pairs += 1
                assert halves[0] * halves[1] < 0
                assert abs_sum - pair_sum >= c - mp.mpf("1e-60")
                for half, sign in zip(halves, (1, -1)):
                    v = phi + sign * b
                    numerator = mp.cos(s / 2)**2 * (1 + mp.cos(v)) + mp.sin(s) * mp.sin(v) / 2
                    smallest_numerator = min(smallest_numerator, numerator)
                    assert numerator >= c - mp.mpf("1e-60")
                    quotient = numerator / (mp.cos(u) - mp.cos(v))
                    worst_quotient_error = max(worst_quotient_error, abs(quotient - half))
    assert len(selected_rows) >= mp.mpf(m) / 8 - 1
    assert min(selected_rows.values()) >= mp.mpf(n) / 8 - 1
    assert defect >= bound
    # Separate finite-polynomial odd-periodic-board computation of S_n(0,s).
    periodic_first = [weighted_chebyshev(mp.cos(j * mp.pi / n), n) for j in range(2 * n)]
    periodic_primitive = mp.mpf(0)
    for index in range(2 * m):
        v = (index * mp.pi + s) / m
        second_prefix = prefix(weighted_chebyshev(mp.cos(v), n))
        for j in range(1 - index % 2, 2 * n, 2):
            f = (((-1)**j) * finite_d(periodic_first[j], second_prefix) - 1) / 2
            periodic_primitive += abs(f) / (n * m)
    primitive_error = abs(primitive - periodic_primitive)
    identity_error = abs(primitive - lam - defect)
    assert max(primitive_error, identity_error, worst_quotient_error) < mp.mpf("1e-60"), {
        "n": n, "endpoint": endpoint, "s": phase, "primitive": str(primitive),
        "periodic_primitive": str(periodic_primitive), "primitive_error": str(primitive_error),
        "triangle_error": str(identity_error), "quotient_error": str(worst_quotient_error)}
    return {"n": n, "endpoint": endpoint, "q": q, "s": phase,
            "lambda": mp.nstr(lam, 30), "primitive": mp.nstr(primitive, 30),
            "defect": mp.nstr(defect, 30), "analytic_lower_bound": mp.nstr(bound, 30),
            "defect_over_bound": mp.nstr(defect / bound, 30),
            "selected_rows": len(selected_rows), "selected_pairs": selected_pairs,
            "min_selected_numerator": mp.nstr(smallest_numerator, 30),
            "periodic_primitive_identity_error": mp.nstr(primitive_error, 10),
            "triangle_identity_error": mp.nstr(identity_error, 10),
            "selected_quotient_error": mp.nstr(worst_quotient_error, 10)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = 80
    start = time.process_time()
    assert c_exact(Q(1, 2)) == Q(1, 32)
    assert c_exact(Q(1, 4)) == Q(19, 160)
    assert Q(25, 45056) > Q(1, 2048)
    assert Q(475, 225280) > Q(1, 512)
    assert Q(7, 288) + Q(112, 225) == Q(33831, 64800) < 1
    cases = [(32, 1, "-0.5"), (32, -1, "0.5"),
             (33, 1, "0.5"), (33, -1, "-0.5"),
             (48, 1, "0.25"), (64, -1, "0")]
    rows = [evaluate(*case) for case in cases]
    topic = Path(__file__).resolve().parents[1]
    sources = [Path(__file__).resolve(), topic / "theory/N5-central-edge-defect.md",
               topic / "ideas/N5-central-edge-defect.md", topic / "novelty-gate-N5.md",
               topic / "theory/N1-row-model.md"]
    summary = {"kind": "MEASURED developer finite-polynomial diagnostic; no ordering claim",
               "input_head": "714f3cad18859c07cd13f31561f2a185f9591a7f",
               "python": platform.python_version(), "mpmath": mp.__version__,
               "decimal_digits": mp.mp.dps, "cases": len(rows),
               "exact_rational_constant_checks": True,
               "all_diagnostics_passed": True,
               "minimum_defect_over_bound": min((row["defect_over_bound"] for row in rows), key=mp.mpf),
               "max_primitive_identity_error": mp.nstr(max(mp.mpf(row["periodic_primitive_identity_error"]) for row in rows), 10),
               "sources": {str(path.relative_to(topic)): sha(path) for path in sources},
               "cpu_seconds": time.process_time() - start,
               "independent_review": "PENDING; execution is by the developer"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"summary": summary, "cases": rows}, indent=2) + "\n")
    summary["bulk_output"] = {"path": str(args.output), "bytes": args.output.stat().st_size,
                              "sha256": sha(args.output)}
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"cases": len(rows), "minimum_defect_over_bound": summary["minimum_defect_over_bound"],
                      "max_primitive_identity_error": summary["max_primitive_identity_error"],
                      "receipt": str(args.receipt), "status": "MEASURED diagnostics passed"}))


if __name__ == "__main__":
    main()
