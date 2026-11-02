"""Independent exact (algebraic-number-field) check of gated-codex-13 parts 1-3.

Auditor: Claude Opus 5.5 (independent of developer code).  Cardinal polynomials
are obtained by solving the Padua interpolation (Vandermonde) system in the
Chebyshev tensor basis T_p(x)T_q(y), p+q<=n, EXACTLY over the number field
Q(cos(pi/n), cos(pi/m)).  No developer kernel, coefficient matrix or closed
formula is used to build the cardinals; the closed formulas of theorem 13 are
only compared afterwards, by exact field equality.  Signs of (nonzero) exact
field elements are read from 60-digit evaluation.
"""
import json
import sys
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ


def cheb(z, N, K):
    t = [K.one, z]
    for _ in range(2, N + 1):
        t.append(2 * z * t[-1] - t[-2])
    return t[:N + 1]


def run(n):
    m = n + 1
    gens = [sp.cos(sp.pi / d) for d in (n, m) if not sp.cos(sp.pi / d).is_rational]
    K = QQ.algebraic_field(*gens) if gens else QQ
    X = cheb(K.from_sympy(sp.cos(sp.pi / n)), n, K)      # cos(j pi/n)
    Y = cheb(K.from_sympy(sp.cos(sp.pi / m)), m, K)      # cos(k pi/m)
    nodes = [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]
    basis = [(p, q) for p in range(n + 1) for q in range(n + 1 - p)]
    assert len(nodes) == len(basis) == (n + 1) * (n + 2) // 2
    TX = [cheb(X[j], n, K) for j in range(n + 1)]
    TY = [cheb(Y[k], n, K) for k in range(m + 1)]
    VT = DomainMatrix([[TX[j][p] * TY[k][q] for (j, k) in nodes] for (p, q) in basis],
                      (len(basis), len(nodes)), K)
    one, zero = K.one, K.zero
    s = lambda e: one if e % 2 == 0 else -one
    rhs = DomainMatrix([[s(p + q),
                         s(p - 1) * K(p * p) * s(q) if p else zero,
                         s(p) * s(q - 1) * K(q * q) if q else zero] for (p, q) in basis],
                       (len(basis), 3), K)
    sol = VT.lu_solve(rhs)
    rows = sol.to_list()          # rows[i] = [L_i(c), L_i,x(c), L_i,y(c)] as field elements
    num = lambda e: sp.N(K.to_sympy(e), 60)
    fails = []
    # ---- part 1: zero mask -------------------------------------------------
    zero_mask = [(j, k) for (j, k), r in zip(nodes, rows) if r[0] == zero]
    expected_zero = [(j, 0) for j in range(2, n + 1, 2)]
    if sorted(zero_mask) != sorted(expected_zero):
        fails.append('zero mask')
    # ---- closed forms, exact field equality ---------------------------------
    for (j, k), r in zip(nodes, rows):
        tau = K((-1) ** (n + j))
        eps = QQ(1, 2) if j in (0, n) else QQ(1)
        eta = QQ(1, 2) if k in (0, m) else QQ(1)
        w = K(2 * eps * eta / (n * m))
        if j == k == 0:
            ev = K(QQ((-1) ** n, m))
            egx = K(-QQ((-1) ** n) * QQ(2 * n * n + 1, 6 * m))
            egy = K(-QQ((-1) ** n) * QQ(2 * n + 1, 6))
        else:
            a, b = X[j], Y[k]
            d, C = b - a, one - b
            if d == zero:
                fails.append(f'd=0 at {(j, k)}')
                continue
            ev = 2 * w * tau * C / d
            egx = 2 * w * tau * (-K(n * n) * C / (2 * d) + K(n) * (a * b - one) / d ** 2
                                 - C * a / d ** 2 + 2 * C * (one - a * a) / d ** 3)
            egy = 2 * w * tau * (-K(m * m) * C / (2 * d) + K(n) * (a * b - one) / d ** 2
                                 + C * (one + 2 * b) / d ** 2 + 2 * C * (one - b * b) / d ** 3)
        for name, got, exp in (('value', r[0], ev), ('gx', r[1], egx), ('gy', r[2], egy)):
            if got != exp:
                fails.append(f'{name} {(j, k)}')
        if k > 0:
            sg = 1 if num(r[0]) > 0 else -1
            if sg != (-1) ** (n + j) * (1 if m * j - n * k > 0 else -1):
                fails.append(f'sign {(j, k)}')
            if sg != (-1) ** (n + j) * (1 if j >= k else -1):
                fails.append(f'sign-alt {(j, k)}')
        if (j, k) in expected_zero:
            if r[1] != r[2]:
                fails.append(f'zero-gradient unequal {(j, k)}')
            if r[1] != -2 * w * tau * K(n) / (one - X[j]):
                fails.append(f'zero-gradient formula {(j, k)}')
    # ---- part 3: zero contribution, slopes -----------------------------------
    sgn = {}
    for (j, k), r in zip(nodes, rows):
        sgn[(j, k)] = 0 if r[0] == zero else (1 if num(r[0]) > 0 else -1)
    Zx = zero
    Zy = zero
    for (j, k), r in zip(nodes, rows):
        if sgn[(j, k)] == 0:
            Zx += r[1] if num(r[1]) > 0 else -r[1]
            Zy += r[2] if num(r[2]) > 0 else -r[2]
    if Zx != K(QQ(n - 1, 6)) or Zy != K(QQ(n - 1, 6)):
        fails.append('zero contribution (n-1)/6')
    A = Zx
    B = Zy
    AI = zero
    BI = zero
    for (j, k), r in zip(nodes, rows):
        if sgn[(j, k)] != 0:
            A += K(sgn[(j, k)]) * r[1]
            B += K(sgn[(j, k)]) * r[2]
            if (j, k) != (0, 0):
                AI += K(sgn[(j, k)]) * r[1]
                BI += K(sgn[(j, k)]) * r[2]
    if A != K(-QQ(n * n + 2, 6 * m)) + AI or B != K(-QQ(n + 2, 6)) + BI:
        fails.append('slope reduction (2)')
    Lc = sum(abs(num(r[0])) for r in rows)
    res = {'n': n, 'field_generators': [str(g) for g in gens], 'cardinals': len(nodes),
           'zero_mask': zero_mask, 'zero_contribution_x': str(K.to_sympy(Zx)),
           'zero_contribution_y': str(K.to_sympy(Zy)),
           'A_n': str(sp.N(K.to_sympy(A), 25)), 'B_n': str(sp.N(K.to_sympy(B), 25)),
           'Lambda_c': str(sp.N(Lc, 25)),
           'A_over_n2_Lc': float(sp.N(K.to_sympy(A), 30) / (n * n * Lc)),
           'B_over_m2_Lc': float(sp.N(K.to_sympy(B), 30) / (m * m * Lc)),
           'failures': fails}
    if n == 2:
        res['n2_exact_slopes'] = [str(K.to_sympy(A)), str(K.to_sympy(B))]
        if A != K(QQ(-7, 3)) or B != K(QQ(-14, 3)):
            fails.append('n2 slopes')
    return res


if __name__ == '__main__':
    degrees = [int(a) for a in sys.argv[1:]] or [2, 3, 4, 5, 6]
    out = []
    for n in degrees:
        t0 = time.time()
        r = run(n)
        r['seconds'] = round(time.time() - t0, 2)
        out.append(r)
        print(json.dumps({k: r[k] for k in ('n', 'zero_contribution_x', 'A_n', 'B_n', 'failures', 'seconds')}),
              file=sys.stderr, flush=True)
    print(json.dumps({'kind': 'auditor independent exact number-field check of theorem 13 parts 1-3; finite n only',
                      'sympy': sp.__version__, 'results': out,
                      'all_pass': all(not r['failures'] for r in out)}, indent=1))
