#!/usr/bin/env python3
"""Exact rational checks of constants in C02; not a projected-Q computation."""
from fractions import Fraction as F
from math import factorial
import json


def main():
    pi_lo, pi_hi = F(157, 50), F(22, 7)
    x_lo, x_hi = pi_lo / 20, pi_hi / 20
    assert x_lo - x_hi**3 / 6 > F(3, 20)
    assert 1 - x_lo**2 / 2 + x_hi**4 / 24 < F(247, 250)
    assert 2 * F(707, 1000)**2 < 1
    assert F(283, 200)**2 > 2  # sqrt(2)-1 <83/200
    log_lo = 2 * (F(1, 9) + F(1, 9)**3 / 3)
    log_hi = F(1, 4) - F(1, 4)**2 / 2 + F(1, 4)**3 / 3
    assert F(3, 2) + 4 * log_lo > F(239, 100)
    assert F(3, 2) + 4 * log_hi < F(12, 5)
    exp_lo = sum(F(5, 3)**k / factorial(k) for k in range(8))
    assert exp_lo == F(5833853, 1102248) > F(830, 157)
    assert (4 * pi_hi + F(1, 2)) / 64 < F(7, 30)
    assert (57 * pi_lo - 65) / 128 > 0
    assert F(225, 1040) / (pi_hi + F(1, 2)) > F(1, 20)
    assert F(957, 3072) / (pi_hi * F(7, 4)) > F(1, 20)
    a, r = F(15, 16), F(1, 2)
    U = F(347, 1000) * a - F(157, 500) * r
    V = F(17, 20) * a - r / 2
    W = F(779, 750) * a - F(5, 6) * r
    assert U > F(21, 125) and V < F(11, 20) and W < F(14, 25)

    def uniform(n):
        return (F(239, 100) * F(21, 125) / pi_hi**2
                - F(12, 5) * F(11, 20) / (pi_lo * n)
                - 5 * F(14, 25) / (pi_lo * n)
                - 5 * F(11, 20) / (n**2 * F(3, 20)))

    margins = {64: uniform(64) - F(1, 64),
               160: uniform(160) - F(1, 32)}
    assert margins[64] == F(34466881, 729484800000) > 0
    assert margins[160] == F(88079689, 182371200000) > 0
    n = 4096
    assert (4 * pi_hi + F(1, 2)) / n < F(1, 45)
    assert F(20, 65) / (pi_hi + F(1, 2)) > F(1, 16)
    assert F(26, 15)**2 > 3
    small_margin = F(33, 16) / (pi_hi * F(26, 15)) * (F(1, 6) - F(1, n)) - F(1, 16)
    assert small_margin == F(1733, 3407872) > 0
    assert pi_lo / 100 - (pi_hi / 100)**3 / 6 > F(3, 100)
    assert 4 * F(56, 81) > F(11, 4)
    assert 4 * F(25, 36) < F(14, 5)
    assert (F(11, 16) * F(6, 25) * pi_lo
            + F(15, 16) * (F(707, 1000) - 1)) > F(6, 25)
    assert exp_lo**2 > F(4150, 157)
    assert (F(11, 16) * F(10, 3)
            - F(15, 16) * F(6, 25) * pi_lo) < F(8, 5)
    large = (F(11, 4) * F(6, 25) / pi_hi**2
             - F(14, 5) * F(11, 16) / (pi_lo * n)
             - 8 * F(8, 5) / (pi_lo * n)
             - 8 * F(11, 16) / (n**2 * F(3, 100)))
    margins[4096] = large - F(1, 16)
    assert margins[4096] == F(3436012187, 1086534451200) > 0
    print(json.dumps({"status": "EXACT_RATIONAL_CONSTANT_CHECK",
                      "degree_or_phase_scan": False,
                      "margins": {str(n): str(v) for n, v in margins.items()},
                      "small_angle_margin_n4096": str(small_margin),
                      "limitation": "Checks finite constants only; the analytic projection and mesh arguments require independent proof review."}, indent=2))


if __name__ == "__main__":
    main()
