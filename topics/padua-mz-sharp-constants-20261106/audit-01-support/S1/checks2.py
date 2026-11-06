"""S1 audit: (i) dense lambda_min replay at small N; (ii) pointwise check of (H);
(iii) higher-order inverse-power fits incl. fixed intercept pi^4/8."""
import json, sys
import numpy as np
from numpy.polynomial import legendre as Lg
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from cc_tools import cc_weights
from trial import make_f
from scipy.integrate import quad

out = {}
# (i) dense replay
src = json.load(open(sys.argv[1]))
meas = {r[0]: r[1] for r in src['rows']}
rep = []
for N in [100, 101, 400, 401, 1600, 1601]:
    x = np.cos(np.arange(N + 1) * np.pi / N)
    w = cc_weights(N)
    V = Lg.legvander(x, N - 1) * np.sqrt((2 * np.arange(N) + 1) / 2)  # orthonormal on [-1,1]
    G = V.T @ (w[:, None] * V)
    lam = np.linalg.eigvalsh(G)[0]
    rep.append(dict(N=N, dense=float(lam), measured=meas[N], rel=float(abs(lam / meas[N] - 1))))
    print(rep[-1], flush=True)
out['dense_replay'] = rep

# (ii) pointwise (H) at N=102400 for f on (0.05,0.95)
N = 102400
L = np.log(N)
f = make_f(0.05, 0.95, 0.05)
k = np.arange(1, N)
k = k[k < N / 2]
a = np.zeros(N + 1)
a[k] = (N / k) * f(np.log(k) / L)
a[N - k] = -a[k]
th_k = np.arange(N + 1) * np.pi / N
F = lambda x: quad(f, 0, x, points=[p for p in (0.05, 0.95) if p < x], limit=400)[0]
ptw = []
for t in [10.3, 50.5, 200.25, 1000.5, 5000.37, 20000.5, 300.0001, 3000.9]:
    th = np.pi * t / N
    p = -np.sin(th) * np.sin(N * th) / N * np.sum(a / (np.cos(th) - np.cos(th_k)))
    lead = 2 * N * L * np.sin(np.pi * t) / (np.pi * t) * F(np.log(t) / L)
    ptw.append(dict(t=t, p=float(p), lead=float(lead), err_times_t_over_N=float((p - lead) * t / N)))
    print(ptw[-1], flush=True)
out['pointwise_H'] = ptw

# (iii) fits
rows = [(r[0], r[1]) for r in src['rows']]
res = {}
for lo in [400, 1600, 18102]:
    Nn = np.array([n for n, _ in rows if n % 2 == 0 and n >= lo], float)
    y = np.array([l for n, l in rows if n % 2 == 0 and n >= lo]) * np.log(Nn) ** 2
    Lv = np.log(Nn)
    for deg in [3, 4, 5]:
        if deg + 1 >= len(Lv):
            continue
        X = np.column_stack([Lv ** -j for j in range(deg + 1)])
        c, *_ = np.linalg.lstsq(X, y, rcond=None)
        res[f'even N>={lo} free c, 1/L^1..{deg}'] = dict(c=float(c[0]), rms=float(np.sqrt(np.mean((X @ c - y) ** 2))))
        X2 = np.column_stack([Lv ** -j for j in range(1, deg + 1)])
        c2, *_ = np.linalg.lstsq(X2, y - np.pi ** 4 / 8, rcond=None)
        res[f'even N>={lo} fixed c=pi^4/8, 1/L^1..{deg}'] = dict(rms=float(np.sqrt(np.mean((X2 @ c2 + np.pi ** 4 / 8 - y) ** 2))))
        for c0 in [13.06114]:
            c3, *_ = np.linalg.lstsq(X2, y - c0, rcond=None)
            res[f'even N>={lo} fixed c=13.06114, 1/L^1..{deg}'] = dict(rms=float(np.sqrt(np.mean((X2 @ c3 + c0 - y) ** 2))))
for k_, v in res.items():
    print(k_, v)
out['inverse_power_fits'] = res
json.dump(out, open(sys.argv[2], 'w'), indent=1)
