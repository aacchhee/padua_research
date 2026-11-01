"""Decisive test gen4-2, T2 supplement: refit of the corner expansion in the shifted variable N = n + 1/2,
y = Lambda_c - (4/pi^2) log^2 N - b log N = c + d1/N + sum_{k=2..K} sum_{m<=k} d_km log^m N / N^k  (b fixed at theory),
using the long-double values of t2_onepage.out and t2_odd.out (even and odd n together and separately).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.
"""
import re, sys
import mpmath as mp
out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
vals = {}
for fn in ('t2_onepage.out', 't2_odd.out'):
    for line in open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/' + fn):
        m = re.match(r'n=(\d+) corner \((-?1), (-?1)\) Lambda_c = ([0-9.]+)', line)
        if m:
            vals[int(m.group(1))] = m.group(4)
mp.mp.dps = 60
a = 4 / mp.pi ** 2; b = 8 / mp.pi ** 2 * (mp.euler + mp.log(8 / mp.pi)); c1 = 2 / mp.pi * (mp.euler + mp.log(8 / mp.pi))


def fit(ns, K, with_log_over_N=False):
    rows = []; rhs = []
    for n in ns:
        N = mp.mpf(n) + mp.mpf(1) / 2; L = mp.log(N)
        y = mp.mpf(vals[n]) - a * L ** 2 - b * L
        cols = [mp.mpf(1), 1 / N] + ([L / N] if with_log_over_N else [])
        for k in range(2, K + 1):
            for mm in range(0, k + 1):
                cols.append(L ** mm / N ** k)
        rows.append(cols); rhs.append(y)
    x, res = mp.qr_solve(mp.matrix(rows), mp.matrix(rhs))
    r = mp.matrix(rows) * x - mp.matrix(rhs)
    return x, max(abs(v) for v in r)


P('set | K | #pts | c | d1 (coeff of 1/N) | [d(log N/N)] | 1/N^2-level coefficients (log^0, log^1, log^2) | max resid')
for label, ns_all in (('even', sorted(n for n in vals if n % 2 == 0)), ('odd', sorted(n for n in vals if n % 2 == 1)), ('all', sorted(vals))):
    for nmin in (64, 128):
        ns = [n for n in ns_all if n >= nmin]
        for K in (2, 3, 4):
            for wl in (False, True):
                npar = 2 + (1 if wl else 0) + sum(k + 1 for k in range(2, K + 1))
                if len(ns) < npar + 3:
                    continue
                try:
                    x, res = fit(ns, K, wl)
                except ValueError:
                    continue
                off = 3 if wl else 2
                P(f"{label} n>={nmin} | {K} | {len(ns)} | {mp.nstr(x[0], 14)} | {mp.nstr(x[1], 10)} | {mp.nstr(x[2], 6) if wl else '-'} | {[mp.nstr(v, 7) for v in x[off:off+3]]} | {mp.nstr(res, 3)}")
P(f'\nreference: kappa = c - c1^2 with c1^2 = {mp.nstr(c1**2, 14)} ; pi^2/8 = {mp.nstr(mp.pi**2/8, 8)} ; 1/12 = {mp.nstr(mp.mpf(1)/12, 8)} ; (4/pi^2)/12 = {mp.nstr(a/12, 8)}')
open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_halfshift.out', 'w').write('\n'.join(out) + '\n')
