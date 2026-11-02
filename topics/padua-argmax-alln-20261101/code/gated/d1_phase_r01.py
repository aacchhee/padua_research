"""Small float64 identity sanity check for d1/r01-phase.md; no proof role."""
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


def ufun(k, z):
    # Finite real Fourier sum, including removable values.
    return float(np.cos(np.arange(1-k, k, 2) * z).sum())


def dpoly(n, u, v):
    p = (u+v)/2
    t = (v-u)/2
    return ufun(n+1, p)*ufun(n+1, t) + ufun(n, p)*ufun(n, t)


def run():
    rng = np.random.default_rng(20261102)
    algebra = []
    factor = []
    collisions = []
    for n in (2, 3, 8, 17, 31, 64):
        m = n+1
        for _ in range(80):
            j = int(rng.integers(0, 2*n))
            r = int(rng.integers(0, 2*m))
            if (j+r) % 2 == 0:
                r = (r+1) % (2*m)
            alpha, beta = rng.uniform(-1, 1, 2)
            u, v = (j*np.pi+alpha)/n, (r*np.pi+beta)/m
            lhs = (-1)**j * (dpoly(n, u, v)-np.cos(n*u))
            numerator = ((np.cos(alpha)+np.cos(beta))*(1+np.cos(v))
                         -np.sin(alpha)*np.sin(u)+np.sin(beta)*np.sin(v))
            # Cleared denominator identity remains valid at collisions.
            algebra.append(abs(lhs*(np.cos(u)-np.cos(v))-numerator))
        for h in range(n//3+1):
            for alpha, beta in ((0., 0.), (.02, -.01), (-.01, .03)):
                x, y = (h*np.pi-alpha)/n, (h*np.pi-beta)/m
                X, T = (x+y)/2, (x-y)/2
                V = lambda z: np.cos((2*n+1)*z/2)/np.cos(z/2)
                rhs = (-1)**n * (V(X)*ufun(m, T)+ufun(n, X)*V(T))
                factor.append(abs(dpoly(n, np.pi-x, np.pi-y)-rhs))
        h = 1
        alpha, beta = h*np.pi/m, 0.
        u, v = ((n-h)*np.pi+alpha)/n, (m-h)*np.pi/m
        collisions.append({'n': n, 'alpha': alpha, 'angle_difference': u-v,
                           'finite_G': dpoly(n, u, v)-np.cos(n*u)})
    return {'status': 'MEASURED sanity only; no interval arithmetic or proof role',
            'seed': 20261102, 'python': platform.python_version(),
            'numpy': np.__version__, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'algebra_cases': len(algebra), 'max_cleared_identity_abs_error': max(algebra),
            'collision_factor_cases': len(factor), 'max_factor_abs_error': max(factor),
            'polynomial_collision_values': collisions}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
