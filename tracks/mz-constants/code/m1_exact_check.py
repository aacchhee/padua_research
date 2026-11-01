#!/usr/bin/env python3
"""Independent-formula checks for M1; exact rationals unless --float is used.

These checks supplement analytic proofs. They do not constitute a computer proof
of the all-N assertions. No supplied research code is imported.
"""
import argparse
import hashlib
from fractions import Fraction as F
from pathlib import Path


def moment(k):
    return F(0) if k % 2 else F(2, 1 - k * k)


def mass_matrices(N):
    idx = range(N)
    T = [[(moment(i + j) + moment(abs(i - j))) / 2 for j in idx] for i in idx]
    Q = [[(moment(min(i + j, 2 * N - i - j)) + moment(abs(i - j))) / 2
          for j in idx] for i in idx]
    D = [[moment(i + j) - moment(min(i + j, 2 * N - i - j))
          for j in idx] for i in idx]
    return T, Q, D


def check(N):
    T, Q, D = mass_matrices(N)
    b = [F(1, 2)] + [F(1)] * (N - 1)
    for i in range(N):
        for j in range(N):
            assert T[i][j] - Q[i][j] == D[i][j] / 2
            assert D[i][j] >= 0
            if (i + j) % 2 or i + j <= N:
                assert D[i][j] == 0
            else:
                assert D[i][j] > 0
            if i != j:
                assert 2 * T[i][j] - Q[i][j] <= 0
        m = N if N % 2 == i % 2 else N + 1
        k = m - 1
        expected = F(1, k) if i == 0 else F(k, k * k - i * i)
        actual = sum(T[i][j] * b[j] for j in range(N))
        assert actual == expected
        assert actual / b[i] >= F(2 if i == 0 else 1, N)
    if N >= 5:
        i = N // 2
        j = i + 2
        assert D[i][i] == 0 and D[i][j] > 0
        assert D[i][i] * D[j][j] - D[i][j] ** 2 < 0
    # The DCT-I weight bracket's exact elementary lower bound.
    m = (N - 1) // 2
    bracket = F(1) - sum((F(2, 4 * k * k - 1) for k in range(1, m + 1)), F(0))
    if N % 2 == 0:
        bracket -= F(1, N * N - 1)
    assert bracket == (F(1, N) if N % 2 else F(N, N * N - 1))
    assert bracket > 0
    obstruction = F(2) / ((moment(0) + moment(2 * N)) / 2)
    assert obstruction == F(2 * (4 * N * N - 1), 4 * N * N - 2) > 2


def float_check(N):
    import numpy as np
    from scipy.linalg import eigvalsh
    k = np.arange(N)
    S = k[:, None] + k[None, :]
    U = abs(k[:, None] - k[None, :])

    def moments(v):
        out = np.zeros_like(v, dtype=float)
        even = v % 2 == 0
        out[even] = 2 / (1 - v[even].astype(float) ** 2)
        return out

    T = (moments(S) + moments(U)) / 2
    Q = (moments(np.minimum(S, 2 * N - S)) + moments(U)) / 2
    ev = eigvalsh(Q, T)
    return ev[0], ev[-1], 2 - 2 / (np.pi * N)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=40)
    parser.add_argument('--float', dest='floats', nargs='*', type=int)
    args = parser.parse_args()
    for N in range(2, args.max_n + 1):
        check(N)
    _, Q5, _ = mass_matrices(5)
    T5, _, _ = mass_matrices(5)
    A5 = [[2 * T5[i][j] - Q5[i][j] for j in range(5)] for i in range(5)]
    dd = A5[2][2] - sum(abs(A5[2][j]) for j in range(5) if j != 2)
    assert dd == -F(2, 35)
    print(f'EXACT: N=2..{args.max_n}: defect, support/sign, Z-matrix, telescoping floor,')
    print('       weight bracket and full-degree obstruction checks PASS.')
    print(f'EXACT: N=5, row 2 unweighted diagonal-dominance margin = {dd}.')
    print('script_sha256=' + hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if args.floats is not None:
        import numpy as np
        import scipy
        print(f'MEASURED: numpy={np.__version__}, scipy={scipy.__version__}')
        for N in args.floats:
            lo, hi, bound = float_check(N)
            print(f'MEASURED: N={N}: lambda_min={lo:.15g}, lambda_max={hi:.15g}, bound={bound:.15g}')
