"""Cheap decisive tests for angle-D drafts (gen4). Seconds-long. Model run: claude-fable-5-1, 2026-10-31."""
import numpy as np, itertools, time

def padua(n):
    pts, wts = [], []
    for j in range(n+1):
        for k in range(n+2):
            if (j+k) % 2 == 0:
                x = np.cos(j*np.pi/n); y = np.cos(k*np.pi/(n+1))
                ej = 0.5 if j in (0, n) else 1.0
                ek = 0.5 if k in (0, n+1) else 1.0
                pts.append((x, y)); wts.append(2*ej*ek/(n*(n+1)))
    return np.array(pts), np.array(wts)

def cheb_basis(X, Y, k):
    """orthonormal product-Chebyshev basis for the product Chebyshev prob. measure, total degree <= k, graded order"""
    idx = [(i, j) for d in range(k+1) for i in range(d, -1, -1) for j in [d-i]]
    Tx = [np.ones_like(X), X]; Ty = [np.ones_like(Y), Y]
    for m in range(2, k+1):
        Tx.append(2*X*Tx[-1]-Tx[-2]); Ty.append(2*Y*Ty[-1]-Ty[-2])
    cols = []
    for (i, j) in idx:
        c = (np.sqrt(2) if i > 0 else 1.0)*(np.sqrt(2) if j > 0 else 1.0)
        cols.append(c*Tx[i]*Ty[j])
    return np.array(cols).T, idx

def test1_christoffel_ratio(n, thetas=(0.5, 0.8, 0.95, 1.0), weights='equal'):
    P, w = padua(n)
    if weights == 'equal':
        w = np.ones(len(P))/len(P)
    # fine evaluation grid
    g = np.cos(np.linspace(0, np.pi, 121))
    GX, GY = np.meshgrid(g, g); GX = GX.ravel(); GY = GY.ravel()
    out = {}
    for th in thetas:
        k = int(round(th*n)) if th < 1 else n
        V, _ = cheb_basis(P[:, 0], P[:, 1], k)
        Q, R = np.linalg.qr(np.sqrt(w)[:, None]*V)
        # discrete orthonormal basis evaluated on grid: phi = basis * R^{-1}
        Vg, _ = cheb_basis(GX, GY, k)
        Phi = np.linalg.solve(R.T, Vg.T).T
        Kd = np.sum(Phi**2, axis=1)
        Kc = np.sum(Vg**2, axis=1)
        r = Kd/Kc
        # corner, edge-mid, centre values
        out[th] = dict(k=k, rmin=r.min(), rmax=r.max(), r_centre=r[len(r)//2],
                       r_corner=r[0], frac_dev5=np.mean(np.abs(r-1) > 0.05))
    return out

def test2_joint_ritz(n, thetas=(0.5, 0.8, 0.95), weights='equal'):
    P, w = padua(n)
    if weights == 'equal':
        w = np.ones(len(P))/len(P)
    res = {}
    for th in thetas:
        k = int(round(th*n))
        V, idx = cheb_basis(P[:, 0], P[:, 1], k)
        Q, R = np.linalg.qr(np.sqrt(w)[:, None]*V)
        Hx = Q.T @ (P[:, 0][:, None]*Q); Hy = Q.T @ (P[:, 1][:, None]*Q)
        comm = np.linalg.norm(Hx@Hy - Hy@Hx)
        # joint eigenvalues via eig of Hx + i Hy (approximate; sections are nearly normal only if comm small)
        ev = np.linalg.eigvals(Hx + 1j*Hy)
        Z = P[:, 0] + 1j*P[:, 1]
        d = np.min(np.abs(ev[:, None] - Z[None, :]), axis=1)
        res[th] = dict(k=k, dim=len(idx), comm=comm, conv1e8=int(np.sum(d < 1e-8)),
                       conv1e3=int(np.sum(d < 1e-3)), med_dist=float(np.median(d)))
    return res

def test3_padua_weights_vs_christoffel(n):
    P, w = padua(n)
    V, idx = cheb_basis(P[:, 0], P[:, 1], n)
    K = np.sum(V**2, axis=1)                      # K_n(B,B) continuous product-Chebyshev kernel
    Tn_y = np.cos(n*np.arccos(np.clip(P[:, 1], -1, 1)))
    # candidates: 1/K, 1/(K - 2 Tn(y)^2)  [normalized T_n has factor sqrt2 -> (sqrt2 Tn)^2 = 2Tn^2], 1/(K - Tn(y)^2)
    c0 = 1/K; c1 = 1/(K - 2*Tn_y**2); c2 = 1/(K - Tn_y**2)
    return dict(err_1overK=np.max(np.abs(c0/w-1)), err_mod2=np.max(np.abs(c1/w-1)), err_mod1=np.max(np.abs(c2/w-1)))

def test4_vandermonde_root(nmax=24):
    """n-th root behaviour of |det V(Pad_n)| in orthonormal Chebyshev basis vs the Gram identity (det V^2 = prod 1/w * 2 ...)."""
    out = []
    for n in range(4, nmax+1, 4):
        P, w = padua(n)
        V, idx = cheb_basis(P[:, 0], P[:, 1], n)
        s = np.linalg.svd(V, compute_uv=False)
        logdet = np.sum(np.log(s))
        ell = sum(i+j for (i, j) in idx)   # sum of degrees
        # Fekete-type normalisation: |det|^{1/ell}
        out.append((n, len(idx), logdet, np.exp(logdet/ell)))
    return out

if __name__ == '__main__':
    t = time.time()
    print('TEST1 Christoffel ratio, equal weights, Padua n=20,40')
    for n in (20, 40):
        print(n, test1_christoffel_ratio(n))
    print('TEST1 cubature weights n=20 (control, expect ratio 1 for theta<1):', test1_christoffel_ratio(20, thetas=(0.5, 0.95), weights='cubature'))
    print('TEST2 joint Ritz, equal weights, n=20,30')
    for n in (20, 30):
        print(n, test2_joint_ritz(n))
    print('TEST2 cubature weights n=20:', test2_joint_ritz(20, weights='cubature'))
    print('TEST3 Padua weights vs Christoffel, n=6,15,30')
    for n in (6, 15, 30):
        print(n, test3_padua_weights_vs_christoffel(n))
    print('TEST4 Vandermonde root', test4_vandermonde_root())
    print('elapsed', time.time()-t)
