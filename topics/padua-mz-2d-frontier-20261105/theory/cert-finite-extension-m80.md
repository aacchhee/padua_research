# PD-T?mz2d-frontier-codex-91 — Candidate signed Padua spectrum at m80

ID kind: PD-T (provisional; orchestrator assigns final ID).
Aliases: G1 m80 native extension; finite m80 signed-dominance certificate.
Split from: initial m60/m80 statement in `cert-finite-extension.md`, provisional90, to preserve the completed m60 proof separately from this pending case.
Split into: none.

## Statement

For the fixed even-checkerboard signed Lebesgue Padua rule on Π_79, m=80 and dimension3,240, its generalized Gram eigenvalue minimum lies strictly in (0.172730,0.172731), and its maximum strictly in (1.816497,1.816498). Decimal endpoints are exact terminating rationals.

## Definitions

Exactly the frozen definitions in `topics/padua-mz-2d-20261101/definitions.md`. H is the continuous dx dy mass matrix and Q the signed quadrature mass matrix in the product-Chebyshev basis; their generalized eigenvalues equal the orthonormal Legendre Gram eigenvalues by PD-T106.

## Assumptions

Precisely m80,n79. Trust: recorded C compiler/executable, canonical GMP rational/integer arithmetic, Python control/integer conversion, FLINT exact integer products. Numerical SciPy eigenvectors/endpoints are untrusted proposals. Actual independent reconstruction and exact checking are required for PROVED computer-assisted status.

## Status by part

Overall status: **CONDITIONAL** — all four exact producer endpoint checks passed; separate independent m80 checker/rerun is running, not yet completed. The m60 independent completion does not establish this case.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Two strict m80 extreme-eigenvalue intervals | CONDITIONAL | Exact producer acceptance complete; independent reconstruction/rerun pending |

Candidate / claim disposition: retained implementation-only extension of existing PD-T107; no new mechanism or novelty claim.

## Depends on

PD-T106 rational pencil and change of basis; PD-T107 integer signed-dominance inertia reduction. The m60 numerical values are not a mathematical dependency.

## Checks

Producer sources `../code/cert_pencil.c`, `../code/cert_native.py`; exact source hashes, binary hash, definitions hash, versions, positive denominator scales, transform hashes, margins and counts in `../evidence/cert-m80.json`. Input/rules SHA `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`; frozen base `440d1079e42c3ef21c40d1cf8870f5b206410c6a`. Developer Codex, assigned gpt-6.1-sol medium, resolved runtime metadata unexposed.

Executed producer command:

```sh
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/cert_native.py --m 80 100 --scratch /tmp/padua-cert-native-large --output-dir topics/padua-mz-2d-frontier-20261105/evidence
```

m80 completed in302.437s wall, peak Python-process RSS2663896KiB; native-child peak RSS unmeasured. m100 remains pending in the same invocation and is not claimed here. Negative endpoint counts are0,1,3239,3240, with no zeros and positive strict margins in every block. No floating tolerance enters acceptance.

## Sources

Local PD-T106/PD-T107. No literature-priority claim or imported finite proof.

## Proof or evidence

The exact reduction is the unchanged PD-T107 reduction, also written explicitly in the Proof section of `cert-finite-extension.md`. Briefly, the canonically constructed rational matrices become H0=DH,Q0=DQ with D>0. Native FLINT computes BH=RᵀH0R,BQ=RᵀQ0R. For rational t=tn/td, td>0, B=td BQ−tn BH equals Rᵀ[D td(Q−tH)]R exactly. Exact symmetry and strict signed diagonal dominance prove B nonsingular with diagonal-sign inertia; this proves R invertible and transfers inertia to Q−tH. Positive definiteness of continuous H turns negative inertia into the generalized eigenvalue count below t. Counts0,1 at minimum endpoints and3239,3240 at maximum endpoints imply the stated strict brackets. The producer accepted all required checks; completion of the independently implemented execution is the remaining finite verification obligation.

## Scope

Only the displayed m80 case. No contiguous integer interval, all-m bound, endpoint law, fixed-ratio result, or uniform signed-operator theorem follows.

## Open items

- Separate worker `/root/replay` has started `code/independent_cert.py` with `--producer-receipt evidence/cert-m80.json`; await actual PASS/FAIL receipt and document exact scope before changing status.
- Required Claude audit remains separate.
- Native and fresh independent transforms/pencils remain regenerable scratch under `/tmp`; AC cold-storage delivery/retrieval pending.

## History

2026-11-05, Codex certifier worker, assigned gpt-6.1-sol medium: preserved the exact m80 candidate as a separate CONDITIONAL record after actual independent m60 completion allowed the m60 case to become PROVED. This split records the original two-case statement without silently discarding its pending part.
