"""Quick checks: (10) projector lemma, (11) normalization lemma (random, float64);
symbolic identity for B_R(u)-uKF and the d >= sqrt2 b inequality chain (sympy)."""
import numpy as np, sympy as sp
rng = np.random.default_rng(5)
worst10 = 0; worst11 = 0
for trial in range(20000):
    n = rng.integers(2, 9); m = rng.integers(1, n + 1)
    Q, _ = np.linalg.qr(rng.standard_normal((n, m)))
    E = rng.standard_normal((n, m)) * 10.0 ** rng.uniform(-6, 0.5)
    Qt, _ = np.linalg.qr(Q + E)
    # choose sign of columns of Qt to be closest to Q (any orthonormal Qt with same columns count is allowed)
    Qt = Qt * np.sign(np.sum(Qt * Q, axis=0) + 1e-300)
    lhs = np.linalg.norm(Qt @ Qt.T - Q @ Q.T, 2)
    mid = np.linalg.norm(Qt - Q, 2); rhs = np.linalg.norm(Qt - Q, 'fro')
    worst10 = max(worst10, lhs / mid if mid > 0 else 0, mid / rhs if rhs > 0 else 0)
    r0 = rng.standard_normal(n); r = r0 + rng.standard_normal(n) * 10.0 ** rng.uniform(-6, 1)
    if np.linalg.norm(r) == 0: continue
    b0, b = np.linalg.norm(r0), np.linalg.norm(r)
    l = np.linalg.norm(r / b - r0 / b0); m1 = (np.linalg.norm(r - r0) + abs(b - b0)) / b0; m2 = 2 * np.linalg.norm(r - r0) / b0
    worst11 = max(worst11, l / m1, m1 / m2)
print('lemma (10): max of ||Pt-P||/||Qt-Q||_2 and ||.||_2/||.||_F =', worst10)
print('lemma (11): max of lhs/middle and middle/right =', worst11)
u, K, F, J, b, d = sp.symbols('u K F J b d', positive=True)
Bexpr = u * K * (F + u * J) / ((1 - u * b) * (1 - u * d))
claim = u**2 * K * (J + F * (b + d) - u * F * b * d) / ((1 - u * b) * (1 - u * d))
print('B - uKF - claimed numerator form simplifies to:', sp.simplify(Bexpr - u * K * F - claim))
