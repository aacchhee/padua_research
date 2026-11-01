"""Exact rational witnesses for T-B5, n=2,...,6; no floating arithmetic.

Nodes (t,t^(n+1)), t=1,...,N, weights 1/N. Construct the rational
monic orthogonal basis by LDL^T, verify the commuting pattern pair after
diagonal scaling, and compute the reduced spectral constraint rank exactly.
The full original commutator-map rank is DEDUCED from the written reduction,
not computed by forming a large radical-valued commutator matrix.
"""
import hashlib
import json
import platform
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def rational_dm(matrix):
    return DomainMatrix.from_Matrix(matrix).convert_to(sp.QQ)


def check(n):
    modes = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    N = len(modes)
    index = {m: j for j, m in enumerate(modes)}
    x = list(range(1, N + 1))
    y = [t ** (n + 1) for t in x]
    exponents = [a + (n + 1) * b for a, b in modes]
    assert len(set(exponents)) == N
    V = sp.Matrix([[t ** e for e in exponents] for t in x])
    determinant = V.det(method="domain-ge")
    assert determinant != 0
    inverse = rational_dm(V).inv().to_Matrix()
    assert V * inverse == sp.eye(N)

    G = V.T * V / N
    lower, D = G.LDLdecomposition(hermitian=False)
    C = rational_dm(lower.T).inv().to_Matrix()
    P = V * C  # evaluations of the monic orthogonal polynomials
    assert P.T * P / N == D
    assert all(D[j, j] > 0 for j in range(N))
    Ax = D.inv() * (P.T * sp.diag(*x) * P / N)
    Ay = D.inv() * (P.T * sp.diag(*y) * P / N)
    assert D * Ax == Ax.T * D
    assert D * Ay == Ay.T * D
    assert Ax * Ay == Ay * Ax

    pix = [index[(a + 1, b)] if a + b < n else None for a, b in modes]
    piy = [index[(a, b + 1)] if a + b < n else None for a, b in modes]

    def pattern(pi):
        return [[(pi[j] is None or i <= pi[j]) and (pi[i] is None or j <= pi[i])
                 for j in range(N)] for i in range(N)]

    Px, Py = pattern(pix), pattern(piy)
    assert all(not Px[i][j] or Py[i][j] for i in range(N) for j in range(N))
    assert [i for i in range(N) if Py[i][0]] == [0, 1, 2]
    for A, mask, pi in ((Ax, Px, pix), (Ay, Py, piy)):
        assert all(mask[i][j] or A[i, j] == 0 for i in range(N) for j in range(N))
        # In the monic basis all leading multiplication pivots are exactly one.
        # Orthonormal pivots are sqrt(D[pi[j],pi[j]] / D[j,j]) > 0.
        assert all(A[pi[j], j] == 1 for j in range(N) if pi[j] is not None)

    constraint = inverse[3:, :]
    rank = rational_dm(constraint).rank()
    assert rank == N - 3
    assert constraint * V[:, :3] == sp.zeros(N - 3, 3)
    assert rational_dm(V[:, :3]).rank() == 3
    variables = sum(Py[i][j] for i in range(N) for j in range(i, N))
    rational_pair_text = "\n".join(str(entry) for M in (D, Ax, Ay) for entry in M)
    return {"n": n, "N": N, "nodes": "(t,t^(n+1)), t=1,...,N", "weight": f"1/{N}",
            "det_V": str(determinant), "distinct_x": True,
            "positive_LDL_norms": True, "exact_commutation": True,
            "exact_self_adjointness_for_D": True, "pattern_violations": 0,
            "positive_orthonormal_pivots": True, "first_column_pattern_y": [0, 1, 2],
            "symmetric_pattern_y_variables": variables,
            "computed_reduced_constraint_shape": [N - 3, N],
            "computed_reduced_constraint_rank": int(rank),
            "reduced_nullspace_equals_affine_values": True,
            "full_commutant_dimension_by_proved_reduction": 3,
            "full_commutator_rank_by_proved_reduction": variables - 3,
            "rational_pair_sha256": hashlib.sha256(rational_pair_text.encode()).hexdigest()}


if __name__ == "__main__":
    output = {"python": platform.python_version(), "sympy": sp.__version__,
              "arithmetic": "integer and rational, with rational LDL diagonal scaling",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "rank_method": "direct rank of last N-3 rows of V^-1; full map rank deduced from written equivalence",
              "results": [check(n) for n in range(2, 7)]}
    print(json.dumps(output, indent=2))
