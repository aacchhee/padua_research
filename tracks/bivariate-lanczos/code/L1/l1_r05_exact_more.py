"""R05 extension (descriptive, not pre-registered): exact certificates for larger grids and a rationally rotated
square grid (rotation with cos = 3/5, sin = 4/5: nodes (3i - 4j, 4i + 3j)).  Usage: python3 -I l1_r05_exact_more.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l1_r05_exact_certificate as E
import l1_recurrence as L
from fractions import Fraction as Fr

orig_main = E.main

def run_nodes(label, nodes, scale_half_width, nmax, s_deg):
    # reuse E.main's logic on an explicit node list (scale = half-width of the node box in these coordinates)
    import math, time
    M = len(nodes); xs = [Fr(a) for a, _ in nodes]; ys = [Fr(b) for _, b in nodes]
    idx, pos, parent, op, start = L.tables(nmax); N = len(idx)
    t0 = time.time()
    psi = [[Fr(1)] * M]; nrm = [Fr(M)]; alpha = [None]
    for k in range(1, N):
        p = parent[k]; a = xs if op[k] == 'J' else ys
        u = [a[i] * psi[p][i] for i in range(M)]
        W = L.window(k, idx, start, 'block'); al = {}; v = list(u)
        for l in W:
            c = sum(u[i] * psi[l][i] for i in range(M)) / nrm[l]; al[l] = c
            if c: v = [v[i] - c * psi[l][i] for i in range(M)]
        psi.append(v); nrm.append(sum(t * t for t in v)); alpha.append(al)
    nz = sum(1 for k in range(N) for l in range(k) if sum(psi[k][i] * psi[l][i] for i in range(M)) != 0)
    print(f"# {label}: M={M} nmax={nmax}; exact orthogonality check nonzero pairs: {nz}", flush=True)
    scale = Fr(scale_half_width) ** 2
    G = {}
    for s in [pos[(s_deg, j)] for j in range(s_deg + 1)]:
        ps = parent[s]; g = {s: [Fr(1)] * M}
        for k in range(s + 1, N):
            p = parent[k]; a = xs if op[k] == 'J' else ys; gp = g.get(p)
            val = [a[i] * gp[i] for i in range(M)] if gp is not None else [Fr(0)] * M
            for l, c in alpha[k].items():
                if c and l in g: val = [val[i] - c * g[l][i] for i in range(M)]
            g[k] = val; n = idx[k][0]
            best = max(t * t for t in val) * nrm[ps] / nrm[k] * scale
            if n not in G or best > G[n]: G[n] = best
    print("   log10 G(n): " + " ".join(f"{n}:{E.log10_fraction(G[n]):.2f}" for n in sorted(G)) + f"   ({time.time() - t0:.0f}s)", flush=True)

for m in (40,):
    run_nodes(f"triangle m={m}", [(i, j) for i in range(m + 1) for j in range(m + 1 - i)], Fr(m, 2), 16, 2)
    run_nodes(f"square m={m}", [(i, j) for i in range(m + 1) for j in range(m + 1)], Fr(m, 2), 16, 2)
m = 24
rot = [(3 * i - 4 * j, 4 * i + 3 * j) for i in range(m + 1) for j in range(m + 1)]
run_nodes("square grid m=24 rotated (3/5, 4/5)", rot, Fr(5 * m, 2), 14, 2)
