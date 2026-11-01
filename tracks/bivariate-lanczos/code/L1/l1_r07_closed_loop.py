"""R07 (IDEA?bivariate-lanczos-claude-120): closed-loop dot-product rounding as the sole error source.
BJ recurrence (block window, CGS) in long double; each coefficient h_{k,l} := long-double inner product
+ u sum_i eps_i q_{i,l} u0_i (eps iid N(0,1), u = 2^-52); everything else long double.  Compared with the
double BJ loss.  MEASURED only.  Usage: python3 -I l1_r07_closed_loop.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_r04_checkerboard as C

LD = np.longdouble
EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2
DEG = (8, 12, 16, 20, 24)


def closed_loop(x, y, w, nmax, seed):
    idx, pos, parent, op, start = L.tables(nmax); N = len(idx); M = len(x)
    xl, yl = x.astype(LD), y.astype(LD); rng = np.random.default_rng(300 + seed)
    Q = np.zeros((M, N), dtype=LD); v = np.sqrt(w.astype(LD)); Q[:, 0] = v / np.sqrt(np.sum(v * v))
    for k in range(1, N):
        p = parent[k]; a = xl if op[k] == 'J' else yl
        u0 = a * Q[:, p]; W = L.window(k, idx, start, 'block'); Qw = Q[:, W]
        terms = Qw.T * u0[None, :]
        h = np.sum(terms, axis=1) + LD(EPS) * np.sum(rng.standard_normal(terms.shape).astype(LD) * terms, axis=1)
        u = u0 - Qw @ h; Q[:, k] = u / np.sqrt(np.sum(u * u))
    G = Q.T @ Q
    return {n: float(np.abs(G[:Nof(n), :Nof(n)] - np.eye(Nof(n), dtype=LD)).max()) for n in DEG}


def run(name, X, Y, nmax=24, seeds=(0, 1, 2)):
    P, w, wx, wy = C.checkerboard(X, Y); x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, _, _ = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    G = Q.T @ Q; loss = {n: float(np.abs(G[:Nof(n), :Nof(n)] - np.eye(Nof(n))).max()) for n in DEG}
    Qn, _, _ = L.recurrence(x, y, w, nmax, win='block', orth='cgs', dtype=LD)
    Gn = Qn.T @ Qn; ldloss = {n: float(np.abs(Gn[:Nof(n), :Nof(n)] - np.eye(Nof(n), dtype=LD)).max()) for n in DEG}
    res = [closed_loop(x, y, w, nmax, sd) for sd in seeds]
    cl = {n: float(np.median([r[n] for r in res])) for n in DEG}
    print(f"== {name} (M={len(x)})", flush=True)
    for lab, d in [('BJ double L(n)', loss), ('closed loop C(n)', cl), ('BJ long double', ldloss)]:
        print(f"   {lab:17s} " + " ".join(f"n{n}:{v:.2e}" for n, v in d.items()), flush=True)
    print("   ratio C/L         " + " ".join(f"n{n}:{cl[n] / loss[n]:.2f}" for n in DEG), flush=True)
    return loss, cl


if __name__ == '__main__':
    print(f"# l1_r07_closed_loop.py numpy={np.__version__}")
    out = {}
    for name, m, f in [('cubic s|s|^2, m=30', 30, lambda s: s * np.abs(s) ** 2),
                       ('equispaced, m=30', 30, lambda s: s),
                       ('quadratic s|s|, m=30', 30, lambda s: s * np.abs(s)),
                       ('quartic s|s|^3, m=30', 30, lambda s: s * np.abs(s) ** 3),
                       ('cubic s|s|^2, m=36', 36, lambda s: s * np.abs(s) ** 2),
                       ('Chebyshev-Lobatto, m=30', 30, None)]:
        if f is None:
            X, Y = np.cos(np.pi * np.arange(m + 1) / m), np.cos(np.pi * np.arange(m + 2) / (m + 1))
        else:
            X, Y = f(np.linspace(-1, 1, m + 1)), f(np.linspace(-1, 1, m + 2))
        out[name] = run(name, X, Y)
    verdicts = []
    for name, (loss, cl) in out.items():
        if loss[20] >= 1e-13:
            r = [cl[n] / loss[n] for n in (16, 20)]
            v = 'killed' if any(x < 0.02 or x > 50 for x in r) else ('survives' if all(0.2 <= x <= 5 for x in r) else 'inconclusive')
        else:
            v = 'survives' if cl[20] < 1e-12 else ('killed' if cl[20] >= 1e-11 else 'inconclusive')
        verdicts.append(v); print(f"   verdict on {name}: {v}")
    order = {'survives': 0, 'inconclusive': 1, 'killed': 2}
    print(f"# overall (worst over sets): {max(verdicts, key=order.get)}")
