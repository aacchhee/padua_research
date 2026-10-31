"""F7 adversarial check: extreme eigenvalues of the Clenshaw-Curtis Gram matrix of
orthonormal Legendre polynomials of degree <= n (n = N-1), for large N.

Works in the Chebyshev coefficient basis: p = sum a_i T_i,
  I(p^2) = a^T T a,  Q_N(p^2) = a^T Qm a,
  T_ij = (I(T_{i+j}) + I(T_{|i-j|}))/2,  Qm_ij = (Q(T_{i+j}) + Q(T_{|i-j|}))/2,
  Q(T_k) = I(T_k) for k <= N, I(T_{2N-k}) for N < k <= 2N (Lobatto aliasing).
eig(G) = generalized eig(Qm, T). Even/odd parts decouple.
Also: Rayleigh quotient of U_{N-1} (vanishes at all interior CC nodes), an explicit
upper bound for lambda_min.
"""
import sys, time, numpy as np
from scipy.linalg import eigh

def Ik(k):
    k = np.asarray(k)
    return np.where(k % 2 == 1, 0.0, 2.0 / (1.0 - k.astype(float) ** 2))

def Qk(k, N):
    k = np.asarray(k)
    return np.where(k <= N, Ik(k), Ik(2 * N - k))

def extremes(N, n, parity):
    idx = np.arange(parity, n + 1, 2)
    S = idx[:, None] + idx[None, :]; D = np.abs(idx[:, None] - idx[None, :])
    T = 0.5 * (Ik(S) + Ik(D)); Qm = 0.5 * (Qk(S, N) + Qk(D, N))
    m = len(idx)
    lo = eigh(Qm, T, eigvals_only=True, subset_by_index=[0, 0])[0]
    hi = eigh(Qm, T, eigvals_only=True, subset_by_index=[m - 1, m - 1])[0]
    return lo, hi

def u_ratio(N):
    # U_{N-1} = sum of T's: U_{N-1} = 2*sum_{j odd/even} T_j (+-T_0 correction)
    a = np.zeros(N)
    for j in range(N - 1, -1, -2):
        a[j] = 2.0
    if (N - 1) % 2 == 0:
        a[0] = 1.0
    idx = np.arange(N)
    S = idx[:, None] + idx[None, :]; D = np.abs(idx[:, None] - idx[None, :])
    T = 0.5 * (Ik(S) + Ik(D)); Qm = 0.5 * (Qk(S, N) + Qk(D, N))
    return (a @ Qm @ a) / (a @ T @ a)

if __name__ == "__main__":
    Ns = [int(s) for s in sys.argv[1:]] or [40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]
    for N in Ns:
        t = time.time(); n = N - 1
        r = [extremes(N, n, p) for p in (0, 1)]
        lo = min(x[0] for x in r); hi = max(x[1] for x in r)
        ur = u_ratio(N) if N <= 5120 else float('nan')
        print(f"N={N:6d} n=N-1: lmin={lo:.6f} (even {r[0][0]:.6f}, odd {r[1][0]:.6f})  lmax={hi:.6f}  "
              f"eta={max(1-lo, hi-1):.6f}  1/lmin={1/lo:.4f}  lnN={np.log(N):.3f}  RQ(U_N-1)={ur:.5f}  [{time.time()-t:.0f}s]", flush=True)
