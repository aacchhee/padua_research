"""Auditor-independent exact check (Claude audit, not developer code).

Builds type-II multiple orthogonal polynomials directly from the moment
linear systems over Fractions with first-order dual numbers, extracts NN
coefficients by polynomial matching, and checks:
  (5)  closed-form multiple-Krawtchouk A/B coefficients for all |nu|<=M;
  (4)  terminal dot b2 formula for the parity second-weight direction;
  (13) summed bound consequence (max over terminal pairs vs S_{M-1}/M);
  proximity: dot c = q^M/delta^(M-1) at terminal (M-1,1) and the kappa
       lower bounds of conditioning-lower-proximity.md.
Integer node variable k=0..M; z-scaling a->4a/M^2, b->2b/M-1.
"""
from fractions import Fraction as Fr
from math import comb
import sys


class D:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(s, o):
        o = o if isinstance(o, D) else D(o)
        return D(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, D) else D(o)
        return D(s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return D(o) - s

    def __neg__(s):
        return D(-s.a, -s.b)

    def __mul__(s, o):
        o = o if isinstance(o, D) else D(o)
        return D(s.a * o.a, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = o if isinstance(o, D) else D(o)
        if o.a == 0:
            raise ZeroDivisionError
        return D(s.a / o.a, (s.b * o.a - s.a * o.b) / (o.a * o.a))

    def iszero(s):
        return s.a == 0


def solve(A, rhs):
    n = len(A)
    A = [row[:] + [r] for row, r in zip(A, rhs)]
    for c in range(n):
        p = next(r for r in range(c, n) if not A[r][c].iszero())
        A[c], A[p] = A[p], A[c]
        for r in range(n):
            if r != c and (A[r][c].a != 0 or A[r][c].b != 0):
                f = A[r][c] / A[c][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[r][n] / A[r][r] for r in range(n)]


def mop(nodes, w1, w2, n, m):
    """monic type II P_{n,m}: list of coefficients low->high (length t+1)."""
    t = n + m
    if t == 0:
        return [D(1)]
    rows, rhs = [], []
    for ws, cnt in ((w1, n), (w2, m)):
        for i in range(cnt):
            mom = [sum((ws[l] * nodes[l] ** (i + j) for l in range(len(nodes))), D(0)) for j in range(t + 1)]
            rows.append(mom[:t])
            rhs.append(-mom[t])
    c = solve(rows, rhs)
    return c + [D(1)]


def nn_coeffs(nodes, w1, w2, M):
    P = {}
    for t in range(M + 2):
        for n in range(t + 1):
            P[(n, t - n)] = mop(nodes, w1, w2, n, t - n)
    out = {}
    for t in range(M + 1):
        for n in range(t + 1):
            m = t - n
            nu = (n, m)
            xP = [D(0)] + P[nu]
            res = {}
            for j, e in ((1, (1, 0)), (2, (0, 1))):
                S = P[(n + e[0], m + e[1])]
                R = [x - y for x, y in zip(xP, S)]
                b = R[t]
                R = [r - b * p for r, p in zip(R[:t], P[nu][:t])]  # degree <= t-1
                res[("b", j)] = b
                preds = []
                if n > 0:
                    preds.append((1, P[(n - 1, m)]))
                if m > 0:
                    preds.append((2, P[(n, m - 1)]))
                if len(preds) == 1:
                    s, Q = preds[0]
                    a = R[t - 1]
                    res[("a", s, j)] = a
                    res[("a", 3 - s, j)] = D(0)
                elif len(preds) == 2:
                    Q1, Q2 = preds[0][1], preds[1][1]
                    # a1+a2 = R[t-1]; a1*Q1[t-2]+a2*Q2[t-2] = R[t-2]
                    s1 = R[t - 1]
                    det = Q2[t - 2] - Q1[t - 2]
                    a1 = (s1 * Q2[t - 2] - R[t - 2]) / det
                    a2 = s1 - a1
                    res[("a", 1, j)] = a1
                    res[("a", 2, j)] = a2
                else:
                    res[("a", 1, j)] = D(0)
                    res[("a", 2, j)] = D(0)
                # residual check: R - a1 Q1 - a2 Q2 == 0
                chk = R[:]
                for s, Q in preds:
                    a = res[("a", s, j)]
                    chk = [x - a * y for x, y in zip(chk, Q[:t] + [D(0)] * (t - len(Q)))]
                assert all(x.a == 0 and x.b == 0 for x in chk), ("NN residual", nu, j)
            # a's must not depend on j (recurrence uniqueness)
            for s in (1, 2):
                assert res[("a", s, 1)].a == res[("a", s, 2)].a
            out[nu] = res
    return out


def binw(M, p, eps_dir=None):
    w = []
    for k in range(M + 1):
        base = Fr(comb(M, k)) * p ** k * (1 - p) ** (M - k)
        der = base * eps_dir[k] if eps_dir else Fr(0)
        w.append(D(base, der))
    return w


def check_closed_form(M, p1, p2):
    nodes = [Fr(k) for k in range(M + 1)]
    co = nn_coeffs(nodes, binw(M, p1), binw(M, p2), M)
    q1, q2 = p1 * (1 - p1), p2 * (1 - p2)
    for (n, m), r in co.items():
        t = n + m
        A1 = n * q1 * (M - t + 1)
        A2 = m * q2 * (M - t + 1)
        for j, pj in ((1, p1), (2, p2)):
            B = pj * (M - t) + (1 - p1) * n + (1 - p2) * m
            assert r[("b", j)].a == B, ((n, m), j, r[("b", j)].a, B)
            assert r[("a", 1, j)].a == A1, ((n, m), "a1")
            assert r[("a", 2, j)].a == A2, ((n, m), "a2")
    return len(co)


def Qcoef(n, r):
    # [v^r] ((1-v/25)/(1-v))^n = [v^r] (1 + c v/(1-v))^n, c=24/25
    if r == 0:
        return Fr(1)
    c = Fr(24, 25)
    return sum(comb(n, j) * c ** j * comb(r - 1, j - 1) for j in range(1, min(n, r) + 1))


def check_terminal_derivative(M):
    p1, p2 = Fr(2, 5), Fr(1, 2)
    nodes = [Fr(k) for k in range(M + 1)]
    par = [(-1) ** k for k in range(M + 1)]
    co = nn_coeffs(nodes, binw(M, p1), binw(M, p2, par), M)
    # field scale of b2 in z: max |2B/M-1|
    b2z = [abs(2 * r[("b", 2)].a / M - 1) for r in co.values()]
    assert max(b2z) == Fr(1, 5)
    best = Fr(0)
    for n in range(M):
        m = M - n
        dB = co[(n, m)][("b", 2)].b
        db1 = co[(n, m)][("b", 1)].b
        assert dB == db1  # terminal equality differentiated
        ratio = abs(2 * dB / M) / Fr(1, 5)
        pred = Fr(5) ** M / M * Qcoef(n, m - 1)
        assert ratio == pred, (M, n, m, ratio, pred)
        # sign claim (11): dot B = (-1)^n 5^n R/2, R = 5^(m-1) Q >= 0
        assert dB == (-1) ** n * Fr(5) ** n * Fr(5) ** (m - 1) * Qcoef(n, m - 1) / 2
        best = max(best, ratio)
    # mass preserved
    S = sum(binw(M, p2, par)[k].b for k in range(M + 1))
    assert S == 0
    return best


def check_proximity(M, delta):
    p1 = Fr(2, 5)
    q = p1 + delta
    r = (1 - q) / q
    zeta = [(-r) ** k / r ** M for k in range(M + 1)]
    assert max(abs(z) for z in zeta) == 1
    nodes = [Fr(k) for k in range(M + 1)]
    co = nn_coeffs(nodes, binw(M, p1), binw(M, q, zeta), M)
    dB = co[(M - 1, 1)][("b", 2)].b
    assert abs(dB) == q ** M / delta ** (M - 1), (M, delta)
    b2z = max(abs(2 * rr[("b", 2)].a / M - 1) for rr in co.values())
    assert b2z == Fr(1, 5)
    dmin = min(abs(2 * (rr[("b", 2)].a - rr[("b", 1)].a) / M) for nu, rr in co.items() if sum(nu) <= M - 1)
    assert dmin == 2 * delta / M
    lb = abs(2 * dB / M) / Fr(1, 5)
    assert lb == 10 * q ** M / (M * delta ** (M - 1))
    return lb, lb * dmin


if __name__ == "__main__":
    Mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    for M in range(1, Mmax + 1):
        for p1, p2 in ((Fr(2, 5), Fr(1, 2)), (Fr(1, 3), Fr(3, 4)), (Fr(2, 5), Fr(9, 20)), (Fr(7, 10), Fr(1, 5))):
            cnt = check_closed_form(M, p1, p2)
        best = check_terminal_derivative(M)
        S = [Fr(1), Fr(1)]
        for L in range(2, M + 1):
            S.append(2 * S[-1] - S[-2] / 25)
        bound13 = Fr(5) ** M / M * S[M - 1] / M
        assert best >= bound13
        assert best >= Fr(5) ** M / M
        line = f"M={M} N={M+1}: closed form (5) OK on {cnt} sites x4 param pairs; terminal (4) OK; max ratio={float(best):.6e} >= (13) {float(bound13):.6e}"
        if M >= 3:
            for delta in (Fr(1, 10), Fr(1, 37), Fr(1, 1000)):
                lb, lbd = check_proximity(M, delta)
            line += f"; proximity OK (delta=1/1000: kappa*dmin >= {float(lbd):.3e})"
        print(line, flush=True)
    print("ALL PASS")
