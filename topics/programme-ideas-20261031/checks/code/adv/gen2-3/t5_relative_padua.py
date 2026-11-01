"""Generator's entry point 2 (relative perturbation), run and reduced to its univariate content.

Facts checked: (i) the Padua pair (n = 8, cubature weights) is sparse with <= 2 nonzeros per column, zero
diagonal, and its graph is ACYCLIC (a union of paths), so Demmel-Gragg-type high relative accuracy of the
eigenvalues of H_x from its entries is the known univariate theorem; (ii) under relative entrywise
perturbation eta of H_x alone the relative eigenvalue changes stay O(eta) for Padua, while for a random-node
pair (nonzero diagonal, cyclic graph) eigenvalues near 0 move by O(eta ||H||), i.e. relative change
~ eta/|x_i| -- the standard 1-D counterexample; (iii) perturbing H_x alone destroys commutation, so "joint
eigenvalues" of the perturbed pair are undefined: T4 can only be a statement about H_x and H_y separately
plus the pairing.

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). Adversarial check gen2-3, 2026-11-01.
Scope: Padua n = 8 (N = 45), random n = 8; eta = 1e-10, 1e-6; 20 random relative perturbations each.
"""
import numpy as np
from pairs import padua_points, padua_exactness_residual, pair_from_nodes, random_pair

n = 8
print(f"Padua n={n}: exactness residual on Pi_{2*n-1} of the constructed weights = {padua_exactness_residual(n):.1e}")
x, y, w = padua_points(n)
Hx, Hy, deg = pair_from_nodes(x, y, w, n)
N = Hx.shape[0]
tol = 1e-12
for name, H in [("Hx", Hx), ("Hy", Hy)]:
    A = np.abs(H) > tol
    nnz_col = A.sum(axis=0)
    diag = np.abs(np.diag(H)).max()
    # graph acyclicity: edges = nnz offdiag / 2; components via union-find
    parent = list(range(N))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    edges = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i, j]:
                edges += 1
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    comps = len({find(i) for i in range(N)})
    print(f"  {name}: max nonzeros/column={nnz_col.max()}, max|diag|={diag:.1e}, edges={edges}, components={comps}, acyclic={'yes' if edges == N - comps else 'NO'}; distinct |entries|: {np.unique(np.round(np.abs(H[A]),6))}")
print(f"  ||[Hx,Hy]||_2 = {np.linalg.norm(Hx@Hy-Hy@Hx,2):.1e}")

def rel_eig_change(H, eta, trials=20, seed=0):
    rng = np.random.default_rng(seed)
    ev0 = np.linalg.eigvalsh(H)
    worst = 0.0; worst_abs = 0.0
    for _ in range(trials):
        F = rng.uniform(-1, 1, H.shape); F = (F + F.T) / 2
        Hp = H * (1 + eta * F)  # relative entrywise, symmetric
        ev = np.linalg.eigvalsh(Hp)
        nz = np.abs(ev0) > 1e-8  # exclude structurally zero eigenvalues (Padua: odd paths), whose relative change is 0/0
        rel = np.abs(ev - ev0)[nz] / np.abs(ev0)[nz]
        worst = max(worst, rel.max()); worst_abs = max(worst_abs, np.abs(ev - ev0)[~nz].max() if (~nz).any() else 0.0)
    return worst, worst_abs, np.abs(ev0[nz]).min()

Hxr, Hyr, degr, xr, yr, wr = random_pair(n, seed=1)
for eta in [1e-10, 1e-6]:
    wp, ap, mp = rel_eig_change(Hx, eta)
    wr_, ar, mr = rel_eig_change(Hxr, eta)
    print(f"eta={eta:.0e}: Padua Hx  max rel change of nonzero eigenvalues = {wp:.1e} (= {wp/eta:.1f} eta; min nonzero |x_i|={mp:.1e}; the structurally zero eigenvalues moved by at most {ap:.1e})")
    print(f"           random Hx max rel eigenvalue change = {wr_:.1e} (= {wr_/eta:.1e} eta; min|x_i|={mr:.1e}; max|diag|={np.abs(np.diag(Hxr)).max():.2f}; no node near 0 in this seed)")
    # random nodes with one node at x = 1e-6: eigenvalue near 0 produced by a nonzero-diagonal, cyclic H_x
    rng2 = np.random.default_rng(21); xs = rng2.uniform(-1, 1, N); ys = rng2.uniform(-1, 1, N); ws = rng2.uniform(0.5, 1.5, N); xs[0] = 1e-6
    Hxs, Hys, _ = pair_from_nodes(xs, ys, ws, n)
    ws_, as_, ms_ = rel_eig_change(Hxs, eta)
    print(f"           random Hx with a node at x=1e-6: max rel change = {ws_:.1e} (= {ws_/eta:.1e} eta), i.e. no relative accuracy from the entries")
    # 1-D Jacobi counterexample
    T = np.array([[1.0, 1.0], [1.0, 1.0 + 1e-6]]); e0 = np.linalg.eigvalsh(T); Tp = T.copy(); Tp[1, 1] *= (1 + eta); e1 = np.linalg.eigvalsh(Tp)
    print(f"           2x2 Jacobi [[1,1],[1,1+1e-6]]: small eigenvalue {e0[0]:.3e} changes relatively by {abs(e1[0]-e0[0])/abs(e0[0]):.1e} = {abs(e1[0]-e0[0])/abs(e0[0])/eta:.1e} eta under a relative perturbation of one diagonal entry")
# (iii) commutation lost under entrywise perturbation of Hx alone
rng = np.random.default_rng(1); F = rng.uniform(-1, 1, (N, N)); F = (F + F.T) / 2
Hxp = Hx * (1 + 1e-6 * F)
print(f"commutator after relative perturbation eta=1e-6 of Hx alone (Padua): {np.linalg.norm(Hxp@Hy-Hy@Hxp,2):.1e} (joint eigenvalues of the perturbed pair are undefined)")
# x-coordinates of the joint spectrum ARE the eigenvalues of Hx
print(f"max |sorted eig(Hx) - sorted x| = {np.abs(np.sort(np.linalg.eigvalsh(Hx)) - np.sort(x)).max():.1e}  (Padua x-coordinates have multiplicity: {len(np.unique(np.round(x,12)))} distinct values among {N})")
