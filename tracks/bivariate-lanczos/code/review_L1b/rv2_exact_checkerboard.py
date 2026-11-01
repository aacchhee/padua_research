"""Exact (Fraction) check of PD-T?bivariate-lanczos-claude-111 part 2 and of its part-1 consequence on small
checkerboards: mu_e(x^a y^b) = 1/2 mu_X(x^a) mu_Y(y^b) for a + b <= 2m (and where it first fails), and the window
coefficients of the graded basis are product-type up to degree m (no within-degree or off-chain coefficients).
Usage: python3 -I -u rv2_exact_checkerboard.py > logs_L1b/exact_checkerboard.log
"""
from fractions import Fraction as Fr


def inv_abs_wprime(xs):
    out = []
    for i, xi in enumerate(xs):
        p = Fr(1)
        for k, xk in enumerate(xs):
            if k != i:
                p *= abs(xi - xk)
        out.append(1 / p)
    return out


def check(xs, ys, e, label):
    m = len(xs) - 1
    assert len(ys) == m + 2
    a = inv_abs_wprime(xs); b = inv_abs_wprime(ys)
    pts = [(xs[i], ys[j], a[i] * b[j]) for i in range(m + 1) for j in range(m + 2) if (i + j) % 2 == e]
    muX = lambda k: sum(ai * xi ** k for ai, xi in zip(a, xs))
    muY = lambda k: sum(bj * yj ** k for bj, yj in zip(b, ys))
    mue = lambda p, q: sum(w * x ** p * y ** q for x, y, w in pts)
    bad = [(p, q) for d in range(2 * m + 1) for p in range(d + 1) for q in [d - p] if mue(p, q) != Fr(1, 2) * muX(p) * muY(q)]
    first_fail = [(p, 2 * m + 1 - p) for p in range(2 * m + 2) if mue(p, 2 * m + 1 - p) != Fr(1, 2) * muX(p) * muY(2 * m + 1 - p)]
    print(f'{label}: m={m}, e={e}, |S_e|={len(pts)} (N_m={(m+1)*(m+2)//2}); moment mismatches for a+b <= 2m: {len(bad)}; '
          f'mismatches at a+b = 2m+1: {first_fail}')
    # product-type window coefficients up to degree m (exact unnormalised Gram-Schmidt, dev products)
    idx = [(t, j) for t in range(m + 1) for j in range(t + 1)]
    pos = {k: i for i, k in enumerate(idx)}
    W = [w for _, _, w in pts]; X = [x for x, _, _ in pts]; Y = [y for _, y, _ in pts]
    V = [[Fr(1)] * len(pts)]
    dot = lambda u, v: sum(wi * ui * vi for wi, ui, vi in zip(W, u, v))
    nonprod = 0
    for k in range(1, len(idx)):
        t, j = idx[k]
        par, A = ((t - 1, 0), X) if j == 0 else ((t - 1, j - 1), Y)
        u = [ai * vi for ai, vi in zip(A, V[pos[par]])]
        r = list(u)
        for l in range(k):
            c = dot(u, V[l]) / dot(V[l], V[l])
            if c != 0:
                tl, jl = idx[l]
                allowed = ((tl, jl) in ((t - 1, 0), (t - 2, 0))) if j == 0 else ((tl, jl) in ((t - 1, j - 1), (t - 2, j - 2)))
                nonprod += 0 if allowed else 1
                r = [ri - c * vl for ri, vl in zip(r, V[l])]
        V.append(r)
    print(f'   graded basis up to degree m: nonzero coefficients outside the product (chain) pattern: {nonprod}')


if __name__ == '__main__':
    print('# rv2_exact_checkerboard.py (exact rationals)')
    m = 4
    s = [Fr(2 * i - m, m) for i in range(m + 1)]; s2 = [Fr(2 * j - (m + 1), m + 1) for j in range(m + 2)]
    check(s, s2, 0, 'equispaced')
    check(s, s2, 1, 'equispaced')
    check([v ** 3 for v in s], [v ** 3 for v in s2], 0, 'cubic-clustered s^3')
    check([Fr(0), Fr(1, 7), Fr(1, 2), Fr(3, 5), Fr(2)], [Fr(-3), Fr(-1), Fr(0), Fr(1, 3), Fr(4, 5), Fr(9, 4)], 0, 'irregular ordered')
    # unordered labels (plan.md AC correction): ordering matters for the |1/w'| weights
    check([Fr(0), Fr(1), Fr(2)], [Fr(0), Fr(1), Fr(3), Fr(2)], 0, 'unordered Y = (0,1,3,2), m = 2')
