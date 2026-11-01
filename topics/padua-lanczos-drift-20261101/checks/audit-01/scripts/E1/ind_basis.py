"""Auditor-independent exact basis for E1 (does not import producer code).

Canonical construction: monomial Vandermonde V, exact Gram G=V^T V,
exact LDL^T, monic orthogonal basis B = V L^{-T}, d = diag(D).
Graded order (t,j) -> x^(t-j) y^j, j increasing within degree t.
"""
import sys, time
from flint import fmpq, fmpq_mat

sys.set_int_max_str_digits(0)


def nodes(name):
    if name == "triangle":
        return [(fmpq(i, 12) - 1, fmpq(j, 12) - 1) for i in range(25) for j in range(25) if i + j <= 24]
    if name == "rotated":
        out = []
        for i in range(25):
            for j in range(25):
                x, y = fmpq(i, 12) - 1, fmpq(j, 12) - 1
                out.append(((3 * x - 4 * y) / 5, (4 * x + 3 * y) / 5))
        return out
    raise ValueError(name)


def monomials(n):
    return [(t, j) for t in range(n + 1) for j in range(t + 1)]


def exact_basis(pts, n):
    mons = monomials(n)
    M, N = len(pts), len(mons)
    V = fmpq_mat(M, N, [x ** (t - j) * y ** j for (x, y) in pts for (t, j) in mons])
    G = V.transpose() * V
    g = [[G[r, c] for c in range(N)] for r in range(N)]
    L = [[fmpq(0)] * N for _ in range(N)]
    D = [fmpq(0)] * N
    for j in range(N):
        s = g[j][j]
        Lj = L[j]
        for k in range(j):
            if Lj[k]:
                s -= Lj[k] * Lj[k] * D[k]
        D[j] = s
        assert s > 0, "Gram not positive definite: injectivity fails"
        Lj[j] = fmpq(1)
        for i in range(j + 1, N):
            s = g[i][j]
            Li = L[i]
            for k in range(j):
                if Li[k] and Lj[k]:
                    s -= Li[k] * Lj[k] * D[k]
            Li[j] = s / D[j]
    Lm = fmpq_mat(N, N, [L[r][c] for r in range(N) for c in range(N)])
    Linv = Lm.inv()
    B = V * Linv.transpose()  # M x N, columns monic orthogonal
    return mons, V, B, D


if __name__ == "__main__":
    name, n = sys.argv[1], int(sys.argv[2])
    t0 = time.time()
    pts = nodes(name)
    mons, V, B, D = exact_basis(pts, n)
    print(name, n, len(pts), len(mons), "basis seconds", round(time.time() - t0, 2))
    BtB = B.transpose() * B
    N = len(mons)
    ok = all(BtB[r, c] == (D[r] if r == c else 0) for r in range(N) for c in range(N))
    print("exact orthogonality B^T B = D:", ok, "seconds", round(time.time() - t0, 2))
