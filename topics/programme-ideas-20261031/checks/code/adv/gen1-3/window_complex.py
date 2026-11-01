"""Adversarial check gen1-3: does the short window of the linear-pole-per-degree recurrence
survive COMPLEX lines (needed for interior singular curves and for point poles
|z - zeta|^2 = conjugate pairs of complex lines)?

Same construction as window_test.py but with complex coefficients in l_k and the
sesquilinear discrete inner product <f,g> = sum w_i conj(f_i) g_i. Three pole models:
  'real'   real lines (control; reproduces window_test.py)
  'pairs'  conjugate pairs: l_{2j-1} = a x + b y - c with complex (a,b,c), l_{2j} = conj
  'cplx'   independent random complex lines
Spans tested for g = l_{t+1} phi_{t+1,s}:
  A : W_{t-1} + W_t + x W_t + y W_t     B : W_t + x W_t + y W_t
  D : W_{t-2} + W_{t-1} + W_t + x W_t + y W_t
  E : W_0 + ... + W_t + x W_t + y W_t  (full lower span: must hold, sanity)
Scope: M = 120 random nodes, n <= 8, 2 seeds; seconds. MEASURED within this scope only.
"""
import numpy as np
from numpy.polynomial import chebyshev as C


def cheb2(x, y, t):
    return np.column_stack([C.chebval(x, [0] * a + [1]) * C.chebval(y, [0] * (t - a) + [1]) for a in range(t + 1)])


def run(seed, model, n=8, M=120):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, M); y = rng.uniform(-1, 1, M)
    w = rng.uniform(0.5, 1.5, M); sw = np.sqrt(w)
    lines = []
    k = 0
    while len(lines) < n + 2:
        th = rng.uniform(0, 2 * np.pi); c = rng.choice([-1, 1]) * rng.uniform(1.6, 2.5)
        if model == 'real':
            lines.append((np.cos(th), np.sin(th), c))
        elif model == 'cplx':
            lines.append((np.cos(th) + 0.3j * rng.standard_normal(), np.sin(th) + 0.3j * rng.standard_normal(), c + 0.5j * rng.standard_normal()))
        else:  # pairs
            L = (np.cos(th) + 0.3j * rng.standard_normal(), np.sin(th) + 0.3j * rng.standard_normal(), c + 0.5j * rng.standard_normal())
            lines.append(L); lines.append(tuple(np.conj(v) for v in L))
    pis = [np.ones(M, dtype=complex)]
    for (a, b, c) in lines:
        pis.append(pis[-1] * (a * x + b * y - c))
    cols, blocks = [], []
    for t in range(n + 1):
        cols.append(cheb2(x, y, t) / pis[t][:, None]); blocks += [t] * (t + 1)
    A = np.column_stack(cols).astype(complex)
    Qw, _ = np.linalg.qr(sw[:, None] * A); Qw, _ = np.linalg.qr(Qw)
    Q = Qw / sw[:, None]
    blocks = np.array(blocks)
    W = lambda t: Q[:, blocks == t]
    lval = lambda k: lines[k - 1][0] * x + lines[k - 1][1] * y - lines[k - 1][2]

    def resid(S, g):
        U, s, _ = np.linalg.svd(sw[:, None] * S, full_matrices=False)
        rk = int(np.sum(s > 1e-10 * s[0])); U = U[:, :rk]
        b = sw * g; r = b - U @ (U.conj().T @ b)
        return np.linalg.norm(r) / np.linalg.norm(b), rk

    print(f"\n=== model {model}, seed {seed} ===")
    print(" t amb |    A(res,rk)       B(res,rk)       D(res,rk)       E(res,rk)")
    for t in range(1, n):
        g = lval(t + 1)[:, None] * W(t + 1)
        Wt, Wt1 = W(t), W(t - 1)
        xWt, yWt = x[:, None] * Wt, y[:, None] * Wt
        spans = {'A': np.column_stack([Wt1, Wt, xWt, yWt]), 'B': np.column_stack([Wt, xWt, yWt]),
                 'E': np.column_stack([Q[:, blocks <= t], xWt, yWt])}
        spans['D'] = np.column_stack([W(t - 2), Wt1, Wt, xWt, yWt]) if t >= 2 else spans['A']
        amb = (t + 2) * (t + 3) // 2
        cells = []
        for key in 'ABDE':
            rs = [resid(spans[key], g[:, s]) for s in range(g.shape[1])]
            cells.append(f"{max(r for r, _ in rs):.1e},{rs[0][1]:3d}")
        print(f"{t:2d} {amb:3d} |  " + "   ".join(cells))


if __name__ == '__main__':
    for model in ('real', 'pairs', 'cplx'):
        for seed in (1, 2):
            run(seed, model)
