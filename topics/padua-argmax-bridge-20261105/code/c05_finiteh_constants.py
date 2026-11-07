#!/usr/bin/env python3
"""Exact scalar budget audit; no finite kernel or model evaluation."""
from fractions import Fraction as F
import json

n0, R = 10**6, 128
q2 = 2 * F(1, 6) * (F(2, 5)**2 + F(2, 5) * F(5, 12) + F(5, 12)**2)
assert q2 < F(1, 5)
assert 4 * (F(2, 9) + F(4, 21) + F(8, 15)) < 4
hessian = 128 + 255 * (4 + 168) + F(515 * R**2 + 1, n0)
assert hessian < 45000
assert 34 + F(177 * R, n0) < 35
assert F(15000, n0) < F(1, 60)
assert 18 + F(3, 1000) + F(7, 20) * 3 < 5 * (3 + 1)
budget = (F(3, 14000) + F(1, 50000) + F(3, 2 * 10**9)
          + F(11270, n0) + F(200 * 15, n0))
assert budget < F(1, 32)
assert F(1, 16) - F(1, 32) - F(3, 14000) == F(869, 28000)
print(json.dumps({
    "status": "EXACT_RATIONAL_CONSTANT_CHECK",
    "endpoint_hessian_coefficient_upper": str(hessian),
    "full_model_budget_upper": str(budget),
    "margin_below_one_over_32": str(F(1, 32) - budget),
    "noncorner_gap": "869/28000",
    "kernel_or_degree_scan": False,
    "limitation": "Only finite constants; analytic identities, cells and normalization need independent reconstruction."
}, indent=2))
