# PD-N?bivariate-lanczos-claude-508 — First-admissible threshold deferral of nodes (online pivot detector, FIFO) does not give order-independent accuracy in point-by-point Givens updating

Final ID: **PD-N031** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: prefix-aware deferral; FIFO deferral; IDEA?bivariate-lanczos-claude-504 (c) and 504c'.
Split from: PD-N?bivariate-lanczos-claude-506 context (finding L9 of reconstruction 01).
Split into: none.

## Statement

[FP, MEASURED; scope = Parameter range below.] Let a node stream be processed by 'scheme' Givens updating with the following deferral rule: before committing a node, insert it tentatively; if the minimum over the monomials j of the absolute primary pivot of the resulting state is below tau (the online detector of PD-T?bivariate-lanczos-claude-503 B), put the node back in a FIFO buffer and try the next one; commit the first node that passes, with a forced insertion if the buffer stalls. Then, on Padua n = 20 and 30 (cubature and U(0.1,1) weights), tau = 1e-8 and tau = 1e-3:

(D1) On the numerically unisolvent orders rand1-3 and gepp (floating-point σ_min estimates of PD-T?bivariate-lanczos-claude-503, not certificates) the rule equals 'scheme' (tau = 1e-8: no deferrals, identical errors) or is within 1.4 times it (tau = 1e-3: 0-29 deferrals; e.g. n = 30 rand3 U weights 1.0e-13 vs 7.5e-14).

(D2) On the structured streams (given, sortx) it is far worse than 'scheme' and than the best order (gepp-scheme 1.9e-14 at n = 20, 3.8e-14 at n = 30): tau = 1e-8: n = 20 3.1e-9 (given), 1.5e-8 (sortx) (cubature), 5.5e-9, 6.3e-9 (U); n = 30 5.6e-5, 2.9e-8 (cubature), 1.4e-5, 1.4e-8 (U); tau = 1e-3: n = 20 5.5e-10, 2.0e-9, 8.8e-10, 5.0e-9; n = 30 1.5e-3, 1.3e-1, 7.8e-4, 8.8e-4. The number of deferral events is 9 000-79 000 and forced insertions occur (0-10 per run). 'scheme' on the same streams is 1.0e-14..2.6e-14.

Hence the rule does not achieve order independence of the accuracy; it makes the structured streams 3-10 orders of magnitude worse than 'scheme' on the same stream. Observed mechanism (consistent with the data, not proved): accepting the first node that passes a threshold does not control the conditioning of the accepted prefix sequence (FIFO takes an admissible but badly conditioned node), and the detector threshold is crossed repeatedly (thousands of deferrals) with forced insertions at stalls.

## Definitions

`defer` (tau = 1e-8) and `defer3` (tau = 1e-3, post-hoc variant, kill test written before it was run, candidates.md 504c'): `exp_r03.py` with env `L5_TAUS`. Errors as in PD-T?bivariate-lanczos-claude-502.

## Assumptions

IEEE double, real nodes, 'scheme' base rule, detector threshold on the min primary pivot, FIFO buffer.

## Status by part

Overall status: MEASURED (the negative statement). Candidate / claim disposition: REJECTED: failed (the rules do not achieve order-independent accuracy in the scope below).

| Mathematical part | Status | Evidence |
|---|---|---|
| D1, D2 | MEASURED | `logs/r03_rules.jsonl` (tau 1e-8), `logs/r03_defer3.jsonl`, `r03_defer3.log` (tau 1e-3) |

## Negative-result scope

Attempted mechanism: IDEA?bivariate-lanczos-claude-504 (c), 504c'. Parameter range: Padua n = 20, 30, tau in {1e-8, 1e-3}, FIFO buffer, orders given, sortx, rand1-3, gepp, both weights. Not covered: other tau, window-based or best-pivot selection (the windowed best-pivot variant 504c'' was **not killed** at n = 20, 30 but gave no gain over 'scheme', an IDEA disposition: no PD-N), larger n.

## Depends on

PD-T?bivariate-lanczos-claude-503 (B, the detector; MEASURED).

## Checks

`L5_TAUS=1e-3 python3 -I exp_r03.py` and the default run, see R03.md section 5. Independent rerun: none.

## Sources

None.

## Proof or evidence

Measured; see Checks.

## Scope

Exactly the range above. Does not show that no deferral strategy can work.

## Open items

n >= 40; a deferral that selects by the conditioning of the prefix rather than by a pivot threshold (the windowed best-pivot variant is the only one tried).

## History

2026-10-31T23:00Z, Claude Sonnet 5.5 (high), created in response to L5 reconstruction 01 finding L9 (AC's L5 decision: a separate evidenced mechanism failure gets its own PD-N).

2026-11-01T08:22:31+01:00, Claude Sonnet 5.5 (high), response to Codex audit-01 (L5) finding **M2** (terminology only): "(D1) On the unisolvent orders rand1-3 and gepp" now say "numerically unisolvent" (floating-point σ_min estimates of PD-T?bivariate-lanczos-claude-503, not exact or interval certificates). No number, scope, status (MEASURED) or disposition changed; audit-01 accepts this record as an eligible scoped negative statement.
