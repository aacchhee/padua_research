"""R05: exact rational certificate of propagator growth (PD-T?bivariate-lanczos-claude-113).
Monic window recurrence (BJ form, block window = exact in exact arithmetic) on integer nodes, all arithmetic in
Python Fractions.  For an impulse at column s, the orthonormal propagator entry at node z satisfies exactly
  (L*(z)^-1)_{k,s}^2 = ||psi_{p(s)}||^2 g_k(z)^2 / ||psi_k||^2   (g = monic impulse response, g_s = 1),
see the theory file.  Reports, per degree n, G(n) = max over impulses s (all columns of degree s_deg), columns k of
degree n and nodes i of that squared entry, rescaled to coordinates normalised to [-1,1] (factor (m/2)^2), as an
exact rational and as log10.  Usage: python3 -I l1_r05_exact_certificate.py <set> <m> <nmax> <s_deg>
  set: triangle (nodes (i,j), i+j<=m) | square ((i,j), 0<=i,j<=m); equal weights."""
import sys, os, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import l1_recurrence as L


def log10_fraction(q):
    q = abs(q)
    return (math.log10(q.numerator) if q.numerator else -math.inf) - math.log10(q.denominator)


def main(setname, m, nmax, s_deg):
    if setname == 'triangle':
        nodes = [(i, j) for i in range(m + 1) for j in range(m + 1 - i)]
    else:
        nodes = [(i, j) for i in range(m + 1) for j in range(m + 1)]
    M = len(nodes); xs = [Fr(a) for a, _ in nodes]; ys = [Fr(b) for _, b in nodes]
    idx, pos, parent, op, start = L.tables(nmax); N = len(idx)
    t0 = time.time()
    psi = [[Fr(1)] * M]; nrm = [Fr(M)]; alpha = [None]
    for k in range(1, N):
        p = parent[k]; a = xs if op[k] == 'J' else ys
        u = [a[i] * psi[p][i] for i in range(M)]
        W = L.window(k, idx, start, 'block'); al = {}
        v = list(u)
        for l in W:
            c = sum(u[i] * psi[l][i] for i in range(M)) / nrm[l]
            al[l] = c
            if c:
                pl = psi[l]
                v = [v[i] - c * pl[i] for i in range(M)]
        psi.append(v); nrm.append(sum(t * t for t in v)); alpha.append(al)
    print(f"# exact monic recurrence: set={setname} m={m} M={M} nmax={nmax} N={N} ({time.time() - t0:.1f}s)", flush=True)
    # exact check: orthogonality of the computed monic basis (must be exactly zero)
    nz = 0
    for k in range(N):
        for l in range(k):
            if sum(psi[k][i] * psi[l][i] for i in range(M)) != 0: nz += 1
    print(f"# exact orthogonality check: nonzero inner products among {N*(N-1)//2} pairs: {nz}", flush=True)
    scale = Fr(m, 2) ** 2
    G = {}
    for s in [pos[(s_deg, j)] for j in range(s_deg + 1)]:
        ps = parent[s]
        g = {s: [Fr(1)] * M}
        for k in range(s + 1, N):
            p = parent[k]; a = xs if op[k] == 'J' else ys
            gp = g.get(p, None)
            val = [a[i] * gp[i] for i in range(M)] if gp is not None else [Fr(0)] * M
            for l, c in alpha[k].items():
                if c and l in g:
                    gl = g[l]
                    val = [val[i] - c * gl[i] for i in range(M)]
            g[k] = val
            n = idx[k][0]
            best = max(t * t for t in val) * nrm[ps] / nrm[k] * scale
            if n not in G or best > G[n][0]:
                G[n] = (best, s, k)
    for n in sorted(G):
        best, s, k = G[n]
        print(f"   degree {n:2d}: max_(s,k,i) (L*(z_i)^-1)_(k,s)^2 = 10^{log10_fraction(best):.3f}  (s={idx[s]}, k={idx[k]})  "
              f"[exact rational with {best.numerator.bit_length()}/{best.denominator.bit_length()} bits]", flush=True)
    print(f"# total time {time.time() - t0:.1f}s", flush=True)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
