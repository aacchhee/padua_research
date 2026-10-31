# PD-T?bivariate-lanczos-claude-305 — n = 1 square case (any three non-collinear nodes): condition (H) holds, δ*(ε) ≍ √ε

ID kind: PD-T.
Aliases: triangle cubic; Padua n = 1; n = 1 square case √ε law.
Split from: none (case of the target PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

Let n = 1, M = N_1 = 3, nodes v_1, v_2, v_3 non-collinear, weights w_i > 0. Then S_1 = span{ℓ_{12} ℓ_{13} ℓ_{23}} (ℓ_{ij} an affine function vanishing on the line v_i v_j), every nonzero element of S_1 has an indefinite Hessian at every node, so (H) holds, and by PD-T?…-303(c)(d): c δ² ≤ r(δ) ≤ C δ², i.e. every consistent ε-perturbation of the degree-1 sections is the exact section pair of a positive measure supported within C√ε of the nodes, and some ε-perturbations need support spread ≥ c√ε. This includes Padua n = 1 ({(1,1), (1,−1), (−1,0)}).

## Definitions / Assumptions

As in PD-T?…-303; [EXACT]; [IDEALIZED: perturbations given as data].

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| S_1 = span{ℓ_12 ℓ_13 ℓ_23} | PROVED | Bézout argument below |
| indefinite Hessians ⇒ (H) ⇒ δ* ≍ √ε | PROVED | below + PD-T?…-303 |

## Depends on

PD-T?…-303 (c), (d).

## Checks

Exact certificate for Padua n = 1 also produced by `exact_certificates.py` (log `directions/L3/logs/exact_certificates.log`: dim S1 = 1, Hessian map injective, dual PD certificate PASS). MEASURED illustration: LP with z* = node_0 + 0.3(cos 1, sin 1): δ_min/√ε = 0.2124, 0.1929, 0.1908, 0.1907, 0.1907 for ε = 1e-2..1e-6 (`lp_rate.py 1 bisect 0.3`, log `lp_rate_n1_r0.3.log`).

## Sources

Bézout's theorem for a line and a cubic (textbook).

## Proof or evidence

Let p ∈ Π_3 be singular (value and gradient zero) at v_1, v_2, v_3. Restricted to the line v_1v_2 (parametrised affinely), p is a univariate polynomial of degree ≤ 3 with double roots at two points, hence identically zero; so p = ℓ_{12} q with q ∈ Π_2. At v_3 ∉ line, ∇p = ℓ_{12}(v_3)∇q(v_3) + q(v_3)∇ℓ_{12} and p(v_3) = ℓ_{12}(v_3) q(v_3) = 0 give q(v_3) = 0, ∇q(v_3) = 0. At v_1: ∇p(v_1) = q(v_1)∇ℓ_{12} = 0 gives q(v_1) = 0; similarly q(v_2) = 0. Restrict q to the line v_3v_1: degree ≤ 2, double root at v_3 and a root at v_1 ≠ v_3, hence zero; so q = ℓ_{13} ℓ′ with ℓ′ affine; ℓ′ must vanish at v_2 (q(v_2) = 0, ℓ_{13}(v_2) ≠ 0) and at v_3 (∇q(v_3) = ℓ′(v_3)∇ℓ_{13} = 0), so ℓ′ = c ℓ_{23}. Hessian of p = ℓ_{12}ℓ_{13}ℓ_{23} at v_1 (where ℓ_{12} = ℓ_{13} = 0): ℓ_{23}(v_1)(a bᵀ + b aᵀ) with a = ∇ℓ_{12}, b = ∇ℓ_{13} linearly independent and ℓ_{23}(v_1) ≠ 0; a bᵀ + b aᵀ has eigenvalues a·b ± |a||b| of opposite signs. Same at v_2, v_3. Hence no nonzero element of S_1 has a PSD Hessian at any node, and (H) holds.

## Scope

All non-collinear triples, all positive weights, n = 1, perturbative exact-representation reading.

## Open items

Explicit constants.

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.
