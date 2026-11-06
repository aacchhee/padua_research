# Supplementary structured CC check

2026-11-06. Codex supplementary checker, requested gpt-6-astra high;
actual runtime model/effort metadata unexposed. Rules/source corpus
`2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`; raw scan pre-registration
`e2652c3`. This is a finite algebra/implementation review, with no new
mechanism, novelty or asymptotic claim; a novelty gate is not applicable.
The required Claude audit is separate.

**PASS within this scope.** Independently reconstructed the coordinate
change and rank-one constraint, inspected S4_structured.py and its finite
validation receipt, and actually executed separate checks at
N=101,1281,8192,8193. No unresolved finding within this bounded scope.

## Reconstruction of the finite reduction

Let C_kj=cos(pi k j/N), D=diag(1/2,1,...,1,1/2), and
A=(2/N)DCD. The unnormalized SciPy DCT-I is 2CD, so the producer's
`transform` is multiplication by A. A is symmetric. For nodal values y,
the Chebyshev coefficient vector is c=Ay. Consequently quadrature
weights are w=A mu, where mu_k is the exact Lebesgue Chebyshev moment.
With z=W^(1/2)y, the quadrature norm is z^T z and the continuous norm
is z^T W^(-1/2) A T A W^(-1/2) z, with
T_ij=(mu_|i-j|+mu_i+j)/2.

The excluded degree-N coefficient is
c_N=(1/N) sum_j d_j(-1)^j z_j/sqrt(w_j). Thus c_N=0 exactly means
z is orthogonal to the producer's normalized h. Writing P=I-hh^T,
the implemented operator is

    K = P W^(-1/2) A T A W^(-1/2) P + hh^T.

On h-perp its eigenvalues are the reciprocal CC generalized eigenvalues
on degree <=N-1. On span(h) it has an artificial eigenvalue 1. This
inserted eigenvalue cannot change either extreme: the constant polynomial
belongs to the physical space and has both norms equal to 2, so the
physical Rayleigh range contains 1. This also handles equality cases;
for N=1 the physical spectrum is itself {1}. N>=1 and positive CC
weights are required. This checker executed N>=101, not N=1.

The Hankel multiply is correct: setting l=N-j turns H_ij=mu_i+j into
a Toeplitz matrix with first column mu_N,...,mu_2N and first row
mu_N,...,mu_0, applied to the reversed coefficient vector. It adds to
the ordinary moment Toeplitz product, then divides by two. Projection
is applied on both sides as required for a symmetric restriction.

This reconstruction verifies existing finite algebra; it does not supply
an asymptotic operator model or an error theorem for floating arithmetic.

## Independent execution

Developer confirmed S4_structured.py frozen at SHA-256
`40e9ffc00edbf8ff9009cfa133646a69815f8423ad8baf4bdd23a69ae604bd8d`.
The [checker](code/check_S4_structured.py) pins this and the historical
dense CC reference implementation before and after execution.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/check_S4_structured.py --output topics/padua-mz-sharp-constants-20261106/evidence/check-S4-structured.json
```

The command ran from `/workspace/sharp-work` and exited successfully.
Seed base20261107 differs from the producer's20261106; tolerance2e-12,
ncv40, maxiter3000. Python3.12.14, NumPy2.3.5, SciPy1.17.0. Full
provenance, timings and output are in the [receipt](evidence/check-S4-structured.json).
No fit was computed or disclosed to S1/S2.

The checker independently constructs 32-mode Chebyshev polynomials on
the CC grid using cosine evaluations and computes their continuous
quadratic forms by direct scalar moment sums. It compares those forms
with z^T K z at every size. Dense generalized-pencil extrema are also
computed at N101 and1281. At the larger sizes it checks changed-seed
extrema, residuals, constraint, bilinear symmetry and sparse forms;
there is no large dense reference.

| N | Minimum | Maximum | Dense relative discrepancy, if tested |
|---:|---:|---:|---:|
| 101 | 0.20386941110031123 | 1.0044381931618709 | 1.100e-14 |
| 1281 | 0.11761761770840215 | 1.0044369899536527 | 1.973e-13 |
| 8192 | 0.08483487997906558 | 1.0044369735014316 | not tested |
| 8193 | 0.08483319180788926 | 1.0044369724002449 | not tested |

Maximum sparse-form relative discrepancy:3.031e-14. Maximum bilinear
symmetry discrepancy:2.989e-16. Maximum inverse eigenpair residual:
5.904e-13. Maximum eigenvector constraint residual:1.895e-14. All
pass the pre-execution guards:1e-10 for dense/form/symmetry comparisons
and1e-9 for inverse residual/constraint. The artificial unit eigenvector
and sparse-polynomial constraint were recorded as additional diagnostics.
Both input hashes remained unchanged.

- Checker SHA-256: `0efc2b3ff7ed78b81e044f7035275170c054d445223ae400018a086e0441fa01`.
- Receipt SHA-256: `eeb1a9a894be90c199c64cff724cb7966109e742295cdd2ac7d18e10cbcbef9a`.
- Receipt size:6198 bytes; no vectors or dense matrices retained.

## Limits

All numerical observations are **MEASURED**. Small residuals and seeded
ARPACK convergence do not provide rigorous extremal enclosures. The
larger finite checks support the implementation but do not certify
untested sizes, prove uniform floating accuracy, establish any sharp
limit, or pass a fit-based K gate. Further raw-scan interpretation and
selective high-precision checks remain the developer's separately
recorded work.
