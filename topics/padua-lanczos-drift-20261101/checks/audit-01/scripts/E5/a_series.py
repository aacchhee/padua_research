#!/usr/bin/env python3
"""Auditor E5 check A: exact SymPy series reconstruction of record30 limits and
record32 part 3, written independently of the developer checker.

Substitute n = 1/h.  With theta = pi*h, phi = pi*h/(1+h), t = a*h^4 every
argument of the cosines is analytic at h = 0, so g_m(zeta_n) is an analytic
function of h; its Taylor coefficients give the limits along h = 1/n exactly.
Also re-derives the two derivative formulas from the raw definition using only
cos(n*theta) = -1, sin(n*theta) = 0, cos((n+1)phi) = -1, sin((n+1)phi) = 0.
"""
import json
import sympy as s

h, a, A = s.symbols('h a A', positive=True)
out = {}

# ---- derivative identities from the raw definition (symbolic n, m) ----
n, m, th, ph, t = s.symbols('n m theta phi t', real=True)
cN, sN, cM, sM = s.symbols('cN sN cM sM')  # placeholders
raw = (s.cos((n - m)*(th + t))*s.cos(m*(ph + t))
       - s.cos(m*(th + t))*s.cos((n + 1 - m)*(ph + t)))
d1 = s.diff(raw, t).subs(t, 0)
d2 = s.diff(raw, t, 2).subs(t, 0)


# expand cos((n+1-m)phi) = cos((n+1)phi - m phi) explicitly
def node_reduce(expr):
    rep = {}
    for f in expr.atoms(s.cos, s.sin):
        arg = s.expand(f.args[0])
        rep[f] = f
    e = expr
    # rewrite each trig of a linear combination by addition formulas manually
    U, V = s.symbols('U V')
    def tr(fn, arg):
        arg = s.expand(arg)
        # split into part with n*theta, (n+1)*phi and remainder
        cth = arg.coeff(n*th) if arg.has(n*th) else 0
        rest = s.expand(arg - cth*n*th)
        cph = rest.coeff(n*ph) if rest.has(n*ph) else 0
        rest = s.expand(rest - cph*n*ph)
        # n*phi = (n+1)phi - phi = pi - phi
        rest = s.expand(rest - cph*ph)          # remove the extra phi
        big = cth*s.pi + cph*s.pi               # integer multiples of pi
        return fn(big + rest)
    e = e.replace(lambda q: isinstance(q, s.cos), lambda q: tr(s.cos, q.args[0]))
    e = e.replace(lambda q: isinstance(q, s.sin), lambda q: tr(s.sin, q.args[0]))
    return s.simplify(s.expand_trig(e))


D_claim = (n + 1)*s.cos(m*th)*s.sin(m*ph) - n*s.sin(m*th)*s.cos(m*ph)
F2_claim = (-(2*n + 1 - 2*m)*s.cos(m*th)*s.cos(m*ph)
            - 2*m*s.sin(m*th)*s.sin(m*ph))
f0 = node_reduce(raw.subs(t, 0))
dd1 = node_reduce(d1)
dd2 = node_reduce(d2)
out['raw_f0_reduces_to_zero'] = bool(s.simplify(f0) == 0)
out['raw_first_derivative_matches'] = bool(s.simplify(dd1 - D_claim) == 0)
out['raw_second_derivative_matches'] = bool(s.simplify(dd2 - F2_claim) == 0)
# sine form: D = [sin(k m d) - k sin(m d)]/2 with theta+phi = k d, d=theta-phi
# check sine form numerically-free: use sin/cos addition with free symbols
al, be = s.symbols('al be', real=True)
Dab = (n + 1)*s.cos(al)*s.sin(be) - n*s.sin(al)*s.cos(be)
Sab = (s.sin(al + be) - (2*n + 1)*s.sin(al - be))/2
out['sine_form_identity'] = bool(s.simplify(s.expand_trig(Dab - Sab)) == 0)
# theta + phi = (2n+1) d  with theta = pi/n, phi = pi/(n+1)
out['theta_plus_phi_eq_k_d'] = bool(s.simplify(
    s.pi/n + s.pi/(n + 1) - (2*n + 1)*(s.pi/n - s.pi/(n + 1))) == 0)

# ---- series along h = 1/n ----
def g_series(mm, tt, order):
    nn = 1/h
    theta = s.pi*h
    phi = s.pi*h/(1 + h)
    arg1 = s.expand((nn - mm)*(theta + tt))
    arg2 = s.expand(mm*(phi + tt))
    arg3 = s.expand(mm*(theta + tt))
    arg4 = s.expand((nn + 1 - mm)*(phi + tt))
    g = s.cos(arg1)*s.cos(arg2) - s.cos(arg3)*s.cos(arg4)
    return s.series(g, h, 0, order).removeO()


lim7 = {}
G = []
for mm in range(4):
    ser = g_series(mm, a*h**4, 9)
    ser = s.expand(ser)
    low = [s.simplify(ser.coeff(h, k)) for k in range(0, 7)]
    c7 = s.simplify(ser.coeff(h, 7))
    expected = -a**2 - s.Rational(2, 3)*a*s.pi**3*mm**3
    lim7[mm] = {'lower_coeffs_zero': all(c == 0 for c in low),
                'h7_coeff': str(c7),
                'matches_claim': bool(s.simplify(c7 - expected) == 0)}
    G.append(ser)
out['n7_g_limits'] = lim7

P = 9*(G[1]**2 - G[0]*G[2]/2) + G[2]**2 - G[1]*G[3]
P = s.expand(P)
lowP = [s.simplify(P.coeff(h, k)) for k in range(0, 14)]
c14 = s.factor(s.simplify(P.coeff(h, 14)))
out['P_lower_coeffs_zero'] = all(c == 0 for c in lowP)
out['n14_P_limit_as_poly_in_a'] = str(c14)
val = s.simplify(c14.subs(a, 20*s.pi**3/9))
out['n14_P_limit_at_a'] = str(val)
out['n14_P_limit_matches'] = bool(s.simplify(val + 6400*s.pi**12/729) == 0)
# negativity interval in a
c = s.Rational(2, 3)*s.pi**3
roots = s.solve(s.Eq(c14/a**2, 0), a)
out['n14_P_zero_set_in_a_over_c'] = [str(s.nsimplify(s.simplify(r/c))) for r in roots]

# distance
theta = s.pi*h
phi = s.pi*h/(1 + h)
dx = s.series((s.cos(theta + a*h**4) - s.cos(theta))/h**5, h, 0, 2).removeO()
dy = s.series((s.cos(phi + a*h**4) - s.cos(phi))/h**5, h, 0, 2).removeO()
out['n5_dx_limit'] = str(s.simplify(dx.subs(h, 0)))
out['n5_dy_limit'] = str(s.simplify(dy.subs(h, 0)))
dist_lim = s.sqrt(dx.subs(h, 0)**2 + dy.subs(h, 0)**2)
out['n5_dist_limit'] = str(s.simplify(dist_lim.subs(a, 20*s.pi**3/9)))
out['n5_dist_limit_matches'] = bool(s.simplify(
    dist_lim.subs(a, 20*s.pi**3/9) - 20*s.sqrt(2)*s.pi**4/9) == 0)

# ---- record32 part3: fixed A, increment A/n^3 ----
Gc = []
ok = True
for mm in range(4):
    ser = s.expand(g_series(mm, A*h**3, 7))
    ok = ok and all(s.simplify(ser.coeff(h, k)) == 0 for k in range(5))
    ok = ok and s.simplify(ser.coeff(h, 5) + A**2) == 0
    Gc.append(ser)
Pc = s.expand(9*(Gc[1]**2 - Gc[0]*Gc[2]/2) + Gc[2]**2 - Gc[1]*Gc[3])
okP = all(s.simplify(Pc.coeff(h, k)) == 0 for k in range(10))
out['coarse_n5_g_limits_all_minus_A2'] = bool(ok)
out['coarse_P_low_zero'] = bool(okP)
out['coarse_n10_P_limit'] = str(s.factor(s.simplify(Pc.coeff(h, 10))))

# ---- record32 parts 1-2 identities ----
dd = s.symbols('d', real=True)
out['equal_phase_identity'] = bool(s.simplify(s.expand_trig(
    9*s.sin(dd)**2 + s.sin(2*dd)**2 - s.sin(dd)*s.sin(3*dd)
    - 10*s.sin(dd)**2)) == 0)
b, C = s.symbols('b C', real=True)
hseq = [b*s.sin(C - j*dd) for j in range(4)]
Pe = 9*(hseq[1]**2 - hseq[0]*hseq[2]/2) + hseq[2]**2 - hseq[1]*hseq[3]
Pe_claim = b**2*(s.Rational(9, 2)*s.sin(C - dd)**2 + s.Rational(11, 2)*s.sin(dd)**2)
diff = s.expand(s.expand_trig(Pe - Pe_claim))
diff = s.simplify(diff.rewrite(s.exp))
out['edge_sine_sequence_identity'] = bool(s.simplify(diff) == 0)
print(json.dumps(out, indent=1, default=str))
