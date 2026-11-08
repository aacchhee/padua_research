#!/usr/bin/env python3
"""F03-identities-support (1)-(8) and H (3): numerical corroboration from the
Padua cardinal formula (MEASURED, finite n only).  mpmath, dps=30.

Nodes (cos(j pi/n), cos(k pi/m)), m=n+1, j+k even (first family).
L_xi(x) = w_xi [K_n(xi,x) - T_n(xi_1) T_n(x_1)],
K_n(x,y) = sum_{i+k<=n} That_i(x1)That_k(x2)That_i(y1)That_k(y2), That_0=1, That_p=sqrt2 T_p,
w_xi = 1/(n m) * {1/2 vertex, 1 edge, 2 interior}.
"""
import sys
import mpmath as mp

mp.mp.dps = 30
pi = mp.pi


def nodes(n):
    m = n + 1
    out = []
    for j in range(n + 1):
        for k in range(m + 1):
            if (j + k) % 2 == 0:
                vert = (j in (0, n)) and (k in (0, m))
                edge = (j in (0, n)) or (k in (0, m))
                w = mp.mpf(1) / (2 * n * m) if vert else (mp.mpf(1) / (n * m) if edge else mp.mpf(2) / (n * m))
                out.append((j, k, w))
    return out


def card(n, j, k, w, X1, X2):
    """L_{(j,k)}(X) with X = (cos X1, cos X2) given as angles."""
    m = n + 1
    th, ph = j * pi / n, k * pi / m
    ci = [mp.cos(i * th) * mp.cos(i * X1) * (1 if i == 0 else 2) for i in range(n + 1)]
    ck = [mp.cos(i * ph) * mp.cos(i * X2) * (1 if i == 0 else 2) for i in range(n + 1)]
    Ksum = mp.fsum(ci[i] * ck[q] for i in range(n + 1) for q in range(n + 1 - i))
    return w * (Ksum - mp.cos(n * th) * mp.cos(n * X1))


def B(x):
    return mp.cot(pi * x) - 1 / (pi * x) + 1 / (pi * (1 - x))


def Hr(r, a):
    return mp.fsum(1 / (l + a) for l in range(r))


def run(n, cardinal_check=False):
    m = n + 1
    res = {}
    nd = nodes(n)
    assert len(nd) == (n + 1) * (n + 2) // 2
    if cardinal_check:
        err = 0
        for (j, k, w) in nd:
            for (j2, k2, _) in nd:
                v = card(n, j, k, w, j2 * pi / n, k2 * pi / m)
                err = max(err, abs(v - (1 if (j, k) == (j2, k2) else 0)))
        res['cardinal_err'] = err
    # corner (-1,-1): angles (pi, pi)
    rowsum = {}
    for (j, k, w) in nd:
        Lval = card(n, j, k, w, pi, pi)
        rowsum[k] = rowsum.get(k, 0) + abs(Lval)
    lam = mp.fsum(rowsum.values())
    res['Lambda_c'] = lam
    # F03 objects
    P, R, Z, Tn, Sgn = {}, {}, {}, {}, {}
    worst = {'pos_set': 0, 'R=2P-n': 0, 'signed=n': 0, 'P=wT': 0, 'cotsum': 0, '(7)': 0}
    V = 0
    Hcal = 0
    for r in range(1, n + 1):
        v = r * pi / m
        F = lambda u: (1 + mp.cos(v)) / (mp.cos(u) - mp.cos(v))
        js = [j for j in range(-n + 1, n + 1) if (j - (1 - r)) % 2 == 0]   # n residues mod 2n
        assert len(js) == n
        vals = {j: F(j * pi / n) for j in js}
        pos = sorted(j for j in js if vals[j] > 0)
        expect = list(range(-r + 1, r, 2))
        worst['pos_set'] = max(worst['pos_set'], 0 if pos == expect else 1)
        P[r] = mp.fsum(vals[j] for j in pos)
        R[r] = mp.fsum(abs(x) for x in vals.values())
        worst['R=2P-n'] = max(worst['R=2P-n'], abs(R[r] - (2 * P[r] - n)))
        worst['signed=n'] = max(worst['signed=n'], abs(mp.fsum(vals.values()) - n))
        a = (1 - mp.mpf(r) / m) / 2
        wr = mp.cot(pi * r / (2 * m))
        T = mp.fsum(mp.cot(pi * (l + a) / n) for l in range(r))
        Tn[r] = T
        worst['P=wT'] = max(worst['P=wT'], abs(P[r] - wr * T))
        full = mp.fsum(mp.cot(pi * (l + a) / n) for l in range(n))
        worst['cotsum'] = max(worst['cotsum'], abs(full - n * mp.tan(v / 2)))
        Bs = mp.fsum(B((l + a) / n) for l in range(r))
        D = Hr(r, a) - Hr(r, n - r + 1 - a)
        worst['(7)'] = max(worst['(7)'], abs(T - (n / pi * D + Bs)))
        Z[r] = P[r] - n
        V += wr * Bs
        Hcal += wr * D
        # per-row correspondence with the cardinal sum: row k = m - r carries (2/(nm)) R_r
        k = m - r
        res.setdefault('row_err', 0)
        res['row_err'] = max(res['row_err'], abs(rowsum[k] - 2 * R[r] / (n * m)))
    Hcal = 4 / (pi * m) * Hcal
    res.update(worst)
    res['row_k=n+1 (R_0=n^2 -> n/m)'] = abs(rowsum[m] - mp.mpf(n) / m)
    res['row_k=0 (R_m=n -> 1/m)'] = abs(rowsum[0] - mp.mpf(1) / m)
    res['(3)'] = abs(lam - (1 - 2 * mp.mpf(n) / m + 4 / mp.mpf(n * m) * mp.fsum(P.values())))
    res['(6)'] = abs(lam - (1 + 2 * mp.mpf(n) / m + 4 / mp.mpf(n * m) * mp.fsum(Z.values())))
    res['Z_r>0 (r<n)'] = min(Z[r] for r in range(1, n)) if n > 1 else mp.mpf(1)
    res['|Z_n|'] = abs(Z[n])
    res['H(3)'] = abs(lam - (-1 + mp.mpf(2) / m + Hcal + 4 * V / (n * m)))
    return res


def main():
    ns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 20, 21, 31, 32]
    allok = True
    for n in ns:
        r = run(n, cardinal_check=(n <= 7))
        line = ['n=%d' % n, 'Lambda_c=%s' % mp.nstr(r['Lambda_c'], 18)]
        for kk in ('cardinal_err', 'row_err', 'row_k=n+1 (R_0=n^2 -> n/m)', 'row_k=0 (R_m=n -> 1/m)',
                   'pos_set', 'R=2P-n', 'signed=n', 'P=wT', 'cotsum', '(7)', '(3)', '(6)', '|Z_n|', 'H(3)'):
            if kk in r:
                line.append('%s:%s' % (kk, mp.nstr(r[kk], 3)))
                if kk != 'pos_set' and r[kk] > mp.mpf(10) ** -20:
                    allok = False
                if kk == 'pos_set' and r[kk] != 0:
                    allok = False
        line.append('minZ(r<n):%s' % mp.nstr(r['Z_r>0 (r<n)'], 5))
        if r['Z_r>0 (r<n)'] <= 0:
            allok = False
        print(' | '.join(line))
    print('ALL_PASS' if allok else 'SOME_FAIL')
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
