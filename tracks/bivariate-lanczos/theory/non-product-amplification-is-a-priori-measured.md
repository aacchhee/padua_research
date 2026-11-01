# PD-T?bivariate-lanczos-claude-109 — The non-product amplification is a property of the exact recurrence for a given selection rule, and its size depends on the selection rule (measured)

Final ID: **PD-T037** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: P* = P; a priori propagator growth; two-relation control removes the instability; triangle orientation scan.
Split from: none.
Split into: none.

## Statement

[MEASURED] With M = 1681 (seed 11 sets), uniform weights, u = 2^-52:

(a) **Exact coefficients give the same amplification.** The idealised node propagator built from exact window coefficients (long double, full reorthogonalisation) [note 2026-11-01T08:41:34+01:00, Codex audit-01 L1-later: these reference coefficients P* are a high-precision floating-point computation, not exact arithmetic. An exact rational certificate of the amplification for the dev rule is PD-T?…-113, on the integer triangle grid T_24, a different measure] has the same response to iid forcing of size u/√M as the propagator of the double run's computed coefficients, to the printed digit, on the square, the square rotated by π/4, the disk (n ≤ 20) and the triangle (n ≤ 16) — e.g. rotated square P* = P = 9e-6 at n = 20 (measured loss 2e-6), disk P* = P = 2e-10 (loss 2e-10), square P* = P = 1e-14. The computed coefficients deviate from the exact ones by up to 2e-7 (rotated square), 1e-3 (triangle), without changing the response.
(b) **Two relations remove it on the tested rotated squares and the disk** (narrowed 2026-10-31, recon-01; see the corrections after (c)). A block recurrence with the same truncation (degree block n from X Q_{n−1} and Y Q_{n−1}, one CGS pass against blocks n−2 and n−1, orthonormal completion by SVD) keeps the loss at 7e-15–6e-14 up to n = 24 on the square rotated by 0.3 and by π/4 and on the disk, where the BJ window recurrence reaches 5e-6, 4e-3 and 1e-8; on the triangle it reaches 3e-10 at n = 24 against 1 for BJ.
(c) **Orientation dependence.** For the triangle, the BJ loss at n = 16 varies with the rotation angle θ of the node set between 1.9e-9 (θ = π/4, a symmetry axis aligned with a coordinate axis) and 6.8e-3 (θ = 0); no angle among 12 tested gives loss at the product level (≤ 1e-14).

Corrections (2026-10-31T23:05Z, reconstruction 01, developer rerun `logs/c01_recon_runs.log`):
- (a) holds for the dev (input-code BJ) selection, which is the one tested. The exact-coefficient propagator itself depends on the selection rule (recon-01 `prop_selection.log`).
- (b) is narrowed. Removed: on the squares rotated by 0.3 and π/4, the disk, the annulus and the tensor grid rotated by 0.3 (recon-01). Not removed:
  - triangle: reduced with one pass (developer 2.6e-10, recon-01 1.0e-10 / 8.5e-12 at n = 24, still growing); two passes 1.4e-11 (developer) / 4.3e-12 (recon-01);
  - Gaussian cloud: 6.3e-8 at n = 24, Ritz-type;
  - tensor 41²: two relations are worse than BJ (8.0e-13 vs 1.8e-14 at n = 24);
  - clustered checkerboard: catastrophic (PD-N?…-103 (c)).

Consequence (corrected 2026-10-31T23:05Z): for a fixed selection rule, the growth is an a priori property of (measure, coordinates, graded order, selection rule), computable from the exact recurrence coefficients. Its size depends strongly on the selection rule: one-relation rules differ by 10³–10⁸ at n = 24 (PD-N?…-105 (a)). Single-pass Gram–Schmidt and the truncation both enter: removing the truncation removes the growth on rotation π/4 and the disk, but not on the triangle or rotation 0.3 (PD-N?…-105 (b)).

Original Consequence sentence: **REJECTED: refuted** (PD-N?bivariate-lanczos-claude-105; reconstruction 01, finding B1). Original wording, preserved: "Consequence: the growth is an a priori property of (measure, ordering, coordinates) — computable from the exact recurrence coefficients — and is caused by the triangular one-relation-per-column selection of the Jacobi pencil (PD-T?…-108), not by the truncation of the window."

## Definitions

P*(n), P(n): max over columns of degree ≤ n of the node-vector norm of the propagator response (PD-T?…-107 (c)). Two-relation recurrence: `code/L1/l1_both_relations.py::both`.

## Assumptions

As stated; IEEE double, x87 long double.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) P* = P | MEASURED | `logs/r03_exact_propagator.log` |
| (b) two-relation control | MEASURED | `logs/r03_both_relations.log` |
| (c) triangle orientation scan | MEASURED | `logs/r03_exact_propagator.log` (scan section) |
| "a priori" consequence (corrected, for a fixed selection rule) | inference from (a) within its scope | an a priori bound remains OPEN |
| original "caused by the one-relation selection, not by the truncation" | REJECTED: refuted | PD-N?…-105 |

## Depends on

PD-T?…-104, -105, -107, -108.

## Checks

`python3 -I l1_exact_propagator.py`, `python3 -I l1_both_relations.py` (from `tracks/bivariate-lanczos/code/L1/`). Independent rerun: none yet.

## Sources

Corrected attribution (2026-10-31, recon-01 P3; PC-6, PC-7, PC-9):
- The two-relation block recurrence is the block Stieltjes procedure of Liu–Narayan (SIAM J. Sci. Comput. 45(3) 2023, A1125–A1147), its algorithmic predecessor, read through the independent prior-art check and a summary.
- The stacked consistent system and its left inverses are classical: Xu's survey §2.2 and Dunkl–Xu Thm 3.2.5 (as cited by BPS).
- That the choice of variable per polynomial affects rounding is in Barrio–Peña–Sauer 2010, Remark 9 and §5 (fulltext read).

Original text: Two-relation block recurrences appear in the literature as reported (xu-siam-1994 recalls the block three-term relations; liu-narayan-2023 multivariate Stieltjes; fasondini-olver-xu-2023 block Lanczos on multiplication matrices) — none of these records reports a stability comparison; not used as evidence.

## Proof or evidence

Measured; see logs.

## Scope

M = 1681, n ≤ 24, five shapes. The two-relation recurrence is a control experiment, not a proposed algorithm with an analysis (its basis inside each degree block is an SVD basis, not the graded-lex one; cost per degree O(M n²), the same order as the window recurrence overall).

## Open items

(i) A priori bound or growth rate of ‖L*(z)⁻¹‖ for non-product measures (e.g. potential-theoretic); (ii) the triangle's residual growth under the two-relation recurrence (Ritz-type or amplification?); (iii) larger M (Runs needed); (iv) hand-off of the two-relation variant to L2/L5 as a candidate remedy.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R03).
- 2026-10-31T23:05Z (response to reconstruction 01):
  - B1: the Consequence sentence is REJECTED: refuted (PD-N?…-105). The title is narrowed; original title: "The non-product amplification is a property of the exact recurrence and of its one-relation-per-column selection (measured)".
  - Major finding on (b): the scope is narrowed to the sets where the growth was removed; the triangle, Gaussian, tensor and clustered-checkerboard exceptions are added; original heading "Two relations remove it.".
  - P3: Liu–Narayan, Xu/Dunkl–Xu and BPS are cited.
  - Also: the support-based reading is withdrawn (PD-N?…-106).
- 2026-11-01T08:41:34+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later table note on T109): (a) now says that the "exact window coefficients" of the P* reference are a long-double computation with full reorthogonalisation, not exact arithmetic. The measured content and the status (MEASURED) are unchanged.
