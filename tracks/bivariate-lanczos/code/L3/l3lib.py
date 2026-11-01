"""L3 helper library (direction L3, topic bivariate-lanczos-20261031).

Conventions (match plan.md and HL BIT Thm 2.1): graded order on Pi_d, degree k
first, then x-exponent ascending within degree: index l(k,s) = k(k+1)/2 + s
<-> monomial x^s y^(k-s).

Node sets:
  padua(n): {(cos(j pi/n), cos(k pi/(n+1))): 0<=j<=n, 0<=k<=n+1, j+k even}
            (one of the four Padua families; N_n = (n+1)(n+2)/2 points).

Numerics use the tensor Chebyshev basis T_a(x) T_b(y), a+b <= d, for
conditioning; everything here is floating point (MEASURED) unless a function
name says exact.
"""
import numpy as np
from numpy.polynomial import chebyshev as C


def exps(d):
    """Graded exponent list (a, b) meaning x^a y^b, a+b <= d; x-exponent ascending."""
    out = []
    for k in range(d + 1):
        for s in range(k + 1):
            out.append((s, k - s))
    return out


def dimPi(d):
    return (d + 1) * (d + 2) // 2


def padua(n):
    pts = []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                pts.append((np.cos(j * np.pi / n) if n > 0 else 1.0, np.cos(k * np.pi / (n + 1))))
    return np.array(pts)


def padua_weights(n):
    """Padua cubature weights for the normalised product Chebyshev measure
    (vertex 1/2, edge 1, interior 2, times 1/(n(n+1))). Positive; only constants
    in L3 depend on them."""
    P = padua(n)
    w = []
    for (x, y) in P:
        onx = abs(abs(x) - 1) < 1e-12
        ony = abs(abs(y) - 1) < 1e-12
        if onx and ony:
            w.append(0.5)
        elif onx or ony:
            w.append(1.0)
        else:
            w.append(2.0)
    w = np.array(w) / (n * (n + 1))
    return w


def _cheb_vals(t, a, der=0):
    c = np.zeros(a + 1)
    c[a] = 1.0
    if der:
        c = C.chebder(c, der)
    return C.chebval(t, c)


def jet_rows(z, d, order):
    """Rows of derivatives of the Chebyshev tensor basis of Pi_d at point z.
    order=0: value; order=1: d/dx, d/dy; order=2: dxx, dxy, dyy."""
    x, y = z
    E = exps(d)
    if order == 0:
        ders = [(0, 0)]
    elif order == 1:
        ders = [(1, 0), (0, 1)]
    else:
        ders = [(2, 0), (1, 1), (0, 2)]
    rows = []
    for (dx, dy) in ders:
        rows.append([_cheb_vals(x, a, dx) * _cheb_vals(y, b, dy) for (a, b) in E])
    return np.array(rows)


def jet_matrix(nodes, d, max_order=1):
    blocks = []
    for z in nodes:
        for o in range(max_order + 1):
            blocks.append(jet_rows(z, d, o))
    return np.vstack(blocks)


def nullspace(A, rtol=1e-10):
    U, s, Vt = np.linalg.svd(A)
    tol = rtol * (s[0] if s.size else 1.0)
    r = int((s > tol).sum())
    return Vt[r:].T, s


def hess_of(p, nodes, d):
    """List of 2x2 Hessians of the polynomial with Chebyshev-tensor coefficient vector p."""
    H = []
    for z in nodes:
        R = jet_rows(z, d, 2) @ p
        H.append(np.array([[R[0], R[1]], [R[1], R[2]]]))
    return H
