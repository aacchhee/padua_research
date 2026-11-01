"""Exact checks for the corrected PD-T?bivariate-lanczos-claude-302(b) and the
scoped refutation PD-N?bivariate-lanczos-claude-309 (response to Codex audit-01,
finding LF-M1).

Independent re-implementation (imports nothing from the audit or the reviewers):
Python integers and fractions.Fraction only; every comparison that involves
sqrt(10) is decided by squaring both (sign-checked) sides.

Setting (the auditor's example, rebuilt here): n = 1, V = Pi_3, ten nodes
(a, b), a, b >= 0 integers, a + b <= 3; the evaluation functionals form a basis
of V* (Vandermonde determinant checked); norm ||sum_i c_i ev_{z_i}|| = ||c||_2,
so ||p||_* = ||(p(z_i))_i||_2, ||1||_* = sqrt(10), ||ev_{z_i}|| = 1, and
C(K_0) is the nonnegative orthant in these coordinates.
Weights: alpha = 1/1000 at t = (1,1), (1 - alpha)/9 elsewhere; mass m = 1.

Parts:
  A  the counterexample numbers (unnormalised vs mass-normalised residual);
  B  extension to positive delta with an explicit rational radius delta'
     (PD-N?...-309 statement);
  C  302(b3): the normalisation factor identity and its bounds;
  D  302(b2): mass-slice inradius r_0, exact threshold (i), fixed-mass residual
     threshold (ii) checked against an exact Euclidean projection onto the
     fixed-mass simplex, and the comparison (iii).
Exit code 0 and 'ALL CHECKS PASS' on success; any failed assertion aborts.
"""
from fractions import Fraction as Fr
import random
import sys


def monomials(d):
    return [(s, k - s) for k in range(d + 1) for s in range(k + 1)]


def mono_val(e, z):
    return Fr(z[0]) ** e[0] * Fr(z[1]) ** e[1]


def solve(A, b):
    """Exact Gauss-Jordan; returns x with A x = b (A square, nonsingular) and det A."""
    n = len(A)
    M = [list(map(Fr, row)) + [Fr(bi)] for row, bi in zip(A, b)]
    det = Fr(1)
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        inv = 1 / M[c][c]
        M[c] = [v * inv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [vr - f * vc for vr, vc in zip(M[r], M[c])]
    return [M[r][n] for r in range(n)], det


def leading_minors(G):
    out = []
    for k in range(1, len(G) + 1):
        sub = [row[:k] for row in G[:k]]
        _, d = solve(sub, [0] * k)
        out.append(d)
    return out


def moment_matrix_deg1(nodes, c):
    basis = [lambda z: Fr(1), lambda z: Fr(z[0]), lambda z: Fr(z[1])]
    return [[sum(ci * f(z) * g(z) for ci, z in zip(c, nodes)) for g in basis] for f in basis]


def sq(v):
    return sum(x * x for x in v)


def simplex_projection_dist2(v, mass):
    """Exact squared Euclidean distance from v to {x >= 0, sum x = mass}."""
    u = sorted(v, reverse=True)
    css, rho, tau = Fr(0), 0, Fr(0)
    for j, uj in enumerate(u, 1):
        css += uj
        t = (css - mass) / j
        if uj - t > 0:
            rho, tau = j, t
    x = [max(vi - tau, Fr(0)) for vi in v]
    assert sum(x) == mass and all(xi >= 0 for xi in x)
    return sq([vi - xi for vi, xi in zip(v, x)]), x


def gt_sqrt10(lhs, coef):
    """Decide lhs > coef*sqrt(10) exactly for Fractions lhs, coef >= 0."""
    assert coef >= 0
    if lhs <= 0:
        return False
    return lhs * lhs > 10 * coef * coef


def main():
    ok = []
    nodes = [(a, t - a) for t in range(4) for a in range(t + 1)]
    mons = monomials(3)
    V = [[mono_val(e, z) for e in mons] for z in nodes]
    _, detV = solve(V, [0] * 10)
    assert detV != 0
    t = nodes.index((1, 1))
    alpha = Fr(1, 1000)
    w = [(1 - alpha) / 9] * 10
    w[t] = alpha
    m = sum(w)
    assert m == 1
    eps = 2 * alpha - alpha ** 2
    theta = Fr(1, 2)
    print('setting: n=1, V=Pi_3, 10 nodes, |det Vandermonde| =', abs(detV), '; m =', m)

    # ---------------- A: counterexample ----------------
    c = list(w)
    c[t] -= eps                       # L_mu + E, E = -eps ev_t, ||E|| = eps, E(1) = -eps
    minors = leading_minors(moment_matrix_deg1(nodes, c))
    assert all(d > 0 for d in minors)
    r0 = min(w)                       # r(0): min of w.v over v >= 0, ||v||_2 = 1
    assert r0 == alpha and r0 > (1 - theta) * eps
    unnorm = -c[t]                    # distance of L_mu+E to the orthant (one negative coordinate)
    assert all(ci >= 0 for i, ci in enumerate(c) if i != t) and c[t] < 0
    assert unnorm == eps - alpha and unnorm <= theta * eps
    sE = m / (m + (-eps))
    norm_dist = sE * unnorm
    assert norm_dist == Fr(1, 999) and norm_dist > theta * eps
    print('A  M_1(L_mu+E) leading minors (basis 1,x,y):', minors)
    print('A  r(0) =', r0, '> (1-theta)eps =', (1 - theta) * eps)
    print('A  (b1) unnormalised dist(L_mu+E, C(K_0)) =', unnorm, '<= theta eps =', theta * eps, ': consistent with (b1)')
    print('A  mass-normalised dist(Lhat, C(K_0)) =', norm_dist, '>', theta * eps, ': old normalised c=1 threshold FAILS')
    ok.append('A')

    # ---------------- B: positive delta (PD-N 309) ----------------
    q, _ = solve(V, [1 if i == t else 0 for i in range(10)])     # Lagrange polynomial at t
    assert all(sum(qk * mono_val(e, z) for qk, e in zip(q, mons)) == (1 if i == t else 0)
               for i, z in enumerate(nodes))
    # |grad q| <= G on the box [-1,4]^2, which contains K_1 (nodes lie in [0,3]^2)
    G = sum(abs(qk) * (e[0] * Fr(4) ** max(e[0] - 1, 0) * Fr(4) ** e[1]
                       + e[1] * Fr(4) ** e[0] * Fr(4) ** max(e[1] - 1, 0)) for qk, e in zip(q, mons))
    Lhat = [ci * sE for ci in c]
    Lhat_q = Lhat[t]                  # Lhat(q) = coordinate t (q(z_i) = delta_it)
    assert Lhat_q == -alpha / (1 - alpha) and sum(Lhat) == m
    # for delta <= 1: p_delta := q + G delta >= 0 on K_delta, Lhat(p_delta) = Lhat(q) + G delta,
    # ||p_delta||_* <= ||q||_* + G delta ||1||_* = 1 + sqrt(10) G delta, and every L' in C(K_delta)
    # has L'(p_delta) >= 0, so dist(Lhat, C(K_delta)) >= (-Lhat(q) - G delta)/(1 + sqrt(10) G delta).
    delta_p = None
    for k in range(1, 30):
        d = Fr(1, 10 ** k)
        lhs = (-Lhat_q - G * d) - theta * eps          # need lhs > theta*eps*sqrt(10)*G*d
        if gt_sqrt10(lhs, theta * eps * G * d):
            delta_p = d
            break
    assert delta_p is not None and delta_p <= 1
    print('B  Lagrange q at (1,1): ||q||_* = 1; gradient bound G on [-1,4]^2 =', G)
    print('B  explicit radius delta\' =', delta_p, ': for every delta in [0, delta\'], dist(Lhat, C(K_delta)) > theta eps')
    ok.append('B')

    # ---------------- C: 302(b3) factor ----------------
    one_star_sq = 10                  # ||1||_*^2
    # s_E in [m/(m+eps*sqrt10), m/(m-eps*sqrt10)]; here s_E = 1/(1-eps) > 1, so the lower bound is trivial
    assert sE > 1 and (1 - eps) > 0
    # upper: 1/(1-eps) <= 1/(1-eps sqrt10)  <=>  eps sqrt10 >= eps
    assert one_star_sq >= 1
    # (b3) upper residual bound: dist(Lhat) <= theta eps m/(m - eps sqrt10) <=> norm_dist(1 - eps sqrt10) <= theta eps
    # <=> norm_dist - theta eps <= norm_dist eps sqrt10
    lhs = norm_dist - theta * eps
    assert lhs > 0 and lhs * lhs <= 10 * (norm_dist * eps) ** 2
    print('C  s_E = m/(m+E(1)) =', sE, '; dist(Lhat) = s_E dist(L_mu+E) exactly; (b3) bound theta eps m/(m - eps||1||_*) holds')
    ok.append('C')

    # ---------------- D: 302(b2) mass-preserving perturbations ----------------
    ones = [Fr(1)] * 10
    Pe = [Fr(9, 10) if i == t else Fr(-1, 10) for i in range(10)]   # P e_t, P = I - 11^T/10
    assert sq(Pe) == Fr(9, 10)
    # r_0(0) = min_i w_i/||P e_i||_2 (concave function on the simplex: min at a vertex); ||P e_i||^2 = 9/10
    r00_sq = min(wi * wi for wi in w) * Fr(10, 9)                   # r_0(0)^2 = 10 alpha^2/9
    assert r00_sq == 10 * alpha ** 2 / 9
    assert r0 * r0 <= r00_sq                                         # (iii) r <= r_0
    # (iii) r >= r_0/(A + B r_0), A = 1 + sqrt10 (e_max = 1), B = sqrt10/alpha, so B r_0 = 10/3 and
    # r_0/(A + B r_0) = alpha (sqrt10/3)/(1 + sqrt10 + 10/3) < alpha (sqrt10/3)/(22/3) <= alpha = r(0)
    # because (sqrt10/3)^2 = 10/9 < (22/3)^2.
    assert Fr(10, 9) < Fr(22, 3) ** 2
    # (i) exact threshold: E* = -r_0 P e_t/||P e_t|| = -(10 alpha/9) P e_t (rational)
    Es = [-(10 * alpha / 9) * x for x in Pe]
    assert sum(Es) == 0 and sq(Es) == r00_sq
    v = [wi + ei for wi, ei in zip(w, Es)]
    assert v[t] == 0 and all(vi >= 0 for vi in v)
    Ebig = [Fr(1001, 1000) * x for x in Es]
    assert sum(w[i] + Ebig[i] for i in range(10)) == m and w[t] + Ebig[t] < 0
    rng = random.Random(302)
    for trial in range(500):
        d = [Fr(rng.randint(-9, 9)) for _ in range(10)]
        mean = sum(d) / 10
        d = [x - mean for x in d]
        if sq(d) == 0:
            continue
        s = Fr(int(float(r00_sq / sq(d)) ** 0.5 * 10 ** 9), 10 ** 9)
        while s * s * sq(d) > r00_sq:
            s -= Fr(1, 10 ** 9)
        assert all(wi + s * di >= 0 for wi, di in zip(w, d))
    # contrast: a general (mass-changing) E of norm r_0 > r(0) leaves the cone
    assert r00_sq > alpha ** 2       # E = -r_0 e_t gives coordinate alpha - r_0 < 0
    print('D(i)  r(0)^2 =', r0 * r0, ' r_0(0)^2 =', r00_sq, ': mass-preserving ball of radius r_0 inside C(K_0)',
          '(boundary attained, 500 random H_0 directions exact-checked); r_0 is not a threshold for general E')
    # (ii) fixed-mass residual threshold, theta = 1/2
    E2 = [2 * x for x in Es]                                          # ||E2|| = 2 r_0: (1-theta)||E2|| = r_0
    approx = [wi + (1 - theta) * ei for wi, ei in zip(w, E2)]
    assert all(a >= 0 for a in approx) and sum(approx) == m
    v2 = [wi + ei for wi, ei in zip(w, E2)]
    d2sq, _ = simplex_projection_dist2(v2, m)
    assert d2sq <= (theta ** 2) * 4 * r00_sq
    E3 = [Fr(101, 100) * x for x in E2]                               # ||E3|| = 2.02 r_0 > r_0/(1-theta)
    v3 = [wi + ei for wi, ei in zip(w, E3)]
    eps3_sq = Fr(101, 100) ** 2 * 4 * r00_sq
    d3sq, _ = simplex_projection_dist2(v3, m)
    assert d3sq > theta ** 2 * eps3_sq
    free3_sq = sum(min(x, Fr(0)) ** 2 for x in v3)                    # free-mass distance to the orthant
    minors3 = leading_minors(moment_matrix_deg1(nodes, v3))
    assert all(dd > 0 for dd in minors3)
    print('D(ii) r_0 = (1-theta)||E2||: fixed-mass dist^2 =', d2sq, '<= (theta||E2||)^2 =', theta ** 2 * 4 * r00_sq)
    print('D(ii) r_0 < (1-theta)||E3||: fixed-mass dist^2 =', d3sq, '> (theta||E3||)^2 =', theta ** 2 * eps3_sq,
          '; M_1 minors', minors3)
    print('D(ii) same E3 with FREE-mass approximants: dist^2 =', free3_sq,
          ('<=' if free3_sq <= theta ** 2 * eps3_sq else '>'), '(theta||E3||)^2 -- mixing conventions loses the exact threshold')
    ok.append('D')
    print('ALL CHECKS PASS:', ','.join(ok))
    return 0


if __name__ == '__main__':
    sys.exit(main())
