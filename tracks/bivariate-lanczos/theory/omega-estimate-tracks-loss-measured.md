# PD-T?bivariate-lanczos-claude-203 — The online 2D ω-estimate (exact ω-recurrence with rounding-model sources) never underestimates the loss by more than 1.44× (E1, E2, E2D, E3) or 3.85× (sign-matched E1D) on the benchmark set; its E1 variant tracks it within 7.1× on the informative non-checkerboard benchmarks (E2 within 12×: triangle overestimate 11.7); it overestimates the clustered-checkerboard coefficient channel by ~10⁵

Final ID: **PD-T048** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: L2-Q1(a) answer; E1/E1D/E2/E2D/E3; 2D Simon ω-estimate; source audit.
Split from: none.
Split into: PD-N?…-205 (E3 failure, formerly only in (b)).

## Statement

[FP, MEASURED] Plain BJ run (block window, CGS), u = 2^-53, the 12 benchmarks of directions/L2/candidates.md. Estimators (IDEA?…-201, -202, -205): online replay of the exact ω-recurrence (PD-T?…-106) with the run's computed coefficients, T_J = Ĥ_J built causally from lower-degree data, in-window CGS cascade propagated, sources θ = ε·u·(‖(h,β)‖₂ + ‖T_Ae_l‖₂) out of window and ε·u·‖(h,β)‖₂ in window; E1: ε iid N(0,1), median of 5 seeds; E1D: ε = sign of the propagation term; E2/E2D: J-columns' rows measured exactly (commutator channel exact); E3: E1 with in-window scale u·|q̂_l|ᵀ|Aq̂_p|. With D = degrees where L or E ≥ 10³u, U := max_D L/E, O := max_D E/L:

| benchmark | E1 U / O | E2 U / O | E1D U | E3 U / O |
|---|---|---|---|---|
| square | 0.64 / 2.5 | 0.65 / 1.9 | 0.07 | 0.59 / 2.6 |
| rot 0.3 | 0.23 / 7.1 | 0.71 / 4.6 | 0.18 | 0.26 / 6.7 |
| rot π/4 | 0.49 / 4.6 | 0.93 / 3.9 | 0.30 | 0.49 / 3.8 |
| disk | 1.04 / 1.4 | 1.14 / 1.4 | 0.65 | 1.20 / 1.2 |
| triangle | 1.06 / 5.6 | 1.04 / 12 | 3.85 | 1.44 / 5.3 |
| L-shape | 0.84 / 1.9 | 1.22 / 1.7 | 0.99 | 0.96 / 1.7 |
| annulus | 1.08 / 2.6 | 1.05 / 2.4 | 0.65 | 1.02 / 2.5 |
| tensor 41², Padua 48, CL checkerboard | uninformative (L, E < 10³u) | uninformative | ≤ 0.20 | uninformative |
| equispaced checkerboard | 0.06 / 23 | 0.15 / 9.6 | 0.06 | 0.08 / 18 |
| cubic-clustered checkerboard | 0.006 / 2.4e5 | 0.002 / 1.4e5 | 0.004 | 0.002 / 1.8e5 |

(a) **Frozen kill test (L2-Q1, first clause): not fired** for any estimator: max U = 1.08 (E1), 1.22 (E2), 3.85 (E1D), 1.15 (E2D), 1.44 (E3) < 10.
(b) **Tracking.** Off the checkerboards E1 tracks within the factor max(U, O) ≤ 7.1 (pre-registered definition) on all informative non-product and near-product sets (23 on the equispaced checkerboard) [audit-01: the factor 7.1 is E1's; the other estimators reach O = 11.7 (E2, triangle; table value 12), 13.6 (E2D, triangle) and 13.4 (E2D, rotπ/4), from the verdict file and audit-01's fresh `omega-rerun.log`], including the triangle where the L1 node-forcing predictor under-estimated by 50–10³ (PD-T?…-107 (c)). It does **not** track within a constant factor on the cubic-clustered checkerboard (overestimate 2.4·10⁵) — the coefficient channel. E3 does not repair this (1.8·10⁵; its pre-registered improvement criterion, ≥ 100× drop, fails).
(c) **Source audit (long double, actual one-step sources / model scale).** F-steps out of window: max 0.06–0.6, median 0.005–0.03 (the model scale u‖·‖ exceeds the actual inner-product rounding by ~√M on spread vectors); in-window: max 1.6–20, median 0.01–0.3; J-steps out of window (contain the commutator source (C_res e_l)ᵀq̂_p): on product-type sets ≤ 2.6 (tensor), ≤ 1.1 (checkerboards); on non-product sets they grow with degree to max 10⁴–10¹⁰ × the model scale (rotπ/4 6.1e8 at n = 24, triangle 8.6e8 at n = 20, L-shape 4.5e10 at n = 30), median 10–3·10⁴. Despite this, E1 (which ignores the commutator source) and E2 (which includes it exactly) give the same verdicts: the commutator sources stay below the propagated in-window and F contributions in the loss (consistent with L1 PD-T?…-107 (d)).
(d) **Cost of the estimate.** As coded (dense storage) O(N²) flops per column, i.e. O(N³) per run; O(N²n) would require exploiting the band sparsity of T_F and Ĥ_J; independent of M in either form; replay times 1–12 s for N ≤ 1176 (all five estimators).

## Definitions

As in candidates.md (IDEA?…-201, -202, -205). L(n) = max|Q̂_nᵀQ̂_n − I| (double Gram), E(n) = max off-diagonal |ω̃| over degree ≤ n (diagonal model u).

## Assumptions

Double precision, NumPy 2.5.3 (OpenBLAS), Python 3.13.18, x87 long double for the audit; single machine (2 cores); seeds 0–4 for the random sources; node sets as in candidates.md.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) kill test not fired | MEASURED | `logs/r01_omega.raw`, `r01_omega_e3.raw`, `r01_verdicts.txt` |
| (b) tracking factors | MEASURED | same |
| (c) source audit | MEASURED | `logs/r01_omega.raw` ("audit" lines; Padua not audited, N > 820) |
| (d) cost | MEASURED (timing) / routine count | script timings |

## Depends on

PD-T?…-106, -104 part 2, -101 (CONDITIONAL inputs; exact ω-recurrence and Ĥ_J construction).

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r01_omega.py > …/L2/logs/r01_omega.raw` (≈ 70 s); `… l2_r01_omega.py --e3 > …/L2/logs/r01_omega_e3.raw`; verdicts by `l2_r01_verdicts.py`. Causality: the estimator uses T_F columns of children already formed and Ĥ_J columns built after each completed degree (J-step at degree t uses degree ≤ t−3), so the replay equals an online run. Independent rerun: Codex audit-01 reran E1/E1D/E2/E2D and E3 on rotπ/4, triangle and the cubic checkerboard (`topics/bivariate-lanczos-20261031/audit-01/L2/omega-rerun.log`, `e3-rerun.log`; Python 3.12.14, NumPy 2.3.5): modest tracking on the first two (E1 U/O 0.495/4.61 and 1.063/5.58; E2 0.931/3.89 and 1.039/11.71), extreme overestimation on the cubic checkerboard (E1 O = 2.43e5); the other nine benchmarks were not rerun.

## Sources

LIT?…-210/-212 (Simon 1984: random-source ω-estimate, overestimates early, tracks near √u — as digested). No comparison with Simon's constants is claimed.

## Proof or evidence

Measured; tables above are the verdict file's numbers.

## Scope

12 benchmarks, M ≤ 3000, BJ block window CGS, n ≤ 47. The estimate is an a posteriori-free online model (no inner products beyond the recurrence's, except E2's J-rows and E3's absolute dot products); it is a diagnostic, not a bound. It tracks loss of orthogonality only: it says nothing about the drift of the spans (PD-N?…-201), which it cannot see.

## Open items

A source model that sees the closed-loop damping of the coefficient channel (PD-T?…-115) so that clustered product-type measures are not over-estimated by 10⁵; the estimate for selection rules other than BJ: for selections satisfying condition (C) of PD-T?…-205 (dev, mirror, alt) both partly implicit sections are defined; for 'adapt' (violates (C) from degree 3) the implicit-section recursion is not defined and no estimate of this form exists; M-dependence of the √M overestimate of the out-of-window scale.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R01). Kill rules written before the runs (candidates.md, 00:06); E3 written after seeing E1 (disclosed there, 00:12).
- 2026-11-01T01:28:43+01:00: (reconstruction 01 F5) title bound corrected; original title: "PD-T?bivariate-lanczos-claude-203 — The online 2D ω-estimate (exact ω-recurrence with rounding-model sources) never underestimates the loss by more than 1.5× on the benchmark set and tracks it within 7× off product-type measures; it overestimates the clustered-checkerboard coefficient channel by ~10⁵". (Reconstruction 01 §4) cost (d) corrected; original: "One dense update of order N per column: O(N²·n) flops with dense storage, independent of M;". (F1) Open item on other selections restricted to (C)-selections; original: "the estimate for selection rules other than BJ (both sections implicit in part);". Measurements unchanged (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
- 2026-11-01T01:29:55+01:00: Split into updated (original: "Split into: none."), reconstruction 01 F3 (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, claim-coverage note on PD-T?…-203: the headline factor 7 applies to E1; triangle E2 overestimate 11.7147; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`) Title: original "…never underestimates the loss by more than 1.44× (E1, E2, E2D, E3) or 3.85× (sign-matched E1D) on the benchmark set and tracks it within 7× off product-type measures; it overestimates the clustered-checkerboard coefficient channel by ~10⁵" → names E1 for the 7.1× tracking and states E2's 11.7×. (b): bracketed note added, original sentence kept. Checks: original "Independent rerun: none." → audit-01 partial rerun recorded. Measurements, verdicts and status MEASURED unchanged.
