# PD-N?bivariate-lanczos-claude-204 — Correctly rounded (or long-double) window dot products do not remove the clustered-checkerboard coefficient channel; they reduce the rotπ/4 loss 14–19×, make the triangle worse at n = 16, and leave the drift unchanged

ID kind: PD-N.
Aliases: IDEA?…-210 killed (P1, P2); L1 hand-off "compensated/extra-precision window dot products" tested; dot rounding is not the special driver.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ block window, one CGS pass, u = 2^-53; window coefficients computed in double (BLAS), correctly rounded ('exact': Dekker products + math.fsum, verified against exact rational arithmetic), or with the whole step in x87 long double and the vectors stored in double ('ld').

(a) **Clustered checkerboards (P1 killed on all four).** L(20), L(24) double → exact: quadratic m = 30 1.17e-11 → 5.11e-12, 1.43e-10 → 1.08e-10 (2.3×, 1.3×); cubic m = 30 6.67e-9 → 1.65e-9, 6.31e-7 → 2.57e-7 (4.0×, 2.5×); quartic m = 30 1.44e-6 → 8.26e-7, 1.78e-3 → 1.00e-3 (1.7×, 1.8×); cubic m = 36 9.79e-9 → 1.78e-9, 5.53e-6 → 6.48e-7 (5.5×, 8.5×). 'ld' gives 1.3–4.8×. The pre-registered requirement (≥ 100×; kill if < 10× at both degrees) fails on every clustered set.
(b) **Vector channel (P2 killed).** rotπ/4: L(16), L(20), L(24) double 1.62e-9, 2.27e-6, 4.17e-3 → exact 1.15e-10, 1.20e-7, 2.37e-4 (14×, 19×, 18×); 'ld' 3.3–4.5×. Triangle: L(16) 4.88e-4 → 4.91e-3 (exact, 10× worse), 'ld' 5.19e-3; L(20) = 1 in all three. So the effect of removing one rounding source is set-dependent and not monotone.
(c) **Drift (P3 survives).** θ_LB at the last degree: rotπ/4 3.1e-4 / 3.2e-4 / 1.6e-4, triangle 7.8e-4 / 6.1e-4 / 3.3e-4 (double / exact / ld): changes < 10×.
(d) **Controls.** Chebyshev–Lobatto checkerboard and tensor 41² flat in all variants (≤ 4.1e-15, ≤ 1.9e-14). PRO-2D-J with exact dots on the cubic checkerboard: L(29) = 7.5e-7 (double 2.0e-7) — the R02 last-degree failure is not repaired.

Reading: on the clustered product-type checkerboards the closed loop of PD-T?…-115 is fed at comparable strength by the rounding of the stored vectors and of the vector operations, not specifically by the dot products; removing ρ leaves the loss within 1.3–8.5×. The hand-off speculation "compensated or extra-precision window dot products would shrink ρ, which drives the closed loop" is refuted in this scope.

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-210 (correctly rounded / extended-precision window dot products as a remedy for the coefficient channel, and as a channel separator).
Parameter range: Harris–Simanek checkerboards with gradings s|s|, s|s|², s|s|³ (m = 30) and s|s|² (m = 36), weights |1/ω′_X||1/ω′_Y|, n ≤ 35; controls as listed; one machine, NumPy 2.5.3, x87 long double. Not covered: storing vectors in extended precision (L1 PD-T?…-115 (c): a long-double run with long-double storage scales with u), compensated vector updates, MGS.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a)–(d) | MEASURED | `logs/r03_dots.raw.gz` |
| exact-dot implementation | checked against exact rational arithmetic on 3 random dot products of length 500 (difference 0) | R03 §2 |

Candidate / claim disposition: IDEA?…-210 REJECTED (failed: P1 on all four clustered sets, P2 on rotπ/4); P3 (drift insensitive to dot precision) survives.
Rejection reason: failed.

## Depends on

PD-T?…-115 (closed-loop reading, CONDITIONAL input), PD-T?…-202 part 5 / -205 (θ_LB).

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r03_dots.py > …/L2/logs/r03_dots.raw` (≈ 40 s). Independent rerun: none.

## Sources

None (L1 hand-off text only).

## Proof or evidence

Measured.

## Scope

Within the stated range, extra-precision dot products are a weak remedy (≤ 8.5×) for the coefficient channel and a moderate one (≈ 18×) for the rotπ/4 vector channel; they do nothing for the space channel.

## Open items

Extended-precision storage of the basis (expected to scale the loss with the storage precision, PD-T?…-115 (c)) at the cost of doubling memory traffic; whether any double-storage scheme removes the coefficient channel.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R03). Kill rules pre-registered 00:44:13 (candidates.md).
- 2026-11-01T01:28:43+01:00: (reconstruction 01 F6) title range corrected from "17–19×" to "14–19×" to match (b) (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
