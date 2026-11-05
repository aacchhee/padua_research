#!/usr/bin/env python3
"""Developer diagnostic against the direct corrected Chebyshev kernel.

This is high-precision numerical comparison, not outward verification and
not the independent checker required by the computer-proof workflow.
"""
import argparse
import csv
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import tempfile

import mpmath as mp


def number(s):
    q = Fraction(s)
    return mp.mpf(q.numerator) / q.denominator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("producer")
    args = parser.parse_args()
    mp.mp.dps = 110
    max_relative_error = mp.mpf(0)
    checked = 0
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for n in range(2, 9):
            m = n + 1
            terms = Path(tmp) / f"n{n}.csv"
            subprocess.run([args.producer, str(n), "256", str(terms)],
                           check=True, stdout=subprocess.DEVNULL)
            actual = {(int(r["j"]), int(r["k"])): r
                      for r in csv.DictReader(terms.open())}
            energy = mp.mpf(0)
            corner = mp.mpf(0)
            for j in range(n + 1):
                for k in range(j % 2, m + 1, 2):
                    if k == 0 and j > 0:
                        assert (j, k) not in actual
                        continue
                    weight = mp.mpf(2) / (n * m)
                    if j in (0, n):
                        weight /= 2
                    if k in (0, m):
                        weight /= 2
                    value, gx, gy = mp.mpf(0), mp.mpf(0), mp.mpf(0)
                    # All physical endpoint derivatives are exact integers:
                    # T_a(-1)=(-1)^a and T'_a(-1)=(-1)^(a+1)*a^2.
                    for a in range(n + 1):
                        for b in range(n + 1 - a):
                            h = (1 if a == 0 else 2) * (1 if b == 0 else 2)
                            if (a, b) == (n, 0):
                                h -= 1
                            coeff = (weight * h * mp.cos(a * j * mp.pi / n)
                                     * mp.cos(b * k * mp.pi / m))
                            sign = (-1) ** (a + b)
                            value += coeff * sign
                            gx -= coeff * sign * a * a
                            gy -= coeff * sign * b * b
                    target = [abs(value), gx / value, gy / value,
                              (gx * gx + gy * gy) / abs(value)]
                    record = actual[j, k]
                    for name, expected in zip(("value", "qx", "qy", "energy"), target):
                        lower, upper = number(record[name + "_lo"]), number(record[name + "_hi"])
                        midpoint = (lower + upper) / 2
                        relative = abs(midpoint - expected) / max(1, abs(expected))
                        max_relative_error = max(max_relative_error, relative)
                        assert relative < mp.mpf("1e-60"), (n, j, k, name, relative)
                        # This tolerance belongs only to the numerical diagnostic.
                    checked += 1
                    corner += target[0]
                    energy += target[3]
            rows.append({"degree": n, "corner": str(corner), "energy": str(energy)})
    print(json.dumps({"status": "MEASURED diagnostic only",
                      "method": "direct corrected coefficient-kernel physical derivatives",
                      "mpmath_version": mp.__version__, "decimal_precision": mp.mp.dps,
                      "degrees": list(range(2, 9)), "nonzero_cardinals_checked": checked,
                      "max_relative_midpoint_error": str(max_relative_error), "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
