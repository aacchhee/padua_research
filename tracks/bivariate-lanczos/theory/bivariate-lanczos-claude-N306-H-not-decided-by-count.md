# PD-N?bivariate-lanczos-claude-306 — MEASURED: condition (H) is not decided by the square count / checkerboard structure alone

ID kind: PD-N.
Aliases: IDEA?bivariate-lanczos-claude-311; node-distribution dependence of (H).
Split from: none (created per finding L10 of L3-reconstruction-01).
Split into: none.

## Statement

The hypothesis "all ordered square Harris–Simanek checkerboards behave like Padua ((H) fails from n = 3)" is false within the measured scope: equispaced checkerboards satisfy (H) for n = 3, 4, 5 (floating SDP margins 1.8e-3, 1.3e-4, 4.8e-6; exactly certified for n ≤ 7 in PD-T?…-310), graded checkerboards for n = 3, 4, while the Chebyshev–Lobatto checkerboard (Padua) fails from n = 3.

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-311. Parameter range: ordered checkerboards (Chebyshev–Lobatto, equispaced, graded, two sorted-uniform draws), n ≤ 6 floating; equispaced n ≤ 7 exact (CONDITIONAL on rerun, PD-T?…-310).

## Status by part

Overall status: MEASURED (the exact equispaced certificates of PD-T?…-310 would make the refutation PROVED once rerun).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (H) for equispaced n = 3..5 | MEASURED (floating); exact certificates CONDITIONAL in 310 | logs `hs_checkerboard_condition.log`, `exact_checkerboard_equi.log` |

Candidate / claim disposition: REJECTED. Rejection reason: refuted (within scope).

## History

- 2026-10-31T23:55:17+01:00, L3 developer: created per finding L10 of L3-reconstruction-01.
