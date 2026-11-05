# PD-T?mz2d-frontier-codex-91 — Certified signed Padua spectrum at m80

ID kind: PD-T (provisional; orchestrator assigns final ID).
Aliases: G1 m80 native extension; finite m80 signed-dominance certificate.
Split from: initial m60/m80 statement in `cert-finite-extension.md`, provisional90, to preserve the completed m60 proof separately from the m80 case that was pending at the time of the split.
Split into: none.

## Statement

For the fixed even-checkerboard signed Lebesgue Padua rule on Π_79, m=80 and dimension3,240, its generalized Gram eigenvalue minimum lies strictly in (0.172730,0.172731), and its maximum strictly in (1.816497,1.816498). Decimal endpoints are exact terminating rationals.

## Definitions

Exactly the frozen definitions in `topics/padua-mz-2d-20261101/definitions.md`. H is the continuous dx dy mass matrix and Q the signed quadrature mass matrix in the product-Chebyshev basis; their generalized eigenvalues equal the orthonormal Legendre Gram eigenvalues by PD-T106.

## Assumptions

Precisely m80,n79. Trust: recorded C compiler/executable, canonical GMP rational/integer arithmetic, Python control/integer conversion, FLINT exact integer products. Numerical SciPy eigenvectors/endpoints are untrusted proposals. Actual independent reconstruction and exact checking are required for PROVED computer-assisted status.

## Status by part

Overall status: **PROVED** (computer-assisted development; actual independent exact checker/rerun complete; Claude audit-01 accepted). This case has its own completed independent reconstruction and acceptance, separate from m60.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Two strict m80 extreme-eigenvalue intervals | PROVED | Exact producer and independently reconstructed checker accepted all endpoints |

Candidate / claim disposition: retained implementation-only extension of existing PD-T107; no new mechanism or novelty claim.

## Depends on

PD-T106 rational pencil and change of basis; PD-T107 integer signed-dominance inertia reduction. The m60 numerical values are not a mathematical dependency.

[Claude audit-01](../audit-01.md) accepted the mathematics at its stated scope; [response-01](../response-01.md) addresses the editorial findings. Supplementary reconstruction is recorded in [independent-checks-math.md](../independent-checks-math.md).

## Checks

Producer sources `../code/cert_pencil.c`, `../code/cert_native.py`; exact source hashes, binary hash, definitions hash, versions, positive denominator scales, transform hashes, margins and counts in `../evidence/cert-m80.json`. Input/rules SHA `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`; frozen base `440d1079e42c3ef21c40d1cf8870f5b206410c6a`. Developer Codex, assigned gpt-6.1-sol medium, resolved runtime metadata unexposed.

Executed producer command:

```sh
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/cert_native.py --m 80 100 --scratch /tmp/padua-cert-native-large --output-dir topics/padua-mz-2d-frontier-20261105/evidence
```

m80 completed in302.437s recorded per-target wall, peak Python-process RSS2663896KiB; native-child peak RSS unmeasured. Timing excludes common startup/compilation and final hashing/receipt serialization. m100 was later stopped by the orchestrator's scope decision without completing an accepted endpoint check; it is not claimed here. Negative endpoint counts are0,1,3239,3240, with no zeros and positive strict margins in every block. No floating tolerance enters acceptance.

Separate worker `/root/replay` actually executed the following command; this developer inspected its source, report and actual receipt after completion:

```sh
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_cert.py --producer-receipt topics/padua-mz-2d-frontier-20261105/evidence/cert-m80.json --scratch /tmp/padua-independent-cert --output topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m80.json
```

The independent checker reconstructs rational moments with Python Fraction and repeated reflection, compares all10,499,200 within-block H/Q entries exactly and checks2,624,000 off-block pairs. Fresh scale10¹³ transforms differ from the producer's10¹²; producer transforms and floating matrices are not read. Every independently computed exact margin was positive; endpoint negative counts were0,1,3239,3240. Actual wall569.136s; sampled Python RSS about2.1GiB, not a measured peak. Source `independent_cert.py` SHA-256 `28228bf2fe412d13c9a581e907aed56385a914b3e51227126b110a9c6b4348cc`; receipt `independent-cert-m80.json` SHA-256 `7b57e74e0e3e919a79262067427e35afa97a637d5d39e0cc17620c93e99cd5fe` (5300 bytes), PASS. Shared FLINT arithmetic and the same mathematical signed-dominance predicate remain explicit trust limitations. Full record: `../independent-checks-cert.md`.

## Sources

Local PD-T106/PD-T107. No literature-priority claim or imported finite proof.

## Proof or evidence

The exact reduction is the unchanged PD-T107 reduction, also written explicitly in the Proof section of `cert-finite-extension.md`. Briefly, the canonically constructed rational matrices become H0=DH,Q0=DQ with D>0. Native FLINT computes BH=RᵀH0R,BQ=RᵀQ0R. For rational t=tn/td, td>0, B=td BQ−tn BH equals Rᵀ[D td(Q−tH)]R exactly. Exact symmetry and strict signed diagonal dominance prove B nonsingular with diagonal-sign inertia; this proves R invertible and transfers inertia to Q−tH. Positive definiteness of continuous H turns negative inertia into the generalized eigenvalue count below t. Counts0,1 at minimum endpoints and3239,3240 at maximum endpoints imply the stated strict brackets. Both producer and independently implemented exact execution accepted every required m80 check. The displayed finite result follows under the stated computational trust.

## Scope

Only the displayed m80 case. No contiguous integer interval, all-m bound, endpoint law, fixed-ratio result, or uniform signed-operator theorem follows.

## Open items

- The separate m80 checker/rerun is complete; independently checked degrees are exactly10,20,30,40,60,80, not every integer below80.
- Claude audit-01 accepted; it is distinct from the completed supplementary checks.
- Native and fresh independent transforms/pencils remain regenerable scratch under `/tmp`; AC cold-storage delivery/retrieval pending.

## History

2026-11-05, Codex certifier worker, assigned gpt-6.1-sol medium: preserved the exact m80 candidate as a separate CONDITIONAL record after actual independent m60 completion allowed the m60 case to become PROVED. This split records the original two-case statement without silently discarding its pending part.

2026-11-05, after actual independent m80 PASS and inspection of source/receipt/report: upgraded this separate case to PROVED computer-assisted development. Required Claude audit remains pending. No additional integer size is inherited from the status change.

2026-11-05, documentation response to audit-01: the pending wording in the earlier dated history above records the development state at that time. Claude audit-01 subsequently accepted the mathematics; response-01 records the permitted editorial changes. No earlier execution or statement is relabeled.
