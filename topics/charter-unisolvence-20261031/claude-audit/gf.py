"""Minimal exact GF(p^k) arithmetic for the Claude audit checker.

Written independently for audit-01; imports no developer or source module.
Elements are integers 0..q-1 (base-p digit vectors of polynomial coefficients
modulo a primitive polynomial). Multiplication uses exp/log tables.
"""
from itertools import product


def _polymulmod(a, b, mod, p):
    # a, b, mod: coefficient lists, low degree first; mod monic of degree k
    k = len(mod) - 1
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                res[i + j] = (res[i + j] + ai * bj) % p
    for d in range(len(res) - 1, k - 1, -1):
        c = res[d]
        if c:
            for t in range(k + 1):
                res[d - k + t] = (res[d - k + t] - c * mod[t]) % p
    return (res + [0] * k)[:k]


class GF:
    def __init__(self, p, k=1):
        self.p, self.k, self.q = p, k, p ** k
        q = self.q
        self.mod = None
        if k == 1:
            # find primitive root
            for g in range(1, p):
                x, seen = 1, set()
                for _ in range(p - 1):
                    seen.add(x)
                    x = x * g % p
                if len(seen) == p - 1:
                    break
            exp = [1]
            for _ in range(q - 2):
                exp.append(exp[-1] * g % p)
        else:
            exp = None
            for tail in product(range(p), repeat=k):
                mod = list(tail) + [1]
                if mod[0] == 0:
                    continue
                cur = [1] + [0] * (k - 1)
                xs = [0, 1] + [0] * (k - 2) if k > 1 else [0]
                vals = []
                seen = set()
                ok = True
                for _ in range(q - 1):
                    v = sum(c * p ** i for i, c in enumerate(cur))
                    if v in seen:
                        ok = False
                        break
                    seen.add(v)
                    vals.append(v)
                    cur = _polymulmod(cur, xs, mod, p)
                if ok and len(seen) == q - 1:
                    exp = vals
                    self.mod = mod
                    break
            assert exp is not None
        self.exp = exp + exp  # doubled for index convenience
        self.log = [None] * q
        for i, v in enumerate(exp):
            self.log[v] = i
        # addition via digit vectors
        self.digits = [[(v // p ** i) % p for i in range(k)] for v in range(q)]
        self.addt = None
        if q <= 400:
            self.addt = [[self._add_digits(a, b) for b in range(q)] for a in range(q)]
        self.negt = [sum(((-d) % p) * p ** i for i, d in enumerate(self.digits[a])) for a in range(q)]
        self.one = 1
        self.zero = 0

    def _add_digits(self, a, b):
        p = self.p
        return sum(((da + db) % p) * p ** i for i, (da, db) in enumerate(zip(self.digits[a], self.digits[b])))

    def add(self, a, b):
        if self.addt is None:
            return self._add_digits(a, b)
        return self.addt[a][b]

    def neg(self, a):
        return self.negt[a]

    def sub(self, a, b):
        return self.add(a, self.negt[b])

    def mul(self, a, b):
        if a == 0 or b == 0:
            return 0
        return self.exp[self.log[a] + self.log[b]]

    def inv(self, a):
        assert a != 0
        return self.exp[(self.q - 1 - self.log[a]) % (self.q - 1)]

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def pow(self, a, e):
        if e == 0:
            return 1
        if a == 0:
            return 0
        return self.exp[(self.log[a] * e) % (self.q - 1)]

    def from_int(self, n):
        # image of integer n
        r = n % self.p
        return r  # prime-field element encoded as constant digit

    def prod(self, xs):
        r = 1
        for x in xs:
            r = self.mul(r, x)
        return r

    def det(self, M):
        M = [row[:] for row in M]
        n = len(M)
        d = 1
        for c in range(n):
            piv = next((r for r in range(c, n) if M[r][c] != 0), None)
            if piv is None:
                return 0
            if piv != c:
                M[c], M[piv] = M[piv], M[c]
                d = self.neg(d)
            d = self.mul(d, M[c][c])
            ic = self.inv(M[c][c])
            for r in range(c + 1, n):
                if M[r][c]:
                    f = self.mul(M[r][c], ic)
                    Mr, Mc = M[r], M[c]
                    for j in range(c, n):
                        if Mc[j]:
                            Mr[j] = self.sub(Mr[j], self.mul(f, Mc[j]))
        return d

    def rank(self, M):
        M = [row[:] for row in M]
        rows, cols = len(M), len(M[0]) if M else 0
        r = 0
        for c in range(cols):
            piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
            if piv is None:
                continue
            M[r], M[piv] = M[piv], M[r]
            ic = self.inv(M[r][c])
            for i in range(rows):
                if i != r and M[i][c]:
                    f = self.mul(M[i][c], ic)
                    for j in range(c, cols):
                        M[i][j] = self.sub(M[i][j], self.mul(f, M[r][j]))
            r += 1
        return r

    def __repr__(self):
        return f"GF({self.p}^{self.k})"
