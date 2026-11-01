"""R05: exact symbolic verification of the boundary-node part of PD-T?bivariate-lanczos-claude-313.

Certificate p*_n = (1-c)(q1^2 - q0 q2) + c(q2^2 - q1 q3), c = 1/10, with the normalised two-term
Padua generators q_m = -g_m/lambda_m (lambda_0 = 2^n, lambda_m = 2^(n-1), m = 1..3; n >= 3),
g_m = T_{n-m}(x)T_m(y) - T_m(x)T_{n+1-m}(y).  At a node, Hess p*(u,u) is proportional
(positive factor 2/4^(n-1)) to Q(w) = (1-c)(w1^2 - w0 w2) + c(w2^2 - w1 w3), w_m = d_u g_m
(m = 1..3), w_0 = d_u g_0 / 2.

Boundary gradient formulas (proved in theory file 313 by Chebyshev identities), t = cos(angle):
  E1 (x = 1, y = cos phi, 0 < phi < pi): grad g_m = (n(n-2m) T_m(t), (n+1) U_{m-1}(t))
  E3 (y = 1, x = cos theta, 0 < theta < pi): grad g_m = (-n U_{m-1}(t), -(n+1)(n+1-2m) T_m(t))
  C11 (corner (1,1)): grad g_m = (n(n-2m), -(n+1)(n+1-2m))
(E2: x = -1, E4: y = -1 and the other corners reduce to these by sign changes (-1)^m and
 u_1 -> -u_1 or u_2 -> -u_2, which leave PD-ness unchanged because Q only contains
 products w_j w_k with j + k even.)

This script (1) cross-checks the boundary gradient formulas against direct differentiation
for n = 3..8 at all boundary Padua nodes (floating, MEASURED sanity check), (2) computes
A, B, X (Q = A u1^2 + X u1 u2 + B u2^2) and D = 4AB - X^2 symbolically in (n, t) with
sympy (exact rational arithmetic), (3) prints D in s = 1 - t^2 and the endpoint bounds
used in the proof, (4) evaluates D exactly at the n = 4 edge nodes.

Usage: python3 r05_boundary_proof.py
"""
import numpy as np
import sympy as sp
from numpy.polynomial import chebyshev as Ch


def check_gradient_formulas():
    def cT(k):
        a = np.zeros(k + 1); a[k] = 1; return a
    T = lambda k, z: Ch.chebval(z, cT(k))
    dT = lambda k, z: Ch.chebval(z, Ch.chebder(cT(k))) if k > 0 else 0.0
    U = lambda k, z: (dT(k + 1, z) / (k + 1)) if k >= 0 else 0.0
    err = 0.0
    for n in range(3, 9):
        for j in range(n + 1):
            for k in range(n + 2):
                if (j + k) % 2:
                    continue
                x, y = np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1))
                for m in range(4):
                    gx = dT(n - m, x) * T(m, y) - dT(m, x) * T(n + 1 - m, y)
                    gy = T(n - m, x) * dT(m, y) - T(m, x) * dT(n + 1 - m, y)
                    if j == 0 and 0 < k < n + 1:          # E1
                        f = (n * (n - 2 * m) * T(m, y), (n + 1) * U(m - 1, y))
                    elif j == n and 0 < k < n + 1:        # E2: (-1)^(n+m) * (-n(n-2m)T_m, (n+1)U_{m-1})
                        sg = (-1) ** (n + m)
                        f = (sg * (-n * (n - 2 * m) * T(m, y)), sg * (n + 1) * U(m - 1, y))
                    elif k == 0 and 0 < j < n:            # E3
                        f = (-n * U(m - 1, x), -(n + 1) * (n + 1 - 2 * m) * T(m, x))
                    elif k == n + 1 and 0 < j < n:        # E4: (-1)^(n+m) * (n U_{m-1}, -(n+1)(n+1-2m)T_m)
                        sg = (-1) ** (n + m)
                        f = (sg * n * U(m - 1, x), -sg * (n + 1) * (n + 1 - 2 * m) * T(m, x))
                    elif (j, k) == (0, 0):                # C11
                        f = (n * (n - 2 * m), -(n + 1) * (n + 1 - 2 * m))
                    elif (j, k) == (0, n + 1):            # (1,-1), n odd: (-1)^m (n(n-2m), (n+1)(n+1-2m))
                        sg = (-1) ** m
                        f = (sg * n * (n - 2 * m), sg * (n + 1) * (n + 1 - 2 * m))
                    elif (j, k) == (n, 0):                # (-1,1), n even: -(-1)^m (n(n-2m), (n+1)(n+1-2m))
                        sg = -(-1) ** m
                        f = (sg * n * (n - 2 * m), sg * (n + 1) * (n + 1 - 2 * m))
                    else:
                        continue                          # interior node
                    err = max(err, abs(gx - f[0]), abs(gy - f[1]))
    print(f"(1) boundary gradient formulas vs direct differentiation, n = 3..8, m = 0..3: max error {err:.2e}")


def symbolic():
    n, t, s, u1, u2 = sp.symbols('n t s u1 u2', real=True)
    c = sp.Rational(1, 10)
    Tm = {0: 1, 1: t, 2: 2 * t ** 2 - 1, 3: 4 * t ** 3 - 3 * t}
    Um = {-1: 0, 0: 1, 1: 2 * t, 2: 4 * t ** 2 - 1}

    def Q(w):
        return sp.Poly(sp.expand((1 - c) * (w[1] ** 2 - w[0] * w[2]) + c * (w[2] ** 2 - w[1] * w[3])), u1, u2)
    fams = {
        'E1': [n ** 2 * u1 / 2] + [n * (n - 2 * m) * Tm[m] * u1 + (n + 1) * Um[m - 1] * u2 for m in (1, 2, 3)],
        'E3': [-(n + 1) ** 2 * u2 / 2] + [-n * Um[m - 1] * u1 - (n + 1) * (n + 1 - 2 * m) * Tm[m] * u2 for m in (1, 2, 3)],
        'C11': [(n ** 2 * u1 - (n + 1) ** 2 * u2) / 2] + [n * (n - 2 * m) * u1 - (n + 1) * (n + 1 - 2 * m) * u2 for m in (1, 2, 3)],
    }
    out = {}
    for name, w in fams.items():
        P = Q(w)
        A = P.coeff_monomial(u1 ** 2); B = P.coeff_monomial(u2 ** 2); X = P.coeff_monomial(u1 * u2)
        D = sp.expand(4 * A * B - X ** 2)
        print(f"(2) {name}: A = {sp.factor(A)};  B = {sp.factor(B)};  X = {sp.factor(X)}")
        print(f"    4AB - X^2 = {sp.factor(D)}")
        out[name] = (A, B, X, D)
        if name in ('E1', 'E3'):
            pref = n ** 2 * (n + 1) ** 2
            Dr = sp.expand(sp.cancel(D / pref))
            Ds = sp.Poly(sp.expand(Dr.subs(t, sp.sqrt(1 - s))), s)
            co = [sp.factor(a) for a in Ds.all_coeffs()]
            L0, L1 = co[-1], sp.factor(co[-1] + co[-2])
            print(f"(3) {name}: (4AB-X^2)/(n^2(n+1)^2) = {co[0]} s^2 + ({co[1]}) s + {co[2]}   [s = 1 - t^2]")
            print(f"    s^2-coefficient > 0, so D >= min(L(0), L(1)) on [0,1]: L(0) = {L0}, L(1) = {L1}")
            out[name] = out[name] + (Dr,)
    # n = 4 edge nodes
    A, B, X, D, Dr = out['E1']
    vals = [sp.radsimp(sp.nsimplify(sp.simplify(Dr.subs({n: 4, t: sp.cos(k * sp.pi / 5)})))) for k in (1, 2, 3, 4)]
    print(f"(4) n = 4, E1/E2 nodes phi = k pi/5 (k = 1..4): D/(n^2(n+1)^2) = {vals}; all > 0: "
          f"{all(sp.N(v) > 0 for v in vals)}  (exact: 247^2 = {247**2} > 89^2*5 = {89**2*5})")


if __name__ == '__main__':
    check_gradient_formulas()
    symbolic()
