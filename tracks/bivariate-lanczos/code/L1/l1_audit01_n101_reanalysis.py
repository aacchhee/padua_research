"""Reanalysis of STORED R01/R02 data for the restatement of PD-N?bivariate-lanczos-claude-101 (Codex audit-01,
finding LL-M1).  No recurrence is rerun: this reads the JSON lines written by l1_kill_test.py (logs/r01_*.raw) and
the one-significant-digit table of l1_node_propagator.py (logs/r02_node_propagator.log).

Reported, separately per scope:
  (A) R01 main non-product runs (Ritz residuals of H_x, H_y, Z, oblique l computed; N_k from the simax run):
      informative degrees, min/max of loss/(u/rho_O) under the pre-registered rule (u := 2^-52, tau = 1e3 u,
      band [1/3, 3]) and under the plan's unit roundoff (u = 2^-53, tau = 1e3 u);
  (B) rotation pairs: rho_Z(rotated)/rho_Z(unrotated) per degree, with the rotated run's loss;
  (C) loss per degree and decades per 4 degrees on the R01 main non-product runs;
  (D) seed-11 sets of l1_node_propagator.py (bj only, Z only, one-digit log values): loss/(u/rho_Z) at degrees with
      loss >= tau.
Developer reanalysis (Claude Opus 5.5, xhigh), 2026-11-01.
Usage (from the repository root):
  python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_n101_reanalysis.py topics/bivariate-lanczos-20261031/directions/L1/logs
"""
import json, math, os, re, sys
from collections import defaultdict

logdir = sys.argv[1]
rows = []
for fn in ('r01_input3.raw', 'r01_rotation.raw', 'r01_irregular.raw'):
    for line in open(os.path.join(logdir, fn)):
        if line.startswith('JSON '):
            rows.append(json.loads(line[5:]))
runs = defaultdict(dict)
for r in rows:
    if r['N'] < r['M']:                     # completion degrees excluded as in R01 (none occur in these runs)
        runs[(r['run'], r['method'])][r['n']] = r

MAIN = ['random1681_s0_rot0.3', 'random1681_s7_rot1.0', 'tensorcheb41_rot0.3', 'Lshape_grid61',
        'Lshape_grid61_rot0.3', 'Lshape_rand3000', 'annulus_rand3000']
OBJ = [('X', 'res_x'), ('Y', 'res_y'), ('Z', 'res_z'), ('l', 'res_l')]
CONV = [('2^-52 (pre-registered rule)', 2.0 ** -52), ('2^-53 (plan unit roundoff)', 2.0 ** -53)]


def judge(recs, key, u, losskey='loss'):
    tau = 1e3 * u
    D = [r for r in recs if r[losskey] >= tau or u / max(r[key], 1e-300) >= tau]
    if not D:
        return None
    q = [r[losskey] / (u / max(r[key], 1e-300)) for r in D]
    inband = sum(1 for v in q if 1 / 3 <= v <= 3)
    return dict(n0=D[0]['n'], ns=[r['n'] for r in D], lo=min(q), hi=max(q), inband=inband,
                below100=sum(1 for v in q if v < 100), below30=sum(1 for v in q if v < 30))


print('# l1_audit01_n101_reanalysis.py (stored data only)')
for cname, u in CONV:
    print(f'\n## (A) R01 main non-product runs, u = {cname}, tau = 1e3 u = {1e3 * u:.3e}')
    glo, ghi, gin, gb100, gb30 = math.inf, 0.0, 0, 0, 0
    for run in MAIN:
        for meth in ('bj', 'hl'):
            recs = [runs[(run, meth)][n] for n in sorted(runs[(run, meth)])]
            out = []
            for o, key in OBJ:
                j = judge(recs, key, u)
                glo, ghi = min(glo, j['lo']), max(ghi, j['hi'])
                gin += j['inband']; gb100 += j['below100']; gb30 += j['below30']
                out.append(f"{o}: [{j['lo']:.2e}, {j['hi']:.2e}] n>={j['n0']}")
            sm = runs[(run, 'simax')]
            paired = [dict(loss=runs[(run, meth)][n]['loss'], res_nk=sm[n]['res_nk'], n=n)
                      for n in sorted(runs[(run, meth)]) if n in sm]
            jn = judge(paired, 'res_nk', u)
            own = judge([sm[n] for n in sorted(sm)], 'res_nk', u)
            gin += jn['inband']; gb100 += jn['below100']; gb30 += jn['below30']
            glo, ghi = min(glo, jn['lo']), max(ghi, jn['hi'])
            out.append(f"Nk(vs this loss): [{jn['lo']:.2e}, {jn['hi']:.2e}] n>={jn['n0']}")
            if meth == 'bj':
                out.append(f"Nk(vs simax own loss): [{own['lo']:.2e}, {own['hi']:.2e}] n>={own['n0']}")
            print(f'{run:22s} {meth:3s} ' + ' | '.join(out))
    print(f'# overall (X, Y, Z, l and Nk vs bj/hl loss): min ratio {glo:.2e}, max ratio {ghi:.2e}; '
          f'informative (run, object, degree) triples in the factor-3 band: {gin}; below 100: {gb100}; below 30: {gb30}')

print('\n## (B) rotation pairs: rho_Z(rotated)/rho_Z(unrotated) per degree [loss of rotated run]')
PAIRS = [('random1681_s0', 'random1681_s0_rot0.3'), ('random1681_s7', 'random1681_s7_rot1.0'),
         ('tensorcheb41', 'tensorcheb41_rot0.3'), ('Lshape_grid61', 'Lshape_grid61_rot0.3')]
for a, b in PAIRS:
    for meth in ('bj', 'hl'):
        ra, rb = runs[(a, meth)], runs[(b, meth)]
        cells = []
        dev_before = 0.0
        for n in sorted(ra):
            if n in rb:
                q = rb[n]['res_z'] / ra[n]['res_z']
                cells.append(f"{n}:{q:.4f}[{rb[n]['loss']:.0e}]")
                if rb[n]['loss'] < 1e-8 and ra[n]['loss'] < 1e-8:
                    dev_before = max(dev_before, abs(q - 1))
        print(f'{b:22s} {meth:3s} max|ratio-1| while both losses < 1e-8: {dev_before:.2e}   ' + ' '.join(cells))

print('\n## (C) loss per degree and decades per 4 degrees (R01 main non-product runs)')
for run in MAIN:
    for meth in ('bj', 'hl'):
        rr = runs[(run, meth)]
        ns = sorted(rr)
        ls = [rr[n]['loss'] for n in ns]
        dec = [math.log10(ls[i + 1] / ls[i]) for i in range(len(ls) - 1)]
        print(f'{run:22s} {meth:3s} ' + ' '.join(f'{n}:{v:.1e}' for n, v in zip(ns, ls)))
        print(f'{"":22s} {"":3s} decades/4 deg: ' + ' '.join(f'{ns[i]}-{ns[i + 1]}:{d:+.1f}' for i, d in enumerate(dec)))

print('\n## (D) seed-11 sets of l1_node_propagator.py (bj, Z only; one significant digit in the log; u = 2^-52)')
tau = 1e3 * 2.0 ** -52
pat = re.compile(r'n(\d+): L=([0-9.e+-]+) P=[0-9.e+-]+ u/rZ=([0-9.e+-]+)')
for line in open(os.path.join(logdir, 'r02_node_propagator.log')):
    name = line[:26].strip()
    cells = pat.findall(line)
    if not cells:
        continue
    q = [(int(n), float(L) / float(p)) for n, L, p in cells if float(L) >= tau]
    print(f'{name:22s} ' + (' '.join(f'n{n}:{v:.1e}' for n, v in q) if q else '(no degree with loss >= tau)'))
