#!/usr/bin/env python3
"""A0 arithmetic diagnostic. Floating roots are not certified degree thresholds."""
import json
import math

A = 4 / math.pi**2
B = 8 / math.pi**2 * (0.5772156649015329 + math.log(8 / math.pi))
C0 = 1.846160310423926


def positive_root(a, b, c):
    return (-b + math.sqrt(b*b - 4*a*c)) / (2*a)


def main():
    rows = []
    for radius in (1/64, 1/16):
        for constant in (1.4, 1.45, 1.6, 1.7):
            q = radius**2 / (2 * math.pi**2)
            # log(n+1) <= log(n)+log(3/2), n >= 2.
            conservative = positive_root(q*A, -constant,
                                         -54*q-constant*math.log(1.5))
            # This is only a zero-remainder quadratic diagnostic.
            quadratic = positive_root(q*A, q*B-constant, q*C0)
            # Valid for these small radii; see the analytic phase minimization.
            sharp_q = 2 * math.sin(radius/4)**2
            sharp = positive_root(sharp_q*A, -constant,
                                  -54*sharp_q-constant*math.log(1.5))
            rows.append(dict(radius=radius, hypothetical_C=constant,
                             coarse_leading_log_n=constant/(q*A),
                             coarse_quadratic_log_n=quadratic,
                             coarse_lower_bound_log_n=conservative,
                             sharp_phase_lower_bound_log_n=sharp))
    print(json.dumps(dict(status="floating arithmetic diagnostic; C is hypothetical",
                          rows=rows), indent=2))


if __name__ == "__main__":
    main()
