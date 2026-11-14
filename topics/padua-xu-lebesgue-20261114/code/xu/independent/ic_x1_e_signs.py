"""Independent check (e): X1-02 (chi) identities, X1-05 Step 2 identity, and the Step 3 witness pairs,
computed directly from d_n values (float64), n = 2..40; plus Delta_n > 0 at all non-vertex complementary
grid points from the fiber sums (n = 2..24)."""
import numpy as np


def dn(n, t):
    j = np.arange(1, n)
    t = np.atleast_1d(t)
    return (1 + 2 * np.cos(np.outer(t, j)).sum(axis=1) + np.cos(n * t)) / (2 * n)


fails = 0
count = 0
for n in range(2, 41):
    odd = np.arange(-8 * n + 1, 8 * n, 2)
    vals = dn(n, odd * np.pi / (2 * n))
    chi = dict(zip(odd.tolist(), np.sign(vals).tolist()))
    assert np.min(np.abs(vals)) > 1e-6
    for m in odd:
        m = int(m)
        if -m in chi and chi[-m] != chi[m]: fails += 1
        if m + 4 * n in chi and chi[m + 4 * n] != chi[m]: fails += 1
        if m + 2 * n in chi and chi[m + 2 * n] != -(-1) ** n * chi[m]: fails += 1
        m0 = m % (4 * n); m0 = m0 if m0 < 2 * n else 4 * n - m0
        if chi[m] != (-1) ** ((m0 - 1) // 2): fails += 1
    for e in range(-6 * n, 6 * n + 1, 2):
        if e % (2 * n) == 0: continue
        if chi[e + 1] * chi[e - 1] != -1: fails += 1
    # Step 3 witnesses at every complementary non-vertex point, and direct Delta via fibers (n <= 24)
    if n <= 24:
        Cn = [p for p in range(4 * n) if p % 2 == (n + 1) % 2]
        fib = {}
        for p in Cn:
            for q in Cn:
                r0, s0 = ((p + q) // 2) % (2 * n), ((p - q) // 2) % (2 * n)
                key = (min(r0, 2 * n - r0), min(s0, 2 * n - s0))
                fib.setdefault(key, []).append((p, q))
        for a in range(n + 1):
            for b in range(n + 1):
                if (a + b) % 2 != n % 2 or (a in (0, n) and b in (0, n)): continue
                i, j = a + b, a - b
                du = {p: dn(n, (i - p) * np.pi / (2 * n))[0] for p in Cn}
                dv = {q: dn(n, (j - q) * np.pi / (2 * n))[0] for q in Cn}
                Delta = sum(sum(abs(du[p] * dv[q]) for p, q in F) - abs(sum(du[p] * dv[q] for p, q in F)) for F in fib.values())
                count += 1
                if not Delta > 1e-8: fails += 1; print('Delta fail', n, a, b, Delta)
print("sign/witness/Delta failures:", fails, "; complementary non-vertex points tested:", count)
