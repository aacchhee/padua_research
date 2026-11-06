#!/usr/bin/env python3
"""High-precision finite-epsilon check of the actual perturbed normalized
algorithm (no derivative formulas): ||(I-P_s)P_s(eps;f)||_2/eps at eps=1e-30
with 90 digits, for the lower witness source and random sources, compared
with the frozen closed-form normal output (formula (6) / mirror)."""
import math, random, sys, json
import mpmath as mp

mp.mp.dps = 90
random.seed(7)


def padua(m):
    lam = lambda j, r: mp.mpf(1) / (2 * r) if j in (0, r) else mp.mpf(1) / r
    P = []
    for j in range(m + 1):
        for k in range(m + 2):
            if (j + k) % 2 == 0:
                P.append((j, k, mp.cos(j * mp.pi / m), mp.cos(k * mp.pi / (m + 1)), 2 * lam(j, m) * lam(k, m + 1)))
    return P


def order(s):
    return [(d - b, b) for d in range(s + 1) for b in range(d + 1)]


def parent(rule, a, b):
    if rule == 'BJ':
        return ('X', (a - 1, b)) if b == 0 else ('Y', (a, b - 1))
    return ('X', (a - 1, b)) if a > 0 else ('Y', (a, b - 1))


def run(m, s, rule, f, eps):
    P = padua(m); M = len(P)
    X = [p[2] for p in P]; Y = [p[3] for p in P]; sw = [mp.sqrt(p[4]) for p in P]
    idx = order(s); loc = {ab: h for h, ab in enumerate(idx)}
    Q = [sw[:]]
    sig = [None]
    for h in range(1, len(idx)):
        op, p = parent(rule, *idx[h])
        A = X if op == 'X' else Y
        a = [A[i] * Q[loc[p]][i] for i in range(M)]
        sig.append(mp.sqrt(mp.fsum(t * t for t in a)))
        if f is not None and idx[h] in f:
            a = [a[i] + eps * f[idx[h]][i] for i in range(M)]
        for _ in range(2):
            for q in Q:
                c = mp.fsum(q[i] * a[i] for i in range(M))
                a = [a[i] - c * q[i] for i in range(M)]
        nr = mp.sqrt(mp.fsum(t * t for t in a))
        Q.append([t / nr for t in a])
    return P, Q, sig, idx, loc


def poly_projector_normal(P, s):
    # orthonormal basis of represented Pi_s via exact unperturbed q_ab = p_a(x)p_b(y)
    def p(l, z):
        return mp.mpf(1) if l == 0 else mp.sqrt(2) * mp.cos(l * mp.acos(z))
    B = [[mp.sqrt(w) * p(a, x) * p(b, y) for (_, _, x, y, w) in P] for (a, b) in order(s)]
    return B


def normal_part(B, v):
    out = v[:]
    for b in B:
        c = mp.fsum(bi * vi for bi, vi in zip(b, out))
        out = [o - c * bi for o, bi in zip(out, b)]
    return out


def spectral(cols):
    Mx = mp.matrix(len(cols[0]), len(cols))
    for j, c in enumerate(cols):
        for i, v in enumerate(c):
            Mx[i, j] = v
    S = mp.svd_r(Mx, compute_uv=False)
    return max(S)


def main():
    rows = []
    eps = mp.mpf('1e-30')
    for (m, s) in [(2, 1), (3, 2), (4, 3), (4, 2), (5, 4)]:
        for rule in ('BJ', 'mirror'):
            P, Q0, sig, idx, loc = run(m, s, rule, None, 0)
            M = len(P)
            B = poly_projector_normal(P, s)
            # check base equals polynomial q_ab (span check: base columns orthonormal and equal B)
            base_err = max(abs(Q0[h][i] - B[h][i]) for h in range(len(idx)) for i in range(M))
            for kind in ('witness', 'random'):
                if kind == 'witness':
                    e = [mp.sqrt(p[4]) * (-1) ** p[0] for p in P]
                    f = {(1, 0): [t / mp.sqrt(2) for t in e]}
                else:
                    f = {ab: [mp.mpf(random.gauss(0, 1)) for _ in range(M)] for ab in idx[1:]}
                    nrm = mp.sqrt(mp.fsum(mp.fsum(t * t for t in f[ab]) / sig[loc[ab]] ** 2 for ab in f))
                    f = {ab: [t / nrm for t in f[ab]] for ab in f}
                _, Qe, _, _, _ = run(m, s, rule, f, eps)
                cols = [normal_part(B, q) for q in Qe]
                fd = spectral(cols) / eps
                # closed form frozen V
                X = [p[2] for p in P]; Y = [p[3] for p in P]
                def U(l, z):
                    a, b = mp.mpf(1), 2 * z
                    if l == 0: return a
                    for _ in range(l - 1): a, b = b, 2 * z * b - a
                    return b
                pp = lambda l, z: mp.mpf(1) if l == 0 else mp.sqrt(2) * mp.cos(l * mp.acos(z))
                K = lambda a, c, z: mp.sqrt(2) * U(a - 1, z) if c == 1 else 2 * U(a - c, z)
                F = lambda ab: f.get(ab, [mp.mpf(0)] * M)
                V = []
                for (a, b) in idx[1:]:
                    if rule == 'BJ':
                        v = [mp.fsum(K(a, c, X[i]) * F((c, 0))[i] for c in range(1, a + 1)) * pp(b, Y[i])
                             + mp.fsum(K(b, d, Y[i]) * F((a, d))[i] for d in range(1, b + 1)) for i in range(M)]
                    else:
                        v = [mp.fsum(K(b, d, Y[i]) * F((0, d))[i] for d in range(1, b + 1)) * pp(a, X[i])
                             + mp.fsum(K(a, c, X[i]) * F((c, b))[i] for c in range(1, a + 1)) for i in range(M)]
                    V.append(normal_part(B, v))
                cf = spectral(V)
                row = dict(m=m, s=s, rule=rule, kind=kind, base_err=float(base_err), fd=float(fd), closed=float(cf),
                           rel=float(abs(fd - cf) / cf), lower=math.sqrt(math.ceil(s / 2)))
                row['witness_ok'] = (kind != 'witness') or bool(fd > mp.sqrt(math.ceil(s / 2)) - mp.mpf('1e-20'))
                row['rel_ok'] = bool(row['rel'] < 1e-20 and base_err < mp.mpf('1e-80'))
                rows.append(row)
                print(json.dumps(row), flush=True)
    json.dump(rows, open(sys.argv[1], 'w'), indent=1)
    assert all(r['witness_ok'] and r['rel_ok'] for r in rows); print('ALL PASS')


if __name__ == '__main__':
    main()
