# PD-N?bivariate-lanczos-claude-202 — PRO-2D with the rounding-only ω-trigger does not maintain semi-orthogonality on non-product measures: after reorthogonalization the commutator J-sources dominate

Final ID: **PD-N014** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: IDEA?…-208 killed; "rounding-only trigger fails under reorthogonalization"; commutator channel in the partial-reorthogonalization regime.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ ordering, two-pass window, partial reorthogonalization triggered when the sign-matched rounding-only estimate (E1D, IDEA?…-201) exceeds √u, against {l : |ω̃_l| > u^{3/4}} plus the window, next column likewise: L(n) > 10√u (pre-registered kill) on rotπ/4 (n = 24: 5.0e-7), triangle (n = 19–20: 2.4e-6), L-shape (n = 27–30: 6.5e-6), annulus (n = 25–30: 1.3e-4), cubic checkerboard (n = 29: 1.5e-7). With the J-rows measured exactly instead (PRO-2D-J, IDEA?…-209; written after this failure) the same runs stay at 7.6e-9, 4.3e-9, 1.5e-8, 9.8e-9 (rotπ/4, triangle, L-shape, annulus); the cubic checkerboard still fails at n = 29 (2.0e-7). [Audit-01, L2-F3: "stay" refers to the registered kill threshold 10√u; the L-shape value 1.48e-8 = 1.41√u exceeds the campaign's strict semi-orthogonality level √u at n = 29–30 (PD-T?…-207 (a)).] In the plain run the same estimate had never underestimated by more than 3.9× (PD-T?…-203).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-208 (rounding-only ω-trigger for 2D partial reorthogonalization).
Parameter range: the 12 R01 benchmarks, M ≤ 3000, n ≤ 47, thresholds √u / u^{3/4}, sign-matched sources.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| failures | MEASURED | `logs/r02_pro.raw.gz`, `logs/r02_verdicts.txt` |
| explanation "commutator sources dominate after reorthogonalization" | MEASURED support only: measuring the J-rows removes 4 of 5 failures; R01 audit shows J-sources 10⁴–10¹⁰ × the rounding scale on these sets; PD-T?…-202 part 3 shows that the in-span commutator residual's recursion contains no reset term (reorthogonalization enters only as further coefficients; it does not show that the residual stays large, audit-01 L2-F1) | not proved |

Candidate / claim disposition: IDEA?…-208 REJECTED (failed).
Rejection reason: failed.

## Depends on

PD-T?…-202, -203.

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r02_pro.py > …/L2/logs/r02_pro.raw`; `… --jmeasure > …/r02_proJ.raw`; verdicts `l2_r02_verdicts.py`. Independent rerun (Codex audit-01, `topics/bivariate-lanczos-20261031/audit-01/L2/pro-rerun.log`): rounding-only PRO fails at rotπ/4 degree 24 and triangle degrees 19–20, max losses 5.0311e-7 and 2.4401e-6.

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
- 2026-11-01T08:32:22+01:00: (Codex audit-01, findings **L2-F1** and **L2-F3**, propagation; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`) Status-table wording: original "PD-T?…-202 part 3 shows reorthogonalization does not reset the in-span commutator residual" → the recursion contains no reset term (no lower bound implied). Statement: bracketed note that "stay" refers to the registered 10√u threshold and that the L-shape exceeds the strict √u level (original sentence kept). Checks: audit-01 independent rerun recorded (original Checks had no rerun line). Verdicts and status MEASURED unchanged.
