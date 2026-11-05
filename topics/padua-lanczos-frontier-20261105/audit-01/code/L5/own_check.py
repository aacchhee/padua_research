#!/usr/bin/env python3
"""Claude audit-01, family L5: auditor's own exact check of the G3 certificates.

Written from scratch by the auditor; imports nothing from the repository checkers/producers
and does not use SymPy.  Arithmetic: python-flint fmpq (exact rationals) for a hand-written
biquadratic field Q(sqrt a, sqrt b) in basis (1, sqrt a, sqrt b, sqrt(ab)); exact ranks via
python-flint fmpq_mat on the regular (4x4 block) rational representation, where
rank_Q(block(M)) = 4 * rank_K(M); signs via rigorous arb ball arithmetic in the embedding
sqrt a, sqrt b > 0 (a sign is accepted only when the ball excludes 0).

Checks
  * nodes: each coordinate is an exact root of T_m(x) = +-1 and its arb enclosure identifies
    cos(j*pi/m) rigorously (roots separated); Padua parity rule j+k even, j=0..n, k=0..n+1.
  * complete first-jet matrix J (value, d/dx, d/dy) in all monomials of degree <= 2n+1:
    exact K-rank (=> kernel dimension = #monomials - rank).
  * n3 upper certificate, kernel-basis-free reformulation:
      rank_K [J; M_W] = dim Pi_7 = 36   <=>  evaluation on S1 = ker J has rank dim S1;
      e = sum_a lambda_a m(w_a) lies in rowspace_K(J)  <=>  sum_a lambda_a s(w_a) = 0 for all s in S1;
      lambda_a > 0 (arb), ||h_a||^2 <= U^2 (exact rationals).
  * lower certificates n3/n4/n5: polynomial identity (pstar from the pinned blob parsed by an
    independent parser; P4/P5 rebuilt from the Chebyshev formula with own recurrence), exact
    zero value/gradient at every node, PD Hessian, all Taylor coefficients of every order
    3..deg p, and the inequality mu/2 - sum_k sum_{a+b=k} |t_ab| L^(k-2) > 0 with
    mu = det/trace, evaluated rigorously in arb; also reports whether 2L fails.
"""
import hashlib, json, re, sys, time
from math import comb
import flint
from flint import fmpq, fmpq_mat, arb, ctx

ctx.prec = 640


class Field:
    """Q(sqrt a, sqrt b), elements (c0,c1,c2,c3) = c0 + c1 sqrt a + c2 sqrt b + c3 sqrt(ab)."""

    def __init__(self, a, b):
        self.a, self.b = fmpq(a), fmpq(b)
        self.ra, self.rb = arb(a).sqrt(), arb(b).sqrt()
        self.rab = arb(a * b).sqrt()
        self.zero = (fmpq(0),) * 4
        self.one = (fmpq(1), fmpq(0), fmpq(0), fmpq(0))

    def c(self, q):
        return (fmpq(q), fmpq(0), fmpq(0), fmpq(0))

    def add(self, x, y):
        return tuple(p + q for p, q in zip(x, y))

    def sub(self, x, y):
        return tuple(p - q for p, q in zip(x, y))

    def neg(self, x):
        return tuple(-p for p in x)

    def scale(self, s, x):
        s = fmpq(s)
        return tuple(s * p for p in x)

    def mul(self, x, y):
        a, b = self.a, self.b
        x0, x1, x2, x3 = x
        y0, y1, y2, y3 = y
        return (x0 * y0 + a * x1 * y1 + b * x2 * y2 + a * b * x3 * y3,
                x0 * y1 + x1 * y0 + b * (x2 * y3 + x3 * y2),
                x0 * y2 + x2 * y0 + a * (x1 * y3 + x3 * y1),
                x0 * y3 + x3 * y0 + x1 * y2 + x2 * y1)

    def pw(self, x, k):
        r = self.one
        for _ in range(k):
            r = self.mul(r, x)
        return r

    def iszero(self, x):
        return all(p == 0 for p in x)

    def toarb(self, x):
        return arb(x[0]) + arb(x[1]) * self.ra + arb(x[2]) * self.rb + arb(x[3]) * self.rab

    def block(self, x):
        """Matrix of multiplication by x on coordinates (y0,y1,y2,y3)."""
        a, b = self.a, self.b
        x0, x1, x2, x3 = x
        return [[x0, a * x1, b * x2, a * b * x3],
                [x1, x0, b * x3, b * x2],
                [x2, a * x3, x0, a * x1],
                [x3, x2, x1, x0]]

    def krank(self, rows):
        m, n = len(rows), len(rows[0])
        ent = []
        for r in rows:
            blocks = [self.block(x) for x in r]
            for i in range(4):
                for bl in blocks:
                    ent.extend(bl[i])
        M = fmpq_mat(4 * m, 4 * n, ent)
        rq = M.rank()
        assert rq % 4 == 0, 'block rank not divisible by 4'
        return rq // 4


def certain_pos(v):
    return v > 0  # arb: True only if the whole ball is > 0


def cheb(F, m, x):
    p, c = F.one, x
    if m == 0:
        return p
    for _ in range(m - 1):
        p, c = c, F.sub(F.scale(2, F.mul(x, c)), p)
    return c


def identify(F, vals, m):
    """vals[j] must equal cos(j*pi/m), j=0..m."""
    assert len(vals) == m + 1
    gap = min(abs(arb.cos_pi_fmpq(fmpq(i, m)) - arb.cos_pi_fmpq(fmpq(i + 1, m))) for i in range(m))
    for j, v in enumerate(vals):
        t = cheb(F, m, v)
        assert F.iszero(F.sub(t, F.c((-1) ** j))), ('T_m(x_j) != (-1)^j', m, j)
        dist = abs(F.toarb(v) - arb.cos_pi_fmpq(fmpq(j, m)))
        assert dist < gap / 4, ('enclosure does not identify cos', m, j)
    return True


def padua(n, F, xs, ys):
    identify(F, xs, n)
    identify(F, ys, n + 1)
    Z = [(xs[j], ys[k]) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    assert len(Z) == (n + 1) * (n + 2) // 2
    return Z


def monomials(D):
    return [(a, t - a) for t in range(D + 1) for a in range(t + 1)]


def jet_rows(F, Z, MON):
    rows = []
    for x, y in Z:
        px = [F.pw(x, k) for k in range(max(a for a, b in MON) + 1)]
        py = [F.pw(y, k) for k in range(max(b for a, b in MON) + 1)]
        rows.append([F.mul(px[a], py[b]) for a, b in MON])
        rows.append([F.scale(a, F.mul(px[a - 1], py[b])) if a else F.zero for a, b in MON])
        rows.append([F.scale(b, F.mul(px[a], py[b - 1])) if b else F.zero for a, b in MON])
    return rows


def rat(s):
    assert re.fullmatch(r'[+-]?\d+(/\d+)?', s), s
    if '/' in s:
        p, q = s.split('/')
        return fmpq(int(p), int(q))
    return fmpq(int(s))


def taylor_check(F, Z, poly, D, L):
    """poly: dict (a,b)->field element.  Returns per-node margins (arb) at L and at 2L."""
    deg = max(a + b for a, b in poly)
    assert deg <= D and any(not F.iszero(c) for c in poly.values())
    out = []
    for x, y in Z:
        px = [F.pw(x, k) for k in range(deg + 1)]
        py = [F.pw(y, k) for k in range(deg + 1)]
        t = {}
        for r in range(deg + 1):
            for s in range(deg + 1 - r):
                v = F.zero
                for (a, b), c in poly.items():
                    if a >= r and b >= s:
                        v = F.add(v, F.scale(comb(a, r) * comb(b, s), F.mul(c, F.mul(px[a - r], py[b - s]))))
                t[r, s] = v
        assert F.iszero(t[0, 0]) and F.iszero(t[1, 0]) and F.iszero(t[0, 1]), 'nonzero first jet'
        hxx, hxy, hyy = F.scale(2, t[2, 0]), t[1, 1], F.scale(2, t[0, 2])
        det = F.sub(F.mul(hxx, hyy), F.mul(hxy, hxy))
        tr = F.add(hxx, hyy)
        A_hxx, A_det, A_tr = F.toarb(hxx), F.toarb(det), F.toarb(tr)
        assert certain_pos(A_hxx) and certain_pos(A_det), 'Hessian not certified PD'
        mu = A_det / A_tr
        sums = {k: sum((abs(F.toarb(t[a, k - a])) for a in range(k + 1)), arb(0)) for k in range(3, deg + 1)}
        res = {}
        for lab, LL in (('L', L), ('2L', 2 * L)):
            rem = sum((sums[k] * arb(LL) ** (k - 2) for k in sums), arb(0))
            res[lab] = mu / 2 - rem
        out.append({'mu': mu, 'margin_L': res['L'], 'margin_2L': res['2L']})
    return out


def P_formula(n):
    """P_n = 9(g1^2 - g0 g2/2) + g2^2 - g1 g3, g_m = T_{n-m}(x)T_m(y) - T_m(x)T_{n+1-m}(y), as dict."""
    def T1d(k):  # coefficient list of T_k
        p, c = [fmpq(1)], [fmpq(0), fmpq(1)]
        if k == 0:
            return p
        for _ in range(k - 1):
            nxt = [fmpq(0)] * (len(c) + 1)
            for i, v in enumerate(c):
                nxt[i + 1] += 2 * v
            for i, v in enumerate(p):
                nxt[i] -= v
            p, c = c, nxt
        return c

    def outer(px, py):
        return {(i, j): u * v for i, u in enumerate(px) for j, v in enumerate(py) if u * v != 0}

    def add(P, Q, s=1):
        R = dict(P)
        for k, v in Q.items():
            R[k] = R.get(k, fmpq(0)) + s * v
        return {k: v for k, v in R.items() if v != 0}

    def mul(P, Q):
        R = {}
        for (a, b), u in P.items():
            for (c, d), v in Q.items():
                R[a + c, b + d] = R.get((a + c, b + d), fmpq(0)) + u * v
        return {k: v for k, v in R.items() if v != 0}

    def sc(s, P):
        return {k: s * v for k, v in P.items()}

    g = [add(outer(T1d(n - m), T1d(m)), outer(T1d(m), T1d(n + 1 - m)), -1) for m in range(4)]
    P = add(sc(9, add(mul(g[1], g[1]), sc(fmpq(1, 2), mul(g[0], g[2])), -1)), add(mul(g[2], g[2]), mul(g[1], g[3]), -1))
    return P


def parse_pstar_blob(path):
    txt = open(path).read()
    sec = txt[txt.index('p* monomial coefficients'):]
    sec = sec[:sec.index('node 0')]
    poly = {}
    for line in sec.splitlines():
        m = re.match(r'\s*x\^(\d+) y\^(\d+): \((.*)\)\s*$', line)
        if m:
            body = m.group(3)
            mm = re.fullmatch(r'([+-]?[\d/]+)\+([+-]?[\d/]+)r2', body)
            assert mm, body
            poly[int(m.group(1)), int(m.group(2))] = (rat(mm.group(1)), rat(mm.group(2)))
    return poly


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def main():
    ev, blob, rec = sys.argv[1], sys.argv[2], sys.argv[3]  # evidence dir, pstar blob copy, committed receipts dir
    t0 = time.monotonic()
    R = {'prec_bits': ctx.prec, 'flint': flint.__version__}
    half = fmpq(1, 2)

    # ---------- n = 3 ----------
    F3 = Field(2, 3)  # Q(sqrt2) inside Q(sqrt2, sqrt3); ranks are field-extension invariant
    r2 = (fmpq(0), fmpq(1), fmpq(0), fmpq(0))
    xs = [F3.c(1), F3.c(half), F3.c(-half), F3.c(-1)]
    ys = [F3.c(1), F3.scale(half, r2), F3.zero, F3.scale(-half, r2), F3.c(-1)]
    Z3 = padua(3, F3, xs, ys)
    MON7 = monomials(7)
    J3 = jet_rows(F3, Z3, MON7)
    rJ = F3.krank(J3)
    R['n3'] = {'nodes': len(Z3), 'monomials': len(MON7), 'J_rows': len(J3), 'rank_J': rJ, 'kernel_dim': len(MON7) - rJ}
    up = json.load(open(ev + '/g3-producer-n3-upper.json'))
    U = rat(up['U'])
    MW, lam, outside, d2 = [], [], 0, []
    e = [F3.zero] * len(MON7)
    for (i, hx, hy), (wa, wb) in zip(up['points'], up['weights']):
        hx, hy = rat(hx), rat(hy)
        assert hx * hx + hy * hy <= U * U, 'off-ball'
        d2.append(str(hx * hx + hy * hy))
        w = (F3.add(Z3[i][0], F3.c(hx)), F3.add(Z3[i][1], F3.c(hy)))
        outside += int(abs(F3.toarb(w[0])) > 1 or abs(F3.toarb(w[1])) > 1)
        row = [F3.mul(F3.pw(w[0], a), F3.pw(w[1], b)) for a, b in MON7]
        MW.append(row)
        l = (rat(wa), rat(wb), fmpq(0), fmpq(0))  # a + b*sqrt2 in basis (1, sqrt2, sqrt3, sqrt6)
        la = F3.toarb(l)
        assert certain_pos(la), 'weight not certified positive'
        lam.append(la)
        e = [F3.add(ei, F3.mul(l, ri)) for ei, ri in zip(e, row)]
    rJW = F3.krank(J3 + MW)
    rJe = F3.krank(J3 + [e])
    R['n3']['upper'] = {'U': str(U), 'points': len(MW), 'weights_positive_arb': True,
                        'min_weight_lower': min(float(x.lower()) for x in lam), 'max_sq_offset': max(d2, key=lambda s: rat(s)),
                        'rank_[J;M_W]': rJW, 'rank_[J;e]': rJe, 'points_outside_square': outside,
                        'eval_rank_on_S1': rJW - rJ, 'balance_on_S1': rJe == rJ}
    assert rJ == 30 and rJW == 36 and rJe == 30
    # proper-subset sanity: dropping all but one point must lose rank (control)
    R['n3']['control_rank_one_point'] = F3.krank(J3 + MW[:1]) - rJ
    # perturbed weight control: e' = e + m(w_0) (weight lambda_0 + 1) must leave rowspace
    e2 = [F3.add(ei, ri) for ei, ri in zip(e, MW[0])]
    R['n3']['control_unbalanced_rank'] = F3.krank(J3 + [e2])

    low3 = json.load(open(ev + '/g3-producer-n3-lower.json'))
    poly3 = {(a, b): (rat(c[0]), rat(c[1]), fmpq(0), fmpq(0)) for a, b, c in low3['polynomial']}
    blobp = parse_pstar_blob(blob)
    assert {k: (v[0], v[1], fmpq(0), fmpq(0)) for k, v in blobp.items()} == poly3, 'pstar mismatch'
    tl = taylor_check(F3, Z3, poly3, 7, rat(low3['L']))
    R['n3']['lower'] = summarize(tl, rat(low3['L']), len(poly3))
    R['n3']['lower']['matches_blob_terms'] = len(blobp)
    R['n3']['lower']['receipt_margin_agreement'] = agree(F3, tl, rec + '/g3-independent.json', 'lower', 2)

    # ---------- n = 4 : Q(sqrt5, sqrt2) basis (1, sqrt5, sqrt2, sqrt10) ----------
    F4 = Field(5, 2)
    s5 = (fmpq(0), fmpq(1), fmpq(0), fmpq(0))
    s2 = (fmpq(0), fmpq(0), fmpq(1), fmpq(0))
    q = fmpq(1, 4)
    xs = [F4.c(1), F4.scale(half, s2), F4.zero, F4.scale(-half, s2), F4.c(-1)]
    ys = [F4.c(1), F4.scale(q, F4.add(F4.one, s5)), F4.scale(q, F4.sub(s5, F4.one)), F4.scale(q, F4.sub(F4.one, s5)),
          F4.scale(-q, F4.add(F4.one, s5)), F4.c(-1)]
    Z4 = padua(4, F4, xs, ys)
    MON9 = monomials(9)
    rJ4 = F4.krank(jet_rows(F4, Z4, MON9))
    low4 = json.load(open(ev + '/g3-n4-producer-lower.json'))
    poly4 = {(a, b): tuple(rat(t) for t in c) for a, b, c in low4['polynomial']}
    P4 = P_formula(4)
    assert {k: (v, fmpq(0), fmpq(0), fmpq(0)) for k, v in P4.items()} == poly4, 'P4 mismatch'
    tl4 = taylor_check(F4, Z4, poly4, 9, rat(low4['L']))
    R['n4'] = {'nodes': len(Z4), 'monomials': len(MON9), 'rank_J': rJ4, 'kernel_dim': len(MON9) - rJ4,
               'lower': summarize(tl4, rat(low4['L']), len(poly4)),
               'P4_formula_terms': len(P4), 'P4_degree': max(a + b for a, b in P4)}
    R['n4']['lower']['receipt_margin_agreement'] = agree(F4, tl4, rec + '/g3-n4-independent-lower.json', 'lower', 4)

    # ---------- n = 5 : Q(sqrt5, sqrt3) basis (1, sqrt5, sqrt3, sqrt15) ----------
    F5 = Field(5, 3)
    s5 = (fmpq(0), fmpq(1), fmpq(0), fmpq(0))
    s3 = (fmpq(0), fmpq(0), fmpq(1), fmpq(0))
    xs = [F5.c(1), F5.scale(q, F5.add(F5.one, s5)), F5.scale(q, F5.sub(s5, F5.one)), F5.scale(q, F5.sub(F5.one, s5)),
          F5.scale(-q, F5.add(F5.one, s5)), F5.c(-1)]
    ys = [F5.c(1), F5.scale(half, s3), F5.c(half), F5.zero, F5.c(-half), F5.scale(-half, s3), F5.c(-1)]
    Z5 = padua(5, F5, xs, ys)
    MON11 = monomials(11)
    rJ5 = F5.krank(jet_rows(F5, Z5, MON11))
    low5 = json.load(open(ev + '/g3-n5-producer-lower.json'))
    poly5 = {(a, b): tuple(rat(t) for t in c) for a, b, c in low5['polynomial']}
    P5 = P_formula(5)
    assert {k: (v, fmpq(0), fmpq(0), fmpq(0)) for k, v in P5.items()} == poly5, 'P5 mismatch'
    tl5 = taylor_check(F5, Z5, poly5, 11, rat(low5['L']))
    R['n5'] = {'nodes': len(Z5), 'monomials': len(MON11), 'rank_J': rJ5, 'kernel_dim': len(MON11) - rJ5,
               'lower': summarize(tl5, rat(low5['L']), len(poly5)),
               'P5_formula_terms': len(P5), 'P5_degree': max(a + b for a, b in P5)}
    R['n5']['lower']['receipt_margin_agreement'] = agree(F5, tl5, rec + '/g3-n5-independent-lower.json', 'lower', 4)

    R['inputs'] = {f: sha(ev + '/' + f) for f in ['g3-producer-n3-upper.json', 'g3-producer-n3-lower.json',
                                                  'g3-n4-producer-lower.json', 'g3-n5-producer-lower.json']}
    R['blob_sha256'] = sha(blob)
    R['elapsed_s'] = time.monotonic() - t0
    R['status'] = 'PASS' if all(R[k]['lower']['all_margins_certified_positive'] for k in ('n3', 'n4', 'n5')) else 'FAIL'
    print(json.dumps(R, indent=1, default=str))


def summarize(tl, L, nterms):
    return {'L': str(L), 'nonzero_terms': nterms, 'nodes': len(tl),
            'all_margins_certified_positive': all(certain_pos(r['margin_L']) for r in tl),
            'min_margin_L': str(min((r['margin_L'] for r in tl), key=lambda v: float(v.mid()))),
            'min_mu': str(min((r['mu'] for r in tl), key=lambda v: float(v.mid()))),
            'nodes_failing_at_2L': sum(int(r['margin_2L'] < 0) for r in tl),
            'nodes_uncertain_at_2L': sum(int(not (r['margin_2L'] < 0) and not (r['margin_2L'] > 0)) for r in tl)}


def agree(F, tl, recpath, key, width):
    rec = json.load(open(recpath))
    nodes = rec[key]['node_certificates']
    ok = True
    for mine, theirs in zip(tl, nodes):
        m = theirs['Taylor_margin']
        coords = [rat(s) for s in m] + [fmpq(0)] * (4 - len(m))
        if width == 2:
            el = (coords[0], coords[1], fmpq(0), fmpq(0))
        else:
            el = tuple(coords)
        ok &= bool(abs(F.toarb(el) - mine['margin_L']) < arb(10) ** -100)
    return ok and len(tl) == len(nodes)


if __name__ == '__main__':
    main()
