#!/usr/bin/env python3
"""Exact finite checks for PD-N?drift-codex-15 (Claude response-01, E34).

Exact rational arithmetic only (fractions.Fraction, Python standard library);
imports no campaign or audit code.

Record 15 states and proves a fixed-degree lemma: with an exact orthonormal
prefix through degree t, fixed admissible degree-(t+1) raw products v_j and one
source f in v_m with nonzero normal part f_perp=(I-P_{t+1})f, every
projection-only rule gives

    Shat_{t+1} = V_m (+) span{g},  V_m = S_t + span{v_j : j != m},
    g = (1+alpha) w + f_perp,  w = (I-P_{V_m}) v_m,  alpha = <f,w>/|w|^2,
    theta_{t+1}^2 = |f_perp|^2 / ((1+alpha)^2 |w|^2 + |f_perp|^2),
    delta_A(t)^2 = kappa_A^2 theta_{t+1}^2,  kappa_A^2 = <Aw, P_t A w>/|w|^2,
    kappa_{A_m}^2 >= b^2 = |w|^2/|q_parent|^2   (unit-parent value of |w|^2).

This script evaluates both sides on explicit instances.  The theta and delta
values are computed directly from projector matrices of rule outputs (D^4 =
lam D^2 with tr D^2 = 2 lam; G^2 = tr(G) G for G = M^*M), and are compared with
the closed forms above.  It also recomputes the record-15 T_3 constants.  The
sampled rules corroborate, and do not prove, the every-rule span identity; the
proof in the record is analytic.

Inner products are weighted: <u,v> = sum_i w_i u_i v_i on node-value vectors.
This is isometric to the record's coordinates [p]_i = sqrt(w_i) p(z_i), and the
diagonal operators X, Y commute with that isometry, so every projector norm is
unchanged.  Prefix columns are unnormalized exact Gram-Schmidt vectors (leading
monomial coefficient 1); spans, theta and kappa are scale invariant, and b is
reported for a unit parent.

Usage (repository root):
  python3 tracks/bivariate-lanczos/code/drift/e4_closure_check.py \
      --output topics/padua-lanczos-drift-20261101/evidence/response-01-e4-closure.json
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
import platform
import random
import sys
import time


# ---------------------------------------------------------------- linear algebra
def rank(vectors):
    rows = [list(v) for v in vectors]
    if not rows:
        return 0
    r = 0
    for c in range(len(rows[0])):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                fct = rows[i][c] / rows[r][c]
                rows[i] = [a - fct * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def solve(A, b):
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for i in range(n):
            if i != c and M[i][c] != 0:
                fct = M[i][c] / M[c][c]
                M[i] = [a - fct * bb for a, bb in zip(M[i], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


class Space:
    """Weighted inner-product space R^M, <u,v> = sum w_i u_i v_i."""

    def __init__(self, weights):
        self.w = list(weights)
        self.m = len(weights)

    def dot(self, u, v):
        return sum((wi * a * b for wi, a, b in zip(self.w, u, v)), F(0))

    def proj(self, v, basis):
        """Orthogonal projection of v onto span(basis) (basis independent)."""
        G = [[self.dot(a, b) for b in basis] for a in basis]
        c = solve(G, [self.dot(b, v) for b in basis])
        return [sum((c[t] * basis[t][i] for t in range(len(basis))), F(0))
                for i in range(self.m)]

    def projector(self, basis):
        """Matrix of the orthogonal projector onto span(basis)."""
        G = [[self.dot(a, b) for b in basis] for a in basis]
        cols = []
        for j in range(self.m):
            ej = [F(int(i == j)) for i in range(self.m)]
            c = solve(G, [self.dot(b, ej) for b in basis])
            cols.append([sum((c[t] * basis[t][i] for t in range(len(basis))), F(0))
                         for i in range(self.m)])
        return [[cols[j][i] for j in range(self.m)] for i in range(self.m)]

    def adjoint(self, Mt):
        """Weighted adjoint W^{-1} M^T W."""
        return [[Mt[j][i] * self.w[j] / self.w[i] for j in range(self.m)]
                for i in range(self.m)]


def matmul(A, B):
    Bt = list(zip(*B))
    return [[sum((a * b for a, b in zip(r, c)), F(0)) for c in Bt] for r in A]


def msub(A, B):
    return [[a - b for a, b in zip(r, s)] for r, s in zip(A, B)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def diag(v):
    n = len(v)
    return [[v[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def trace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def scal_mat(c, A):
    return [[c * a for a in r] for r in A]


def lin(*terms):
    out = None
    for c, v in terms:
        if out is None:
            out = [c * a for a in v]
        else:
            out = [o + c * a for o, a in zip(out, v)]
    return out


# ---------------------------------------------------------------- polynomials
def monomials(deg):
    """Graded order: degree d, within degree x^(d-j) y^j, j = 0..d."""
    return [(d - j, j) for d in range(deg + 1) for j in range(d + 1)]


def N(deg):
    return (deg + 1) * (deg + 2) // 2


def index(d, j):
    return N(d - 1) + j if d > 0 else 0


# ---------------------------------------------------------------- one instance
def instance(name, points, weights, t, selection, m, source, rng, n_rules=12,
             extra=None):
    """selection: list of length t+2; entry j = 'X' or 'Y' (parent forced by
    admissibility).  source: dict with keys eta (normal part coefficient),
    c_w (coefficient on w), c_V (coefficient on a fixed element of V_m)."""
    sp = Space(weights)
    M = len(points)
    ev = lambda a, b: [F(x) ** a * F(y) ** b for x, y in points]
    X = [F(x) for x, _ in points]
    Y = [F(y) for _, y in points]
    res = {'name': name, 'nodes': M, 't': t, 'perturbed_column': '(%d,%d)' % (t + 1, m),
           'selection_degree_t+1': ''.join(selection)}
    # U(t+1) and room for a normal source
    vand = [ev(a, b) for a, b in monomials(t + 1)]
    assert rank(vand) == N(t + 1), 'U(t+1) fails'
    assert M > N(t + 1)
    res['U(t+1)'] = True
    # exact unnormalized Gram-Schmidt prefix through degree t (graded order)
    pref = []
    for a, b in monomials(t):
        v = ev(a, b)
        if pref:
            v = [vi - pi for vi, pi in zip(v, sp.proj(v, pref))]
        pref.append(v)
    S_t = pref
    S_t1 = [ev(a, b) for a, b in monomials(t + 1)]
    # raw degree-(t+1) products
    raws, parents = [], []
    for j, A in enumerate(selection):
        if A == 'X':
            assert j <= t, 'X inadmissible'
            p = index(t, j)
            raws.append([x * q for x, q in zip(X, pref[p])])
        else:
            assert j >= 1, 'Y inadmissible'
            p = index(t, j - 1)
            raws.append([y * q for y, q in zip(Y, pref[p])])
        parents.append(p)
    assert rank(S_t + raws) == N(t + 1)          # products complete S_{t+1}
    V_m = S_t + [raws[j] for j in range(t + 2) if j != m]
    vm = raws[m]
    w = [a - b for a, b in zip(vm, sp.proj(vm, V_m))]
    w2 = sp.dot(w, w)
    assert w2 > 0
    qp2 = sp.dot(pref[parents[m]], pref[parents[m]])
    b2_unit = w2 / qp2
    # normal direction: normal part of y^(t+2) (as in record 15), else the first
    # other degree-(t+2) monomial with nonzero normal part
    deg_next = monomials(t + 2)[N(t + 1):]
    for a, b in [deg_next[-1]] + deg_next[:-1]:
        c = ev(a, b)
        r = [ci - pi for ci, pi in zip(c, sp.proj(c, S_t1))]
        if any(r):
            res['normal_direction'] = 'normal part of x^%d y^%d w.r.t. S_%d' % (a, b, t + 1)
            break
    r2 = sp.dot(r, r)
    fV = V_m[0]                                     # a fixed element of V_m
    eta, c_w, c_V = source['eta'], source.get('c_w', F(0)), source.get('c_V', F(0))
    f = lin((eta, r), (c_w, w), (c_V, fV))
    f_perp = [a - b for a, b in zip(f, sp.proj(f, S_t1))]
    fp2 = sp.dot(f_perp, f_perp)
    alpha = sp.dot(f, w) / w2
    lam_pred = fp2 / ((1 + alpha) ** 2 * w2 + fp2)
    g = lin((1 + alpha, w), (F(1), f_perp))
    pred = V_m + [g]
    vm_src = [a + b for a, b in zip(vm, f)]
    srcs = list(raws)
    srcs[m] = vm_src

    def run_rule(rr, mode):
        stored = [list(c) for c in S_t]
        for raw in srcs:
            v = list(raw)
            for _ in range(rr.randint(0, 3)):
                for c in stored:
                    if mode == 'random':
                        coef = F(rr.randint(-40, 40), rr.randint(1, 9))
                    elif mode == 'orth':
                        coef = sp.dot(v, c) / sp.dot(c, c)
                    else:
                        coef = F(0)
                    v = [vi - coef * ci for vi, ci in zip(v, c)]
            assert any(v)
            s = F(rr.choice([-1, 1]) * rr.randint(1, 20), rr.randint(1, 20))
            stored.append([s * vi for vi in v])
        return stored

    modes = ['random', 'orth', 'none']
    same = True
    for k in range(n_rules):
        cols = run_rule(random.Random(rng.randint(0, 10 ** 9)), modes[k % 3])
        assert rank(cols) == N(t + 1)            # full column rank
        same &= rank(cols + pred) == N(t + 1)
    assert same
    res['sampled_rules'] = n_rules
    res['all_sampled_rules_full_rank_and_span_equal_to_V_m+span{g}'] = True
    # direct projector computation on one rule output
    cols = run_rule(random.Random(rng.randint(0, 10 ** 9)), 'random')
    Ph = sp.projector(cols)
    P1 = sp.projector(S_t1)
    Pt = sp.projector(S_t)
    D = msub(Ph, P1)
    D2 = matmul(D, D)
    D4 = matmul(D2, D2)
    lam = trace(D2) / 2
    assert D4 == scal_mat(lam, D2)
    assert lam == lam_pred
    I = eye(M)
    out = {}
    for nm, A in (('X', X), ('Y', Y)):
        Mm = matmul(msub(I, Ph), matmul(diag(A), Pt))
        G = matmul(sp.adjoint(Mm), Mm)
        tG = trace(G)
        assert matmul(G, G) == scal_mat(tG, G)   # rank <= 1, so ||M||^2 = tr G
        Aw = [a * b for a, b in zip(A, w)]
        kappa2 = sp.dot(Aw, sp.proj(Aw, S_t)) / w2
        assert tG == kappa2 * lam
        # kappa_A = 0 iff A S_t is contained in V_m
        AS = [[a * b for a, b in zip(A, s)] for s in S_t]
        assert (kappa2 == 0) == (rank(V_m + AS) == len(V_m))
        out[nm] = {'delta_sq': str(tG), 'kappa_sq': str(kappa2),
                   'kappa_sq_over_b_sq_unit_parent': str(kappa2 / b2_unit),
                   'delta_sq_eq_kappa_sq_theta_sq': True}
    creator = selection[m]
    assert F(out[creator]['kappa_sq']) >= b2_unit
    res.update({'b_sq_unit_parent': str(b2_unit), 'normal_part_sq_of_source': str(fp2),
                'alpha': str(alpha), 'theta_sq': str(lam), 'theta_sq_eq_closed_form': True,
                'D4_eq_theta_sq_D2_and_trD2_eq_2theta_sq': True,
                'creating_operator': creator,
                'kappa_creator_sq_ge_b_sq': True,
                'delta_X': out['X'], 'delta_Y': out['Y'],
                'r_sq': str(r2)})
    if extra:
        res.update(extra(locals()))
    return res


# ---------------------------------------------------------------- record-15 extras
def t3_record_extras(L):
    """Record-15 constants: polynomials w, r, b^2, |r|^2, (8) equality, delta_Y."""
    sp, points, w, r = L['sp'], L['points'], L['w'], L['r']
    w_rec = [F(11 * x * x + 26 * x * y - 39 * x + 6 * y * y - 26 * y + 18, 23) for x, y in points]
    r_rec = [F(y ** 3) - F(30, 7) * y * y + F(29, 7) * y - F(6, 35) for x, y in points]
    assert w == w_rec and r == r_rec
    b2 = L['w2']
    assert b2 == F(28, 115) and L['r2'] == F(72, 175) and L['b2_unit'] == b2
    vm = L['vm']
    assert sp.dot(vm, vm) == F(3, 2)
    # V_m equals the record's V = span{1, x, y, x^2, xy+2y^2}
    Vgen = [[F(1)] * len(points), [F(x) for x, y in points], [F(y) for x, y in points],
            [F(x * x) for x, y in points], [F(x * y + 2 * y * y) for x, y in points]]
    assert rank(Vgen) == 5 and rank(L['V_m'] + Vgen) == 5
    # sqrt(3) J q_y = 2 v_21 + (x^2 - 3x + 2y), the last term in V
    extra_t = [F(x * x - 3 * x + 2 * y) for x, y in points]
    assert all(F(x * (x + 2 * y - 3)) == 2 * F(y * (x - 1)) + e for (x, y), e in zip(points, extra_t))
    assert rank(Vgen + [extra_t]) == 5
    lam = L['lam']
    dX2 = F(L['out']['X']['delta_sq'])
    dY2 = F(L['out']['Y']['delta_sq'])
    eps2 = L['eta'] ** 2 * F(72, 175)
    assert lam == eps2 / (b2 + eps2)                       # (7)
    assert dX2 == F(4, 3) * b2 * lam                        # (8) with equality
    assert dY2 == b2 * lam                                  # delta_Y(1) = b theta_2
    return {'record15_polynomials_w_r_match': True, 'V_m_equals_record_V': True,
            'Jq_y_identity_remainder_in_V': True, 'b_sq': str(b2), 'r_sq': '72/175',
            'v21_sq': '3/2', 'eps_sq': str(eps2),
            'eq7_theta_sq_eq_eps_sq_over_b_sq_plus_eps_sq': True,
            'eq8_deltaX_sq_eq_(4/3)b_sq_theta_sq_equality': True,
            'deltaY_sq_eq_b_sq_theta_sq': True}


def ineq9():
    """(9) for eps = u sqrt(3/2): exact closed forms and thresholds."""
    b2 = F(28, 115)
    out = {}
    for u in (F(1, 4), F(1, 10), F(1, 1000)):
        e2 = F(3, 2) * u * u
        th = e2 / (b2 + e2) / (u * u)
        dX = F(4, 3) * b2 * e2 / (b2 + e2) / (u * u)
        dY = b2 * e2 / (b2 + e2) / (u * u)
        assert th == F(345) / (56 + 345 * u * u)
        assert dX == F(112) / (56 + 345 * u * u)
        assert dY == F(84) / (56 + 345 * u * u)
        assert th >= 4 and dX >= 1 and dY >= 1
        out['u=%s' % u] = {'theta_sq/u_sq': str(th), 'deltaX_sq/u_sq': str(dX),
                          'deltaY_sq/u_sq': str(dY)}
    out['thresholds'] = {'theta>=2u iff u^2<=': '121/1380',
                         'deltaX>=u iff u^2<=': '56/345',
                         'deltaY>=u iff u^2<=': '28/345',
                         '1/16 below all three': F(1, 16) <= min(F(121, 1380), F(56, 345), F(28, 345))}
    assert out['thresholds']['1/16 below all three']
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    t0 = time.time()
    rng = random.Random(20261101)
    T3 = [(i, j) for i in range(4) for j in range(4 - i)]
    T4 = [(i, j) for i in range(5) for j in range(5 - i)]
    Q3 = [(i, j) for i in range(4) for j in range(4)]
    uni = lambda P: [F(1, len(P))] * len(P)
    nonuni = [F(1 + i + 2 * j) for i, j in T3]
    nonuni = [c / sum(nonuni) for c in nonuni]
    rpts = []
    rr = random.Random(7)
    while len(rpts) < 12:
        p = (F(rr.randint(-30, 30), rr.randint(1, 7)), F(rr.randint(-30, 30), rr.randint(1, 7)))
        if p not in rpts:
            rpts.append(p)
    rw = [F(rr.randint(1, 9)) for _ in rpts]
    rw = [c / sum(rw) for c in rw]
    BJ2, MIR2 = ['X', 'Y', 'Y'], ['X', 'X', 'Y']
    cases = []
    # record-15 instance: T_3, uniform, BJ, source eta*r in (2,1)
    for eta in (F(1), F(1, 3), F(-7, 2), F(1, 1000)):
        cases.append(instance('T3_uniform_BJ_record15_eta=%s' % eta, T3, uni(T3), 1, BJ2, 1,
                              {'eta': eta}, rng, extra=t3_record_extras))
    # controls: other perturbed columns, mirror, product grid, non-uniform weights
    cases.append(instance('T3_uniform_BJ_source_(2,0)', T3, uni(T3), 1, BJ2, 0, {'eta': F(1)}, rng))
    cases.append(instance('T3_uniform_BJ_source_(2,2)', T3, uni(T3), 1, BJ2, 2, {'eta': F(1)}, rng))
    cases.append(instance('T3_uniform_mirror_source_(2,1)', T3, uni(T3), 1, MIR2, 1, {'eta': F(1)}, rng))
    for m in range(3):
        cases.append(instance('Q3_product_grid_uniform_BJ_source_(2,%d)' % m, Q3, uni(Q3), 1, BJ2, m,
                              {'eta': F(1)}, rng))
    cases.append(instance('T3_nonuniform_weights_BJ_source_(2,1)', T3, nonuni, 1, BJ2, 1, {'eta': F(1)}, rng))
    # general source with components along w and in V_m (alpha != 0), incl. 1+alpha = 0
    cases.append(instance('T3_uniform_BJ_(2,1)_general_source', T3, uni(T3), 1, BJ2, 1,
                          {'eta': F(1, 2), 'c_w': F(-3, 2), 'c_V': F(5)}, rng))
    cases.append(instance('T3_uniform_BJ_(2,1)_source_cancels_w', T3, uni(T3), 1, BJ2, 1,
                          {'eta': F(1, 5), 'c_w': F(-1), 'c_V': F(2)}, rng))
    # degree t = 2 -> 3 on T_4: BJ, mirror and a non-staircase admissible choice
    for sel in (['X', 'Y', 'Y', 'Y'], ['X', 'X', 'X', 'Y'], ['X', 'Y', 'X', 'Y']):
        for m in range(4):
            cases.append(instance('T4_uniform_t2_%s_source_(3,%d)' % (''.join(sel), m), T4, uni(T4), 2,
                                  sel, m, {'eta': F(1)}, rng, n_rules=6))
    # degree t = 0 and t = 1 on 12 random rational nodes with random weights
    for m in range(2):
        cases.append(instance('random12_t0_source_(1,%d)' % m, rpts, rw, 0, ['X', 'Y'], m,
                              {'eta': F(1)}, rng))
    cases.append(instance('random12_t1_BJ_source_(2,1)', rpts, rw, 1, BJ2, 1, {'eta': F(2, 3)}, rng))
    elapsed = time.time() - t0
    with open(__file__, 'rb') as fh:
        code_sha = hashlib.sha256(fh.read()).hexdigest()
    rec = {
        'purpose': 'Exact finite checks of the fixed-degree lemma and T_3 instance in '
                   'PD-N?drift-codex-15 (Claude response-01, E34). Corroboration of an '
                   'analytic proof; sampled rules do not prove the every-rule identity.',
        'command': 'python3 tracks/bivariate-lanczos/code/drift/e4_closure_check.py --output '
                   + args.output,
        'code': 'tracks/bivariate-lanczos/code/drift/e4_closure_check.py',
        'code_sha256': code_sha,
        'python': sys.version.split()[0],
        'platform': platform.platform(),
        'packages': 'none beyond the Python standard library (fractions, random, hashlib, json)',
        'arithmetic': 'exact rationals (fractions.Fraction); no floating point in any assertion',
        'seed': 20261101,
        'record15_ineq9': ineq9(),
        'instances': cases,
        'all_assertions_passed': True,
        'elapsed_seconds': round(elapsed, 2),
    }
    with open(args.output, 'w') as fh:
        json.dump(rec, fh, indent=1)
        fh.write('\n')
    print('PASS: %d instances, %.1f s' % (len(cases), elapsed))


if __name__ == '__main__':
    main()
