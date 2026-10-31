"""Claude audit-01 independent checker for PD-T001, PD-T002, PD-N001, PD-T003.

Written from the theorem statements only (developer checkers were not read before
writing this file). Exact arithmetic in GF(p^k) via gf.py. Exhaustive over all
labelled axis pairs in small fields (this reaches many singular boards, so both
directions of each iff are exercised), seeded random samples in larger fields.

Checks per labelled pair (X,Y) and parity e in {0,1}:
  * PD-T002 identity  det(V_e)^2 W_e == A_E * Q^2         (every characteristic)
  * PD-T002 iff       det(V_e)!=0  <=>  H_r(X),H_r(Y)!=0 on r=1..floor((L-2)/2)
  * PD-T001 identity  det(V_e)^2 W_e == 2^-N prod_{r<=m+1} Delta_r(X)Delta_r(Y)  (char != 2)
  * PD-T001 iff       (char != 2)
  * Delta_{L-r} == Delta_r, Delta_L == 1, A_E != 0, terminal odd-axis H_k != 0
  * PD-T003 kernel cardinality (char != 2, criterion holds; on a subsample)
  * PD-N001: in char 2 record unisolvent boards whose original alternation
    cutoff condition fails; also confirm "original sufficiency" never fails.
Usage: python3 check_checkerboard.py OUTPUT.json
"""
import itertools
import json
import random
import sys
import hashlib
import platform

sys.path.insert(0, __import__('os').path.dirname(__file__))
from gf import GF


def monomials(m):
    return [(a, d - a) for d in range(m + 1) for a in range(d, -1, -1)]


def omega_prime(F, H, i):
    return F.prod(F.sub(H[i], H[j]) for j in range(len(H)) if j != i)


def sign(F, i):
    return F.one if i % 2 == 0 else F.neg(F.one)


def alt_weights(F, H):
    return [F.mul(sign(F, i), F.inv(omega_prime(F, H, i))) for i in range(len(H))]


def hankel_minors(F, H, weights, rmax):
    # moments of functional sum_i weights[i] f(h_i)
    mom = []
    for k in range(2 * rmax + 1):
        s = 0
        for h, w in zip(H, weights):
            s = F.add(s, F.mul(w, F.pow(h, k)))
        mom.append(s)
    out = [F.one]
    for r in range(1, rmax + 1):
        out.append(F.det([[mom[a + b] for b in range(r)] for a in range(r)]))
    return out


def board(F, X, Y, m, e):
    S = [(i, j) for i in range(len(X)) for j in range(len(Y)) if (i + j) % 2 == e]
    mons = monomials(m)
    V = [[F.mul(F.pow(X[i], a), F.pow(Y[j], b)) for (a, b) in mons] for (i, j) in S]
    return S, V


def vand_sq(F, H):
    r = F.one
    for i in range(len(H)):
        for j in range(i + 1, len(H)):
            d = F.sub(H[j], H[i])
            r = F.mul(r, F.mul(d, d))
    return r


def check_pair(F, X, Y, m, stats, do_kernel=False):
    char2 = F.p == 2
    N = (m + 1) * (m + 2) // 2
    wX, wY = alt_weights(F, X), alt_weights(F, Y)
    LX, LY = len(X), len(Y)
    DX = hankel_minors(F, X, wX, LX)
    DY = hankel_minors(F, Y, wY, LY)
    # complementary minors and full minor
    for D, L in ((DX, LX), (DY, LY)):
        assert D[L] == F.one, 'full alternation minor != 1'
        for r in range(L + 1):
            assert D[L - r] == D[r], 'complementary minor failure'
    # B_H even-index barycentric functional
    def Bdata(H):
        L = len(H)
        bw = [F.inv(omega_prime(F, H, i)) if i % 2 == 0 else 0 for i in range(L)]
        k = L // 2
        Hm = hankel_minors(F, H, bw, max(k, 1))
        return Hm
    HX, HY = Bdata(X), Bdata(Y)
    # terminal odd-axis minor and even-axis central minor
    for H, Hm in ((X, HX), (Y, HY)):
        L = len(H)
        k = L // 2
        if L % 2 == 1 and k >= 1:
            assert Hm[k] != 0, 'terminal odd-axis H_k vanished'
        if L % 2 == 0:
            ev = [H[i] for i in range(0, L, 2)]
            A = F.mul(vand_sq(F, ev), F.prod(F.inv(omega_prime(F, H, i)) for i in range(0, L, 2)))
            assert Hm[k] == A and A != 0, 'A_E failure'
    E, HE = (X, HX) if LX % 2 == 0 else (Y, HY)
    A_E = HE[len(E) // 2]
    Q = F.one
    for H, Hm in ((X, HX), (Y, HY)):
        L = len(H)
        R = range(1, L // 2) if L % 2 == 0 else range(1, L // 2 + 1)
        for r in R:
            Q = F.mul(Q, Hm[r])
    crit_new = all(HX[r] != 0 for r in range(1, (LX - 2) // 2 + 1)) and \
        all(HY[r] != 0 for r in range(1, (LY - 2) // 2 + 1))
    crit_orig = all(DX[r] != 0 for r in range(1, LX)) and all(DY[r] != 0 for r in range(1, LY))
    rhs1 = None
    if not char2:
        inv2N = F.inv(F.pow(2 % F.p, N))
        rhs1 = F.mul(inv2N, F.prod(F.mul(DX[r], DY[r]) for r in range(1, m + 2)))
    results = []
    for e in (0, 1):
        S, V = board(F, X, Y, m, e)
        assert len(S) == N
        dV = F.det(V)
        W = F.prod(F.mul(wX[i], wY[j]) for (i, j) in S)
        lhs = F.mul(F.mul(dV, dV), W)
        assert W != 0
        assert lhs == F.mul(A_E, F.mul(Q, Q)), 'PD-T002 identity (2) failed'
        uni = dV != 0
        assert uni == crit_new, 'PD-T002 iff failed'
        if not char2:
            assert lhs == rhs1, 'PD-T001 identity (1) failed'
            assert uni == crit_orig, 'PD-T001 iff failed'
        else:
            if uni and not crit_orig:
                stats['char2_unisolvent_orig_fails'] += 1
            # sufficiency of original condition must never fail
            if crit_orig and not uni:
                stats['orig_sufficiency_failures'] += 1
            if crit_orig:
                stats['char2_orig_condition_true'] += 1
        stats['boards'] += 1
        stats['singular' if not uni else 'unisolvent'] += 1
        results.append(uni)
        if do_kernel and uni and not char2:
            check_kernel(F, X, Y, m, e, S, wX, wY, DX, DY)
            stats['kernel_checked'] += 1
    if results[0] != results[1]:
        stats['parity_disagreement'] += 1
    return results


def monic_ops(F, H, w, deg):
    # monic orthogonal polys p_0..p_deg for functional sum w_i f(h_i), via Gram-Schmidt on values
    vals = []
    polys = []
    def ip(u, v):
        s = 0
        for a, b, c in zip(u, v, w):
            s = F.add(s, F.mul(c, F.mul(a, b)))
        return s
    for a in range(deg + 1):
        coeffs = [0] * a + [F.one]
        v = [F.pow(h, a) for h in H]
        for b in range(a):
            nb = ip(vals[b], vals[b])
            c = F.div(ip(v, vals[b]), nb)
            v = [F.sub(x, F.mul(c, y)) for x, y in zip(v, vals[b])]
            pb = polys[b]
            for t in range(len(pb)):
                coeffs[t] = F.sub(coeffs[t], F.mul(c, pb[t]))
        vals.append(v)
        polys.append(coeffs)
    norms = [ip(v, v) for v in vals]
    return polys, norms


def peval(F, coeffs, t):
    s = 0
    for c in reversed(coeffs):
        s = F.add(F.mul(s, t), c)
    return s


def check_kernel(F, X, Y, m, e, S, wX, wY, DX, DY):
    P, nP = monic_ops(F, X, wX, m)
    Qp, nQ = monic_ops(F, Y, wY, m)
    for a in range(m + 1):
        assert nP[a] == F.div(DX[a + 1], DX[a])
        assert nQ[a] == F.div(DY[a + 1], DY[a])
    two = 2 % F.p
    for (i, j) in S:
        coef = F.mul(two, F.mul(wX[i], wY[j]))
        for (i2, j2) in S:
            s = 0
            for a in range(m + 1):
                for b in range(m + 1 - a):
                    t = F.mul(F.mul(peval(F, P[a], X[i2]), peval(F, Qp[b], Y[j2])),
                              F.mul(peval(F, P[a], X[i]), peval(F, Qp[b], Y[j])))
                    s = F.add(s, F.div(t, F.mul(nP[a], nQ[b])))
            val = F.mul(coef, s)
            assert val == (F.one if (i, j) == (i2, j2) else 0), 'kernel cardinality failed'


def new_stats():
    return dict(boards=0, singular=0, unisolvent=0, parity_disagreement=0,
                char2_unisolvent_orig_fails=0, orig_sufficiency_failures=0,
                char2_orig_condition_true=0, kernel_checked=0, pairs=0)


def run():
    out = {'checker': 'claude-audit-01 check_checkerboard.py', 'python': platform.python_version(),
           'checker_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(), 'cases': []}
    rng = random.Random(20261031)
    exhaustive = [((2, 1), 0), ((3, 1), 0), ((2, 2), 0), ((2, 2), 1), ((3, 1), 1), ((5, 1), 1),
                  ((2, 2), 2), ((5, 1), 2), ((2, 3), 2), ((5, 1), 3), ((7, 1), 2)]
    sampled = [((3, 2), 2, 4000), ((2, 3), 3, 3000), ((2, 3), 4, 1500), ((2, 4), 3, 1500), ((2, 4), 4, 800),
               ((2, 4), 5, 300), ((3, 2), 3, 2000), ((3, 2), 4, 800), ((5, 2), 4, 500),
               ((7, 1), 3, 2000), ((7, 1), 4, 800), ((11, 1), 4, 500), ((11, 1), 5, 300),
               ((13, 1), 6, 150), ((2, 5), 6, 100), ((3, 3), 6, 100)]
    for (p, k), m in exhaustive:
        F = GF(p, k)
        if F.q < m + 2:
            continue
        st = new_stats()
        for X in itertools.permutations(range(F.q), m + 1):
            for Y in itertools.permutations(range(F.q), m + 2):
                st['pairs'] += 1
                check_pair(F, list(X), list(Y), m, st, do_kernel=(st['pairs'] % 37 == 0))
        out['cases'].append({'field': repr(F), 'm': m, 'mode': 'exhaustive', **st})
        print(json.dumps(out['cases'][-1]), flush=True)
    for (p, k), m, ns in sampled:
        F = GF(p, k)
        st = new_stats()
        for _ in range(ns):
            X = rng.sample(range(F.q), m + 1)
            Y = rng.sample(range(F.q), m + 2)
            st['pairs'] += 1
            check_pair(F, X, Y, m, st, do_kernel=(st['pairs'] % 50 == 0))
        out['cases'].append({'field': repr(F), 'm': m, 'mode': f'seeded-sample({ns})', **st})
        print(json.dumps(out['cases'][-1]), flush=True)
    # explicit PD-N001 examples
    F4 = GF(2, 2)
    # find a: element not 0,1 ; check X=(0,1),Y=(0,1,a)
    a = 2
    st = new_stats()
    r = check_pair(F4, [0, 1], [0, 1, a], 1, st)
    assert r == [True, True] and st['char2_unisolvent_orig_fails'] == 2
    out['PD-N001_F4_example'] = {'unisolvent_both': r, 'orig_condition_fails': st['char2_unisolvent_orig_fails'] == 2,
                                 'modulus_low_first': F4.mod}
    F8 = GF(2, 3)
    # PD-N001 example uses a root a of a^3+a+1 (our table modulus may differ); test every such root
    roots = [x for x in range(8) if F8.add(F8.add(F8.pow(x, 3), x), 1) == 0]
    assert len(roots) == 3
    ex = []
    for a8 in roots:
        st = new_stats()
        r = check_pair(F8, [0, 1, a8], [0, 1, a8, F8.mul(a8, a8)], 2, st)
        assert r == [True, True] and st['char2_unisolvent_orig_fails'] == 2
        ex.append({'root_code': a8, 'unisolvent_both': r, 'orig_condition_fails': True})
    out['PD-N001_F8_example'] = {'roots_of_a3_a_1': ex, 'table_modulus_low_first': F8.mod}
    tot = sum(c['orig_sufficiency_failures'] for c in out['cases'])
    out['total_orig_sufficiency_failures'] = tot
    out['all_assertions'] = 'PASS'
    return out


if __name__ == '__main__':
    res = run()
    with open(sys.argv[1], 'w') as fh:
        json.dump(res, fh, indent=1)
    print('ALL PASS; boards', sum(c['boards'] for c in res['cases']))
