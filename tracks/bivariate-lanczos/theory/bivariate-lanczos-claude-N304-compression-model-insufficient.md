# PD-N?bivariate-lanczos-claude-304 — The compression (POVM/dilation) backward model does not imply exact sections

Final ID: **PD-N023** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: route (ii) failure; compression ⇏ section; IDEA?bivariate-lanczos-claude-303.
Split from: none (created per finding L10 of L3-reconstruction-01).
Split into: none.

## Statement

There are square-case section data — Padua n = 3, Ĥ = Φ(L_μ + E) with E(p*) < 0 and ‖E‖ ≤ ε ≤ ε_1 — that are compressions of commuting symmetric pairs with joint spectrum in K_δ for every δ > 0 once ε < ρ(δ)/L_Φ (PD-T?…-308; ρ(δ) bounds ‖Ĥ − H‖ in a matrix norm and ‖Φ(L_μ + E) − Φ(L_μ)‖ ≤ L_Φ‖E‖ with L_Φ the local Lipschitz constant of Φ, PD-T?…-301(c)), but are not the exact sections of any positive measure supported in K_δ for δ ≤ δ_0 (PD-N?…-301). Hence the existence of a compression/dilation backward model does not imply the existence of an exact-section backward model in reading (E) (perturbations given as data); nothing is claimed about the finite-precision reading (G).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?bivariate-lanczos-claude-303 (route (ii) of L3-Q1: decide L3-Q1 via the minimal matrix convex set / POVM dilation over K_δ).
Parameter range: square case, perturbative regime; witnessed at Padua n = 3 (and, under Padua unisolvence, n ≥ 4 via PD-N?…-303, PROVED).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| compression model exists for small perturbations, every δ > 0 | PROVED | PD-T?…-308 |
| exact-section model fails, δ ≤ δ_0 | PROVED | PD-N?…-301 (independent rerun done) |

Candidate / claim disposition: REJECTED (route (ii) as a decision method for L3-Q1). Rejection reason: failed.

## Depends on / Checks / Sources / Proof

PD-T?…-308, PD-N?…-301; combine both with ε < min(ρ(δ)/L_Φ, ε_1).

## Scope / Open items

Route (ii) remains a valid weaker backward statement (compression), recorded as PD-T?…-308.

## History

- 2026-10-31T23:55:17+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer: created per finding L10 of L3-reconstruction-01.
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): finding L5 (hypothesis ε < ρ(δ)/L_Φ) of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «for every δ > 0 once ε < ρ(δ) (PD-T?…-308)»; «combine both with ε < min(ρ(δ), ε_1).».
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): consolidated item 4 of Codex audit-01 (reading (E) only; audit-01.md, candidate 5ccfac2) and stale 'conditionally' label (LC-L1 spirit). Statement content and status unchanged. Original wording of the replaced passages: «Hence the existence of a compression/dilation backward model does not imply the existence of an exact-section (Greenbaum-type) backward model.»; «witnessed at Padua n = 3 (and n ≥ 4 conditionally via PD-N?…-303).».
