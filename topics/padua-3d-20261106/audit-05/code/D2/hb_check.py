"""Auditor-independent Padua Hilbert-Burch check (own Fraction polynomial arithmetic).

Usage: python -I hb_check.py <fd2-exact.json> <out.json>
Only SymPy's parser (to read recorded strings) and SymPy groebner (quotient check) are used.
"""
import itertools as it, json, sys, math
from fractions import Fraction as F
import mpmath as mp

# ---- tiny bivariate polynomial algebra: dict {(i,j): Fraction}
def padd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + s * v
        if r[k] == 0: del r[k]
    return r
def pmul(a, b):
    r = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            key = (i + k, j + l); r[key] = r.get(key, 0) + u * v
    return {k: v for k, v in r.items() if v != 0}
def pscale(a, c): return {k: v * c for k, v in a.items() if v * c != 0}
ONE = {(0, 0): F(1)}; X = {(1, 0): F(1)}; Y = {(0, 1): F(1)}
def cheb(k, var):
    t0, t1 = ONE, var
    if k == 0: return t0
    for _ in range(k - 1): t0, t1 = t1, padd(pscale(pmul(var, t1), 2), t0, -1)
    return t1
def det(M):  # Laplace expansion along first row, polynomial entries
    n = len(M)
    if n == 1: return M[0][0]
    r = {}
    for j in range(n):
        if not M[0][j]: continue
        sub = [row[:j] + row[j + 1:] for row in M[1:]]
        r = padd(r, pmul(M[0][j], det(sub)), (-1) ** j)
    return r
def nullspace(rows, ncols):  # rows: list of lists of Fraction; returns basis of kernel
    A = [r[:] for r in rows]; piv = []; rr = 0
    for c in range(ncols):
        p = next((i for i in range(rr, len(A)) if A[i][c] != 0), None)
        if p is None: continue
        A[rr], A[p] = A[p], A[rr]; inv = 1 / A[rr][c]; A[rr] = [v * inv for v in A[rr]]
        for i in range(len(A)):
            if i != rr and A[i][c] != 0:
                f = A[i][c]; A[i] = [u - f * v for u, v in zip(A[i], A[rr])]
        piv.append(c); rr += 1
    free = [c for c in range(ncols) if c not in piv]; basis = []
    for f in free:
        v = [F(0)] * ncols; v[f] = F(1)
        for i, c in enumerate(piv): v[c] = -A[i][f]
        basis.append(v)
    return basis
def rank(rows):
    if not rows: return 0
    return len(rows[0]) - len(nullspace(rows, len(rows[0])))

def from_sympy(e):
    import sympy as s
    x, y = s.symbols('x y')
    P = s.Poly(s.sympify(e), x, y)
    return {m: F(int(c.p), int(c.q)) for m, c in zip(P.monoms(), P.coeffs()) if c != 0}

def check(n, rec):
    q = [padd(cheb(n + 1, X), cheb(n - 1, X), -1)] + [
        padd(pmul(cheb(n + 1 - k, X), cheb(k, Y)), pmul(cheb(k - 1, X), cheb(n + 1 - k, Y)), -1)
        for k in range(1, n + 2)]
    out = {'n': n}
    rq = [from_sympy(g) for g in rec['generators']]
    out['generators_equal_recorded'] = (rq == q)
    # numerical vanishing at the N Padua points (60 digits), plus distinctness
    mp.mp.dps = 60
    pts = [(mp.cos(i * mp.pi / n), mp.cos(j * mp.pi / (n + 1))) for i in range(n + 1) for j in range(n + 2) if (i + j) % 2 == 0]
    out['padua_count'] = len(pts); out['N'] = (n + 1) * (n + 2) // 2
    ev = lambda p, P: sum(mp.mpf(v.numerator) / v.denominator * P[0] ** a * P[1] ** b for (a, b), v in p.items())
    out['max_abs_generator_at_points'] = float(max(abs(ev(g, P)) for g in q for P in pts))
    out['min_pair_distance'] = float(min(mp.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) for a, b in it.combinations(pts, 2)))
    # leading (degree n+1) forms span all n+2 degree-(n+1) monomials
    top = [[g.get((n + 1 - j, j), F(0)) for j in range(n + 2)] for g in q]
    out['top_forms_rank'] = rank(top)
    # linear syzygies: unknowns (a_i,b_i,c_i) with sum (a_i + b_i x + c_i y) q_i = 0
    mons = sorted({(i + di, j + dj) for g in q for (i, j) in g for di, dj in ((0, 0), (1, 0), (0, 1))})
    cols = [pmul(t, g) for g in q for t in (ONE, X, Y)]
    rows = [[c.get(m, F(0)) for c in cols] for m in mons]
    ns = nullspace(rows, len(cols)); out['linear_syzygy_dimension'] = len(ns)
    mine = [[{k: v for k, v in padd(padd(pscale(ONE, b[3*i]), pscale(X, b[3*i+1])), pscale(Y, b[3*i+2])).items()} for b in ns] for i in range(n + 2)]
    # recorded matrix
    H = [[from_sympy(e) for e in row] for row in rec['matrix']]
    zero = all(not functools_sum([pmul(q[i], H[i][j]) for i in range(n + 2)]) for j in range(n + 1))
    out['recorded_H_annihilates_q'] = zero
    def vec(h):  # linear form -> coefficient triple
        assert all(a + b <= 1 for a, b in h)
        return [h.get((0, 0), F(0)), h.get((1, 0), F(0)), h.get((0, 1), F(0))]
    Hcols = [sum((vec(H[i][j]) for i in range(n + 2)), []) for j in range(n + 1)]
    out['recorded_columns_rank'] = rank(Hcols)
    out['recorded_columns_span_equals_mine'] = rank(Hcols + ns) == len(ns) == rank(Hcols)
    sc = F(rec['minor_scale']) if '/' in rec['minor_scale'] else F(int(rec['minor_scale']))
    def minors(M):
        return [pscale(det([M[r] for r in range(n + 2) if r != i]), (-1) ** i) for i in range(n + 2)]
    mr = minors(H)
    out['recorded_minors_equal_scale_times_q'] = all(padd(a, pscale(b, sc), -1) == {} for a, b in zip(mr, q))
    mm = minors(mine)
    # find constant c with mm = c q
    c0 = next(v for k, v in mm[0].items()) / q[0][next(iter(mm[0]))] if mm[0] else None
    out['own_basis_minors_proportional'] = c0 is not None and c0 != 0 and all(padd(a, pscale(b, c0), -1) == {} for a, b in zip(mm, q))
    out['own_basis_minor_scale'] = str(c0)
    out['recorded_nonzero_entries'] = sum(1 for row in H for e in row if e)
    out['own_rref_basis_nonzero_entries'] = sum(1 for row in mine for e in row if e)
    # Groebner quotient check of (q) over Q
    import sympy as s
    x, y = s.symbols('x y')
    expr = lambda p: sum(s.Rational(v.numerator, v.denominator) * x ** a * y ** b for (a, b), v in p.items())
    G = s.groebner([expr(g) for g in q], x, y, order='grevlex', method='buchberger')
    lm = [p.LM(order=G.order).exponents for p in G.polys]
    std = [(a, b) for a in range(2 * n + 4) for b in range(2 * n + 4) if not any(a >= u and b >= v for u, v in lm)]
    out['groebner_quotient_dimension'] = len(std)
    out['standard_monomials_are_deg_le_n'] = sorted(std) == sorted((a, b) for a in range(n + 1) for b in range(n + 1 - a))
    return out

def functools_sum(ps):
    r = {}
    for p in ps: r = padd(r, p)
    return r

if __name__ == '__main__':
    rec = json.load(open(sys.argv[1]))
    res = [check(r['n'], r) for r in rec['padua']]
    json.dump(res, open(sys.argv[2], 'w'), indent=1, sort_keys=True)
    for r in res: print(r)
