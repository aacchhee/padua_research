#!/usr/bin/env python3
"""Independent Claude audit checker for padua-3d-20261106 directions T2/T3.

Written from the mathematical statements only; imports no repository code.
Proof-relevant parts use Python integers / Fractions only.

  A  monomial-basis Laurent check mod t^M-1 of every H39 null polynomial
  B  per-node evaluation in the field Q[t]/Phi_39(t) (t -> primitive 39th root)
  C  end-to-end reduction over all 39^3 residue triples z (T3-02 statement)
  D  exact Q-rank screen n=2,3,4 in the MONOMIAL basis (independent of D matrix)
  E  K/T/O quadratic falsifiers at n=2 and n=1 full rank
  F  T3 short-relation annihilators (symbolic + exact per-node with phases)
  G  T3-01 factorization V = 2^-d F B exactly in Q(zeta_L), zero-index sign
     multiplicities, folded D at zero phase
  H  (MEASURED only) floating sampled Lebesgue values of the eight survivors
Usage: python claude_t23_check.py /path/to/t2-n3-null-cover.json
"""
import itertools, json, math, sys, random, hashlib
from fractions import Fraction

# ---------------------------------------------------------------- algebra
def cheb_coeffs(a):
    """Monomial coefficients of T_a (index = power), via T_{a+1}=2xT_a-T_{a-1}."""
    if a == 0:
        return [1]
    prev, cur = [1], [0, 1]
    for _ in range(1, a):
        nxt = [0] * (len(cur) + 1)
        for i, c in enumerate(cur):
            nxt[i + 1] += 2 * c
        for i, c in enumerate(prev):
            nxt[i] -= c
        prev, cur = cur, nxt
    return cur

def cheb_to_mono(terms):
    """terms: iterable of (alpha tuple, int coeff) in product-Chebyshev basis."""
    poly = {}
    for alpha, v in terms:
        cs = [cheb_coeffs(a) for a in alpha]
        for idx in itertools.product(*[range(len(c)) for c in cs]):
            w = v
            for c, i in zip(cs, idx):
                w *= c[i]
            if w:
                poly[idx] = poly.get(idx, 0) + w
    return {k: v for k, v in poly.items() if v}

def laurent_mono(poly, freqs, M, D):
    """2^D * P((t^f+t^-f)/2 ...) reduced in Z[t]/(t^M-1), via binomial expansion."""
    out = [0] * M
    for e, v in poly.items():
        assert sum(e) <= D
        parts = []
        for ej, f in zip(e, freqs):
            parts.append([(math.comb(ej, m), f * (2 * m - ej)) for m in range(ej + 1)])
        scale = v * 2 ** (D - sum(e))
        for combo in itertools.product(*parts):
            c = scale
            s = 0
            for (bc, ex) in combo:
                c *= bc
                s += ex
            out[s % M] += c
    return out

def poly_divmod(a, b):
    """Integer polynomials (lists, low->high), b monic. Returns quotient, remainder."""
    a = a[:]
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        if a[-1] == 0:
            a.pop(); continue
        sh = len(a) - len(b)
        c = a[-1]
        q[sh] = c
        for i, x in enumerate(b):
            a[sh + i] -= c * x
        a.pop()
    while a and a[-1] == 0:
        a.pop()
    return q, a

_phi = {}
def cyclo(n):
    """Phi_n by exact division of t^n-1 by Phi_d, d|n, d<n."""
    if n in _phi:
        return _phi[n]
    p = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            p, r = poly_divmod(p, cyclo(d))
            assert not r
    while p[-1] == 0:
        p.pop()
    _phi[n] = p
    return p

class Field:
    """Q(zeta_L) = Z[t]/Phi_L with integer arithmetic (elements scaled by 2^D)."""
    def __init__(self, L):
        self.L = L
        self.phi = cyclo(L)
        self.deg = len(self.phi) - 1
    def red(self, a):
        _, r = poly_divmod(a, self.phi)
        return r
    def mul(self, a, b):
        if not a or not b:
            return []
        c = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    c[i + j] += x * y
        return self.red(c)
    def add(self, a, b):
        n = max(len(a), len(b))
        c = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
        while c and c[-1] == 0:
            c.pop()
        return c
    def scal(self, a, s):
        return self.red([s * x for x in a])
    def tpow(self, e):
        e %= self.L
        return self.red([0] * e + [1])
    def two_cos(self, e):
        return self.add(self.tpow(e), self.tpow(-e))

def eval_node_field(F, poly, exps, D):
    """2^D * P(node) in F, node coords (zeta^e_j + zeta^-e_j)/2; poly monomial.
    Returns [] iff the node value is exactly zero (Q[t]/Phi_L is a field and
    t -> exp(2 pi i/L) embeds it in C)."""
    cache = F.__dict__.setdefault('_pw', {})
    def pw(e, p):
        key = (e % F.L, p)
        if key not in cache:
            cache[key] = [1] if p == 0 else F.mul(pw(e, p - 1), F.two_cos(e))
        return cache[key]
    tot = []
    for e, v in poly.items():
        term = [v * 2 ** (D - sum(e))]
        for j, ej in enumerate(e):
            if ej:
                term = F.mul(term, pw(exps[j], ej))
        tot = F.add(tot, term)
    return tot

def fold(s, M):
    s %= M
    return min(s, M - s)

def exact_rank(rows):
    """Rank over Q of an integer matrix (list of lists), Fraction-free elimination."""
    A = [r[:] for r in rows if any(r)]
    if not A:
        return 0
    ncol = len(A[0]); rank = 0; piv_row = 0
    for col in range(ncol):
        p = next((i for i in range(piv_row, len(A)) if A[i][col]), None)
        if p is None:
            continue
        A[piv_row], A[p] = A[p], A[piv_row]
        pr = A[piv_row]
        for i in range(len(A)):
            if i != piv_row and A[i][col]:
                a, b = pr[col], A[i][col]
                A[i] = [a * x - b * y for x, y in zip(A[i], pr)]
                g = math.gcd(*A[i])
                if g > 1:
                    A[i] = [x // g for x in A[i]]
        piv_row += 1; rank += 1
        if piv_row == len(A):
            break
    return rank

def mono_basis(n):
    return [e for e in itertools.product(range(n + 1), repeat=3) if sum(e) <= n]

# ---------------------------------------------------------------- parts
LOG = {}

def part_AB(cover):
    assert (cover['n'], cover['N'], cover['M'], cover['count']) == (3, 20, 39, 171)
    want = set(itertools.combinations(range(1, 20), 2))
    got = [(b, c) for b, c, _, _ in cover['witnesses']]
    assert len(got) == 171 and set(got) == want, 'coverage'
    F = Field(39)
    assert F.deg == 24
    stats = {'laurent_zero': 0, 'field_zero_nodes': 0, 'nonzero': 0, 'maxdeg': 0}
    store = {}
    for b, c, rank, terms in cover['witnesses']:
        alphas = [tuple(a) for a, _ in terms]
        assert len(set(alphas)) == len(alphas)
        assert all(len(a) == 3 and min(a) >= 0 and sum(a) <= 3 for a in alphas)
        assert all(isinstance(v, int) and v != 0 for _, v in terms)
        mono = cheb_to_mono([(tuple(a), v) for a, v in terms])
        assert mono, 'zero polynomial'
        stats['nonzero'] += 1
        stats['maxdeg'] = max(stats['maxdeg'], max(sum(e) for e in mono))
        assert all(x == 0 for x in laurent_mono(mono, (1, b, c), 39, 3)), (b, c)
        stats['laurent_zero'] += 1
        for k in range(20):   # k and 39-k give the same node
            val = eval_node_field(F, mono, (k, k * b, k * c), 3)
            assert val == [], (b, c, k)
            stats['field_zero_nodes'] += 1
        # distinct node count for z=(1,b,c): exactly 20
        nodes = {(fold(k, 39), fold(k * b, 39), fold(k * c, 39)) for k in range(39)}
        assert len(nodes) == 20
        store[(b, c)] = (terms, rank)
    LOG['AB'] = stats
    return store

def part_C(store):
    """All residue triples z mod 39: produce a verified annihilator or <20 nodes."""
    M = 39
    units = {u for u in range(M) if math.gcd(u, M) == 1}
    cnt = {'total': 0, 'lt20_nodes': 0, 'quad13': 0, 'linear': 0, 'cover': 0,
           'unit_triples_with_20_nodes': 0}
    hit = set()
    for z in itertools.product(range(M), repeat=3):
        cnt['total'] += 1
        nodes = {tuple(fold(k * zj, M) for zj in z) for k in range(M)}
        uidx = [i for i in range(3) if z[i] in units]
        if not uidx:
            if any(zj % 13 == 0 for zj in z):
                j = next(i for i in range(3) if z[i] % 13 == 0)
                # (x_j-1)(2x_j+1) = 2x^2 - x - 1
                e = lambda p: tuple(p if i == j else 0 for i in range(3))
                poly = {e(2): 2, e(1): -1, e(0): -1}
                assert all(x == 0 for x in laurent_mono(poly, z, M, 3))
                cnt['quad13'] += 1
            else:
                assert all(zj % 3 == 0 for zj in z)
                assert len(nodes) <= 7, (z, len(nodes))
                cnt['lt20_nodes'] += 1
            continue
        assert len(nodes) == 20, z
        cnt['unit_triples_with_20_nodes'] += 1
        i = uidx[0]
        u = pow(z[i], -1, M)
        others = [j for j in range(3) if j != i]
        w = {j: fold(u * z[j], M) for j in others}
        j1, j2 = sorted(others, key=lambda j: (w[j], j))
        b, c = w[j1], w[j2]
        def lin(p, q):  # x_p - x_q  (q=None -> x_p - 1)
            poly = {tuple(1 if t == p else 0 for t in range(3)): 1}
            key = (0, 0, 0) if q is None else tuple(1 if t == q else 0 for t in range(3))
            poly[key] = poly.get(key, 0) - 1
            return poly
        if b == 0:
            poly = lin(j1, None); cnt['linear'] += 1
        elif b == 1:
            poly = lin(j1, i); cnt['linear'] += 1
        elif b == c:
            poly = lin(j1, j2); cnt['linear'] += 1
        else:
            terms, _ = store[(b, c)]
            hit.add((b, c))
            axis = (i, j1, j2)   # cover variable v -> original axis axis[v]
            mapped = []
            for a, v in terms:
                beta = [0, 0, 0]
                for vv in range(3):
                    beta[axis[vv]] = a[vv]
                mapped.append((tuple(beta), v))
            poly = cheb_to_mono(mapped)
            cnt['cover'] += 1
        assert poly and all(x == 0 for x in laurent_mono(poly, z, M, 3)), z
    cnt['distinct_cover_pairs_used'] = len(hit)
    LOG['C'] = cnt

def part_D(cover_ranks):
    out = {}
    for n in (2, 3, 4):
        N = math.comb(n + 3, 3); M = 2 * N - 1
        basis = mono_basis(n); assert len(basis) == N
        dist = {}; full = []; ranks = {}
        for b, c in itertools.combinations(range(1, N), 2):
            cols = [laurent_mono({e: 1}, (1, b, c), M, n) for e in basis]
            rows = [list(r) for r in zip(*cols)]   # M x N
            r = exact_rank(rows)
            ranks[(b, c)] = r
            dist[r] = dist.get(r, 0) + 1
            if r == N:
                full.append((1, b, c))
        out[n] = {'count': sum(dist.values()), 'dist': dict(sorted(dist.items())),
                  'max': max(dist), 'full': full}
        if n == 3:
            mism = [(k, ranks[k], cover_ranks[k]) for k in ranks if ranks[k] != cover_ranks[k]]
            out[n]['cover_rank_mismatches'] = mism
    LOG['D'] = out

def part_E():
    F = Field(19)
    res = {}
    fam = {'K': ((1, 3, 9), [((0, 0, 2), 1), ((1, 0, 0), -1)]),
           'T': ((1, 3, 6), [((0, 2, 0), 1), ((0, 0, 1), -1)]),
           'O': ((1, 5, 13), [((1, 0, 1), 2), ((0, 1, 0), -1), ((0, 0, 2), -1)])}
    for name, (z, terms) in fam.items():
        mono = cheb_to_mono(terms)
        assert mono and max(sum(e) for e in mono) == 2
        assert all(x == 0 for x in laurent_mono(mono, z, 19, 2))
        assert all(eval_node_field(F, mono, tuple(k * zj for zj in z), 2) == [] for k in range(19))
        # n=1 generators and exact rank 4 (M=7)
        n1 = {'K': (1, 2, 4), 'T': (1, 2, 3), 'O': (1, 3, 5)}[name]
        cols = [laurent_mono({e: 1}, n1, 7, 1) for e in mono_basis(1)]
        r1 = exact_rank([list(r) for r in zip(*cols)])
        cols2 = [laurent_mono({e: 1}, z, 19, 2) for e in mono_basis(2)]
        r2 = exact_rank([list(r) for r in zip(*cols2)])
        res[name] = {'n2_annihilator_zero': True, 'n1_rank': r1, 'n2_rank': r2}
    LOG['E'] = res

def short_poly(u, delta):
    """Chebyshev-basis annihilator of T3 short relations; returns (terms, q)."""
    S = [j for j in range(3) if u[j]]
    a = [abs(x) for x in u]
    s = (-1) ** delta
    e = lambda d: tuple(d.get(j, 0) for j in range(3))
    if len(S) == 1:
        i = S[0]
        return [(e({i: a[i]}), 1), (e({}), -s)], a[i]
    if len(S) == 2:
        i, j = S
        return [(e({i: a[i]}), 1), (e({j: a[j]}), -s)], max(a[i], a[j])
    # U^2+V^2+W^2-2sUVW-1 with T_a^2 = (T_2a + 1)/2  -> scale by 2
    terms = [(e({0: 2 * a[0]}), 1), (e({1: 2 * a[1]}), 1), (e({2: 2 * a[2]}), 1),
             (e({}), 1), (e({0: a[0], 1: a[1], 2: a[2]}), -4 * s)]
    return terms, max(2 * a[0], 2 * a[1], 2 * a[2], sum(a))

def part_F():
    import sympy as sp
    A, B, sg = sp.symbols('A B s')
    for s in (1, -1):
        U, V, W = sp.cos(A), sp.cos(B), s * sp.cos(A + B)
        expr = sp.expand_trig(U**2 + V**2 + W**2 - 2 * s * U * V * W - 1)
        assert sp.simplify(expr) == 0
    rnd = random.Random(20261106)
    cases = 0; degs_ok = 0; supp_sizes = {}
    for _ in range(60):
        L = rnd.choice([12, 20, 24, 30, 36, 40])
        Ms = [m for m in range(3, L + 1) if L % m == 0]
        M = rnd.choice(Ms)
        z = [rnd.randrange(M) for _ in range(3)]
        supp = rnd.choice([[0], [1], [0, 1], [0, 2], [0, 1, 2], [0, 1, 2]])
        # find u supported on supp with u.z = 0 mod M, small entries
        cand = [u for u in itertools.product(range(-4, 5), repeat=3)
                if all((u[j] != 0) == (j in supp) for j in range(3))
                and sum(x * y for x, y in zip(u, z)) % M == 0]
        if not cand:
            continue
        u = rnd.choice(cand)
        # phases phi_j = 2 pi a_j / L with u.a = delta*L/2 (mod L), L even
        delta = rnd.randrange(2)
        for _t in range(200):
            aph = [rnd.randrange(L) for _ in range(3)]
            if sum(x * y for x, y in zip(u, aph)) % L == (delta * L // 2) % L:
                break
        else:
            continue
        terms, q = short_poly(u, delta)
        mono = cheb_to_mono(terms)
        assert mono and max(sum(e) for e in mono) == q
        degs_ok += 1
        F = Field(L)
        D = max(sum(e) for e in mono)
        for k in range(M):
            exps = tuple(aph[j] + k * z[j] * (L // M) for j in range(3))
            assert eval_node_field(F, mono, exps, D) == [], (L, M, z, u, aph, k)
        cases += 1
        key = f'supp{len(supp)}_delta{delta}'
        supp_sizes[key] = supp_sizes.get(key, 0) + 1
    LOG['F'] = {'symbolic_identity': True, 'random_exact_cases': cases, 'degree_equals_q': degs_ok, 'by_support': supp_sizes}

def part_G():
    """V = 2^-d F B exactly in Q(zeta_L); B keeps all 2^d sign choices."""
    rnd = random.Random(7)
    checked = 0
    for (d, n, M, L) in [(3, 2, 7, 28), (3, 2, 9, 18), (2, 3, 8, 16), (3, 1, 5, 20)]:
        F = Field(L)
        r = L // M
        z = [rnd.randrange(1, M) for _ in range(d)]
        aph = [rnd.randrange(L) for _ in range(d)]
        I = [e for e in itertools.product(range(n + 1), repeat=d) if sum(e) <= n]
        for alpha in I:
            # B[r,alpha] in Q(zeta_L) as element; scaled by nothing
            Bcol = [[] for _ in range(M)]
            for eps in itertools.product((-1, 1), repeat=d):
                rr = sum(e * a * zz for e, a, zz in zip(eps, alpha, z)) % M
                ph = sum(e * a * p for e, a, p in zip(eps, alpha, aph))
                Bcol[rr] = F.add(Bcol[rr], F.tpow(ph))
            for k in range(M):
                # 2^d V[k,alpha] via Chebyshev values from node coords
                val = [1]
                for j in range(d):
                    two_x = F.two_cos(aph[j] + k * z[j] * r)
                    # T_a(x) * 2 computed from recurrence on 2x: 2T_{a+1}=2x*2T_a - 2T_{a-1}... use cos identity-free recurrence
                    t_prev, t_cur = [2], two_x       # 2*T_0, 2*T_1
                    for _ in range(1, alpha[j]):
                        t_prev, t_cur = t_cur, F.add(F.mul(two_x, t_cur), F.scal(t_prev, -1))
                    twoT = [2] if alpha[j] == 0 else t_cur
                    val = F.mul(val, twoT)
                rhs = []
                for rr in range(M):
                    rhs = F.add(rhs, F.mul(F.tpow(k * rr * r), Bcol[rr]))
                assert val == rhs, (d, n, M, alpha, k)
                checked += 1
    # dedup-at-zero-index variant has wrong scaling: alpha=0 column would be 1 not 2^d
    LOG['G'] = {'entries_checked_exactly': checked}

def part_H():
    """MEASURED floating sampled Lebesgue values (not proof)."""
    import numpy as np
    from numpy.polynomial import chebyshev as C
    g = np.cos(np.pi * np.arange(21) / 20)
    mesh = np.array(list(itertools.product(g, repeat=3)))
    out = {}
    for n, gens in {2: [(1, 3, 7), (1, 4, 6), (1, 5, 8), (1, 7, 8)],
                    4: [(1, 11, 15), (1, 15, 19), (1, 21, 29), (1, 25, 30)]}.items():
        N = math.comb(n + 3, 3); M = 2 * N - 1
        I = mono_basis(n)
        def ev(P):
            cols = []
            for a in I:
                v = np.ones(len(P))
                for j in range(3):
                    cc = np.zeros(a[j] + 1); cc[-1] = 1
                    v = v * C.chebval(P[:, j], cc)
                cols.append(v)
            return np.array(cols).T
        Emesh = ev(mesh)
        for z in gens:
            P = np.cos(2 * np.pi * np.arange(N)[:, None] * np.array(z)[None, :] / M)
            V = ev(P)
            Lag = np.linalg.solve(V.T, Emesh.T)   # N x mesh
            out[f'n{n}{z}'] = round(float(np.abs(Lag).sum(0).max()), 10)
    LOG['H'] = out

if __name__ == '__main__':
    path = sys.argv[1]
    raw = open(path, 'rb').read()
    LOG['input_sha256'] = hashlib.sha256(raw).hexdigest()
    LOG['checker_sha256'] = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    cover = json.loads(raw)
    store = part_AB(cover); print('AB', LOG['AB'], flush=True)
    part_C(store); print('C', LOG['C'], flush=True)
    part_E(); print('E', LOG['E'], flush=True)
    part_F(); print('F', LOG['F'], flush=True)
    part_G(); print('G', LOG['G'], flush=True)
    part_D({k: v[1] for k, v in store.items()}); print('D', json.dumps({k: v for k, v in LOG['D'].items()}, default=str), flush=True)
    part_H(); print('H', LOG['H'], flush=True)
    print('ALL ASSERTIONS PASSED')
