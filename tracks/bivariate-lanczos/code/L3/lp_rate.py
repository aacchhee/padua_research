"""MEASURED: smallest support radius delta for which the perturbed functional
L' = L_mu - eps * ev_{z*} on Pi_{2n+1} has a positive representing measure on a
discretised K_delta (union of balls around the Padua nodes).

mu = Padua points of degree n with Padua cubature weights.  z* = node_0 + r*
(r* = 0.03 * (cos 1, sin 1)), so the perturbation removes a tiny mass near a
node.  By the truncated Favard theorem (theory file 301) representability of L'
on K_delta is equivalent to the degree-n sections Phi(L') being exact sections
of a positive measure on K_delta.

Discretisation: each closed ball B(z_i, delta) is replaced by the points
z_i + rho*(cos th, sin th) with rho in {0, delta/R, ..., delta} (R radii) and
nth angles; restricted to the ball, so FEASIBLE on the grid => representable
(inner approximation, up to LP tolerance); INFEASIBLE on the grid does not
prove non-representability (the proof for n = 3 is the certificate p*).
LP: find lambda >= 0 with sum_j lambda_j b_k(xi_j) = L'(b_k), b_k Chebyshev
tensor basis of Pi_{2n+1}.  Solver: scipy.optimize.linprog (HiGHS).
delta_min(eps) by bisection on [0, 0.5].

Usage: python3 lp_rate.py n [R nth]
"""
import sys
import numpy as np
from scipy.optimize import linprog
from l3lib import padua, padua_weights, jet_rows


def basis_vals(pts, d):
    return np.array([jet_rows(z, d, 0)[0] for z in pts]).T  # D x npts


def feasible(nodes, Lp, d, delta, R, nth):
    pts = []
    for z in nodes:
        pts.append(z)
        if delta > 0:
            for rho in np.linspace(delta / R, delta, R):
                for th in np.linspace(0, 2 * np.pi, nth, endpoint=False):
                    pts.append(z + rho * np.array([np.cos(th + 0.37 * rho / delta), np.sin(th + 0.37 * rho / delta)]))
    pts = np.array(pts)
    A = basis_vals(pts, d)
    res = linprog(np.zeros(A.shape[1]), A_eq=A, b_eq=Lp, bounds=(0, None), method='highs',
                  options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10))
    return res.status == 0


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    R = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    nth = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    d = 2 * n + 1
    nodes = padua(n); w = padua_weights(n)
    zstar = nodes[0] + 0.03 * np.array([np.cos(1.0), np.sin(1.0)])
    Lmu = basis_vals(nodes, d) @ w
    ev = basis_vals([zstar], d)[:, 0]
    print(f"Padua n={n} D={len(Lmu)} grid R={R} nth={nth}; z*={zstar}")
    for eps in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        Lp = Lmu - eps * ev
        lo, hi = 0.0, 0.5
        if not feasible(nodes, Lp, d, hi, R, nth):
            print(f"  eps={eps:.0e}: infeasible even at delta={hi}")
            continue
        if feasible(nodes, Lp, d, 0.0, R, nth):
            print(f"  eps={eps:.0e}: feasible at delta=0")
            continue
        for _ in range(30):
            mid = 0.5 * (lo + hi)
            if feasible(nodes, Lp, d, mid, R, nth):
                hi = mid
            else:
                lo = mid
        print(f"  eps={eps:.0e}: delta_min ~ {hi:.4e}  delta_min/sqrt(eps) = {hi/np.sqrt(eps):.3f}  delta_min/eps = {hi/eps:.3g}")


if __name__ == '__main__':
    main()
