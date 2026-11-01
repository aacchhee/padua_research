# PD-N?bivariate-lanczos-claude-101 — Ritz-residual governance of loss of orthogonality fails for the BJ/HL window recurrence on the listed non-product node sets (R01 main runs: all sections; seed-11 sets: Z only)

Final ID: **PD-N007** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: "loss ≈ u / min Ritz residual" fails; joint-Ritz governance fails off product supports; single-section over-prediction on tensor grids; K1/K2 outcome of plan L1-Q1.
Split from: none.
Split into: none.

## Statement

[Statement (a) rewritten 2026-11-01T08:33:59+01:00, Codex audit-01 finding LL-M1 and consolidated item 3. The original preamble and (a) are preserved verbatim in History.]

[FP, MEASURED] For the BJ window recurrence (block window, CGS, no reorthogonalization) and the HL variant (exact window, MGS with conditional second pass). ρ_O(n) is the minimal Ritz residual of the object O on the computed span (one Householder QR of Q̂_n), and L(n) = max|Q̂_nᵀQ̂_n − I|.

**Thresholds.** The pre-registered decision rule of R01 (candidates.md, IDEA?…-101) fixes u := 2^-52 and τ = 10³u. The informative degrees are D_{r,O} = {n : L(n) ≥ τ or u/ρ_O(n) ≥ τ}. "O predicts" iff L(n)/(u/ρ_O(n)) ∈ [1/3, 3] for every n ∈ D_{r,O}. This factor-3 band is the only kill threshold. The reporting tag "/under" (ratio > 30 at some informative degree, post hoc, R01 §2) and the magnitudes quoted below are descriptive, not thresholds. The plan's [FP] u is the unit roundoff 2^-53, so the ranges are given for both conventions.

(a1) **R01 main non-product runs — all sections.**
   - Runs (14): the uniform random square M = 1681, seed 0 rotated by 0.3 and seed 7 rotated by 1.0; tensor Chebyshev 41² rotated by 0.3; the L-shape grid (61-grid, M = 2760) and its rotation by 0.3; the random L-shape (M = 3000, seed 1); the random annulus 0.5 ≤ r ≤ 1 (M = 3000, seed 2). Each with methods bj and hl, n = 4, 8, …, 40.
   - Objects: O = H_x, H_y, Z = H_x + iH_y, the oblique section cos 1·H_x + sin 1·H_y, and N_k. N_k is computed on the span of the complex HL SIMAX run on the same set and compared with the bj/hl loss.
   - Under the pre-registered rule (u = 2^-52) no object predicts on any of the 14 runs. No informative (run, object, degree) triple lies in the factor-3 band. At every informative degree of every (run, object), L(n)/(u/ρ_O(n)) ∈ [1.02·10², 1.03·10¹⁴]. The first informative degree is 8, 12 or 16.
   - At u = 2^-53 (τ = 10³·2^-53, which adds lower informative degrees) the ratios lie in [4.4·10¹, 2.1·10¹⁴]. Again none is in the band and none is below 30, but the lower end 10² does not hold: e.g. annulus hl, H_y, 44 at n = 12; random1681 s0 rotated 0.3, hl, H_x, 55 at n = 12.
   - N_k against the SIMAX run's own loss: ratios between 1.5·10² and 5.3·10¹³ at 2^-52 (PD-N?…-102).
   - Loss growth: on these runs the loss rises by 1.3–4.4 decades per 4 degrees between n = 8 and n = 24 (0.0–1.7 between n = 4 and 8), and saturates at 0.1–1 by n = 28–36.
   - Rotation pairs (random1681 s0 / 0.3, s7 / 1.0, tensor 41² / 0.3, L-shape grid / 0.3; bj and hl): ρ_Z of the rotated set equals that of the unrotated set to relative 2.3·10⁻¹² while both losses are below 10⁻⁸, and to four printed digits through n = 24. The two separate from n = 28, when the rotated loss is O(0.1–1).
   - Evidence: stored R01 data, reanalysed in `logs/a01_n101_reanalysis.log` (A)–(C).
(a2) **Seed-11 sets of `l1_node_propagator.py` — Z only, bj only.**
   - Sets: the square M = 1681 (default_rng(11)) rotated by 0.3 and by π/4, the disk, and a triangle (M = 1681 each). The triangle is a different random realisation from the probe's.
   - At the degrees with L(n) ≥ τ (u = 2^-52), L/(u/ρ_Z) ≈ 5.7·10³–8.3·10⁷ (rotation 0.3, n = 16–24), 2.0·10³–6.7·10¹⁰ (π/4, n = 12–24), 3·10²–1.2·10⁶ (disk, n = 12–24) and 1.7·10³–1.1·10¹³ (triangle, n = 8–20).
   - These ratios are formed from one-significant-digit log values, so each is uncertain by up to a factor ≈ 3. H_x, H_y, the oblique section and N_k were not computed on these sets.
   - Evidence: `logs/r02_node_propagator.log`; reanalysis (D).
(a3) **Probe-only sets — no Ritz residuals computed; not part of the negative statement.**
   - `l1_defect_probe.py` (seed 11, M = 1681, n ≤ 24) measured only the loss and the defects on the square rotated by 0.05, the sheared squares (x, y + 0.5x) and (x + 0.5y, y), and the product Beta set rotated by 0.3 (and on the sets of (a2)). No statement about Ritz governance is made for these sets.
   - In particular the 0.05 rotation is not evidence for (a). Its loss is 2e-13 at n = 24 (probe). An independent Codex audit-01 implementation on the same seed-11 set gives loss 4.21e-13 at n = 24 and L/(u/ρ_O) = 3.72 (H_x), 3.93 (H_y), 7.16 (Z) at u = 2^-52 (7.4, 7.9, 14.3 at 2^-53): outside the factor-3 band, but far below 10².
   - Source: `audit-01/L1-later/independent_checks.log`; this is the auditor's measurement, recorded here as context only.
(a′) **Growth scales with the unit roundoff.** On the seed-11 square rotated by 0.3 (M = 1681, bj), the loss at n = 16 / 20 is 3.8e-11 / 1.2e-8 in double and 6.8e-14 / 2.0e-11 in long double: ratio ≈ 560–600 for an ε-ratio of 2048 (`logs/r01_precision_scaling.log`).
(b) On the tensor Chebyshev grid 41² at n = 40, ρ_{H_x} = 1.8e-15 and ρ_{H_y} = 1.4e-15 (exact one-coordinate invariant subspaces inside S_40) while the loss is 1.8e-14 (bj) and 8.6e-15 (hl): single-section prediction exceeds the measured loss by ~10¹³.

   **(b) withdrawn as evidence (2026-10-31T23:05Z, reconstruction 01, B2).** n = 40 is the chain-completion degree of the 41 abscissae: S_40 contains every function of x, the one-coordinate subspaces are exactly invariant, and Bs = 0 in PD-T?…-103. At n = 36 the single-section prediction is consistent with the loss (u/ρ_X = 2.3e-14 at u = 2^-53, loss 1.8e-14; `logs/r01_input3.raw`). This is the same degeneracy that R01 excluded for Padua (N = M); excluded symmetrically, (b) is no evidence against single sections (`logs/c01_rule_sensitivity.log`). The measurement itself stands; its use does not.

Consequences for the candidates (corrected 2026-10-31T23:05Z, B2): IDEA?…-101 and IDEA?…-102 fail together on (a) and only there. On the informative product-type runs, single and joint residuals are not separated: under the frozen factor-3 rule the outcome flips between u = 2^-52 and u = 2^-53 (C01-1, `logs/c01_rule_sensitivity.log`).

   Original wording, preserved: "Consequences for the candidates: IDEA?…-101 (single-section governance) fails on (a) and (b); IDEA?…-102 (joint governance, IDEA?…-002/-006 re-measured) fails on (a). Both are consistent with the loss on random squares (regime of PD-T?…-107), where they do not separate."

## Negative-result scope (PD-N only)

Attempted mechanism: "loss of orthogonality of the BJ/HL window recurrence is predicted within a factor 3 by u divided by the minimal Ritz residual of a section" (IDEA?bivariate-lanczos-claude-101 with single sections; -102 with the joint section / N_k; frozen plan L1-Q1).
Parameter range [split by scope 2026-11-01T08:33:59+01:00, LL-M1; original in History]:
- (a1) uniform random square M = 1681 (seed 0 rotated by 0.3, seed 7 rotated by 1.0 rad); tensor Chebyshev 41² rotated by 0.3; random L-shape [−1,1]² \ (0,1]² M = 3000 (seed 1); random annulus 0.5 ≤ r ≤ 1, M = 3000 (seed 2); L-shape 61-grid M = 2760 and its rotation by 0.3. Degrees 4–40 step 4, bj and hl, all five objects.
- (a2) the seed-11 square rotated by 0.3 and π/4, the disk and a triangle (M = 1681, n ≤ 24, triangle n ≤ 20), bj, Z only.
- The probe-only sets (a3) are outside the negative statement.
- (b) tensor 41², n = 40.
- Uniform weights except where stated. IEEE double, NumPy 2.5.3 / OpenBLAS.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a1) no section (H_x, H_y, Z, oblique, N_k) predicts on the 14 R01 main non-product runs | MEASURED | `logs/r01_verdict.txt`, `logs/r01_{rotation,irregular,input3}.raw`; ranges at 2^-52 and 2^-53 in `logs/a01_n101_reanalysis.log` |
| (a2) Z does not predict on the four seed-11 non-product sets (bj) | MEASURED | `logs/r02_node_propagator.log` (one significant digit); `logs/a01_n101_reanalysis.log` (D) |
| (a3) probe-only sets | no claim (loss data only, no Ritz residuals) | `logs/r01_defect_probe.log`; Codex audit-01 `independent_checks.log` (rotation 0.05: 3.7–7.2 at 2^-52) |
| (a′) growth is amplified rounding (scales with u) | MEASURED | `logs/r01_precision_scaling.log` (seed-11 square rotated 0.3; double vs long double, ratio ≈ 560–600 for an ε-ratio of 2048) |
| (b) tensor over-prediction | MEASURED; withdrawn as evidence against single sections (chain-completion degree, B2) | `logs/r01_input3.raw` (tensorcheb41 rows), exact invariance explained in R01 §3 M2; `logs/c01_rule_sensitivity.log` |

Candidate / claim disposition: IDEA?…-101 REJECTED: failed and IDEA?…-102 REJECTED: failed, both on (a1)–(a2) only (narrowed 2026-10-31, B2; IDEA?…-101 previously also on (b); narrowed 2026-11-01T08:33:59+01:00, LL-M1: the probe-only sets (a3) were never part of the evidence and are removed from the scope). On product-type runs the two are not separated (K1 inconclusive). Both survive only as a regime statement on the listed set types (PD-T?…-107 (a)).
Rejection reason: failed (mechanisms shown not to achieve their aim within the stated node sets and degree range; MEASURED, not a universal refutation).

## Depends on

PD-T?…-101 part 6 (Z and N_k coincide in exact arithmetic; used to read N_k residuals from the real runs).

## Checks

Commands in `topics/bivariate-lanczos-20261031/directions/L1/R01.md` §6; code `tracks/bivariate-lanczos/code/L1/{l1_recurrence,l1_kill_test,l1_analyze_r01,l1_defect_probe,l1_precision_scaling}.py`.
- Reanalysis of the stored data for (a1)–(a2) (added 2026-11-01T08:33:59+01:00): `python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_n101_reanalysis.py topics/bivariate-lanczos-20261031/directions/L1/logs > topics/bivariate-lanczos-20261031/directions/L1/logs/a01_n101_reanalysis.log`. This reads stored data only and reruns no recurrence.
- Independent checks (Codex audit-01, L1-later; [replaces "Independent rerun: none yet (Runs needed for the auditor)"]):
  - An independent CGS/QR/Ritz implementation on the seed-11 square rotated by 0.05 and by π/4 (n = 24), and on the exp(8xy) square. For π/4, Z: 8.82·10¹⁰ at 2^-52. Log `audit-01/L1-later/independent_checks.log`, sha256 `dd49d6a0bbd2ec832b5d3274f7ff06bc6404bf2e6f404d35ca6f33190efab0ad`.
  - A reanalysis of the stored R01 raw data: K1 true at 2^-52 and false at 2^-53, with the recorded sets. Log `rule_reanalysis.log`, sha256 `611e9d0aa5ce7e292be59a035238601527dd576b3d1772b65a9affd5ecc71e55`.
  - The R01 main runs (a1) have not been re-executed independently.

## Sources

HL SIMAX p. 1088 (observation, LIT?…-119) for the joint formulation; plan.md L1-Q1 (frozen kill test).

## Proof or evidence

Measured; see the logs and `logs/a01_n101_reanalysis.log`. Representative: random square M = 1681 seed 0 rotated by 0.3, bj: loss 2.9e-11 / 1.1e-4 / 1.0 at n = 16 / 24 / 32 with ρ_Z = 5.0e-2 / 4.3e-3 / 1.0e-4 (unrotated: loss 6.9e-15 / 2.9e-14 / 1.5e-12 with the same ρ_Z).

## Scope

Only the window recurrence as implemented (block and exact windows, CGS and ORTH) and the sets of (a1)–(a2), with the objects stated there; the probe-only sets (a3) carry no Ritz claim; it does not say that Ritz pairs are irrelevant (they track loss on random squares), nor anything about recurrences with full reorthogonalization.

## Open items

Larger M (10⁵–10⁶) to check that the growth rate is M-independent (Runs needed, AC servers). Mechanism: R02 (PD-T?…-104–107).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R01).
- 2026-10-31T23:05Z (response to reconstruction 01):
  - B2: (b) is withdrawn as evidence (chain-completion degree, excluded symmetrically to Padua N = M). The Consequences line is narrowed to (a); original wording kept in the Statement.
  - Major finding on PD-T?…-107: the title phrase "outside product-aligned supports" means the listed non-product set types. It is not a support classifier (PD-N?…-106: product supports with weights exp(8xy) and Gaussian clouds also lose far above the Ritz level).
  - PC-1 (R04) is folded in: the probe sets carry no Ritz data.
- 2026-11-01T08:33:59+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later LL-M1 and consolidated item 3; branch head 5f52331). Status unchanged (MEASURED); the scope is narrowed.
  - The old (a) asserted a 10²–10¹⁴ excess on every listed set and for each residual. That included probe sets with no Ritz data (rotation 0.05, shears, rotated Beta set) and objects never computed on the seed-11 sets. It also held only at u = 2^-52. Now:
    - (a1) gives the R01 main runs with all objects, at both conventions;
    - (a2) gives the seed-11 sets with Z only;
    - (a3) states that the probe-only sets carry no Ritz claim. The 0.05 rotation is near the Ritz level by the auditor's independent measurement.
  - The factor-3 band is identified as the only kill threshold; the factor 30 and the quoted magnitudes are descriptive. (L1 defines no √u threshold. The √u-versus-10√u distinction of the consolidated checklist concerns L2's T207.)
  - The rotation-pair statement on ρ_Z and the exponential-growth sentence are restated with the measured precision and degree ranges.
  - Original title: "PD-N?bivariate-lanczos-claude-101 — Ritz-residual governance of loss of orthogonality fails for the window recurrence outside product-aligned supports, and single sections over-predict on tensor grids".
  - Original Statement preamble and (a), verbatim:
    > [FP, MEASURED] For the BJ window recurrence (block window, CGS, no reorthogonalization) and the HL variant (exact window, MGS with conditional second pass), with u := 2^-52:
    > 
    > (a) On every node set listed under Scope (b) — supports not aligned with the coordinate axes as a product — the measured loss max|Q̂_nᵀQ̂_n − I| exceeds u/ρ_O(n) by factors from 10² to 10¹⁴ at the informative degrees for each of O = H_x, H_y, Z = H_x + iH_y, the oblique section cos 1·H_x + sin 1·H_y, and N_k (HL SIMAX), where ρ_O(n) is the minimal Ritz residual of O on the computed span. Loss grows exponentially in n from n ≈ 8–12 while ρ_Z is identical, to the printed digits, to that of the unrotated set (rotation pairs).
  - Original Parameter range: "(a) uniform random square M = 1681 (seeds 0, 7) rotated by 0.3 and 1.0 rad; tensor Chebyshev 41² rotated by 0.3; random L-shape [−1,1]² \ (0,1]² M = 3000 (seed 1); random annulus 0.5 ≤ r ≤ 1 M = 3000 (seed 2); L-shape 61-grid M = 2760 and its rotation by 0.3; degrees 4–40 step 4; plus the probe sets (square rotated 0.05, π/4; disk; triangle; product Beta set rotated 0.3; sheared squares; M = 1681, n ≤ 24). (b) tensor 41², n = 40. Uniform weights except where stated. IEEE double, NumPy 2.5.3 / OpenBLAS."
  - Original status row (a): "| (a) no Ritz residual predicts on non-product supports | MEASURED | `logs/r01_verdict.txt`, `logs/r01_{rotation,irregular}.raw`, `logs/r01_defect_probe.log` |".
  - Correction of the previous History entry: the 2026-10-31T23:05Z bullet "PC-1 (R04) is folded in: the probe sets carry no Ritz data" was inaccurate. The Statement kept the blanket range; PC-1 is applied only now.
