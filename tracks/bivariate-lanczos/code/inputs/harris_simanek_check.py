"""Check: the explicit Padua recurrence (RESULTS.md item 2) is a special case of a
corollary of Harris & Simanek, Proc. AMS 149 (2021) 3485-3497 (eqs. (6),(7),(11),(14), Thm 5).

For ANY decreasing X = {h_0..h_m}, Y = {g_0..g_{m+1}}, take the checkerboard nodes
N^1_{m,k} = {(h_i, g_j): i-j = k mod 2}. Let p_i (q_j) be orthonormal w.r.t. the discrete
"alternation" measure w_n = (-1)^n / prod_{l!=n}(h_n - h_l) on X (resp. Y).
Claims tested:
 (a) with weights lam = 1/K_m(xi,xi), K_m = sum_{i+j<=m} p_i(s)^2 q_j(t)^2, the product basis
     {p_i(s) q_j(t) : i+j<=m} is discretely ORTHONORMAL (no exceptional element in this normalization);
 (b) lam integrates every product p_i q_j with i+j <= 2m-1 like the product measure mu x mu~ (Thm 5);
 (c) H_x = Q^T X Q, H_y = Q^T Y Q have <= 3 nonzeros/column (<= 2 if the 1D Jacobi matrices have zero
     diagonal), the degree-m block closing via the alternation/aliasing identity (11);
 (d) the IEP basis (Gram-Schmidt of W^{1/2} V in graded order = QR) equals this basis up to signs;
 (e) for Chebyshev-Lobatto X, Y the weights lam are exactly the Padua cubature weights.
"""
import numpy as np

def alt_ops(h):
    """Orthonormal OPs p_0..p_m on decreasing nodes h w.r.t. normalized alternation weights.
    Returns values P[n, i] = p_i(h_n), weights w, and Jacobi matrix J (via Lanczos/Stieltjes)."""
    h = np.asarray(h, float); m1 = len(h)
    w = np.array([(-1)**n / np.prod([h[n]-h[l] for l in range(m1) if l != n]) for n in range(m1)])
    assert (w > 0).all(); w = w / w.sum()
    # Stieltjes with full reorthogonalization (small sizes)
    P = np.zeros((m1, m1)); P[:, 0] = 1.0
    a = np.zeros(m1); b = np.zeros(m1)
    for i in range(m1):
        if i > 0:
            v = h*P[:, i-1] - a[i-1]*P[:, i-1] - (b[i-1]*P[:, i-2] if i > 1 else 0)
            for r in range(2):
                v -= P[:, :i] @ (P[:, :i].T @ (w*v))
            b[i-1] = np.sqrt(np.sum(w*v*v)); P[:, i] = v/b[i-1]
        a[i] = np.sum(w*h*P[:, i]**2)
    return P, w, a, b

def check(hx, hy, k=0, label=""):
    m = len(hx)-1; assert len(hy) == m+2
    Px, wx, ax, bx = alt_ops(hx); Py, wy, ay, by = alt_ops(hy)
    # alternation property (6): p_{m-i}(h_n) = (-1)^n p_i(h_n)  (up to the sign convention)
    alt_err = max(np.abs(Px[:, m-i] - ((-1)**np.arange(m+1))*Px[:, i]).max() for i in range(m+1))
    nodes = [(i, j) for i in range(m+1) for j in range(m+2) if (i-j) % 2 == k]
    idx = [(i, d-i) for d in range(m+1) for i in range(d, -1, -1)]          # graded order
    V = np.array([[Px[i, a_]*Py[j, b_] for (a_, b_) in idx] for (i, j) in nodes])
    lam = 1.0/np.sum(V**2, axis=1)                                           # 1/K_m(xi,xi)
    N = len(nodes)
    G = V.T @ (lam[:, None]*V)
    orth = np.abs(G - np.eye(N)).max()
    # (b) exactness for products of degree <= 2m-1 against product of 1D discrete measures
    ex = 0.0
    for a1 in range(m+1):
        for b1 in range(m+2):
            if a1+b1 <= 2*m-1:
                disc = sum(l*Px[i, a1]*Py[j, b1] for l, (i, j) in zip(lam, nodes))
                ex = max(ex, abs(disc - (1.0 if a1 == b1 == 0 else 0.0)))
    X = np.array([hx[i] for (i, j) in nodes]); Y = np.array([hy[j] for (i, j) in nodes])
    Q = np.sqrt(lam)[:, None]*V
    out = {}
    for name, c in (("Hx", X), ("Hy", Y)):
        H = Q.T @ (c[:, None]*Q); nnz = (np.abs(H) > 1e-10*np.abs(H).max()).sum(axis=0)
        out[name] = (nnz.max(), int(nnz.sum()), np.abs(H-H.T).max())
    # (d) IEP basis = Gram-Schmidt (QR) of W^{1/2} * [T_a(s) T_b(t)] in the same graded order
    #     (any graded-triangular starting basis gives the same orthonormal basis up to signs)
    sx = (X - (hx.max()+hx.min())/2)/((hx.max()-hx.min())/2); sy = (Y - (hy.max()+hy.min())/2)/((hy.max()-hy.min())/2)
    Tb = np.array([np.cos(a_*np.arccos(np.clip(sx, -1, 1)))*np.cos(b_*np.arccos(np.clip(sy, -1, 1))) for (a_, b_) in idx]).T
    Qr, R = np.linalg.qr(np.sqrt(lam)[:, None]*Tb)
    dev = np.abs(np.abs(Qr) - np.abs(Q)).max()
    print(f"{label} m={m} k={k} N={N}: alternation err {alt_err:.1e}; sum lam={lam.sum():.15f}; "
          f"max|Gram-I|={orth:.1e}; exactness(deg<=2m-1) err {ex:.1e}; "
          f"Hx maxnnz/col={out['Hx'][0]} (nnz {out['Hx'][1]}), Hy maxnnz/col={out['Hy'][0]} (nnz {out['Hy'][1]}); "
          f"max| |Q_QR|-|Q_explicit| |={dev:.1e}")
    return nodes, lam

rng = np.random.default_rng(0)
for m in (6, 15, 30):
    hx = np.sort(rng.uniform(-1, 1, m+1))[::-1]; hy = np.sort(rng.uniform(-1, 1, m+2))[::-1]
    check(hx, hy, 0, "random  ")
    check(hx, hy, 1, "random  ")
    # Gauss-Jacobi-like / Legendre-Lobatto-like nodes
    hx = np.cos(np.linspace(0, np.pi, m+1)**1.3/np.pi**0.3); hy = np.sort(np.polynomial.legendre.leggauss(m+2)[0])[::-1]
    check(hx, hy, 0, "warped  ")
    # Chebyshev-Lobatto = Padua (first/third family)
    hx = np.cos(np.arange(m+1)*np.pi/m); hy = np.cos(np.arange(m+2)*np.pi/(m+1))
    nodes, lam = check(hx, hy, 0, "Padua   ")
    e = lambda i, M: 0.5 if i in (0, M) else 1.0
    wpad = np.array([2*e(i, m)*e(j, m+1)/(m*(m+1)) for (i, j) in nodes])
    print(f"          Padua cubature weights reproduced: max|lam - w_Padua| = {np.abs(lam-wpad).max():.1e}")
