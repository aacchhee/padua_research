"""Probe: discrete OPs of a time-sampled measure on a closed trigonometric curve.
Quantities: Hilbert function (rank per total degree), bandwidth of H_x,H_y in the
graded discrete-OP basis restricted to the quotient, and conditioning of the
restriction Pi_n -> L^2(curve, dt) relative to the product-Chebyshev measure.
Pure numpy, seconds.
"""
import numpy as np, sys

def curve(name, t):
    if name == "lissajous_5_6":          # Chebyshev/Lissajous: T_6(x)=T_5(y) type, degree 6
        return np.cos(5*t), np.cos(6*t)
    if name == "radial_7_1":             # rhodonea-type (Erb 2018): r=cos 7t
        return np.cos(7*t)*np.cos(t), np.cos(7*t)*np.sin(t)
    if name == "generic_trig_3":         # generic trig curve of trig-degree 4, not Chebyshev
        x = 0.7*np.cos(t) + 0.25*np.cos(3*t+0.4)
        y = 0.7*np.sin(2*t) + 0.2*np.sin(4*t+1.1)
        return x, y
    if name == "generic_trig_5":
        x = 0.6*np.cos(t) + 0.2*np.cos(3*t+0.4) + 0.1*np.cos(5*t+0.9)
        y = 0.6*np.sin(2*t) + 0.2*np.sin(4*t+1.1) + 0.1*np.sin(5*t+0.3)
        return x, y
    raise ValueError(name)

def cheb_basis(x, y, n):
    """orthonormal product-Chebyshev basis (w.r.t. product arcsine measure) in graded order"""
    Tx = np.polynomial.chebyshev.chebvander(x, n)
    Ty = np.polynomial.chebyshev.chebvander(y, n)
    cols, idx = [], []
    for d in range(n+1):
        for j in range(d+1):            # x-degree d-j, y-degree j
            i = d-j
            c = Tx[:, i]*Ty[:, j]*np.sqrt((2 if i else 1)*(2 if j else 1))
            cols.append(c); idx.append((i, j))
    return np.column_stack(cols), idx

def probe(name, M=4000, nmax=14, tol=1e-10):
    t = 2*np.pi*np.arange(M)/M
    x, y = curve(name, t)
    V, idx = cheb_basis(x, y, nmax)
    V = V/np.sqrt(M)                     # discrete inner product = mean over time samples
    print(f"\n== {name}: M={M}, nmax={nmax}")
    # Hilbert function via rank of V restricted to Pi_d
    ranks, kappas = [], []
    for d in range(nmax+1):
        N = (d+1)*(d+2)//2
        s = np.linalg.svd(V[:, :N], compute_uv=False)
        r = int(np.sum(s > tol*s[0]))
        ranks.append(r)
        kappas.append(s[0]/s[min(r, N)-1] if r == N else np.inf)
    print("degree       :", list(range(nmax+1)))
    print("rank h(d)    :", ranks)
    print("increments   :", [ranks[0]] + [ranks[d]-ranks[d-1] for d in range(1, nmax+1)])
    print("kappa restr. :", ["%.1e" % k for k in kappas])
    # graded discrete OPs by pivoted (graded) Gram-Schmidt with tolerance; H_x, H_y bandwidth
    Q, kept, deg = [], [], []
    for k, (i, j) in enumerate(idx):
        v = V[:, k].copy()
        for q in Q: v -= q*(q@v)
        for q in Q: v -= q*(q@v)
        nv = np.linalg.norm(v)
        if nv > tol:
            Q.append(v/nv); kept.append(k); deg.append(i+j)
    Q = np.column_stack(Q); deg = np.array(deg)
    Hx = Q.T @ (x[:, None]*Q); Hy = Q.T @ (y[:, None]*Q)
    def bandwidth(H):
        r, c = np.nonzero(np.abs(H) > 1e-8)
        return int(np.max(np.abs(r-c)))
    # degree-bandwidth: max |deg(row)-deg(col)| over nonzeros (should be <=1 always)
    r, c = np.nonzero(np.abs(Hx) > 1e-8)
    print(f"#OPs kept up to degree {nmax}: {Q.shape[1]} of {len(idx)}; "
          f"index bandwidth Hx={bandwidth(Hx)}, Hy={bandwidth(Hy)}; "
          f"max degree jump Hx={int(np.max(np.abs(deg[r]-deg[c])))}")
    print("orthonormality of kept basis: %.1e" % np.linalg.norm(Q.T@Q-np.eye(Q.shape[1])))

if __name__ == "__main__":
    for name in ["lissajous_5_6", "radial_7_1", "generic_trig_3", "generic_trig_5"]:
        probe(name)
