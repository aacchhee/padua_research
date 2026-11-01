# PD-N?bivariate-lanczos-claude-203 — No tested one-relation selection rule keeps the computed spans within √u of S_n on all non-product benchmarks under full reorthogonalization (dev, mirror, alt, adapt)

ID kind: PD-N.
Aliases: IDEA?…-207 killed for every rule; "adaptive selection is not uniformly safe"; rotπ/4 counterexample for adapt.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] With CGS2 against all previous columns and block window, the reference-free drift bound θ_LB exceeds √u = 1.05e-8 (or the reference drift exceeds √u with reference bound < 1e-11) on: dev — rot0.3, rotπ/4, triangle, L-shape, annulus; mirror — rot0.3, rotπ/4, triangle, L-shape; alt — rotπ/4 (drift 2.1e-8), triangle (drift 7.6e-8), L-shape, annulus (θ_LB 1.1e-5, 1.3e-7); adapt — rotπ/4 (θ_LB 2.1e-7, drift 1.9e-6 at n = 24; first above √u at n = 22).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-207 "selection rule S keeps the spans near S_n under full reorthogonalization", S ∈ {dev, mirror, alt, adapt}.
Parameter range: the six non-product benchmarks of PD-T?…-206 (M = 1681–3000), n ≤ 30, double precision, block window. Not covered: other rules, larger M, other windows.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| per-rule failures | MEASURED | `logs/r02_verdicts.txt`, `logs/r02_selection.raw.gz` |

Candidate / claim disposition: IDEA?…-207 REJECTED for each of the four rules (failed, scope above).
Rejection reason: failed.

## Depends on

PD-T?…-208 (bound; formerly cited as PD-T?…-205 part 4), PD-T?…-206 (measurements).

## Checks

As PD-T?…-206 (including Codex audit-01's partial rerun on rotπ/4, the triangle and the cubic checkerboard).

## Sources

None beyond PD-T?…-206.

## Proof or evidence

Measured.

## Scope

Does not refute that adaptive selection is much better than BJ (it is, by 7–10 decades on four sets); it refutes uniform safety of the tested rules on the tested sets. It does not quantify over all possible one-relation selections (audit-01); in particular the adaptive exceptions and the two-relation control of PD-T?…-206 stand.

## Open items

As PD-T?…-206.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02).
