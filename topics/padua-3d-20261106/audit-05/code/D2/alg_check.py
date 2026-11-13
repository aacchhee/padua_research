"""Auditor-independent replay of D2 R1 exact algebra cases.

Own pencil reconstruction (checked against recorded matrix_sha256), own integer
minor expansion, SymPy groebner with method='buchberger' (producer used f5b),
own standard-monomial enumeration, multiplication matrix for a DIFFERENT linear
form, and squarefree test.  Usage: python -I alg_check.py fd2-exact.json out.json n,typ,fam,field ...
"""
import hashlib, itertools as it, json, math, random, sys, time
import sympy as s

P = 1000003
x, y, z = s.symbols('x y z')

def digest(obj): return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()

# polynomials as dict {(a,b,c): int}
def padd(a, b, sg=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + sg * v
        if r[k] == 0: del r[k]
    return r
def pmul(a, b):
    r = {}
    for k1, u in a.items():
        for k2, v in b.items():
            k = (k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2]); r[k] = r.get(k, 0) + u*v
    return {k: v for k, v in r.items() if v}
def det(M, memo=None):
    n = len(M)
    if n == 1: return M[0][0]
    r = {}
    for j in range(n):
        if not M[0][j]: continue
        r = padd(r, pmul(M[0][j], det([row[:j]+row[j+1:] for row in M[1:]])), (-1)**j)
    return r
def lin(c): return {m: v for m, v in zip(((0,0,0),(1,0,0),(0,1,0),(0,0,1)), c) if v}

def pencil(n, typ, fam, field):
    k = n+1 if typ == 'en' else n+2
    rows = n+3 if typ == 'en' else k
    seed = 202611120201 + 100*n + 10*(typ == 'sym') + (field == 'Q')
    if fam == 'structured':
        pl = [[-t**3, 1, t, t*t] for t in range(n+3)]
        if typ == 'en':   # diag(l_t) * B, B rows (1,t,..,t^n)
            C = [[[pl[t][a]*t**j for a in range(4)] for j in range(k)] for t in range(n+3)]
        else:             # diag(l_0..l_{k-1}) + l_k 11^T
            C = [[[pl[k][a] + (pl[i][a] if i == j else 0) for a in range(4)] for j in range(k)] for i in range(k)]
    else:
        rng = random.Random(seed); mats = []
        for _ in range(4):
            m = [[rng.randint(-2, 2) for j in range(k)] for i in range(rows)]  # row-major
            if typ == 'sym': m = [[m[min(i, j)][max(i, j)] for j in range(k)] for i in range(k)]
            mats.append(m)
        C = [[[mats[a][i][j] for a in range(4)] for j in range(k)] for i in range(rows)]
    return C, seed, k, rows

def generators(C, typ, k, rows):
    M = [[lin(c) for c in row] for row in C]
    if typ == 'en':
        return [det([M[r] for r in keep]) for keep in it.combinations(range(rows), k)]
    return [det([[M[r][c] for c in range(k) if c != j] for r in range(k) if r != i]) for i in range(k) for j in range(i, k)]

def run(n, typ, fam, field, rec):
    t0 = time.process_time()
    C, seed, k, rows = pencil(n, typ, fam, field)
    out = {'case': [n, typ, fam, field], 'seed': seed, 'matrix_sha256_match': (digest(C) == rec['matrix_sha256']) if 'matrix_sha256' in rec else 'not recorded'}
    gs = [g for g in generators(C, typ, k, rows) if g]
    out['nonzero_generators'] = len(gs)
    kw = {'modulus': P} if field == 'GF' else {'domain': s.QQ}
    ex = [sum(v * x**a * y**b * z**c for (a, b, c), v in g.items()) for g in gs]
    G = s.groebner(ex, x, y, z, order='grevlex', method='buchberger', **kw)
    out['gb_sha256_match_recorded_f5b'] = (digest([str(p.as_expr()) for p in G.polys]) == rec['gb_sha256']) if 'gb_sha256' in rec else 'not recorded'
    lm = [p.LM(order=G.order).exponents for p in G.polys]
    pure = [any(e[v] > 0 and sum(e) == e[v] for e in lm) for v in range(3)]
    out['zero_dimensional_pure_powers'] = all(pure)
    D = 3 * (2*n + 4)
    std = [a for a in it.product(range(D), repeat=3) if not any(all(u >= w for u, w in zip(a, b)) for b in lm)]
    N = math.comb(n+3, 3)
    out['quotient_dimension'] = len(std)
    out['standard_equals_deg_le_n'] = sorted(std) == sorted(a for a in it.product(range(n+1), repeat=3) if sum(a) <= n)
    # multiplication by a different form, 5x - 7y + 11z
    pos = {a: i for i, a in enumerate(std)}
    Mx = s.zeros(len(std))
    for j, a in enumerate(std):
        rem = G.reduce(s.expand((5*x - 7*y + 11*z) * x**a[0] * y**a[1] * z**a[2]))[1]
        for b, c in s.Poly(rem, x, y, z, **kw).terms(): Mx[pos[b], j] = c
    u = s.Symbol('u')
    f = s.Poly(Mx.charpoly(u).as_expr(), u, **kw)
    out['charpoly_degree'] = f.degree()
    out['squarefree_5x-7y+11z'] = s.gcd(f, f.diff(u)).degree() == 0
    out['recorded'] = {kk: rec.get(kk) for kk in ('quotient_dimension', 'all_degree_le_n_standard', 'radicality')}
    out['cpu'] = time.process_time() - t0
    return out

if __name__ == '__main__':
    rec = json.load(open(sys.argv[1]))
    byk = {(c['n'], c['type'], c['family'], c['field']): c for c in rec['cases']}
    res = []
    for spec in sys.argv[3:]:
        n, typ, fam, field = spec.split(','); n = int(n)
        r = run(n, typ, fam, field, byk[(n, typ, fam, field)]); res.append(r); print(json.dumps(r), flush=True)
        json.dump(res, open(sys.argv[2], 'w'), indent=1)
