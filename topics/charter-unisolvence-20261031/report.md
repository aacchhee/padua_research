# Campaign report and ranked development briefs

Rules/base `d36722823441dc40c6e19d69a174459348dd309c`; branch `codex/charter-unisolvence-20261031`. Claude audit-01 accepted the mathematical scope and all 13 epistemic statuses/dispositions at eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64. Response-01 resolves the administrative findings; Stage PR, with only AC authorized to merge.

## Main outcome and exact U1 scope

The original U1 iff over arbitrary fields is **REJECTED: refuted** by characteristic2 (PD-N001). Its necessary condition fails: alternation signs collapse and the first barycentric moment is zero, although checkerboards can be unisolvent. An elementary F4,m1 example and an exact F8,m2 example are retained. This refutes necessity, not global sufficiency: the hypothesis is impossible in characteristic2, and sufficiency holds in other characteristics.

PD-T001 proves the original iff for every m≥0 in characteristic≠2, for both parity choices, all label orders, and no cross-axis distinctness assumption. The finite-support cutoff is exactly minors1,…,L−1 for an axis of lengthL.

PD-T002 supplies the replacement over **every field**. For a lengthL axis H=(h_i), define B_H(f)=Σ_(i even) f(h_i)/ω_H′(h_i). Require its leading Hankel minors of orders1,…,floor((L−2)/2) nonzero, independently on X and Y; empty ranges impose no condition. This is equivalent to checkerboard unisolvence for either parity. A determinant-square identity proves the criterion and parity independence; all denominators are within-axis differences. Characteristic0 indeterminates are explicitly proof scaffolding, and a localized integer-ring argument transfers the identity to every characteristic.

## Ranking and development briefs

| Rank | Survivor and exact status | Development brief / remaining value | Closest predecessor / limit |
|---|---|---|---|
| 1 | PD-T001/002 PROVED; PD-N001 PROVED negative | Audit signs, complementary minors, finite cutoff, localized-Z transfer and both degree parities. Package as a self-contained field-uniform reformulation with the explicit correction to source U1. | De Marchi–Usevich2014 and Camargo–De Marchi2015 already give axis determinant factorization; Harris–Simanek gives ordered-real kernels. No new-mechanism or exhaustive novelty claim. |
| 2 | PD-T006 discriminant and PD-T007 quadratic description PROVED | A short note could pair exact Dickson-coordinate determinant, rationality dictionary and endpoint-corrected character sets. Verify publication-level overlap before proposing novelty. | Classical weighted Gram/Padua theory and torus traces; sourced claims independently reconstructed here, originality UNVERIFIED. |
| 3 | PD-T004/005/008 PROVED; PD-T012 PROVED bounds; PD-T009/010 MEASURED | Reusable exact benchmark and coding examples. Five core proofs have independent Astra reconstruction; source and independent checks include prime powers3,9. Code dimensions/dual/distance lower bound proved; attained small distances remain measured. | Affine-variety/Cartesian/downset codes and standard projective arcs. Universal bounds d≤7 and d≤4 match measured q7 attainments, without a Ball dependency. |
| 4 | PD-T003 PROVED direct U3 consequence | Explicit monic-OP Lagrange formula without square roots in characteristic≠2. Discrete-product cubature through degree2m needs no quasi-definiteness. | Classical kernel argument; distinguish the discrete alternation product functional from continuous Chebyshev cubature. No claim this normalization works in characteristic2. |

## Retained non-survivors, deferred openings and corrections

- Original arbitrary-field alternation iff: refuted necessity, retained with PD-N001 and exact original wording. No family-wide rejection.
- Naive expansion of a global multivariate rational symbolic expression: bounded aborted computational route, not a mathematical PD-N. Factored axis assembly replaces it; exact coverage is in directions/U1/evidence.md.
- Axis separation as a new mechanism: equivalent to existing determinant-factor structure; no PD-N for equivalence. The all-characteristic formulation and cutoff have a local proof, with conservative attribution.
- HS Conjecture3 over decreasing real nodes: supplied notes called it open, but Cao–Ghimire–Wang2022 proves it. U2 must not rediscover that claim. General arbitrary-field patterns remain deferred without a frozen new proof opening.
- U0 ideal/H-basis/recurrence transfer and unrestricted-length transform complexity: OPEN in PD-T011. The source implementation has quadratic prime-length FFT leaves; successful finite timings do not establish the stated asymptotic bound. Bounded quick registration stops here as requested.
- U3 exact labelling counts, characteristic2 kernel alternatives and non-checkerboard patterns remain frontier questions, not accepted candidates. The existing matrix inverse alone is not a separating new mechanism.
- Every contextual proposal, failed source route and corrected ranking from the five input documents is retained in state/IDEAS.md and the original baseline. Excluded Lanczos, MZ, 3D Padua and external moment-complexity work was not developed.

## Evidence, verification and audit limits

All17 input checksums passed; ZIP SHA256 is in LOG.md. The unchanged source suite was run before relying on it, then per-child exits were captured because run_all.py itself hides failures. Independent Astra reruns actually executed all six children, the producer exact checker, and separately implemented finite-field checks. U1 has an independently written checker, separate producer reruns and independently reconstructed proofs; finite aggregate observations remain MEASURED, not the reason the general theorem is PROVED.

The source HS sample description is corrected from reported12settings/14400 tests to actual14settings×600axis labellings×2parities=16800 parity checks. Floating source determinant agreement measures log absolute determinants, not relative determinant error. The full m3 factor contains A(X)B(Y); the source’s one-variable Y slices could not establish X-independence. Source n1 sign types collapse; q3 and q9 extend its originally prime-only character check.

No third-party PDFs or fulltext extracts are committed. The41 literature statements retain reading coverage and UNVERIFIED/pending-reference gaps. Missing/paywalled text does not stop this independent proof development. No exhaustive absence or priority assertion is made.

Cold outputs are staged with hashes and manifests, and a handoff bundle is provided for AC's chosen Windows directory. Cloud-local staging is not a receipt of Windows delivery. See COLD_STORAGE.md.

Claude audit-01 reviewed the exact handoff commit and accepted its mathematics/statuses. Response-01 records the non-material follow-up, reconciled batch order and AC’s Windows-verification waiver. Only AC may merge.

Stage PR. Next: `Codex (gpt-6.1-sol medium): Continue codex/charter-unisolvence-20261031 — check PR #2 readiness before AC’s merge.`
