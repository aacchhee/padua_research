# PD-N?bivariate-lanczos-claude-202 — PRO-2D with the rounding-only ω-trigger does not maintain semi-orthogonality on non-product measures: after reorthogonalization the commutator J-sources dominate

ID kind: PD-N.
Aliases: IDEA?…-208 killed; "rounding-only trigger fails under reorthogonalization"; commutator channel in the partial-reorthogonalization regime.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ ordering, two-pass window, partial reorthogonalization triggered when the sign-matched rounding-only estimate (E1D, IDEA?…-201) exceeds √u, against {l : |ω̃_l| > u^{3/4}} plus the window, next column likewise: L(n) > 10√u (pre-registered kill) on rotπ/4 (n = 24: 5.0e-7), triangle (n = 19–20: 2.4e-6), L-shape (n = 27–30: 6.5e-6), annulus (n = 25–30: 1.3e-4), cubic checkerboard (n = 29: 1.5e-7). With the J-rows measured exactly instead (PRO-2D-J, IDEA?…-209; written after this failure) the same runs stay at 7.6e-9, 4.3e-9, 1.5e-8, 9.8e-9 (rotπ/4, triangle, L-shape, annulus); the cubic checkerboard still fails at n = 29 (2.0e-7). In the plain run the same estimate had never underestimated by more than 3.9× (PD-T?…-203).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-208 (rounding-only ω-trigger for 2D partial reorthogonalization).
Parameter range: the 12 R01 benchmarks, M ≤ 3000, n ≤ 47, thresholds √u / u^{3/4}, sign-matched sources.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| failures | MEASURED | `logs/r02_pro.raw.gz`, `logs/r02_verdicts.txt` |
| explanation "commutator sources dominate after reorthogonalization" | MEASURED support only: measuring the J-rows removes 4 of 5 failures; R01 audit shows J-sources 10⁴–10¹⁰ × the rounding scale on these sets; PD-T?…-202 part 3 shows reorthogonalization does not reset the in-span commutator residual | not proved |

Candidate / claim disposition: IDEA?…-208 REJECTED (failed).
Rejection reason: failed.

## Depends on

PD-T?…-202, -203.

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r02_pro.py > …/L2/logs/r02_pro.raw`; `… --jmeasure > …/r02_proJ.raw`; verdicts `l2_r02_verdicts.py`.

## Sources

Simon 1984 §§5–6 (LIT?…-212) for the template; not a dependency.

## Proof or evidence

Measured.

## Scope

A tracking estimate validated on unreorthogonalized runs need not remain valid once reorthogonalization removes the dominant propagated part; for the 2D recurrence the residual part is the commutator channel. The cubic-checkerboard failure at its last degree (M − N_29 = 31) is unexplained.

## Open items

Cause of the cubic-checkerboard last-degree failure; a cheaper commutator model than measuring the n J-rows.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02).
