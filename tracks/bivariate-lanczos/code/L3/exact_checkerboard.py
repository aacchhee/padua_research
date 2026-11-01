"""R04: exact-arithmetic certificates for condition (H) on rational node sets
(default: ordered equispaced Harris-Simanek checkerboards).

Node family 'equi': S_0 = {(-1 + 2i/n, -1 + 2j/(n+1)) : 0<=i<=n, 0<=j<=n+1, i+j even},
M = N_n = (n+1)(n+2)/2 rational points (square case).

For each n (exact Fraction arithmetic via the Q2 class of exact_certificates.py,
imported, not modified):
 1. exact jet matrix (values, gradients) on the monomial basis of Pi_{2n+1};
    exact nullspace S_1; exact rank of the Hessian map on S_1;
 2. DUAL attempt: floating SDP (cvxpy/CLARABEL, tight tolerances) on an
    ORTHONORMALISED basis of the constraint row space, rounding to rationals
    (denominator 10^14), exact least-norm correction onto the exact constraints
    G a = 0, exact PD test of each A_i (a > 0, ac - b^2 > 0);
 3. PRIMAL attempt (only if the dual fails): floating SDP for p in S_1 with
    PD Hessians, exact rational element of S_1 near it, exact PD test.
Verdict per n: '(H) CERTIFIED', 'FAILURE CERTIFIED' or 'UNRESOLVED'. The floating
SDP only proposes candidates; acceptance is exact. The certified minimum over
nodes of det(A_i)/tr(A_i) (a lower bound for lambda_min) is printed as a float.

Usage: python3 exact_checkerboard.py nmin nmax [family]
"""
import sys
import time
from fractions import Fraction as F
import numpy as np
import cvxpy as cp
from exact_certificates import Q2, ZERO, ONE, exps, mono_der, nullspace, rank, hess_entries, is_pd

TOL = dict(tol_gap_abs=1e-12, tol_gap_rel=1e-12, tol_feas=1e-12, max_iter=400)


def nodes_equi(n):
    return [(Q2(F(-1) + F(2 * i, n)), Q2(F(-1) + F(2 * j, n + 1)))
            for i in range(n + 1) for j in range(n + 2) if (i + j) % 2 == 0]


def ratvec(v, den=10 ** 14):
    return [Q2(F(int(round(x * den)), den)) for x in v]


def exact_solve(Mx, rhs):
    K = len(Mx)
    aug = [Mx[r][:] + [rhs[r]] for r in range(K)]
    for c in range(K):
        p = next(i for i in range(c, K) if not aug[i][c].iszero())
        aug[c], aug[p] = aug[p], aug[c]
        inv = aug[c][c].inv()
        aug[c] = [v * inv for v in aug[c]]
        for i in range(K):
            if i != c and not aug[i][c].iszero():
                f = aug[i][c]
                aug[i] = [vi - f * vc for vi, vc in zip(aug[i], aug[c])]
    return [aug[r][K] for r in range(K)]


def dual(nodes, Hs, K):
    M = len(nodes)
    G = []
    for k in range(K):
        row = []
        for i in range(M):
            hxx, hxy, hyy = Hs[i][k]
            row += [hxx, Q2(2) * hxy, hyy]
        G.append(row)
    Gf = np.array([[float(v) for v in r] for r in G])
    U, s, Vt = np.linalg.svd(Gf, full_matrices=False)
    Vt = Vt[s > 1e-13 * s[0]]
    a = cp.Variable(3 * M); t = cp.Variable()
    cons = [Vt @ a == 0, sum(a[3 * i] + a[3 * i + 2] for i in range(M)) == 1]
    for i in range(M):
        Ai = cp.bmat([[a[3 * i], a[3 * i + 1]], [a[3 * i + 1], a[3 * i + 2]]])
        cons.append(Ai - t * np.eye(2) >> 0)
    cp.Problem(cp.Maximize(t), cons).solve(solver=cp.CLARABEL, **TOL)
    if a.value is None:
        return False, None, None
    a0 = ratvec(a.value)
    GG = [[sum((G[r][c] * G[q][c] for c in range(3 * M)), ZERO) for q in range(K)] for r in range(K)]
    Ga0 = [sum((G[r][c] * a0[c] for c in range(3 * M)), ZERO) for r in range(K)]
    y = exact_solve(GG, Ga0)
    ax = [a0[c] - sum((G[r][c] * y[r] for r in range(K)), ZERO) for c in range(3 * M)]
    assert all(sum((G[r][c] * ax[c] for c in range(3 * M)), ZERO).iszero() for r in range(K))
    Ai = [(ax[3 * i], ax[3 * i + 1], ax[3 * i + 2]) for i in range(M)]
    ok = all(is_pd(h) for h in Ai)
    marg = min(float(h[0] * h[2] - h[1] * h[1]) / float(h[0] + h[2]) for h in Ai)
    return ok, float(t.value), marg


def primal(nodes, S, E, Hs, K):
    M = len(nodes)
    Hf = np.array([[[float(v) for v in Hs[i][k]] for k in range(K)] for i in range(M)])  # M x K x 3
    # orthonormalise S_1 coordinates w.r.t. the stacked Hessian map for conditioning
    B = Hf.transpose(0, 2, 1).reshape(3 * M, K)
    Qb, Rb = np.linalg.qr(B)
    c = cp.Variable(K); lam = cp.Variable()
    cons = [cp.norm(c, 'inf') <= 1]
    for i in range(M):
        h = Qb[3 * i:3 * i + 3] @ c
        Hi = cp.bmat([[h[0], h[1]], [h[1], h[2]]])
        cons.append(0.5 * (Hi + Hi.T) - lam * np.eye(2) >> 0)
    cp.Problem(cp.Maximize(lam), cons).solve(solver=cp.CLARABEL, **TOL)
    if c.value is None:
        return False, None
    coords = np.linalg.solve(Rb, c.value)  # coordinates in the exact basis
    cr = ratvec(coords / np.max(np.abs(coords)), 10 ** 12)
    H = [tuple(sum((cr[k] * Hs[i][k][q] for k in range(K)), ZERO) for q in range(3)) for i in range(M)]
    return all(is_pd(h) for h in H), float(lam.value)


def run(n, family):
    t0 = time.time()
    d = 2 * n + 1
    E = exps(d)
    nodes = nodes_equi(n) if family == 'equi' else None
    J = []
    for (x, y) in nodes:
        for (dx, dy) in [(0, 0), (1, 0), (0, 1)]:
            J.append([mono_der(x, y, a, b, dx, dy) for (a, b) in E])
    S, rk = nullspace(J, len(E))
    K = len(S)
    Hs = [[hess_entries(z, s, E) for s in S] for z in nodes]
    Hmat = [[Hs[i][k][q] for k in range(K)] for i in range(len(nodes)) for q in range(3)]
    hr = rank(Hmat, K)
    line = f"{family} n={n}: M={len(nodes)} D={len(E)} rank J={rk} dim S1={K} (exp {n*(n+1)//2}) rank Hess|S1={hr}"
    ok, t, marg = dual(nodes, Hs, K)
    if ok and hr == K:
        print(line + f" | DUAL exact PASS (float t={t:.3e}; exact min det/tr over nodes={marg:.3e}) => (H) CERTIFIED"
              f" [{time.time()-t0:.0f}s]", flush=True)
        return
    okp, lam = primal(nodes, S, E, Hs, K)
    if okp:
        print(line + f" | dual {'FAIL' if not ok else 'n/a'} (float t={t}); PRIMAL exact PASS (float lam={lam:.3e})"
              f" => FAILURE CERTIFIED [{time.time()-t0:.0f}s]", flush=True)
        return
    print(line + f" | dual exact {'PASS' if ok else 'FAIL'} (float t={t}, margin {marg}); primal exact FAIL "
          f"(float lam={lam}) => UNRESOLVED [{time.time()-t0:.0f}s]", flush=True)


def main():
    nmin = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    family = sys.argv[3] if len(sys.argv) > 3 else 'equi'
    print(f"exact_checkerboard family={family} n={nmin}..{nmax}; numpy {np.__version__}, cvxpy {cp.__version__}")
    for n in range(nmin, nmax + 1):
        run(n, family)


if __name__ == '__main__':
    main()
