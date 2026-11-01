"""Adversarial probe for gen3-draft-3 (boundary-polynomial calculus on algebraic domains).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) - adversarial check gen3-3 - 2026-11-01

What it measures (numpy only, seconds; n <= 8 for structure, n <= 16 for conditioning trends):
  A. Degree-bandwidth of pi*d_x, pi*d_y, pi^2*Lap in the numerically generated graded orthonormal basis of
     (Omega, w) for several algebraic domains / weights, against the semiclassical structure relation
     (Alvarez de Morales-Fernandez-Perez-Pinar, JCAM 214 (2008) Thm 3.1: band j in [n-s-1, n+p-1],
     p = deg Phi = b, s = max(p-2, q-1) = b-2 for Phi = pi*I, Psi = (alpha+1) grad pi  =>  band (b-1, b-1)).
  B. Intra-block density of pi*d_x (are the degree blocks dense?), nnz of H_x and of pi*d_x versus N
     (sparse-solve / recurrence-evaluation cost), with the square (tensor-Legendre = Koornwinder) as control.
  C. Dirichlet formulations with trial space pi*Pi_n:
       (PG)  test space Pi_n  (the draft's "Petrov-Galerkin"): M_ij = <Lap(pi p_j), q_i>  -> lower band?
       (G)   test space pi*Pi_n (symmetric Galerkin): S_ij = <grad(pi p_j), grad(pi p_i)>  -> band 2b-2
     condition numbers kappa(S), kappa(M) and kappa after symmetric block-diagonal (degree-block) preconditioning,
     n = 4..16, with least-squares growth exponents.
All statements are MEASURED in the stated finite scope only.
"""
import numpy as np, sys, time

np.set_printoptions(linewidth=150)
TOL = 1e-9

# ---------------------------------------------------------------- quadrature meshes (exact Lebesgue measure)
def tri_quad(a, b, c, g):
    x, w = np.polynomial.legendre.leggauss(g)
    u = (x + 1) / 2; wu = w / 2
    U, Vv = np.meshgrid(u, u, indexing="ij"); WU, WV = np.meshgrid(wu, wu, indexing="ij")
    s = U.ravel(); t = (Vv * (1 - U)).ravel(); wt = (WU * WV * (1 - U)).ravel()
    P = a[None, :] * (1 - s - t)[:, None] + b[None, :] * s[:, None] + c[None, :] * t[:, None]
    area2 = abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]))
    return P, wt * area2

def polygon_mesh(V, g, fan_from=None):
    """fan triangulation from a given interior point (convex) or explicit triangle list"""
    pts, wts = [], []
    if fan_from is not None:
        cen = fan_from
        for i in range(len(V)):
            P, w = tri_quad(cen, V[i], V[(i + 1) % len(V)], g); pts.append(P); wts.append(w)
    return np.vstack(pts), np.concatenate(wts)

def lshape_mesh(g):
    """non-convex L-shape = [-1,1]^2 minus (0,1)x(0,1); three unit squares, each split in two triangles"""
    squares = [((-1, -1), (0, 0)), ((0, -1), (1, 0)), ((-1, 0), (0, 1))]
    pts, wts = [], []
    for (x0, y0), (x1, y1) in squares:
        a = np.array([x0, y0]); b = np.array([x1, y0]); c = np.array([x1, y1]); d = np.array([x0, y1])
        for tri in [(a, b, c), (a, c, d)]:
            P, w = tri_quad(*tri, g); pts.append(P); wts.append(w)
    return np.vstack(pts), np.concatenate(wts)

def star_domain_mesh(pi_fun, nth=400, nr=16, R0=2.0):
    """star-shaped domain {pi > 0} containing the origin: trapezoid in theta (spectrally accurate for smooth
    boundary), Gauss-Legendre in r on [0, R(theta)] with Jacobian r (exact for polynomial integrands)."""
    th = 2 * np.pi * np.arange(nth) / nth; wth = 2 * np.pi / nth
    xr, wr = np.polynomial.legendre.leggauss(nr)
    pts, wts = [], []
    for t in th:
        c, s = np.cos(t), np.sin(t)
        # radial root of pi(r c, r s) = 0 by bisection from R0 inward
        lo, hi = 0.0, R0
        assert pi_fun(np.array([0.0]), np.array([0.0]))[0] > 0 and pi_fun(np.array([hi * c]), np.array([hi * s]))[0] < 0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if pi_fun(np.array([mid * c]), np.array([mid * s]))[0] > 0: lo = mid
            else: hi = mid
        R = 0.5 * (lo + hi)
        r = (xr + 1) / 2 * R; w = wr / 2 * R * r * wth
        pts.append(np.column_stack([r * c, r * s])); wts.append(w)
    return np.vstack(pts), np.concatenate(wts)

# ---------------------------------------------------------------- boundary polynomials
def poly_lines(V):
    """pi = product of edge lines, positive inside for a convex polygon traversed counter-clockwise"""
    def pi(x, y):
        out = np.ones_like(x)
        for i in range(len(V)):
            a, b = V[i], V[(i + 1) % len(V)]
            out = out * ((b[0] - a[0]) * (y - a[1]) - (b[1] - a[1]) * (x - a[0]))
        return out
    def grad(x, y):
        L, gx, gy = [], [], []
        for i in range(len(V)):
            a, b = V[i], V[(i + 1) % len(V)]
            L.append((b[0] - a[0]) * (y - a[1]) - (b[1] - a[1]) * (x - a[0]))
            gx.append(-(b[1] - a[1]) * np.ones_like(x)); gy.append((b[0] - a[0]) * np.ones_like(x))
        L = np.array(L); dx = np.zeros_like(x); dy = np.zeros_like(x)
        for i in range(len(V)):
            others = np.prod(np.delete(L, i, axis=0), axis=0)
            dx += gx[i] * others; dy += gy[i] * others
        return dx, dy
    def lap(x, y):
        # Laplacian of a product of linear forms: sum over pairs i<j of 2 * (grad l_i . grad l_j) * prod_{k != i,j} l_k
        m = len(V); L, G = [], []
        for i in range(m):
            a, b = V[i], V[(i + 1) % m]
            L.append((b[0] - a[0]) * (y - a[1]) - (b[1] - a[1]) * (x - a[0]))
            G.append(np.array([-(b[1] - a[1]), (b[0] - a[0])]))
        L = np.array(L); out = np.zeros_like(x)
        for i in range(m):
            for j in range(i + 1, m):
                others = np.prod(np.delete(L, [i, j], axis=0), axis=0)
                out += 2 * (G[i] @ G[j]) * others
        return out
    return pi, grad, lap

def poly_quartic():
    """pi = 1 - x^4 - y^4 - 0.3 x^2 y (degree 4, smooth convex-ish curved boundary, origin inside)"""
    pi = lambda x, y: 1 - x**4 - y**4 - 0.3 * x**2 * y
    grad = lambda x, y: (-4 * x**3 - 0.6 * x * y, -4 * y**3 - 0.3 * x**2)
    lap = lambda x, y: -12 * x**2 - 12 * y**2 - 0.6 * y
    return pi, grad, lap

def poly_lshape():
    """L-shape boundary: lines x=+-1, y=+-1, x=0, y=0  -> pi = (1-x^2)(1-y^2) x y, degree 6 (changes sign inside)"""
    pi = lambda x, y: (1 - x**2) * (1 - y**2) * x * y
    grad = lambda x, y: ((1 - 3 * x**2) * (1 - y**2) * y, (1 - x**2) * (1 - 3 * y**2) * x)
    lap = lambda x, y: (-6 * x) * (1 - y**2) * y + (1 - x**2) * (-6 * y) * x
    return pi, grad, lap

def poly_square():
    pi = lambda x, y: (1 - x**2) * (1 - y**2)
    grad = lambda x, y: (-2 * x * (1 - y**2), -2 * y * (1 - x**2))
    lap = lambda x, y: -2 * (1 - y**2) - 2 * (1 - x**2)
    return pi, grad, lap

# ---------------------------------------------------------------- graded orthonormal basis from a discrete measure
def graded_basis(X, W, n):
    cheb = np.polynomial.chebyshev
    Tx = cheb.chebvander(X[:, 0], n); Ty = cheb.chebvander(X[:, 1], n)
    D1 = np.array([cheb.chebder(np.eye(n + 1)[k], 1).tolist() + [0.0] for k in range(n + 1)]).T
    D2 = np.array([cheb.chebder(np.eye(n + 1)[k], 2).tolist() + [0.0, 0.0] for k in range(n + 1)]).T
    dTx, dTy, d2Tx, d2Ty = Tx @ D1, Ty @ D1, Tx @ D2, Ty @ D2
    idx = [(d - j, j) for d in range(n + 1) for j in range(d + 1)]
    deg = np.array([i + j for i, j in idx])
    col = lambda A, B: np.column_stack([A[:, i] * B[:, j] for i, j in idx])
    B = col(Tx, Ty); Bx = col(dTx, Ty); By = col(Tx, dTy); Bxx = col(d2Tx, Ty); Byy = col(Tx, d2Ty); Bxy = col(dTx, dTy)
    sw = np.sqrt(W)[:, None]
    Q, R = np.linalg.qr(sw * B); Q2, R2 = np.linalg.qr(Q); Q = Q2; R = R2 @ R
    Rinv = np.linalg.inv(R)
    orth = np.linalg.norm(Q.T @ Q - np.eye(Q.shape[1]))
    # values of the orthonormal polynomials and their derivatives at the nodes (unweighted)
    P = B @ Rinv; Px = Bx @ Rinv; Py = By @ Rinv; Pxx = Bxx @ Rinv; Pyy = Byy @ Rinv; Pxy = Bxy @ Rinv
    return dict(P=P, Px=Px, Py=Py, Pxx=Pxx, Pyy=Pyy, Pxy=Pxy, deg=deg, idx=idx, orth=orth)

def ip(W, F, G):
    return F.T @ (W[:, None] * G)

def deg_band(Mat, deg, tol=TOL):
    r, c = np.nonzero(np.abs(Mat) > tol * np.abs(Mat).max())
    return int(np.max(deg[r] - deg[c])), int(np.max(deg[c] - deg[r]))

def block_density(Mat, deg, tol=TOL):
    """fraction of nonzero entries inside each (row-degree, col-degree) block that is nonzero at all"""
    out = {}
    mx = np.abs(Mat).max()
    for kr in range(deg.max() + 1):
        for kc in range(deg.max() + 1):
            blk = Mat[np.ix_(deg == kr, deg == kc)]
            nz = np.sum(np.abs(blk) > tol * mx)
            if nz: out[(kr, kc)] = nz / blk.size
    return out

def nnz(Mat, tol=TOL):
    return int(np.sum(np.abs(Mat) > tol * np.abs(Mat).max()))

def block_precond_kappa(S, deg):
    """symmetric block-diagonal (degree-block) preconditioning D^{-1/2} S D^{-1/2}; also plain Jacobi"""
    Dh = np.zeros_like(S)
    for k in range(deg.max() + 1):
        m = deg == k
        blk = S[np.ix_(m, m)]
        w, U = np.linalg.eigh(0.5 * (blk + blk.T))
        Dh[np.ix_(m, m)] = U @ np.diag(1 / np.sqrt(np.abs(w))) @ U.T
    Sp = Dh @ S @ Dh
    return np.linalg.cond(Sp)

def operators(basis, W, pi, grad, lap, alpha=0):
    P, Px, Py, Pxx, Pyy, deg = basis["P"], basis["Px"], basis["Py"], basis["Pxx"], basis["Pyy"], basis["deg"]
    pv = pi; gx, gy = grad; lv = lap
    Dx_pi = ip(W, P, pv[:, None] * Px)
    Dy_pi = ip(W, P, pv[:, None] * Py)
    Dx_plain = ip(W, P, Px)
    L_pi2 = ip(W, P, (pv**2)[:, None] * (Pxx + Pyy))
    # trial u = pi*p: grad u = p grad pi + pi grad p ; Lap u = p Lap pi + 2 grad pi . grad p + pi Lap p
    Ux = P * gx[:, None] + pv[:, None] * Px; Uy = P * gy[:, None] + pv[:, None] * Py
    LapU = P * lv[:, None] + 2 * (gx[:, None] * Px + gy[:, None] * Py) + pv[:, None] * (Pxx + Pyy)
    S = ip(W, Ux, Ux) + ip(W, Uy, Uy)          # symmetric Galerkin, trial = test = pi*Pi_n  (w = Lebesgue only)
    M = ip(W, P, LapU)                           # draft's PG: test Pi_n, trial pi*Pi_n:  M_ij = <q_i, Lap(pi p_j)>
    Mpi = ip(W, pv[:, None] * P, LapU)           # test pi*Pi_n: equals -S by Green (check)
    return dict(Dx_pi=Dx_pi, Dy_pi=Dy_pi, Dx_plain=Dx_plain, L_pi2=L_pi2, S=S, M=M, Mpi=Mpi)

# ---------------------------------------------------------------- A + B: bandwidth and density, n = 8
V5 = np.array([[-0.9, -0.7], [0.8, -0.9], [1.0, 0.3], [0.1, 0.95], [-0.95, 0.4]])   # generator's pentagon
V7 = np.array([[np.cos(2 * np.pi * k / 7 + 0.3) * (1 + 0.15 * (-1) ** k), np.sin(2 * np.pi * k / 7 + 0.3) * (1 - 0.1 * (k % 3))] for k in range(7)])
cases = []
Xp, Wp = polygon_mesh(V5, 20, fan_from=V5.mean(axis=0)); pi5, g5, l5 = poly_lines(V5)
cases.append(("pentagon b=5 Lebesgue", Xp, Wp, pi5, g5, l5, 5, 0))
cases.append(("pentagon b=5 weight pi^1", Xp, Wp, pi5, g5, l5, 5, 1))
cases.append(("pentagon b=5 weight pi^2", Xp, Wp, pi5, g5, l5, 5, 2))
X7, W7 = polygon_mesh(V7, 20, fan_from=np.zeros(2)); pi7, g7, l7 = poly_lines(V7)
cases.append(("heptagon b=7 Lebesgue", X7, W7, pi7, g7, l7, 7, 0))
piq, gq, lq = poly_quartic(); Xq, Wq = star_domain_mesh(piq, nth=480, nr=18)
cases.append(("quartic curved b=4 Lebesgue", Xq, Wq, piq, gq, lq, 4, 0))
cases.append(("quartic curved b=4 weight pi^1", Xq, Wq, piq, gq, lq, 4, 1))
XL, WL = lshape_mesh(20); piL, gL, lL = poly_lshape()
cases.append(("L-shape (non-convex) b=6 Lebesgue", XL, WL, piL, gL, lL, 6, 0))
Xs, Ws = polygon_mesh(np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]], float), 20, fan_from=np.zeros(2)); pis, gs, ls = poly_square()
cases.append(("square b=4 Lebesgue (Koornwinder control)", Xs, Ws, pis, gs, ls, 4, 0))

n = 8
print("=== A/B: degree bandwidths and block density at n = %d ===" % n)
print("%-42s %5s %9s %9s %9s %9s %9s | %8s %8s %8s %6s" % ("case", "b", "orth", "pi*dx", "pi*dy", "pi^2*Lap", "plain dx", "nnzHx", "nnz pidx", "N", "dens"))
for name, X, W0, pi, grad, lap, b, alpha in cases:
    pv = pi(X[:, 0], X[:, 1]); W = W0 * pv**alpha
    assert np.all(W > -1e-14) or alpha % 2 == 0, name
    bs = graded_basis(X, W, n)
    gx, gy = grad(X[:, 0], X[:, 1]); lv = lap(X[:, 0], X[:, 1])
    ops = operators(bs, W, pv, (gx, gy), lv)
    deg = bs["deg"]
    Hx = ip(W, bs["P"], X[:, 0][:, None] * bs["P"])
    dens = block_density(ops["Dx_pi"], deg)
    # mean density of the strictly-lower band blocks (row degree < col degree)
    low = [v for (kr, kc), v in dens.items() if kr < kc]
    print("%-42s %5d %9.1e %9s %9s %9s %9s | %8d %8d %8d %6.2f" % (
        name, b, bs["orth"], deg_band(ops["Dx_pi"], deg), deg_band(ops["Dy_pi"], deg), deg_band(ops["L_pi2"], deg),
        deg_band(ops["Dx_plain"], deg), nnz(Hx), nnz(ops["Dx_pi"]), len(deg), np.mean(low)))

# ---------------------------------------------------------------- C: Dirichlet formulations on the pentagon
print("\n=== C: Dirichlet formulations with trial space pi*Pi_n on the pentagon (Lebesgue), b = 5 ===")
print("Green check (test pi*Pi_n equals -S): ", end="")
bs = graded_basis(Xp, Wp, 8); pv = pi5(Xp[:, 0], Xp[:, 1]); gx, gy = g5(Xp[:, 0], Xp[:, 1]); lv = l5(Xp[:, 0], Xp[:, 1])
ops = operators(bs, Wp, pv, (gx, gy), lv)
print("%.2e" % (np.linalg.norm(ops["Mpi"] + ops["S"]) / np.linalg.norm(ops["S"])))
print("n = 8: degree band of S (test pi*Pi_n) =", deg_band(ops["S"], bs["deg"]), " expected (2b-2, 2b-2) = (8, 8)")
print("n = 8: degree band of M (draft PG, test Pi_n) =", deg_band(ops["M"], bs["deg"]), " (lower band = n means NOT banded below)")
print("\n%4s %5s %12s %12s %12s %12s %12s" % ("n", "N", "kappa(S)", "kappa(S) bp", "kappa(M)", "kappa(M) bp", "lambda_min(S)"))
rows = []
for n in range(4, 17, 2):
    t0 = time.time()
    g = max(20, n + 8)
    X, W = polygon_mesh(V5, g, fan_from=V5.mean(axis=0))
    bs = graded_basis(X, W, n); pv = pi5(X[:, 0], X[:, 1]); gx, gy = g5(X[:, 0], X[:, 1]); lv = l5(X[:, 0], X[:, 1])
    ops = operators(bs, W, pv, (gx, gy), lv)
    S, M, deg = ops["S"], ops["M"], bs["deg"]
    kS = np.linalg.cond(S); kSp = block_precond_kappa(S, deg)
    kM = np.linalg.cond(M)
    # block-diagonal preconditioning of the nonsymmetric PG matrix: left-right by block diag of M (via its symmetric part is meaningless); use D^{-1} M with D = block diag(M)
    D = np.zeros_like(M)
    for k in range(deg.max() + 1):
        m = deg == k; D[np.ix_(m, m)] = M[np.ix_(m, m)]
    kMp = np.linalg.cond(np.linalg.solve(D, M))
    lmin = np.linalg.eigvalsh(0.5 * (S + S.T))[0]
    rows.append((n, len(deg), kS, kSp, kM, kMp, lmin))
    print("%4d %5d %12.3e %12.3e %12.3e %12.3e %12.3e   (%.1fs)" % (n, len(deg), kS, kSp, kM, kMp, lmin, time.time() - t0))
rows = np.array(rows)
def slope(y):
    return np.polyfit(np.log(rows[:, 0]), np.log(y), 1)[0]
def slope_tail(y):
    sel = rows[:, 0] >= 8
    return np.polyfit(np.log(rows[sel, 0]), np.log(y[sel]), 1)[0]
print("\nLS growth exponents in n (all n / n>=8): kappa(S) %.2f / %.2f ; kappa(S) block-precond %.2f / %.2f ; kappa(M) %.2f / %.2f ; kappa(M) block-precond %.2f / %.2f ; lambda_min(S) %.2f / %.2f" % (
    slope(rows[:, 2]), slope_tail(rows[:, 2]), slope(rows[:, 3]), slope_tail(rows[:, 3]), slope(rows[:, 4]), slope_tail(rows[:, 4]), slope(rows[:, 5]), slope_tail(rows[:, 5]), slope(rows[:, 6]), slope_tail(rows[:, 6])))

# ---------------------------------------------------------------- D: recurrence-evaluation cost vs dense
print("\n=== D: nnz(H_x)+nnz(H_y) (= flops per evaluation point of the graded recurrence) versus N and N^(3/2) ===")
for n in [4, 6, 8, 10, 12]:
    X, W = polygon_mesh(V5, 20, fan_from=V5.mean(axis=0))
    bs = graded_basis(X, W, n)
    Hx = ip(W, bs["P"], X[:, 0][:, None] * bs["P"]); Hy = ip(W, bs["P"], X[:, 1][:, None] * bs["P"])
    N = len(bs["deg"]); z = nnz(Hx) + nnz(Hy)
    print("n=%2d N=%4d nnz(Hx)+nnz(Hy)=%6d  ratio to N=%.2f  ratio to N^1.5=%.3f" % (n, N, z, z / N, z / N**1.5))

# ---------------------------------------------------------------- E: the 1D-Shen / Olver-ladder choice of trial basis
# trial u = pi * ptilde with ptilde orthonormal w.r.t. pi*dmu (one more weighted QR on the SAME mesh: no conversion
# operator needed in the discrete setting).  Weighted differentiation D_x : ptilde -> d_x(pi ptilde) expanded in the
# dmu-orthonormal basis is block-banded (degrees deg+1 .. deg+b-1) by the same integration by parts; the stiffness is
# S~ = D_x^T D_x + D_y^T D_y (banded) and its conditioning is measured below.
print("\n=== E: trial basis pi * (OPs of pi*dmu) on the pentagon: band of weighted differentiation and kappa ===")
print("%4s %5s %14s %14s %12s %12s" % ("n", "N", "band Dx~", "band S~", "kappa(S~)", "kappa(S~) bp"))
rowsE = []
for n in range(4, 17, 2):
    g = max(20, n + 8)
    X, W = polygon_mesh(V5, g, fan_from=V5.mean(axis=0))
    pv = pi5(X[:, 0], X[:, 1]); gx, gy = g5(X[:, 0], X[:, 1])
    bs = graded_basis(X, W, n + 4)        # dmu-orthonormal range basis up to degree n+b-1 (b = 5)
    bt = graded_basis(X, W * pv, n)       # pi*dmu-orthonormal (trial basis generator), degree n
    Ux = bt["P"] * gx[:, None] + pv[:, None] * bt["Px"]; Uy = bt["P"] * gy[:, None] + pv[:, None] * bt["Py"]
    Dx = ip(W, bs["P"], Ux); Dy = ip(W, bs["P"], Uy)
    St = Dx.T @ Dx + Dy.T @ Dy
    deg = bt["deg"]; degR = bs["deg"]
    # exact stiffness for comparison (direct quadrature of grad u . grad u)
    Sex = ip(W, Ux, Ux) + ip(W, Uy, Uy)
    err = np.linalg.norm(St - Sex) / np.linalg.norm(Sex)
    kS = np.linalg.cond(St); kSp = block_precond_kappa(St, deg)
    rowsE.append((n, kS, kSp))
    r, c = np.nonzero(np.abs(Dx) > TOL * np.abs(Dx).max())
    bandDx = (int(np.max(degR[r] - deg[c])), int(np.max(deg[c] - degR[r])))
    print("%4d %5d %14s %14s %12.3e %12.3e   |S~ - S_exact|/|S| = %.1e" % (n, len(deg), bandDx, deg_band(St, deg), kS, kSp, err))
rowsE = np.array(rowsE)
sel = rowsE[:, 0] >= 8
print("LS growth exponents (all / n>=8): kappa(S~) %.2f / %.2f ; block-precond %.2f / %.2f" % (
    np.polyfit(np.log(rowsE[:, 0]), np.log(rowsE[:, 1]), 1)[0], np.polyfit(np.log(rowsE[sel, 0]), np.log(rowsE[sel, 1]), 1)[0],
    np.polyfit(np.log(rowsE[:, 0]), np.log(rowsE[:, 2]), 1)[0], np.polyfit(np.log(rowsE[sel, 0]), np.log(rowsE[sel, 2]), 1)[0]))
print("(expected band of Dx~: (b-1, -1) = (4, -1): d_x(pi ptilde_j) lives in dmu-degrees deg_j+1 .. deg_j+b-1)")
