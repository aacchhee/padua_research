"""Developer check for PD-N?programme-ideas-claude-03 (response-02, 2026-11-01).

Exact (SymPy) verification that a joint Ritz residual can vanish at a non-saturated node:
equal weights on the grid {-1,-1/2,0,1/2,1}^2, total degree k = 2, node B = (0,0).
Computes s_k(B) = w_B K_k(B,B) and the two compressed residuals P X P e_B, P Y P e_B
(P = V (V^T W V)^{-1} V^T W, the W-orthogonal projector onto evaluated Pi_k), in exact rationals.
Also checks k = 4 on the same grid and k = 2 on a 7x7 grid (parity mechanism, even k).
"""
import json
import sympy as sp

def check(grid, k):
    pts = [(a, b) for a in grid for b in grid]
    M = len(pts)
    w = [sp.Rational(1, M)] * M
    mons = [(a, d - a) for d in range(k + 1) for a in range(d, -1, -1)]
    V = sp.Matrix([[x ** a * y ** b for (a, b) in mons] for (x, y) in pts])
    W = sp.diag(*w)
    G = V.T * W * V
    Ginv = G.inv()
    iB = pts.index((0, 0))
    vB = V[iB, :].T
    K_BB = (vB.T * Ginv * vB)[0]
    s = w[iB] * K_BB
    # kernel function values K(z_i, B) at all nodes
    Kcol = V * Ginv * vB
    X = sp.diag(*[p[0] for p in pts]); Y = sp.diag(*[p[1] for p in pts])
    P = V * Ginv * V.T * W
    rx = P * X * Kcol
    ry = P * Y * Kcol
    return {"grid": [str(g) for g in grid], "k": k, "dim_Pi_k": len(mons), "s_k(B)": str(sp.nsimplify(s)),
            "deficit": str(sp.nsimplify(1 - s)),
            "residual_x_is_zero": all(sp.simplify(v) == 0 for v in rx),
            "residual_y_is_zero": all(sp.simplify(v) == 0 for v in ry)}

h = sp.Rational(1, 2); t = sp.Rational(1, 3)
out = [check([-1, -h, 0, h, 1], 2), check([-1, -h, 0, h, 1], 4),
       check([-1, -2 * t, -t, 0, t, 2 * t, 1], 2)]
print(json.dumps(out, indent=1))
