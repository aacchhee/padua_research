#!/usr/bin/env python3
"""Adversarial check M1 (gen4-draft-3 half): graded real symmetric commuting
extensions of Möller size for several weights, n <= 6.

Object.  Sections (H_x, H_y) of a positive measure on Pi_{n-1} (size r = dim Pi_{n-1}).
A graded symmetric extension of size N = r + s is
      A = [[H_x, C_x], [C_x', D_x]],  B = [[H_y, C_y], [C_y', D_y]],
with C_x, C_y supported on the degree-(n-1) rows only (n x s each) and D_x, D_y
symmetric s x s, such that [A, B] = 0.  By Degani-Schiff-Tannor (Numer. Math.
2005, Thms 9-11) this is the same thing as a positive cubature rule of degree
2n-1 with N real nodes (joint eigenvalues; nodes anywhere in R^2) and weights
= squared first components of the joint eigenvectors (positivity automatic).
Möller size: s = rank[H_x, H_y] / 2 (DST Thm 2 / Thm 12 = Möller's bound).

For each weight and n we report: rank of the commutator, Möller bound,
least-squares residual of [A,B] = 0 over random starts (Levenberg-Marquardt),
and for converged solutions the nodes inside/outside the support, min weight,
and the local dimension of the solution set (Jacobian nullity minus the O(s)
gauge dimension s(s-1)/2).

Weights (all discretised by product rules exact well beyond degree 2n+2):
  cheb     product Chebyshev (first kind) on the square
  legendre constant weight on the square
  disk     constant weight on the unit disk
  triangle constant weight on the standard triangle
  jacobi   (1-x)^0.5 (1+x)^0 (1-y)^0 (1+y)^1.5 on the square (non-symmetric)

Known facts to compare with (LITERATURE): Chebyshev and Legendre attain Möller
for all tested n (Morrow-Patterson 1978, Möller 1976 degree 9 = 17 nodes,
Cools-Haegemans 1988 / Cools-Schmid 1989); DST 2005 Sec. 6.1: the degree-5
7-point (Radon) rules on square and disk form one-parameter families; the disk
at degree 9 has NO rule attaining Möller's bound (Hirao-Sawa SINUM 2009 as
reported; Verlinden-Cools 1992; Cools-Schmid 1993).

Scope: n = 2..6, 12 random starts per case, scipy least_squares.  Seconds.
"""
import numpy as np
from scipy.optimize import least_squares

rng = np.random.default_rng(1)


def graded_monomials(deg):
    return [(a - b, b) for a in range(deg + 1) for b in range(a + 1)]


def dimP(k):
    return (k + 1) * (k + 2) // 2


def gauss_legendre(m):
    return np.polynomial.legendre.leggauss(m)


def gauss_jacobi(m, alpha, beta):
    # Golub-Welsch for Jacobi weight (1-t)^alpha (1+t)^beta on [-1,1]
    from scipy.special import roots_jacobi
    return roots_jacobi(m, alpha, beta)


def discretise(weight, deg):
    """Return nodes x, y and weights w of a positive discrete measure whose
    moments agree with the continuous weight up to total degree >= deg."""
    m = deg + 2
    if weight == 'cheb':
        t = np.cos((2 * np.arange(1, m + 1) - 1) * np.pi / (2 * m)); wt = np.full(m, np.pi / m)
        X, Y = np.meshgrid(t, t); W = np.outer(wt, wt)
    elif weight == 'legendre':
        t, wt = gauss_legendre(m)
        X, Y = np.meshgrid(t, t); W = np.outer(wt, wt)
    elif weight == 'jacobi':
        tx, wx = gauss_jacobi(m, 0.5, 0.0); ty, wy = gauss_jacobi(m, 0.0, 1.5)
        X, Y = np.meshgrid(tx, ty, indexing='ij'); W = np.outer(wx, wy)
    elif weight == 'disk':
        # polar: r in (0,1) with weight r dr (Gauss-Jacobi on [-1,1] mapped), theta equispaced
        tr, wr = gauss_jacobi(m, 0.0, 1.0)            # weight (1+u) on [-1,1]; r = (1+u)/2
        r = (1 + tr) / 2; wr = wr / 4                  # r dr = ((1+u)/2) du/2
        nth = 2 * deg + 4
        th = 2 * np.pi * np.arange(nth) / nth; wth = np.full(nth, 2 * np.pi / nth)
        R, TH = np.meshgrid(r, th, indexing='ij'); W = np.outer(wr, wth)
        X, Y = R * np.cos(TH), R * np.sin(TH)
    elif weight == 'triangle':
        # Duffy map of a tensor Gauss rule onto {x,y >= 0, x + y <= 1}
        tu, wu = gauss_jacobi(m, 1.0, 0.0); tv, wv = gauss_legendre(m)
        u = (1 + tu) / 2; v = (1 + tv) / 2; wu = wu / 4; wv = wv / 2   # (1-u) du factor from Jacobi(1,0)
        U, V = np.meshgrid(u, v, indexing='ij'); W = np.outer(wu, wv)
        X, Y = U, (1 - U) * V
    else:
        raise ValueError(weight)
    return X.ravel(), Y.ravel(), W.ravel() / W.sum()


def sections(x, y, w, deg):
    mons = graded_monomials(deg)
    V = np.array([[xi ** i * yi ** j for (i, j) in mons] for xi, yi in zip(x, y)])
    Q, R = np.linalg.qr(np.sqrt(w)[:, None] * V)
    Q = Q * np.sign(np.diag(R))
    return Q.T @ (x[:, None] * Q), Q.T @ (y[:, None] * Q)


def unpack(p, n, s):
    k = 0
    Cx = p[k:k + n * s].reshape(n, s); k += n * s
    Cy = p[k:k + n * s].reshape(n, s); k += n * s
    iu = np.triu_indices(s)
    Dx = np.zeros((s, s)); Dx[iu] = p[k:k + len(iu[0])]; Dx = Dx + Dx.T - np.diag(np.diag(Dx)); k += len(iu[0])
    Dy = np.zeros((s, s)); Dy[iu] = p[k:k + len(iu[0])]; Dy = Dy + Dy.T - np.diag(np.diag(Dy)); k += len(iu[0])
    return Cx, Cy, Dx, Dy


def build(Hx, Hy, p, n, s):
    r = Hx.shape[0]
    Cx, Cy, Dx, Dy = unpack(p, n, s)
    A = np.zeros((r + s, r + s)); B = np.zeros((r + s, r + s))
    A[:r, :r] = Hx; B[:r, :r] = Hy
    A[r - n:r, r:] = Cx; A[r:, r - n:r] = Cx.T; A[r:, r:] = Dx
    B[r - n:r, r:] = Cy; B[r:, r - n:r] = Cy.T; B[r:, r:] = Dy
    return A, B


def residual(p, Hx, Hy, n, s):
    A, B = build(Hx, Hy, p, n, s)
    Cm = A @ B - B @ A
    return Cm[np.triu_indices(A.shape[0], 1)]


def joint_spectrum(A, B):
    # commuting symmetric pair: diagonalise a generic combination
    t = 0.6180339887
    vals, U = np.linalg.eigh(t * A + (1 - t) * B)
    xs = np.einsum('ij,ij->j', U, A @ U); ys = np.einsum('ij,ij->j', U, B @ U)
    wts = U[0, :] ** 2
    return xs, ys, wts, U


def inside(weight, xs, ys, tol=1e-9):
    if weight in ('cheb', 'legendre', 'jacobi'):
        return np.all(np.abs(xs) <= 1 + tol) and np.all(np.abs(ys) <= 1 + tol)
    if weight == 'disk':
        return np.all(xs ** 2 + ys ** 2 <= 1 + tol)
    if weight == 'triangle':
        return np.all(xs >= -tol) and np.all(ys >= -tol) and np.all(xs + ys <= 1 + tol)


def main():
    print("# M1 adversarial script: graded symmetric commuting extensions of Möller size")
    print("# columns: weight n | dimPi_{n-1} rank[Hx,Hy] Möller N | starts converged (res<1e-10) / 12 | best residual | "
          "for converged: #nodes inside support / N, min weight, local dim (mod O(s) gauge) [set of values]")
    for weight in ('cheb', 'legendre', 'disk', 'triangle', 'jacobi'):
        for n in range(2, 7):
            r = dimP(n - 1)
            x, y, w = discretise(weight, 2 * n + 4)
            Hxf, Hyf = sections(x, y, w, n + 1)
            Hx, Hy = Hxf[:r, :r], Hyf[:r, :r]
            Cm = Hx @ Hy - Hy @ Hx
            sv = np.linalg.svd(Cm, compute_uv=False)
            rank = int(np.sum(sv > 1e-9 * max(1.0, sv[0])))
            s = rank // 2
            N = r + s
            npar = 2 * n * s + s * (s + 1)
            conv = 0; best = np.inf; infos = []
            for start in range(12):
                p0 = rng.normal(size=npar) * 0.5
                sol = least_squares(residual, p0, args=(Hx, Hy, n, s), method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=20000)
                res = np.linalg.norm(sol.fun)
                best = min(best, res)
                if res < 1e-10:
                    conv += 1
                    A, B = build(Hx, Hy, sol.x, n, s)
                    xs, ys, wts, U = joint_spectrum(A, B)
                    # local dimension: nullity of the Jacobian at the solution minus gauge
                    J = sol.jac
                    svj = np.linalg.svd(J, compute_uv=False)
                    nullity = npar - int(np.sum(svj > 1e-7 * max(1.0, svj[0])))
                    gauge = s * (s - 1) // 2
                    infos.append((int(np.sum([inside(weight, np.array([a]), np.array([b])) for a, b in zip(xs, ys)])), wts.min(), nullity - gauge))
            if infos:
                ins = sorted(set(i[0] for i in infos)); mw = min(i[1] for i in infos); dims = sorted(set(i[2] for i in infos))
                extra = "inside %s / %d, min weight %.2e, local dim %s" % (ins, N, mw, dims)
            else:
                extra = "no converged solution (best residual %.1e)" % best
            print("%-8s n=%d | r=%2d rank=%2d Möller N=%2d | %2d/12 | best res %.1e | %s" % (weight, n, r, rank, N, conv, best, extra))


if __name__ == "__main__":
    main()
