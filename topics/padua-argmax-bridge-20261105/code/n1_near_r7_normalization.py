#!/usr/bin/env python3
"""Preregistered MEASURED normalization pilot; no model evaluation or fit."""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import resource
import sys
import time

import mpmath as mp

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
    mp.mp.dps = 60
    start = time.process_time()
    source = TOPIC / 'code/n1_rows.py'
    spec = importlib.util.spec_from_file_location('n1_rows_r7_dependency', source)
    rows = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rows)
    cases = []
    for n in (17, 24, 32):
        m = n + 1
        periodic = mp.mpf(0)
        collisions = 0
        for r in range(2*m):
            v = F(r, m)
            delta = (1-r) % 2
            for k in range(n):
                u = F(delta+2*k, n)
                collisions += bool(rows.collision(u, v))
                periodic += abs(rows.finite_g(n, u, v))/2
        periodic /= n*m
        positive = mp.mpf(0)
        for j in range(n+1):
            x = mp.cos(mp.pi*j/n)
            ej = mp.mpf(1)/2 if j in (0, n) else mp.mpf(1)
            for k in range(n+1):
                if (j+k) % 2 == 0:
                    continue
                y = mp.cos(mp.pi*k/m)
                fk = mp.mpf(1)/2 if k == 0 else mp.mpf(1)
                positive += ej*fk*(1+y)/abs(x-y)
        corner = 4*positive/(n*m) + mp.mpf(1)/m
        discrepancy = abs(periodic-corner)
        assert discrepancy < mp.mpf('1e-50')
        cases.append(dict(n=n, primitive=str(periodic), corner=str(corner),
                          absolute_discrepancy=str(discrepancy),
                          periodic_polynomial_collisions=collisions))

    # These finite rational comparisons explain the elementary proof constants.
    h10 = sum((F(1, k) for k in range(1, 11)), F())
    e_lower = sum((F(2303, 1000)**j / factorial(j)
                   for j in range(11)), F())
    x = F(17, 39)
    log_lower = 2*(x+x**3/3)
    rational_controls = {
        'exp_2303_over_1000_partial_order10_gt10': e_lower > 10,
        'H10_minus2303_over1000_minus1over20_gt23over40':
            h10-F(2303, 1000)-F(1, 20) > F(23, 40),
        'log28over11_artanh_order3_gt37over40': log_lower > F(37, 40),
        'pi_lower31over10_squared_gt48over5': F(31, 10)**2 > F(48, 5),
        'coefficient_rational_upper': str(1-F(6*47, 192)
                                         +F(15, 16)-F(2*47, 192)),
    }
    assert all(v for v in rational_controls.values() if isinstance(v, bool))
    assert rational_controls['coefficient_rational_upper'] == '-1/48'
    out = {
        'status': 'MEASURED_ONLY; normalization, not M_near evaluation or a proof',
        'command': 'python topics/padua-argmax-bridge-20261105/code/n1_near_r7_normalization.py',
        'input_head': '8dc1521cf68f7780bd10e02495f6f71a639c03c6',
        'degrees': [17, 24, 32], 'phase_alpha_beta': [0, 0],
        'python': platform.python_version(), 'mpmath': mp.__version__,
        'decimal_precision': mp.mp.dps, 'cpu_cap_seconds': 300,
        'cpu_seconds': time.process_time()-start,
        'source_sha256': digest(Path(__file__).resolve()),
        'dependency_sha256': {'code/n1_rows.py': digest(source)},
        'cases': cases, 'rational_controls': rational_controls,
        'limits': 'Floating arithmetic; no rigorous roundoff enclosure, no fit, no M_near validity inference below 1e6.',
    }
    print(json.dumps(out, indent=2, sort_keys=True))


def factorial(k):
    result = 1
    for j in range(2, k+1):
        result *= j
    return result


if __name__ == '__main__':
    run()
