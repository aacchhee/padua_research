"""Decisive test gen4-2, T3 validation (independent of the certificates): for every certified maximum of t3_maxima.json,
(i) a ring test (lambda at the point >= lambda on rings of radius 1e-3, 1e-4, 1e-5 in angle, 64 directions, even extension);
(ii) for every pair of certified maxima closer than 0.05, the minimum of lambda on the segment between them must be strictly
below both endpoints (a genuine valley); (iii) a brute-force search for maxima missed by the certifier: discrete local maxima
on a 1201^2 Chebyshev-angle mesh of the closed square (edges and corners included through the even extension), Newton-polished
with the adversary-style fixed-sign iteration, ring-tested, and matched to the certified list (1e-6).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.
"""
import sys, json, time
import numpy as np
from scipy.ndimage import maximum_filter
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2')
from leb_common import LebDense, LebDCT

out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
data = json.load(open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_maxima.json'))
PUB = {3: (7, 15), 4: (13, 27), 5: (14, 25), 6: (23, 39), 7: (27, 42), 8: (38, 56)}
t0 = time.time()
P('n | certified int/edge/corner/total | published | ring-test failures (1e-3,1e-4,1e-5) | close pairs (<0.05): count, min valley depth | brute-force maxima found | brute-force maxima NOT in certified list | certified maxima NOT found by brute force')
for ns, D in data.items():
    n = int(ns); f = LebDense(n); dct = LebDCT(n)
    pts = [tuple(p) for p in D['interior'] + D['edge'] + D['corner']]
    # (i) ring tests
    fails = []
    ang = np.linspace(0, 2 * np.pi, 64, endpoint=False)
    for rad in (1e-3, 1e-4, 1e-5):
        nf = 0
        for (t, p, v) in pts:
            tt = t + rad * np.cos(ang); pp = p + rad * np.sin(ang)
            v0 = f([t], [p])[0]; vr = f(tt, pp)
            if np.any(vr > v0 + 1e-12):
                nf += 1
        fails.append(nf)
    # (ii) valleys between close pairs
    pairs = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            dist = np.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
            if dist < 0.05:
                s = np.linspace(0, 1, 2001)
                tt = pts[i][0] + s * (pts[j][0] - pts[i][0]); pp = pts[i][1] + s * (pts[j][1] - pts[i][1])
                vals = f(tt, pp)
                depth = min(vals[0], vals[-1]) - vals.min()
                pairs.append((dist, depth, pts[i][:2], pts[j][:2]))
    # (iii) brute force: mesh of the closed square with margins (even extension), discrete local maxima, polish
    m = 1201
    g = np.linspace(-0.02, np.pi + 0.02, m)
    lam = dct.lambda_mesh(g, g)
    mx = maximum_filter(lam, size=3, mode='nearest') == lam
    I, J = np.where(mx)
    found = []
    for i, j in zip(I, J):
        t, p = g[i], g[j]
        if t < -1e-9 or t > np.pi + 1e-9 or p < -1e-9 or p > np.pi + 1e-9:
            continue
        # polish by the fixed-sign Newton (re-signed each step); project edge-near points onto the edge by symmetry
        x = np.array([t, p])
        for _ in range(40):
            d = f.cardinals([x[0]], [x[1]], derivs=2)
            s = np.sign(d['L'][0]); s[s == 0] = 1
            gr = np.array([np.sum(s * d['Lt'][0]), np.sum(s * d['Lp'][0])])
            H = np.array([[np.sum(s * d['Ltt'][0]), np.sum(s * d['Ltp'][0])], [np.sum(s * d['Ltp'][0]), np.sum(s * d['Lpp'][0])]])
            if np.linalg.norm(gr) < 1e-13:
                break
            try:
                step = np.linalg.solve(H, -gr)
            except np.linalg.LinAlgError:
                break
            if np.linalg.norm(step) > 0.01:
                step *= 0.01 / np.linalg.norm(step)
            x = x + step
        # snap to the closed square (mirror) and dedupe
        x = np.array([abs(x[0]) if x[0] < 0 else (2 * np.pi - x[0] if x[0] > np.pi else x[0]), abs(x[1]) if x[1] < 0 else (2 * np.pi - x[1] if x[1] > np.pi else x[1])])
        if abs(x[0]) < 1e-9: x[0] = 0.0
        if abs(x[0] - np.pi) < 1e-9: x[0] = np.pi
        if abs(x[1]) < 1e-9: x[1] = 0.0
        if abs(x[1] - np.pi) < 1e-9: x[1] = np.pi
        v0 = f([x[0]], [x[1]])[0]
        ok = True
        for rad in (1e-4, 1e-5):
            tt = x[0] + rad * np.cos(ang); pp = x[1] + rad * np.sin(ang)
            if np.any(f(tt, pp) > v0 + 1e-12):
                ok = False
        if ok and all(np.hypot(x[0] - a, x[1] - b) > 1e-6 for a, b, _ in found):
            found.append((x[0], x[1], v0))
    missing_cert = [q for q in found if all(np.hypot(q[0] - a, q[1] - b) > 1e-6 for a, b, _ in pts)]
    missing_bf = [q for q in pts if all(np.hypot(q[0] - a, q[1] - b) > 1e-6 for a, b, _ in found)]
    P(f"{n} | {len(D['interior'])}/{len(D['edge'])}/{len(D['corner'])}/{len(pts)} | {PUB[n][0]}/{PUB[n][1]} | {fails} | {len(pairs)}, {min([p[1] for p in pairs]) if pairs else float('nan'):.2e} | {len(found)} | {len(missing_cert)} | {len(missing_bf)}   [{time.time()-t0:.0f}s]")
    for dist, depth, a, b in sorted(pairs):
        P(f'    pair dist {dist:.3e} valley depth {depth:.3e}: ({a[0]:.6f},{a[1]:.6f}) - ({b[0]:.6f},{b[1]:.6f})')
    for q in missing_cert:
        P(f'    brute-force maximum not certified: ({q[0]:.6f},{q[1]:.6f}) lambda {q[2]:.6f}')
    for q in missing_bf:
        P(f'    certified maximum not found by brute force (mesh resolution): ({q[0]:.6f},{q[1]:.6f}) lambda {q[2]:.6f}')
open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_validate.out', 'w').write('\n'.join(out) + '\n')
