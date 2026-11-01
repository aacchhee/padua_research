"""Inspect the numerical robust-failure certificate p* in S_1 (Padua, degree n).

Finds p* = S_1 c maximising the minimal Hessian eigenvalue over nodes (box
normalisation), then reports: Hessian eigenvalues at nodes, min of p* on
circles of radius r around each node (r in a list), estimate of delta_0 =
largest radius with p* >= 0 on all closed balls, and min of p* on [-1,1]^2.
Floating point only: MEASURED.

Usage: python3 inspect_certificate.py n
"""
import sys
import numpy as np
import cvxpy as cp
from numpy.polynomial import chebyshev as C
from l3lib import padua, jet_matrix, nullspace, jet_rows, exps


def evalp(p, d, X, Y):
    E = exps(d)
    out = np.zeros_like(X)
    for coef, (a, b) in zip(p, E):
        ca = np.zeros(a + 1); ca[a] = 1
        cb = np.zeros(b + 1); cb[b] = 1
        out += coef * C.chebval(X, ca) * C.chebval(Y, cb)
    return out


def certificate(nodes, n):
    d = 2 * n + 1
    S, _ = nullspace(jet_matrix(nodes, d, 1), rtol=1e-11)
    Hm = [jet_rows(z, d, 2) @ S for z in nodes]
    c = cp.Variable(S.shape[1]); lam = cp.Variable()
    cons = [cp.norm(c, 'inf') <= 1]
    for i in range(len(nodes)):
        hxx, hxy, hyy = Hm[i][0] @ c, Hm[i][1] @ c, Hm[i][2] @ c
        Hi = cp.bmat([[hxx, hxy], [hxy, hyy]])
        cons.append(0.5 * (Hi + Hi.T) - lam * np.eye(2) >> 0)
    cp.Problem(cp.Maximize(lam), cons).solve(solver=cp.CLARABEL)
    return S @ c.value, lam.value


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    nodes = padua(n); d = 2 * n + 1
    p, lam = certificate(nodes, n)
    p = p / np.max(np.abs(p))
    print(f"Padua n={n}: lambda_P={lam:.4g}; p normalised to max|coef|=1")
    eigs = []
    for z in nodes:
        R = jet_rows(z, d, 2) @ p
        Hz = np.array([[R[0], R[1]], [R[1], R[2]]])
        eigs.append(np.linalg.eigvalsh(Hz))
        print(f"  node ({z[0]:+.4f},{z[1]:+.4f}): val={jet_rows(z,d,0)@p} grad={jet_rows(z,d,1)@p} Hess eig={np.linalg.eigvalsh(Hz)}")
    th = np.linspace(0, 2 * np.pi, 721)
    for r in [1e-3, 1e-2, 3e-2, 0.05, 0.1, 0.15, 0.2, 0.3]:
        worst = np.inf
        for z in nodes:
            for rr in np.linspace(r / 20, r, 20):
                v = evalp(p, d, z[0] + rr * np.cos(th), z[1] + rr * np.sin(th)).min()
                worst = min(worst, v)
        print(f"  min p* over balls radius {r}: {worst:.3e}")
    g = np.linspace(-1, 1, 801)
    XX, YY = np.meshgrid(g, g)
    V = evalp(p, d, XX, YY)
    i = np.unravel_index(np.argmin(V), V.shape)
    print(f"  min p* on [-1,1]^2 grid 801^2: {V.min():.3e} at ({XX[i]:.3f},{YY[i]:.3f}); max {V.max():.3e}")


if __name__ == '__main__':
    main()
