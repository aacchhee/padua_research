#!/usr/bin/env python3
"""Independent M2 witness checks; floating results are measurements, not proofs.

The --exact command checks the U witness using rational arithmetic.  The
--measure command evaluates the endpoint-cancelled harmonic U witness by a
Chebyshev mass matrix, without a generalized eigensolver.
"""
import argparse
from fractions import Fraction
import json
import platform


def exact_u(n):
    h = sum((Fraction(1, 2*j-1) for j in range(1, n+1)), Fraction())
    q = Fraction(2) if n % 2 else Fraction(2*n*n, n*n-1)
    ratio = q/(2*h)
    return {"N": n, "U_norm2": str(2*h), "U_Q": str(q),
            "U_RQ_float": float(ratio), "RQ_lt_1_4": ratio < Fraction(1, 4),
            "Hodd8_gt_201_100": sum((Fraction(1, 2*j-1) for j in range(1, 9)), Fraction()) > Fraction(201, 100),
            "exp4_bound": Fraction(11, 4)**4 < Fraction(1025, 17)}


def measure(n):
    import numpy as np
    import scipy
    from scipy.fft import dct
    m = (n-1)//2
    k = np.arange(n+1)
    theta = np.pi*k/n
    moments = np.zeros(2*n+1)
    even = np.arange(0, 2*n+1, 2)
    moments[even] = 2/(1-even.astype(float)**2)
    edge = np.ones(n+1)
    edge[[0, -1]] = 2
    w = dct(moments[:n+1], type=1)/(n*edge)
    u_coeff = np.zeros(n)
    if m:
        r = np.arange(1, m+1)
        u_coeff[n-1-2*r] = 1/r
        u_coeff[n-1] = -np.sum(1/r)+2*m/n
    # U_j = 2(T_j + T_(j-2) + ...) with its T_0 coefficient halved.
    cheb = np.zeros(n)
    for parity in (0, 1):
        idx = np.arange(parity, n, 2)
        cheb[idx] = 2*np.cumsum(u_coeff[idx][::-1])[::-1]
    cheb[0] /= 2
    j = np.arange(n)
    mass = (moments[j[:, None]+j[None, :]]
            +moments[np.abs(j[:, None]-j[None, :])])/2
    norm2 = float(cheb@mass@cheb)
    vals = np.polynomial.chebyshev.chebval(np.cos(theta), cheb)
    vals[[0, -1]] = 0  # exact analytic cancellation, avoid endpoint roundoff.
    q = float(w@(vals*vals))
    harmonic = np.sum(1/np.arange(1, n+2))
    half_harmonic = np.sum(1/np.arange(1, n//2+2))
    h = 2*harmonic-1
    lower = 1/(4*np.pi**2*(np.pi+1)**2*h*(h+2*half_harmonic))
    return {"N": n, "M": m, "Q": q, "norm2": norm2, "RQ": q/norm2 if norm2 else None,
            "RQ_logN2": q/norm2*np.log(n)**2 if norm2 else None,
            "weight_floor_ratio": float(np.min(w*n*n/(1+np.minimum(k,n-k)))),
            "proved_lower_bound": lower, "endpoint_residual_float": float(np.max(np.abs(np.polynomial.chebyshev.chebval(np.array([-1.,1.]), cheb)))),
            "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact", type=int)
    parser.add_argument("--measure", nargs="+", type=int)
    args = parser.parse_args()
    if args.exact:
        print(json.dumps(exact_u(args.exact), sort_keys=True))
    for size in args.measure or []:
        print(json.dumps(measure(size), sort_keys=True))
