"""Reviewer (L3 reconstruction 02): symbolic checks behind PD-T?...-312 and -313 (all n).

(1) 312 interior quadratic form. With v_m := A sin(m al) + B sin(m be) (v_0 = 0),
    Q_c := (1-c) v_1^2 + c (v_2^2 - v_1 v_3)  equals  sin^2(al) A^2 + sin^2(be) B^2 + 2 W A B,
    W = (S - T)(1 - 8 c S T), al = th + ph, be = th - ph, S = sin^2 th, T = sin^2 ph, and
    sin(al) sin(be) = S - T. Checked as an exact identity of Laurent polynomials in
    a = e^{i th}, b = e^{i ph} (no node condition used).
(2) 313 boundary forms with SYMBOLIC n, re-derived from the reviewer's own hand-derived gradient
    formulas (E1: x = 1; E3: y = 1; C11: corner (1,1)); Q(w) = (9/10)(w1^2 - w0 w2) + (1/10)(w2^2 - w1 w3),
    w0 = d_u g0 / 2. Prints A, X, B and (4AB - X^2)/(n^2 (n+1)^2) in s = 1 - t^2, and compares with the
    developer's printed closed forms (typed in from 313, not imported).
(3) n = 4, E1/E2 edge nodes (phi = 2 pi/5, 4 pi/5): exact value of the E1 expression.
"""
import sympy as sp

a, b, A, B, c = sp.symbols('a b A B c')
I = sp.I


def s_(z, m=1):   # sin(m*arg z) for |z| = 1, as Laurent polynomial
    return (z ** m - z ** (-m)) / (2 * I)


def check_312():
    al, be = a * b, a / b
    v = {m: A * s_(al, m) + B * s_(be, m) for m in (1, 2, 3)}
    Qc = (1 - c) * v[1] ** 2 + c * (v[2] ** 2 - v[1] * v[3])
    S, T = s_(a) ** 2, s_(b) ** 2
    W = (S - T) * (1 - 8 * c * S * T)
    rhs = s_(al) ** 2 * A ** 2 + s_(be) ** 2 * B ** 2 + 2 * W * A * B
    d1 = sp.simplify(sp.expand(Qc - rhs))
    d2 = sp.simplify(sp.expand(s_(al) * s_(be) - (S - T)))
    print(f"(1) 312 identity Q_c - [sin^2 al A^2 + sin^2 be B^2 + 2 W A B] = {d1};  sin al sin be - (S - T) = {d2}")
    return d1 == 0 and d2 == 0


def check_313():
    n, t, s, u1, u2 = sp.symbols('n t s u1 u2')
    T_ = [sp.Integer(1), t, 2 * t ** 2 - 1, 4 * t ** 3 - 3 * t]
    U_ = {-1: sp.Integer(0), 0: sp.Integer(1), 1: 2 * t, 2: 4 * t ** 2 - 1}
    grads = {
        'E1': [(n * (n - 2 * m) * T_[m], (n + 1) * U_[m - 1]) for m in range(4)],
        'E3': [(-n * U_[m - 1], -(n + 1) * (n + 1 - 2 * m) * T_[m]) for m in range(4)],
        'C11': [(n * (n - 2 * m), -(n + 1) * (n + 1 - 2 * m)) for m in range(4)],
    }
    dev = {  # developer's printed closed forms (313 file / r05_boundary_proof.log), typed in
        'E1': (sp.Rational(32, 5), n * (121 * n - 1040) / 100, 99 * n ** 2 / 100),
        'E3': (sp.Rational(32, 5), (n + 1) * (121 * n - 919) / 100, 99 * (n + 1) ** 2 / 100),
    }
    ok = True
    for name, gr in grads.items():
        w = [gx * u1 + gy * u2 for (gx, gy) in gr]
        w[0] = w[0] / 2
        Q = sp.expand(sp.Rational(9, 10) * (w[1] ** 2 - w[0] * w[2]) + sp.Rational(1, 10) * (w[2] ** 2 - w[1] * w[3]))
        P = sp.Poly(Q, u1, u2)
        Aq, Bq, Xq = P.coeff_monomial(u1 ** 2), P.coeff_monomial(u2 ** 2), P.coeff_monomial(u1 * u2)
        D = sp.expand(4 * Aq * Bq - Xq ** 2)
        print(f"(2) {name}: A = {sp.factor(Aq)};  X = {sp.factor(Xq)};  B = {sp.factor(Bq)}")
        if name == 'C11':
            ok &= sp.simplify(D - 99 * n ** 2 * (n + 1) ** 2 / 25) == 0
            ok &= sp.simplify(Aq - n ** 2 * (9 * n ** 2 - 36 * n + 80) / 20) == 0
            print(f"    C11: 4AB - X^2 = {sp.factor(D)}  (dev: 99 n^2 (n+1)^2/25)")
            continue
        Dr = sp.expand(sp.cancel(D / (n ** 2 * (n + 1) ** 2)))
        assert sp.expand(Dr.subs(t, -t) - Dr) == 0      # even in t
        Ds = sp.Poly(sp.expand(Dr.subs(t ** 2, 1 - s).subs(t, sp.sqrt(1 - s))), s)
        co = Ds.all_coeffs()
        print(f"    {name}: (4AB - X^2)/(n^2(n+1)^2) = ({sp.factor(co[0])}) s^2 + ({sp.factor(co[1])}) s + {sp.factor(co[2])}")
        okd = all(sp.simplify(x1 - x2) == 0 for x1, x2 in zip(co, dev[name]))
        print(f"    matches developer's closed form: {okd}; value at s=1 (dropping s^2): {sp.factor(co[1] + co[2])}")
        ok &= okd
        if name == 'E1':
            Bs = Bq
            ok &= sp.simplify(Bs - (n + 1) ** 2) == 0
            vals = []
            for k in (2, 4):
                sv = sp.sin(k * sp.pi / 5) ** 2
                val = sp.nsimplify(sp.radsimp(sp.expand(sp.expand_trig(Ds.as_expr().subs({n: 4, s: sv})))))
                vals.append((k, sp.simplify(val), sp.N(val, 20)))
            print(f"(3) n=4, E1/E2 nodes k=2,4 (phi = k pi/5): {vals}")
            ok &= all(v[2] > 0 for v in vals)
        if name == 'E3':
            ok &= sp.simplify(Aq - n ** 2) == 0
    return ok


if __name__ == '__main__':
    r1 = check_312()
    r2 = check_313()
    print(f"RESULT: 312 identity {'PASS' if r1 else 'FAIL'}; 313 closed forms {'PASS' if r2 else 'FAIL'}")
