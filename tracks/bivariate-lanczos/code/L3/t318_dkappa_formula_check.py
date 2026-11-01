"""MEASURED sanity check of PD-T?bivariate-lanczos-claude-318 (response to Codex
audit-01, finding LF-M2): the derivative of the last-block commutator
kappa(Phi(L)) at a square-case measure L_mu is E -> (E(s_ab))_{a<b}, with
s_ab = R^y_a R^x_b - R^x_a R^y_b in S_1, and its rank equals
dim F, F = {p_C : C perp Hankel}.  Also checks the exact identity (a)
kappa(Phi(L))_ab = L(R^y_a(L) R^x_b(L) - R^x_a(L) R^y_b(L)) at a NON-measure L.

Floating point (numpy), monomial basis in the graded order of PD-T?...-301
(degree, then x-exponent ascending; (s, k-s) <-> x^s y^(k-s)).  Central finite
differences with step h on every moment coordinate give d(kappa o Phi).  This is
a verification record (MEASURED); the statement is proved in the theory file.

Usage: python3 t318_dkappa_formula_check.py
"""
import sys
import numpy as np


def exps(d):
    return [(s, k - s) for k in range(d + 1) for s in range(k + 1)]


def pmul(p, q):
    out = {}
    for (a, b), c in p.items():
        for (a2, b2), c2 in q.items():
            k = (a + a2, b + b2)
            out[k] = out.get(k, 0.0) + c * c2
    return out


def padd(p, q, s=1.0):
    out = dict(p)
    for k, c in q.items():
        out[k] = out.get(k, 0.0) + s * c
    return out


def shift(p, dx, dy):
    return {(a + dx, b + dy): c for (a, b), c in p.items()}


def peval(p, z):
    return sum(c * z[0] ** a * z[1] ** b for (a, b), c in p.items())


def pgrad(p, z):
    gx = sum(c * a * z[0] ** (a - 1) * z[1] ** b for (a, b), c in p.items() if a > 0)
    gy = sum(c * b * z[0] ** a * z[1] ** (b - 1) for (a, b), c in p.items() if b > 0)
    return gx, gy


def apply_L(mom, p):
    return sum(c * mom[e] for e, c in p.items() if abs(c) > 0)


def measure_moments(nodes, w, d):
    return {e: float(sum(wi * z[0] ** e[0] * z[1] ** e[1] for wi, z in zip(w, nodes))) for e in exps(d)}


def sections(mom, n):
    mons = exps(n)
    N = len(mons)
    G = np.array([[mom[(a[0] + b[0], a[1] + b[1])] for b in mons] for a in mons])
    Gx = np.array([[mom[(a[0] + b[0] + 1, a[1] + b[1])] for b in mons] for a in mons])
    Gy = np.array([[mom[(a[0] + b[0], a[1] + b[1] + 1)] for b in mons] for a in mons])
    Lc = np.linalg.cholesky(G)
    Ci = np.linalg.inv(Lc.T)                  # p_a = sum_b Ci[b,a] m_b
    Hx = Ci.T @ Gx @ Ci
    Hy = Ci.T @ Gy @ Ci
    ps = [{mons[b]: Ci[b, a] for b in range(N) if Ci[b, a] != 0.0} for a in range(N)]
    return Hx, Hy, ps


def kappa(mom, n):
    Hx, Hy, _ = sections(mom, n)
    K = Hx @ Hy - Hy @ Hx
    lo = n * (n + 1) // 2
    return K[lo:, lo:]


def interp(nodes, n, f):
    mons = exps(n)
    Vn = np.array([[z[0] ** e[0] * z[1] ** e[1] for e in mons] for z in nodes])
    c = np.linalg.solve(Vn, np.array([peval(f, z) for z in nodes]))
    return {e: ci for e, ci in zip(mons, c)}


def proj_L(mom, ps, f):
    out = {}
    for pc in ps:
        out = padd(out, pc, apply_L(mom, pmul(f, pc)))
    return out


def s_polys(n, ps, P):
    """s_ab for deg a = deg b = n, a < b, with projection P (callable)."""
    lo = n * (n + 1) // 2
    top = ps[lo:]
    Rx = [padd(shift(p, 1, 0), P(shift(p, 1, 0)), -1.0) for p in top]
    Ry = [padd(shift(p, 0, 1), P(shift(p, 0, 1)), -1.0) for p in top]
    out = {}
    for a in range(n + 1):
        for b in range(a + 1, n + 1):
            s = padd(pmul(Ry[a], Rx[b]), pmul(Rx[a], Ry[b]), -1.0)
            topdeg = max(abs(c) for e, c in s.items() if sum(e) == 2 * n + 2) if any(sum(e) == 2 * n + 2 for e in s) else 0.0
            out[(a, b)] = ({e: c for e, c in s.items() if sum(e) <= 2 * n + 1}, topdeg)
    return out


def node_set(kind, n, seed=0):
    if kind == 'padua':
        return [(np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1)))
                for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    if kind == 'equi':
        return [(-1 + 2 * i / n, -1 + 2 * j / (n + 1))
                for i in range(n + 1) for j in range(n + 2) if (i + j) % 2 == 0]
    rng = np.random.default_rng(seed)
    N = (n + 1) * (n + 2) // 2
    return [tuple(v) for v in rng.uniform(-1, 1, size=(N, 2))]


def rank(sv, rtol=1e-9):
    return int(np.sum(sv > rtol * sv[0])) if len(sv) else 0


def run(kind, n, h=None):
    nodes = node_set(kind, n)
    N = len(nodes)
    w = np.random.default_rng(1).uniform(0.5, 1.5, N)
    w = w / w.sum()
    V = exps(2 * n + 1)
    mom = measure_moments(nodes, w, 2 * n + 2)
    if h is None:   # central-difference step scaled to the positive-definiteness margin of M_n(L_mu)
        Gm = np.array([[mom[(a[0] + b[0], a[1] + b[1])] for b in exps(n)] for a in exps(n)])
        h = min(1e-5, 2e-4 * np.linalg.eigvalsh(Gm)[0])
    _, _, ps = sections(mom, n)
    S = s_polys(n, ps, lambda f: interp(nodes, n, f))
    pairs = sorted(S)
    # s_ab in S_1 (values, gradients at nodes) and degree <= 2n+1
    jet_res = max(max(abs(peval(s, z)), *map(abs, pgrad(s, z))) for s, _ in S.values() for z in nodes)
    top_res = max(t for _, t in S.values())
    Fm = np.array([[S[pr][0].get(e, 0.0) for e in V] for pr in pairs])
    # finite differences of kappa o Phi along the moment coordinates
    D = np.zeros_like(Fm)
    for k, e in enumerate(V):
        mp = dict(mom); mm = dict(mom)
        mp[e] += h; mm[e] -= h
        dk = (kappa(mp, n) - kappa(mm, n)) / (2 * h)
        D[:, k] = [dk[a, b] for a, b in pairs]
    rel = np.max(np.abs(D - Fm)) / np.max(np.abs(Fm))
    svD = np.linalg.svd(D, compute_uv=False)
    # dim F: q_j = x^j y^(n+1-j) - I_n(.), C(e_i,e_j) = sym(e_i e_{j+1}^T - e_{i+1} e_j^T), i < j <= n
    qs = []
    for j in range(n + 2):
        mj = {(j, n + 1 - j): 1.0}
        qs.append(padd(mj, interp(nodes, n, mj), -1.0))
    W = exps(2 * n + 2)
    rows = []
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            pc = padd(pmul(qs[i], qs[j + 1]), pmul(qs[i + 1], qs[j]), -1.0)   # q^T C q with C = C(e_i, e_j) (times 1)
            rows.append([pc.get(e, 0.0) for e in W])
    svF = np.linalg.svd(np.array(rows), compute_uv=False)
    # dim S_1 from the jet matrix
    J = []
    for z in nodes:
        J.append([z[0] ** a * z[1] ** b for a, b in V])
        J.append([a * z[0] ** max(a - 1, 0) * z[1] ** b if a else 0.0 for a, b in V])
        J.append([b * z[0] ** a * z[1] ** max(b - 1, 0) if b else 0.0 for a, b in V])
    svJ = np.linalg.svd(np.array(J), compute_uv=False)
    dimS1 = len(V) - rank(svJ, 1e-11)
    # identity (a) at a non-measure functional
    rng = np.random.default_rng(7)
    monsn = exps(n)
    G0 = np.array([[mom[(a[0] + b[0], a[1] + b[1])] for b in monsn] for a in monsn])
    amp = 0.3 * np.linalg.eigvalsh(G0)[0] / len(monsn)     # keeps M_n(L) positive definite
    mom2 = dict(mom)
    for e in exps(2 * n + 1):
        mom2[e] += amp * rng.uniform(-1, 1)
    _, _, ps2 = sections(mom2, n)
    S2 = s_polys(n, ps2, lambda f: proj_L(mom2, ps2, f))
    K2 = kappa(mom2, n)
    err_a = max(abs(K2[a, b] - apply_L(mom2, S2[(a, b)][0])) for a, b in S2) / max(1e-300, np.max(np.abs(K2)))
    top2 = max(t for _, t in S2.values())
    print(f'{kind:6s} n={n}: N={N} dim V={len(V)} dim S_1={dimS1} (n(n+1)/2={n*(n+1)//2}); '
          f'max|s_ab jets at nodes|={jet_res:.1e}, max|deg-(2n+2) coeff|={top_res:.1e}')
    print(f'          FD d(kappa) vs formula E(s_ab): max rel diff = {rel:.2e} (h={h:g}); '
          f'rank d(kappa)={rank(svD)}, dim F={rank(svF)}; singular values of d(kappa): '
          + ' '.join(f'{s:.4g}' for s in svD))
    print(f'          identity (a) at non-measure L: max rel |kappa_ab - L(s_ab(L))| = {err_a:.2e}; '
          f'max|deg-(2n+2) coeff| = {top2:.1e}; max|kappa(L)| = {np.max(np.abs(K2)):.3e}')
    return rel, err_a


def main():
    print('numpy', np.__version__)
    worst = 0.0
    for kind, n in [('padua', 1), ('padua', 2), ('padua', 3), ('padua', 4), ('equi', 3), ('random', 3)]:
        rel, err_a = run(kind, n)
        worst = max(worst, rel, err_a)
    print(f'worst relative discrepancy = {worst:.2e}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
