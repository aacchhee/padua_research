"""Auditor checks for D2 R2: natural lattice (exact, n=1..8), exact ranks of both
structured pencils at the nodes, ORSV and bordered real-node counts (exact Groebner +
Sturm counting).  Usage: python -I real_check.py fd2-real.json out.json [maxsize]"""
import itertools as it, json, math, sys, time
from fractions import Fraction as F
import numpy as np
import sympy as s

def frank(M):
    A = [[F(v) for v in r] for r in M]; r = 0
    for c in range(len(A[0])):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]; A[i] = [u - f * v for u, v in zip(A[i], A[r])]
        r += 1
    return r

def natural(n):
    m = n + 3; ts = range(m); ids = list(it.combinations(ts, 3))
    P = [(a*b*c, -(a*b+a*c+b*c), a+b+c) for a, b, c in ids]
    l = lambda t, p: p[0] + t*p[1] + t*t*p[2] - t**3
    ok_id = all(l(t, p) == -(t-a)*(t-b)*(t-c) for (a, b, c), p in zip(ids, P) for t in ts)
    distinct = len(set(P)) == math.comb(n+3, 3)
    card = all((math.prod(l(t, q) for t in ts if t not in I) != 0) == (I == J) for I in ids for J, q in zip(ids, P))
    # exact ranks of the two structured pencils at every node, and full rank at 5 random rational points
    k = n + 2
    def EN(p): return [[l(t, p) * t**j for j in range(n+1)] for t in ts]
    def SYM(p): return [[l(k, p) + (l(i, p) if i == j else 0) for j in range(k)] for i in range(k)]
    en_ok = all(frank(EN(p)) == n for p in P)
    sym_ok = all(frank(SYM(p)) == k - 2 for p in P)
    rng = np.random.default_rng(1)
    rnd = [tuple(F(int(v), 7) for v in rng.integers(-50, 50, 3)) for _ in range(5)]
    generic = all(frank(EN(p)) == n + 1 and frank(SYM(p)) >= k - 1 for p in rnd)
    lo = [min(c) for c in zip(*P)]; hi = [max(c) for c in zip(*P)]
    return {'n': n, 'N': len(P), 'distinct': distinct, 'l_t(p_I)=-(t-a)(t-b)(t-c)': ok_id,
            'cardinal_products_exact': card, 'EN_rank_n_at_all_nodes': en_ok,
            'SYM_corank2_at_all_nodes': sym_ok, 'generic_points_not_on_locus': generic,
            'positive_widths': all(h > q for h, q in zip(hi, lo))}

ORSV = [
 [[18,6,6,-6],[6,2,2,-2],[6,2,2,-2],[-6,-2,-2,4]],
 [[4,-6,6,4],[-6,13,-9,-8],[6,-9,9,6],[4,-8,6,5]],
 [[1,0,-3,0],[0,4,0,6],[-3,0,9,0],[0,6,0,9]],
 [[9,-3,0,0],[-3,10,9,-6],[0,9,9,-6],[0,-6,-6,4]]]

def orsv_pencil(k):
    X = s.symbols('a b c')
    A = [[[s.Integer(0)]*k for _ in range(k)] for _ in range(4)]
    for a in range(4):
        for i in range(4):
            for j in range(4):
                A[a][i][j] = s.Integer(ORSV[a][i][j]) - (s.Integer([0, 2, 4, 8][a]) * ORSV[0][i][j] if a else 0)
    for j in range(4, k):
        t = j + 1
        for a, v in enumerate([-t**3, 1, t, t*t]): A[a][j][j] = s.Integer(v)
        for i in range(j):
            A[0][j][i] = A[0][i][j] = s.Rational(1, 10)
            A[1][j][i] = A[1][i][j] = s.Rational(3, 100)
    M = s.Matrix(k, k, lambda i, j: A[0][i][j] + sum(X[a-1]*A[a][i][j] for a in (1, 2, 3)))
    return M, X

def count_real(k, budget):
    t0 = time.process_time()
    M, X = orsv_pencil(k)
    gs = [s.expand(M.extract([r for r in range(k) if r != i], [c for c in range(k) if c != j]).det(method='berkowitz'))
          for i in range(k) for j in range(i, k)]
    G = s.groebner(gs, *X, order='grevlex', method='buchberger', domain=s.QQ)
    lm = [p.LM(order=G.order).exponents for p in G.polys]
    std = [e for e in it.product(range(4*k), repeat=3) if not any(all(u >= w for u, w in zip(e, b)) for b in lm)]
    pos = {e: i for i, e in enumerate(std)}
    form = 5*X[0] - 7*X[1] + 11*X[2]
    Mx = s.zeros(len(std))
    for j, e in enumerate(std):
        rem = G.reduce(s.expand(form * X[0]**e[0] * X[1]**e[1] * X[2]**e[2]))[1]
        for b, c in s.Poly(rem, *X).terms(): Mx[pos[b], j] = c
    u = s.Symbol('u'); f = s.Poly(Mx.charpoly(u).as_expr(), u, domain=s.QQ)
    sqf = s.gcd(f, f.diff(u)).degree() == 0
    nreal = int(s.Poly(f, u).count_roots()) if sqf else None
    return {'size': k, 'quotient_dimension': len(std), 'expected': math.comb(k+1, 3),
            'charpoly_squarefree': sqf, 'exact_real_points_in_chart': nreal, 'cpu': time.process_time() - t0}

if __name__ == '__main__':
    rec = json.load(open(sys.argv[1])); out = {'natural': [natural(n) for n in range(1, 9)]}
    for r in out['natural']: print(r, flush=True)
    # compare recorded natural nodes
    out['recorded_natural_nodes_match'] = all(
        sorted(map(tuple, r['raw_integer_nodes'])) == sorted((a*b*c, -(a*b+a*c+b*c), a+b+c) for a, b, c in it.combinations(range(r['n']+3), 3))
        for r in rec['natural'])
    print('recorded natural nodes match', out['recorded_natural_nodes_match'])
    out['orsv'] = []
    for k in range(4, int(sys.argv[3]) + 1 if len(sys.argv) > 3 else 6):
        r = count_real(k, None); r['recorded_found'] = rec['orsv'][k-4]['real_distinct_nodes_found']; out['orsv'].append(r); print(r, flush=True)
        json.dump(out, open(sys.argv[2], 'w'), indent=1)
    json.dump(out, open(sys.argv[2], 'w'), indent=1)
