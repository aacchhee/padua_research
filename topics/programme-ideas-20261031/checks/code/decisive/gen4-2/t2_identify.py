"""Decisive test gen4-2, T2 (d) continued: consensus for b, c, kappa from the long-double corner values saved in
t2_onepage.out, and the identification tiers at (i) the strict pre-registered uncertainty (spread over ALL fits, which
is dominated by the degenerate K = 5 fits) and (ii) the determined-fit uncertainty (fits with <= #points - 4 parameters
whose residual reaches the 1e-15 noise floor). A PSLQ hit must have a non-zero kappa coefficient.
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.
"""
import re, sys, itertools
import mpmath as mp
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2')
from t2_onepage import em_fit

out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
vals = {}
for line in open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_onepage.out'):
    m = re.match(r'n=(\d+) corner \((-?1), (-?1)\) Lambda_c = ([0-9.]+)', line)
    if m:
        vals[int(m.group(1))] = m.group(4)
even = sorted(n for n in vals if n % 2 == 0); odd = sorted(n for n in vals if n % 2 == 1)
P(f'values parsed: {len(even)} even n in [{even[0]}, {even[-1]}], {len(odd)} odd n in [{odd[0]}, {odd[-1]}]')
mp.mp.dps = 60
b_th = 8 / mp.pi ** 2 * (mp.euler + mp.log(8 / mp.pi)); c1 = 2 / mp.pi * (mp.euler + mp.log(8 / mp.pi))
allfits = []; det = []
P('parity | K | n_min | #pts | #params | b | c | max resid | determined?')
for parity, nset in (('even', even), ('odd', odd)):
    for K in (3, 4, 5):
        for nmin in sorted(set([nset[0], 127, 128, 255, 256, 512])):
            ns = [n for n in nset if n >= nmin]
            npar = 2 + K * (K + 3) // 2
            if len(ns) < npar + 2:
                continue
            for bfix in (None, b_th):
                try:
                    b, c, res, x = em_fit(ns, [vals[n] for n in ns], K, b_fixed=bfix, dps=60)
                except ValueError:
                    continue
                npar_eff = npar - (1 if bfix is not None else 0)
                isdet = (npar_eff <= len(ns) - 4) and (res < mp.mpf('2e-15')) and K <= 4
                allfits.append((parity, K, nmin, bfix is not None, b, c, res))
                if isdet:
                    det.append((parity, K, nmin, bfix is not None, b, c, res))
                P(f"{parity} | {K} | {nmin} | {len(ns)} | {npar_eff} | {'fixed ' if bfix is not None else ''}{mp.nstr(b, 14)} | {mp.nstr(c, 14)} | {mp.nstr(res, 3)} | {'yes' if isdet else 'no'}")


def consensus(fits, label):
    cs = [f[5] for f in fits]; bs = [f[4] for f in fits if not f[3]]
    cm = (max(cs) + min(cs)) / 2; cu = (max(cs) - min(cs)) / 2 + 10 * max(f[6] for f in fits)
    bm = (max(bs) + min(bs)) / 2; bu = (max(bs) - min(bs)) / 2 + 10 * max(f[6] for f in fits)
    P(f'{label}: {len(fits)} fits; b = {mp.nstr(bm, 15)} ± {mp.nstr(bu, 2)} (|b - b_theory| = {mp.nstr(abs(bm - b_th), 2)}); '
      f'c = {mp.nstr(cm, 15)} ± {mp.nstr(cu, 2)}; kappa = c - c1^2 = {mp.nstr(cm - c1 ** 2, 15)} ± {mp.nstr(cu, 2)}')
    return bm, bu, cm, cu


ev_all = [f for f in allfits if f[0] == 'even']; ev_det = [f for f in det if f[0] == 'even']
P('\n-- consensus --')
b1, bu1, c_strict, cu_strict = consensus(ev_all, 'STRICT (all even-n fits, pre-registered rule)')
b2, bu2, c_det, cu_det = consensus(ev_det, 'DETERMINED (even-n fits with <= #pts-4 parameters at the noise floor, K <= 4)')
od = [f for f in det if f[0] == 'odd'] or [f for f in allfits if f[0] == 'odd' and f[1] == 3]
if od:
    bo, buo, co, cuo = consensus(od, 'ODD n (determined or K = 3)')
    P(f'c_odd - c_even = {mp.nstr(co - c_det, 3)} (uncertainties {mp.nstr(cuo, 2)}, {mp.nstr(cu_det, 2)}) -> same constant? {abs(co - c_det) < cuo + cu_det}')
# STABLE subset: fits whose added terms are resolved (b-fixed with K in {3,4} and nmin <= 128; b-free with K = 3 and nmin <= 256)
ev_stab = [f for f in ev_det if (f[3] and f[2] <= 128) or ((not f[3]) and f[1] == 3 and f[2] <= 256)]
b3, bu3, c_stab, cu_stab = consensus(ev_stab, 'STABLE (b-fixed K=3,4 with nmin<=128; b-free K=3 with nmin<=256)')
kap = c_det - c1 ** 2
P(f'\nkappa (determined) = {mp.nstr(kap, 14)} ± {mp.nstr(cu_det, 2)} ; kappa (stable) = {mp.nstr(c_stab - c1**2, 14)} ± {mp.nstr(cu_stab, 2)} ; adversary had 0.919711 (double precision, n <= 2048)')
kap = c_stab - c1 ** 2
P('d-coefficients of the determined fit (even, K=4, nmin=64, b fixed), for the record: log n/n, 1/n, log^2/n^2, log/n^2, 1/n^2, ...')
for f in ev_det:
    if f[1] == 4 and f[2] == 64 and f[3]:
        b, c, res, x = em_fit([n for n in even if n >= 64], [vals[n] for n in even if n >= 64], 4, b_fixed=b_th, dps=60)
        P('  ', [mp.nstr(v, 8) for v in x])
        break

g = mp.euler; l2 = mp.log(2); lp = mp.log(mp.pi); L = g + mp.log(8 / mp.pi)
target = mp.pi ** 2 / 4 * kap


def try_pslq(label, vec, maxcoeff, tol):
    rel = mp.pslq(vec, tol=tol, maxcoeff=maxcoeff, maxsteps=200000)
    if rel is None or rel[0] == 0:
        P(f'  {label}: no relation with non-zero kappa-coefficient, |coeff| <= {maxcoeff}, tol {mp.nstr(tol, 2)}' + (f'  (pslq returned a basis-only relation {rel})' if rel else ''))
        return None
    val = sum(r * v for r, v in zip(rel, vec))
    P(f'  {label}: relation {rel}  residual {mp.nstr(val, 3)}  kappa-coefficient {rel[0]}')
    return rel


for label, tol in (('STRICT tolerance', 10 * cu_strict), ('DETERMINED tolerance', 10 * cu_det), ('STABLE tolerance', 10 * cu_stab)):
    P(f'\n== identification at {label} = {mp.nstr(tol, 2)} ==')
    P('tier 1: (pi^2/4) kappa vs {1, L, L^2}, L = gamma + log(8/pi), |integer coefficients| <= 1024 (covers denominators <= 16, numerators <= 64)')
    try_pslq('tier1', [target, 1, L, L ** 2], 1024, tol)
    P('tier 2: {(pi^2/4) kappa, kappa, pi^2 kappa} vs {1, gamma, log 2, log pi}')
    for lab, tg in (('(pi^2/4)kappa', target), ('kappa', kap), ('pi^2 kappa', 4 * target)):
        try_pslq('tier2 ' + lab, [tg, 1, g, l2, lp], 1024, tol)
    P('tier 3: (pi^2/4) kappa vs {1, gamma, log2, logpi, gamma^2, gamma log2, gamma logpi, log^2 2, log2 logpi, log^2 pi}, |coeff| <= 6')
    try_pslq('tier3', [target, 1, g, l2, lp, g * g, g * l2, g * lp, l2 * l2, l2 * lp, lp * lp], 6, tol)
    # chance levels: number of candidate relations times tol divided by the typical scale of the combinations
    P(f'  chance levels (expected number of spurious hits ~ #relations * tol / scale): tier1 ~ {float(2049**3 * tol / 50):.1e}, '
      f'tier2 ~ {float(2049**4 * tol / 50):.1e}, tier3 ~ {float(13**10 * tol / 10):.1e}')
P('\ninformational only (outside the pre-registered 1-D criterion): (pi^2/4) kappa vs {1, gamma, log2, logpi, pi^2, Catalan, zeta(3), gamma^2, log^2 2, gamma log 2}, |coeff| <= 12, determined tolerance')
try_pslq('info', [target, 1, g, l2, lp, mp.pi ** 2, mp.catalan, mp.zeta(3), g * g, l2 * l2, g * l2], 12, 10 * cu_stab)
P('mpmath.identify of kappa and (pi^2/4)kappa with constants [gamma, log2, logpi] (informational):')
mp.mp.dps = 15
for lab, v in (('kappa', kap), ('(pi^2/4)kappa', target), ('pi^2 kappa', 4 * target)):
    P(f'  {lab} = {mp.nstr(v, 11)} -> {mp.identify(v, ["euler", "log(2)", "log(pi)"], tol=float(10 * cu_stab))}')
with open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_identify.out', 'w') as f:
    f.write('\n'.join(out) + '\n')
