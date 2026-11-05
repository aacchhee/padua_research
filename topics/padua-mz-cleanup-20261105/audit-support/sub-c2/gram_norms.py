#!/usr/bin/env python3
"""Auditor check (Claude subC2): (i) G_{m,n}=I for 2n<=m (theta<=1/2) and failure at n=floor(m/2)+1,
odd and even m; (ii) continuous squared norms of the odd-m carriers vs C0^2 via exact Chebyshev
product/integration in float; (iii) lambda_-(m,m-1), lambda_+(m,m-1) at a few odd m (diagnostic)."""
import numpy as np, sys
from scipy.special import eval_legendre
sys.path.insert(0, '/tmp/claude-0/subC2')
from majorant import weights

def gram(m, n):
    W, _, mask = weights(m)
    J, K = np.nonzero(mask)
    w = W[J, K]
    x = np.cos(np.pi * J / m); y = np.cos(np.pi * K / (m + 1))
    lx = np.array([np.sqrt((2 * r + 1) / 2) * eval_legendre(r, x) for r in range(n + 1)])
    ly = np.array([np.sqrt((2 * r + 1) / 2) * eval_legendre(r, y) for r in range(n + 1)])
    B = np.array([lx[a] * ly[d - a] for d in range(n + 1) for a in range(d, -1, -1)]).T
    return B.T @ (w[:, None] * B)

def cheb_mul(p, q):
    out = np.zeros(len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        if pi == 0: continue
        out[i:i + len(q)] += pi * q / 2
        for j2, qj in enumerate(q):
            out[abs(i - j2)] += pi * qj / 2
    return out

def cheb_int(c):
    l = np.arange(len(c))
    h = np.where(l % 2 == 0, 2.0 / (1 - l * l + 0.0), 0.0)
    return float(np.sum(c * h))

def fejer_coef(u):
    return np.concatenate([[1.0], 2 * (1 - np.arange(1, u + 1) / (u + 1))])

if __name__ == '__main__':
    print('(i) ||G_{m,n}-I||_2 at n=floor(m/2) (2n<=m) and n=floor(m/2)+1:')
    for m in (5, 7, 9, 21, 31, 51, 6, 20):
        n0 = m // 2
        e0 = np.linalg.norm(gram(m, n0) - np.eye((n0 + 1) * (n0 + 2) // 2), 2)
        e1 = np.linalg.norm(gram(m, n0 + 1) - np.eye((n0 + 2) * (n0 + 3) // 2), 2)
        print(f'  m={m:3d} ({"odd" if m % 2 else "even"}): n={n0}: {e0:.2e};  n={n0+1}: {e1:.3e}')
    C0 = (1 + np.pi ** 4) / 2
    print(f'(ii) C0={C0:.6f}, C0^2={C0**2:.4f}; max_u<=2000 ||F_u||^2 =',
          max(cheb_int(cheb_mul(fejer_coef(u), fejer_coef(u))) for u in list(range(0, 60)) + [100, 500, 1000, 2000]))
    for m in (33, 65, 129, 257):
        M = m + 1
        for (a, b, sg) in ((0.25, 0.2, '-'), (0.125, 0.2, '+')):
            r, s = int(a * m), int(b * m)
            car = np.zeros(M // 2 + r + 1)
            if sg == '-':
                car[M // 2] = 1.0
            else:
                car[M // 2 - r] = 0.5; car[M // 2 + r] = -0.5
            Fr = fejer_coef(r); Fs = fejer_coef(s)
            A = cheb_mul(car, Fr)
            nrm = cheb_int(cheb_mul(A, A)) * cheb_int(cheb_mul(Fs, Fs))
            print(f'  m={m} p{sg} a={a} b={b}: ||p||^2={nrm:.12f} (<= C0^2: {nrm <= C0**2}, >0: {nrm > 0})')
    print('(iii) diagnostic extreme eigenvalues at n=m-1 (float64, formula weights):')
    for m in (21, 41, 61, 81):
        ev = np.linalg.eigvalsh(gram(m, m - 1))
        print(f'  m={m}: lambda_-={ev[0]:.6f} lambda_+={ev[-1]:.6f}')
