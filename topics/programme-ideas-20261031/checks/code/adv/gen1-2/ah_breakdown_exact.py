"""Entry point 2 of gen1-draft-2, run exactly over Q (adversarial check gen1-2).

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) - 2026-11-01

Alexander-Hirschowitz breakdown test: generic double points in the plane, Hermite data
(value, d/dx, d/dy) -> Hermite-Vandermonde over Q in graded-lex order; exact rank and the
exact rank profile (= position of the first zero pivot of the Sobolev Gram's LDL^T, i.e. the
breakdown degree of any exact orthogonalisation / IEP in this order).

Cases:
  A  5 double points, degree 4: 15 functionals vs dim Pi_4 = 15. AH exception (n,d,k)=(2,4,5):
     expected rank 14 (kernel = square of the conic through the 5 points).
  B  control: 4 double points + 3 simple points, degree 4: 15 functionals, expected rank 15.
  C  2 double points, degree 2: 6 functionals vs dim Pi_2 = 6; AH exception d=2,k=2: rank 5
     (kernel = square of the line through the two points).
  D  3 double points, degree 3: 9 functionals vs dim Pi_3 = 10: expected rank 9 (no defect).
  E  Padua-type configuration: double points at the 6 Padua points of degree 2 (18 functionals),
     degree 5 (21 monomials): is the Hilbert function expected (rank 18)?
Scope: random rational points with small numerators/denominators, 5 seeds per case.
"""
from fractions import Fraction
import random
import sympy as sp

def glex(deg):
    return [(a, b) for t in range(deg + 1) for a in range(t, -1, -1) for b in [t - a]]

def hv(points, doubles, deg):
    """Hermite-Vandermonde over Q: rows = values at all points, then (d/dx, d/dy) at the first
    `doubles` points; columns = monomials in graded-lex order."""
    idx = glex(deg)
    rows = []
    for (x, y) in points:
        rows.append([x ** a * y ** b for (a, b) in idx])
    for (x, y) in points[:doubles]:
        rows.append([(a * x ** (a - 1) * y ** b if a > 0 else 0) for (a, b) in idx])
        rows.append([(b * x ** a * y ** (b - 1) if b > 0 else 0) for (a, b) in idx])
    return sp.Matrix(rows), idx

def rank_profile(V):
    """Exact column rank profile: list of column indices that are dependent on earlier columns.
    Equivalent to zero pivots of the LDL^T of the Gram V^T V in this column order."""
    dep = []
    basis = sp.zeros(V.rows, 0)
    r = 0
    for j in range(V.cols):
        cand = basis.row_join(V[:, j])
        if cand.rank() > r:
            basis = cand; r += 1
        else:
            dep.append(j)
    return dep

def gram_ldl_pivots(V):
    G = V.T * V
    n = G.rows
    A = sp.Matrix(G)
    piv = []
    for k in range(n):
        d = A[k, k]
        piv.append(d)
        if d == 0:
            # cannot continue a plain LDL^T past a zero pivot; stop here
            break
        for i in range(k + 1, n):
            f = A[i, k] / d
            for j in range(k + 1, n):
                A[i, j] -= f * A[k, j]
    return piv

def rand_pts(k, rng, den=7):
    return [(sp.Rational(rng.randint(-20, 20), rng.randint(1, den)), sp.Rational(rng.randint(-20, 20), rng.randint(1, den))) for _ in range(k)]

def run_case(name, npts, doubles, deg, seeds=range(5), pts_fn=None):
    print(f"Case {name}: {npts} points, {doubles} of them double, degree {deg}, dim Pi_deg = {len(glex(deg))}, functionals = {npts + 2*doubles}")
    for seed in seeds:
        rng = random.Random(seed)
        pts = pts_fn(rng) if pts_fn else rand_pts(npts, rng)
        V, idx = hv(pts, doubles, deg)
        r = V.rank()
        dep = rank_profile(V)
        piv = gram_ldl_pivots(V)
        zero_at = [idx[j] for j in dep]
        first_zero_piv = next((k for k, d in enumerate(piv) if d == 0), None)
        print(f"  seed {seed}: rank = {r} / {min(V.rows, V.cols)}; dependent columns (monomials) = {zero_at}; "
              f"first zero LDL^T pivot of the Sobolev Gram at column {first_zero_piv}"
              + (f" = monomial {idx[first_zero_piv]} (degree {sum(idx[first_zero_piv])})" if first_zero_piv is not None else " (none)"))
        if name == 'A' and r == 14:
            ker = V.nullspace()[0]
            x, y = sp.symbols('x y')
            p = sum(c * x ** a * y ** b for c, (a, b) in zip(ker, idx))
            fac = sp.factor(p)
            print(f"      kernel polynomial factors as: {fac}")

def padua_pts(rng=None):
    # Padua points of degree n=2 on [-1,1]^2 (6 points), rational? Chebyshev-Lobatto nodes cos(k pi/2), cos(k pi/3)
    # cos(pi/3) = 1/2 rational, cos(pi/2) = 0: all 6 Padua points of degree 2 are rational.
    import itertools
    n = 2
    xs = [sp.cos(sp.pi * k / n) for k in range(n + 1)]          # 1, 0, -1
    ys = [sp.cos(sp.pi * k / (n + 1)) for k in range(n + 2)]    # 1, 1/2, -1/2, -1
    pts = []
    for i, xv in enumerate(xs):
        for j, yv in enumerate(ys):
            if (i + j) % 2 == 0:
                pts.append((sp.nsimplify(xv), sp.nsimplify(yv)))
    return pts

if __name__ == "__main__":
    run_case('A', 5, 5, 4)
    run_case('B', 7, 4, 4)
    run_case('C', 2, 2, 2)
    run_case('D', 3, 3, 3)
    pp = padua_pts()
    print("Padua degree-2 points:", pp)
    run_case('E', 6, 6, 5, seeds=[0], pts_fn=lambda rng: pp)
    run_case('E2 (degree 4, Padua double points: 18 functionals vs 15 monomials)', 6, 6, 4, seeds=[0], pts_fn=lambda rng: pp)
