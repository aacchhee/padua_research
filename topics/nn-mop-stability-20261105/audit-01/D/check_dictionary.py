"""Auditor-D independent exact checks of the D6 graph/copy/lattice statements."""
import json, random, sys
from fractions import Fraction as Q
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from exact_core import nn_exact, indices, peval, moments, moment_matrix, det, mop

out = {}
rng = random.Random(6)
# (graph) mixed tests on rho = sum w1 delta_(x, w2/w1) equal the type-II sums, random P
ok = 0
for _ in range(50):
    N = rng.randint(1, 7)
    x = [Q(v, 2) for v in rng.sample(range(-10, 11), N)]
    w1 = [Q(rng.randint(1, 30), rng.randint(1, 6)) for _ in range(N)]
    w2 = [Q(rng.randint(1, 30), rng.randint(1, 6)) for _ in range(N)]
    phi = [b / a for a, b in zip(w1, w2)]
    Pc = [Q(rng.randint(-9, 9)) for _ in range(rng.randint(1, 6))]
    for k in range(6):
        lhs1 = sum(a * xl**k * peval(Pc, xl) for a, xl in zip(w1, x))
        lhs2 = sum(a * xl**k * peval(Pc, xl) for a, xl in zip(w2, x))
        rho1 = sum(a * peval(Pc, xl) * xl**k for a, xl in zip(w1, x))
        rhoy = sum(a * peval(Pc, xl) * (yl * xl**k) for a, xl, yl in zip(w1, x, phi))
        assert lhs1 == rho1 and lhs2 == rhoy
    ok += 1
out['graph_identity_random'] = ok

# (G) explicit instance
x = [Q(v) for v in (0, 1, 2, 3)]; w1 = [Q(1)] * 4; w2 = [Q(v) for v in (1, 2, 4, 8)]
mom = [moments(x, w1, 3), moments(x, w2, 3)]
P = mop(mom, (1, 1))
phi = [b / a for a, b in zip(w1, w2)]
ip = lambda f: sum(a * f(xl, yl) * peval(P, xl) for a, xl, yl in zip(w1, x, phi))
out['G'] = dict(moments_w1=[str(v) for v in mom[0]], moments_w2=[str(v) for v in mom[1]],
               D11=str(det(moment_matrix(mom, (1, 1))[0])), P11=[str(v) for v in P],
               ip_1=str(ip(lambda a, b: 1)), ip_y=str(ip(lambda a, b: b)), ip_x=str(ip(lambda a, b: a)),
               eq2_rhs_check=str(mom[1][0] * P[0] + mom[1][1] * P[1]))
# full-triangle normality of this instance (not claimed by D6; informational)
try:
    nn_exact(x, [w1, w2]); out['G']['full_triangle_normal_through_N'] = True
except ArithmeticError as e:
    out['G']['full_triangle_normal_through_N'] = 'no: %s' % (e.args,)

# (C) two-sheet Gram on Pi_2 singular: q=y^2-y, and Gram rank
pts = [(xl, Q(0), a) for xl, a in zip(x, w1)] + [(xl, Q(1), a) for xl, a in zip(x, w2)]
mons = [lambda X, Y: 1, lambda X, Y: X, lambda X, Y: Y, lambda X, Y: X*X, lambda X, Y: X*Y, lambda X, Y: Y*Y]
G = [[sum(w * f(X, Y) * g(X, Y) for X, Y, w in pts) for g in mons] for f in mons]
q = [0, 0, -1, 0, 0, 1]
out['C'] = dict(Gram_det=str(det(G)), Gq_zero=all(sum(G[i][j] * q[j] for j in range(6)) == 0 for i in range(6)))
# compression of y to diagonal subspace D: weights w1+w2, multiplier w2/(w1+w2)
out['compression_multiplier'] = [str(b / (a + b)) for a, b in zip(w1, w2)]

# (lattice) H1 f = H2 f = x_l f on eigenstates f_l(nu)=P_nu(x_l)
cnt = 0
for _ in range(20):
    N = rng.randint(2, 5)
    xs = [Q(v, 3) for v in sorted(rng.sample(range(-9, 10), N))]
    W = [[Q(rng.randint(1, 20), rng.randint(1, 5)) for _ in range(N)] for _ in range(2)]
    try:
        Pd, D, co = nn_exact(xs, W)
    except ArithmeticError:
        continue
    for xl in xs:
        f = {nu: peval(Pd[nu], xl) for nu in Pd}
        for nu in indices(N - 1):
            for j in range(2):
                up = tuple(v + (i == j) for i, v in enumerate(nu))
                val = f[up] + co[nu]['b%d' % (j+1)] * f[nu] + sum(
                    co[nu]['a%d' % (s+1)] * f[tuple(v - (i == s) for i, v in enumerate(nu))] for s in range(2) if nu[s])
                assert val == xl * f[nu]
    cnt += 1
out['lattice_eigen_cases'] = cnt
print(json.dumps(out, indent=1))
