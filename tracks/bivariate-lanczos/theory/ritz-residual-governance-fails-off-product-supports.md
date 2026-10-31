# PD-N?bivariate-lanczos-claude-101 — Ritz-residual governance of loss of orthogonality fails for the window recurrence outside product-aligned supports, and single sections over-predict on tensor grids

ID kind: PD-N.
Aliases: "loss ≈ u / min Ritz residual" fails; joint-Ritz governance fails off product supports; single-section over-prediction on tensor grids; K1/K2 outcome of plan L1-Q1.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] For the BJ window recurrence (block window, CGS, no reorthogonalization) and the HL variant (exact window, MGS with conditional second pass), with u := 2^-52:

(a) On every node set listed under Scope (b) — supports not aligned with the coordinate axes as a product — the measured loss max|Q̂_nᵀQ̂_n − I| exceeds u/ρ_O(n) by factors from 10² to 10¹⁴ at the informative degrees for each of O = H_x, H_y, Z = H_x + iH_y, the oblique section cos 1·H_x + sin 1·H_y, and N_k (HL SIMAX), where ρ_O(n) is the minimal Ritz residual of O on the computed span. Loss grows exponentially in n from n ≈ 8–12 while ρ_Z is identical, to the printed digits, to that of the unrotated set (rotation pairs).
(b) On the tensor Chebyshev grid 41² at n = 40, ρ_{H_x} = 1.8e-15 and ρ_{H_y} = 1.4e-15 (exact one-coordinate invariant subspaces inside S_40) while the loss is 1.8e-14 (bj) and 8.6e-15 (hl): single-section prediction exceeds the measured loss by ~10¹³.

   **(b) withdrawn as evidence (2026-10-31T23:05Z, reconstruction 01, B2).** n = 40 is the chain-completion degree of the 41 abscissae: S_40 contains every function of x, the one-coordinate subspaces are exactly invariant, and Bs = 0 in PD-T?…-103. At n = 36 the single-section prediction is consistent with the loss (u/ρ_X = 2.3e-14 at u = 2^-53, loss 1.8e-14; `logs/r01_input3.raw`). This is the same degeneracy that R01 excluded for Padua (N = M); excluded symmetrically, (b) is no evidence against single sections (`logs/c01_rule_sensitivity.log`). The measurement itself stands; its use does not.

Consequences for the candidates (corrected 2026-10-31T23:05Z, B2): IDEA?…-101 and IDEA?…-102 fail together on (a) and only there. On the informative product-type runs, single and joint residuals are not separated: under the frozen factor-3 rule the outcome flips between u = 2^-52 and u = 2^-53 (C01-1, `logs/c01_rule_sensitivity.log`).

   Original wording, preserved: "Consequences for the candidates: IDEA?…-101 (single-section governance) fails on (a) and (b); IDEA?…-102 (joint governance, IDEA?…-002/-006 re-measured) fails on (a). Both are consistent with the loss on random squares (regime of PD-T?…-107), where they do not separate."

## Negative-result scope (PD-N only)

Attempted mechanism: "loss of orthogonality of the BJ/HL window recurrence is predicted within a factor 3 by u divided by the minimal Ritz residual of a section" (IDEA?bivariate-lanczos-claude-101 with single sections; -102 with the joint section / N_k; frozen plan L1-Q1).
Parameter range: (a) uniform random square M = 1681 (seeds 0, 7) rotated by 0.3 and 1.0 rad; tensor Chebyshev 41² rotated by 0.3; random L-shape [−1,1]² \ (0,1]² M = 3000 (seed 1); random annulus 0.5 ≤ r ≤ 1 M = 3000 (seed 2); L-shape 61-grid M = 2760 and its rotation by 0.3; degrees 4–40 step 4; plus the probe sets (square rotated 0.05, π/4; disk; triangle; product Beta set rotated 0.3; sheared squares; M = 1681, n ≤ 24). (b) tensor 41², n = 40. Uniform weights except where stated. IEEE double, NumPy 2.5.3 / OpenBLAS.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) no Ritz residual predicts on non-product supports | MEASURED | `logs/r01_verdict.txt`, `logs/r01_{rotation,irregular}.raw`, `logs/r01_defect_probe.log` |
| (a′) growth is amplified rounding (scales with u) | MEASURED | `logs/r01_precision_scaling.log` (double vs long double, ratio ≈ 560–600 for an ε-ratio of 2048) |
| (b) tensor over-prediction | MEASURED; withdrawn as evidence against single sections (chain-completion degree, B2) | `logs/r01_input3.raw` (tensorcheb41 rows), exact invariance explained in R01 §3 M2; `logs/c01_rule_sensitivity.log` |

Candidate / claim disposition: IDEA?…-101 REJECTED: failed and IDEA?…-102 REJECTED: failed, both on (a) only (narrowed 2026-10-31, B2; IDEA?…-101 previously also on (b)). On product-type runs the two are not separated (K1 inconclusive). Both survive only as a regime statement on the listed set types (PD-T?…-107 (a)).
Rejection reason: failed (mechanisms shown not to achieve their aim within the stated node sets and degree range; MEASURED, not a universal refutation).

## Depends on

PD-T?…-101 part 6 (Z and N_k coincide in exact arithmetic; used to read N_k residuals from the real runs).

## Checks

Commands in `topics/bivariate-lanczos-20261031/directions/L1/R01.md` §6; code `tracks/bivariate-lanczos/code/L1/{l1_recurrence,l1_kill_test,l1_analyze_r01,l1_defect_probe,l1_precision_scaling}.py`. Independent rerun: none yet (Runs needed for the auditor).

## Sources

HL SIMAX p. 1088 (observation, LIT?…-119) for the joint formulation; plan.md L1-Q1 (frozen kill test).

## Proof or evidence

Measured; see the logs. Representative: random square M = 1681 seed 0 rotated by 0.3, bj: loss 2.9e-11 / 1.1e-4 / 1.0 at n = 16 / 24 / 32 with ρ_Z = 5.0e-2 / 4.3e-3 / 1.0e-4 (unrotated: loss 6.9e-15 / 2.9e-14 / 1.5e-12 with the same ρ_Z).

## Scope

Only the window recurrence as implemented (block and exact windows, CGS and ORTH) and the listed sets; it does not say that Ritz pairs are irrelevant (they track loss on random squares), nor anything about recurrences with full reorthogonalization.

## Open items

Larger M (10⁵–10⁶) to check that the growth rate is M-independent (Runs needed, AC servers). Mechanism: R02 (PD-T?…-104–107).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R01).
- 2026-10-31T23:05Z (response to reconstruction 01):
  - B2: (b) is withdrawn as evidence (chain-completion degree, excluded symmetrically to Padua N = M). The Consequences line is narrowed to (a); original wording kept in the Statement.
  - Major finding on PD-T?…-107: the title phrase "outside product-aligned supports" means the listed non-product set types. It is not a support classifier (PD-N?…-106: product supports with weights exp(8xy) and Gaussian clouds also lose far above the Ritz level).
  - PC-1 (R04) is folded in: the probe sets carry no Ritz data.
