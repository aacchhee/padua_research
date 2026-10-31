# PD-T?bivariate-lanczos-claude-311 — MEASURED: super-geometric decay of the certified (H) margins on equispaced checkerboards

ID kind: PD-T.
Aliases: margin decay; constant collapse in the √ε regime; R04.
Split from: none (measured companion of PD-T?bivariate-lanczos-claude-310).
Split into: none.

## Statement

MEASURED (values read off exact certificates, plus floating proposals): for the equispaced checkerboards S_0(n) of PD-T?…-310 with the SDP normalisation Σ_i tr A_i = 1, the exact certificates found have min_i det(A_i)/tr(A_i) = 4.3e-2, 1.0e-2, 9.1e-4, 6.6e-5, 2.4e-6, 2.3e-8, 3.4e-11 (n = 1..7), against floating SDP optima t_D = 8.6e-2, 2.0e-2, 1.8e-3, 1.3e-4, 4.8e-6, 4.6e-8, 4.5e-11 (double precision; the high-precision optimum at n = 7 is 6.78e-11, L3-reconstruction-02, so the double value underestimates it). At n = 8 the double-precision optimum −1.3e-12 had the wrong sign; the reviewer's high-precision optimum is t_D = 4.12e-15 and (H) holds at n = 8 (reviewer computation, see PD-T?…-310). With the high-precision values the ratios t_D(n)/t_D(n+1) are 4.28, 10.97, 13.78, 27.4, 105, 680, 16 400 (n = 1→8) — super-geometric decay on 8 values. The "certified margin" min det/tr is ≈ t_D/2 by construction (for A_i ≈ tI, det/tr = t/2) and is not a separate observation.

## Definitions / Assumptions

Floating point for t_D; exact rational values for the certified margins (reported as floats). The margin is a property of the normalised SDP, not directly the constant c of PD-T?…-303(d); the relation is qualitative (c ≥ const·κ, κ related to the dual margin by conic duality — not made explicit).

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| margin values n = 1..7 | MEASURED | logs as in PD-T?…-310 |
| "super-geometric decay" | MEASURED (pattern over 7 values only) | — |

## Depends on / Checks / Sources

As PD-T?…-310 (same runs). No independent rerun yet.

## Proof or evidence

Measurements only.

## Scope

Equispaced checkerboards n ≤ 8.

## Open items

Explicit relation between the dual margin and c in r(δ) ≥ cδ²; asymptotics in n.

## History

2026-10-31T23:15+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R04.
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): finding L4 (t_D(7), ratio 680, margin ≈ t_D/2, n = 8 resolved by the reviewer) of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «against floating SDP optima t_D = 8.6e-2, 2.0e-2, 1.8e-3, 1.3e-4, 4.8e-6, 4.6e-8, 4.5e-11; at n = 8 the floating optimum is −1.3e-12 (unresolved). The ratios t_D(n)/t_D(n+1) are 4.3, 11, 14, 27, 105, 1030 — faster than geometric decay.».
