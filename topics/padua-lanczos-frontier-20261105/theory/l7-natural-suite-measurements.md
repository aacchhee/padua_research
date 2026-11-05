# PD-T?lanczos-frontier-codex-L7-01 — reference-conditioned natural fitting measurements

ID kind: PD-T (provisional; no final ID allocated).
Aliases: `PD-T?lanczos-frontier-L7` (historical ID); `PD-T?lanczos-frontier-codex-L7` (response working alias); L7 natural suite; fixed-target build/fit/recurrence study.
Split from: none.
Split into: none.

## Statement

For the exact frozen four-domain, two-seed,1600-training-node suite at nested degrees8/16/24, all10 prescribed binary64 methods and four fixed targets were executed. The casewise numerical reference accepts16 of24 degree cases and rejects8. On accepted references,20 of1280 method/target/test-distribution cells meet the preregistered resolved-loss rule. All20 occur on triangle24; no accepted-reference resolved loss is detected in the other accepted cases. Six matching method-pair directions satisfy the>2 error-ratio criterion in both seeds, all for triangle24/tanh/boundary. These are finite end-to-end measurements under the Haswell OpenBLAS dispatch identified below and the stated implementation/reference screens. The six directions use a post-registration same-group restriction; six additional cross-group directions meet the same criterion.

## Definitions

[Preregistration](../l7-preregistration.md) fixes the complete domains, seeds, target formulas, independent interior/boundary-band samples, methods, numerical reference, metrics and comparison rules. The four targets are rational, tanh, absolute and entire control; no Franke target is included. A resolved loss requires accepted reference, method relative-l2 error>2 reference error, and prediction difference divided by truth norm>max(1e-10,100*eps*kappa_reference). A paired-method advantage requires an error ratio>2 in the same direction for both seeds at the identical domain/degree/target/distribution. Comparisons here pair methods within the same full/window reorthogonalization group; actual upstream methods belong to the full group.

The1280 denominator is16 accepted degree cases*10methods*4targets*2distributions. The degree24 construction supplies nested prefixes; no lower-degree reconstruction replaces it. Stored Q is fit by SVD least squares. Predictions evaluate the recorded recurrence in binary64; replay differences are reported, not silently removed. Training residual refers to stored Q times fitted coefficients.

## Assumptions

Pinned numerical producer and actual polyrat source, binary64 arithmetic, NumPy2.3.5/SciPy1.17.0, Python3.12.14, OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1, extended longdouble nmant63. Reference acceptance requires full numerical rank at the saved SVD cutoff, kappa<1e8, longdouble Gram max<1e-12, double/LD span discrepancy<1e-7, and wider LD significand. These are numerical screening rules, not rigorous enclosures.

## Status by part

Overall status: MEASURED.

| Part | Status | Evidence / remaining gap |
|---|---|---|
| Frozen developer suite and implementation equality | MEASURED | All8 runs exit0; all64 own/L2 Q and parent validations exact. |
| Reference-conditioned loss/paired-method counts | MEASURED | Compact summary and complete raw aggregate; independent supplementary check complete; Claude audit-01 findings addressed below, focused re-audit pending. |

No candidate rejection or theorem claim is made.

## Depends on

G0/G4 additive resolutions authorize this suite; [G4 disposition](../g4-disposition-04.md) preserves historical replay failures. Numerical dependencies and empirical thresholds are exactly the saved preregistration. This result does not depend on inherited mathematical capacity/selection theorems, and it does not establish their IEEE activation.

## Checks

Rules/input head `9825d184517db81d0aad8542fbd6639f2164b803`; developer Codex gpt-6.1-sol medium. [Methods](../l7-suite-methods.md) records prospective staging and executed commands. [Pilot receipt](../evidence/l7-suite-pilot.json), [remaining receipt](../evidence/l7-suite-remaining.json), and [summary](../evidence/l7-suite-summary.json) pin exact source/input/environment/command/artifact identities. Producer SHA256 `ba2beac1ea8041dd035d8072a1533592deb8c209bc54e801af54906d7f533fb7` is identical throughout. Worker sum116.0615s; caps600s/case, sequential. Compilation is only a syntax check; actual degree24 validation is performed in every case. Self-checks do not constitute independent approval.

## Sources

Actual external polyrat pinned commit6903d7af9995c9d88e661fb229626696e00fdfba is executed through the namespace loader; source-file hashes are in each metadata artifact. [External-code coverage](../external-code.md) retains access limitations. No unread primary fulltext is cited as an executed literature task. BNT/Octave and identifiable Zhu–Nakatsukasa author-code execution are not completed by this suite. No novelty or priority claim is made.

## Evidence

| Domain | Accepted degrees, both seeds | Rejected degrees, both seeds |
|---|---|---|
| disk | 8,16 | 24 |
| L-shape | 8,16 | 24 |
| triangle | 8,16,24 | none |
| annular sector | 8 | 16,24 |

All20 resolved-loss cells are triangle24: seed2026110501 has3 (tanh upstream_xy uniform/boundary and dev_window boundary); seed2026110502 has17 (rational upstream_yx/dev_full/dev_window both distributions; tanh upstream_xy boundary, upstream_yx/dev_full both, dev_window boundary; absolute upstream_yx/dev_full both and dev_window boundary). Entire control has no detected loss on accepted references.

Paired-seed advantages, restricted to triangle24/tanh/boundary, are:

| Lower-error method | Comparator | Comparator/lower ratios, seed1; seed2 |
|---|---|---|
| mirror_full | upstream_xy | 4.7867;2.2426 |
| alt_full | upstream_xy | 4.8463;2.2454 |
| adapt_full | upstream_xy | 4.8462;2.2426 |
| mirror_window | dev_window | 2.3970;4.7955 |
| alt_window | dev_window | 2.3899;4.8016 |
| adapt_window | dev_window | 2.3899;4.7959 |

Each method pair has64 matching accepted-reference target/distribution cells across both seeds; its remaining63 are mixed/below threshold. All other same-group pairs have no matching>2 direction across both seeds. This is the stated empirical comparison, with no statistical inference beyond the two saved seeds.

The maximum raw training replay entry discrepancy is5.9126 (triangle seed1 n24 upstream_yx), despite tiny Gram defects for full CGS2. The same case has accepted reference kappa367.0 and span gaps close to1 for upstream/dev; mirror, alternating and adaptive values differ substantially. Exact own/L2 construction agreement does not imply recurrence replay accuracy. Observed natural-fit differences combine construction, fitting and recurrence evaluation arithmetic; these measurements alone do not identify a cause. The upstream_yx/dev_full Q matrices agree exactly, while their independent evaluator arithmetic can produce different predictions.

## Scope

This finite empirical record covers the fixed samples, degrees, targets, machine precision, ten implementations and accepted reference screens. It gives no causal, universal, platform-independent or all-degree conclusion. Rejected-reference cases retain raw diagnostics without trusted span/fitting attribution. Absence of detected loss applies only to the saved criterion. Basis coefficient norms remain basis-dependent diagnostics.

## Open items

Distinct supplementary checking and Claude audit-01 are complete; the platform/grouping/evidence response below requires focused Claude re-audit. No final ID or merge readiness is implied. Windows archival delivery remains pending; local `/tmp` retention is not guaranteed, and source/code manifests permit regeneration. General behavior outside the suite and missing external literature/code tasks remain open.

## History

2026-11-05, Codex gpt-6.1-sol medium, input9825d184517db81d0aad8542fbd6639f2164b803: prospectively staged and actually executed the unchanged suite after G4 resolution; recorded developer measurements pending distinct review. Earlier suite-NOT-RUN checkpoints describe their original dates and remain unchanged.

### Distinct supplementary check addendum

Separate reviewer execution PASS: all8 cases independently regenerate coordinates and reference matrices, validate screens, recompute recurrence replay/paths and QR/Gram/SVD fits, and reproduce every loss flag and the6 paired directions (117.425s). A separate full triangle seed1 producer rerun matches all43 saved raw arrays exactly. [Independent receipt](../evidence/l7-independent.json) pins checker/source/outputs; independent report records scope. The stated finite measurements and interpretation pass this supplementary check. This closes the supplementary-pending item above while preserving the generated developer receipt's original timestamped label; later required Claude scientific/protocol audit and Windows archival delivery remain pending. No causal interpretation or theorem is added.

### Audit-01 platform, comparison and evidence addendum — 2026-11-05

The original receipts omitted CPU identity and BLAS dispatch. The audit identifies **OpenBLAS Haswell** as the dispatch reproducing the committed 20 loss cells and 6 same-group directions, including cell identity and displayed ratios; G0 contemporaneously reported OpenBLAS 0.3.30 Haswell. The historical CPU model/ISA and glibc were not recorded and cannot be reconstructed from this agreement. No historical CPU is inferred. The separate response-session environment observation in [response-numerical-environment.json](../evidence/response-numerical-environment.json) records AMD EPYC 7763, exposed CPU flags, glibc 2.41 and actual Haswell OpenBLAS 0.3.30 dispatch for both NumPy/SciPy with one thread; it is not a suite rerun or a historical receipt.

On the auditor's AVX-512 host, default dispatch gave **18 loss cells and 9 same-group directions**, with different cells and pairs; pinned Haswell gave exactly **20 and 6**, and disabling NumPy AVX-512 in addition did not change the Haswell result. The MEASURED label remains. Specific cells, ratios and pair directions depend on the platform. Robust features across those runs are: the accepted/rejected references; losses confined to triangle24 with none on the entire control; paired directions confined to triangle24/tanh/boundary; exact own/L2 construction agreement; and unchanged span-gap ranking. Several cells lie within 1–6% of the threshold, so the count is not a platform-independent statistic. No response suite rerun was performed.

The full/window same-group restriction was a **post-registration analysis choice**, not part of the preregistered pair rule. Applying that unchanged >2 both-seeds criterion to all 24 cross-group method pairs (64 matching accepted cells per pair) gives six additional directions, all triangle24/tanh/boundary: upstream_xy is beaten by mirror_window, alt_window and adapt_window; dev_window is beaten by mirror_full, alt_full and adapt_full. There are thus 12 qualifying directions among all 45 method pairs in the recorded Haswell data. [Cross-group evidence](../evidence/l7-cross-group.json) retains the ratios and worker pins; no extra dataset or threshold was selected.

The [full 20-row loss list](../evidence/l7-full-loss-list.json) is committed with exact original JSON float displays, full-aggregate pin and aggregator source/command. Aggregator SHA256 is `e6fe858208a36206a7bcf9a4e81412fd3b8920cd45dfde5835a26a3c8c363a01`. [Evidence response](../evidence-response-01.md) records packaging/check commands and provenance. The audit verified the prospective methods-prefix receipt pin even though methods and results share a commit (L7G1-5); no stronger Git chronology is asserted. Triangle replay defects already reach approximately 2.8e-6 and 2.3e-6 at degree16, respectively (L7G1-6), so recurrence sensitivity is not confined to degree24.

History: this dated response scopes the unchanged finite observation and reports the post-registration grouping; it does not revise the frozen preregistration, source, thresholds or original receipts. The agent-qualified provisional ID retains its former spelling as an alias.
