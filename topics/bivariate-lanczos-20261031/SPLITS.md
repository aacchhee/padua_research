# Provisional splits (to be moved to ID_CROSSWALK.md at PR preparation)

Created by the orchestrator for the response to Codex audit-01. Each direction developer appends rows only in its own section.

## L1/L4

| Original ID / file | Split result ID / file | Relation / exact scope | Reason / finding |
|---|---|---|---|
| PD-T?bivariate-lanczos-claude-105 / `tracks/bivariate-lanczos/theory/product-measure-propagator-factorization.md` (PROVED; stays PROVED: parts 1–3, exact product structure and factorisation of the idealised propagator) | PD-T?bivariate-lanczos-claude-116 / `tracks/bivariate-lanczos/theory/product-measure-computed-propagator-transfer-conditional.md` (CONDITIONAL) | Former part 2′ and its Assumptions sentence: transfer of the part-2 factorisation to the computed propagator L̂(z) of a floating-point run, to first order in δ = ‖L̂ − L‖_∞, under the named hypothesis H_δ (κ(z_i)δ ≪ 1). Contains a minor routine PROVED perturbation step (Neumann bounds, κ ≤ B) | Codex audit-01 L1-foundations S1; consolidated item 5 |
| PD-T?bivariate-lanczos-claude-114 / `tracks/bivariate-lanczos/theory/first-order-coefficient-channel-gains-product-type.md` (was "parts 1–4 PROVED; part 5 MEASURED"; now PROVED: parts 1–4, exact first-order Gram derivative at a product-type point) | PD-T?bivariate-lanczos-claude-117 / `tracks/bivariate-lanczos/theory/coefficient-channel-gain-census-checkerboards-measured.md` (MEASURED) | Former part 5 (gain census and first-order predictions on two m = 30 checkerboards, dev rule, block window, degrees ≤ 20), its closing reading, and the title clause "the clustered-checkerboard loss is this first-order channel". The formula check stays in -114 as a verification record | Codex audit-01 L1-later LL-M2; protocol P1; consolidated item 5 |

## L2

| Original ID / file | Split result ID / file | Relation / exact scope | Reason / finding |
|---|---|---|---|

## L3

| Original ID / file | Split result ID / file | Relation / exact scope | Reason / finding |
|---|---|---|---|
| PD-T?bivariate-lanczos-claude-304 (`tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-304-square-case-commutator-bounds.md`), part (c), second clause: «when the 3N_n jet conditions are independent (…) S_1 ≅ (V*/T)* and κ is, to first order, the S_1*-component of the perturbation» | PD-T?bivariate-lanczos-claude-316 (`…/bivariate-lanczos-claude-316-square-case-first-order-commutator-isomorphism.md`) | OPEN general target: the induced map V*/T → Skew_{n+1} is an isomorphism (square case, independent jets, all n). 304 keeps (a), (b) and the factorisation part of (c), PROVED | LF-M2 (audit-01/L3-framework.md) |
| PD-T?…-304, status row «(c) the induced map V*/T → Skew_{n+1} is an isomorphism … MEASURED … rank n(n+1)/2 for Padua n = 2, 3» | PD-T?bivariate-lanczos-claude-317 (`…/bivariate-lanczos-claude-317-first-order-commutator-rank-measurements.md`) | MEASURED: numerical rank n(n+1)/2 of d(κ∘Φ) at Padua n = 1..4, equispaced n = 3, random n = 3 (developer) and Padua n = 2, 3 (reviewer) | LF-M2 |
| — (new supporting result, not a split) | PD-T?bivariate-lanczos-claude-318 (`…/bivariate-lanczos-claude-318-first-order-commutator-formula.md`) | PROVED: d(κ∘Φ)(E)_ab = E(s_ab), rank = dim{p_C : C ⊥ Hankel}; 316 ⟺ the open conjunct of 309 | LF-M2 |
| PD-T?bivariate-lanczos-claude-302 (`…/bivariate-lanczos-claude-302-backward-reduction-moment-cone.md`), pre-audit (b): «the same threshold, with ε replaced by (1−θ)ε, governs representation up to a residual θε» with Definitions «L̂ := Φ^{-1}(Ĥ) normalised by L̂(1) = L_μ(1) … (c = 1)» | PD-T?…-302 (same ID; corrected (b1)–(b4)) and PD-N?bivariate-lanczos-claude-309 (`…/bivariate-lanczos-claude-N309-normalized-residual-threshold-refuted.md`) | corrected in place with conventions (R1)–(R3); the factor-1 normalised variant REJECTED: refuted (N309 PROVED: explicit n = 1 instance, all δ ∈ [0, 10⁻⁸]) | LF-M1 (audit-01/L3-framework.md) |
| PD-T?bivariate-lanczos-claude-313, Open items «So δ_0(n) → 0 with n (…): the obstruction holds for each n, with no radius uniform in n» and PD-N?bivariate-lanczos-claude-303, Statement «The radius δ_0(n) shrinks with n (…), so the obstruction is per degree, not uniform in n» | PD-T?bivariate-lanczos-claude-319 (`…/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`) | OPEN: (U1) does the positivity radius ρ_n of P_n tend to 0? (U2) is there an obstruction radius uniform in n? Old wording withdrawn; 313 and N303 keep their PROVED per-degree statements | LC-M1 (audit-01/L3-certificates.md) |
