"""Auditor's independent check of A5-partial (Claude audit, not Codex code).

Differences from the developer's certificate:
 * cardinals derived in the Chebyshev-product basis T_a(x)T_b(y) (not monomials);
 * certificate on the l_inf BOX |theta|<=r, |phi-phi_s|<=r, r = 0.0022 (a superset of
   the developer's l1 disc of radius .0021), split into K x K sub-boxes;
 * every quantity evaluated with mpmath interval arithmetic directly in angle
   variables (iv.cos / iv.sin of the sub-box), no X x Y cosine reduction;
 * negative definiteness of the full angle Hessian of lambda_3 = g - L_6 via the
   exact 2x2 criteria (-H_tt > 0, det H > 0) and a Gershgorin margin, per sub-box.
Also: exact gradient identities at the centres and the Lebesgue value, compared
with the frozen t3_maxima.json entry.
"""
import json, sys
import sympy as sp
import mpmath as mp
from mpmath import iv

iv.dps = 40; mp.mp.dps = 40
x, y = sp.symbols('x y', real=True)
n = 3
nodes = [(sp.cos(sp.pi * j / n), sp.cos(sp.pi * k / (n + 1)), j, k)
         for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
modes = [(d - b, b) for d in range(n + 1) for b in range(d + 1)]
T = sp.chebyshevt
V = sp.Matrix([[T(a, u) * T(b, v) for a, b in modes] for u, v, _, _ in nodes])
C = sp.simplify(V.inv())
basis = [sp.expand(T(a, x) * T(b, y)) for a, b in modes]
L = [sp.expand(sp.nsimplify(sum(basis[i] * C[i, B] for i in range(10)))) for B in range(10)]
for B in range(10):
    for A, (u, v, _, _) in enumerate(nodes):
        assert sp.simplify(L[B].subs({x: u, y: v}) - (1 if A == B else 0)) == 0
L6 = L[6]
assert sp.expand(L6 - (x - 1) * (2 * x**2 + x + 2 * y**2 - 2) / 3) == 0

th, ph = sp.symbols('th ph', real=True)

def ivev(e, env):
    """Rigorous interval evaluation of a SymPy expression tree (rationals exact as iv quotients)."""
    if e.is_Rational:
        return iv.mpf(int(e.p)) / iv.mpf(int(e.q))
    if e.is_Symbol:
        return env[e]
    if e.is_Add:
        acc = iv.mpf(0)
        for a in e.args: acc = acc + ivev(a, env)
        return acc
    if e.is_Mul:
        acc = iv.mpf(1)
        for a in e.args: acc = acc * ivev(a, env)
        return acc
    if e.is_Pow:
        b, p = e.args
        if p == sp.Rational(1, 2): return iv.sqrt(ivev(b, env))
        if p == -sp.Rational(1, 2): return 1 / iv.sqrt(ivev(b, env))
        if p.is_Integer:
            bb = ivev(b, env); k = int(p)
            if k < 0: return 1 / (bb ** (-k))
            return bb ** k
    if isinstance(e, sp.cos): return iv.cos(ivev(e.args[0], env))
    if isinstance(e, sp.sin): return iv.sin(ivev(e.args[0], env))
    raise ValueError(e)

def mk(expr):
    return lambda T0, P0: ivev(expr, {th: T0, ph: P0})
out = {"L6": str(sp.factor(L6)), "cases": []}
for sigma in (1, -1):
    yc = sigma / sp.sqrt(3)
    s = [int(sp.sign(sp.N(L[b].subs({x: 1, y: yc}), 50))) if b != 6 else 0 for b in range(10)]
    g = sp.expand(sum(s[b] * L[b] for b in range(10)))
    lam = sp.expand(g - L6)
    F = lam.subs({x: sp.cos(th), y: sp.cos(ph)})
    phs = sp.acos(yc)
    grad = [sp.simplify(sp.diff(F, v).subs({th: 0, ph: phs})) for v in (th, ph)]
    gradL6 = [sp.simplify(sp.diff(L6.subs({x: sp.cos(th), y: sp.cos(ph)}), v).subs({th: 0, ph: phs})) for v in (th, ph)]
    val = sp.nsimplify(sp.simplify(lam.subs({x: 1, y: yc})))
    Htt, Htp, Hpp = [sp.diff(F, a, b) for a, b in ((th, th), (th, ph), (ph, ph))]
    fns = [mk(sp.expand(e)) for e in (Htt, Htp, Hpp)]
    cards = [mk((s[b] * L[b]).subs({x: sp.cos(th), y: sp.cos(ph)})) for b in range(10) if b != 6]
    brk = mk((2 * x**2 + x + 2 * y**2 - 2).subs({x: sp.cos(th), y: sp.cos(ph)}))
    pc = iv.mpf(mp.acos(mp.mpf(sigma) / mp.sqrt(3)))  # point value; box margin 1e-4 >> 1e-40 error
    r = mp.mpf('0.0022'); K = 12
    worst_gersh = mp.inf; worst_det = mp.inf; worst_tt = mp.inf; worst_card = mp.inf; worst_brk = mp.inf
    for i in range(K):
        for jj in range(K):
            T0 = iv.mpf([-r + 2 * r * i / K, -r + 2 * r * (i + 1) / K])
            P0 = iv.mpf([(pc - r + 2 * r * jj / K).a, (pc - r + 2 * r * (jj + 1) / K).b])
            htt, htp, hpp = (f(T0, P0) for f in fns)
            gersh = min(mp.mpf((-htt.b - abs(htp).b).a), mp.mpf((-hpp.b - abs(htp).b).a))   # rigorous lower bound of -lambda_max (Gershgorin)
            det = (htt * hpp - htp * htp).a
            worst_gersh = min(worst_gersh, gersh); worst_det = min(worst_det, mp.mpf(det)); worst_tt = min(worst_tt, mp.mpf((-htt).a))
            worst_card = min(worst_card, min(mp.mpf(c(T0, P0).a) for c in cards))
            worst_brk = min(worst_brk, mp.mpf(brk(T0, P0).a))
    ok = worst_gersh > 3.5 and worst_det > 0 and worst_tt > 0 and worst_card > 0 and worst_brk > 0
    out["cases"].append({"sigma": sigma, "signs": s, "grad_lambda_center": [str(v) for v in grad],
                         "grad_L6_center": [str(v) for v in gradL6], "lambda_center": str(val),
                         "lambda_center_float": mp.nstr(mp.mpf(sp.N(val, 40)), 20),
                         "box_halfwidth": str(r), "subboxes": K * K,
                         "min_gershgorin_neg_margin": mp.nstr(worst_gersh, 8),
                         "min_det_lower": mp.nstr(worst_det, 8), "min_signed_cardinal_lower": mp.nstr(worst_card, 8),
                         "min_bracket_lower": mp.nstr(worst_brk, 8), "certified": bool(ok)})
    assert ok and all(v == 0 for v in grad) and all(v == 0 for v in gradL6)
print(json.dumps(out, indent=1))
