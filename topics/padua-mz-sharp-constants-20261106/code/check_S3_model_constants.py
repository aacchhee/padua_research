"""Supplementary finite exact checks; the all-R proof is analytic."""
from fractions import Fraction as F


def main():
    worst, count = F(0), 0
    for R in range(2, 257):
        for a in range(1, R // 2 + 1):
            for b in range(R - a + 1, R + 1):
                ratio = ((F(R * R - b * b) + F(1, 4))
                         / (F(b * b) - F(1, 4)) / F(12 * a, R))
                assert ratio <= 1
                worst, count = max(worst, ratio), count + 1
        for m in (2 * R, 2 * R + 1):
            assert F(m * (m + 1), R * R) <= F(15, 2)
    assert 134 * F(15, 2) * 4 == 4020 < 4096
    assert 16 * F(15, 2) == 120
    print({"strip_coefficient_cases": count, "R_range": [2, 256],
           "max_bound_fraction": str(worst), "form_constant": 4020,
           "norm_constant": 120})


if __name__ == "__main__":
    main()
