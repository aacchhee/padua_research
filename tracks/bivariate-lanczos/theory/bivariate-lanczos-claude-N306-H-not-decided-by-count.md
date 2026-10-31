# PD-N?bivariate-lanczos-claude-306 — MEASURED: condition (H) is not decided by the square count / checkerboard structure alone

ID kind: PD-N.
Aliases: IDEA?bivariate-lanczos-claude-311; node-distribution dependence of (H).
Split from: none (created per finding L10 of L3-reconstruction-01).
Split into: none.

## Statement

The hypothesis "all ordered square Harris–Simanek checkerboards behave like Padua ((H) fails from n = 3)" is false: the ordered equispaced checkerboard S_0(3) satisfies (H) (exact certificate, PD-T?…-310, PROVED with an independent exact rerun), while the Chebyshev–Lobatto checkerboard of the same size (Padua n = 3) fails it robustly (PD-N?…-301, PROVED). The survey parts (graded checkerboards, sorted-uniform draws; MEASURED) are evidence recorded in PD-T?…-307 item 6 and are not part of this statement.

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-311. Parameter range: ordered checkerboards (Chebyshev–Lobatto, equispaced, graded, two sorted-uniform draws), n ≤ 6 floating; equispaced n ≤ 7 exact (CONDITIONAL on rerun, PD-T?…-310).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (H) for equispaced n = 3 (refutation) | PROVED | PD-T?…-310 (developer exact certificate; independent exact rerun L3-reconstruction-02) |
| contrast: Padua n = 3 fails (H) robustly | PROVED | PD-N?…-301 |
| survey (graded, sorted-uniform) | MEASURED, outside this statement | PD-T?…-307 item 6 |

Candidate / claim disposition: REJECTED. Rejection reason: refuted (within scope).

## History

- 2026-10-31T23:55:17+01:00, L3 developer: created per finding L10 of L3-reconstruction-01.
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): refutation part upgraded to PROVED, survey parts moved out of the statement (review recommendation for N306) of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «The hypothesis "all ordered square Harris–Simanek checkerboards behave like Padua ((H) fails from n = 3)" is false within the measured scope: equispaced checkerboards satisfy (H) for n = 3, 4, 5 (floating SDP margins 1.8e-3, 1.3e-4, 4.8e-6; exactly certified f …»; «Overall status: MEASURED (the exact equispaced certificates of PD-T?…-310 would make the refutation PROVED once rerun).»; «| (H) for equispaced n = 3..5 | MEASURED (floating); exact certificates CONDITIONAL in 310 | logs `hs_checkerboard_condition.log`, `exact_checkerboard_equi.log` |».
