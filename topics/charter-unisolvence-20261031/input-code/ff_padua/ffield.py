"""Minimal exact finite-field toolkit (pure Python, no dependencies).

F_p      : Python ints mod p.
F_{p^2}  : pairs (a, b) = a + b*s with s^2 = r, r a fixed quadratic non-residue mod p.
           Elements of F_p are the pairs (a, 0).
Also: Gaussian elimination mod p (rank, det, solve), primitive roots of unity in F_{p^2},
and a mixed-radix FFT over F_{p^2} (works for any length L | p^2-1).
"""
import random

def is_prime(m):
    if m < 2: return False
    if m % 2 == 0: return m == 2
    d = 3
    while d * d <= m:
        if m % d == 0: return False
        d += 2
    return True

def factorize(m):
    f, d = {}, 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1: f[m] = f.get(m, 0) + 1
    return f

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


class Fp2:
    """Arithmetic in F_{p^2} = F_p[s]/(s^2 - r)."""
    def __init__(self, p):
        assert is_prime(p) and p > 2
        self.p = p
        self.r = next(a for a in range(2, p) if legendre(a, p) == -1)
        self._gen = None

    # --- basic ops on pairs ---
    def add(self, x, y): p = self.p; return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)
    def sub(self, x, y): p = self.p; return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)
    def neg(self, x): p = self.p; return ((-x[0]) % p, (-x[1]) % p)
    def mul(self, x, y):
        p = self.p
        return ((x[0] * y[0] + self.r * x[1] * y[1]) % p, (x[0] * y[1] + x[1] * y[0]) % p)
    def smul(self, c, x): p = self.p; return ((c * x[0]) % p, (c * x[1]) % p)
    def norm(self, x): return (x[0] * x[0] - self.r * x[1] * x[1]) % self.p
    def inv(self, x):
        nn = pow(self.norm(x), self.p - 2, self.p)
        return ((x[0] * nn) % self.p, (-x[1] * nn) % self.p)
    def pow(self, x, e):
        res, b = (1, 0), x
        if e < 0: b, e = self.inv(x), -e
        while e:
            if e & 1: res = self.mul(res, b)
            b = self.mul(b, b); e >>= 1
        return res
    def frob(self, x): return (x[0], (-x[1]) % self.p)     # x -> x^p
    def in_base(self, x): return x[1] % self.p == 0

    def generator(self):
        """A generator of the cyclic group F_{p^2}^*."""
        if self._gen is None:
            Q = self.p * self.p - 1
            primes = list(factorize(Q))
            rng = random.Random(12345)
            while True:
                g = (rng.randrange(self.p), rng.randrange(1, self.p))
                if all(self.pow(g, Q // l) != (1, 0) for l in primes):
                    self._gen = g; break
        return self._gen

    def root_of_unity(self, N):
        """Primitive N-th root of unity in F_{p^2} (requires N | p^2 - 1)."""
        Q = self.p * self.p - 1
        if Q % N: raise ValueError(f"no primitive {N}-th root of unity in F_{self.p}^2")
        z = self.pow(self.generator(), Q // N)
        assert all(self.pow(z, N // l) != (1, 0) for l in factorize(N)) and self.pow(z, N) == (1, 0)
        return z


# ---------------- linear algebra mod p ----------------
def rank_mod_p(M, p):
    A = [[v % p for v in row] for row in M]
    nr, nc = len(A), len(A[0]) if A else 0
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if A[i][c]), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        iv = pow(A[r][c], p - 2, p)
        A[r] = [(v * iv) % p for v in A[r]]
        for i in range(nr):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[r])]
        r += 1
        if r == nr: break
    return r

def det_mod_p(M, p):
    A = [[v % p for v in row] for row in M]; n = len(A); d = 1
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i][c]), None)
        if piv is None: return 0
        if piv != c: A[c], A[piv] = A[piv], A[c]; d = -d
        d = (d * A[c][c]) % p
        iv = pow(A[c][c], p - 2, p)
        for i in range(c + 1, n):
            if A[i][c]:
                f = (A[i][c] * iv) % p
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[c])]
    return d % p

def matmul_mod(A, B, p):
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) % p for col in Bt] for row in A]

def transpose(A): return [list(r) for r in zip(*A)]


# ---------------- FFT over F_{p^2} ----------------
def _fft_rec(F, a, pw, stride, L0):
    """DFT of a (length L) w.r.t. root w = pw[stride], where pw[e] = w0^e, w0 of order L0, L*stride = L0."""
    L = len(a)
    if L == 1: return list(a)
    r = min(factorize(L))
    if r == L:                              # prime length: naive O(L^2)
        out = []
        for k in range(L):
            s = (0, 0)
            for j in range(L):
                s = F.add(s, F.mul(a[j], pw[(stride * j * k) % L0]))
            out.append(s)
        return out
    m = L // r
    subs = [_fft_rec(F, a[i::r], pw, stride * r, L0) for i in range(r)]
    out = [None] * L
    for k in range(m):
        tw = [F.mul(subs[i][k], pw[(stride * i * k) % L0]) for i in range(r)]
        for s in range(r):
            acc = (0, 0)
            for i in range(r):          # w^{m*s*i}
                acc = F.add(acc, F.mul(tw[i], pw[(stride * m * s * i) % L0]))
            out[k + s * m] = acc
    return out

def power_table(F, w, L):
    pw = [(1, 0)] * L
    for e in range(1, L): pw[e] = F.mul(pw[e - 1], w)
    return pw

def fft(F, a, w, pw=None):
    """Mixed-radix Cooley-Tukey DFT y_k = sum_j a_j w^{jk}, w a primitive len(a)-th root.
    Cost O(L * sum of prime factors of L) field operations (O(L log L) for smooth L)."""
    L = len(a)
    if pw is None: pw = power_table(F, w, L)
    return _fft_rec(F, a, pw, 1, L)

def dft_naive(F, a, w):
    L = len(a); pw = power_table(F, w, L)
    return [ _sum(F, [F.mul(a[j], pw[(j * k) % L]) for j in range(L)]) for k in range(L)]

def _sum(F, xs):
    s = (0, 0)
    for x in xs: s = F.add(s, x)
    return s
