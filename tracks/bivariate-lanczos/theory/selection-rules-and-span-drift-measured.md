# PD-T?bivariate-lanczos-claude-206 — Selection rule vs the space channel (measured): under full reorthogonalization the pivot-adaptive selection keeps the reference-free drift bound below √u on five of six non-product benchmarks (7–10 decades below BJ), the two-relation block recurrence on all six; no one-relation rule is uniformly safe

ID kind: PD-T.
Aliases: IDEA?…-207 measurements; adaptive selection + reorthogonalization; drift by selection; two-relation control.
Split from: none.
Split into: none. Negative parts: PD-N?…-203.

## Statement

[FP, MEASURED] One-relation window recurrences with selection rules dev (BJ), mirror (HL BIT), alt (X for 2j < t, else Y) and adapt (per column the candidate with larger β/‖Aq̂_p‖; reconstruction-01 rules, own implementation), block window, each with (A) CGS2 against all previous columns and (B) two-pass window without reorthogonalization; control: two-relation block recurrence, two CGS passes against blocks n−2, n−1, SVD completion. u = 2^-53. θ_LB := max_A max_{s<n} δ_A(s)/(2‖A‖) (reference-free lower bound on max_{s≤n} θ_s, θ_s the largest principal angle between the computed and the exact graded space of degree s; PD-T?…-205 part 4, valid for every selection); drift against the unrotated-frame reference (rotated squares, u·κ ≤ 4e-13) and a Koornwinder–Dubiner reference (triangle, u·κ ≤ 1e-14). Max over degrees, (A) runs:

| set (n max) | dev θ_LB | mirror | alt | adapt | two-relation |
|---|---|---|---|---|---|
| rot 0.3 (24) | 4.4e-7 | 2.2e-9 | 3.4e-10 | 1.6e-13 | 1.1e-15 |
| rot π/4 (24) | 2.8e-4 | 1.6e-1 | 1.5e-9 | 2.1e-7 | 1.2e-15 |
| disk (24) | 3.8e-10 | 2.4e-12 | 1.2e-12 | 1.5e-12 | 1.2e-15 |
| triangle (20) | 7.8e-4 | 2.8e-8 | 5.5e-9 | 6.4e-11 | 1.1e-13 |
| L-shape (30) | 8.7e-3 | 1.3e-1 | 1.1e-5 | 8.7e-13 | 4.6e-13 |
| annulus (30) | 1.3e-2 | 1.8e-9 | 1.3e-7 | 2.2e-10 | 1.7e-15 |
| square (32) | 1.2e-13 | 3.8e-13 | 3.9e-14 | 4.5e-14 | 4.0e-15 |
| tensor 41² (39) | 8.3e-15 | 8.3e-15 | 8.3e-15 | 1.6e-11 | 2.1e-12 |
| cubic checkerboard (29) | 4.9e-14 | 3.6e-12 | 5.0e-12 | 6.2e-16 | 1.3e-3 (loss 0.53) |

Reference drift at the last degree (A): rot0.3 5.2e-6 / 1.6e-8 / 2.1e-9 / 1.2e-12 / 6.1e-13; rotπ/4 4.1e-3 / 0.94 / 2.1e-8 / 1.9e-6 / 6.2e-13; triangle 1.0e-2 / 1.7e-7 / 7.6e-8 / 9.5e-10 / 3.7e-12 (dev / mirror / alt / adapt / two-relation). On the triangle and rotated squares the drift is 5–15× θ_LB (the lower bound is informative within about one decade).

(a) With the two-pass window and no reorthogonalization (B), adapt has plain loss ≤ 3.9e-13 (rot0.3), 2.9e-7 (rotπ/4), 7.9e-12 (disk), 1.6e-11 (triangle), 1.5e-12 (L-shape), 1.2e-10 (annulus), 1.5e-12 (square), 6.6e-11 (tensor), 7.4e-4 (cubic checkerboard); its θ_LB in (B) equals (A) within a factor 2. So for adapt the loss of orthogonality and the drift are of the same size, and reorthogonalization buys almost nothing beyond the two-pass window, except on the cubic checkerboard (coefficient channel; loss 7.4e-4 while θ_LB = 6e-16).
(b) Selection trades channels: adapt is 10³ worse than BJ on the tensor grid (θ_LB 1.6e-11 vs 8e-15) and its plain loss on the cubic checkerboard is similar to BJ's; the two-relation recurrence is ≥ 10³ better than every one-relation rule on the non-product sets but fails on the cubic checkerboard (loss 0.53, θ_LB 1.3e-3) and is 10³ worse than BJ on the tensor grid (consistent with reconstruction 01).
(c) Pre-registered verdicts (IDEA?…-207): dev killed (rot0.3, rotπ/4, triangle, L-shape, annulus), mirror killed (rot0.3, rotπ/4, triangle, L-shape), alt killed (rotπ/4, triangle via reference drift; L-shape, annulus via θ_LB), adapt killed on rotπ/4 only (θ_LB > √u from n = 22). No rule survives.

## Definitions

As in PD-T?…-202/-205 and candidates.md (IDEA?…-207).

## Assumptions

Double precision, NumPy 2.5.3; node sets of candidates.md; for 'adapt' under (A) the choice is made after the CGS2-against-all orthogonalization (under (B) after the first window pass) — the rule therefore picks possibly different parents in (A) and (B) (disclosed; the θ_LB of (A) and (B) agree within 2×).

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| table, (a)–(c) | MEASURED | `logs/r02_selection.raw.gz`, `logs/r02_verdicts.txt` |

## Depends on

PD-T?…-205 (θ_LB for both operators), PD-T?…-202.

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r02_selection.py > …/L2/logs/r02_selection.raw` (≈ 4 min), verdicts `l2_r02_verdicts.py`. The disk, L-shape, annulus and checkerboard drift references are ill-conditioned (u·κ up to 1e10); only θ_LB is used there. Independent rerun: none.

## Sources

Selection rules from reconstruction 01 (reviewer's finding; the origin of the adaptive rule as an L2 candidate), BPS 2010 Remark 9 (LIT?…-302, point-dependent variable choice); two-relation recurrence: Liu–Narayan 2023 (as reported, LIT record liu-narayan-2023).

## Proof or evidence

Measured; see logs.

## Scope

Nine node sets, M ≤ 3000, n ≤ 39; block window; four one-relation rules and one two-relation control. Not covered: rules that switch per node set region, two-relation with one pass, larger M (R02 cost run covers M ≤ 10⁵ for two sets).

## Open items

A selection criterion with a provable bound on the coupled residual growth (PD-T?…-205 covers only (C)-selections; 'adapt' violates (C) from degree 3, so neither PD-T?…-205's recursion nor an ω-estimate of the PD-T?…-203 form is available for it); a hybrid that uses two relations only where one-relation rules fail (rotπ/4-type isotropic supports) and one relation on product-type measures (where the two-relation completion fails).

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02). Kill rules pre-registered 00:24:54 (candidates.md).
- 2026-11-01T01:28:43+01:00: (reconstruction 01 F7) θ_LB described as a bound on max_{s≤n} θ_s; original: "(reference-free lower bound on the principal angle to S_n, PD-T?…-205 part 4);". (F1) Open item notes that 'adapt' violates (C). Measurements and verdicts unchanged (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
