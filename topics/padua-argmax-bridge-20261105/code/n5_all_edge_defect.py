#!/usr/bin/env python3
"""Developer checks of selected defect blocks; no degree-ordering scan."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform
import time

import mpmath as mp

from n5_central_edge_defect import finite_d, prefix, weighted_chebyshev


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_case(n, endpoint, q, phase, first):
    m, s = n + 1, mp.mpf(phase)
    j_endpoint = 0 if endpoint == 1 else n
    phi = (q * mp.pi + s) / m
    distance = min(q, m - q)
    pairs = []
    if distance <= 4:
        top = q > m / 2
        eta = distance % 2 if top else 1 - distance % 2
        for index in range((3 * n + 7) // 8, n // 2 + 1):
            k = index + eta
            r = n - index if top else index
            pairs.append((r, k))
        category, floor = "near", mp.mpf(1) / 864
        numerator_floor = mp.mpf(1) / 8
        assert len(pairs) >= mp.mpf(n) / 16
    else:
        gamma = min(phi, mp.pi - phi)
        assert gamma > 4 * mp.pi / n
        top = phi > mp.pi / 2
        if gamma <= mp.pi / 6:
            row_start, row_end = (m + 2) // 3, m // 2
            category, floor = "small", 7 / (768 * mp.pi)
        else:
            row_start, row_end = (m + 11) // 12, m // 6
            category, floor = "middle", mp.mpf(7) / 6144
        numerator_floor = mp.mpf(7) / 32
        row_counts = []
        for index in range(row_start, row_end + 1):
            b_prime = index * mp.pi / m
            k = m - index if top else index
            if category == "small":
                low, high = b_prime - gamma / 2, b_prime + gamma / 2
            else:
                low, high = gamma - b_prime / 2, gamma + b_prime / 2
            selected = [r for r in range(1, n) if (r + k - j_endpoint) % 2 == 0
                        and low <= r * mp.pi / n <= high]
            row_counts.append(len(selected))
            pairs.extend((r, k) for r in selected)
        if category == "small":
            assert len(row_counts) >= mp.mpf(m) / 12
            assert min(row_counts) >= n * gamma / (4 * mp.pi)
        else:
            assert len(row_counts) >= mp.mpf(m) / 16
            assert min(row_counts) >= mp.mpf(n) / 48
    subset = mp.mpf(0)
    smallest_numerator, worst_identity = mp.inf, mp.mpf(0)
    row_cache = {}
    for r, k in pairs:
        assert 0 < r < n and 0 < k < m
        assert (r + k - j_endpoint) % 2 == 0
        original_j = r if endpoint == 1 else n - r
        assert (original_j + k) % 2 == 0
        u, b = r * mp.pi / n, k * mp.pi / m
        halves = []
        for sign in (1, -1):
            key = (k, sign)
            v = phi + sign * b
            if key not in row_cache:
                row_cache[key] = prefix(weighted_chebyshev(mp.cos(v), n))
            half = (((-1)**r) * finite_d(first[r], row_cache[key]) - 1) / 2
            numerator = mp.cos(s / 2)**2 * (1 + mp.cos(v)) + mp.sin(s) * mp.sin(v) / 2
            smallest_numerator = min(smallest_numerator, numerator)
            assert numerator >= numerator_floor - mp.mpf("1e-60")
            denominator = mp.cos(u) - mp.cos(v)
            assert abs(denominator) > mp.mpf("1e-60")
            worst_identity = max(worst_identity, abs(half - numerator / denominator))
            halves.append(half)
        assert halves[0] * halves[1] < 0
        defect = abs(halves[0]) + abs(halves[1]) - abs(halves[0] + halves[1])
        subset += 2 * defect / (n * m)
    assert subset >= floor
    assert worst_identity < mp.mpf("1e-60")
    return {"n": n, "endpoint": endpoint, "q": q, "s": phase,
            "category": category, "selected_pairs": len(pairs),
            "selected_defect": mp.nstr(subset, 30),
            "analytic_case_floor": mp.nstr(floor, 30),
            "selected_defect_over_case_floor": mp.nstr(subset / floor, 30),
            "min_numerator": mp.nstr(smallest_numerator, 30),
            "max_finite_polynomial_quotient_error": mp.nstr(worst_identity, 10)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = 80
    started = time.process_time()
    # Exact endpoint budgets and conservative comparisons used in the proof.
    assert Q(3 * 64, 40) - Q(43, 10) == Q(1, 2)
    assert Q(64, 10) - Q(22, 5) == 2
    assert Q(3, 8) * 3 > Q(1, 2)
    assert 8 * Q(22, 7) + 1 < 27
    assert Q(11, 5)**2 < 5 and Q(7, 20) < Q(9, 25)
    assert Q(15, 16) * Q(2, 5) - Q(1, 4) == Q(1, 8)
    assert Q(15, 32) - Q(1, 4) == Q(7, 32)
    assert min(Q(1, 864), Q(7, 3072), Q(7, 6144)) > Q(1, 1024)
    assert Q(7, 576) + Q(112, 225) == Q(66087, 129600) < 1
    rows = []
    for n in (64, 65):
        m = n + 1
        first = [weighted_chebyshev(mp.cos(r * mp.pi / n), n) for r in range(n + 1)]
        for endpoint in (1, -1):
            eligible = [q for q in range(1, m) if endpoint**n * (-1)**q == -1]
            centers = {q for q in eligible if min(q, m - q) <= 4}
            far = [q for q in eligible if min(q, m - q) >= 5]
            for target in (5, mp.mpf(m) / 2, m - 5):
                centers.add(min(far, key=lambda q: (abs(q - target), q)))
            for q in sorted(centers):
                for phase in ("-0.5", "0.5"):
                    rows.append(selected_case(n, endpoint, q, phase, first))
    topic = Path(__file__).resolve().parents[1]
    sources = [Path(__file__).resolve(), topic / "code/n5_central_edge_defect.py",
               topic / "theory/N5-all-edge-defect.md", topic / "ideas/N5-all-edge-defect.md",
               topic / "novelty-gate-N5.md", topic / "theory/N1-row-model.md"]
    summary = {"kind": "MEASURED developer selected-block checks; analytic theorem independent",
               "input_head": "c000899f3fb10d6ba0f1725341a045fe11ec943a",
               "python": platform.python_version(), "mpmath": mp.__version__,
               "decimal_digits": mp.mp.dps, "cases": len(rows),
               "category_counts": {category: sum(row["category"] == category for row in rows)
                                   for category in ("near", "small", "middle")},
               "exact_rational_budgets_passed": True, "all_diagnostics_passed": True,
               "min_selected_defect_over_case_floor": min(
                   (row["selected_defect_over_case_floor"] for row in rows), key=mp.mpf),
               "max_finite_polynomial_quotient_error": mp.nstr(max(
                   mp.mpf(row["max_finite_polynomial_quotient_error"]) for row in rows), 10),
               "sources": {str(path.relative_to(topic)): sha(path) for path in sources},
               "cpu_seconds": time.process_time() - started,
               "independent_review": "PENDING; execution is by developer"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"summary": summary, "cases": rows}, indent=2) + "\n")
    summary["bulk_output"] = {"path": str(args.output), "bytes": args.output.stat().st_size,
                              "sha256": sha(args.output)}
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"cases": summary["cases"], "categories": summary["category_counts"],
                      "min_selected_defect_over_case_floor": summary["min_selected_defect_over_case_floor"],
                      "max_finite_polynomial_quotient_error": summary["max_finite_polynomial_quotient_error"],
                      "status": "MEASURED diagnostics passed"}))


if __name__ == "__main__":
    main()
