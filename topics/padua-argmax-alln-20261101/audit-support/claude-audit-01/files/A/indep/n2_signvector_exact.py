"""Independent exact n=2 check (auditor code; SymPy exact rationals).

Route differs from the developer's Bernstein-quadrant proof: lambda(z)=max_sigma sum sigma_i L_i(z)
over the 64 sign vectors, so max_Q lambda = max_sigma max_Q f_sigma and
{lambda=M} = union over sigma with max f_sigma = M of argmax_Q f_sigma.
Each f_sigma is a quadratic; its maximizers on the closed square lie among interior
critical points, critical points of the four edge restrictions, and the corners.
Cardinals come from a SymPy linear solve in the monomial basis, not from the record.
"""
import itertools
import json
import sys

import sympy as sp

x, y, s = sp.symbols("x y s", real=True)
n = 2
nodes = [(sp.cos(j * sp.pi / n), sp.cos(k * sp.pi / (n + 1)), j, k)
         for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
mon = [x**a * y**b for a in range(n + 1) for b in range(n + 1 - a)]
V = sp.Matrix([[m.subs({x: X, y: Y}) for m in mon] for X, Y, j, k in nodes])
Vi = V.inv()
L = [sp.expand(sum(Vi[r, c] * mon[r] for r in range(len(mon)))) for c in range(len(nodes))]
for i, (X, Y, j, k) in enumerate(nodes):
    for l in range(len(L)):
        assert sp.simplify(L[l].subs({x: X, y: Y}) - (1 if i == l else 0)) == 0


def max_on_square(f):
    """Exact max of a polynomial of degree<=2 on [-1,1]^2 and the full argmax set
    (returns ('points', set) or raises if a continuum of maximizers occurs)."""
    cands = set()
    curves = []
    # interior
    sol = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    for d in sol:
        if x in d and y in d and not d[x].free_symbols and not d[y].free_symbols:
            if -1 < d[x] < 1 and -1 < d[y] < 1:
                cands.add((d[x], d[y]))
        elif sol:
            curves.append(("interior", d))
    if sp.diff(f, x) == 0 and sp.diff(f, y) == 0:
        curves.append(("constant", {}))
    # edges
    for fix, val in ((x, -1), (x, 1), (y, -1), (y, 1)):
        g = sp.expand(f.subs(fix, val))
        other = y if fix == x else x
        dg = sp.diff(g, other)
        if dg == 0:
            curves.append(("edge-constant", (fix, val)))
            continue
        for r in sp.solve(dg, other):
            if r.is_real and -1 < r < 1:
                cands.add((val, r) if fix == x else (r, val))
    for a in (-1, 1):
        for b in (-1, 1):
            cands.add((sp.Integer(a), sp.Integer(b)))
    vals = {c: sp.nsimplify(f.subs({x: c[0], y: c[1]})) for c in cands}
    M = max(vals.values())
    arg = {c for c, v in vals.items() if v == M}
    return M, arg, curves


best = None
argset = set()
report = []
for sigma in itertools.product((-1, 1), repeat=len(L)):
    f = sp.expand(sum(sg * Li for sg, Li in zip(sigma, L)))
    M, arg, curves = max_on_square(f)
    report.append((sigma, M, arg, curves))
    if best is None or M > best:
        best = M
best_sigmas = [(sg, M, arg, curves) for sg, M, arg, curves in report if M == best]
problem = []
for sg, M, arg, curves in best_sigmas:
    # A continuum of critical points could hide extra maximizers; examine any such case.
    for kind, data in curves:
        problem.append((sg, kind, str(data)))
    argset |= arg
out = {
    "route": "max over sign vectors of exact quadratics; SymPy monomial-basis solve for cardinals",
    "global_max": str(best),
    "maximizing_sign_vectors": [list(sg) for sg, *_ in best_sigmas],
    "argmax_set": sorted([[str(a), str(b)] for a, b in argset]),
    "degenerate_cases_among_maximizing_sigmas": problem,
    "second_largest_sigma_max": str(sorted({M for _, M, _, _ in report})[-2]),
    "nodes": [[str(X), str(Y), j, k] for X, Y, j, k in nodes],
    "cardinals": [str(Li) for Li in L],
}
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(json.dumps(out, indent=1))
