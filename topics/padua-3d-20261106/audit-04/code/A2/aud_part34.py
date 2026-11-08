"""Part 3: own Lebesgue evaluator (Legendre product basis, lstsq-free LU solve) on 21^3
Chebyshev-Lobatto tensor mesh. Part 4: symmetry orbits of selected n5/n7 generators."""
import sys, math, json, itertools as it
import numpy as np
from numpy.polynomial import legendre as Lg
import scipy.linalg as la
sys.path.insert(0, sys.argv[1])
from aud_common import total_modes, fold_nodes

def leg_basis(P, n):
    P = np.asarray(P, float)
    tabs = [Lg.legvander(P[:, j], n) * np.sqrt(2 * np.arange(n + 1) + 1) for j in range(3)]
    return np.column_stack([tabs[0][:, a] * tabs[1][:, b] * tabs[2][:, c] for a, b, c in total_modes(n)])

AX = np.cos(np.pi * np.arange(21) / 20)
MESH = np.array(list(it.product(AX, repeat=3)))

def lebesgue(P, n):
    V = leg_basis(P, n); E = leg_basis(MESH, n)
    lu = la.lu_factor(V.T)
    Lc = la.lu_solve(lu, E.T)          # cardinal values, N x mesh
    s = np.linalg.svd(V, compute_uv=False)
    return float(np.abs(Lc).sum(axis=0).max()), float(s[0] / s[-1])

def hs_points(n, z):
    N = math.comb(n + 3, 3); M = 2 * N
    L, nodes = fold_nodes(z, z, 2 * M, M)
    assert len(nodes) == N
    return np.cos(2 * np.pi * np.array(nodes, float) / L)

def cheb_logabsdet(n, z):
    P = hs_points(n, z)
    tabs = [np.cos(np.outer(np.arccos(np.clip(P[:, j], -1, 1)), np.arange(n + 1))) for j in range(3)]
    V = np.column_stack([tabs[0][:, a] * tabs[1][:, b] * tabs[2][:, c] for a, b, c in total_modes(n)])
    return float(np.linalg.slogdet(V)[1] + sum(sum(x > 0 for x in al) for al in total_modes(n)) * math.log(2) / 2)

def orbit(n, z):
    N = math.comb(n + 3, 3); M = 2 * N; P = 2 * M
    units = [u for u in range(1, P) if math.gcd(u, P) == 1]
    out = set()
    for u in units:
        w = [(u * x) % P for x in z]
        for perm in it.permutations(range(3)):
            v = [w[i] for i in perm]
            # each coordinate: cos same under v->-v; reflection under v->M-v
            opts = [sorted({min(x, P - x), min((M - x) % P, P - (M - x) % P)}) for x in v]
            if 1 not in opts[0]:
                continue
            for b in opts[1]:
                for c in opts[2]:
                    if 1 <= b < c < M:
                        out.add((1, b, c))
    return sorted(out)

res = {}
# n3 survivors: quality with own evaluator
surv = [(1,4,11),(1,4,29),(1,6,15),(1,6,25),(1,11,36),(1,15,34),(1,25,34),(1,29,36)]
res['n3_survivors'] = {str(z): lebesgue(hs_points(3, z), 3) for z in surv}
res['n3_orbits'] = {str(z): orbit(3, z) for z in [(1,4,11),(1,6,15)]}
for n, z in [(5, (1,10,49)), (7, (1,17,212))]:
    orb = orbit(n, z)
    res['n%d' % n] = {'selected': list(z), 'orbit': orb, 'lexmin': list(orb[0]),
        'orbit_logabsdet_float': {str(o): cheb_logabsdet(n, o) for o in orb},
        'lebesgue_cond_selected': lebesgue(hs_points(n, z), n),
        'lebesgue_cond_lexmin': lebesgue(hs_points(n, orb[0]), n)}
# controls with own evaluator (control sets defined as in the frozen helper)
def leja_axis(v):
    rem = list(range(len(v))); order = [rem.pop(0)]
    while rem:
        best = max(rem, key=lambda i: (np.prod([abs(v[i] - v[j]) for j in order]), -i)); order.append(best); rem.remove(best)
    return v[order]
def graded(n):
    return [(a, b, d - a - b) for d in range(n + 1) for a in range(d + 1) for b in range(d - a + 1)]
ctrl = {}
for n in (3, 5, 7):
    ax = leja_axis(np.cos(np.pi * np.arange(n + 1) / n))
    leja = np.array([[ax[a], ax[b], ax[c]] for a, b, c in graded(n)])
    can = np.array(list(it.product(np.cos(np.pi * np.arange(2 * n + 1) / (2 * n)), repeat=3)))
    th = np.arccos(np.clip(can, -1, 1))
    T = [np.cos(np.outer(th[:, j], np.arange(n + 1))) for j in range(3)]
    A = np.column_stack([T[0][:, a] * T[1][:, b] * T[2][:, c] for a, b, c in graded(n)])
    _, _, piv = la.qr(A.T, pivoting=True, mode='economic')
    N = math.comb(n + 3, 3)
    ctrl[n] = {'Leja': lebesgue(leja, n), 'QR': lebesgue(can[piv[:N]], n)}
res['controls'] = ctrl
json.dump(res, open(sys.argv[2], 'w'), indent=1)
print(json.dumps(res, indent=0)[:6000])
