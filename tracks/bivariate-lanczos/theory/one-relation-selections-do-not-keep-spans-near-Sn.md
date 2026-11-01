# PD-N?bivariate-lanczos-claude-203 — No tested one-relation selection rule keeps the computed spans within √u of S_n on all non-product benchmarks under full reorthogonalization (dev, mirror, alt, adapt)

Final ID: **PD-N015** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

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

## Independent public-code extension (MEASURED)

PD-T146 executes actual polyrat 0.2.2 numerical source at commit6903d7af9995c9d88e661fb229626696e00fdfba on the frozen suite. Upstream input [y,x] matches campaign dev including column order; default [x,y] is mirror with reversed within-degree order and is not numerically equivalent to forward mirror. Separate root execution reproduces the rotated-square n24 gap0.004105 and triangle n20 gap0.010164. The post-hoc worst-polynomial training residuals equal those gaps by construction; the worst-polynomial off-sample error depends on the test distribution (1.0e-3 to 1.5e-2 on rotated square). The fixed ridge target exp(x+y) is fit near machine precision on the tested samples. Ill-conditioned/rank-deficient references elsewhere do not certify span drift. This is additional scoped measurement, not an upgrade of this negative result or a proof of every-rule failure. The scalar-operation and aggregate sensitivity statements in the new E1 records remain separately scoped.

## Open items

As PD-T?…-206.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02).
- 2026-11-01T08:32:22+01:00: (Codex audit-01: L2-F4 reference to the split drift bound; claim-coverage note "does not quantify over all possible selections"; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`) Depends on: original "PD-T?…-205 part 4 (bound), PD-T?…-206 (measurements)." → PD-T?…-208. Checks: original "As PD-T?…-206." extended. Scope sentence added. Statement, disposition and status MEASURED unchanged.
