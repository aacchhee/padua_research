# PD-T?padua-xu-lebesgue-20261114-claude-34 — translation (product) formula for the Morrow–Patterson fundamental polynomials and the averaged shifted-lattice bound

ID kind: PD-T.
Aliases: X2-34; translation formula; box-average formula; averaged bound; Ξ-functional; tool for steps P2–P4 of the X2-28 plan.
Split from: none.
Split into: none.

## Statement

Let n ≥ 2 be even, M = n + 2, N = M(M+1), and
G̃(α, β) := Σ_{k,l≥1, k+l≤M} kl sin(kα) sin(lβ) = ¼ ∂_α∂_β D_M(α, β) (so G̃(α,β) = sin α sin β · G_n(cos α, cos β), G_n the corner kernel of X2-21).
For real a₁, a₂ define the shifted-lattice sum
Ξ_n(a₁, a₂) := (8/N) Σ_{(p,q)∈𝒩} sin w_p sin v_q |G̃(w_p + a₁, v_q + a₂)|.

(a) **Translation formula.** For θ₁, θ₂ ∈ (0, π) and every node,
ℓ_{p,q}(cos θ₁, cos θ₂) = (2 sin w_p sin v_q / (N sin θ₁ sin θ₂)) ∫_{−θ₁}^{θ₁} ∫_{−θ₂}^{θ₂} G̃(w_p + a₁, v_q + a₂) da₂ da₁.

(b) **Averaged bound.** λ_n(cos θ₁, cos θ₂) ≤ (4 sin θ₁ sin θ₂)⁻¹ ∫_{−θ₁}^{θ₁}∫_{−θ₂}^{θ₂} Ξ_n(a₁,a₂) da₂ da₁ = (θ₁θ₂/(sin θ₁ sin θ₂)) · mean of Ξ_n over the box [−θ₁,θ₁]×[−θ₂,θ₂], and Ξ_n(0,0) = λ_n(1,1).

(c) **Equality near the vertex.** If, for every node, (a₁,a₂) ↦ G̃(w_p + a₁, v_q + a₂) has no sign change on the box, then (b) is an equality. This holds for all sufficiently small θ₁, θ₂ (depending on n), because G̃(w_p, v_q) ≠ 0 at every node (X2-23 (f)).

(d) **One-variable form.** For θ₁ ∈ (0,π): ℓ_{p,q}(cos θ₁, 1) = (4 sin w_p sin v_q/(N sin θ₁)) ∫_{−θ₁}^{θ₁} G̃(w_p + a₁, v_q) da₁, and λ_n(cos θ₁, 1) ≤ (θ₁/sin θ₁)·mean_{|a₁|≤θ₁} Ξ_n(a₁, 0).

## Definitions

As in X2-21, X2-33 (D_M). The box mean is with respect to Lebesgue measure.

## Assumptions

n even, n ≥ 2. (c) uses X2-23 (f).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) translation formula | PROVED | from (K1) of X2-33 |
| (b) averaged bound | PROVED | triangle inequality |
| (c) equality case | PROVED | — |
| (d) one-variable form | PROVED | limit θ₂ → 0 of (a) |
| limit of Ξ_n(φ₁/M, φ₂/M)/M² | not claimed here (heuristic + MEASURED) | X2-N35, X2-28 addendum |

Candidate / claim disposition: none.

## Depends on

X2-33 Step 0, formula (K1) (which rests on X2-21 definitions only); X2-23 (f) for (c).

## Checks

- `python3 code/mp/research/x2r3_checks.py transl` (mpmath 30 digits; 2026-11-14): (a) at all nodes of n = 2, two points (θ₁,θ₂) ∈ {(0.3, 1.1), (2.0, 0.7)}, by two-dimensional quadrature of the double sum: max error 1.6e−30 (43 s); closed form of G̃ (float64) against the double sum: relative error 3.6e−14; Ξ_20(0,0) − λ_20(1,1) = 1.4e−12 (float64).
- Independent rerun: pending.

## Sources

None used. The formula is the bivariate form of the classical product formula for Chebyshev polynomials of the second kind, U_i(cos θ)U_i(cos w)/(i+1) = (2 sin θ sin w)⁻¹∫_{w−θ}^{w+θ} U_i(cos α) sin α dα (textbook; not used as a lemma, the proof below is direct).

## Proof or evidence

**(a)** D_M is even in each variable. In (K1) of X2-33, Σ_{σ₁,σ₂}σ₁σ₂D_M(θ₁ − σ₁w, θ₂ − σ₂v) = D_M(w−θ₁, v−θ₂) − D_M(w−θ₁, v+θ₂) − D_M(w+θ₁, v−θ₂) + D_M(w+θ₁, v+θ₂) = ∫_{w−θ₁}^{w+θ₁}∫_{v−θ₂}^{v+θ₂} ∂_α∂_βD_M dβ dα = 4∫_{−θ₁}^{θ₁}∫_{−θ₂}^{θ₂} G̃(w + a₁, v + a₂) da₂ da₁. Insert in (K1). The identity G̃ = ¼∂_α∂_βD_M: Σ_{|k|+|l|≤M} kl e^{i(kα+lβ)} = Σ_{k,l≥1} kl[2cos(kα+lβ) − 2cos(kα−lβ)] = −4Σ kl sin kα sin lβ, and ∂_α∂_β e^{i(kα+lβ)} = −kl e^{i(kα+lβ)}. Finally sin kα sin lβ = sin α sin β U_{k−1}(cos α)U_{l−1}(cos β) gives G̃ = sin α sin β G_n(cos α, cos β). ∎

**(b)** Take absolute values under the integral in (a) and sum over the nodes: λ_n ≤ (2/(N sin θ₁ sin θ₂))∫∫ Σ sin w sin v |G̃| = (4 sin θ₁ sin θ₂)⁻¹∫∫ Ξ_n. At a = 0: Ξ_n(0,0) = (8/N)Σ sin²w sin²v |G_n(x_p,y_q)| = Σ ω_{p,q}|K_n((1,1), z_{p,q})| = λ_n(1,1). ∎

**(c)** If G̃(w_p + ·, v_q + ·) keeps one sign on the box, then |∫∫G̃| = ∫∫|G̃| for that node, so every inequality used in (b) is an equality. G̃ is continuous and G̃(w_p, v_q) = sin w_p sin v_q G_n(x_p, y_q) ≠ 0 by X2-23 (f); there are finitely many nodes. ∎

**(d)** Let θ₂ → 0 in (a): (sin θ₂)⁻¹∫_{−θ₂}^{θ₂} G̃(w + a₁, v + a₂) da₂ → 2G̃(w + a₁, v), uniformly in a₁; ℓ_{p,q} is continuous. So ℓ_{p,q}(cos θ₁, 1) = (4 sin w sin v/(N sin θ₁))∫_{−θ₁}^{θ₁} G̃(w + a₁, v) da₁. Summing absolute values: λ_n(cos θ₁, 1) ≤ (2 sin θ₁)⁻¹∫_{−θ₁}^{θ₁} Ξ_n(a₁, 0) da₁. ∎

Remark (second-order exactness; not used elsewhere). By (c), near the vertex λ_n(cos θ₁, cos θ₂) equals the box mean of Ξ_n times θ₁θ₂/(sin θ₁ sin θ₂), and Ξ_n is real-analytic near 0; comparing second-order terms with X2-31 gives D_x = −(Ξ_n(0) + ∂²_{a₁}Ξ_n(0))/3 and D_y = −(Ξ_n(0) + ∂²_{a₂}Ξ_n(0))/3. So the averaged bound loses nothing at second order at the vertex; it loses only where the box contains sign changes of the shifted kernels.

## Scope

Exact identities and one inequality, every even n ≥ 2. The inequality (b) is useful only for small boxes: for shifts of size ≫ 1/n in both variables Ξ_n contains an extra factor of order log n (heuristic count in `attempts/X2-round3.md`, §4), so (b) cannot replace X2-33 away from the vertices.

## Open items

Asymptotics of Ξ_n(φ₁/M, φ₂/M) with explicit error (X2-28 addendum, item W).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-3; uncommitted at writing. First version.
