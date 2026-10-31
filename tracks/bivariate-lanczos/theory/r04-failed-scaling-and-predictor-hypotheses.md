# PD-N?bivariate-lanczos-claude-103 — R04 failures: linear onset of the rotation-induced growth rate, universality of the node-propagator predictor, and unconditional stability of the two-relation control

ID kind: PD-N.
Aliases: H_lin failure; predictor non-universality; two-relation failure on clustered checkerboards.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] Within the stated ranges:

(a) **H_lin fails** (IDEA?…-112, pre-registered K3): the excess growth rate g̃(θ) of the exact-coefficient propagator response on the square (M = 1681, seed 11) rotated by θ is not linear in θ: g̃/θ = 1.02 at θ = 0.025 and 4.39 at θ = 0.2 (factor 4.3 > 3).
(b) **The node-propagator response is not a universal loss predictor** (IDEA?…-107, -114, -115): with uniform forcing u/√M it under-predicts the triangle (50× at n = 12, 10³ at n = 16) and over-predicts the clustered checkerboard by more than 10¹⁸ (response 1e3 at n = 8, where the loss is 7e-16: the uniform forcing drives nodes of weight down to 1e-33 at the wrong scale); with componentwise-scaled forcing it under-predicts the triangle (25×, 350×) and the clustered checkerboard (2.5·10³ at n = 16, 4·10⁵ at n = 20); with worst-case absolute coefficient noise it over-predicts by up to 10⁷ (clustered checkerboard) and 40× (square).
(c) **The two-relation block recurrence (R03 control) is not unconditionally stable** (scope restriction of IDEA?…-111): on the clustered checkerboard (m = 30) its loss is 1e-11, 1e-5, 1e-3, 0.4 at n = 8, 12, 16, 20, far worse than BJ (7e-16, 3e-14, 1e-11, 4e-9).

## Negative-result scope (PD-N only)

Attempted mechanisms: (a) linear-in-coupling onset of the non-product amplification (toy-model expectation, R04 §2); (b) "the per-node propagator response predicts loss" (IDEA?…-107 with forcing models of IDEA?…-114, -115); (c) "using both relations removes the instability" as an unconditional remedy (IDEA?…-111).
Parameter range: (a) θ ∈ {0.0125, 0.025, 0.05, 0.1, 0.2, 0.4}, n = 12…24; (b) seed-11 sets (square, rotation π/4, disk, triangle), checkerboards m = 30 (Chebyshev–Lobatto, equispaced, cubic clustering), n ≤ 32; (c) the cubic-clustered checkerboard, n ≤ 28.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r04_near_product.log` |
| (b) | MEASURED | `logs/r02_node_propagator.log`, `r04_scaled_predictor.log`, `r04_coef_forcing.log`, `r04_checkerboard_diag.log` |
| (c) | MEASURED | `logs/r04_checkerboard_more.log` |

Candidate / claim disposition: H_lin REJECTED: failed; IDEA?…-114 REJECTED: failed (as an improvement, S1); IDEA?…-115 REJECTED: failed; IDEA?…-107 restricted (diagnostic for the vector channel only); IDEA?…-111 restricted (survives on rotated squares and the disk, fails on the clustered checkerboard).
Rejection reason: failed (MEASURED, stated ranges).

## Depends on

PD-T?…-104, -107, -109, -112.

## Checks

R04.md §5 commands.

## Sources

None.

## Proof or evidence

Measured; see logs.

## Scope

Finite ranges only; (a) concerns the onset at moderate degrees (n ≤ 24) and does not exclude linear asymptotics for larger n.

## Open items

A predictor for the coefficient channel; a stable remedy covering both channels (L2 hand-off).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R04).
