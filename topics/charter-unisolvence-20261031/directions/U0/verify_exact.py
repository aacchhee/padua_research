"""Developer cross-check independent of supplied modules, fixed U0 finite scope.

Prime code nodes come directly from characters; monomial generator matrices use
last-nonzero projective normalization, unlike the source's first-nonzero scheme.
Also checks q=3,9 in a separately implemented F_81 for the character formula,
cardinality, rank and Dickson determinant. All arithmetic is exact. No RNG.
This is not an independent-agent audit or a computer-assisted proof claim.
"""
import json
import numpy as np

EXPECTED = {7: (7, 4), 11: (17, 13), 13: (23, 18), 17: (39, 33)}


def character_nodes(q):
    def chi(v):
        v %= q
        return 0 if v == 0 else (1 if pow(v, (q - 1) // 2, q) == 1 else -1)
    xs = [x for x in range(q) if chi(x*x - 1) != -1]
    ys = [y for y in range(q) if chi(y*y - 1) != 1]
    def eps(x):
        return chi(-1) if x == q - 1 else chi(2*(x + 1))
    def delta(y):
        return -chi(-1) if y == q - 1 else chi(2*(y + 1))
    return [(x, y) for x in xs for y in ys if eps(x) == delta(y)]


def distance(q, degree):
    points = character_nodes(q)
    basis = [(a, d-a) for d in range(degree+1) for a in range(d, -1, -1)]
    generator = np.array([[pow(x, a, q)*pow(y, b, q) % q for x, y in points]
                          for a, b in basis], dtype=np.int64)
    best, witness, checked = len(points)+1, None, 0
    for last in range(len(basis)):
        for start in range(0, q**last, 20000):
            numbers = np.arange(start, min(start+20000, q**last), dtype=np.int64)
            messages = np.zeros((len(numbers), len(basis)), dtype=np.int64)
            messages[:, last] = 1
            for position in range(last):
                messages[:, position] = numbers % q
                numbers //= q
            words = (messages @ generator) % q
            weights = np.count_nonzero(words, axis=1)
            index = int(np.argmin(weights))
            if int(weights[index]) < best:
                best = int(weights[index]); witness = messages[index].tolist()
            checked += len(messages)
    assert checked == (q**len(basis)-1)//(q-1)
    assert best == EXPECTED[q][degree-1]
    return {"q": q, "degree": degree, "N": len(points), "K": len(basis),
            "distance": best, "projective_messages": checked,
            "monomial_basis": basis, "minimum_witness": witness}


class F81:
    """F_3[t]/(t^4+t+2); integers encode four base-3 coefficients.

    The modulus has no roots in F3 and no factor among its three monic
    irreducible quadratics (t²+1,t²+t+2,t²+2t+2), hence is irreducible.
    """
    @staticmethod
    def digits(x):
        return [(x//3**i) % 3 for i in range(4)]

    def add(self, x, y):
        return sum(((a+b) % 3)*3**i for i, (a, b) in enumerate(zip(self.digits(x), self.digits(y))))

    def neg(self, x):
        return sum((-a % 3)*3**i for i, a in enumerate(self.digits(x)))

    def mul(self, x, y):
        a, b = self.digits(x), self.digits(y)
        c = [sum(a[i]*b[k-i] for i in range(4) if 0 <= k-i < 4) % 3 for k in range(7)]
        for k in range(6, 3, -1):
            c[k-4] = (c[k-4]-2*c[k]) % 3
            c[k-3] = (c[k-3]-c[k]) % 3
        return sum(c[i]*3**i for i in range(4))

    def power(self, x, e):
        if e < 0:
            x, e = self.power(x, 79), -e
        value = 1
        while e:
            if e % 2:
                value = self.mul(value, x)
            x = self.mul(x, x); e //= 2
        return value

    def determinant(self, matrix):
        a = [row[:] for row in matrix]; value = 1
        for col in range(len(a)):
            pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
            if pivot is None:
                return 0
            if pivot != col:
                a[col], a[pivot] = a[pivot], a[col]; value = self.neg(value)
            value = self.mul(value, a[col][col])
            inverse = self.power(a[col][col], -1)
            for row in range(col+1, len(a)):
                factor = self.mul(a[row][col], inverse)
                a[row] = [self.add(v, self.neg(self.mul(factor, w))) for v, w in zip(a[row], a[col])]
        return value


def extension_check(q):
    field = F81()
    assert all(field.power(x, 80) == 1 for x in range(1, 81))
    gen = next(x for x in range(1, 81) if field.power(x, 40) != 1 and field.power(x, 16) != 1)
    n = (q-1)//2
    z, e = field.power(gen, 80//(q-1)), field.power(gen, 80//(q+1))
    def trace_half(root, j):
        return field.mul(2, field.add(field.power(root, j), field.power(root, -j)))
    xs = [trace_half(z, j) for j in range(n+1)]
    ys = [trace_half(e, j) for j in range(n+2)]
    canonical = {(x, y) for j, x in enumerate(xs) for k, y in enumerate(ys) if (j+k) % 2 == 0}
    base = [x for x in range(81) if field.power(x, q) == x]
    assert len(base) == q and all(x in base for x in xs+ys)
    def chi(x):
        value = field.power(x, (q-1)//2) if x else 0
        assert value in (0, 1, 2)
        return -1 if value == 2 else value
    cx = [x for x in base if chi(field.add(field.mul(x, x), 2)) != -1]
    cy = [y for y in base if chi(field.add(field.mul(y, y), 2)) != 1]
    eps = lambda x: chi(2) if x == 2 else chi(field.mul(2, field.add(x, 1)))
    delta = lambda y: -chi(2) if y == 2 else chi(field.mul(2, field.add(y, 1)))
    described = {(x, y) for x in cx for y in cy if eps(x) == delta(y)}
    assert described == canonical and len(canonical) == (n+1)*(n+2)//2
    basis = [(a, d-a) for d in range(n+1) for a in range(d, -1, -1)]
    matrix = [[field.mul(field.power(field.mul(2, x), a), field.power(field.mul(2, y), b))
               for a, b in basis] for x, y in sorted(canonical)]
    det = field.determinant(matrix)
    predicted = (pow(2, (n*n+3*n+6)//2, 3)*pow(n*(n+1), len(canonical), 3)) % 3
    assert det != 0 and field.mul(det, det) == predicted
    return {"q": q, "characteristic": 3, "n": n, "N": len(canonical),
            "field_modulus": [2, 1, 0, 0, 1], "generator": gen,
            "character_description": True, "determinant_nonzero": True,
            "determinant_squared": field.mul(det, det), "predicted": predicted}


if __name__ == "__main__":
    for q in (3, 9):
        print(json.dumps(extension_check(q)), flush=True)
    for q in EXPECTED:
        for degree in (1, 2):
            print(json.dumps(distance(q, degree)), flush=True)
