# PD-T?mz2d-frontier-codex-90 — Certified signed Padua spectrum at m60

ID kind: PD-T (provisional; orchestrator assigns final ID).
Aliases: G1 hybrid native certificate; C GMP pencil and FLINT signed-dominance congruence; finite m60 extension.
Split from: verification support for PD-T028/PD-T110; their universal targets remain unchanged and OPEN.
Split into: m80 remains a separate CONDITIONAL record, PD-T?mz2d-frontier-codex-91 in `cert-finite-extension-m80.md`.

## Statement

For the fixed even-checkerboard signed Lebesgue Padua rule Q_m on total-degree Π_(m−1), the generalized extreme eigenvalues of its exact product-Chebyshev pencil (Q,H) lie in these strict open intervals:

| m | n | Dimension | Minimum | Maximum |
|---|---|---:|---|---|
| 60 | 59 | 1,830 | (0.188593,0.188594) | (1.802011,1.802012) |

Every decimal endpoint is an exact terminating rational. The claim is restricted to m60. It does not assert a complete integer range 2..60 or any m80 case.

## Definitions

Conventions and signs are exactly `topics/padua-mz-2d-20261101/definitions.md`. H is the continuous dx dy Gram matrix, Q the signed quadrature Gram matrix in basis T_a(x)T_b(y), a+b≤m−1. This Q is the matrix called R in some earlier records. H is positive definite; generalized eigenvalues equal the Legendre Gram eigenvalues by PD-T106. Inertia is ordered (negative,zero,positive). R below denotes only an integer transformation proposal.

## Assumptions

Precisely m=60, n=59, with the unchanged PD-T106 alias formula. Computational trust: recorded compiler and native C executable, GMP exact rational/integer arithmetic, Python integer/Fraction conversion/control, and FLINT exact integer matrix kernels. Numerical SciPy results are untrusted proposals and never acceptance premises. The independently executed checker shares FLINT and the signed-dominance predicate; it independently reconstructs the rational pencil in Python using repeated reflection and uses fresh transforms, without importing the C producer or its driver.

## Status by part

Overall status: **PROVED** (computer-assisted development; actual independent exact checker/rerun complete; required Claude audit remains pending). The independent finite-execution obligation is complete specifically at m60. No m80 or contiguous-range result is inherited from this status.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| m60 strict intervals | PROVED | All four exact endpoint tests accepted by producer and independently reconstructed checker |

Candidate / claim disposition: retained finite verification using the existing PD-T107 mechanism. No novelty claim and no new mechanism. The implementation-only scope needs no idea-generation novelty gate. It changes evaluation language/order, not the invariant or proof step.

## Depends on

PD-T106: exact moments and rational pencil, and equivalence with the orthonormal Gram spectrum. PD-T107: signed-dominance integer congruence reduction. Elementary continuous dependence of symmetric eigenvalues, Sylvester's law of inertia, and positive definiteness of the continuous mass matrix. No floating accuracy theorem is a dependency.

## Checks

Producer code: `../code/cert_pencil.c`, `../code/cert_native.py`. Developer full-entry reference regression: `../code/cert_validate.py`; matching 940,942 rational entries at m2,3,10,11,20,30,40 (including both parity conventions). Sources and execution metadata are hashed inside `../evidence/cert-m60.json` and `../evidence/cert-exact-entry-regression.json`. Rules/input SHA `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`, frozen main `440d1079e42c3ef21c40d1cf8870f5b206410c6a`; exact modified producer content is identified by SHA-256 in receipts. Developer: Codex, assigned gpt-6.1-sol medium, resolved runtime metadata unexposed.

Executed commands, from repository root:

```sh
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/cert_native.py --m 10 20 30 40 60 --scratch /tmp/padua-cert-native --output-dir topics/padua-mz-2d-frontier-20261105/evidence
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_cert.py --producer-receipt topics/padua-mz-2d-frontier-20261105/evidence/cert-m60.json --scratch /tmp/padua-independent-cert --output topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m60.json
```

The second command was actually executed by the separate `/root/replay` worker, not by this developer. Independent source `independent_cert.py` SHA-256 `28228bf2fe412d13c9a581e907aed56385a914b3e51227126b110a9c6b4348cc`; independent receipt `independent-cert-m60.json` SHA-256 `931f2c632943af1bd5d0772d3d7218f8883d08504c7c7bb2e949d616f4dcae23` (4878 bytes), verdict PASS. Its independent Fraction/repeated-reflection reconstruction checked 837,000 off-block pairs and compared all 3,349,800 within-block H/Q entries as exact rationals with the C output. Fresh transforms use scale10¹³, rather than the producer's10¹²; the original transforms/float file are not read. All four independent exact inertia counts passed: (0,1,1829,1830). Actual independent wall time232.594s. Full provenance and limitations are in `../independent-checks-cert.md`. The developer inspected that receipt and record after the independent worker reported completion.

All four frozen PD-T107 m10..40 intervals matched and were separately replayed by that worker as well. Producer m60 wall time46.912s; peak Python-process RSS747052KiB; native-child peak memory was not separately measured. The G1 m60 two-hour wall criterion passes.

Each case's negative counts are (0,1) at minimum lower/upper endpoints, and (N−1,N) at maximum lower/upper endpoints. Every individual block passes exact symmetry and positive strict-dominance margins; zero inertia is zero throughout. Four malformed matrix controls reject and a valid mixed-sign dominant control accepts. A real m10 rerun at rounding scale1 rejects strict dominance before emitting any accepted certificate.

## Sources

Local proved PD-T106/PD-T107 only. This is not a literature-priority claim. Earlier audits and receipts are context; the new m60 independent execution is separately identified above.

## Proof or evidence

For each basis pair (a,b),(c,d), sum all four product-to-sum terms with r∈{a+c,|a−c|}, s∈{b+d,|b−d|}, retaining repeated terms. Continuous moments are h(r)h(s), h(k)=0 for odd k and 2/(1−k²) for even k. Fold A=f_m(r), B=f_(m+1)(s); the quadrature moment is h(A)h(B) when A+B≤m, and h(m−A)h(m+1−B) otherwise. Divide sums by4. PD-T106 proves these formulas. The C implementation canonicalizes every initialized h rational, then uses canonical GMP rational operations. Both matrices' upper off-parity entries are explicitly checked to vanish, with x parity when m is even and y parity when m is odd. Formula symmetry justifies copying lower entries.

For each block, let D>0 be the LCM of the canonical denominators of both H and Q. Exact divisibility is checked before constructing integer H0=DH,Q0=DQ. For endpoint t=tn/td, td>0, the code computes exact integer matrices

`BH=RᵀH0R`, `BQ=RᵀQ0R`, `B=td*BQ−tn*BH`.

By distributivity, B=Rᵀ[D td (Q−tH)]R exactly. Neither D nor D td needs to be the minimal common denominator: positive scaling preserves inertia. R comes from rounded numerical eigenvectors; no invertibility assumption or approximate orthogonality is trusted.

The checker requires exact symmetry and |B_ii|>Σ_(j≠i)|B_ij| for every row. For s∈[0,1], multiply every off-diagonal entry by s while retaining the diagonal. Strict dominance persists, so the resulting symmetric matrix is nonsingular: in a hypothetical null vector choose a maximal absolute component and apply its row inequality to obtain a strict contradiction. Therefore no eigenvalue crosses zero along this continuous path. B has exactly its diagonal sign inertia, with no zero eigenvalues.

Since B is nonsingular, R has trivial kernel and is square invertible. Sylvester's law and the positive factor D td transfer this exact inertia to Q−tH. Congruence by H^(−1/2) identifies its negative count with the number of generalized eigenvalues below t. Zero counts at both endpoints exclude equality. Negative counts0 then1 bound the minimum; countsN−1 thenN bound the maximum. This proves the finite implication from accepted exact checks to the table. Both producer and independent reconstruction/execution accepted every required m60 check, establishing the displayed finite result under the stated computational trust.

## Scope

Only m60, n59. Positivity and upper bound2 in this case follow from the intervals. This does not prove universal positivity, an all-m upper bound, a fixed-ratio theorem, an asymptotic law, or a uniform signed-operator bound. Contiguous-range batch receipts and m80 producer acceptance are separate evidence and do not silently enlarge this statement.

## Open items

- m60 independent checker/rerun is complete; m80 remains separate and pending in `cert-finite-extension-m80.md`.
- Required Claude audit remains separate from supplementary independent checking.
- m100 result pending at this checkpoint. All-integer2..60 batch incomplete at this checkpoint.
- Bulk scratch pencils/transforms are regenerable and hashed in receipts; AC cold-storage export/retrieval is pending. No scratch locator is represented as archived storage.

## History

2026-11-05, Codex certifier worker, assigned gpt-6.1-sol medium: implementation-only native pencil port, frozen full-entry validation, exact m60/m80 producer acceptance; initial combined statement CONDITIONAL pending independent replay. The existing PD-T107 statement is unchanged.

2026-11-05, after inspecting the separate replay worker's actual m60 receipt and record: split the initial statement by case. This file retains m60 with PROVED computer-assisted development status; m80 moved to separate provisional91 with CONDITIONAL status and its exact pending obligation preserved. Neither the universal nor the contiguous-range target is narrowed or relabeled.
