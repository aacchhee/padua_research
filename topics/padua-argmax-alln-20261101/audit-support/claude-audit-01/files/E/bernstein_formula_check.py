"""Symbolic check of theory17 eq.(2) (power-to-Bernstein weights on [a,b]) and the repo's
bernstein_weights implementation at n=7,12 (exact sympy/Fraction comparison)."""
import sys, json
from fractions import Fraction as F
from math import comb
import sympy as sp
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/user/padua_research/topics/padua-argmax-alln-20261101/code/gated')
import d3_edge_common as c
z, a, w = sp.symbols('z a w')
out = {}
for n in (7, 12):
    ok = True
    for i in range(n + 1):
        expr = sum(sum(sp.binomial(i, h) * a ** (i - h) * w ** h * sp.Rational(comb(r, h), comb(n, h))
                       for h in range(min(i, r) + 1)) * sp.binomial(n, r) * z ** r * (1 - z) ** (n - r)
                   for r in range(n + 1))
        if sp.expand(expr - (a + w * z) ** i) != 0:
            ok = False
    out[f'eq2_symbolic_identity_n{n}'] = ok
    # implementation equals eq.(2) at an actual source interval (n,k)
    k = 5 if n == 12 else 2
    lo, hi = c.source_interval(n, k)
    W = c.bernstein_weights(n, lo, hi)
    A, Wd = F(lo, c.g.S), F(hi - lo, c.g.S)
    same = all(W[r][i] == sum(F(comb(i, h) * comb(r, h), comb(n, h)) * A ** (i - h) * Wd ** h
                              for h in range(min(i, r) + 1)) for r in range(n + 1) for i in range(n + 1))
    out[f'impl_matches_eq2_n{n}_k{k}'] = same
    # source interval contains the exact cell image (float sanity) and lo<hi
    import math
    m = n + 1
    out[f'source_interval_n{n}_k{k}'] = [float(A), float(A + Wd), math.cos((k + 1) * math.pi / m), math.cos((k - 1) * math.pi / m)]
print(json.dumps(out, indent=1))
