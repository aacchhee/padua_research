"""Decisive test gen4-2, T1 tail: the main run (t1_argmax.py) was interrupted after n = 161; this script re-parses its rows,
adds n = 200 ((2n+1)^2 mesh) and computes the pre-registered summary (trend of G(n), fits, ratios).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.
"""
import sys, re, time, json
import numpy as np
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2')
from t1_argmax import analyse

T0 = time.time()
out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
rows = []
for line in open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_argmax.out'):
    m = re.match(r'(\d+) \| (\d+)\^2 \| ([0-9.]+) \| ([0-9.]+) \| (\w+) \| ([0-9.]+) \| ([0-9.]+) \| ([0-9.]+) \| ([0-9.]+) \| ([0-9.]+) \| (\w+) \|', line)
    if m:
        rows.append(dict(n=int(m.group(1)), mesh=int(m.group(2)), Lc=float(m.group(3)), R=float(m.group(4)), where=m.group(5), dist=float(m.group(6)),
                         G=float(m.group(7)), mesh_max_nc=float(m.group(9)), edge_max_nc=float(m.group(10)), kill=(m.group(11) == 'KILL')))
P(f'parsed {len(rows)} rows from t1_argmax.out (n = {rows[0]["n"]}..{rows[-1]["n"]})')
for n in (200,):
    t0 = time.time()
    r = analyse(n, 2 * n + 1, 20 * n + 1)
    r['t_total'] = time.time() - t0
    rows.append(r)
    P(f"{n} | {2*n+1}^2 | {r['Lc']:.9f} | {r['R']:.9f} | {r['where']} | {r['dist']:.4f} | {r['G']:.6f} | {r['G']/np.log(n):.5f} | "
      f"{r['mesh_max_nc']:.6f} | {r['edge_max_nc']:.6f} | {'KILL' if r['kill'] else 'ok'} | {r['t_mesh']:.1f} | {r['t_total']:.1f}")
    P('   edge maxima detail (value, angle):', {k: (round(v[0], 6), round(v[1], 5)) for k, v in r['edge_vals'].items()}, 'non-node corners', r['non_node'], 'runner-up at', [round(x, 6) for x in r['best'][:3]])
rows.sort(key=lambda z: z['n'])
G = np.array([r['G'] for r in rows]); nn = np.array([r['n'] for r in rows], float); Lc = np.array([r['Lc'] for r in rows])
P('\nG(n) = Lambda_c - R(n): decreasing for n >= 32? %s ; G at n = 32, 64, 128, 200: %s ; G/Lc at largest n: %.4f' %
  (bool(np.all(np.diff(G[nn >= 32]) < 0)), [round(float(G[nn == k][0]), 5) for k in (32, 64, 128, 200) if np.any(nn == k)], G[-1] / Lc[-1]))
P('where is the runner-up: ' + ', '.join(f"{w}:{sum(1 for r in rows if r['where'] == w)}" for w in sorted(set(r['where'] for r in rows))))
P('distance of the runner-up from the nearest non-node corner (angles): min %.4f, max %.4f; values for n = 8, 64, 128, 200: %s' %
  (min(r['dist'] for r in rows), max(r['dist'] for r in rows), [round(r['dist'], 4) for r in rows if r['n'] in (8, 64, 128, 200)]))
m = nn >= 32
for name, cols in (('a + b/n', np.c_[np.ones(m.sum()), 1 / nn[m]]), ('a + b log n/n', np.c_[np.ones(m.sum()), np.log(nn[m]) / nn[m]]),
                   ('a + b log n/n + c/n', np.c_[np.ones(m.sum()), np.log(nn[m]) / nn[m], 1 / nn[m]]), ('a + b log n', np.c_[np.ones(m.sum()), np.log(nn[m])]),
                   ('a + b/log n', np.c_[np.ones(m.sum()), 1 / np.log(nn[m])])):
    coef, *_ = np.linalg.lstsq(cols, G[m], rcond=None)
    P(f'fit G(n) = {name} (n >= 32, {m.sum()} points): coefficients {np.round(coef, 5)}, max resid {np.max(np.abs(G[m] - cols @ coef)):.2e}')
P('ratio R/Lc: ' + ' '.join(f"{int(r['n'])}:{r['R']/r['Lc']:.4f}" for r in rows if r['n'] in (2, 3, 4, 5, 6, 7, 8, 12, 16, 24, 32, 48, 64, 96, 128, 160, 200)))
P('any KILL: %s ; elapsed %.0f s' % (any(r['kill'] for r in rows), time.time() - T0))
json.dump([{k: (v if not isinstance(v, (np.floating, np.integer)) else float(v)) for k, v in r.items() if k in ('n', 'mesh', 'Lc', 'R', 'where', 'dist', 'G', 'mesh_max_nc', 'edge_max_nc', 'kill')} for r in rows],
          open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_argmax.json', 'w'), indent=0, default=float)
open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_tail.out', 'w').write('\n'.join(out) + '\n')
