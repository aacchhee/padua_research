"""Auditor-D independent exact checks of D4-01..D4-04 (no repository imports)."""
import json, random, sys
from fractions import Fraction as Q
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from exact_core import nn_exact, check_nn, indices, peval, moments, moment_matrix, det

out = {}

def sh(nu, j, d=1):
    return tuple(v + d * (i == j) for i, v in enumerate(nu))

# ---------- D4-01 Christoffel, own transport derived from the written proof ----------
def transport(co, N, c):
    R = {}
    for nu in indices(N - 1):
        for j in range(2):
            low = sum((co[nu]['a%d' % (s+1)] / R[sh(nu, s, -1), s] for s in range(2) if nu[s]), Q(0))
            R[nu, j] = c - co[nu]['b%d' % (j+1)] - low
            assert R[nu, j] != 0
    new = {}
    for nu in indices(N - 1):
        r = {}
        for j in range(2):
            r['a%d' % (j+1)] = co[nu]['a%d' % (j+1)] * R[nu, j] / R[sh(nu, j, -1), j] if nu[j] else Q(0)
            if sum(nu) == N - 1:
                r['b%d' % (j+1)] = c - R[nu, j]
            else:
                r['b%d' % (j+1)] = co[sh(nu, j)]['b%d' % (j+1)] + R[sh(nu, j), j] - R[nu, j]
        new[nu] = r
    return new, R

rng = random.Random(20261106)
chris = []
for trial in range(40):
    N = rng.randint(2, 6)
    x = sorted(rng.sample(range(-9, 10), N)); x = [Q(v, 3) for v in x]
    W = [[Q(rng.randint(1, 30), rng.randint(1, 7)) for _ in range(N)] for _ in range(2)]
    try:
        P, D, co = nn_exact(x, W)
    except ArithmeticError:
        continue
    check_nn(x, P, co)
    # c: exterior below, exterior above, or interior non-node (non-positive weights)
    kind = trial % 3
    c = (min(x) - Q(rng.randint(1, 9), 4)) if kind == 0 else (max(x) + Q(rng.randint(1, 9), 4)) if kind == 1 else (x[0] + x[-1]) / 2 + Q(1, 97)
    if c in x:
        continue
    Wt = [[(xl - c) * wl for xl, wl in zip(x, w)] for w in W]
    mom_t = [moments(x, w, 2 * N + 1) for w in Wt]
    # determinant identity at every |nu|<=N
    for nu in indices(N):
        A, _ = moment_matrix(mom_t, nu)
        Dt = det(A) if A else Q(1)
        assert Dt == (-1) ** sum(nu) * peval(P[nu], c) * D[nu], nu
    allnz = all(peval(P[nu], c) != 0 for nu in indices(N - 1))
    if not allnz:
        chris.append(dict(N=N, kind=kind, transformed_normal=False)); continue
    Pt, Dt, cot = nn_exact(x, Wt)
    got, R = transport(co, N, c)
    assert got == cot
    for nu in indices(N - 1):  # recursion ratio equals evaluation ratio
        for j in range(2):
            assert R[nu, j] == peval(P[sh(nu, j)], c) / peval(P[nu], c)
    # terminal shared b
    assert all(cot[nu]['b1'] == cot[nu]['b2'] for nu in indices(N - 1) if sum(nu) == N - 1)
    chris.append(dict(N=N, kind=kind, transformed_normal=True, match=True))
out['christoffel_random'] = dict(cases=len(chris), matched=sum(1 for r in chris if r.get('match')),
                                 by_kind={k: sum(1 for r in chris if r['kind'] == k and r.get('match')) for k in range(3)})

# ---------- D4-02 positivity-to-normality counterexample ----------
x = [Q(0), Q(1), Q(2)]
W = [[Q(11), Q(1), Q(1)], [Q(13), Q(2), Q(1)]]
P, D, co = nn_exact(x, W)
ce = dict(D={str(k): str(v) for k, v in D.items()}, P11=[str(v) for v in P[1, 1]])
Wt = [[(xl + 1) * wl for xl, wl in zip(x, w)] for w in W]
mt = [moments(x, w, 7) for w in Wt]
A, _ = moment_matrix(mt, (1, 1))
ce['weights_times_x_plus_1'] = [[str(v) for v in w] for w in Wt]
ce['D11_transformed'] = str(det(A))
ce['transformed_D_all'] = {str(nu): str(det(moment_matrix(mt, nu)[0]) if sum(nu) else 1) for nu in indices(3)}
ce['P11_at_minus1'] = str(peval(P[1, 1], Q(-1)))
# exponential path: weights a^x_l * w, a=e^t. D_nu(a) polynomial in a, degree <= 2|nu|.
def Dpath(a, nu):
    Wa = [[wl * a ** int(xl) for xl, wl in zip(x, w)] for w in W]
    m = [moments(x, w, 7) for w in Wa]
    return det(moment_matrix(m, nu)[0]) if sum(nu) else Q(1)
def interp(nu, deg=8):
    pts = list(range(1, deg + 2))
    # solve Vandermonde exactly
    from exact_core import solve
    V = [[Q(p) ** k for k in range(deg + 1)] for p in pts]
    coef = solve(V, [Dpath(Q(p), nu) for p in pts])
    for p in (Q(1, 3), Q(17, 5), Q(-2)):
        assert sum(cf * p ** k for k, cf in enumerate(coef)) == Dpath(p, nu)
    return coef
import numpy as np
path = {}
astar = 13 ** 0.5 - 2
for nu in indices(3):
    if sum(nu) == 0: continue
    coef = interp(nu)
    roots = np.roots([float(c) for c in reversed(coef)]) if any(coef[1:]) else []
    real = sorted(r.real for r in roots if abs(r.imag) < 1e-9)
    path[str(nu)] = dict(coeffs=[str(c) for c in coef], real_roots=[round(r, 9) for r in real],
                         roots_in_1_to_astar=[round(r, 9) for r in real if 1 < r <= astar + 1e-9],
                         positive_roots=[round(r, 9) for r in real if r > 1e-12])
out['counterexample'] = ce
out['exp_path'] = dict(astar=astar, t_star=float(np.log(astar)), determinants=path)

# ---------- D4-04 Toda: exact derivative by dual numbers ----------
class Dual:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=Q(0)): s.a, s.b = Q(a), Q(b)
    def _c(o): return o if isinstance(o, Dual) else Dual(o)
    def __add__(s, o): o = Dual._c(o); return Dual(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return Dual(-s.a, -s.b)
    def __sub__(s, o): return s + (-Dual._c(o))
    def __rsub__(s, o): return Dual._c(o) - s
    def __mul__(s, o): o = Dual._c(o); return Dual(s.a * o.a, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = Dual._c(o); return Dual(s.a / o.a, (s.b * o.a - s.a * o.b) / (o.a * o.a))
    def __rtruediv__(s, o): return Dual._c(o) / s
    def __eq__(s, o): o = Dual._c(o); return s.a == o.a and s.b == o.b
    def __ne__(s, o): return not s == o
    def __bool__(s): return s.a != 0 or s.b != 0
    def __pow__(s, n):
        r = Dual(1)
        for _ in range(n): r = r * s
        return r
    __hash__ = None

toda = []
for trial in range(25):
    N = rng.randint(2, 5)
    x = [Q(v, 2) for v in sorted(rng.sample(range(-8, 9), N))]
    W0 = [[Q(rng.randint(1, 20), rng.randint(1, 5)) for _ in range(N)] for _ in range(2)]
    try:
        P0, D0, co0 = nn_exact(x, W0)
    except ArithmeticError:
        continue
    Wd = [[Dual(wl, wl * xl) for xl, wl in zip(x, w)] for w in W0]   # d/dt exp(tx)w at t=0
    try:
        _, _, cod = nn_exact(x, Wd)
    except (ArithmeticError, ZeroDivisionError):
        continue
    cod = {nu: {k: (v if isinstance(v, Dual) else Dual(v)) for k, v in r.items()} for nu, r in cod.items()}
    for nu in indices(N - 1):
        S = co0[nu]['a1'] + co0[nu]['a2']
        for j in range(2):
            a, b = 'a%d' % (j+1), 'b%d' % (j+1)
            assert cod[nu][a].a == co0[nu][a] and cod[nu][b].a == co0[nu][b]
            ad = co0[nu][a] * (co0[nu][b] - co0[sh(nu, j, -1)][b]) if nu[j] else Q(0)
            up = sh(nu, j)
            Sup = co0[up]['a1'] + co0[up]['a2'] if sum(up) <= N - 1 else Q(0)
            assert cod[nu][a].b == ad, (nu, j, 'a')
            assert cod[nu][b].b == Sup - S, (nu, j, 'b')
    toda.append(N)
out['toda_dual'] = dict(cases=len(toda), sizes=sorted(set(toda)))

# ---------- D4-03 common-ratio invariant ----------
inv = 0
for trial in range(30):
    N = rng.randint(2, 7)
    W = [[Q(rng.randint(1, 50), rng.randint(1, 9)) for _ in range(N)] for _ in range(2)]
    I0 = [[W[1][l] * W[0][r] / (W[0][l] * W[1][r]) for r in range(N)] for l in range(N)]
    for step in range(5):
        q = [Q(rng.choice([-1, 1]) * rng.randint(1, 9), rng.randint(1, 9)) for _ in range(N)]
        al = [Q(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(2)]
        W = [[al[s] * q[l] * W[s][l] for l in range(N)] for s in range(2)]
    I1 = [[W[1][l] * W[0][r] / (W[0][l] * W[1][r]) for r in range(N)] for l in range(N)]
    assert I0 == I1; inv += 1
# proportional pair: (1,1) singular
x = [Q(0), Q(1), Q(3)]; w = [Q(2), Q(5), Q(7)]
m = [moments(x, w, 3), moments(x, [3 * v for v in w], 3)]
out['ratio_invariant'] = dict(trials=inv, proportional_D11=str(det(moment_matrix(m, (1, 1))[0])))
print(json.dumps(out, indent=1))
