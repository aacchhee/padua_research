"""Check: with Padua cubature weights, the discrete orthonormal basis (graded order)
is the normalized product Chebyshev basis, and H_x, H_y = Q^T X Q, Q^T Y Q are
nearly explicit (<=2 nonzeros/column except the top degree block).
Also compare with equal weights (as in Van Barel-Chesnokov 2010)."""
import numpy as np

def padua(n):
    # Pad_n = {(cos(j pi/n), cos(k pi/(n+1))) : 0<=j<=n, 0<=k<=n+1, j+k even}  (first family)
    pts, w = [], []
    for j in range(n+1):
        for k in range(n+2):
            if (j+k) % 2 == 0:
                x, y = np.cos(j*np.pi/n), np.cos(k*np.pi/(n+1))
                pts.append((x, y))
                ej = 0.5 if j in (0, n) else 1.0
                ek = 0.5 if k in (0, n+1) else 1.0
                w.append(2*ej*ek/(n*(n+1)))     # weights sum to 1 (normalized Chebyshev measure)
    return np.array(pts), np.array(w)

def cheb_basis(pts, n):
    # orthonormal Chebyshev product basis, graded (total degree) order: degree d, then j=x-degree desc
    x, y = pts[:, 0], pts[:, 1]
    tx = np.cos(np.outer(np.arccos(np.clip(x, -1, 1)), np.arange(n+1)))
    ty = np.cos(np.outer(np.arccos(np.clip(y, -1, 1)), np.arange(n+1)))
    cols, idx = [], []
    for d in range(n+1):
        for i in range(d, -1, -1):
            j = d - i
            s = (np.sqrt(2) if i > 0 else 1) * (np.sqrt(2) if j > 0 else 1)
            cols.append(s*tx[:, i]*ty[:, j]); idx.append((i, j))
    return np.array(cols).T, idx

for n in [6, 20, 60]:
    P, w = padua(n)
    V, idx = cheb_basis(P, n)
    N = len(w)
    G = V.T @ (w[:, None]*V)
    off = G - np.diag(np.diag(G))
    bad = [idx[k] for k in range(N) if abs(G[k, k]-1) > 1e-10]
    print(f"n={n}: N={N}, sum w={w.sum():.15f}, max|offdiag Gram|={abs(off).max():.2e}, "
          f"basis elems with norm^2 != 1: {bad} (norm^2={[round(G[idx.index(b), idx.index(b)], 12) for b in bad]})")
    # Orthonormal Q from Padua-weight inner product: Q = W^{1/2} V D^{-1/2}
    Q = np.sqrt(w)[:, None]*V/np.sqrt(np.diag(G))
    print("   ||Q^T Q - I|| =", np.linalg.norm(Q.T@Q - np.eye(N)))
    for name, c in [("H_x", P[:, 0]), ("H_y", P[:, 1])]:
        H = Q.T @ (c[:, None]*Q)
        nnz = (abs(H) > 1e-12).sum(axis=0)
        top = [k for k in range(N) if sum(idx[k]) == n]
        low = [k for k in range(N) if sum(idx[k]) < n]
        print(f"   {name}: max nnz/col for deg<n: {nnz[low].max()}, deg=n block: max nnz/col {nnz[top].max()}, "
              f"total nnz {int((abs(H)>1e-12).sum())} of {N*N}")
    # Equal weights (seed paper's setting): orthonormalize Chebyshev basis by QR -> Hessenberg-like structure
    Qe, R = np.linalg.qr(V/np.sqrt(N))
    Hx = Qe.T @ (P[:, 0][:, None]*Qe)
    nnz_e = int((abs(Hx) > 1e-10).sum())
    print(f"   equal weights: H_x nnz {nnz_e} of {N*N} (lower bandwidth-type structure, not explicit)")
