# PD-N?bivariate-lanczos-claude-205 — Componentwise in-window source scaling (E3) does not repair the ω-estimate's overestimate of the clustered-checkerboard coefficient channel

ID kind: PD-N.
Aliases: IDEA?…-205 failed; E3; abs-dot source scale.
Split from: PD-T?…-203 (b) (the failure was previously recorded only there; split out after reconstruction 01, finding F3).
Split into: none.

## Statement

[FP, MEASURED] Replacing the in-window source scale u‖(h, β)‖₂ of the ω-estimate E1 (PD-T?…-203) by u·|q̂_l|ᵀ|Aq̂_p| (E3) leaves the overestimate on the cubic-clustered Harris–Simanek checkerboard (m = 30) at O = max_D E/L = 1.79·10⁵ (E1: 2.43·10⁵). The pre-registered improvement criterion (O(cb_cubic) reduced ≥ 100×, no other O rising > 3×) fails; the frozen kill rule (L/E > 10) does not fire (max L/E = 1.44).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-205 (componentwise in-window rounding scale as a coefficient-channel-aware source model).
Parameter range: the 12 R01 benchmarks, plain BJ block window CGS, 5 seeds, u = 2⁻⁵³. Not covered: componentwise out-of-window scales, closed-loop source models.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| failure of the improvement aim | MEASURED | `directions/L2/logs/r01_omega_e3.raw.gz`, `r01_verdicts.txt` |

Candidate / claim disposition: IDEA?…-205 REJECTED. Rejection reason: failed.

## Depends on

PD-T?…-203.

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r01_omega.py --e3`. Reconstruction 01 did not rerun E3.

## Sources

None.

## Proof or evidence

Measured. Reading: the overestimate is the open-loop random-source effect on the off-pattern gains (cf. L1 PD-N?…-104), not the in-window scale.

## Scope

As stated; the estimate remains safe (no underestimate), only its cost-relevant overestimate is unrepaired.

## Open items

A closed-loop source model (PD-T?…-115).

## History

- 2026-11-01T01:29:29+01:00: created from PD-T?…-203 (b) and candidates.md (R01 dispositions) in response to reconstruction 01 finding F3 (Claude Opus 5.5, xhigh; L2 developer).
