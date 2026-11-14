#!/usr/bin/env python3
"""Numerical sanity check of the printed constants (audit X; MEASURED only).

Lambda_c(n) = sum_{B in P_n} |L_B(-1,-1)| from the printed cardinal formula
L_B = w_jk (K_n(z,B) - T_n(z1) T_n(B1)) (paper eq. (6)), nodes eq. (2).
Compared with the printed expansion (5): (4/pi^2) log^2 N + b log N + c - 1/N,
N = n + 1/2, constants (3)-(4). Float64/mpmath; no proof claim.
"""
import math
import sys

import numpy as np



def corner_value(n):
    j = np.arange(n + 1)
    k = np.arange(n + 2)
    theta = j * np.pi / n
    phi = k * np.pi / (n + 1)
    p = np.arange(n + 1)
    nu = np.where(p == 0, 1.0, 2.0)
    sgn = (-1.0) ** p
    A = (nu * sgn)[None, :] * np.cos(np.outer(theta, p))          # A[j,p]
    b = (nu * sgn)[:, None] * np.cos(np.outer(p, phi))           # b[q,k]
    cum = np.cumsum(b, axis=0)                                    # cum[r,k] = sum_{q<=r} b[q,k]
    C = cum[n - p, :]                                             # C[p,k] = sum_{q<=n-p}
    K = A @ C                                                     # K[j,k]
    K -= ((-1.0) ** n * np.cos(n * theta))[:, None]
    eps = np.where((j == 0) | (j == n), 0.5, 1.0)
    eta = np.where((k == 0) | (k == n + 1), 0.5, 1.0)
    w = 2.0 * np.outer(eps, eta) / (n * (n + 1))
    mask = ((j[:, None] + k[None, :]) % 2) == 0
    return float(np.sum(np.abs(w * K)[mask])), float(np.sum((w * K)[mask]))


def kappa():
    """kappa = (8/pi) int_0^1 t^2 cot(pi t/2) sum_{l odd} 1/(l(l^2-t^2)) dt.

    Series via digamma: sum_{l odd} 1/(l(l^2-t^2)) = t^-2 * S(t),
    S(t) = -(1/4)[psi((1-t)/2)+psi((1+t)/2)-2 psi(1/2)]. Gauss-Legendre on (0,1).
    """
    from scipy.special import digamma
    from scipy.integrate import quad

    def integrand(t):
        if t >= 1.0:
            return math.pi / 4
        s = -(digamma((1 - t) / 2) + digamma((1 + t) / 2) - 2 * digamma(0.5)) / 4
        return math.cos(math.pi * t / 2) / math.sin(math.pi * t / 2) * s
    val, err = quad(integrand, 0, 1, epsabs=1e-14, epsrel=1e-14, limit=200)
    # cross-check by direct series at one interior t
    t = 0.37
    direct = sum(1 / (l * (l * l - t * t)) for l in range(1, 200001, 2))
    s = -(digamma((1 - t) / 2) + digamma((1 + t) / 2) - 2 * digamma(0.5)) / 4
    assert abs(direct - s / t ** 2) < 1e-9, (direct, s / t ** 2)
    return (8 / math.pi) * val


def main():
    ka = float(kappa())
    a = 2 / math.pi
    d = 0.5772156649015329 + math.log(8 / math.pi)
    c1 = a * d
    b = 2 * a * c1
    c = c1 ** 2 + ka
    print(f'kappa={ka:.12f} d={d:.12f} b={b:.12f} c={c:.12f}')
    for n in [int(x) for x in sys.argv[1:]] or [10, 11, 50, 51, 100, 101, 200, 201, 400, 401]:
        lam, signed = corner_value(n)
        N = n + 0.5
        L = math.log(N)
        expo = a * a * L * L + b * L + c - 1 / N
        R = lam - expo
        print(f'n={n:4d} Lambda_c={lam:.12f} expansion={expo:.12f} R={R:+.3e} '
              f'R*N^2/logN={R * N * N / L:+.4f} (1/N={1 / N:.3e}) sum L_B={signed:.12f}')


if __name__ == '__main__':
    main()
