"""Apply the pre-registered R01 decision rule (candidates.md, IDEA?...-101/-102) to the JSON lines
written by l1_kill_test.py.  Usage: python3 -I l1_analyze_r01.py logs/r01_*.raw > logs/r01_verdict.txt
"""
import sys, json
from collections import defaultdict

EPS = 2.0 ** -52
TAU = 1e3 * EPS
LO, HI = 1 / 3, 3.0

rows = []
for fn in sys.argv[1:]:
    for line in open(fn):
        if line.startswith('JSON '):
            rows.append(json.loads(line[5:]))

# post-hoc exclusion (disclosed in R01.md): degrees with N = M (completed basis; every Ritz pair is exact and
# there is no next vector), reported separately
completion = [(r['run'], r['method'], r['n']) for r in rows if r['N'] >= r['M']]
rows = [r for r in rows if r['N'] < r['M']]
runs = defaultdict(list)
for r in rows:
    runs[(r['run'], r['method'])].append(r)
simax = {k[0]: v for k, v in runs.items() if k[1] == 'simax'}

OBJ = [('X', 'res_x'), ('Y', 'res_y'), ('Z', 'res_z'), ('l', 'res_l')]


def judge(recs, key, losskey='loss'):
    D = [r for r in recs if r[losskey] >= TAU or EPS / max(r[key], 1e-300) >= TAU]
    if not D:
        return 'uninformative', None, None, []
    ratios = [r[losskey] / (EPS / max(r[key], 1e-300)) for r in D]
    pred = all(LO <= q <= HI for q in ratios)
    # secondary 'tracks' needs >= 2 informative degrees (post-hoc fix, R01: with one degree it is vacuous)
    track = len(ratios) >= 2 and max(ratios) / min(ratios) <= 9
    tag = 'PREDICTS' if pred else ('tracks' if track else 'fails')
    if not pred and min(ratios) < 1 / 30:
        tag += '/over'      # u/res exceeds measured loss by > 30x somewhere (converged pairs without loss)
    if not pred and max(ratios) > 30:
        tag += '/under'     # measured loss exceeds u/res by > 30x somewhere (loss without convergence)
    return tag, min(ratios), max(ratios), [r['n'] for r in D]


print(f"# decision rule: tau = {TAU:.2e}, band [{LO:.3f}, {HI}], u := 2^-52")
print(f"# excluded completion degrees (N = M): {completion}")
print(f"# {'run':28s} {'meth':5s} " + "  ".join(f"{o:>34s}" for o, _ in OBJ))
verdict = {}
for (run, meth), recs in sorted(runs.items()):
    if meth == 'simax':
        continue
    recs = sorted(recs, key=lambda r: r['n'])
    out = []
    for o, key in OBJ:
        tag, lo, hi, D = judge(recs, key)
        verdict[(run, meth, o)] = tag
        out.append(f"{tag:>13s} [{(lo or 0):8.1e},{(hi or 0):8.1e}] n>={(D[0] if D else 0):2d}")
    if run in simax:
        # (N,N*) section of the complex HL SIMAX run, paired (a) with this run's loss, (b) with its own loss
        sm = {r['n']: r for r in simax[run]}
        paired = [dict(n=r['n'], loss=r['loss'], res_nk=sm[r['n']]['res_nk']) for r in recs if r['n'] in sm]
        tag_a = judge(paired, 'res_nk')
        own = sorted(simax[run], key=lambda r: r['n'])
        tag_b = judge(own, 'res_nk')
        verdict[(run, meth, 'Nk')] = tag_a[0]
        verdict[(run, 'simax', 'Nk-own')] = tag_b[0]
        out.append(f"Nk(vs this loss) {tag_a[0]}; Nk(vs SIMAX own loss) {tag_b[0]} [{(tag_b[1] or 0):.1e},{(tag_b[2] or 0):.1e}]")
    print(f"{run:30s} {meth:5s} " + " | ".join(out))

print()
# Frozen K1: exists a run where Z predicts, and on every such run X or Y predicts
zpred = [(r, m) for (r, m, o), t in verdict.items() if o == 'Z' and t == 'PREDICTS']
k1_runs = [(r, m, verdict[(r, m, 'X')], verdict[(r, m, 'Y')]) for (r, m) in zpred]
k1 = bool(zpred) and all(vx == 'PREDICTS' or vy == 'PREDICTS' for _, _, vx, vy in k1_runs)
print("K1 (frozen first clause): runs where Z predicts:")
for r, m, vx, vy in k1_runs:
    print(f"   {r:30s} {m:4s}  X:{vx:13s} Y:{vy:13s}")
print(f"K1 fires: {k1}")
over = [(r, m, o) for (r, m, o), t in verdict.items() if o in ('X', 'Y') and t.startswith(('fails', 'tracks'))
        and 'over' in t and verdict.get((r, m, 'Z')) in ('PREDICTS', 'uninformative')]
print("Runs where a single section FAILS while Z predicts/tracks/is uninformative (falsifier of -101):")
for r, m, o in sorted(over):
    print(f"   {r:30s} {m:4s} {o}  (Z: {verdict.get((r, m, 'Z'))})")
# input's three families: uniform random square, tensor Chebyshev, Padua with uniform weights (and x<->y swaps)
new_sets = [k for k in verdict if ('rot' in k[0]) or k[0].startswith(('Lshape', 'annulus')) or k[0].endswith('_cub')]
informative = defaultdict(list)
for (r, m, o) in new_sets:
    informative[(r, m)].append(verdict[(r, m, o)])
k2_cands = [(rm, v) for rm, v in informative.items() if any(t != 'uninformative' for t in v)]
k2 = bool(k2_cands) and all(all(not t.startswith('PREDICTS') for t in v) for _, v in k2_cands)
print(f"K2 (frozen second clause, new node sets with informative degrees): {len(k2_cands)} informative runs; fires: {k2}")
for rm, v in sorted(k2_cands):
    print(f"   {rm[0]:30s} {rm[1]:5s} {v}")
