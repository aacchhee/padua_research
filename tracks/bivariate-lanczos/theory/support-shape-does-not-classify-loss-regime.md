# PD-N?bivariate-lanczos-claude-106 — The support shape does not classify the loss regime: product supports with non-product weights, and sampled product densities, lose orthogonality far above the Ritz level

ID kind: PD-N.
Aliases: support-based classifier refuted; "product-aligned supports" reading withdrawn; recon-01 major finding on PD-T?…-107.
Split from: PD-T?bivariate-lanczos-claude-107 ((a)/(b) read as a classifier by support), PD-N?…-101 (title wording).
Split into: none.

## Statement

[FP, MEASURED] BJ window recurrence (block window, CGS, double). u = 2^-53 and u/ρ_Z the joint Ritz prediction on the computed span (minimal Ritz residual of Z = X + iY) [note 2026-10-31T23:37Z, recon-02 m2: Paige's prediction is u‖A‖/ρ. On the square ‖X‖, ‖Y‖ ≤ 1, so (a) is unaffected. On the standard Gaussian cloud ‖X‖, ‖Y‖ ≈ 3–4, so "2.4·10³×" in (b) overstates the excess by about that factor (≈ 6–8·10² × u‖Z‖/ρ_Z). The conclusion is unchanged].

(a) **Product support, non-product weights.** On the seed-11 square (M = 1681) with weights exp(c·xy), loss / u/ρ_Z:

   | c | n = 12 | n = 24 |
   |---|---|---|
   | 1 | 2.3e-15 / 1.3e-15 | 8.9e-14 / 3.3e-14 (2.7×) |
   | 4 | — | 1.9e-12 / 5.9e-14 (32×) |
   | 8 | 2.5e-12 / 2.2e-15 | 1.9e-8 / 1.2e-13 (1.6·10⁵×) |

(b) **Sampled product density.** A standard Gaussian cloud (M = 1681, default_rng(12)) reaches loss 1.1e-4 at n = 24 against u/ρ_Z = 4.6e-8 (2.4·10³×). The two-relation block recurrence reaches 6.3e-8 there, i.e. Ritz-type (1.4×).

Consequence: "product-aligned support ⇒ Ritz-type (product-level) loss" is false. Both examples have a product support: the square in (a), and in (b) the plane with a product density. The regime is set by the measure, through its recurrence coefficients (compare the within-degree coupling of PD-T?…-107 (e) and the product-type coefficients of PD-T?…-105, -111), not by the support.

The uniformly sampled square, also a sampled product density, is Ritz-type to n ≈ 22 (PD-T?…-107 (a)). So "sampled product density" is not a classifier either.

## Negative-result scope (PD-N only)

- Attempted classification: the support-based reading of PD-T?…-107 (a)/(b), of the PD-N?…-101 title ("outside product-aligned supports"), and of the R01 M1 and R02/R03 §4 wording.
- Parameter range: the sets above, n ≤ 24.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a), (b) | MEASURED | `topics/bivariate-lanczos-20261031/directions/L1/logs/c01_recon_runs.log` (developer rerun, own seeds); independently `reviews/logs_L1/extra.log` (ii) and `sweep_alt.log` (reconstruction 01: exp(8xy) 4.0e-7 at n = 24, ≈ 10³ above u/ρ_Z; Gaussian 3.6e-5 vs 5.8e-7; their exp(4xy) run was stable, mine shows a 32× excess at n = 24) |

Candidate / claim disposition: support-based classification REJECTED: refuted (stated scope). PD-T?…-107 (a), (b) are kept as statements about the listed set types.
Rejection reason: refuted (MEASURED).

## Depends on

PD-T?…-107.

## Checks

The criterion C01-4 (candidates.md) was written before the run. Both parts were reproduced by an independent implementation (reconstruction 01).

## Sources

Reconstruction 01 (reviews/L1-reconstruction-01.md, PD-T?…-107 major finding) found this first.

## Proof or evidence

Measured: `python3 -I tracks/bivariate-lanczos/code/L1/l1_c01_recon_checks.py runs` (C01-4 section).

## Scope

Two weight families and one cloud; one seed each.

## Open items

A quantitative classifier in terms of the measure. Candidates are the within-degree coupling (PD-T?…-107 (e)), the exact-propagator norm (PD-T?…-109 (a)), and the off-pattern gains of PD-T?…-114 at a nearby product-type point. None is tested as a classifier.

## History

- 2026-10-31T23:05Z: created (Claude Opus 5.5, xhigh; L1 response to reconstruction 01, major finding on PD-T?…-107).
- 2026-10-31T23:37Z (response to reconstruction 02): CONFIRMED WITH CORRECTIONS. m2 (‖A‖ factor) is noted in the Statement. Recon-02 corrects its own recon-01 wording: its exp(4xy) run gives 4.6× u/ρ_Z at n = 24, not "stable". The developer's 32× is a seed-level difference, not a contradiction.
