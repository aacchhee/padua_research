# L1 — Response to reconstruction 01 (reviews/L1-reconstruction-01.md)

Developer: Claude Opus 5.5, xhigh. Written 2026-10-31T23:13Z (real times; History and Correction stamps written in this response were first entered as guessed future minutes, 23:12–23:20Z, and were replaced by the real minutes at 23:14Z). I read the review in full and did not edit it. Checks were run with my own code and seeds, against criteria written beforehand in candidates.md, section C01 (23:02:34Z; C01-6 at 23:09:22Z):
- `logs/c01_rule_sensitivity.log`
- `logs/c01_recon_runs.log`
- `logs/c01_u53_rerun.log`

Scripts: `code/L1/l1_c01_recon_checks.py`, `l1_c01_u53_rerun.py`. Every finding below is answered as **fix**, **rejection with evidence**, or **unresolved**. Corrected files carry dated History or Correction lines naming the finding, and the original wording is kept wherever a claim is narrowed.

## Blocking findings

**B1 — the PD-T?…-109 Consequence ("caused by the one-relation-per-column selection, not by the truncation"): fix; the claim is REJECTED: refuted.**
- Confirmed (C01-2, C01-3):
  - At the same block window and one CGS pass, the parent rules give at n = 24:
    - rotation 0.3: dev 5.8e-6, mirror 2.1e-8, alt 1.1e-9, adapt 2.9e-12;
    - rotation π/4: dev 4.2e-3, mirror 3.4e-1, alt 1.5e-8, adapt 9.4e-7;
    - triangle at n = 20: dev 1.0, adapt 1.6e-9.
  - Dev rule without truncation, at n = 24: rotation π/4 1.9e-14, disk 6.9e-15. Without truncation the triangle is still 1.0 at n = 20, and rotation 0.3 reaches 1.6e-6 at n = 24.
- New scoped record: PD-N?…-105 (MEASURED).
- Dispositions:
  - 109 Consequence: REJECTED: refuted. The title is narrowed and the corrected Consequence reads "a priori for a fixed selection rule; magnitude selection-dependent; truncation and single-pass GS both enter".
  - IDEA?…-111 as titled: REJECTED: refuted; its novelty-gate line is added.
  - R03 F8 and §3 B inference: withdrawn.
  - R03 §4, STATUS R03, SUMMARY item 3: corrected.
- Dependence check:
  - 109 (a) (P* = P) holds for the dev rule.
  - 113 (certificate) is restated as a dev-rule statement; recon-01's `prop_selection.log` shows the triangle propagator ≈ 10^7.5 smaller under adapt.
  - The rotation sweep and H_lin (R04, PD-T?…-112 (e), PD-N?…-103 (a)) are dev-rule measurements.
  - The coefficient-channel results 110, 111, 114, 115 and PD-N?…-104 do not depend on B1. They are exact algebra or concern product-type measures; 114 covers the dev and mirror rules.
  - The R04 framing "product-type vs non-product" survives as a statement about measures with product-type coefficients versus the listed non-product sets under the dev rule. It is not a statement about one-relation recurrences in general.

**B2 — "K1 fires" and the tensor single-section falsifier: fix; withdrawn.**
- Confirmed (C01-1, C01-1′). The pre-registered rule fixed u := 2^-52, while the plan's [FP] u is the unit roundoff 2^-53. At 2^-53, K1 does not fire:
  - Z predicts on random1681_s0 hl (neither single section predicts) and on random1681_s7 hl;
  - single sections predict where Z only tracks on three bj runs.
- Excluding the tensor chain-completion degree n = 40 symmetrically to Padua N = M removes the only single-section 'over'.
- Corrected report: **K1 inconclusive (no separation); K2 fires**. L1-Q1 "neither" survives through K2 only.
- Applied to: R01 (corrections section), STATUS R01, PD-N?…-101 ((b) withdrawn as evidence; Consequences narrowed to (a)), IDEA?…-101/-102 (rejection reason narrowed to (a)), SUMMARY item 1.
- The plan's round ledger is orchestrator-owned and still says "K1 and K2 both fire"; it needs this correction.
- **Consequential finding (same convention issue, R07): fix.** The R07 noise models used u = 2^-52. Re-run at 2^-53 (C01-6):
  - IDEA?…-118 H_term: inconclusive → survives;
  - IDEA?…-119: killed → inconclusive;
  - IDEA?…-120: survives → inconclusive.
  All three are now recorded as **convention-sensitive** in R07, candidates.md, PD-T?…-115, PD-N?…-104 (title narrowed) and STATUS R07. Convention-independent: H_sign killed (10³×), φ/ρ cancellation, the scale effect, and closed-loop C/L ∈ [0.14, 1.06].
  - The R04 predictor failures and the R06 verdicts are off by orders of magnitude and so are not sensitive to the factor 2 (not rerun).

## Major findings

- **PD-T?…-107, support-based classifier: fix; the classifier is REJECTED: refuted.** Confirmed (C01-4): square with exp(8xy) weights, loss 1.9e-8 at n = 24 = 1.6·10⁵ u/ρ_Z; Gaussian cloud 2.4·10³ u/ρ_Z, where the two-relation recurrence is Ritz-type (6.3e-8). New PD-N?…-106. 107 has a corrections block, the regimes are restated as listed set types, and the R01, R02, PD-N?…-101 and SUMMARY wording is corrected. Differences from recon-01: my exp(4xy) shows a 32× excess at n = 24 (theirs was stable); exp(xy) is stable in both.
- **PD-T?…-109 (b), two-relation scope: fix.** Confirmed (C01-5): tensor 8.0e-13 vs BJ 1.8e-14; triangle one pass 2.6e-10, two passes 1.4e-11. The Gaussian-cloud result is also confirmed. The heading of 109 (b) and its scope are narrowed (original kept); PD-N?…-103 History is updated.
- **PD-T?…-105 Scope overreach: fix.** The scope now says it explains the idealised propagator, not the loss; the link is OPEN. Original wording kept.
- **PD-T?…-108 attribution (P3): fix.** Sources added: Xu / Dunkl–Xu left inverse (Dunkl–Xu not read by me), BPS 2010 (fulltext pages read), Liu–Narayan, OTV, with the separation (monic vs coupled graded basis, discrete Lanczos, loss link). PC-7 and PC-9 had recorded this in R04/R05 but not in the file.
- **P2, asymmetric N = M exclusion: fix** (see B2).
- **P3, missing predecessors: fix.**
  - Liu–Narayan is cited in 109 and IDEA?…-111.
  - BPS and Xu are cited in 108 and IDEA?…-110/-111.
  - Zaccaron is cited in IDEA?…-106 (gate verdict corrected per PC-5; Zaccaron not read by me).
- **P2, IDEA?…-110/-111 missing novelty-gate lines: fix** (added).
- **P2, IDEA?…-106 "intrinsic amplification" untested against the selection: fix.** A note is added: "intrinsic" holds per selection rule.
- **P4, scope overreach list: fix, item by item.**
  - "(measure, ordering, coordinates)" now includes the selection rule (109, IDEA?…-110).
  - "caused by selection, not truncation": see B1.
  - "product-aligned supports": PD-N?…-106.
  - "two relations remove it": narrowed.
  - "exponential": qualified as convex / increasing rate in 107, 113 and R02 (my c01 runs also show increasing decades per 4 degrees, e.g. 2.3 → 2.5 → 2.8 on rotation 0.3).

## Minor findings

- **101**, part 5 is immediate: agreed; no change. History notes the confirmation.
- **102**: fixed (Correction block after Proof 1 (HL); part 4 wording). The three items are:
  - the invalid ‖h‖ inequality (now κ‖a‖ + γ_M√wμ‖a‖);
  - the HL coefficient-sum rounding (absorbed by the κ² slack);
  - the muddled ‖r‖ monotonicity sentence.
- **103**, "all terms of Ω are local" is descriptive: fix. A note says that with the block window K contains the off-pattern asymmetry, which is the coefficient channel of 114/115.
- **105**:
  - probability normalisation: fixed;
  - A′_t definition vs part 3: fixed, read with 0 ≤ r < j;
  - (n+1)² → (n+1): recorded as recon-01's observation, not re-derived; the bound is valid either way;
  - part 3 near-vacuous: agreed;
  - 2′ needs ‖L⁻¹‖δ ≪ 1: fixed.
- **106**, the deg(l)+1 ≤ deg(k)−2 inequality is false for the exact window: fixed in place; the conclusion is unchanged.
- **401**: fixed.
  - The Checks counts were wrong; the log and script show 400 nodes, n ≤ 8.
  - The Corollary 2 class issue is noted.
  - Transfer item 3 is narrowed.
  - Real A only is noted, with the complex transfer.
  - "computational content only inside the commutant" is labelled as an assertion.
  - Recon-01's own extensions (commutant + rank r; affine continuation) are recorded as theirs, unaudited, and not adopted.
- **N102**, onset n ≈ 8–10 for ORTH: noted in History; original kept.
- **P2**, the "tracks ≥ 2 degrees" change relabels only random6724 hl: agreed; already disclosed in R01.
- **P2**, the IDEA?…-106/-107 post-hoc criteria: already disclosed; no change.

## Unresolved

- A selection principle: which rule minimises max_z‖L*(z)⁻¹‖ (L2 hand-off).
- The mechanism of single-pass CGS instability without truncation on the triangle and rotation 0.3.
- A measure-based regime classifier.
- Calibration of the rounding model for R07-type ratio tests.
- Recon-01's T-401 extensions, which need an audit.
- My checks use one seed per shape and M = 1681, like recon-01's, so both are finite-range MEASURED statements.

## Files changed

- Theory: 101–109, 113–115, 401, N101–N104 (History or correction lines). 110–112 have re-check lines.
- New: PD-N?…-105 `selection-and-truncation-both-matter-measured.md`, PD-N?…-106 `support-shape-does-not-classify-loss-regime.md`.
- Records: R01–R07 (appended correction sections), candidates.md (IDEA-101, -102, -106, -110, -111 corrections; C01 criteria and results), STATUS.md (R01, R03, R07 notes).
- SUMMARY.md: the write was blocked by the tool; its full corrected text is in the return.
- Code and logs: `l1_c01_recon_checks.py`, `l1_c01_u53_rerun.py`; `logs/c01_*.log`.
