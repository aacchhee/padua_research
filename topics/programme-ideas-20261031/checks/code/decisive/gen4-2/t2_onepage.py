"""Decisive test gen4-2, T2: is Paper A (corner expansion) a one-page product of 1-D expansions?
(a) closed form of the corner value as an O(N) sum of rhombus-kernel values (checked against the O(Nn) formula);
(b) long-double (80-bit) evaluation with exact mod-4 reduction of the sine arguments, cross-checked with mpmath (30 digits);
(c) Euler-Maclaurin least-squares fits -> b, c, kappa = c - c1^2 with an uncertainty from the spread over models;
(d) identification of kappa against 1-D constants (three pre-registered tiers) with PSLQ, plus a list of natural candidates.
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.
"""
import sys, time, itertools
import numpy as np
import mpmath as mp
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2')
from leb_common import corner_value, corner_max

T0 = time.time()
LD = np.longdouble
PI_LD = LD('3.14159265358979323846264338327950288')


def sin_q(q, eps):
    """sin(q*pi/2 + eps) for integer array q and (long double) eps, with exact reduction of the quarter turns."""
    r = np.mod(q, 4)
    s = np.sin(eps); c = np.cos(eps)
    return np.where(r == 0, s, np.where(r == 1, c, np.where(r == 2, -s, -c)))


def corner_closed(n, corner=(1, -1), dtype=LD, chunk_rows=64):
    """Lambda at the corner (sx, sy) via K(c,B) = D^rh_n(th_c + th_j, ph_c + ph_k),
    D^rh_n(u,v) = U_{n+1}(S)U_{n+1}(T) + U_n(S)U_n(T), U_m(x) = sin(m x)/sin(x), S = (u+v)/2, T = (v-u)/2,
    with the quarter-turn parts of m*S, m*T reduced exactly in integer arithmetic. Pairwise summation in `dtype`."""
    sx, sy = corner
    pi = PI_LD if dtype == LD else np.float64(np.pi)
    jc = 0 if sx == 1 else 2 * n            # th_c = jc * pi/(2n) ∈ {0, pi}
    kc = 0 if sy == 1 else 2 * (n + 1)      # ph_c = kc * pi/(2(n+1))
    Tn_c = 1.0 if sx == 1 else (-1.0) ** n
    k = np.arange(n + 2)
    ek = np.where((k == 0) | (k == n + 1), 0.5, 1.0).astype(dtype)
    tot = dtype(0)
    for j0 in range(0, n + 1, chunk_rows):
        j = np.arange(j0, min(n + 1, j0 + chunk_rows))
        J, K = np.meshgrid(j, k, indexing='ij')
        msk = ((J + K) % 2 == 0)
        J = J[msk]; K = K[msk]
        # u = (jc + 2j) pi/(2n) ; v = (kc + 2k) pi/(2(n+1)) ; S = (u+v)/2, T = (v-u)/2
        a = (jc + 2 * J).astype(np.int64); b = (kc + 2 * K).astype(np.int64)         # u = a pi/(2n), v = b pi/(2(n+1))
        # m*S = (m a/(2n) + m b/(2(n+1))) pi/2 ; for m = n:   a/2 + b/2 - b/(2(n+1))      -> q = a + b (half turns... see below)
        # Work in units of pi/4: m*S = [m a/n + m b/(n+1)] pi/4.
        #   m = n:   n a/n + n b/(n+1)         = a + b - b/(n+1)
        #   m = n+1: (n+1) a/n + b              = a + b + a/n
        #   m*T = [m b/(n+1) - m a/n] pi/4:  m = n: b - b/(n+1) - a ; m = n+1: b - a - a/n
        # quarter turns of pi/2 = 2 units of pi/4: q = floor(units/2), eps = (units - 2q) pi/4 ; we keep the integer part exact.
        A = a.astype(dtype); Bv = b.astype(dtype)
        def u_pair(int_part, frac):          # value = (int_part + frac) * pi/4, int_part integer array, frac in (-1,1) dtype
            q, rem = np.divmod(int_part, 2)
            return q, (rem.astype(dtype) + frac) * (pi / 4)
        qS_n, eS_n = u_pair(a + b, -Bv / (n + 1))
        qS_n1, eS_n1 = u_pair(a + b, A / n)
        qT_n, eT_n = u_pair(b - a, -Bv / (n + 1))
        qT_n1, eT_n1 = u_pair(b - a, -A / n)
        S = (A / n + Bv / (n + 1)) * (pi / 4); T = (Bv / (n + 1) - A / n) * (pi / 4)
        sS = np.sin(S); sT = np.sin(T)
        def U(num_sin, m, x, sx_):
            ok = np.abs(sx_) > dtype(1e-15)
            lim = m * np.cos(m * x) / np.cos(x)
            return np.where(ok, num_sin / np.where(ok, sx_, dtype(1)), lim)
        Un1S = U(sin_q(qS_n1, eS_n1), n + 1, S, sS); Un1T = U(sin_q(qT_n1, eT_n1), n + 1, T, sT)
        UnS = U(sin_q(qS_n, eS_n), n, S, sS); UnT = U(sin_q(qT_n, eT_n), n, T, sT)
        Krh = Un1S * Un1T + UnS * UnT
        ej = np.where((J == 0) | (J == n), 0.5, 1.0).astype(dtype)
        w = dtype(2) * ej * ek[K] / dtype(n * (n + 1))
        tot = tot + np.sum(np.abs(w * (Krh - dtype(Tn_c) * ((-1.0) ** J).astype(dtype))))
    return tot


def corner_mp(n, corner=(1, -1), dps=30):
    """Same sum in mpmath (reference)."""
    mp.mp.dps = dps
    sx, sy = corner
    thc = mp.mpf(0) if sx == 1 else mp.pi; phc = mp.mpf(0) if sy == 1 else mp.pi
    Tn_c = 1 if sx == 1 else (-1) ** n
    tot = mp.mpf(0)
    def U(m, x):
        sx_ = mp.sin(x)
        return mp.sin(m * x) / sx_ if abs(sx_) > mp.mpf(10) ** (-dps + 5) else m * mp.cos(m * x) / mp.cos(x)
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2:
                continue
            u = thc + j * mp.pi / n; v = phc + k * mp.pi / (n + 1)
            S = (u + v) / 2; T = (v - u) / 2
            Krh = U(n + 1, S) * U(n + 1, T) + U(n, S) * U(n, T)
            ej = mp.mpf(1) / 2 if j in (0, n) else 1; ek = mp.mpf(1) / 2 if k in (0, n + 1) else 1
            w = 2 * ej * ek / (n * (n + 1))
            tot += abs(w * (Krh - Tn_c * (-1) ** j))
    return tot


def em_fit(ns, vals, K, b_fixed=None, dps=40):
    """Least squares in mpmath for y = Lambda - (4/pi^2) log^2 n = b log n + c + sum_{k<=K} sum_{m<=k} d_km log^m n / n^k."""
    mp.mp.dps = dps
    a = 4 / mp.pi ** 2
    rows = []; rhs = []
    for n, v in zip(ns, vals):
        L = mp.log(n); y = mp.mpf(v) - a * L ** 2
        cols = [] if b_fixed is not None else [L]
        if b_fixed is not None:
            y -= b_fixed * L
        cols.append(mp.mpf(1))
        for k in range(1, K + 1):
            for m in range(0, k + 1):
                cols.append(L ** m / mp.mpf(n) ** k)
        rows.append(cols); rhs.append(y)
    A = mp.matrix(rows); yv = mp.matrix(rhs)
    x, res = mp.qr_solve(A, yv)
    r = A * x - yv
    maxres = max(abs(ri) for ri in r)
    if b_fixed is None:
        return x[0], x[1], maxres, x
    return b_fixed, x[0], maxres, x


if __name__ == '__main__':
    out = []
    P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
    c1 = (2 / np.pi) * (np.euler_gamma + np.log(8 / np.pi))
    P('=== (a) closed form (O(N) rhombus-kernel sum) vs O(Nn) formula, n = 3..64, both corners of each parity ===')
    worst = 0.0
    for n in range(3, 65):
        for corner in ((1, -1), (-1, -1), (-1, 1), (1, 1)):
            v1 = corner_value(n, *corner); v2 = float(corner_closed(n, corner, dtype=np.float64))
            worst = max(worst, abs(v1 - v2))
    P(f'max |closed - O(Nn)| over n = 3..64 and all four corners: {worst:.2e}   [{time.time()-T0:.0f}s]')
    P('=== (b) long-double closed form vs mpmath (30 digits) at n = 64, 128, 256 (corner (1,-1)) ===')
    for n in (64, 128, 256):
        t = time.time(); vm = corner_mp(n); tm = time.time() - t
        vl = corner_closed(n)
        P(f'n={n}: mp = {mp.nstr(vm, 25)}  longdouble = {np.format_float_positional(vl, precision=22)}  diff = {float(abs(mp.mpf(str(vl)) - vm)):.1e}  (mp {tm:.1f}s)')
    P('=== (b) long-double corner values ===')
    even = [64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384, 448, 512, 640, 768, 896, 1024, 1280, 1536, 1792, 2048, 2560, 3072, 3584, 4096, 5120, 6144, 8192]
    odd = [65, 127, 129, 255, 257, 511, 513, 1023, 1025, 2049, 4097]
    vals = {}
    for n in even + odd:
        t = time.time()
        corner = (1, -1) if n % 2 == 0 else (-1, -1)
        vals[n] = corner_closed(n, corner)
        P(f'n={n} corner {corner} Lambda_c = {np.format_float_positional(vals[n], precision=19)}  [{time.time()-t:.1f}s]')
    P('=== (c) Euler-Maclaurin fits: y = Lambda_c - (4/pi^2) log^2 n = b log n + c + sum_{k<=K, m<=k} d_km log^m n / n^k ===')
    mp.mp.dps = 40
    b_th = 8 / mp.pi ** 2 * (mp.euler + mp.log(8 / mp.pi))
    c1m = 2 / mp.pi * (mp.euler + mp.log(8 / mp.pi))
    P(f'1-D constants: c1 = (2/pi)(gamma + log(8/pi)) = {mp.nstr(c1m, 15)} ; b_theory = (8/pi^2)(gamma+log(8/pi)) = {mp.nstr(b_th, 15)} ; c1^2 = {mp.nstr(c1m**2, 15)}')
    results = []
    P('parity | K | n_min | #pts | b | c | max resid')
    for parity, nset in (('even', even), ('odd', odd)):
        for K in (3, 4, 5):
            for nmin in ((64, 128, 256, 512) if parity == 'even' else (65, 127, 255)):
                ns = [n for n in nset if n >= nmin]
                npar = 2 + K * (K + 3) // 2
                if len(ns) < npar + 2:
                    continue
                vs = [np.format_float_positional(vals[n], precision=19) for n in ns]
                for bfix in (None, b_th):
                    try:
                        b, c, res, x = em_fit(ns, vs, K, b_fixed=bfix, dps=60)
                    except ValueError as ex:
                        P(f"{parity} | {K} | {nmin} | {len(ns)} | {'fixed' if bfix is not None else 'free'} | fit failed: {ex}")
                        continue
                    results.append((parity, K, nmin, len(ns), bfix is not None, b, c, res))
                    P(f"{parity} | {K} | {nmin} | {len(ns)} | {'fixed ' if bfix is not None else ''}{mp.nstr(b, 13)} | {mp.nstr(c, 13)} | {mp.nstr(res, 3)}")
    # consensus: even-n fits with K >= 4, nmin >= 128, resid < 1e-12 (fallback: all K>=4)
    good = [r for r in results if r[0] == 'even' and r[1] >= 4 and r[2] >= 128 and r[7] < mp.mpf('1e-12')]
    if len(good) < 3:
        good = [r for r in results if r[0] == 'even' and r[1] >= 4]
    cs = [r[6] for r in good]; bs = [r[5] for r in good if not r[4]]
    c_mid = (max(cs) + min(cs)) / 2; c_unc = (max(cs) - min(cs)) / 2 + 10 * max(r[7] for r in good)
    b_mid = (max(bs) + min(bs)) / 2 if bs else b_th; b_unc = ((max(bs) - min(bs)) / 2 if bs else 0) + 10 * max(r[7] for r in good)
    kap = c_mid - c1m ** 2
    P(f'\nCONSENSUS (even n, {len(good)} fits): b = {mp.nstr(b_mid, 14)} ± {mp.nstr(b_unc, 2)}  (b_theory = {mp.nstr(b_th, 14)}, |b - b_theory| = {mp.nstr(abs(b_mid - b_th), 2)})')
    P(f'                                     c = {mp.nstr(c_mid, 14)} ± {mp.nstr(c_unc, 2)} ;  kappa = c - c1^2 = {mp.nstr(kap, 14)} ± {mp.nstr(c_unc, 2)}')
    oddc = [r[6] for r in results if r[0] == 'odd' and r[1] >= 3]
    if oddc:
        P(f'odd-n constant: c_odd in [{mp.nstr(min(oddc), 12)}, {mp.nstr(max(oddc), 12)}] ; c_odd - c_even = {mp.nstr((max(oddc)+min(oddc))/2 - c_mid, 3)}')
    P('=== (d) identification of kappa against 1-D constants ===')
    tol = 10 * c_unc
    g = mp.euler; l2 = mp.log(2); lp = mp.log(mp.pi); Lc = g + mp.log(8 / mp.pi)
    target = mp.pi ** 2 / 4 * kap
    P(f'(pi^2/4) kappa = {mp.nstr(target, 14)} ; pi^2 kappa = {mp.nstr(4*target, 14)} ; kappa = {mp.nstr(kap, 14)} ; tolerance for a hit = {mp.nstr(tol, 2)}')
    def try_pslq(label, vec, maxcoeff, maxsteps=100000):
        rel = mp.pslq(vec, tol=tol, maxcoeff=maxcoeff, maxsteps=maxsteps)
        if rel is None:
            P(f'  {label}: no relation with |coeff| <= {maxcoeff} at tol {mp.nstr(tol, 2)}')
            return None
        val = sum(r * v for r, v in zip(rel, vec))
        P(f'  {label}: relation {rel}  residual {mp.nstr(val, 3)}  (kappa-coefficient {rel[0]})')
        return rel
    P('tier 1: (pi^2/4) kappa vs {1, L, L^2}, L = gamma + log(8/pi); rational coefficients (denominator <= 16, numerators <= 64)')
    try_pslq('tier1', [target, 1, Lc, Lc ** 2], maxcoeff=64 * 16)
    P('tier 2: {(pi^2/4) kappa, kappa, pi^2 kappa} vs {1, gamma, log 2, log pi}, same coefficient bounds')
    for lab, tg in (('(pi^2/4)kappa', target), ('kappa', kap), ('pi^2 kappa', 4 * target)):
        try_pslq('tier2 ' + lab, [tg, 1, g, l2, lp], maxcoeff=64 * 16)
    P('tier 3: (pi^2/4) kappa vs the 10-element quadratic basis, integer coefficients <= 6 (hit only if it holds to >= 10 digits)')
    basis3 = [1, g, l2, lp, g * g, g * l2, g * lp, l2 * l2, l2 * lp, lp * lp]
    try_pslq('tier3', [target] + basis3, maxcoeff=6)
    P('natural candidates for kappa (value, kappa - value):')
    cands = {'c1^2': c1m ** 2, '(4/pi^2) L': 4 / mp.pi ** 2 * Lc, '(4/pi^2)(L^2 - 1/4)': 4 / mp.pi ** 2 * (Lc ** 2 - mp.mpf(1) / 4),
             '(4/pi^2)(L^2 + log 2 ... ) [L^2 only]': 4 / mp.pi ** 2 * Lc ** 2, 'c1^2 - (4/pi^2) log 2 / 8': c1m ** 2 - 4 / mp.pi ** 2 * l2 / 8,
             '(4/pi^2)*2': 8 / mp.pi ** 2, '(4/pi^2)(2 + gamma)': 4 / mp.pi ** 2 * (2 + g), '(2/pi) c1': 2 / mp.pi * c1m,
             '1 - (4/pi^2) log 2 ...': 1 - 4 / mp.pi ** 2 * l2 / 4, 'pi^2/12': mp.pi ** 2 / 12, '(4/pi^2)(gamma + log 8)': 4 / mp.pi ** 2 * (g + mp.log(8)),
             '(4/pi^2)(L^2 + 1/4) ': 4 / mp.pi ** 2 * (Lc ** 2 + mp.mpf(1) / 4), '(4/pi^2) (pi^2/4 - ... ) [=1]': mp.mpf(1)}
    for k_, v_ in cands.items():
        P(f'  {k_:45s} {mp.nstr(v_, 12):>16s}   kappa - value = {mp.nstr(kap - v_, 4)}')
    P(f'\nelapsed {time.time()-T0:.0f} s')
    with open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_onepage.out', 'w') as f:
        f.write('\n'.join(out) + '\n')
