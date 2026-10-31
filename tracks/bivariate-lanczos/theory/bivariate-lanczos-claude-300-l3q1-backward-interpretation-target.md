# PD-T?bivariate-lanczos-claude-300 — L3-Q1 target: Greenbaum-type backward interpretation of computed degree-n sections

ID kind: PD-T.
Aliases: L3-Q1; IDEA?bivariate-lanczos-claude-031 (seed); nearby representing measure; commuting backward model; backward interpretation.
Split from: none.
Split into: PD-T?bivariate-lanczos-claude-301 (truncated Favard), 302 (precise form / reduction), 303 (rate theorem), 304 (square-case commutator bounds), 305 (n = 1 √ε), 306 (Padua n = 2 √ε, CONDITIONAL), 307 (MEASURED survey), 308 (compression model); PD-N?bivariate-lanczos-claude-301 (Padua n = 3 obstruction, CONDITIONAL), PD-N?bivariate-lanczos-claude-302 (no δ = O(ε) in the square case). Mapping to be recorded in ID_CROSSWALK.md at PR preparation.

## Statement

Frozen wording (plan.md §L3-Q1, not reworded): "Given [IDEALIZED: perturbations given as data] computed sections (Ĥ_x, Ĥ_y) of degree n that satisfy the exact structural zero pattern and the recurrence relations up to O(ε), does there exist a positive discrete measure μ′ supported within distance δ of the original nodes whose exact degree-n sections equal (Ĥ_x, Ĥ_y) up to O(ε) (a Greenbaum-type backward interpretation)? Decide, separately for the overdetermined case (M ≥ dim Π_{2n+1}, generic nodes) and the square case M = N_n (Padua), either an existence statement with an explicit δ(ε) or an explicit obstruction family."

Precise readings (PD-T?…-302): (L) literal, perturbative — trivial (μ′ = μ, δ = 0); (E) exact representation of consistent ε-perturbed data (residual strictly smaller than the perturbation) — decided case by case below; (G) Greenbaum regime — data far from Φ(μ) but satisfying the local relations of the recurrence up to O(ε) (loss of orthogonality) — OPEN.

## Definitions / Assumptions

As in PD-T?…-301/302/303.

## Status by part

Overall status: OPEN (reading (G) open; reading (E) decided in the cases below with mixed statuses, so not PARTIAL).

| Part of the target | Status | Result / file |
|---|---|---|
| (L) literal perturbative reading | PROVED (routine) | trivial with δ = 0; 302(c) |
| (E) overdetermined, M ≥ dim Π_{2n+1}, nodes Π_{2n+1}-unisolvent | PROVED | existence with δ = 0 (same nodes, weights w + O(ε)) for ε < r(0) ≥ w_min σ_1; 303(a) |
| (E) intermediate M with S_1 = {0} | PROVED | δ(ε) ≍ ε; 303(b) |
| (E) square case, all Π_n-unisolvent sets, n ≥ 1: δ = O(ε) impossible, δ ≳ √ε necessary; δ ≥ c√‖κ(Ĥ)‖ | PROVED | PD-N?…-302, 303(c), 304(a) |
| (E) square case with exactly commuting data | PROVED | δ ≤ ‖ΔH‖, N_n atoms; 304(b) |
| (E) square, n = 1 (any triangle incl. Padua n = 1) | PROVED | δ ≍ √ε; 305 |
| (E) Padua n = 2 | CONDITIONAL (independent rerun of exact checker) | δ ≍ √ε; 306 |
| (E) Padua n = 3 | CONDITIONAL (independent rerun of exact checker) | obstruction: no δ(ε) → 0; explicit family E = −ε ev_ζ; PD-N?…-301 |
| (E) Padua n = 4..7; random square sets | MEASURED | robust failure of (H) numerically (obstruction regime) for Padua 4..7; random sets: (H) n ≤ 2, mixed n = 3, failure n ≥ 4; 307 |
| (G) Greenbaum (loss-of-orthogonality) regime, both cases | OPEN | needs the L1 local relations; R01 next question |

## Depends on

The split-off files listed above.

## Checks

See the split-off files and `topics/bivariate-lanczos-20261031/directions/L3/R01.md`.

## Sources

`xu-siam-1994` (context for the cubature link), arXiv:1703.01497 (context for boundary points of moment cones; summary only).

## Proof or evidence

In the split-off files.

## Scope

Cubature link (recorded as required by plan.md): by PD-T?…-302(a), reading (E) is exactly the existence of a positive cubature formula of degree 2n+1 for the perturbed functional L̂ with all nodes in K_δ. Exactly commuting square data (κ = 0) ⟺ L̂ has an N_n-node positive cubature of degree 2n+1 (odd-degree "Gaussian" type, the Mysovskikh situation: degree-(n+1) orthogonal polynomials with N_n common zeros), and then the nodes are the joint eigenvalues (304(b)), the discrete analogue of Xu's joint-eigenvalue characterisation (xu-siam-1994 Thm 3.1/4.1, which concerns even degree 2n−2 with dim Π_{n−1} nodes and a modified last block). The obstruction p* of PD-N?…-301 is a classical dual certificate for non-existence of a localized positive cubature (a polynomial nonnegative on the node region whose functional value is negative).

## Open items

(1) Reading (G): characterize the reconstructed functional L̂ of a long finite-precision run and decide L̂ ∈ C(K_δ) + B(0, O(u)). (2) Exact certificates for Padua n ≥ 4. (3) Structural reason for the n = 2 → 3 transition. (4) Degenerate subcase of 303. (5) Constants.

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01 with the split listed above. The frozen wording is preserved verbatim; the readings (L)/(E)/(G) are interpretations recorded in 302 with reasons, not a narrowing of the target ((G) stays OPEN).
