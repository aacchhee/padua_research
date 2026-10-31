"""F1 probe: loss of orthogonality of the truncated bivariate recurrence (BJ 1985: window = degrees
t-2..t, CGS, no reorthogonalisation; and HL: MGS + one reorth) versus degree, and its relation to
convergence of Ritz pairs of the section Z_k = H_x + i H_y (Huhtanen-Larsen SIMAX 2002 p.1088 conjecture).
Ritz residual of (theta, s):  || (X + iY) Q s - theta Q s || with Q the computed basis (k columns).
Node sets: tensor Chebyshev grid (n+1)^2 (Zaccaron-like), uniform random M=(n+1)^2, Padua (M=N).
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import f6_givens_vs_hl_deficit as F

def probe(name, P, nmax, reorth, mgs):
    x, y = P[:, 0].copy(), P[:, 1].copy(); v = np.ones(len(x))
    Nmax = min((nmax + 1) * (nmax + 2) // 2, len(x))
    Q = F.krylov(x, y, v, Nmax, window=True, reorth=reorth, mgs=mgs)
    out = []
    for n in range(4, nmax + 1, 4):
        N = (n + 1) * (n + 2) // 2
        if N > Nmax: break
        Qk = Q[:, :N]; loss = np.abs(Qk.T @ Qk - np.eye(N)).max()
        # Ritz pairs from orthonormalised basis to avoid contamination
        U, _ = np.linalg.qr(Qk)
        Z = U.T @ ((x + 1j * y)[:, None] * U)
        th, S = np.linalg.eig(Z)
        Y = U @ S; R = (x + 1j * y)[:, None] * Y - Y * th
        res = np.linalg.norm(R, axis=0) / np.linalg.norm(Y, axis=0)
        out.append((n, N, loss, res.min(), int(np.sum(res < 1e-8))))
    print(name, "reorth" if reorth else "plain-CGS")
    for r in out:
        print(f"   deg {r[0]:3d} N={r[1]:5d}  max|Q^TQ-I|={r[2]:.1e}  min Ritz residual={r[3]:.1e}  #Ritz res<1e-8: {r[4]}")

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    for n in [24, 40]:
        g = np.cos(np.pi * (np.arange(n + 1) + 0.5) / (n + 1))
        T = np.array([(a, b) for a in g for b in g])
        probe(f"tensor Chebyshev {n+1}^2", T, n, False, False)
        R = rng.uniform(-1, 1, ((n + 1) ** 2, 2))
        probe(f"random M={(n+1)**2}", R, n, False, False)
        R4 = rng.uniform(-1, 1, (4 * (n + 1) ** 2, 2))
        probe(f"random M={4*(n+1)**2}", R4, n, False, False)
    probe("tensor 41^2 (HL reorth)", np.array([(a, b) for a in np.cos(np.pi*(np.arange(41)+.5)/41) for b in np.cos(np.pi*(np.arange(41)+.5)/41)]), 40, True, True)
