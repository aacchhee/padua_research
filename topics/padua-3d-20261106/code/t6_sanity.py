#!/usr/bin/env python3
"""Bounded T6 formula checks; no finite calculation is an all-n proof.

Run from any directory. Default receipt is ../evidence/t6-sanity.json.
Exact integer/Fraction assertions are deterministic formula sanity checks.
FFT grid averages are explicitly MEASURED, with no enclosure claim.
"""

import argparse
from fractions import Fraction
from itertools import product
import json
from math import pi
from pathlib import Path

import numpy as np


def ball(n, d=3):
    return [k for k in product(range(-n, n + 1), repeat=d)
            if sum(map(abs, k)) <= n]


def facet(k, n):
    base = n - sum(k)
    return (base,) + tuple(base + 2 * k[j] for j in range(1, len(k)))


def exact_checks():
    counts = []
    for n in range(17):
        ks = ball(n)
        rs = [facet(k, n) for k in ks]
        assert all(min(r) >= 0 for r in rs)
        assert len(set(rs)) == len(ks)
        # The polynomial coefficient after reflection and translation
        # averaging is 2^-s, including zero-coordinate strata.
        assert all(Fraction(1, 2 ** sum(t != 0 for t in k)) *
                   product_multiplier(k) == 1 for k in ks)
        m = n // 2
        retained = 0
        for a, b, c in product(range(1, m + 1), repeat=3):
            if a <= b and a <= c:
                k = (n - b - c, b - a, c - a)
                assert min(k) >= 0 and sum(k) <= n
                assert facet(k, n) == (2 * a, 2 * b, 2 * c)
                retained += 1
        counts.append({"n": n, "ball_size": len(ks),
                       "retained_positive_frequencies": retained})

    harmonic = []
    for m in (1, 2, 3, 4, 8, 16, 32):
        h = sum((Fraction(1, a) for a in range(1, m + 1)), Fraction(0))
        # Nested tails compute the exact sum over a <= b and a <= c.
        s = sum((Fraction(1, a) *
                 sum((Fraction(1, b) for b in range(a, m + 1)),
                     Fraction(0)) ** 2
                 for a in range(1, m + 1)), Fraction(0))
        assert 3 * s >= h ** 3
        harmonic.append({"m": m, "harmonic": str(h),
                         "positive_margin_3S_minus_Hcubed": str(3*s-h**3)})

    # Additional general-d checks exercise the d-3 inverse coefficient.
    general = []
    for d, n in ((3, 6), (4, 6), (5, 8)):
        m = n // (d - 1)
        checked = 0
        for a in product(range(1, m + 1), repeat=d):
            if a[0] <= min(a[1:]):
                k = (n - sum(a[1:]) + (d - 3)*a[0],) + tuple(
                    a[j] - a[0] for j in range(1, d))
                assert min(k) >= 0 and sum(k) == n - 2*a[0]
                assert facet(k, n) == tuple(2*x for x in a)
                checked += 1
        general.append({"d": d, "n": n, "retained_checked": checked})
    return {"scope": "finite exact integer/Fraction formula sanity only",
            "facet_matrix_d3": [[-1, -1, -1], [-1, 1, -1], [-1, -1, 1]],
            "facet_determinant_d3": -4, "support_checks": counts,
            "harmonic_checks": harmonic, "general_dimension_subset": general,
            "projection_multiplier_identity": "2^(-s(k))*2^s(k)=1 on B_n; outside coefficient=0"}


def product_multiplier(k):
    ans = 1
    for entry in k:
        ans *= 1 if entry == 0 else 2
    return ans


def measured_checks():
    rows = []
    for n, grid in ((2, 64), (4, 64), (8, 128), (16, 128), (32, 256)):
        freq = np.zeros((grid, grid, grid), dtype=np.float64)
        for k in ball(n):
            freq[tuple(t % grid for t in k)] = 1
        values = np.fft.ifftn(freq) * grid ** 3
        mesh_mean = float(np.mean(np.abs(values)))
        m = n // 2
        h = sum(1 / a for a in range(1, m + 1))
        lower_fourier = h ** 3 / (24*pi ** 3)
        assert mesh_mean > lower_fourier
        # This Fourier projection is a convenient particular real P.
        # Its even-extension translation average has weights 2^-s.
        avg_freq = np.zeros_like(freq)
        for k in ball(n):
            avg_freq[tuple(t % grid for t in k)] = 2.0 ** (-sum(t != 0 for t in k))
        avg_values = np.fft.ifftn(avg_freq) * grid ** 3
        corrected_freq = avg_freq.copy()
        for axis in range(3):
            mult = np.full(grid, 2.0)
            mult[0] = 1.0
            shape = [1, 1, 1]
            shape[axis] = grid
            corrected_freq *= mult.reshape(shape)
        assert np.array_equal(corrected_freq, freq)
        rows.append({"n": n, "grid_axis_count": grid,
                     "status": "MEASURED",
                     "Fourier_L1_grid_average": mesh_mean,
                     "averaged_cosine_kernel_L1_grid_average":
                     float(np.mean(np.abs(avg_values))),
                     "proven_Fourier_lower_evaluated_float": lower_fourier,
                     "proven_Lebesgue_lower_evaluated_float": lower_fourier/27,
                     "max_imaginary_grid_error": float(np.max(np.abs(values.imag)))})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=
                        Path(__file__).resolve().parents[1] / "evidence/t6-sanity.json")
    args = parser.parse_args()
    receipt = {"claim_status": "MEASURED finite sanity, not a computer proof",
               "rules_sha": "ccd9e905d19c0c625c196c4a3f3e707058ed042a",
               "command": "python topics/padua-3d-20261106/code/t6_sanity.py",
               "exact_checks": exact_checks(), "measured_fft": measured_checks(),
               "numpy_version": np.__version__,
               "limits": "No certified quadrature, no finite-to-infinite extrapolation; analytic proofs are independent of this receipt."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "bytes": args.output.stat().st_size,
                      "status": "PASS finite sanity checks",
                      "measured_degrees": [r["n"] for r in receipt["measured_fft"]]}))


if __name__ == "__main__":
    main()
