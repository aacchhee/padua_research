"""Decisive test gen4-2, T2 supplement: odd-n corner values (non-node corner (-1,-1)) with enough points for a K = 3
Euler-Maclaurin fit, to test whether odd n share the constant c of even n. Also the first E-M coefficients for both parities.
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.
"""
import sys, re, time
import numpy as np, mpmath as mp
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2')
from t2_onepage import corner_closed, em_fit

T0 = time.time(); out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
vals = {}
for line in open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_onepage.out'):
    m = re.match(r'n=(\d+) corner \((-?1), (-?1)\) Lambda_c = ([0-9.]+)', line)
    if m:
        vals[int(m.group(1))] = m.group(4)
extra_odd = [95, 191, 383, 639, 767, 895, 1279, 1535, 1791, 2559, 3071]
for n in extra_odd:
    t = time.time(); v = corner_closed(n, (-1, -1)); vals[n] = np.format_float_positional(v, precision=19)
    P(f'n={n} corner (-1,-1) Lambda_c = {vals[n]}  [{time.time()-t:.1f}s]')
# also both non-node corners agree for odd n? (symmetry check) and the node corners are 1
for n in (65, 129):
    P(f'n={n}: corners (-1,-1) {np.format_float_positional(corner_closed(n,(-1,-1)),precision=16)} (-1,1) {np.format_float_positional(corner_closed(n,(-1,1)),precision=16)} (1,1) {float(corner_closed(n,(1,1))):.12f} (1,-1) {float(corner_closed(n,(1,-1))):.12f}')
odd = sorted(n for n in vals if n % 2 == 1); even = sorted(n for n in vals if n % 2 == 0)
mp.mp.dps = 60
b_th = 8 / mp.pi ** 2 * (mp.euler + mp.log(8 / mp.pi)); c1 = 2 / mp.pi * (mp.euler + mp.log(8 / mp.pi))
P(f'odd n available: {odd}')
P('parity | K | n_min | #pts | b | c | max resid | first coefficients (log n/n, 1/n, log^2/n^2, log/n^2, 1/n^2)')
for parity, nset in (('odd', odd), ('even', even)):
    for K in (2, 3):
        for nmin in (64, 128, 256):
            ns = [n for n in nset if n >= nmin]
            npar = 2 + K * (K + 3) // 2
            if len(ns) < npar + 2:
                continue
            for bfix in (None, b_th):
                try:
                    b, c, res, x = em_fit(ns, [vals[n] for n in ns], K, b_fixed=bfix, dps=60)
                except ValueError as ex:
                    continue
                off = 1 if bfix is None else 0
                P(f"{parity} | {K} | {nmin} | {len(ns)} | {'fixed ' if bfix is not None else ''}{mp.nstr(b, 13)} | {mp.nstr(c, 13)} | {mp.nstr(res, 3)} | {[mp.nstr(v, 7) for v in x[off+1:off+6]]}")
P(f'elapsed {time.time()-T0:.0f} s')
open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_odd.out', 'w').write('\n'.join(out) + '\n')
