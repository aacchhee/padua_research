#!/usr/bin/env python3
"""Independent Bernstein positive-interpolation check of the Padua argmax
at a fixed degree n (audit G-assembly, Claude Opus 5.5).

Written from the theory statements only (PD-T101 cardinal formula,
PD-T210 certificate implication); it imports no repository code.

Arithmetic: python-flint (Arb ball arithmetic, FLINT/GMP) for every
quantity that depends on cos(rational*pi); exact fmpq for all
polynomial/basis data.  Strict tests use Arb's certain-only `<`.

Cardinals (PD-T101):
  L_jk(x,y) = w_jk * sum_{p+q<=n} h_pq T_p(cos(j pi/n)) T_q(cos(k pi/(n+1))) T_p(x) T_q(y)
  h_pq = nu_p nu_q (nu_0=1, nu_r=2) except h_{n0} = 1;  w_jk = 2 e_j f_k /(n(n+1)).

Mode A (own search): recursive closed midpoint subdivision of [-1,1]^2,
alternating x then y, each leaf must satisfy the bound or corner
predicate.  Mode B (--cert FILE): replay the leaf paths of a repository
certificate (data only) with this arithmetic, and check that the paths
form a complete prefix partition.
"""
import sys, json, gzip, time, argparse
from fractions import Fraction as Fr
from flint import arb, arb_mat, fmpq, fmpq_poly, fmpz_poly, ctx

def toarb(v):
    if isinstance(v, Fr): return arb(fmpq(v.numerator, v.denominator))
    if isinstance(v, int): return arb(v)
    return v

def binom(a, b):
    from math import comb
    return comb(a, b)

class Padua:
    def __init__(self, n, prec=256):
        ctx.prec = prec
        self.n = n; m = n + 1; self.m = m
        self.nodes = [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]
        assert len(self.nodes) == (n + 1) * (n + 2) // 2
        nu = [1] + [2] * n
        self.nu = nu
        # X[p][j] = cos(p j pi / n), Y[q][k] = cos(q k pi / m), as Arb balls
        def cospi(num, den):
            r = Fr(num, den) % 2
            if r == 0: return arb(1)
            if r == 1: return arb(-1)
            if r == Fr(1, 2) or r == Fr(3, 2): return arb(0)
            return arb(fmpq(r.numerator, r.denominator)).cos_pi()
        self.X = [[cospi(p * j, n) for j in range(n + 1)] for p in range(n + 1)]
        self.Y = [[cospi(q * k, m) for k in range(m + 1)] for q in range(n + 1)]
        e = lambda j, top: Fr(1, 2) if j in (0, top) else Fr(1)
        self.w = {(j, k): arb(fmpq(*(lambda f: (f.numerator, f.denominator))(2 * e(j, n) * e(k, m) / (n * m))))
                  for (j, k) in self.nodes}
        self.cheb = [fmpq_poly(fmpz_poly.chebyshev_t(p)) for p in range(n + 1)]
        # Bernstein conversion matrix: power coeff r -> Bernstein index i: C(i,r)/C(n,r)
        self.P2B = [[fmpq(binom(i, r), binom(n, r)) if i >= r else fmpq(0) for i in range(n + 1)] for r in range(n + 1)]

    def coef(self, p, q):
        if p == self.n and q == 0: return 1
        return self.nu[p] * self.nu[q]

    def cardinal_value(self, B, x, y):
        """Arb value of L_B at (x,y) given Arb/rational x,y (direct)."""
        n = self.n; j, k = B
        x = toarb(x); y = toarb(y)
        Tx = [arb(1), x]; Ty = [arb(1), y]
        for r in range(2, n + 1):
            Tx.append(2 * x * Tx[-1] - Tx[-2]); Ty.append(2 * y * Ty[-1] - Ty[-2])
        s = arb(0)
        for p in range(n + 1):
            for q in range(n + 1 - p):
                s += self.coef(p, q) * self.X[p][j] * self.Y[q][k] * Tx[p] * Ty[q]
        return self.w[B] * s

    def lam(self, x, y):
        return sum((abs(self.cardinal_value(B, x, y)) for B in self.nodes), arb(0))

    def bern_1d(self, lo, hi):
        """beta[p][i]: exact Bernstein coefficients (degree n) of T_p on [lo,hi]."""
        n = self.n
        lin = fmpq_poly([fmpq(lo.numerator, lo.denominator), fmpq((hi - lo).numerator, (hi - lo).denominator)])
        out = []
        for p in range(n + 1):
            c = self.cheb[p](lin).coeffs()
            c = list(c) + [fmpq(0)] * (n + 1 - len(c))
            out.append([sum((c[r] * self.P2B[r][i] for r in range(i + 1)), fmpq(0)) for i in range(n + 1)])
        return out

    def leaf_sums(self, box):
        """U[i][l] = Arb ball containing sum_B |c_{B,il}| on box."""
        n, m = self.n, self.m
        (x0, x1), (y0, y1) = box
        bx = self.bern_1d(x0, x1); by = self.bern_1d(y0, y1)
        # A_q[i][j] = sum_{p<=n-q} bx[p][i] nu_p X[p][j]  (cumulative over p)
        # rows (i,j), cols q
        rows = (n + 1) * (n + 1)
        cum = [[arb(0)] * (n + 1) for _ in range(n + 1)]  # cum[i][j] running over p
        Acols = {}  # q -> list over (i,j) of A_q
        partial = []  # partial[p] = matrix after including p
        for p in range(n + 1):
            for i in range(n + 1):
                bpi = arb(bx[p][i]) * self.nu[p]
                for j in range(n + 1):
                    cum[i][j] = cum[i][j] + bpi * self.X[p][j]
            partial.append([row[:] for row in cum])
        Amat = arb_mat(rows, n + 1)
        for q in range(n + 1):
            P = partial[n - q]
            for i in range(n + 1):
                for j in range(n + 1):
                    Amat[i * (n + 1) + j, q] = P[i][j]
        cols = (n + 1) * (m + 1)
        Bmat = arb_mat(n + 1, cols)
        for q in range(n + 1):
            for l in range(n + 1):
                bql = arb(by[q][l]) * self.nu[q]
                for k in range(m + 1):
                    Bmat[q, l * (m + 1) + k] = bql * self.Y[q][k]
        F = Amat * Bmat
        # correction for the exceptional (n,0) mode: kernel coefficient nu_n nu_0 = 2 -> 1
        # subtract 1 * bx[n][i] X[n][j] * by[0][l] Y[0][k]  (Y[0][k] = 1)
        U = [[arb(0)] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            bni = arb(bx[n][i])
            for l in range(n + 1):
                b0l = arb(by[0][l])
                corr_base = bni * b0l
                s = arb(0)
                for (j, k) in self.nodes:
                    v = F[i * (n + 1) + j, l * (m + 1) + k] - corr_base * self.X[n][j]
                    s += self.w[(j, k)] * abs(v)
                U[i][l] = s
        return U

WRONG_PARITY = False
def corners_for(n):
    even = (n % 2 == 0) != WRONG_PARITY
    return [(-1, -1), (1, -1)] if even else [(-1, -1), (-1, 1)]

def vertex_index(box, c, n):
    (x0, x1), (y0, y1) = box
    i = 0 if c[0] == x0 else (n if c[0] == x1 else None)
    l = 0 if c[1] == y0 else (n if c[1] == y1 else None)
    if i is None or l is None: return None
    return (i, l)

def test_leaf(P, box, C):
    """Return ('bound'|'corner'|None, margin_info)."""
    U = P.leaf_sums(box); n = P.n
    cs = [c for c in corners_for(n) if vertex_index(box, c, n) is not None]
    if not cs:
        ok = all(U[i][l] < C for i in range(n + 1) for l in range(n + 1))
        return ('bound' if ok else None), U
    if len(cs) > 1: return None, U
    vi = vertex_index(box, cs[0], n)
    ok = all(U[i][l] < C for i in range(n + 1) for l in range(n + 1) if (i, l) != vi)
    return ('corner' if ok else None), U

def split(box, axis):
    (x0, x1), (y0, y1) = box
    if axis == 0:
        xm = (x0 + x1) / 2; return ((x0, xm), (y0, y1)), ((xm, x1), (y0, y1))
    ym = (y0 + y1) / 2; return ((x0, x1), (y0, ym)), ((x0, x1), (ym, y1))

def maxupper(U, skip=None):
    best = None
    for i in range(len(U)):
        for l in range(len(U)):
            if (i, l) == skip: continue
            u = U[i][l].upper()
            if best is None or u > best: best = u
    return best

def run(n, cert=None, maxdepth=14, prec=256):
    t0 = time.process_time()
    P = Padua(n, prec)
    root = ((Fr(-1), Fr(1)), (Fr(-1), Fr(1)))
    # corner values: both designated corners; independent direct evaluation
    cv = [P.lam(Fr(c[0]), Fr(c[1])) for c in corners_for(n)]
    if not WRONG_PARITY: assert cv[0].overlaps(cv[1])
    C = cv[0]
    # sanity: cardinal property at a few node pairs (ball containment only)
    sanity = []
    for B in P.nodes[:3]:
        for A in P.nodes[:3]:
            xa = P.X[1][A[0]]; ya = P.Y[1][A[1]]
            v = P.cardinal_value(B, xa, ya)
            sanity.append(bool(v.contains(1 if A == B else 0)))
    leaves = []; area = Fr(0); failures = []
    if cert is None:
        stack = [(root, '', 0)]
        while stack:
            box, path, d = stack.pop()
            kind, U = test_leaf(P, box, C)
            if kind:
                leaves.append((path, kind)); w = (box[0][1] - box[0][0]) * (box[1][1] - box[1][0]); area += w
            elif d >= maxdepth:
                failures.append(path); area += 0
            else:
                a, b = split(box, d % 2)
                stack.append((b, path + '1', d + 1)); stack.append((a, path + '0', d + 1))
    else:
        d = json.load(gzip.open(cert)) if cert.endswith('.gz') else json.load(open(cert))
        assert d['n'] == n and d['complete'] and not d['pending']
        paths = [(lf['path'], lf['kind']) for lf in d['leaves']]
        # prefix-partition completeness: build tree
        ps = set(p for p, _ in paths)
        assert len(ps) == len(paths), 'duplicate leaf'
        for p in ps:
            for t in range(len(p)):
                assert p[:t] not in ps, 'ancestor overlap'
        def complete(prefix):
            if prefix in ps: return True
            if len(prefix) > 60: return False
            return complete(prefix + '0') and complete(prefix + '1')
        assert complete(''), 'incomplete partition'
        for p, kind_claimed in paths:
            box = root
            for t, ch in enumerate(p):
                a, b = split(box, t % 2); box = a if ch == '0' else b
            kind, U = test_leaf(P, box, C)
            if kind != kind_claimed: failures.append((p, kind_claimed, kind))
            else:
                leaves.append((p, kind)); area += (box[0][1] - box[0][0]) * (box[1][1] - box[1][0])
    cpu = time.process_time() - t0
    res = {
        'n': n, 'mode': 'own-search' if cert is None else 'replay:' + cert.split('/')[-1],
        'prec_bits': prec, 'corner_value_ball': str(C), 'corner_value_lower': str(C.lower()),
        'leaves': len(leaves), 'bound_leaves': sum(1 for _, k in leaves if k == 'bound'),
        'corner_leaves': sum(1 for _, k in leaves if k == 'corner'),
        'max_depth': max(len(p) for p, _ in leaves) if leaves else None,
        'covered_area': str(area), 'complete': (area == 4 and not failures),
        'failures': failures[:10], 'cardinal_sanity_ball_containment': all(sanity),
        'cpu_seconds': round(cpu, 3),
    }
    return res

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('n', type=int); ap.add_argument('--cert'); ap.add_argument('--maxdepth', type=int, default=14)
    ap.add_argument('--prec', type=int, default=256)
    ap.add_argument('--wrong-parity', action='store_true')
    a = ap.parse_args()
    if a.wrong_parity: WRONG_PARITY = True
    r = run(a.n, a.cert, a.maxdepth, a.prec)
    print(json.dumps(r, indent=1))
    sys.exit(0 if r['complete'] else 1)
