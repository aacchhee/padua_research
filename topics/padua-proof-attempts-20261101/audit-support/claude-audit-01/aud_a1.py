"""Auditor's independent check of A1 (Claude audit, not Codex code).

Route deliberately different from the developer's checker: cardinals are
obtained by solving the Lagrange system in a *monomial* basis with mpmath at
80 digits (no kernel formula, no Chebyshev basis), for n = 1..14, and the
corner Lebesgue values are compared with the A1 formula evaluated with
U_m via explicit geometric sums (no sin quotient, so no singular limits).
Also checks term-by-term (cardinal-level) agreement, not only the absolute sum.
MEASURED in this scope (high-precision floating); the all-n claim rests on the proof.
"""
import json
import mpmath as mp

mp.mp.dps = 80


def nodes(n):
    out = []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                ej = mp.mpf(1) / 2 if j in (0, n) else 1
                ek = mp.mpf(1) / 2 if k in (0, n + 1) else 1
                out.append((j, k, mp.cos(j * mp.pi / n), mp.cos(k * mp.pi / (n + 1)), mp.mpf(2) * ej * ek / (n * (n + 1))))
    return out


def Ugeom(m, t):
    # sum_{r=-m+1, step 2}^{m-1} e^{irt}, real
    return mp.fsum(mp.cos(r * t) for r in range(-m + 1, m, 2))


def D(n, u, v):
    S, T = (u + v) / 2, (v - u) / 2
    return Ugeom(n + 1, S) * Ugeom(n + 1, T) + Ugeom(n, S) * Ugeom(n, T)


res = []
for n in range(1, 11):
    nd = nodes(n)
    mons = [(d - b, b) for d in range(n + 1) for b in range(d + 1)]
    V = mp.matrix([[x ** a * y ** b for a, b in mons] for _, _, x, y, _ in nd])
    Vinv = mp.inverse(V)
    worst_card = mp.mpf(0)
    worst_sum = mp.mpf(0)
    for tc in (0, mp.pi):
        for pc in (0, mp.pi):
            cx, cy = mp.cos(tc), mp.cos(pc)
            mvec = [cx ** a * cy ** b for a, b in mons]
            # L_B(c) = sum_i mvec_i Vinv[i, B]
            lam = mp.mpf(0)
            rhs = mp.mpf(0)
            for B, (j, k, x, y, w) in enumerate(nd):
                LB = mp.fsum(mvec[i] * Vinv[i, B] for i in range(len(mons)))
                formula = w * (D(n, tc + j * mp.pi / n, pc + k * mp.pi / (n + 1)) - mp.cos(n * tc) * (-1) ** j)
                worst_card = max(worst_card, abs(LB - formula))
                lam += abs(LB)
                rhs += abs(formula)
            worst_sum = max(worst_sum, abs(lam - rhs))
    res.append({"n": n, "N": len(nd), "max_cardinal_diff": mp.nstr(worst_card, 3),
                "max_corner_sum_diff": mp.nstr(worst_sum, 3)})
    assert worst_card < mp.mpf(10) ** -40, (n, worst_card)
print(json.dumps({"check": "A1 auditor independent (monomial Vandermonde, mpmath 80 dps)", "results": res}, indent=1))
