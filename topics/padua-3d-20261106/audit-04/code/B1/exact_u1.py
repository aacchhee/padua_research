#!/usr/bin/env python3
"""Auditor audit04-B1 exact checks of the U1 parity algebra (own code).

Exact integer / rational / cyclotomic arithmetic only (no producer code).
 (a) folded enumeration and multiplicities from explicit Haar-group preimages
 (b) Gram by an exact character-sum formula, all n<=16, both families
 (c) Gram by exact cyclotomic group-ring sums over the actual folded nodes, n<=6
 (d) exact tr(C_W C_W^T) at n=1..16 via exact diag(V^T W^2 V)
 (e) exact OLS tr((V^T V)^-1) and Gauss-Markov identity, n=1..4
 (f) generic exact rational Gauss-Markov and GLS weighted identities
"""
import itertools as it, json, math, sys, random
from fractions import Fraction as F
import numpy as np
import sympy

out = {}

def exps(n):
    return [(a, b, d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]

def orders(n, equal):
    return (n+1,)*3 if equal else (n, n+1, n+1)

def folded_nodes(m):
    ids = [i for i in it.product(*(range(v+1) for v in m)) if i[0] % 2 == i[1] % 2 == i[2] % 2]
    mult = [math.prod(1 if (i[j] == 0 or i[j] == m[j]) else 2 for j in range(3)) for i in ids]
    return ids, mult

def group_preimages(m):
    """Count preimages of each folded index under the explicit Haar group."""
    cnt = {}
    def fold(t, mj):  # t = numerator of angle pi*t/mj, t in [0, 2mj)
        t %= 2*mj
        return t if t <= mj else 2*mj - t
    for grid in (0, 1):
        for r in it.product(*(range(v) for v in m)):
            idx = tuple(fold(2*r[j] + grid, m[j]) for j in range(3))
            cnt[idx] = cnt.get(idx, 0) + 1
    return cnt

# (a)
part_a = []
for equal in (False, True):
    for n in range(1, 21):
        m = orders(n, equal)
        ids, mult = folded_nodes(m)
        pre = group_preimages(m)
        ok = (sorted(pre) == sorted(ids) and all(pre[i] == b for i, b in zip(ids, mult))
              and sum(mult) == 2*math.prod(m))
        M = len(ids)
        if not equal:
            Mf = (n+1)*(n+2)**2//4 if n % 2 == 0 else (n+1)*(n*n+4*n+5)//4
            assert ((n+1)*(n+2)**2 % 4 == 0) if n % 2 == 0 else ((n+1)*(n*n+4*n+5) % 4 == 0)
            ok = ok and M == Mf
        part_a.append((equal, n, M, ok))
        assert ok, (equal, n)
ratio_ok = all(F((n+1)*(n+2)**2 if n % 2 == 0 else (n+1)*(n*n+4*n+5), 4) < F(3, 2)*math.comb(n+3, 3)
               for n in range(1, 5001))
out['a_enumeration'] = {'cases': len(part_a), 'all_ok': all(x[3] for x in part_a),
                        'M_aniso_4_8_12_16': [x[2] for x in part_a if not x[0] and x[1] in (4, 8, 12, 16)],
                        'M_equal_4_8_12_16': [x[2] for x in part_a if x[0] and x[1] in (4, 8, 12, 16)],
                        'M_over_N_below_3_2_n1_5000': ratio_ok}

# (b) character-sum Gram: E[prod cos(k_j th_j)] = [m_j|k_j all j]*(1+(-1)^{sum k_j/m_j})/2
def A(k, m):
    if any(kj % mj for kj, mj in zip(k, m)):
        return F(0)
    return F(1) if sum(kj//mj for kj, mj in zip(k, m)) % 2 == 0 else F(0)

def gram_char(n, equal):
    m = orders(n, equal)
    E = exps(n)
    s = [sum(v > 0 for v in a) for a in E]
    bad = 0
    for p, a in enumerate(E):
        for q in range(p, len(E)):
            b = E[q]
            val = F(0)
            for sg in it.product((1, -1), repeat=3):
                val += A(tuple(a[j] + sg[j]*b[j] for j in range(3)), m)
            val /= 8
            # orthonormal entry = 2^{(s_a+s_b)/2} * val ; compare exactly via squares
            if p == q:
                target = 2 if (not equal and a == (n, 0, 0)) else 1
                ok = val * 2**s[p] == target
            else:
                ok = val == 0
            bad += not ok
    return bad

part_b = {}
for equal in (False, True):
    for n in range(1, 17):
        part_b[f"{'equal' if equal else 'aniso'}{n}"] = gram_char(n, equal)
out['b_gram_charsum_mismatches'] = part_b
assert all(v == 0 for v in part_b.values())

# cyclotomic helpers
def cyclo(N):
    x = sympy.symbols('x')
    return [int(c) for c in reversed(sympy.Poly(sympy.cyclotomic_poly(N, x), x).all_coeffs())]

def reduce_poly(c, phi):
    c = [int(v) for v in c]
    d = len(phi)-1
    for k in range(len(c)-1, d-1, -1):
        q = c[k]
        if q:
            for t in range(d+1):
                c[k-d+t] -= q*phi[t]
    return c[:d]

def node_exponents(m):
    P = math.lcm(*m)
    ids, mult = folded_nodes(m)
    e = np.array([[i[j]*(P//m[j]) for j in range(3)] for i in ids], dtype=np.int64)
    return P, e, np.array(mult, dtype=np.int64), ids

SIGNS = np.array(list(it.product((1, -1), repeat=3)), dtype=np.int64)

def pair_ring(a, b, P, e, wint):
    """Integer group-ring vector c with  sum_i wint_i T_a(x_i)T_b(x_i) = c(zeta)/64, zeta=exp(i pi/P)."""
    a = np.array(a); b = np.array(b)
    tot = np.zeros(2*P, dtype=object)
    acc = np.zeros(2*P, dtype=np.int64)
    for s in SIGNS:
        for t in SIGNS:
            k = s*a + t*b
            ex = (e @ k) % (2*P)
            acc += np.bincount(ex, weights=wint.astype(np.float64), minlength=2*P).round().astype(np.int64)
    return acc

def ring_value(acc, P, phi):
    # fold zeta^P = -1, then reduce mod Phi_{2P}
    c = [int(acc[k]) - int(acc[k+P]) for k in range(P)]
    r = reduce_poly(c, phi)
    return r

# (c) exact cyclotomic Gram over actual folded nodes, n<=6 (full matrices)
part_c = {}
for equal in (False, True):
    for n in range(1, 7):
        m = orders(n, equal)
        P, e, mult, ids = node_exponents(m)
        phi = cyclo(2*P)
        E = exps(n); s = [sum(v > 0 for v in a) for a in E]
        den = 64*2*math.prod(m)
        bad = 0
        for p, a in enumerate(E):
            for q in range(p, len(E)):
                r = ring_value(pair_ring(E[p], E[q], P, e, mult), P, phi)
                if any(r[1:]):
                    bad += 1; continue
                val = F(r[0], den)
                if p == q:
                    target = 2 if (not equal and a == (n, 0, 0)) else 1
                    bad += (val*2**s[p] != target)
                else:
                    bad += (val != 0)
        part_c[f"{'equal' if equal else 'aniso'}{n}"] = bad
out['c_gram_cyclotomic_mismatches'] = part_c
assert all(v == 0 for v in part_c.values())

# (d) exact tr(C_W C_W^T) = tr K - 3/4 K_ee (aniso) or tr K (equal), K = V^T W^2 V (orthonormal)
def exact_trace(n, equal):
    m = orders(n, equal)
    P, e, mult, ids = node_exponents(m)
    phi = cyclo(2*P)
    E = exps(n); s = [sum(v > 0 for v in a) for a in E]
    tot = np.zeros(2*P, dtype=np.int64); kee = None
    w2 = mult*mult
    for a, sa in zip(E, s):
        acc = pair_ring(a, a, P, e, w2) * (2**sa)
        tot += acc
        if not equal and a == (n, 0, 0):
            kee = acc.copy()
    den = 64*(2*math.prod(m))**2
    r = ring_value(tot, P, phi); assert not any(r[1:]); trK = F(r[0], den)
    if equal:
        tr = trK
    else:
        r2 = ring_value(kee, P, phi); assert not any(r2[1:]); Kee = F(r2[0], den)
        tr = trK - F(3, 4)*Kee
    M = len(ids); N = math.comb(n+3, 3)
    wmax = F(max(mult), 2*math.prod(m))
    trGinv = F(N) - (F(1, 2) if not equal else F(0))
    bound_mid = wmax*trGinv
    bound_closed = F(4)*trGinv/math.prod(m)
    return tr, M, bound_mid, bound_closed

part_d = {}
for equal in (False, True):
    for n in list(range(1, 9)) + [12, 16]:
        tr, M, b1, b2 = exact_trace(n, equal)
        print(equal, n, float(tr), float(b1), float(b2), flush=True); assert tr <= b1 <= b2
        part_d[f"{'equal' if equal else 'aniso'}{n}"] = {
            'trace': str(tr), 'trace_float': float(tr), 'M': M, 'M_trace': float(M*tr),
            'wmax_bound': float(b1), 'closed_bound': float(b2)}
out['d_exact_traces'] = part_d

# (e) exact OLS: U_T = V_T^T V_T (rational), tr(C0 C0^T) = sum 2^{-s} (U_T^{-1})_aa ; Gauss-Markov identity
def exact_matrix(n, equal, weight):
    m = orders(n, equal)
    P, e, mult, ids = node_exponents(m)
    phi = cyclo(2*P)
    E = exps(n); N = len(E)
    if weight == 'one':
        wint = np.ones(len(ids), dtype=np.int64); den = 64
    else:
        wint = mult; den = 64*2*math.prod(m)
    Mx = [[None]*N for _ in range(N)]
    for p in range(N):
        for q in range(p, N):
            r = ring_value(pair_ring(E[p], E[q], P, e, wint), P, phi)
            assert not any(r[1:])
            Mx[p][q] = Mx[q][p] = F(r[0], den)
    return sympy.Matrix(Mx), E

part_e = {}
for equal in (False, True):
    for n in (1, 2, 3, 4):
        U, E = exact_matrix(n, equal, 'one')        # T-basis V_T^T V_T
        G, _ = exact_matrix(n, equal, 'haar')       # T-basis V_T^T W V_T
        s = [sum(v > 0 for v in a) for a in E]
        D2inv = sympy.diag(*[sympy.Rational(1, 2**k) for k in s])
        Uinv = U.inv()
        trC0 = (D2inv*Uinv).trace()                 # tr((V^T V)^-1) in orthonormal basis
        trCW = sympy.Rational(*F(part_d[f"{'equal' if equal else 'aniso'}{n}"]['trace']).as_integer_ratio())
        # cross term tr(C_W C_0^T) computed with full matrices: C_W C_0^T = D^-1 G_T^-1 G_T U_T^-1 D^-1
        cross = (D2inv*(G.inv()*G*Uinv)).trace()
        frob = trCW - 2*cross + trC0
        part_e[f"{'equal' if equal else 'aniso'}{n}"] = {
            'trace_OLS': str(trC0), 'trace_OLS_float': float(trC0),
            'trace_Haar_float': float(trCW), 'reduction_rel': float(1-trC0/trCW),
            'identity_exact': bool(sympy.simplify(trCW - trC0 - frob) == 0 and frob >= 0)}
        assert part_e[f"{'equal' if equal else 'aniso'}{n}"]['identity_exact']
out['e_exact_OLS'] = part_e

# (f) generic exact rational identities
rng = random.Random(20261108)
gm = 0
for trial in range(30):
    Mr, Nr = rng.randint(3, 7), None
    Nr = rng.randint(1, Mr-1)
    V = sympy.Matrix(Mr, Nr, lambda i, j: sympy.Rational(rng.randint(-5, 5), rng.randint(1, 4)))
    if V.rank() < Nr: continue
    C0 = (V.T*V).inv()*V.T
    Z = sympy.Matrix(Nr, Mr, lambda i, j: sympy.Rational(rng.randint(-3, 3), rng.randint(1, 3)))
    Dm = Z*(sympy.eye(Mr) - V*C0)  # DV=0
    C = C0 + Dm
    assert C*V == sympy.eye(Nr)
    assert C*C.T - C0*C0.T == Dm*Dm.T
    r = [rng.randint(1, 5) for _ in range(Mr)]
    R = sympy.diag(*r); S = sympy.diag(*[sympy.Rational(1, v) for v in r])
    Cs = (V.T*R*V).inv()*V.T*R
    Dg = C - Cs
    assert Cs*V == sympy.eye(Nr) and Dg*V == sympy.zeros(Nr, Nr)
    assert C*S*C.T - Cs*S*Cs.T == Dg*S*Dg.T
    gm += 1
out['f_generic_identities_exact'] = gm

# (g) greedy integer allocation vs exhaustive (own brute force)
def greedy(a, B):
    r = [1]*len(a)
    for _ in range(B-len(a)):
        j = max(range(len(a)), key=lambda t: (F(a[t], r[t]*(r[t]+1)), -t))
        r[j] += 1
    return sum(F(x, y) for x, y in zip(a, r))
def compositions(B, k):
    if k == 1:
        yield (B,); return
    for f in range(1, B-k+2):
        for rest in compositions(B-f, k-1):
            yield (f,)+rest
ga = 0
for trial in range(60):
    k = rng.randint(1, 4); B = rng.randint(k, k+8)
    a = [rng.randint(0, 9) for _ in range(k)]
    best = min(sum(F(x, y) for x, y in zip(a, c)) for c in compositions(B, k))
    assert greedy(a, B) == best
    ga += 1
out['g_allocation_bruteforce_exact'] = ga

json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(json.dumps({k: (v if k != 'd_exact_traces' else {kk: vv['trace_float'] for kk, vv in v.items()}) for k, v in out.items() if k not in ('b_gram_charsum_mismatches','c_gram_cyclotomic_mismatches')}, indent=1)[:4000])
