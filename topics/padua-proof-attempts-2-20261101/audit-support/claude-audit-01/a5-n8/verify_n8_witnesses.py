#!/usr/bin/env python3
"""Independent rigorous verifier for the A5 n=8 interior root witnesses.

Claude audit-01 sub-auditor.  Imports NO repository code.  Reads only the
mathematical records (mask, R, C) of the standalone witness JSON; ignores every
metadata/count/flag field except to report it.

Construction (rigorous ball arithmetic, python-flint arb, default 320 bits):
  * nodes z_(j,k) = (cos(j*pi/8), cos(k*pi/9)), 0<=j<=8, 0<=k<=9, j+k even,
    lexicographic in (j,k)  (the convention of theory 60 / schema; mask bit i
    set  <=>  s_i = +1 for node i in that order);
  * cardinals: coefficient matrix = rigorous arb inverse of the 45x45 monomial
    Vandermonde (unisolvence is certified by the inverse succeeding);
  * cross-check: closed-form Padua kernel formula (Bos-De Marchi-Vianello-Xu)
    in Chebyshev form, converted to monomials, must overlap every coefficient.
Per record, on the closed rational rectangle R:
  (i)   every signed cardinal s_i L_i has a strictly positive lower bound on R
        (Taylor-model enclosure at the exact box centre; bisection fallback
        that must cover the whole of R);
  (ii)  Krawczyk: K = c - C g(c) + (I - C H(R))(R - c) lies in int R and
        ||I - C H(R)||_inf < 1  (=> unique zero of grad P_s in R);
  (iii) H_xx(R) < 0 and det H(R) > 0  (negative definite throughout R);
  (iv)  -1 < xl < xh < 1, -1 < yl < yh < 1 (exact rationals);
  (v)   rectangles pairwise disjoint (exact rationals, closed boxes).
"""
import argparse, hashlib, json, sys, time
from fractions import Fraction
from itertools import combinations

import flint
from flint import arb, arb_mat, fmpq, ctx

N_DEG = 8


def F2q(fr):
    return fmpq(fr.numerator, fr.denominator)


def nodes_arb():
    pts, idx = [], []
    for j in range(N_DEG + 1):
        for k in range(N_DEG + 2):
            if (j + k) % 2 == 0:
                x = (arb.pi() * j / N_DEG).cos() if j not in (0, N_DEG) else arb(1 if j == 0 else -1)
                y = (arb.pi() * k / (N_DEG + 1)).cos() if k not in (0, N_DEG + 1) else arb(1 if k == 0 else -1)
                pts.append((x, y)); idx.append((j, k))
    return pts, idx


POWERS = [(i, d - i) for d in range(N_DEG + 1) for i in range(d, -1, -1)]  # (px, py)


def vandermonde_cardinals(pts):
    rows = []
    for (x, y) in pts:
        xp = [arb(1)]; yp = [arb(1)]
        for _ in range(N_DEG):
            xp.append(xp[-1] * x); yp.append(yp[-1] * y)
        rows.append([xp[i] * yp[j] for (i, j) in POWERS])
    V = arb_mat(rows)
    Vi = V.inv()  # rigorous enclosure; raises if not certainly invertible
    # cardinal b: coefficients Vi[k, b] on monomial POWERS[k]
    card = [[Vi[k, b] for k in range(len(POWERS))] for b in range(len(pts))]
    # residual check V*Vi contains I
    P = V * Vi
    ok = all(P[r, c].contains(1 if r == c else 0) for r in range(45) for c in range(45))
    return card, ok


def cheb_coeffs(m):
    """Integer monomial coefficients of T_m (list, index = power)."""
    T = [[1], [0, 1]]
    for k in range(2, m + 1):
        a = [0] + [2 * c for c in T[-1]]
        b = T[-2] + [0] * (len(a) - len(T[-2]))
        T.append([u - v for u, v in zip(a, b)])
    return T[m]


def formula_cardinals(pts, idx):
    """Closed-form Lagrange basis L_xi(x) = w_xi (K_n(xi,x) - T_n(xi_1) T_n(x_1)),
    K_n = sum_{a+b<=n} That_a(xi1)That_b(xi2)That_a(x1)That_b(x2), That_0=1,
    That_p = sqrt2 T_p, w = 1/(n(n+1)) * (1/2 vertex, 1 edge, 2 interior)."""
    n = N_DEG
    Tc = [cheb_coeffs(m) for m in range(n + 1)]
    pos = {p: q for q, p in enumerate(POWERS)}
    out = []
    for (x0, y0), (j, k) in zip(pts, idx):
        on_x = j in (0, n); on_y = k in (0, n + 1)
        w = fmpq(1, 2) if (on_x and on_y) else (fmpq(1) if (on_x or on_y) else fmpq(2))
        w = arb(w) / (n * (n + 1))
        Tx0 = [arb(1), x0]; Ty0 = [arb(1), y0]
        for m in range(2, n + 1):
            Tx0.append(2 * x0 * Tx0[-1] - Tx0[-2]); Ty0.append(2 * y0 * Ty0[-1] - Ty0[-2])
        coef = [arb(0)] * len(POWERS)
        for a in range(n + 1):
            for b in range(n + 1 - a):
                fa = 1 if a == 0 else 2  # That_a(xi)That_a(x) = fa*T_a T_a
                fb = 1 if b == 0 else 2
                c_ab = fa * fb * Tx0[a] * Ty0[b]
                if a == n and b == 0:
                    c_ab = c_ab - Tx0[n]  # subtract T_n(xi1) T_n(x1)
                for pa, ca in enumerate(Tc[a]):
                    if ca == 0:
                        continue
                    for pb, cb in enumerate(Tc[b]):
                        if cb == 0:
                            continue
                        q = pos[(pa, pb)]
                        coef[q] = coef[q] + c_ab * (ca * cb)
        out.append([w * c for c in coef])
    return out


def taylor_shift(coef, cx, cy):
    """Coefficients a[(p,q)] of f(cx+u, cy+v) for f = sum coef[k] x^i y^j."""
    from math import comb
    cxp = [arb(1)]; cyp = [arb(1)]
    for _ in range(N_DEG):
        cxp.append(cxp[-1] * cx); cyp.append(cyp[-1] * cy)
    a = {}
    for (p, q) in POWERS:
        s = arb(0)
        for k, (i, j) in enumerate(POWERS):
            if i >= p and j >= q:
                s += coef[k] * (comb(i, p) * comb(j, q)) * cxp[i - p] * cyp[j - q]
        a[(p, q)] = s
    return a


def deriv_shift(a, dx, dy):
    """Taylor coefficients (at same centre) of d^dx/dx d^dy/dy f."""
    from math import perm
    b = {}
    for (p, q) in POWERS:
        if p + dx + q + dy <= N_DEG and (p + dx, q + dy) in a:
            b[(p, q)] = a[(p + dx, q + dy)] * (perm(p + dx, dx) * perm(q + dy, dy))
    return b


def enclose(b, rx, ry):
    """Ball enclosing {sum b_pq u^p v^q : |u|<=rx, |v|<=ry}; rx, ry arb >=0."""
    c0 = b.get((0, 0), arb(0))
    rad = arb(0)
    for (p, q), v in b.items():
        if (p, q) == (0, 0):
            continue
        rad += arb(v.abs_upper()) * rx ** p * ry ** q
    rad = rad.abs_upper()
    return c0 + arb(0, rad)  # midpoint c0, extra radius rad


def lower(z):
    return z.lower()


def box_center_radius(xl, xh, yl, yh):
    cx = F2q((xl + xh) / 2); cy = F2q((yl + yh) / 2)
    rx = F2q((xh - xl) / 2); ry = F2q((yh - yl) / 2)
    return arb(cx), arb(cy), arb(rx), arb(ry)


def signed_positive_on(cards, s, xl, xh, yl, yh, depth=0, maxdepth=12, stats=None):
    """Prove s_i L_i > 0 on the closed box for all i; bisect if needed.
    Returns (ok, min_lower_bound)."""
    cx, cy, rx, ry = box_center_radius(xl, xh, yl, yh)
    bad = []
    mn = None
    for i, cf in enumerate(cards):
        a = taylor_shift(cf, cx, cy)
        val = enclose(a, rx, ry) * s[i]
        if not (val > 0):
            bad.append(i)
        else:
            lb = val.lower()
            mn = lb if mn is None or lb < mn else mn
    if not bad:
        return True, mn
    if depth >= maxdepth:
        return False, None
    if stats is not None:
        stats['bisections'] = stats.get('bisections', 0) + 1
    # bisect widest side (exact rationals) and recheck all cardinals on children
    if (xh - xl) >= (yh - yl):
        xm = (xl + xh) / 2
        kids = [(xl, xm, yl, yh), (xm, xh, yl, yh)]
    else:
        ym = (yl + yh) / 2
        kids = [(xl, xh, yl, ym), (xl, xh, ym, yh)]
    m2 = None
    for kb in kids:
        ok, m = signed_positive_on(cards, s, *kb, depth + 1, maxdepth, stats)
        if not ok:
            return False, None
        m2 = m if m2 is None or m < m2 else m2
    return True, m2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('witness_json')
    ap.add_argument('--prec', type=int, default=320)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    t0 = time.time()
    ctx.prec = args.prec
    raw = open(args.witness_json, 'rb').read()
    sha = hashlib.sha256(raw).hexdigest()
    d = json.loads(raw)
    recs = d['interior_roots']

    pts, idx = nodes_arb()
    assert len(pts) == 45
    cards, vinv_ok = vandermonde_cardinals(pts)
    form = formula_cardinals(pts, idx)
    overlap = all(cards[b][k].overlaps(form[b][k]) for b in range(45) for k in range(45))
    max_rad = max(float(cards[b][k].rad()) for b in range(45) for k in range(45))
    # partition of unity on coefficients
    pou = all(sum((cards[b][k] for b in range(45)), arb(0)).contains(1 if k == 0 else 0) for k in range(45))

    # physical embedding sanity of the supplied field intervals (reported only)
    fe = d.get('field_embedding', {})
    emb = {}
    try:
        al, ah = [Fraction(v) for v in fe['a_interval']]
        bl, bh = [Fraction(v) for v in fe['b_interval']]
        a_true = 2 * (arb.pi() / 8).cos(); b_true = 2 * (arb.pi() / 9).cos()
        emb = {'a_interval_contains_2cos(pi/8)': bool(a_true > arb(F2q(al)) and a_true < arb(F2q(ah))),
               'b_interval_contains_2cos(pi/9)': bool(b_true > arb(F2q(bl)) and b_true < arb(F2q(bh)))}
    except Exception as e:  # noqa
        emb = {'error': repr(e)}

    results = []
    boxes = []
    for r in recs:
        rid = r['id']; mask = int(r['mask'])
        res = {'id': rid, 'mask': str(mask)}
        (xl, xh), (yl, yh) = [[Fraction(v) for v in iv] for iv in r['R']]
        C = [[Fraction(v) for v in row] for row in r['C']]
        boxes.append((rid, xl, xh, yl, yh))
        s = [1 if (mask >> i) & 1 else -1 for i in range(45)]
        # (iv) strictly inside open square, nondegenerate
        res['iv_inside_open_square'] = bool(-1 < xl < xh < 1 and -1 < yl < yh < 1)
        cx, cy, rx, ry = box_center_radius(xl, xh, yl, yh)
        Ps = [sum((s[b] * cards[b][k] for b in range(45)), arb(0)) for k in range(len(POWERS))]
        a = taylor_shift(Ps, cx, cy)
        # gradient at exact centre
        gx = a[(1, 0)]; gy = a[(0, 1)]
        Hxx = enclose(deriv_shift(a, 2, 0), rx, ry)
        Hxy = enclose(deriv_shift(a, 1, 1), rx, ry)
        Hyy = enclose(deriv_shift(a, 0, 2), rx, ry)
        Ca = [[arb(F2q(C[i][j])) for j in range(2)] for i in range(2)]
        H = [[Hxx, Hxy], [Hxy, Hyy]]
        M = [[(arb(1) if i == j else arb(0)) - (Ca[i][0] * H[0][j] + Ca[i][1] * H[1][j]) for j in range(2)]
             for i in range(2)]
        Cg = [Ca[i][0] * gx + Ca[i][1] * gy for i in range(2)]
        rr = [rx, ry]; cc = [cx, cy]; lo = [xl, yl]; hi = [xh, yh]
        K = []
        for i in range(2):
            spread = arb(M[i][0].abs_upper()) * rr[0] + arb(M[i][1].abs_upper()) * rr[1]
            K.append(cc[i] - Cg[i] + arb(0, spread.abs_upper()))
        kin = all(bool(K[i] > arb(F2q(lo[i]))) and bool(K[i] < arb(F2q(hi[i]))) for i in range(2))
        row_norms = [arb(M[i][0].abs_upper()) + arb(M[i][1].abs_upper()) for i in range(2)]
        norm_ok = all(bool(rn < 1) for rn in row_norms)
        res['ii_krawczyk_inclusion'] = bool(kin)
        res['ii_contraction_norm_lt_1'] = bool(norm_ok)
        res['ii_contraction_norm_upper'] = float(max(rn.upper() for rn in row_norms))
        # margin of K inside R relative to box half-width
        res['ii_K_rel_margin'] = min(
            min(float(((K[i].lower() - arb(F2q(lo[i]))) / rr[i]).lower()),
                float(((arb(F2q(hi[i])) - K[i].upper()) / rr[i]).lower()))
            for i in range(2))
        det = Hxx * Hyy - Hxy * Hxy
        res['iii_Hxx_neg'] = bool(Hxx < 0)
        res['iii_det_pos'] = bool(det > 0)
        res['iii_Hxx_upper'] = float(Hxx.upper()); res['iii_det_lower'] = float(det.lower())
        stats = {}
        ok_pos, mn = signed_positive_on(cards, s, xl, xh, yl, yh, stats=stats)
        res['i_all_signed_cardinals_positive'] = bool(ok_pos)
        res['i_min_signed_cardinal_lower'] = float(mn) if mn is not None else None
        res['i_bisections'] = stats.get('bisections', 0)
        val = enclose(a, rx, ry)
        res['lambda_on_R_enclosure'] = [float(val.lower()), float(val.upper())]
        res['centre'] = [float(cx), float(cy)]
        res['all_ok'] = all([res['iv_inside_open_square'], res['ii_krawczyk_inclusion'],
                             res['ii_contraction_norm_lt_1'], res['iii_Hxx_neg'], res['iii_det_pos'],
                             res['i_all_signed_cardinals_positive']])
        results.append(res)
    # (v) pairwise disjointness
    overlaps = []
    for (i1, a1, b1, c1, d1), (i2, a2, b2, c2, d2) in combinations(boxes, 2):
        sep = (b1 < a2 or b2 < a1) or (d1 < c2 or d2 < c1)
        if not sep:
            overlaps.append([i1, i2])
    ids = [r['id'] for r in recs]
    nok = sum(1 for r in results if r['all_ok'])
    out = {
        'verifier': 'claude-audit-01 independent n8 witness verifier (no repo imports)',
        'input': args.witness_json, 'input_sha256': sha,
        'python': sys.version.split()[0], 'python_flint': flint.__version__, 'prec_bits': args.prec,
        'convention': 'nodes (cos(j pi/8), cos(k pi/9)), j+k even, lexicographic (j,k); mask bit i set <=> s_i=+1',
        'vandermonde_inverse_contains_identity': bool(vinv_ok),
        'formula_vs_vandermonde_all_coefficients_overlap': bool(overlap),
        'partition_of_unity_coefficients': bool(pou),
        'max_cardinal_coefficient_radius': max_rad,
        'supplied_embedding_check': emb,
        'n_records': len(recs), 'ids_unique': len(set(map(str, ids))) == len(ids),
        'v_pairwise_disjoint': not overlaps, 'overlapping_pairs': overlaps,
        'n_records_all_predicates_ok': nok,
        'independently_confirmed_lower_bound': nok if not overlaps else None,
        'supplied_metadata_ignored': {k: d.get(k) for k in ('observed_lower_bound', 'lower_bound_certified',
                                                           'completeness_certified', 'global_maximum_certified', 'scope')},
        'records': results,
        'seconds': time.time() - t0,
    }
    with open(args.output, 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'records'}, indent=1))
    return 0 if (nok == len(recs) and not overlaps and vinv_ok and overlap) else 1


if __name__ == '__main__':
    sys.exit(main())
