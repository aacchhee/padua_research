"""MEASURED: smallest support radius delta for which the perturbed functional
L' = L_mu - eps * ev_{z*} on Pi_{2n+1} has a positive representing measure on a
discretised K_delta (union of closed balls of radius delta around the nodes).

mu = Padua points of degree n with Padua cubature weights; z* = node_0 + r*(cos 1, sin 1)
(default r = 0.03: removal of a tiny mass near a node).  By the truncated
Favard theorem (theory file 301), representability of L' on K_delta is
equivalent to the degree-n sections Phi(L') being exact sections of a positive
measure on K_delta.

Discretisation: each ball is replaced by z_i + rho*(cos th, sin th), rho in
{0, delta/R, ..., delta}, nth (rotated) angles; FEASIBLE on the grid =>
representable (inner approximation) up to LP tolerance; INFEASIBLE on the grid
does not prove non-representability (for Padua n = 3 the proof is the
certificate p*, exact_certificates.py).
Reliability check: S1-component residual. For a numerical basis c_k of S_1
(coefficient vectors), report rel = max_k |c_k.(A lam - L')| / max_k |c_k.E|.
A 'feasible' verdict with rel > 0.1 is flagged UNRELIABLE (the LP tolerance is
then comparable to the part of E that forces delta ~ sqrt(eps)).

Usage: python3 lp_rate.py n mode [r] [R] [nth]
  mode = bisect : delta_min(eps) by bisection on [0, 0.5], eps = 1e-2..1e-6
  mode = scan   : feasibility at delta in a fixed list, eps in {1e-3, 1e-6}
"""
import sys
import numpy as np
from scipy.optimize import linprog
from l3lib import padua, padua_weights, jet_rows, jet_matrix, nullspace


def basis_vals(pts, d):
    return np.array([jet_rows(z, d, 0)[0] for z in pts]).T  # D x npts


def grid(nodes, delta, R, nth):
    pts = []
    for z in nodes:
        pts.append(z)
        if delta > 0:
            for rho in np.linspace(delta / R, delta, R):
                for th in np.linspace(0, 2 * np.pi, nth, endpoint=False):
                    a = th + 0.37 * rho / delta
                    pts.append(z + rho * np.array([np.cos(a), np.sin(a)]))
    return np.array(pts)


def solve(nodes, Lp, d, delta, R, nth):
    A = basis_vals(grid(nodes, delta, R, nth), d)
    res = linprog(np.zeros(A.shape[1]), A_eq=A, b_eq=Lp, bounds=(0, None), method='highs',
                  options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10,
                               time_limit=120.0))
    if res.status == 0:
        return True, A @ res.x - Lp
    return False, None


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    mode = sys.argv[2] if len(sys.argv) > 2 else 'bisect'
    r = float(sys.argv[3]) if len(sys.argv) > 3 else 0.03
    R = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    nth = int(sys.argv[5]) if len(sys.argv) > 5 else 24
    d = 2 * n + 1
    nodes = padua(n); w = padua_weights(n)
    zstar = nodes[0] + r * np.array([np.cos(1.0), np.sin(1.0)])
    Lmu = basis_vals(nodes, d) @ w
    ev = basis_vals([zstar], d)[:, 0]
    S, _ = nullspace(jet_matrix(nodes, d, 1), rtol=1e-11)
    print(f"Padua n={n} D={len(Lmu)} dimS1={S.shape[1]} grid R={R} nth={nth}; z*={zstar} (r={r}); mode={mode}")

    def rel(resid, eps):
        if S.shape[1] == 0:
            return 0.0
        num = np.max(np.abs(S.T @ resid))
        den = np.max(np.abs(S.T @ (eps * ev)))
        return num / den

    if mode == 'resid':
        # min l1 moment residual over positive measures on a NESTED grid of K_delta
        # (radii 0 and 12 geometric radii delta*10^(-3..0), 24 rotated angles);
        # always feasible LP. Lower bound from the certificate p* (theory file 303)
        # when p* >= 0 on K_delta: resid >= eps * p*(z*) / ||c*||_inf.
        from inspect_certificate import certificate
        cstar = None
        if S.shape[1] > 0:
            cs, lam = certificate(nodes, n)
            if lam > 0:
                cstar = cs / np.max(np.abs(cs))
        for eps in [1e-3, 1e-5]:
            Lp = Lmu - eps * ev
            for delta in [0.0, 1e-3, 3e-3, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.2]:
                pts = [z for z in nodes]
                if delta > 0:
                    for z in nodes:
                        for rho in delta * np.logspace(-3, 0, 12):
                            for th in np.linspace(0, 2 * np.pi, 24, endpoint=False):
                                a = th + 0.37 * np.log10(rho / delta)
                                pts.append(z + rho * np.array([np.cos(a), np.sin(a)]))
                A = basis_vals(np.array(pts), d)
                Dd, m = A.shape
                c = np.r_[np.zeros(m), np.ones(2 * Dd)]
                Aeq = np.c_[A, np.eye(Dd), -np.eye(Dd)]
                res = linprog(c, A_eq=Aeq, b_eq=Lp, bounds=(0, None), method='highs',
                              options=dict(time_limit=300.0))
                lb = ''
                if cstar is not None:
                    pz = float(basis_vals([zstar], d)[:, 0] @ cstar)
                    lb = f"  cert LB (valid if delta<=delta0) = {eps * pz / 1.0:.3e}"
                if res.fun is None:
                    print(f"  eps={eps:.0e} delta={delta:<6}: status={res.status} ({res.message[:60]}) -- no value", flush=True)
                    continue
                print(f"  eps={eps:.0e} delta={delta:<6}: status={res.status} min l1 resid = {res.fun:.3e}"
                      f"  resid/eps = {res.fun/eps:.3e}{lb}", flush=True)
        return
    if mode == 'scan':
        for eps in [1e-3, 1e-6]:
            Lp = Lmu - eps * ev
            for delta in [0.0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.5]:
                ok, resid = solve(nodes, Lp, d, delta, R, nth)
                tag = f"feasible (S1-rel resid {rel(resid, eps):.1e})" if ok else "infeasible"
                print(f"  eps={eps:.0e} delta={delta:<5}: {tag}", flush=True)
        return
    for eps in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        Lp = Lmu - eps * ev
        lo, hi = 0.0, 0.5
        ok, resid = solve(nodes, Lp, d, hi, R, nth)
        if not ok:
            print(f"  eps={eps:.0e}: infeasible even at delta={hi}", flush=True)
            continue
        last = resid
        for _ in range(30):
            mid = 0.5 * (lo + hi)
            ok, resid = solve(nodes, Lp, d, mid, R, nth)
            if ok:
                hi = mid; last = resid
            else:
                lo = mid
        rr = rel(last, eps)
        flag = "UNRELIABLE" if rr > 0.1 else "ok"
        print(f"  eps={eps:.0e}: delta_min ~ {hi:.4e}  /sqrt(eps) = {hi/np.sqrt(eps):.4f}  /eps = {hi/eps:.3g}"
              f"  S1-rel resid {rr:.1e} [{flag}]", flush=True)


if __name__ == '__main__':
    main()
