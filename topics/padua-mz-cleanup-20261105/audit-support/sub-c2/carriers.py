#!/usr/bin/env python3
"""Auditor check (Claude subC2): odd-m y-mesh carriers of odd-carriers.md.
  p^-(x,y) = T_{M/2}(y) F_r(y) F_s(x),                       M=m+1, r=floor(a m), s=floor(b m)
  p^+(x,y) = [T_{M/2-r}(y) - T_{M/2+r}(y)] F_r(y) F_s(x)/2
Full signed energy Q_m(p^2) = sum_{j+k even} w_jk p(x_j,y_k)^2 with w from formula (3), via
  Q = 1/(m(m+1)) sum_{a+b<=R} t_a t_b (X_a Y_b + X'_a Y'_b)   (checkerboard split, DCT-I sums),
cross-checked against the direct node sum at moderate m.  Carrier values are computed from the
Chebyshev definitions cos(n arccos y), not from the sine-product identity."""
import numpy as np, sys
from scipy.fft import dct
sys.path.insert(0, '/tmp/claude-0/subC2')

def fejer(u, tt):
    tt = np.asarray(tt, dtype=float)
    out = np.empty_like(tt)
    z = np.abs(np.sin(tt / 2)) < 1e-300
    out[z] = u + 1
    nz = ~z
    out[nz] = (np.sin((u + 1) * tt[nz] / 2) / np.sin(tt[nz] / 2)) ** 2 / (u + 1)
    return out

def profiles(m, a, b, sign):
    M = m + 1
    r, s = int(np.floor(a * m)), int(np.floor(b * m))
    tx = np.pi * np.arange(m + 1) / m
    ty = np.pi * np.arange(M + 1) / M
    Bx = fejer(s, tx)
    if sign == '-':
        Ay = np.cos((M // 2) * ty) * fejer(r, ty)
        deg = M // 2 + r + s
    else:
        Ay = 0.5 * (np.cos((M // 2 - r) * ty) - np.cos((M // 2 + r) * ty)) * fejer(r, ty)
        deg = M // 2 + 2 * r + s
    return r, s, deg, Bx ** 2, Ay ** 2

def Q_dct(m, a, b, sign):
    assert m % 2 == 1
    R = m // 2
    r, s, deg, Bx2, Ay2 = profiles(m, a, b, sign)
    sx = (-1.0) ** np.arange(m + 1); sy = (-1.0) ** np.arange(m + 2)
    X = dct(Bx2, type=1)[0:2 * R + 1:2] / 2;  Xp = dct(sx * Bx2, type=1)[0:2 * R + 1:2] / 2
    Y = dct(Ay2, type=1)[0:2 * R + 1:2] / 2;  Yp = dct(sy * Ay2, type=1)[0:2 * R + 1:2] / 2
    aa = np.arange(R + 1)
    t = np.where(aa == 0, 2.0, -4.0 / (4.0 * aa * aa - 1.0))
    cY = np.cumsum(t * Y); cYp = np.cumsum(t * Yp)
    Q = np.sum(t * X * cY[R - aa]) + np.sum(t * Xp * cYp[R - aa])
    return Q / (m * (m + 1)), r, s, deg

def Q_direct(m, a, b, sign):
    from majorant import weights
    W, _, mask = weights(m)
    r, s, deg, Bx2, Ay2 = profiles(m, a, b, sign)
    return float(np.sum(np.where(mask, W * np.outer(Bx2, Ay2), 0.0)))

def D(u):
    return 1 + u * (2 * u + 1) / (3 * (u + 1))

def finite_identities(m, a, b):
    M = m + 1
    r, s = int(np.floor(a * m)), int(np.floor(b * m))
    eps = np.ones(m + 1); eps[[0, m]] = 0.5
    eta = np.ones(M + 1); eta[[0, M]] = 0.5
    _, _, _, Bx2, Am2 = profiles(m, a, b, '-')
    _, _, _, _, Ap2 = profiles(m, a, b, '+')
    U = Bx2 / m ** 2; Vm = Am2 / m ** 2; Vp = Ap2 / m ** 2
    k = np.arange(M + 1); j = np.arange(m + 1)
    d_r = D(r) / 2 - 1 / (2 * (r + 1) ** 2)
    return {
        'sum eps U - D_s/m': np.sum(eps * U) - D(s) / m,
        'alt sum eps U': np.sum(eps * (-1.0) ** j * U),
        'sum eta V- - M D_r/(2m^2)': np.sum(eta * Vm) - M * D(r) / (2 * m * m),
        'max |V-| on odd k': np.max(np.abs(Vm[k % 2 == 1])),
        'sum eta V+ - M d_r/(2m^2)': np.sum(eta * Vp) - M * d_r / (2 * m * m),
        'max |V+| on even k': np.max(np.abs(Vp[k % 2 == 0])),
        'scale D_s/m': D(s) / m, 'scale M D_r/(2m^2)': M * D(r) / (2 * m * m)}

if __name__ == '__main__':
    print('finite identities (8),(10) at odd m, (a,b)=(0.1,0.2):')
    for m in (101, 1001, 10001):
        print(' m=%d' % m, {kk: float('%.3e' % v) for kk, v in finite_identities(m, 0.1, 0.2).items()})
    print('cross-check DCT route vs direct node sum (weights from formula (3)):')
    for m in (101, 201, 301):
        for (a, b, sg) in ((0.2, 0.2, '-'), (0.1, 0.2, '+')):
            q1 = Q_dct(m, a, b, sg)[0]; q2 = Q_direct(m, a, b, sg)
            print(f' m={m} p{sg} a={a} b={b}: Q_dct={q1:+.12e} Q_direct={q2:+.12e} rel.diff={abs(q1-q2)/abs(q2):.1e}')
    cases = [(0.2, 0.2, '-'), (0.3, 0.1, '-'), (0.05, 0.4, '-'), (0.1, 0.2, '+'), (0.2, 0.05, '+'), (0.05, 0.3, '+')]
    ms = [1001, 10001, 100001, 1000001, 10000001]
    for (a, b, sg) in cases:
        pred = -16 * a * b / 9 if sg == '-' else 8 * a * b / 9
        prev = None; out = []
        first_ok = None
        for m in range(3, 4001, 2):
            r, s = int(np.floor(a * m)), int(np.floor(b * m))
            deg = (m + 1) // 2 + (r if sg == '-' else 2 * r) + s
            ok = deg <= m - 1 and (sg == '-' or r >= 1)
            if ok and first_ok is None: first_ok = m
            if not ok: first_ok = None
        for m in ms:
            Q, r, s, deg = Q_dct(m, a, b, sg)
            assert deg <= m - 1
            lg = np.log(m)
            item = f'm={m}: Q={Q:+.5f} Q/log m={Q/lg:+.5f}'
            if prev is not None:
                item += f' slope={(Q-prev[0])/(lg-prev[1]):+.6f}'
            out.append(item); prev = (Q, lg)
        print(f'p{sg} a={a} b={b}: predicted {pred:+.6f}; degree<=m-1 for all odd m>={first_ok} (scanned to 3999)')
        for it in out: print('   ', it)
