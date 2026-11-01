#!/usr/bin/env python3
"""Finite exact kill tests for M3 upper signs and filtered reproduction.

The universal statements have analytic proofs. Optional generalized spectra are
floating MEASURED observations; no source-supplied code is imported.
"""
import argparse
import hashlib
from fractions import Fraction as F
from pathlib import Path


def moment(k):
    return F(0) if k % 2 else F(2, 1 - k * k)


def filter_coefficient(N, n, k):
    ak = abs(k)
    return (F(max(N - ak, 0)) - F(max(n - ak, 0))) / (N - n)


def check(N, n):
    rho = max(F(2 * n, N) - 1, F(0)) ** 2
    for k in range(-n, n + 1):
        assert filter_coefficient(N, n, k) == 1
        for l in range(-(N - 1), N):
            if (k - l) % (2 * N) == 0:
                assert k == l
    assert filter_coefficient(N, n, N) == 0
    for i in range(n + 1):
        for j in range(n + 1):
            s, d = i + j, abs(i - j)
            M = (moment(s) + moment(d)) / 2
            R = (moment(min(s, 2 * N - s)) + moment(d)) / 2
            if 2 * n <= N:
                assert M == R
            elif i != j:
                assert (1 + rho) * M - R <= 0
                if s > N and s % 2 == 0:
                    r = 2 * N - s
                    assert d >= 2 and r > d
                    assert F(d * d - 1, r * r - 1) <= F(d * d, r * r) <= rho


def float_spectrum(N, n):
    import numpy as np
    from scipy.linalg import eigvalsh
    k = np.arange(n + 1)
    S = k[:, None] + k[None, :]
    D = abs(k[:, None] - k[None, :])

    def mu(v):
        out = np.zeros_like(v, dtype=float)
        even = v % 2 == 0
        out[even] = 2 / (1 - v[even].astype(float) ** 2)
        return out

    M = (mu(S) + mu(D)) / 2
    R = (mu(np.minimum(S, 2 * N - S)) + mu(D)) / 2
    values = eigvalsh(R, M)
    C = 12 * (1 + np.pi) ** 4 * (1 + 2 / np.pi)
    lower = (1 - n / N) ** 2 / C
    upper = 1 + max(2 * n / N - 1, 0) ** 2
    return values[0], values[-1], lower, upper


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=25)
    parser.add_argument('--measure', type=int, nargs='*')
    args = parser.parse_args()
    pairs = 0
    for N in range(2, args.max_n + 1):
        for n in range(N):
            check(N, n)
            pairs += 1
    print(f'EXACT: {pairs} pairs, 2<=N<={args.max_n}, 0<=n<N: PASS')
    print('       filter plateau, degree cutoff, no-alias reproduction, upper Z signs and ratio bound.')
    print('script_sha256=' + hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if args.measure is not None:
        import numpy as np
        import scipy
        print(f'MEASURED: numpy={np.__version__}, scipy={scipy.__version__}')
        for N in args.measure:
            for theta in (0.5, 0.6, 0.75, 0.9, 0.95):
                n = min(int(theta * N), N - 1)
                lo, hi, A, B = float_spectrum(N, n)
                print(f'MEASURED: N={N} n={n}: lo={lo:.12g} hi={hi:.12g} lower={A:.12g} upper={B:.12g}')
