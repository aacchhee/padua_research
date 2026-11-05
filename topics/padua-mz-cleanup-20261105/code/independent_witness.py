#!/usr/bin/env python3
"""Independent ball-table/IEEE BLAS error-bound check of a dyadic witness.

No eigensolver output is an acceptance premise. See independent-checks-witness.md
for the arithmetic model and the two tensor-product forward-error bounds.
"""
import argparse
import gzip
import hashlib
import json
import platform
import sys
import time
from pathlib import Path

import numpy as np
import scipy
from flint import arb, ctx


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked_float(value, radius):
    value = arb(value)
    out = float(value)
    if not np.isfinite(out) or not abs(value-arb(out)) < radius:
        raise ValueError('ball-to-binary64 table enclosure failed')
    return out


def legendre_table(mesh, n, delta):
    out = np.empty((mesh+1, n+1))
    ctx.prec = 2*n+192
    pi = arb.pi()
    for j in range(mesh+1):
        x = arb(1) if j == 0 else arb(-1) if j == mesh else (pi*j/mesh).cos()
        p0, p1 = arb(1), x
        out[j, 0] = 1
        if n:
            out[j, 1] = checked_float(p1, delta)
        for k in range(1, n):
            p0, p1 = p1, ((2*k+1)*x*p1-k*p0)/(k+1)
            out[j, k+1] = checked_float(p1, delta)
    return out


def cosine_table(mesh, R, delta):
    ctx.prec = 128
    pi = arb.pi()
    out = np.empty((mesh+1, R+1))
    for j in range(mesh+1):
        for a in range(R+1):
            out[j, a] = checked_float((pi*(2*a*j)/mesh).cos(), delta)
    return out


def upward_sum(values):
    """Enclose a nonnegative sum of binary64 entries, using gamma_N."""
    values = np.asarray(values, dtype=float)
    if not np.all(np.isfinite(values)) or np.any(values < 0):
        raise ValueError('nonnegative finite summands required')
    total = float(np.sum(values))
    count = int(values.size)
    u = arb(1)/(1 << 53)
    gamma = count*u/(1-count*u)
    return (arb(total)+count*arb(2)**-1074)/(1-gamma)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--witness', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    start = time.monotonic()
    with gzip.open(args.witness, 'rt') as stream:
        raw = json.load(stream)
    m, n, bits = int(raw['m']), int(raw['n']), int(raw['bits'])
    if m < 2 or n >= m or n < 0 or not 1 <= bits <= 100:
        raise ValueError('invalid dimensions')
    ints = raw['coefficients']
    if len(ints) != (n+1)**2 or any(type(v) is not int for v in ints):
        raise ValueError('expected a dense row-major integer coefficient array')
    if any(v and a+b > n for (a,b),v in zip(np.ndindex(n+1,n+1), ints)):
        raise ValueError('polynomial exceeds the total-degree cutoff')
    if not any(ints):
        raise ValueError('zero polynomial')
    # Integer-to-binary64 rounding has relative error <= u; division by the
    # normal power of two is exact. Cover that coefficient conversion below.
    if any(abs(v).bit_length() > 900 for v in ints):
        raise ValueError('dyadic numerator exceeds supported binary64 range')
    C = np.array(ints, dtype=float).reshape(n+1,n+1)/(2.0**bits)
    ctx.prec = 128
    coefficient_l1 = arb(sum(abs(v) for v in ints))/(1 << bits)
    delta = arb(2)**-48
    A = legendre_table(m, n, delta)
    B = legendre_table(m+1, n, delta)
    table_seconds = time.monotonic()-start
    P = (A @ C) @ B.T
    if not np.all(np.isfinite(P)):
        raise ValueError('nonfinite polynomial evaluation')
    ctx.prec = 128
    u = arb(2)**-53
    gamma = (n+1)*u/(1-(n+1)*u)
    # Standard gamma model for two matrix products, including certified input
    # table error. A generous absolute underflow term covers every scalar op.
    underflow = arb(2)**-1000 * (n+2)**3 * (1+coefficient_l1)
    coefficient_error_l1 = u*coefficient_l1
    p_error = (coefficient_l1+coefficient_error_l1)*(1+delta)**2*(1+gamma)**2-coefficient_l1+underflow

    R = m//2
    X = cosine_table(m, R, delta)
    Y = cosine_table(m+1, R, delta)
    D = np.zeros((R+1,R+1))
    d_l1 = arb(0)
    d_error_l1 = arb(0)
    for a in range(R+1):
        ta = arb(2) if a == 0 else -arb(4)/(4*a*a-1)
        for b in range(R-a+1):
            tb = arb(2) if b == 0 else -arb(4)/(4*b*b-1)
            value = ta*tb
            if m % 2 == 0 and a == R and b == 0:
                value -= arb(4)/(1-m*m)
            f = float(value)
            D[a,b] = f
            d_l1 += abs(value)
            d_error_l1 += abs(value-arb(f))
    kernel = (X @ D) @ Y.T
    g = (R+1)*u/(1-(R+1)*u)
    kernel_error = (d_l1+d_error_l1)*(1+delta)**2*(1+g)**2-d_l1
    kernel_error += arb(2)**-1000*(R+2)**3*(1+d_l1)
    # Floating scale, endpoints and parity are performed independently here.
    rho_exact = arb(2)/(m*(m+1))
    rho = float(rho_exact)
    scale_error = abs(rho_exact-arb(rho))
    weights = kernel*rho
    weights[[0,-1],:] *= 0.5
    weights[:,[0,-1]] *= 0.5
    keep = (np.arange(m+1)[:,None]+np.arange(m+2)[None,:]) % 2 == 0
    weights[~keep] = 0
    # |kernel| <= ||D||_1; endpoint factors cannot amplify the error.
    w_error = rho_exact*kernel_error + scale_error*(d_l1+kernel_error)
    w_error += u*abs(arb(rho))*(d_l1+kernel_error)+arb(2)**-1000

    # All summands below use ordinary binary64. Their nonnegative upper sums
    # include product rounding and sequential-sum gamma bounds in Arb.
    count = int(np.count_nonzero(keep))
    p = P[keep]
    w = weights[keep]
    abs_wp = upward_sum(np.abs(w)*np.abs(p))/(1-u)
    abs_w = upward_sum(np.abs(w))
    p2 = upward_sum(p*p)/(1-u)
    abs_p = upward_sum(np.abs(p))
    q_terms = w*p*p
    q_float = float(np.sum(q_terms))
    abs_terms = upward_sum(np.abs(q_terms))/(1-u)**2
    sum_gamma = (count+3)*u/(1-(count+3)*u)
    q_round = sum_gamma*abs_terms+arb(2)**-1000*(count+1)
    q_error = q_round + 2*p_error*abs_wp+p_error*p_error*abs_w
    q_error += w_error*(p2+2*p_error*abs_p+count*p_error*p_error)
    enclosure = arb(q_float) + arb(0, q_error.abs_upper())
    # A nonzero rational Legendre coefficient proves positive continuous norm.
    # Display one exact positive summand; no expensive full rational norm needed.
    at = next(i for i,c in enumerate(ints) if c)
    aa, bb = divmod(at,n+1)
    norm_lower = arb(4)*ints[at]**2/((1 << (2*bits))*(2*aa+1)*(2*bb+1))
    accepted = bool(enclosure < 0 or enclosure > 0)
    if not accepted:
        raise ValueError(f'sign enclosure straddles zero: {enclosure}')
    report = dict(status='rigorous forward-error sign enclosure under stated IEEE BLAS model',
        accepted=True, sign='negative' if enclosure < 0 else 'positive',m=m,n=n,
        witness_sha256=digest(args.witness), code_sha256=digest(__file__),
        command=sys.argv, python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        q_center=q_float,q_enclosure=str(enclosure),q_absolute_error=str(q_error),
        relative_width_upper=str(2*q_error/abs(enclosure)),
        polynomial_error_max=str(p_error),weight_error_max=str(w_error),
        coefficient_l1=str(coefficient_l1),positive_norm_summand_lower=str(norm_lower),
        retained_nodes=count,ball_table_seconds=table_seconds,total_seconds=time.monotonic()-start,
        arithmetic_assumptions=['Arb outward intervals','binary64 round-to-nearest scalar operations',
            'each BLAS dot product satisfies standard gamma_k error model; FMA permitted',
            'no overflow; absolute underflow allowance included'],
        independent_path='ball node tables plus floating tensor contractions with analytic l1 forward bounds')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)


if __name__ == '__main__':
    main()
