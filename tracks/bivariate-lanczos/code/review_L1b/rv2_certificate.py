"""Independent exact rerun of the PD-T?bivariate-lanczos-claude-113 certificate (L1 reconstruction 02).

Written from the statement of PD-T?...-113 and PD-T?...-101/-104 only; it does not import or copy the developer's
checker (code/L1/l1_r05_exact_certificate.py) or l1_recurrence.py.

Quantity (PD-T?...-113 part 2): G(n) = max over impulse columns s of degree 2, columns k of degree n with k > s,
and nodes z_i, of ((L*(z_i))^{-1})_{k,s}^2, where L*(z) is the exact orthonormal node propagator of the dev-rule
window recurrence ((t,0) = X (t-1,0); (t,j) = Y (t-1,j-1)), coordinates rescaled to [-1,1] (factor c = 2/m).

Route (all exact rationals, integer node coordinates, unit weights; rescaling applied at the end by the factor
(m/2)^2, which part 1's scaling rule predicts and which is re-verified directly for T_24):
  A. monic graded basis psi_k by FULL Gram-Schmidt of the dev-rule products A_k psi_{p(k)} against all previous
     vectors (no window tables); the off-window coefficients are checked to be exactly zero;
  B. the same basis independently from an exact LDL^T factorisation of the monomial moment matrix
     (psi = L^{-1} m, D_k = <psi_k, psi_k>); psi node values and D_k compared exactly with A;
  C. exact orthogonality of all pairs;
  D. entries via the impulse identity  ((L*)^{-1})_{k,s}^2 = D_{p(s)} g_k^2 / D_k  with the monic impulse response
     g (g_s = 1, g_k = a_k g_{p(k)} - sum_l alpha_{k,l} g_l);
  E. part 1 (the identity) checked numerically: the orthonormal L*(z) is built in mpmath (60 digits) from the exact
     data (beta_k = sqrt(D_k/D_p), h_l = alpha_l sqrt(D_l/D_p)) and inverted at selected nodes.
Usage: python3 -I -u rv2_certificate.py <triangle|square|rotsquare> <m> <nmax> [rescaled]
"""
import sys, time, math
from fractions import Fraction as Fr


def cols(nmax):
    idx = [(t, j) for t in range(nmax + 1) for j in range(t + 1)]
    return idx, {k: i for i, k in enumerate(idx)}


def dev_rule(t, j):
    return ('X', (t - 1, 0)) if j == 0 else ('Y', (t - 1, j - 1))


def exact_window(op, t, j, pos):
    W = []
    if t >= 2:
        i0 = j if op == 'X' else max(j - 2, 0)
        W += [pos[(t - 2, i)] for i in range(i0, t - 1)]
    W += [pos[(t - 1, i)] for i in range(t)]
    W += [pos[(t, r)] for r in range(j)]
    return W


def nodes(kind, m, rescaled=False):
    if kind == 'triangle':
        P = [(i, j) for i in range(m + 1) for j in range(m + 1 - i)]
    elif kind == 'square':
        P = [(i, j) for i in range(m + 1) for j in range(m + 1)]
    elif kind == 'rotsquare':      # Q_m rotated by (cos, sin) = (3/5, 4/5), scaled by 5: (3i - 4j, 4i + 3j)
        P = [(3 * i - 4 * j, 4 * i + 3 * j) for i in range(m + 1) for j in range(m + 1)]
    else:
        raise ValueError(kind)
    if rescaled:
        c = Fr(2, m)
        P = [(c * Fr(a) - 1, c * Fr(b) - 1) for a, b in P]
    else:
        P = [(Fr(a), Fr(b)) for a, b in P]
    return P


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def method_A(P, nmax):
    idx, pos = cols(nmax)
    xs = [p[0] for p in P]; ys = [p[1] for p in P]
    psi = [[Fr(1)] * len(P)]
    D = [dot(psi[0], psi[0])]
    alpha = [None]
    offwin = 0
    for k in range(1, len(idx)):
        t, j = idx[k]
        op, par = dev_rule(t, j)
        p = pos[par]
        a = [(x if op == 'X' else y) * v for x, y, v in zip(xs, ys, psi[p])]
        al = {}
        r = list(a)
        for l in range(k):
            c = dot(a, psi[l]) / D[l]
            if c != 0:
                al[l] = c
                r = [ri - c * vi for ri, vi in zip(r, psi[l])]
        Wex = set(exact_window(op, t, j, pos))
        offwin += sum(1 for l in al if l not in Wex)
        psi.append(r); D.append(dot(r, r)); alpha.append(al)
    return idx, pos, psi, D, alpha, offwin


def method_B(P, nmax):
    """monic graded basis from the exact LDL^T factorisation of the moment matrix"""
    idx, pos = cols(nmax)
    mon = [[x ** (t - j) * y ** j for (x, y) in P] for (t, j) in idx]
    N = len(idx)
    G = [[dot(mon[a], mon[b]) for b in range(N)] for a in range(N)]
    L = [[Fr(0)] * N for _ in range(N)]
    D = [Fr(0)] * N
    for k in range(N):
        D[k] = G[k][k] - sum(L[k][j] * L[k][j] * D[j] for j in range(k))
        for i in range(k + 1, N):
            L[i][k] = (G[i][k] - sum(L[i][j] * L[k][j] * D[j] for j in range(k))) / D[k]
    psi = []
    for k in range(N):
        v = list(mon[k])
        for j in range(k):
            if L[k][j] != 0:
                v = [vi - L[k][j] * wj for vi, wj in zip(v, psi[j])]
        psi.append(v)
    return psi, D


def log10_fr(q):
    if q == 0:
        return float('-inf')
    return math.log10(q.numerator) - math.log10(q.denominator)


def certificate(P, idx, pos, psi, D, alpha, nmax):
    xs = [p[0] for p in P]; ys = [p[1] for p in P]
    M = len(P)
    best = {}
    imp = [pos[(2, j)] for j in range(3)]
    for s in imp:
        ps = pos[dev_rule(*idx[s])[1]]
        g = {s: [Fr(1)] * M}
        for k in range(s + 1, len(idx)):
            t, j = idx[k]
            op, par = dev_rule(t, j)
            p = pos[par]
            a = xs if op == 'X' else ys
            gp = g.get(p)
            v = [ai * gi for ai, gi in zip(a, gp)] if gp is not None else [Fr(0)] * M
            for l, c in alpha[k].items():
                if l in g:
                    v = [vi - c * gi for vi, gi in zip(v, g[l])]
            g[k] = v
            n = t
            ent = max(gi * gi for gi in v) * D[ps] / D[k]
            if n not in best or ent > best[n][0]:
                best[n] = (ent, idx[s], idx[k])
    return best


def mp_identity_check(P, idx, pos, D, alpha, node_ids, nmax):
    import mpmath as mp
    mp.mp.dps = 60
    N = len(idx)
    worst = mp.mpf(0)
    for i in node_ids:
        x, y = P[i]
        Lm = mp.zeros(N, N); Lm[0, 0] = 1
        for k in range(1, N):
            t, j = idx[k]
            op, par = dev_rule(t, j)
            p = pos[par]
            Lm[k, k] = mp.sqrt(mp.mpf(D[k].numerator) / D[k].denominator / (mp.mpf(D[p].numerator) / D[p].denominator))
            for l, c in alpha[k].items():
                Lm[k, l] += mp.mpf(c.numerator) / c.denominator * mp.sqrt((mp.mpf(D[l].numerator) / D[l].denominator) / (mp.mpf(D[p].numerator) / D[p].denominator))
            Lm[k, p] -= mp.mpf((x if op == 'X' else y).numerator) / (x if op == 'X' else y).denominator
        for s in [pos[(2, j)] for j in range(3)]:
            ps = pos[dev_rule(*idx[s])[1]]
            e = mp.zeros(N, 1); e[s] = 1
            gam = mp.lu_solve(Lm, e)
            # exact monic impulse response at this node
            g = {s: Fr(1)}
            for k in range(s + 1, N):
                t, j = idx[k]
                op, par = dev_rule(t, j)
                p = pos[par]
                a = x if op == 'X' else y
                v = a * g.get(p, Fr(0)) - sum(c * g.get(l, Fr(0)) for l, c in alpha[k].items())
                g[k] = v
            for k in range(s, N):
                exact = Fr(D[ps]) * g[k] * g[k] / D[k]
                num = gam[k] ** 2
                ex = mp.mpf(exact.numerator) / exact.denominator
                if ex != 0:
                    worst = max(worst, abs(num - ex) / ex)
                else:
                    worst = max(worst, abs(num))
    return worst


def main():
    kind, m, nmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    rescaled = len(sys.argv) > 4 and sys.argv[4] == 'rescaled'
    t0 = time.time()
    P = nodes(kind, m, rescaled)
    print(f'# rv2_certificate {kind} m={m} M={len(P)} nmax={nmax} coordinates={"rescaled [-1,1]" if rescaled else "integer"} python {sys.version.split()[0]}')
    idx, pos, psi, D, alpha, offwin = method_A(P, nmax)
    print(f'# A (full exact Gram-Schmidt, dev products): {time.time() - t0:.1f}s; nonzero coefficients outside the exact window: {offwin}')
    nz = 0
    for k in range(len(idx)):
        for l in range(k):
            if dot(psi[k], psi[l]) != 0:
                nz += 1
    print(f'# C exact orthogonality: nonzero inner products among {len(idx) * (len(idx) - 1) // 2} pairs: {nz}')
    if kind != 'rotsquare' and len(idx) <= 91 and m <= 24:
        t1 = time.time()
        psiB, DB = method_B(P, nmax)
        same = all(a == b for va, vb in zip(psi, psiB) for a, b in zip(va, vb)) and all(a == b for a, b in zip(D, DB))
        print(f'# B (moment-matrix LDL^T) agrees exactly with A (node values and D_k): {same} ({time.time() - t1:.1f}s)')
    best = certificate(P, idx, pos, psi, D, alpha, nmax)
    scale = 0.0 if rescaled else 2 * math.log10(m / 2) + (2 * math.log10(5) if kind == 'rotsquare' else 0.0)   # rotated grid is 5x scaled: c = 2/(5m)
    print('# G(n) in rescaled coordinates: log10 G_int(n) + 2 log10(m/2)' + (' + 2 log10 5 (rotated grid is 5x scaled)' if kind == 'rotsquare' else '') if not rescaled else '# G(n) computed directly in rescaled coordinates')
    for n in sorted(best):
        ent, s, k = best[n]
        print(f'   n={n:2d}: log10 G = {log10_fr(ent) + scale:8.3f}   (s={s}, k={k}; exact rational with {ent.numerator.bit_length()}/{ent.denominator.bit_length()} bits)')
    if 6 in best and 12 in best:
        print(f'# criterion: log10 G(12) - log10 G(6) = {log10_fr(best[12][0]) - log10_fr(best[6][0]):.3f}  (triangle: >= 6 required; square: <= 2 required)')
        r = best[12][0] / best[6][0]
        print(f'# exact rational comparisons (scale-free): G(12) >= 10^6 G(6): {r >= 10**6};  G(12) <= 10^2 G(6): {r <= 100};  G(12) >= 10^3 G(6): {r >= 10**3};  G(12) > 10^4 G(6): {r > 10**4}')
    if len(sys.argv) > 5 and sys.argv[5] == 'mp':
        ids = [0, len(P) // 2, len(P) - 1]
        w = mp_identity_check(P, idx, pos, D, alpha, ids, nmax)
        print(f'# E part-1 identity, mpmath 60 digits at nodes {ids}: max relative deviation = {float(w):.2e}')
    print(f'# total {time.time() - t0:.1f}s')


if __name__ == '__main__':
    main()
