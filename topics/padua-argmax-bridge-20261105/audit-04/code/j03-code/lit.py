"""J3 audit: float64 (MEASURED) Lebesgue function from the published Padua Lagrange formula
(Caliari-De Marchi-Vianello / Bos-De Marchi-Vianello-Xu reproducing-kernel form, first family):
L_xi(x) = w_xi [K_n(xi,x) - (1/2) That_n(xi_1) That_n(x_1)], K_n = sum_{p+q<=n} That_p That_q That_p That_q,
That_0=1, That_p=sqrt2 T_p, w = (1/(n(n+1))) {1/2 vertex, 1 edge, 2 interior}; nodes (cos j pi/n, cos k pi/(n+1)),
j+k even. Self-validated by the cardinal property at small n (no reliance on the paper's reflection formula)."""
import numpy as np
def nodes(n):
    m = n + 1
    return [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]
def basis_values(n, x1, x2):
    m = n + 1; p = np.arange(n + 1); sc = np.where(p == 0, 1.0, np.sqrt(2.0))
    th = np.arange(n + 1) * np.pi / n; ph = np.arange(m + 1) * np.pi / m
    t1 = np.arccos(np.clip(x1, -1, 1)); t2 = np.arccos(np.clip(x2, -1, 1))
    A = (sc * np.cos(np.outer(th, p))) * (sc * np.cos(p * t1))        # [j,p]
    B = (sc * np.cos(np.outer(ph, p))) * (sc * np.cos(p * t2))        # [k,q]
    C = np.cumsum(B, axis=1)                                            # [k,t]=sum_{q<=t}
    K = A @ C[:, ::-1].T                                                # [j,k]=sum_p A[j,p] C[k,n-p]
    corr = 0.5 * (np.sqrt(2) * np.cos(n * th))[:, None] * (np.sqrt(2) * np.cos(n * t1))
    e = np.where((np.arange(n + 1) == 0) | (np.arange(n + 1) == n), 0.5, 1.0)
    f = np.where((np.arange(m + 1) == 0) | (np.arange(m + 1) == m), 0.5, 1.0)
    w = 2 * np.outer(e, f) / (n * m)
    L = w * (K - corr)
    mask = (np.add.outer(np.arange(n + 1), np.arange(m + 1)) % 2) == 0
    return L[mask]
def lebesgue(n, x1, x2): return float(np.abs(basis_values(n, x1, x2)).sum())
def cardinal_defect(n):
    worst = 0.0
    for idx, (j, k) in enumerate(nodes(n)):
        L = basis_values(n, np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1)))
        e = np.zeros_like(L); e[idx] = 1.0; worst = max(worst, float(np.abs(L - e).max()))
    return worst
