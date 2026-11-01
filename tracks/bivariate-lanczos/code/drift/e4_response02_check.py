#!/usr/bin/env python3
"""Response-02 (Claude) regression check for PD-N?drift-codex-15, audit-02 A02-M1.

Exact rational arithmetic only (fractions.Fraction, Python standard library).
Imports no campaign or audit code.  It does not modify, import or re-run
e4_closure_check.py, whose hash is pinned in response-01 evidence.

Claim checked (record 15, Negative statement, as corrected in response-02).
Unit normal source f = eps*e, e orthogonal to S_(t+1), relative size
eps = u*||v_m|| (v_m is the raw product of a unit parent).  Then, for every
rule in the class R and both A in {X, Y},

    (delta_A(t)/u)^2 = kappa_A^2 ||v_m||^2 / (b^2 + u^2 ||v_m||^2),          (*)
    lim_{u->0} (delta_A(t)/u)^2 = (kappa_A^2 / b^2) ||v_m||^2 =: L_A^2,

and kappa_(A_m) >= b, so L_(A_m) >= ||v_m||, with equality iff kappa_(A_m) = b.
The response-01 wording asserted L_(A_m) = ||v_m|| for every instance.

For every instance the script computes
  (1) the closed-form ingredients b^2, kappa_X^2, kappa_Y^2, ||v_m||^2 and the
      limits L_X^2, L_Y^2, from w = (I - P_(V_m)) v_m and P_t A w only;
  (2) independently of those closed forms, delta_A(t)^2 directly from the
      projector of the completed span V_m + span{v_m + eta r} (the span every
      rule in R produces, record 15 (b); one deterministic non-orthogonal
      two-pass rule with rescaling is run at each eta and its stored columns
      are asserted to have full rank and this span), at several exact rational eta, as
      lambda_max of the rank-one generalized Gram matrix of (I - Phat) A on the
      orthogonal prefix (rank <= 1 asserted exactly, so lambda_max = trace);
  (3) u^2 = eta^2 ||r||^2 / ||raw_m||^2 (exact; u itself need not be rational)
      and asserts (*) exactly at each eta;
  (4) the limit from the direct values alone: 1/(delta/u)^2 is asserted to be
      affine in u^2 on all sample points, and its value at u^2 = 0
      (extrapolated from the two smallest samples) is asserted to equal L_A^2;
  (5) the gaps L_A^2 - (delta_A/u)^2, asserted positive, decreasing to 0 and
      bounded by L_A^2 * u^2 ||v_m||^2 / b^2;
  (6) kappa_(A_m)^2 >= b^2, and whether the old assertion L_(A_m)^2 = ||v_m||^2
      holds (it holds iff kappa_(A_m)^2 = b^2).
Record-15 constants are asserted: T_3/BJ source in v_21 (kappa_Y = b, limits
3/2 for Y and 2 for X, matching (9)'s closed forms 84/(56+345u^2) and
112/(56+345u^2)); source in v_20 (||v_20||^2 = 22/5, b^2 = 7/15,
kappa_X^2 = 28/45, L_X^2 = 88/15, and audit-02's symbolic formula
delta_X^2 = 672 eta^2/(5(216 eta^2 + 245)) at every sample eta).

The finite checks corroborate the analytic proof in record 15; they are not a
proof of the universally quantified lemma.

Inner products are weighted node-value products <a,b> = sum_i w_i a_i b_i,
isometric to the record's sqrt(w_i)-scaled coordinates; X, Y commute with that
isometry.  Prefix columns are unnormalized exact Gram-Schmidt vectors (leading
monomial coefficient 1).  Scale-invariant quantities (kappa^2, u, limits) do
not depend on this; b^2 and ||v_m||^2 are reported for a unit parent.

Usage (repository root):
  PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 \
  python3 -B tracks/bivariate-lanczos/code/drift/e4_response02_check.py \
      --output topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
import os
import platform
import random
import sys
import time

CODE = 'tracks/bivariate-lanczos/code/drift/e4_response02_check.py'
R01_EVIDENCE = 'topics/padua-lanczos-drift-20261101/evidence/response-01-e4-closure.json'
ETAS = (F(1, 10), F(1, 100), F(-1, 1000), F(1, 10 ** 4), F(1, 10 ** 6))


# ------------------------------------------------------------ exact linear algebra
def solve(A, rhs):
    """Solve A x = rhs (A square, nonsingular) by exact Gauss-Jordan elimination."""
    n = len(A)
    M = [list(A[i]) + [rhs[i]] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for i in range(n):
            if i != c and M[i][c] != 0:
                fct = M[i][c] / M[c][c]
                M[i] = [a - fct * b for a, b in zip(M[i], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


def rank(vectors):
    rows = [list(v) for v in vectors]
    r = 0
    for c in range(len(rows[0]) if rows else 0):
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


class Space:
    def __init__(self, weights):
        self.w = list(weights)

    def dot(self, a, b):
        return sum((wi * x * y for wi, x, y in zip(self.w, a, b)), F(0))

    def projector_onto(self, basis):
        """Return a function x -> orthogonal projection of x onto span(basis)."""
        G = [[self.dot(a, b) for b in basis] for a in basis]
        n = len(basis)
        # exact inverse of the Gram matrix, column by column
        inv_cols = [solve(G, [F(int(i == j)) for i in range(n)]) for j in range(n)]
        Ginv = [[inv_cols[j][i] for j in range(n)] for i in range(n)]

        def proj(x):
            rhs = [self.dot(b, x) for b in basis]
            c = [sum((Ginv[i][j] * rhs[j] for j in range(n)), F(0)) for i in range(n)]
            return [sum((c[k] * basis[k][i] for k in range(n)), F(0)) for i in range(len(x))]
        return proj


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def hadamard(a, b):
    return [x * y for x, y in zip(a, b)]


# ------------------------------------------------------------ polynomial data
def monomials(deg):
    return [(d - j, j) for d in range(deg + 1) for j in range(d + 1)]


def N(deg):
    return (deg + 1) * (deg + 2) // 2


def index(d, j):
    return N(d - 1) + j if d > 0 else 0


def short(x):
    """Exact string, or float plus digest if the exact string is long."""
    s = str(x)
    if len(s) <= 120:
        return s
    return {'float': '%.17g' % float(x), 'exact_sha256': hashlib.sha256(s.encode()).hexdigest(),
            'exact_len': len(s)}


# ------------------------------------------------------------ one instance
def instance(name, points, weights, t, selection, m, normal_monomial=None):
    sp = Space(weights)
    M = len(points)
    ev = lambda a, b: [F(x) ** a * F(y) ** b for x, y in points]
    ops = {'X': [F(x) for x, _ in points], 'Y': [F(y) for _, y in points]}
    assert rank([ev(a, b) for a, b in monomials(t + 1)]) == N(t + 1), 'U(t+1) fails'
    assert M > N(t + 1)
    # exact orthogonal (unnormalized) Gram-Schmidt prefix through degree t
    pref = []
    for a, b in monomials(t):
        v = ev(a, b)
        if pref:
            v = sub(v, sp.projector_onto(pref)(v))
        pref.append(v)
    pref_n2 = [sp.dot(p, p) for p in pref]
    # admissible raw products
    raws, parents = [], []
    for j, A in enumerate(selection):
        p = index(t, j) if A == 'X' else index(t, j - 1)
        assert (A == 'X' and j <= t) or (A == 'Y' and j >= 1), 'inadmissible'
        raws.append(hadamard(ops[A], pref[p]))
        parents.append(p)
    assert rank(pref + raws) == N(t + 1)
    creator = selection[m]
    raw_m = raws[m]
    raw2 = sp.dot(raw_m, raw_m)
    par2 = pref_n2[parents[m]]
    V_m = pref + [raws[j] for j in range(t + 2) if j != m]
    w = sub(raw_m, sp.projector_onto(V_m)(raw_m))
    w2 = sp.dot(w, w)
    assert w2 > 0
    # closed-form ingredients (scale-invariant kappa^2; unit-parent b^2, ||v_m||^2)
    proj_t = sp.projector_onto(pref)
    kappa2 = {}
    for nm, A in ops.items():
        Aw = hadamard(A, w)
        PAw = proj_t(Aw)
        kappa2[nm] = sp.dot(PAw, PAw) / w2
    b2 = w2 / par2
    v2 = raw2 / par2
    L2 = {nm: kappa2[nm] * raw2 / w2 for nm in ops}      # = kappa^2 ||v_m||^2 / b^2
    assert L2[creator] == kappa2[creator] * v2 / b2
    assert kappa2[creator] >= b2                          # creator bound kappa_(A_m) >= b
    # a normal direction r (normal part of a degree-(t+2) monomial w.r.t. S_(t+1))
    S_t1 = [ev(a, b) for a, b in monomials(t + 1)]
    proj_t1 = sp.projector_onto(S_t1)
    cand = monomials(t + 2)[N(t + 1):]
    order = [normal_monomial] if normal_monomial else [cand[-1]] + cand[:-1]
    for a, bexp in order:
        c = ev(a, bexp)
        r = sub(c, proj_t1(c))
        if any(r):
            normal_label = 'normal part of x^%d y^%d w.r.t. S_%d' % (a, bexp, t + 1)
            break
    r2 = sp.dot(r, r)
    assert all(sp.dot(r, s) == 0 for s in S_t1)
    # direct evaluation of delta_A(t)^2 from the completed span, at exact eta
    others = [raws[j] for j in range(t + 2) if j != m]
    samples = []
    direct = {nm: [] for nm in ops}                      # exact (u^2, (delta/u)^2) from projectors
    for eta in ETAS:
        col = [a + eta * b for a, b in zip(raw_m, r)]
        # one deterministic rule in R (reverse creation order, two passes of
        # non-orthogonal rational subtractions, nonzero rescaling) has the same span
        inputs = list(raws)
        inputs[m] = col
        stored = [list(p) for p in pref]
        for pos, j in enumerate(reversed(range(t + 2))):
            v = list(inputs[j])
            for run in range(2):
                for k, q in enumerate(stored):
                    c = F((-1) ** (k + run) * (k + 2), pos + run + 3)
                    v = [vi - c * qi for vi, qi in zip(v, q)]
            assert any(v)
            stored.append([F((-1) ** pos * (pos + 2), pos + 1) * vi for vi in v])
        assert rank(stored) == N(t + 1) and rank(stored + pref + others + [col]) == N(t + 1)
        proj_hat = sp.projector_onto(pref + others + [col])
        u2 = eta * eta * r2 / raw2                       # ||eta r|| = u ||raw_m||
        rec = {'eta': str(eta), 'u_sq': short(u2)}
        dsq = {}
        for nm, A in ops.items():
            # Z_i = (I - Phat) A p_i on the orthogonal prefix; delta^2 = lambda_max(B^-1 G)
            Z = []
            for p in pref:
                Ap = hadamard(A, p)
                Z.append(sub(Ap, proj_hat(Ap)))
            n = len(pref)
            G = [[sp.dot(Z[i], Z[j]) for j in range(n)] for i in range(n)]
            K = [[G[i][j] / pref_n2[i] for j in range(n)] for i in range(n)]   # B^-1 G
            tr = sum((K[i][i] for i in range(n)), F(0))
            K2 = [[sum((K[i][k] * K[k][j] for k in range(n)), F(0)) for j in range(n)]
                  for i in range(n)]
            assert all(K2[i][j] == tr * K[i][j] for i in range(n) for j in range(n)), 'rank > 1'
            delta2 = tr
            ratio = delta2 / u2
            dsq[nm] = delta2
            direct[nm].append((u2, ratio))
            closed = kappa2[nm] * raw2 / (w2 + u2 * raw2)    # (*) in scale-free form
            assert ratio == closed, (name, nm, str(eta))
            gap = L2[nm] - ratio
            if kappa2[nm] > 0:
                assert gap > 0
                assert gap <= L2[nm] * u2 * v2 / b2
            else:
                assert delta2 == 0 and gap == 0
            rec[nm] = {'delta_sq': short(delta2), 'delta_sq_over_u_sq': short(ratio),
                       'limit_minus_value': short(gap), 'equals_closed_form_exactly': True}
        if name == 'T3_uniform_BJ_source_(2,0)':
            # audit-02 E34 symbolic witness, source eta*[normal part of y^3]
            assert dsq['X'] == F(672) * eta * eta / (5 * (216 * eta * eta + 245))
            rec['X']['equals_audit02_symbolic_672eta2_over_5(216eta2+245)'] = True
        if name.startswith('T3_uniform_BJ_source_(2,1)'):
            rr = 1 / (56 + 345 * u2)
            assert dsq['Y'] / u2 == 84 * rr
            assert dsq['X'] / u2 == 112 * rr
            rec['matches_record15_eq9_closed_forms_84_and_112_over_(56+345u^2)'] = True
        samples.append((u2, rec))
    # the limit from the direct projector values alone, and monotone convergence
    extrap = {}
    for nm in ops:
        pts = sorted(direct[nm])                          # increasing u^2
        if kappa2[nm] == 0:
            assert all(v == 0 for _, v in pts)
            extrap[nm] = '0 (delta identically 0)'
            continue
        y = [(u2, 1 / v) for u2, v in pts]
        (x1, y1), (x2, y2) = y[0], y[1]
        slope = (y2 - y1) / (x2 - x1)
        assert all(yk == y1 + slope * (xk - x1) for xk, yk in y)   # 1/(delta/u)^2 affine in u^2
        y0 = y1 - slope * x1                                       # value at u^2 = 0
        assert y0 > 0 and 1 / y0 == L2[nm]
        gaps = [L2[nm] - v for _, v in pts]
        assert all(g1 < g2 for g1, g2 in zip(gaps, gaps[1:]))      # gap shrinks as u decreases
        extrap[nm] = short(1 / y0)
    old_holds = (L2[creator] == v2)
    assert old_holds == (kappa2[creator] == b2)
    res = {
        'name': name, 'nodes': M, 't': t, 'selection_degree_t+1': ''.join(selection),
        'perturbed_column': '(%d,%d)' % (t + 1, m), 'creating_operator': creator,
        'normal_direction': normal_label, 'r_sq': short(r2),
        'v_m_sq_unit_parent': short(v2), 'b_sq_unit_parent': short(b2),
        'kappa_sq': {nm: short(kappa2[nm]) for nm in ops},
        'kappa_sq_over_b_sq': {nm: short(kappa2[nm] / b2) for nm in ops},
        'limit_delta_sq_over_u_sq': {nm: short(L2[nm]) for nm in ops},
        'limit_from_direct_values_extrapolated': extrap,
        'creator_limit_sq': short(L2[creator]),
        'creator_limit_sq_over_v_m_sq': short(L2[creator] / v2),
        'kappa_creator_sq_ge_b_sq': True,
        'response01_wording_limit_eq_v_m_holds': old_holds,
        'samples_by_eta': [rec for _, rec in samples],
    }
    return res, {'kappa2': kappa2, 'b2': b2, 'v2': v2, 'L2': L2, 'creator': creator}


# ------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    t0 = time.time()
    T3 = [(i, j) for i in range(4) for j in range(4 - i)]
    T4 = [(i, j) for i in range(5) for j in range(5 - i)]
    Q3 = [(i, j) for i in range(4) for j in range(4)]
    uni = lambda P: [F(1, len(P))] * len(P)
    nonuni = [F(1 + i + 2 * j) for i, j in T3]
    nonuni = [c / sum(nonuni) for c in nonuni]
    # the same twelve random rational nodes and weights as response-01's checker
    rpts, rr = [], random.Random(7)
    while len(rpts) < 12:
        p = (F(rr.randint(-30, 30), rr.randint(1, 7)), F(rr.randint(-30, 30), rr.randint(1, 7)))
        if p not in rpts:
            rpts.append(p)
    rw = [F(rr.randint(1, 9)) for _ in rpts]
    rw = [c / sum(rw) for c in rw]
    BJ2, MIR2 = ['X', 'Y', 'Y'], ['X', 'X', 'Y']
    specs = []
    for m in range(3):
        specs.append(('T3_uniform_BJ_source_(2,%d)' % m, T3, uni(T3), 1, BJ2, m, None))
    specs.append(('T3_uniform_BJ_source_(2,0)_normal_x2y', T3, uni(T3), 1, BJ2, 0, (2, 1)))
    specs.append(('T3_uniform_BJ_source_(2,1)_normal_x3', T3, uni(T3), 1, BJ2, 1, (3, 0)))
    specs.append(('T3_uniform_mirror_source_(2,1)', T3, uni(T3), 1, MIR2, 1, None))
    for m in range(3):
        specs.append(('Q3_product_grid_uniform_BJ_source_(2,%d)' % m, Q3, uni(Q3), 1, BJ2, m, None))
    specs.append(('T3_nonuniform_weights_BJ_source_(2,1)', T3, nonuni, 1, BJ2, 1, None))
    for sel in (['X', 'Y', 'Y', 'Y'], ['X', 'X', 'X', 'Y'], ['X', 'Y', 'X', 'Y']):
        for m in range(4):
            specs.append(('T4_uniform_t2_%s_source_(3,%d)' % (''.join(sel), m), T4, uni(T4), 2, sel, m, None))
    for m in range(2):
        specs.append(('random12_t0_source_(1,%d)' % m, rpts, rw, 0, ['X', 'Y'], m, None))
    specs.append(('random12_t1_BJ_source_(2,1)', rpts, rw, 1, BJ2, 1, None))

    cases, raw = [], {}
    for spec in specs:
        res, data = instance(*spec)
        cases.append(res)
        raw[spec[0]] = data

    # record-15 constants
    d20 = raw['T3_uniform_BJ_source_(2,0)']
    assert d20['v2'] == F(22, 5) and d20['b2'] == F(7, 15) and d20['kappa2']['X'] == F(28, 45)
    assert d20['L2']['X'] == F(88, 15) and d20['L2']['X'] != d20['v2']
    assert d20['L2']['X'] / d20['v2'] == F(4, 3)
    d21 = raw['T3_uniform_BJ_source_(2,1)']
    assert d21['b2'] == F(28, 115) and d21['v2'] == F(3, 2)
    assert d21['kappa2']['Y'] == d21['b2'] and d21['kappa2']['X'] == F(4, 3) * d21['b2']
    assert d21['L2']['Y'] == F(3, 2) == d21['v2'] and d21['L2']['X'] == F(2)
    # the limit does not depend on the chosen unit normal direction
    for a, b in (('T3_uniform_BJ_source_(2,0)', 'T3_uniform_BJ_source_(2,0)_normal_x2y'),
                 ('T3_uniform_BJ_source_(2,1)', 'T3_uniform_BJ_source_(2,1)_normal_x3')):
        assert raw[a]['L2'] == raw[b]['L2']

    # cross-check kappa^2/b^2 against the committed response-01 evidence (read only)
    xcheck = {'file': R01_EVIDENCE, 'available': False}
    if os.path.exists(R01_EVIDENCE):
        with open(R01_EVIDENCE, 'rb') as fh:
            blob = fh.read()
        r01 = json.loads(blob)
        by_name = {c['name']: c for c in r01['instances']}
        alias = {'T3_uniform_BJ_source_(2,1)': 'T3_uniform_BJ_record15_eta=1'}
        compared = 0
        for c in cases:
            key = alias.get(c['name'], c['name'])
            if key not in by_name:
                continue
            o = by_name[key]
            for nm in ('X', 'Y'):
                mine = raw[c['name']]['kappa2'][nm] / raw[c['name']]['b2']
                theirs = F(o['delta_' + nm]['kappa_sq_over_b_sq_unit_parent'])
                assert mine == theirs, (c['name'], nm)
            assert F(o['b_sq_unit_parent']) == raw[c['name']]['b2']
            compared += 1
        xcheck = {'file': R01_EVIDENCE, 'available': True,
                  'sha256': hashlib.sha256(blob).hexdigest(),
                  'instances_compared': compared,
                  'kappa_sq_over_b_sq_and_b_sq_equal': True}

    creators = [(c['name'], raw[c['name']]['kappa2'][raw[c['name']]['creator']] / raw[c['name']]['b2'])
                for c in cases]
    strict = [nm for nm, q in creators if q > 1]
    equal = [nm for nm, q in creators if q == 1]
    elapsed = time.time() - t0
    with open(__file__, 'rb') as fh:
        code_sha = hashlib.sha256(fh.read()).hexdigest()
    out = {
        'purpose': 'Response-02 (Claude) exact regression for A02-M1: corrected relative-source '
                   'limit lim delta_(A)/u = (kappa_A/b)||v_m|| in PD-N?drift-codex-15, '
                   'kappa_(A_m) >= b; finite corroboration of an analytic proof, not a proof.',
        'command': 'PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 '
                   'python3 -B ' + CODE + ' --output ' + args.output,
        'code': CODE,
        'code_sha256': code_sha,
        'python': sys.version.split()[0],
        'platform': platform.platform(),
        'packages': 'Python standard library only (fractions, random, hashlib, json, os, platform, time)',
        'arithmetic': 'exact rationals (fractions.Fraction); every assertion exact; '
                      'floats appear only as display values for long exact numbers (with digests)',
        'eta_values': [str(e) for e in ETAS],
        'source_model': 'raw_m -> raw_m + eta*r with r a nonzero normal vector (r orthogonal to '
                        'S_(t+1)); u^2 = eta^2 ||r||^2/||raw_m||^2, i.e. ||f|| = u ||v_m||',
        'record15_constants': {
            'T3_BJ_source_v20': {'v20_sq': '22/5', 'b_sq': '7/15', 'kappaX_sq': '28/45',
                                 'kappaX_sq_over_b_sq': '4/3', 'limit_sq_X': '88/15',
                                 'response01_asserted_limit_sq': '22/5', 'asserted_value_correct': False},
            'T3_BJ_source_v21': {'v21_sq': '3/2', 'b_sq': '28/115', 'kappaY_sq_eq_b_sq': True,
                                 'limit_sq_Y': '3/2', 'limit_sq_X': '2',
                                 'response01_asserted_limit_sq': '3/2', 'asserted_value_correct': True},
        },
        'summary': {
            'instances': len(cases),
            'creator_ratio_kappa_sq_over_b_sq_ge_1_all': True,
            'instances_with_kappa_creator_gt_b': strict,
            'instances_with_kappa_creator_eq_b': equal,
            'max_creator_ratio': str(max(q for _, q in creators)),
        },
        'response01_evidence_crosscheck': xcheck,
        'instances': cases,
        'all_assertions_passed': True,
        'elapsed_seconds': round(elapsed, 2),
    }
    with open(args.output, 'w') as fh:
        json.dump(out, fh, indent=1)
        fh.write('\n')
    print('PASS: %d instances, %d with kappa_creator > b, %.1f s' % (len(cases), len(strict), elapsed))


if __name__ == '__main__':
    main()
