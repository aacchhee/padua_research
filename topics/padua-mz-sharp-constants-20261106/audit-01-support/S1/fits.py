"""S1 audit: intercept sensitivity of extrapolation models for y=(log N)^2 lambda_min (MEASURED data
from evidence/S4-essential-cc.json). Diagnostic only; no claim about the true limit."""
import json, sys
import numpy as np
from scipy.optimize import curve_fit

src = sys.argv[1]
d = json.load(open(src))
rows = [(r[0], r[1]) for r in d['rows']]
PI48 = np.pi ** 4 / 8


def data(par, lo, hi):
    N = np.array([n for n, _ in rows if n % 2 == par and lo <= n <= hi], float)
    lam = np.array([l for n, l in rows if n % 2 == par and lo <= n <= hi])
    L = np.log(N)
    return N, L, L ** 2 * lam


def linfit(L, y, cols):
    X = np.column_stack([c(L) for c in cols])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef, np.sqrt(np.mean((X @ coef - y) ** 2))


one = lambda L: np.ones_like(L)
ll = lambda L: np.log(L) / L
inv = lambda L: 1 / L
inv2 = lambda L: 1 / L ** 2
ll2 = lambda L: (np.log(L) / L) ** 2
models = {
    'K1: 1, loglogN/logN, 1/logN': [one, ll, inv],
    '1, 1/L': [one, inv],
    '1, 1/L, 1/L^2': [one, inv, inv2],
    '1, 1/L, 1/L^2, 1/L^3': [one, inv, inv2, lambda L: L ** -3.],
    '1, ll/L, 1/L, 1/L^2': [one, ll, inv, inv2],
    '1, ll/L, 1/L, (ll/L)^2': [one, ll, inv, ll2],
}
windows = {'A 1600-12801': (1600, 12801), 'B 18102-102401': (18102, 102401), 'all >=400': (400, 102401),
           'all >=1600': (1600, 102401)}
out = {}
for par in [0, 1]:
    for wn, (lo, hi) in windows.items():
        N, L, y = data(par, lo, hi)
        for mn, cols in models.items():
            if len(cols) >= len(L):
                continue
            c, rms = linfit(L, y, cols)
            out[f'{"even" if par == 0 else "odd"} | {wn} | {mn}'] = dict(intercept=float(c[0]), rms=float(rms))
        # shifted-log model y = C*(L/(L+s))^2  (lambda ~ C/(log N + s)^2)
        f2 = lambda L, C, s: C * (L / (L + s)) ** 2
        p, _ = curve_fit(f2, L, y, p0=[12, 3])
        out[f'{"even" if par == 0 else "odd"} | {wn} | C(L/(L+s))^2'] = dict(intercept=float(p[0]), s=float(p[1]),
                                                                               rms=float(np.sqrt(np.mean((f2(L, *p) - y) ** 2))))
        f3 = lambda L, C, s, e: C * (L / (L + s)) ** 2 + e / L ** 2
        try:
            p, _ = curve_fit(f3, L, y, p0=[12, 3, 0], maxfev=20000)
            out[f'{"even" if par == 0 else "odd"} | {wn} | C(L/(L+s))^2+e/L^2'] = dict(intercept=float(p[0]), s=float(p[1]),
                                                                                       rms=float(np.sqrt(np.mean((f3(L, *p) - y) ** 2))))
        except Exception as ex:
            out[f'{"even" if par == 0 else "odd"} | {wn} | C(L/(L+s))^2+e/L^2'] = str(ex)

# local effective exponent: if y = C - A/L^q, local slope analysis via 3-point differences in 1/L
N, L, y = data(0, 100, 102401)
x = 1 / L
loc = []
for i in range(1, len(x) - 1):
    # local linear extrapolation in 1/L using neighbours (Richardson-type)
    s = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])
    loc.append((int(N[i]), float(y[i] - s * x[i])))
out['local_linear_in_1/L_extrapolation_even'] = loc
for k, v in out.items():
    print(k, v)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
