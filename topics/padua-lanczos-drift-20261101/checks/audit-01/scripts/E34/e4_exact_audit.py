#!/usr/bin/env python3
"""Independent exact-rational audit of PD-N?drift-codex-15 (Claude audit E34).

Own implementation (fractions only). Does not import campaign code.
Coordinates: node-value coordinates (vector of p(z_i)); the uniform measure
inner product is (1/M) * sum.  Projectors/spans are scale invariant, so the
1/sqrt(10) normalisation and the 1/sqrt(3) in q_y are absorbed into rule
coefficients (the rule class allows arbitrary nonzero scalings).
"""
from fractions import Fraction as F
import random, sys, json

random.seed(20261101)

def dot(u, v): return sum((a*b for a, b in zip(u, v)), F(0))
def sub(u, v, c=F(1)): return [a - c*b for a, b in zip(u, v)]
def scal(c, u): return [c*a for a in u]
def matvec(A, v): return [dot(r, v) for r in A]
def matmul(A, B):
    Bt = list(zip(*B)); return [[dot(r, c) for c in Bt] for r in A]
def transpose(A): return [list(c) for c in zip(*A)]
def eye(n): return [[F(int(i == j)) for j in range(n)] for i in range(n)]
def madd(A, B, c=F(1)): return [[a + c*b for a, b in zip(r, s)] for r, s in zip(A, B)]
def trace(A): return sum((A[i][i] for i in range(len(A))), F(0))

def rank(vectors):
    """exact rank of a list of vectors (rows) by Gaussian elimination"""
    M = [list(v) for v in vectors]
    r = 0; ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f*b for a, b in zip(M[i], M[r])]
        r += 1
    return r

def solve(A, b):
    n = len(A); M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c] / M[c][c]
                M[i] = [a - f*bb for a, bb in zip(M[i], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]

def projector(basis, ip):
    """orthogonal projector (in the inner product ip = (1/M) sum, equivalently
    Euclidean since projector is scale invariant) onto span(basis)."""
    k = len(basis); m = len(basis[0])
    G = [[dot(a, b) for b in basis] for a in basis]
    # P = B G^{-1} B^T ; compute column by column
    P = [[F(0)]*m for _ in range(m)]
    for j in range(m):
        ej = [F(int(i == j)) for i in range(m)]
        rhs = [dot(bv, ej) for bv in basis]
        c = solve(G, rhs)
        col = [sum((c[t]*basis[t][i] for t in range(k)), F(0)) for i in range(m)]
        for i in range(m): P[i][j] = col[i]
    return P

def proj_vec(v, basis):
    G = [[dot(a, b) for b in basis] for a in basis]
    c = solve(G, [dot(b, v) for b in basis])
    return [sum((c[t]*basis[t][i] for t in range(len(basis))), F(0)) for i in range(len(v))]

out = {}

# ---------------- T_3 ----------------
pts = [(i, j) for j in range(4) for i in range(4 - j)]  # ordering irrelevant
M = len(pts); assert M == 10
ev = lambda f: [F(f(x, y)) for x, y in pts]
E = lambda vec: sum(vec, F(0)) / M  # uniform mean
one = ev(lambda x, y: 1); X = ev(lambda x, y: x); Yv = ev(lambda x, y: y)
mom = {'E[x]': E(X), 'E[y]': E(Yv), 'E[x^2]': E([a*a for a in X]),
       'E[y^2]': E([a*a for a in Yv]), 'E[xy]': E([a*b for a, b in zip(X, Yv)])}
assert mom == {'E[x]': 1, 'E[y]': 1, 'E[x^2]': 2, 'E[y^2]': 2, 'E[xy]': F(1, 2)}
out['T3_moments'] = {k: str(v) for k, v in mom.items()}

# U(3): Vandermonde of all 10 monomials of degree <=3 is nonsingular
mons3 = [(a, t - a) for t in range(4) for a in range(t, -1, -1)]  # x^(t-j) y^j
V3 = [[F(x)**a * F(y)**b for (a, b) in mons3] for x, y in pts]
out['T3_U3_vandermonde_rank'] = rank(V3)
assert rank(V3) == 10

# exact degree-one prefix (value coordinates; [p] = p/sqrt(10))
qx = ev(lambda x, y: x - 1)                 # [x-1]
qy_s = ev(lambda x, y: x + 2*y - 3)        # sqrt(3)*[ (x+2y-3)/sqrt3 ]
assert E(qx) == 0 and E(qy_s) == 0 and E([a*b for a, b in zip(qx, qy_s)]) == 0
assert E([a*a for a in qx]) == 1 and E([a*a for a in qy_s]) == 3   # unit norms after /sqrt3
v20 = [x*a for x, a in zip(X, qx)]          # X q_x
v21 = [y*a for y, a in zip(Yv, qx)]         # Y q_x
v22_s = [y*a for y, a in zip(Yv, qy_s)]     # sqrt3 * Y q_y
out['norm2_v21'] = str(E([a*a for a in v21]))
assert E([a*a for a in v21]) == F(3, 2)

S1 = [one, qx, qy_s]
mons2 = [(a, t - a) for t in range(3) for a in range(t, -1, -1)]
S2 = [ev(lambda x, y, a=a, b=b: F(x)**a * F(y)**b) for (a, b) in mons2]
assert rank(S2) == 6
Vgen = [one, X, Yv, ev(lambda x, y: x*x), ev(lambda x, y: x*y + 2*y*y)]
assert rank(Vgen) == 5
# V = S1 + span{v20, v22}
assert rank(S1 + [v20, v22_s]) == 5 and rank(S1 + [v20, v22_s] + Vgen) == 5

# independent w = (I-P_V) v21 and r = normal part of y^3 w.r.t. S2
w_ind = sub(v21, proj_vec(v21, Vgen))
w_rec = ev(lambda x, y: F(11*x*x + 26*x*y - 39*x + 6*y*y - 26*y + 18, 23))
assert w_ind == w_rec
y3 = ev(lambda x, y: y**3)
r_ind = sub(y3, proj_vec(y3, S2))
r_rec = ev(lambda x, y: F(y**3) - F(30, 7)*y*y + F(29, 7)*y - F(6, 35))
assert r_ind == r_rec
b2 = E([a*a for a in w_ind]); r2 = E([a*a for a in r_ind])
out['b2'] = str(b2); out['norm2_r'] = str(r2)
assert b2 == F(28, 115) and r2 == F(72, 175)
assert all(dot(r_ind, s) == 0 for s in S2) and all(dot(w_ind, v) == 0 for v in Vgen)
# table in record15
tab = {(x, y): (23*wv, 35*rv) for (x, y), wv, rv in zip(pts, w_ind, r_ind)}
rec_tab = {(0,0):(18,-6),(1,0):(-10,-6),(2,0):(-16,-6),(3,0):(0,-6),(0,1):(-2,24),
           (1,1):(-4,24),(2,1):(16,24),(0,2):(-10,-36),(1,2):(14,-36),(0,3):(-6,24)}
assert all(tab[k] == (F(a), F(b)) for k, (a, b) in rec_tab.items())
assert sum(a*a for a, _ in rec_tab.values()) == 1288 and sum(b*b for _, b in rec_tab.values()) == 5040
out['record15_table'] = 'all 10 rows match; sums 1288, 5040'
# J q_y identity (times sqrt3): x(x+2y-3) = 2 y(x-1) + (x^2-3x+2y)
Xqy_s = [x*a for x, a in zip(X, qy_s)]
assert Xqy_s == [2*a + b for a, b in zip(v21, ev(lambda x, y: x*x - 3*x + 2*y))]
assert rank(Vgen + [ev(lambda x, y: x*x - 3*x + 2*y)]) == 5

P1 = projector(S1, None); P2 = projector(S2, None)
I = eye(M)

def run_rule(eta, rng, mode):
    """Projection-only rule: degree-two steps, each starting from the raw product
    (only v21 perturbed by eta*r), arbitrary finitely many passes subtracting
    arbitrary combinations of all previously stored columns, then a nonzero scaling."""
    stored = [list(c) for c in S1]
    raws = [v20, [a + eta*b for a, b in zip(v21, r_ind)], v22_s]
    for raw in raws:
        v = list(raw)
        npass = rng.randint(0, 4)
        for _ in range(npass):
            for c in stored:
                if mode == 'random':
                    coef = F(rng.randint(-50, 50), rng.randint(1, 9))
                elif mode == 'orth':  # exact orthogonal projection coefficient
                    coef = dot(v, c) / dot(c, c)
                else:
                    coef = F(0)
                v = sub(v, c, coef)
        s = F(rng.choice([-1, 1]) * rng.randint(1, 30), rng.randint(1, 30))
        stored.append(scal(s, v))
    return stored

results = []
for eta in [F(1), F(1, 3), F(-7, 2), F(1, 1000)]:
    eps2 = eta*eta*r2
    lam = eps2 / (b2 + eps2)
    pred = Vgen + [[a + eta*c for a, c in zip(w_ind, r_ind)]]
    spans_ok = True
    for trial in range(12):
        mode = ['random', 'orth', 'none'][trial % 3]
        cols = run_rule(eta, random.Random(1000*trial + int(eta.numerator) % 997), mode)
        assert rank(cols) == 6
        if rank(cols + pred) != 6: spans_ok = False
    assert spans_ok
    cols = run_rule(eta, random.Random(7), 'random')
    assert rank(cols + S2) == 7       # drifted span differs from S_2
    Ph2 = projector(cols, None)
    D = madd(Ph2, P2, F(-1)); D2 = matmul(D, D); D4 = matmul(D2, D2)
    assert D4 == [[lam*a for a in row] for row in D2] and trace(D2) == 2*lam
    # J = X defect and F = Y defect at degree one, Phat_1 = P_1 exact
    def defect2(A):
        Ad = [[F(0)]*M for _ in range(M)]
        for i in range(M): Ad[i][i] = A[i]
        Mm = matmul(madd(I, Ph2, F(-1)), matmul(Ad, P1))
        G = matmul(transpose(Mm), Mm)
        t = trace(G)
        assert matmul(G, G) == [[t*a for a in row] for row in G]   # rank <= 1 -> ||M||^2 = tr G
        return t
    dX2 = defect2(X); dY2 = defect2(Yv)
    assert dX2 == F(4, 3)*b2*lam and dY2 == b2*lam
    results.append({'eta': str(eta), 'eps2': str(eps2), 'theta2_sq': str(lam),
                    'theta2_sq_eq_eps2/(b2+eps2)': True,
                    'deltaX1_sq': str(dX2), 'deltaX1_sq_eq_(4/3)b2*theta2_sq (bound (8) is equality)': True,
                    'deltaY1_sq': str(dY2), 'deltaY1_sq_eq_b2*theta2_sq': True,
                    'deltaY/deltaX': 'sqrt(3)/2',
                    'all_12_sampled_rules_same_span': True})
out['T3_BJ_v21_source'] = results

# (9): eps = u sqrt(3/2): theta^2/u^2 = (3/2)/(b2 + (3/2)u^2); witness^2/u^2 = 2 b2/(b2+(3/2)u^2)
u = F(1, 4)
th = F(3, 2) / (b2 + F(3, 2)*u*u); wt = 2*b2 / (b2 + F(3, 2)*u*u)
assert th == F(345) / (56 + 345*u*u) and th >= 4 and wt >= 1
out['ineq9_at_u=1/4'] = {'theta2^2/u^2': str(th), 'deltaJ^2/u^2': str(wt)}
# largest u for which theta2>=2u holds: 345 >= 224 + 1380u^2 -> u^2 <= 121/1380
out['ineq9_thresholds'] = {'theta>=2u iff u^2<=': str(F(121, 1380)),
                           'deltaJ>=u iff u^2<=': str(b2 / F(3, 2))}

# --------- genericity controls -----------
def generic_case(points, selection, perturb_index):
    ev2 = lambda f: [F(f(x, y)) for x, y in points]
    m = len(points)
    one_ = ev2(lambda x, y: 1); X_ = ev2(lambda x, y: x); Y_ = ev2(lambda x, y: y)
    # exact (unnormalised) Gram-Schmidt prefix; scaling does not change spans
    qx_ = sub(X_, proj_vec(X_, [one_]))
    qy_ = sub(Y_, proj_vec(Y_, [one_, qx_]))
    S1_ = [one_, qx_, qy_]
    S2_ = [ev2(lambda x, y, a=a, b=b: F(x)**a * F(y)**b) for (a, b) in mons2]
    assert rank(S2_) == 6
    mul = lambda A, v: [a*b for a, b in zip(A, v)]
    if selection == 'BJ':      # (2,0)=X q_x, (2,1)=Y q_x, (2,2)=Y q_y
        raws = [mul(X_, qx_), mul(Y_, qx_), mul(Y_, qy_)]
    elif selection == 'mirror':  # (2,0)=X q_x, (2,1)=X q_y, (2,2)=Y q_y
        raws = [mul(X_, qx_), mul(X_, qy_), mul(Y_, qy_)]
    for mon in [(0, 3), (3, 0), (2, 1), (1, 2)]:
        c = ev2(lambda x, y, a=mon[0], b=mon[1]: F(x)**a * F(y)**b)
        e = sub(c, proj_vec(c, S2_))
        if any(e): break
    raws[perturb_index] = [a + b for a, b in zip(raws[perturb_index], e)]
    cols = S1_ + raws          # zero-pass rule; every projection-only rule has this span
    assert rank(cols) == 6 and rank(cols + S2_) == 7
    Ph2 = projector(cols, None); P1_ = projector(S1_, None); I_ = eye(m)
    res = {'selection': selection, 'perturbed_column': ['(2,0)', '(2,1)', '(2,2)'][perturb_index],
           'normal_direction_from_monomial': 'x^%d y^%d' % mon}
    for nm, A in (('X', X_), ('Y', Y_)):
        Ad = [[F(0)]*m for _ in range(m)]
        for i in range(m): Ad[i][i] = A[i]
        Mm = matmul(madd(I_, Ph2, F(-1)), matmul(Ad, P1_))
        G = matmul(transpose(Mm), Mm)
        t = trace(G)
        assert matmul(G, G) == [[t*a for a in row] for row in G]
        res['delta_%s(1)^2' % nm] = str(t)
        res['delta_%s(1)_float' % nm] = float(t)**0.5
    return res

Q3 = [(i, j) for i in range(4) for j in range(4)]
out['control_Q3_product_grid_BJ_perturb_(2,1)'] = generic_case(Q3, 'BJ', 1)
out['control_T3_BJ_perturb_(2,0)'] = generic_case(pts, 'BJ', 0)
out['control_T3_BJ_perturb_(2,1)_unit-scale-free'] = generic_case(pts, 'BJ', 1)
out['control_T3_BJ_perturb_(2,2)'] = generic_case(pts, 'BJ', 2)
out['control_T3_mirror_perturb_(2,1)'] = generic_case(pts, 'mirror', 1)
print(json.dumps(out, indent=1))
