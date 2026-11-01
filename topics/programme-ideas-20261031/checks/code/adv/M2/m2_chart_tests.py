"""M2 adversarial script 3: entry charts of the commuting generalized-Hessenberg pair.

Model: claude-fable-5-1, effort max (as requested by the orchestrator) . Adversarial check . 2026-11-01

(a) Which blocks determine the data? Numerical Jacobian rank of (x, y, w) -> selected entries of (Hx, Hy), random
    real nodes, M = N, n = 3..6 (central differences, step 1e-6, gap criterion):
      top diagonal blocks (B_{n,x}, B_{n,y})            : 2N entries   (the 'rim' of Kreuzer-Robbiano 2025 Prop. 5.6 in
                                                                        orthonormal coordinates)
      top blocks plus coupling blocks A_{n-1,x}, A_{n-1,y}: 2N + N + n entries
      all pattern entries                               : expected 3N-1
(b) Chasability of an entry chart S (|S| = 3N-1, chosen greedily by Jacobian rank in three orders: recurrence order,
    reverse order, top blocks first): the linearised commutator equations in the remaining unknowns U \\ S are square-
    rank-full by construction; we ask whether they can be solved one unknown at a time (structural triangularity):
    maximum bipartite matching equations<->unknowns, then strongly connected components of the matched digraph.
    Largest SCC = size of the smallest block that must be solved simultaneously.
Scope: n = 3..6 (N = 10..28), floating point, generic random nodes; MEASURED only.
Run: python3 -I m2_chart_tests.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching, connected_components
from m2_common import *

def entries_vector(x, y, w, n, sel):
    Q, R, Hx, Hy = pair_from_nodes(x, y, w, n)
    v = []
    for (which, i, j) in sel:
        v.append((Hx if which == 'x' else Hy)[i, j])
    return np.array(v)

def jac_rank(x, y, w, n, sel, h=1e-6):
    p = np.concatenate([x, y, w]); m = len(p)
    cols = []
    for t in range(m):
        pp = p.copy(); pm = p.copy(); pp[t] += h; pm[t] -= h
        fp = entries_vector(pp[:len(x)], pp[len(x):2*len(x)], pp[2*len(x):], n, sel)
        fm = entries_vector(pm[:len(x)], pm[len(x):2*len(x)], pm[2*len(x):], n, sel)
        cols.append((fp - fm) / (2 * h))
    J = np.array(cols).T
    s = np.linalg.svd(J, compute_uv=False)
    # gap criterion
    tol = 1e-6 * s[0]
    r = int(np.sum(s > tol))
    gap = (s[r-1] / s[r]) if r < len(s) and s[r] > 0 else np.inf
    return r, gap, J

def all_pattern_entries(n):
    Px, Py = pattern(n, 'x'), pattern(n, 'y')
    sel = [('x', i, j) for (i, j) in sym_basis(Px)] + [('y', i, j) for (i, j) in sym_basis(Py)]
    return sel

def degree_of(n):
    return np.array([a + b for a, b in monomials(n)])

def part_a(n, rng):
    N = dim_pi(n); deg = degree_of(n)
    x, y, w = random_nodes(n, rng)
    sel_all = all_pattern_entries(n)
    sel_top = [e for e in sel_all if deg[e[1]] == n and deg[e[2]] == n]
    sel_topA = [e for e in sel_all if (deg[e[1]] >= n - 1 and deg[e[2]] >= n - 1) and not (deg[e[1]] == n - 1 and deg[e[2]] == n - 1)]
    r_top, g_top, _ = jac_rank(x, y, w, n, sel_top)
    r_topA, g_topA, _ = jac_rank(x, y, w, n, sel_topA)
    r_all, g_all, J_all = jac_rank(x, y, w, n, sel_all)
    print(f"n={n} N={N}: rank(top B blocks, {len(sel_top)} entries) = {r_top} (gap {g_top:.1e}); "
          f"rank(top B + A_(n-1) blocks, {len(sel_topA)} entries) = {r_topA} (gap {g_topA:.1e}); "
          f"rank(all {len(sel_all)} pattern entries) = {r_all} (gap {g_all:.1e}); 2N={2*N}, 3N-1={3*N-1}")
    return x, y, w, sel_all, J_all

def greedy_chart(J_all, order, target):
    """Greedy selection of rows of J_all (entries) in the given order while the rank increases."""
    chosen = []
    basis = np.zeros((0, J_all.shape[1]))
    for r in order:
        cand = np.vstack([basis, J_all[r:r+1, :]])
        s = np.linalg.svd(cand, compute_uv=False)
        if s[-1] > 1e-7 * s[0]:
            basis = cand; chosen.append(r)
            if len(chosen) == target:
                break
    return chosen

def commutator_jacobian(Hx, Hy, sel):
    """Linearised commutator equations (strict upper triangle of [Hx,Hy]) w.r.t. the symmetric entry variables in sel."""
    N = Hx.shape[0]
    eqs = [(a, b) for a in range(N) for b in range(a + 1, N)]
    eidx = {e: k for k, e in enumerate(eqs)}
    J = np.zeros((len(eqs), len(sel)))
    for c, (which, i, j) in enumerate(sel):
        E = np.zeros((N, N)); E[i, j] = 1; E[j, i] = 1
        C = (E @ Hy - Hy @ E) if which == 'x' else (Hx @ E - E @ Hx)
        for (a, b) in eqs:
            if abs(C[a, b]) > 1e-13:
                J[eidx[(a, b)], c] = C[a, b]
    return J

def triangularity(J):
    """Structural analysis: J (equations x unknowns). Returns (matched unknowns, largest SCC, #singleton SCCs)."""
    A = csr_matrix((np.abs(J) > 1e-12).astype(float))
    match = maximum_bipartite_matching(A, perm_type='row')   # for each column (unknown) the matched row, or -1
    m = int(np.sum(match >= 0))
    nunk = J.shape[1]
    # digraph on unknowns: u -> u' if equation matched to u involves u'
    rows, cols = [], []
    for u in range(nunk):
        e = match[u]
        if e < 0:
            continue
        for u2 in np.nonzero(np.abs(J[e, :]) > 1e-12)[0]:
            if u2 != u and match[u2] >= 0:
                rows.append(u); cols.append(u2)
    G = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(nunk, nunk))
    ncomp, labels = connected_components(G, directed=True, connection='strong')
    sizes = np.bincount(labels)
    # ignore unmatched singletons
    matched_mask = match >= 0
    sizes_matched = np.bincount(labels[matched_mask]) if m > 0 else np.array([0])
    return m, int(sizes_matched.max()), int(np.sum(sizes_matched == 1))

def part_b(n, x, y, w, sel_all, J_all):
    N = dim_pi(n); deg = degree_of(n)
    Q, R, Hx, Hy = pair_from_nodes(x, y, w, n)
    target = 3 * N - 1
    # orders
    # recurrence order: by column j (graded), within column by row i, Hx before Hy
    rec_order = sorted(range(len(sel_all)), key=lambda r: (sel_all[r][2], 0 if sel_all[r][0] == 'x' else 1, sel_all[r][1]))
    rev_order = rec_order[::-1]
    top_order = sorted(range(len(sel_all)), key=lambda r: (-(deg[sel_all[r][1]] + deg[sel_all[r][2]]), sel_all[r][2], sel_all[r][1]))
    Jc = commutator_jacobian(Hx, Hy, sel_all)
    for name, order in (('recurrence order', rec_order), ('reverse order', rev_order), ('top blocks first', top_order)):
        S = greedy_chart(J_all, order, target)
        rest = [r for r in range(len(sel_all)) if r not in set(S)]
        Jr = Jc[:, rest]
        rk, s = numrank(Jr, 1e-9)
        m, big, singles = triangularity(Jr)
        print(f"  n={n}: chart '{name}': |S|={len(S)} (target {target}); unknowns outside S: {len(rest)}; "
              f"rank of linearised commutator system in them: {rk} ({'determined' if rk == len(rest) else 'UNDERDETERMINED'}); "
              f"matched {m}; largest irreducible block {big}; singleton blocks {singles}")

def main():
    rng = np.random.default_rng(7)
    for n in range(3, 7):
        x, y, w, sel_all, J_all = part_a(n, rng)
        part_b(n, x, y, w, sel_all, J_all)

if __name__ == '__main__':
    main()
