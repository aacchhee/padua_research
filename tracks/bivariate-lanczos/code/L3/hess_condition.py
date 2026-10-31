"""Decide condition (H) numerically (MEASURED) for a node set and degree n.

S_1 = {p in Pi_{2n+1}: p(z_i) = 0, grad p(z_i) = 0 for all nodes}.
(H): no nonzero p in S_1 with Hess p(z_i) >= 0 (PSD) at every node.
Alternative (proved in theory file 3nn-moment-cone-inradius):
 (H) <=> [Hess map injective on S_1] and [exists A_i > 0 (2x2 PD) with
         sum_i <A_i, Hess_i p> = 0 for all p in S_1].
Dual SDP:   t_D = max t  s.t. A_i >= t I, sum_i tr A_i = 1, linear equalities.
Primal SDP: l_P = max l  s.t. Hess_i(S_1 c) >= l I, ||c||_inf <= 1.
t_D > 0 => (H) holds;  l_P > 0 => robust failure (obstruction regime).

Usage: python3 hess_condition.py [family] [nmax] [seed]
  family in {padua, random, randtri}
"""
import sys
import numpy as np
import cvxpy as cp
from l3lib import padua, jet_matrix, nullspace, jet_rows, dimPi


def analyse(nodes, n, verbose=True):
    d = 2 * n + 1
    J = jet_matrix(nodes, d, 1)
    S, s = nullspace(J, rtol=1e-11)
    dimS = S.shape[1]
    M = len(nodes)
    out = dict(M=M, D=dimPi(d), threeM=3 * M, expected=max(0, dimPi(d) - 3 * M), dimS1=dimS)
    if dimS == 0:
        out.update(tD=None, lP=None, kerHess=0)
        return out
    # Hessian map: for each node, 3 x dimS matrix (hxx, hxy, hyy) of basis elements
    Hm = [jet_rows(z, d, 2) @ S for z in nodes]
    Hstack = np.vstack(Hm)
    kernel, sv = nullspace(Hstack, rtol=1e-10)
    out['kerHess'] = kernel.shape[1]
    # dual
    A = [cp.Variable((2, 2), symmetric=True) for _ in range(M)]
    t = cp.Variable()
    cons = [A[i] - t * np.eye(2) >> 0 for i in range(M)]
    cons.append(sum(cp.trace(A[i]) for i in range(M)) == 1)
    for k in range(dimS):
        expr = 0
        for i in range(M):
            hxx, hxy, hyy = Hm[i][:, k]
            expr = expr + A[i][0, 0] * hxx + 2 * A[i][0, 1] * hxy + A[i][1, 1] * hyy
        cons.append(expr == 0)
    prob = cp.Problem(cp.Maximize(t), cons)
    prob.solve(solver=cp.CLARABEL)
    out['tD'] = float(t.value) if t.value is not None else None
    out['dual_status'] = prob.status
    # primal
    c = cp.Variable(dimS)
    lam = cp.Variable()
    cons2 = [cp.norm(c, 'inf') <= 1]
    for i in range(M):
        hxx = Hm[i][0] @ c
        hxy = Hm[i][1] @ c
        hyy = Hm[i][2] @ c
        Hi = cp.bmat([[hxx, hxy], [hxy, hyy]])
        cons2.append(0.5 * (Hi + Hi.T) - lam * np.eye(2) >> 0)
    prob2 = cp.Problem(cp.Maximize(lam), cons2)
    prob2.solve(solver=cp.CLARABEL)
    out['lP'] = float(lam.value) if lam.value is not None else None
    out['primal_status'] = prob2.status
    out['sv_tail'] = s[-(dimS + 2):].tolist() if s.size >= dimS + 2 else s.tolist()
    return out


def main():
    fam = sys.argv[1] if len(sys.argv) > 1 else 'padua'
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    rng = np.random.default_rng(seed)
    print(f"family={fam} nmax={nmax} seed={seed} numpy={np.__version__} cvxpy={cp.__version__}")
    for n in range(1, nmax + 1):
        if fam == 'padua':
            nodes = padua(n)
        elif fam == 'random':
            nodes = rng.uniform(-1, 1, size=(dimPi(n), 2))
        else:
            raise SystemExit('unknown family')
        r = analyse(nodes, n)
        print(f"n={n} M={r['M']} D={r['D']} 3M={r['threeM']} expected_dimS1={r['expected']} "
              f"dimS1={r['dimS1']} kerHess={r['kerHess']} tD={r['tD']} lP={r['lP']} "
              f"[{r.get('dual_status')},{r.get('primal_status')}]")


if __name__ == '__main__':
    main()
