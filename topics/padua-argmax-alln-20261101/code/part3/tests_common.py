"""Float64 helpers for the pre-registered T1--T4 measurements (not proofs).

The diamond kernel is evaluated as U_n(S)U_n(T)+U_(n-1)(S)U_(n-1)(T)
-cos(nu), S=(u+v)/2, T=(u-v)/2.  Validation against the original
coefficient-matrix evaluator is an executed prerequisite, not an enclosure.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize, minimize_scalar

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import maj


def uq(k, t):
    """U_k(cos t), stable near multiples of pi, float64."""
    m = np.rint(t / np.pi).astype(np.int64)
    z = t - m * np.pi
    return ((-1.) ** ((k * m) % 2)) * (k + 1) * np.sinc((k + 1) * z / np.pi) / np.sinc(z / np.pi)


def kernel(n, u, v):
    a, b = (u + v) / 2, (u - v) / 2
    return uq(n, a) * uq(n, b) + uq(n - 1, a) * uq(n - 1, b) - np.cos(n * u)


def divided(n, u, v):
    """Broadcast divided-difference D_n, using rhombus formula near collision."""
    u, v = np.asarray(u), np.asarray(v)
    x, y = np.cos(u), np.cos(v)
    den = y - x
    pu = np.cos((n + 1) * u) + np.cos(n * u)
    pv = np.cos((n + 1) * v) + np.cos(n * v)
    mask = np.abs(den) < 1e-7
    den = np.where(mask, 1., den)
    ans = (pv - pu) / den
    if np.any(mask):
        u, v = np.broadcast_arrays(u, v)
        a, b = (u[mask] + v[mask]) / 2, (u[mask] - v[mask]) / 2
        ans[mask] = uq(n, a) * uq(n, b) + uq(n - 1, a) * uq(n - 1, b)
    return ans


class Edge:
    """PD-T185 two-copy edge evaluator; dimensions O(n^2)."""
    def __init__(self, n):
        self.n = n
        th, ph, self.w, _, _ = maj.setup(n)
        self.th, self.ph = th[:, None], ph[None, :]
        self.tau = (-1.) ** np.arange(n + 1)[:, None]
        self.lc = max(self.one('v+', np.pi), self.one('v-', 0.))

    def one(self, edge, t):
        n = self.n
        if edge[0] == 'v':
            theta = 0. if edge[1] == '+' else np.pi
            g = (divided(n, theta + self.th, t + self.ph)
                 + divided(n, theta + self.th, t - self.ph)) / 2 - np.cos(n * theta) * self.tau
        else:
            phi = 0. if edge[1] == '+' else np.pi
            g = (divided(n, t + self.th, phi + self.ph)
                 + divided(n, t - self.th, phi + self.ph)) / 2 - np.cos(n * t) * self.tau
        return float(np.sum(self.w * np.abs(g)))


class Primitive:
    def __init__(self, n):
        self.n = n
        j, r = np.nonzero((np.arange(n + 1)[:, None] + np.arange(2 * (n + 1))[None, :]) % 2)
        self.u, self.v = j * np.pi / n, r * np.pi / (n + 1)
        self.w = np.where((j == 0) | (j == n), .5, 1.) / (n * (n + 1))
        self.lc = self.one(0.)

    def one(self, s):
        return float(np.dot(self.w, np.abs(kernel(self.n, self.u, self.v + s / (self.n + 1)))))


class Eval:
    def __init__(self, n):
        self.n = n
        th, ph, w, _, _ = maj.setup(n)
        jj, kk = np.nonzero(w)
        self.th, self.ph, self.w = th[jj], ph[kk], w[jj, kk]
        self.lc = max(self.one(0, np.pi)[0], self.one(np.pi, 0)[0])

    def one(self, t, p):
        gs = [kernel(self.n, t + a * self.th, p + b * self.ph)
              for a in (-1, 1) for b in (-1, 1)]
        return (float(np.dot(self.w, np.abs(np.mean(gs, axis=0)))),
                float(np.dot(self.w, np.mean(np.abs(gs), axis=0))))

    def many(self, ts, ps):
        return np.array([self.one(t, p) for t, p in zip(ts, ps)])

    def cellmax(self, j, k, phases=5):
        """Search rectangular half-step box about anti-node (j,k)."""
        n = self.n
        lo = np.maximum([j - .5, k - .5], [0, 0])
        hi = np.minimum([j + .5, k + .5], [n, n + 1])
        q = np.linspace(0, 1, phases)
        starts = [lo + (hi - lo) * [x, y] for x in q for y in q]
        def f(z):
            return -self.one(z[0] * np.pi / n, z[1] * np.pi / (n + 1))[0]
        vals = np.array([f(z) for z in starts])
        best = int(vals.argmin())
        res = minimize(f, starts[best], method='Nelder-Mead', bounds=list(zip(lo, hi)),
                       options={'xatol': 1e-7, 'fatol': 1e-10, 'maxiter': 100})
        return -min(res.fun, vals[best]), res.x - [j, k]


def validate():
    rng = np.random.default_rng(20261101)
    errs = []
    for n in (2, 3, 4, 8, 16):
        e = Eval(n)
        points = rng.uniform(0, np.pi, (8, 2))
        points = np.vstack((points, [[0, np.pi], [0, 0], [np.pi / 2, np.pi / 2]]))
        aa = e.many(points[:, 0], points[:, 1])
        bb = np.array(maj.lam(n, points[:, 0], points[:, 1], maj.setup(n))).T
        errs.append({'n': n, 'max_abs_error': float(np.max(np.abs(aa - bb)))})
    assert max(r['max_abs_error'] for r in errs) < 1e-10
    return errs
