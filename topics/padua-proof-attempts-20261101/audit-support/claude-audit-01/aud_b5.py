"""Auditor's independent check of B5 (Claude audit, not Codex code).

Unlike the developer's reduced check (rank of rows 3.. of V^{-1}, which is
N-3 for ANY invertible V), this computes the actual commutant dimension:
the nullity of the full linear system on F supported on the structural
P_y mask, with [A_x, F] = 0 and D F = F^T D (= symmetry of E = S F S^{-1},
S = D^{1/2}), over QQ.  Instances:
  * moment-curve witness (t, t^(n+1)), t = 1..N, w = 1/N, n = 2..5  -> expect 3
  * seeded random rational distinct-x nodes, random rational weights, n = 2..4 -> expect 3
  * Padua n = 2 (rational nodes) -> expect 6 (PD-N?...-04 control)
  * a repeated-x random instance n = 3 (diagnostic only; theorem says nothing)
"""
import json
import random
from fractions import Fraction as Fr

import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ


def mons(n):
    return [(d - b, b) for d in range(n + 1) for b in range(d + 1)]


def mask(n, which):
    ms = mons(n); idx = {m: i for i, m in enumerate(ms)}; N = len(ms)
    pi = []
    for a, b in ms:
        if a + b < n:
            pi.append(idx[(a + 1, b)] if which == 'x' else idx[(a, b + 1)])
        else:
            pi.append(None)
    return [[(pi[j] is None or i <= pi[j]) and (pi[i] is None or j <= pi[i]) for j in range(N)] for i in range(N)]


def monic_pair(xs, ys, ws, n):
    ms = mons(n); N = len(ms)
    V = sp.Matrix([[sp.Rational(x) ** a * sp.Rational(y) ** b for a, b in ms] for x, y in zip(xs, ys)])
    W = sp.diag(*[sp.Rational(w) for w in ws])
    G = V.T * W * V
    # LDL^T by hand (exact)
    L = sp.eye(N); Dg = [0] * N
    for j in range(N):
        Dg[j] = G[j, j] - sum(L[j, k] ** 2 * Dg[k] for k in range(j))
        assert Dg[j] > 0
        for i in range(j + 1, N):
            L[i, j] = (G[i, j] - sum(L[i, k] * L[j, k] * Dg[k] for k in range(j))) / Dg[j]
    P = V * L.T.inv()
    Dm = sp.diag(*Dg)
    assert P.T * W * P == Dm
    X = sp.diag(*[sp.Rational(x) for x in xs]); Y = sp.diag(*[sp.Rational(y) for y in ys])
    Ax = Dm.inv() * P.T * W * X * P
    Ay = Dm.inv() * P.T * W * Y * P
    assert Ax * Ay == Ay * Ax
    return Ax, Ay, Dg


def commutant_dim(Ax, Dg, My):
    N = Ax.shape[0]
    var = [(i, j) for i in range(N) for j in range(N) if My[i][j]]
    col = {v: c for c, v in enumerate(var)}
    rows = []
    # [Ax, F]_{ik} = sum_j Ax_ij F_jk - F_ij Ax_jk
    for i in range(N):
        for k in range(N):
            r = [QQ(0)] * len(var)
            for j in range(N):
                if (j, k) in col and Ax[i, j] != 0:
                    r[col[(j, k)]] += QQ(Ax[i, j].p, Ax[i, j].q)
                if (i, j) in col and Ax[j, k] != 0:
                    r[col[(i, j)]] -= QQ(Ax[j, k].p, Ax[j, k].q)
            if any(r):
                rows.append(r)
    for (i, j) in var:
        if i < j:
            r = [QQ(0)] * len(var)
            r[col[(i, j)]] += QQ(Dg[i].p, Dg[i].q)
            r[col[(j, i)]] -= QQ(Dg[j].p, Dg[j].q)
            rows.append(r)
    M = DomainMatrix(rows, (len(rows), len(var)), QQ)
    return len(var) - M.rank(), len(var)


def in_mask(A, Mk):
    N = A.shape[0]
    return all(A[i, j] == 0 or Mk[i][j] for i in range(N) for j in range(N))


out = []
def run(label, xs, ys, ws, n, expect=None):
    Ax, Ay, Dg = monic_pair(xs, ys, ws, n)
    Mx, My = mask(n, 'x'), mask(n, 'y')
    assert in_mask(Ax, Mx) and in_mask(Ay, My)
    dim, nv = commutant_dim(Ax, Dg, My)
    rec = {"instance": label, "n": n, "N": len(xs), "mask_vars": nv, "commutant_dim": dim,
           "distinct_x": len(set(xs)) == len(xs)}
    if expect is not None:
        assert dim == expect, rec
    out.append(rec); print(rec, flush=True)


for n in range(2, 6):
    N = (n + 1) * (n + 2) // 2
    run("moment-curve", [Fr(t) for t in range(1, N + 1)], [Fr(t ** (n + 1)) for t in range(1, N + 1)], [Fr(1, N)] * N, n, 3)

rng = random.Random(20261101)
for n in range(2, 5):
    N = (n + 1) * (n + 2) // 2
    xs = rng.sample(range(-200, 200), N); xs = [Fr(v, 97) for v in xs]
    ys = [Fr(rng.randint(-200, 200), 89) for _ in range(N)]
    ws = [Fr(rng.randint(1, 50)) for _ in range(N)]; s = sum(ws); ws = [w / s for w in ws]
    run("random-rational distinct x (seed 20261101)", xs, ys, ws, n, 3)

# Padua n = 2 control (expect 6)
xs, ys, ws = [], [], []
cx = {0: Fr(1), 1: Fr(0), 2: Fr(-1)}; cy = {0: Fr(1), 1: Fr(1, 2), 2: Fr(-1, 2), 3: Fr(-1)}
for j in range(3):
    for k in range(4):
        if (j + k) % 2 == 0:
            xs.append(cx[j]); ys.append(cy[k])
            ws.append(Fr(2) * (Fr(1, 2) if j in (0, 2) else 1) * (Fr(1, 2) if k in (0, 3) else 1) / 6)
run("Padua n=2 (control, PD-N04)", xs, ys, ws, 2, 6)

# repeated-x diagnostic, n = 3
N = 10
xs = [Fr(v, 7) for v in [-3, -3, -2, -1, 0, 1, 2, 3, 4, 5]]
ys = [Fr(rng.randint(-50, 50), 13) for _ in range(N)]
ws = [Fr(1, N)] * N
try:
    run("repeated-x diagnostic (two equal x)", xs, ys, ws, 3)
except AssertionError as e:
    out.append({"instance": "repeated-x diagnostic", "error": str(e)})
print(json.dumps(out, indent=1))
