"""Probe: on a convex pentagon (not a Koornwinder domain) with Lebesgue measure, compute
graded discrete orthonormal polynomials from an exact-enough triangle quadrature mesh and
check whether the operators  p -> pi * d_x p  and  p -> pi * d_y p  (pi = product of the 5
edge lines, vanishing on the boundary) are block-banded in total degree with bandwidth
b-1 = 4, as the integration-by-parts argument predicts for ANY algebraic domain.
Also report the degree-bandwidth of plain d_x (expected: full lower triangle) and the
conditioning of the resulting block-banded first-order system.  numpy only, seconds.
"""
import numpy as np

# convex pentagon vertices (irregular)
V = np.array([[-0.9, -0.7], [0.8, -0.9], [1.0, 0.3], [0.1, 0.95], [-0.95, 0.4]])

def tri_quad(a, b, c, g=12):
    """tensor Gauss-Legendre on a triangle via Duffy map; exact for degree ~2g-2 in the collapsed coords"""
    x, w = np.polynomial.legendre.leggauss(g)
    u = (x+1)/2; wu = w/2
    U, Vv = np.meshgrid(u, u, indexing="ij"); WU, WV = np.meshgrid(wu, wu, indexing="ij")
    s = U.ravel(); t = (Vv*(1-U)).ravel(); wt = (WU*WV*(1-U)).ravel()
    P = a[None, :]*(1-s-t)[:, None] + b[None, :]*s[:, None] + c[None, :]*t[:, None]
    area2 = abs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1]))
    return P, wt*area2

cen = V.mean(axis=0)
pts, wts = [], []
for i in range(5):
    P, w = tri_quad(cen, V[i], V[(i+1) % 5]); pts.append(P); wts.append(w)
X = np.vstack(pts); W = np.concatenate(wts)
print("mesh points:", len(X), " total weight (area):", W.sum())

def edge_lines(x, y):
    pi = np.ones_like(x)
    for i in range(5):
        a, b = V[i], V[(i+1) % 5]
        pi = pi * ((b[0]-a[0])*(y-a[1]) - (b[1]-a[1])*(x-a[0]))
    return pi
pi_val = edge_lines(X[:, 0], X[:, 1])
# derivatives of pi by finite differences would be sloppy; use exact product rule
def edge_lines_grad(x, y):
    L = []; gx = []; gy = []
    for i in range(5):
        a, b = V[i], V[(i+1) % 5]
        L.append((b[0]-a[0])*(y-a[1]) - (b[1]-a[1])*(x-a[0])); gx.append(-(b[1]-a[1])*np.ones_like(x)); gy.append((b[0]-a[0])*np.ones_like(x))
    L = np.array(L); dx = np.zeros_like(x); dy = np.zeros_like(x)
    for i in range(5):
        others = np.prod(np.delete(L, i, axis=0), axis=0)
        dx += gx[i]*others; dy += gy[i]*others
    return dx, dy

n = 10
Tx = np.polynomial.chebyshev.chebvander(X[:, 0], n); Ty = np.polynomial.chebyshev.chebvander(X[:, 1], n)
dTx = np.polynomial.chebyshev.chebvander(X[:, 0], n) @ np.array([np.polynomial.chebyshev.chebder(np.eye(n+1)[k], 1).tolist()+[0.0] for k in range(n+1)]).T
dTy = np.polynomial.chebyshev.chebvander(X[:, 1], n) @ np.array([np.polynomial.chebyshev.chebder(np.eye(n+1)[k], 1).tolist()+[0.0] for k in range(n+1)]).T
idx = [(d-j, j) for d in range(n+1) for j in range(d+1)]
deg = np.array([i+j for i, j in idx])
B = np.column_stack([Tx[:, i]*Ty[:, j] for i, j in idx])
Bx = np.column_stack([dTx[:, i]*Ty[:, j] for i, j in idx])
By = np.column_stack([Tx[:, i]*dTy[:, j] for i, j in idx])
sw = np.sqrt(W)[:, None]
Q, R = np.linalg.qr(sw*B); Q2, R2 = np.linalg.qr(Q); Q = Q2; R = R2 @ R
Rinv = np.linalg.inv(R)
# derivative of the orthonormal basis: d_x (B R^-1) = Bx R^-1
QX = (sw*Bx) @ Rinv; QY = (sw*By) @ Rinv
print("orthonormality:", np.linalg.norm(Q.T@Q - np.eye(Q.shape[1])))

def deg_bandwidth(Mat, tol=1e-9):
    r, c = np.nonzero(np.abs(Mat) > tol*np.abs(Mat).max())
    lo = int(np.max(deg[r]-deg[c])); hi = int(np.max(deg[c]-deg[r]))
    return lo, hi

Dx_plain = Q.T @ QX
Dx_pi = Q.T @ (pi_val[:, None]*QX)
Dy_pi = Q.T @ (pi_val[:, None]*QY)
Hx = Q.T @ (X[:, 0][:, None]*Q)
print("plain d_x: degree band (below, above) =", deg_bandwidth(Dx_plain))
print("pi*d_x   : degree band (below, above) =", deg_bandwidth(Dx_pi), " expected (4, 4)")
print("pi*d_y   : degree band (below, above) =", deg_bandwidth(Dy_pi), " expected (4, 4)")
print("H_x      : degree band =", deg_bandwidth(Hx), " expected (1, 1)")
# second-order: operator p -> pi * Laplacian(p) is NOT banded below (pi vanishes to order 1 only);
# p -> pi^2 Laplacian p is banded with bandwidth 2b-2 = 8 (two integrations by parts)
lapQ = None
# second derivatives of basis
d2Tx = np.polynomial.chebyshev.chebvander(X[:, 0], n) @ np.array([np.polynomial.chebyshev.chebder(np.eye(n+1)[k], 2).tolist()+[0.0, 0.0] for k in range(n+1)]).T
d2Ty = np.polynomial.chebyshev.chebvander(X[:, 1], n) @ np.array([np.polynomial.chebyshev.chebder(np.eye(n+1)[k], 2).tolist()+[0.0, 0.0] for k in range(n+1)]).T
Bxx = np.column_stack([d2Tx[:, i]*Ty[:, j] for i, j in idx]); Byy = np.column_stack([Tx[:, i]*d2Ty[:, j] for i, j in idx])
LQ = (sw*(Bxx+Byy)) @ Rinv
L_pi2 = Q.T @ ((pi_val**2)[:, None]*LQ)
L_pi = Q.T @ (pi_val[:, None]*LQ)
print("pi*Lap   : degree band =", deg_bandwidth(L_pi))
print("pi^2*Lap : degree band =", deg_bandwidth(L_pi2), " expected (8, 8)")
# conditioning of the leading N_n x N_n block of pi^2*Lap restricted to degrees <= n-?  (Dirichlet via pi-weighted trial space is the real method; here only a structure probe)
Nn = len(idx)
s = np.linalg.svd(L_pi2, compute_uv=False)
print("pi^2*Lap full block: sigma_max/sigma_min = %.2e (dim %d); numerical rank = %d" % (s[0]/s[-1], Nn, int(np.sum(s > 1e-10*s[0]))))
