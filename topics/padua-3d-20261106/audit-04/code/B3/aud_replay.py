"""Auditor replay of the frozen M/R seeded schedules (own nodes/rank/score; numpy RNG and
scipy Nelder-Mead semantics as registered). Not a producer import."""
import sys, json, math, time
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from alib import modes, rank_mod, split_prime
import aud_mr
from aud_mr import m_nodes, r_nodes, cheb_rank

OUT = sys.argv[1]
_P = {}


def prime_for(L):
    if L not in _P:
        _P[L] = split_prime(L, 1_750_000_000)
    return _P[L]


def score_pts(P, n):
    T = [np.polynomial.chebyshev.chebvander(P[:, j], n) for j in range(3)]
    mo = modes(n)
    V = np.array([T[0][:, a] * T[1][:, b] * T[2][:, c] for a, b, c in mo]).T
    s, d = np.linalg.slogdet(V)
    if not s or not np.isfinite(d):
        return None
    return float(d + sum(sum(x > 0 for x in a) for a in mo) * math.log(2) / 2)


def rational_eval(route, n, key):
    L, A, B = (m_nodes if route == 'M' else r_nodes)(n, key)
    U = sorted(A | B); N = len(modes(n)); assert len(U) == N and not (A & B)
    r, _ = cheb_rank(n, L, U, prime_for(L))
    sc = score_pts(np.cos(2 * np.pi * np.array(U, dtype=float) / L), n) if r == N else None
    return r, sc


def cont_points(route, n, key, phase):
    N = len(modes(n)); q = N - 9
    if route == 'M':
        b, c = key[:2]; L = 4 * q
        A = {tuple(min((2 * k + 1) * g % L, L - (2 * k + 1) * g % L) for g in (1, b, c)) for k in range(2 * q)}
        first = np.cos(2 * np.pi * np.array(sorted(A), dtype=float) / L)
        torus = np.array([[u / 3, v / 3, (u + v) / 3] for u in range(3) for v in range(3)])
    else:
        r, s, b, c = key[:4]; L = 12
        A = {tuple(min(t % L, L - t % L) for t in (4 * u + 2 * v + 1, 2 * v + 1, 4 * r * u + s * (2 * v + 1)))
             for u in range(3) for v in range(6)}
        first = np.cos(2 * np.pi * np.array(sorted(A), dtype=float) / L)
        torus = np.arange(q)[:, None] * np.array([[1, b, c]]) / q
    return np.concatenate([first, np.cos(2 * np.pi * (torus + np.array(phase)))])


def replay(route, n):
    N = len(modes(n)); q = N - 9
    rng = np.random.default_rng(202611070300 + 100 * {'M': 3, 'R': 4}[route] + n)
    valid = [(r, s) for r in (1, 2) for s in range(6)] if route == 'R' else None
    seen = set(); props = []; pos = 0
    while len(seen) < 512:
        mod = 2 * q if route == 'M' else q
        b, c = sorted(int(x) for x in rng.choice(np.arange(1, mod), 2, replace=False))
        ts = [int(x) for x in rng.integers(1, 257, 3)]
        key = ([b, c] + ts) if route == 'M' else list(valid[int(rng.integers(len(valid)))]) + [b, c] + ts
        if tuple(key) in seen:
            continue
        seen.add(tuple(key))
        r, sc = rational_eval(route, n, key)
        if r == N:
            pos += 1
            if sc is not None:
                props.append((key, sc))
    top = sorted(props, key=lambda t: (-t[1], t[0]))[:3]; refined = []
    for key, _ in top:
        start = np.array(key[-3:]) / 257
        def fun(x):
            v = score_pts(cont_points(route, n, key, x), n)
            return -v if v is not None else 1e100
        simplex = np.tile(start, (4, 1)); simplex[1:] += np.eye(3) * 0.025
        opt = minimize(fun, start, method='Nelder-Mead',
                       options={'maxfev': 240, 'initial_simplex': simplex, 'xatol': 1e-9, 'fatol': 1e-9})
        ts = [int(round(float(x) * 257)) % 257 or 1 for x in opt.x]
        nk = key[:-3] + ts
        r, sc = rational_eval(route, n, nk)
        if r == N and sc is not None:
            refined.append((nk, sc, int(opt.nfev)))
    allc = props + [(k, s) for k, s, _ in refined]
    best = max(s for _, s in allc); tied = [t for t in allc if best - t[1] <= 1e-9]
    sel = min(tied, key=lambda t: t[0])
    gaps = sorted({round(s, 12) for _, s in allc}, reverse=True)[:3]
    return {'gaps': [gaps[0] - g for g in gaps[1:]], 'rel_tol_abs': 1e-9 * abs(best), 'positives': pos, 'top3': [t[0] for t in top], 'refined': refined, 'selected': sel[0], 'score': sel[1],
            'tie_count': len(tied)}


def main():
    res = {}; t0 = time.time()
    for route in 'MR':
        for n in range(3, 9):
            res[f'{route}{n}'] = replay(route, n)
            print(route, n, res[f'{route}{n}']['positives'], res[f'{route}{n}']['selected'], res[f'{route}{n}']['score'],
                  [x[2] for x in res[f'{route}{n}']['refined']], round(time.time() - t0), flush=True)
    json.dump(res, open(OUT, 'w'), indent=1)


if __name__ == '__main__':
    main()
