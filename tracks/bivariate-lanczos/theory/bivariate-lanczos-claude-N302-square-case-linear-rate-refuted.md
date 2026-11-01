# PD-N?bivariate-lanczos-claude-302 — In the square case no backward construction achieves δ = O(ε)

ID kind: PD-N.
Aliases: kill-test alternative "construction always works with δ = O(ε)" refuted for M = N_n; √ε necessity in the square case.
Split from: none (case of the target PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

For every n ≥ 1, every Π_n-unisolvent node set with M = N_n points and every positive weights, there are C > 0 and, for every small ε > 0, a consistent ε-perturbation Ĥ = Φ(L_μ + E) of the degree-n sections such that every positive measure whose exact degree-n sections equal Ĥ has a support point at distance ≥ (ε/C)^{1/2} from the nodes. In particular no construction with δ = O(ε) works in the square case (Padua or not).

## Negative-result scope (PD-N only)

Attempted mechanism: the second branch of the frozen L3-Q1 kill test ("a construction that always works with δ = O(ε)") in the square case; IDEA?bivariate-lanczos-claude-306.
Parameter range: square case M = N_n, n ≥ 1, perturbative regime, exact representation of perturbations given as data (reading (E)); residual variant (Proof): residual ≤ θε, 0 ≤ θ < 1, in any of the conventions (R1)–(R3) of PD-T?…-302, with constants depending also on θ and the convention. The pre-audit wording "with the residual defined with fixed scale c = 1 as in PD-T?…-302" referred to the normalised threshold refuted in PD-N?…-309. The overdetermined case is not affected (there δ = 0, PD-T?…-303(a)).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| S_1 ≠ {0} in the square case | PROVED | dim Π_{2n+1} − 3N_n = n(n+1)/2 > 0 |
| r(δ) ≤ Cδ² ⇒ δ* ≥ (ε/C)^{1/2} | PROVED | PD-T?…-303(c), PD-T?…-302(b1) |
| residual variant in conventions (R1)–(R3) | PROVED (routine) | proof below; PD-T?…-302(b1)–(b3) |

Candidate / claim disposition: REJECTED (the δ = O(ε) construction, square case). Rejection reason: refuted.

## Depends on

PD-T?…-302, 303 (alternatively PD-T?…-304(a) via the commutator).

## Checks

Proof only; MEASURED illustrations in PD-T?…-307.

## Sources

None.

## Proof or evidence

PD-T?…-303(c) and PD-T?…-302(b1) (take E along the minimiser p of r(δ) for δ = (ε/C)^{1/2}/2).
Residual variant (routine). Let r(δ) ≤ C′δ² for δ ≤ δ_1 (303(c)) and fix θ ∈ [0, 1). (R1): for δ := ((1−θ)ε/C′)^{1/2}/2 (≤ δ_1 for small ε), r(δ) < (1−θ)ε, and the E of 302(b1) (‖E‖ = ε) has dist(L_μ + E, C(K_δ)) > θε; since C(K_{δ′}) ⊂ C(K_δ) for δ′ ≤ δ, every positive μ′ with ‖L_{μ′} − (L_μ + E)‖ ≤ θε has a support point at distance > δ from the nodes. (R3): for the same E, dist(L̂, C(K_δ)) ≥ s_E(ε − r(δ)) ≥ m(ε − r(δ))/(m + ε‖1‖_*) (302(b3)); with δ := ((1−θ)ε/(2C′))^{1/2}/2 one has r(δ) ≤ (1−θ)ε/8, hence ε − r(δ) ≥ ε(1+θ)/2, and the bound exceeds θε as soon as θε‖1‖_* < m(1−θ)/2. (R2): by 302(b2)(iii), r_0(δ) ≤ A r(δ)/(1 − B r(δ)) ≤ 2AC′δ² when B r(δ) ≤ 1/2; with δ := ((1−θ)ε/(2AC′))^{1/2}/2, r_0(δ) < (1−θ)ε, and 302(b2)(ii) gives E ∈ H_0, ‖E‖ ≤ ε, such that every positive μ′ of mass m with ‖L_{μ′} − (L_μ + E)‖ ≤ θε has a support point at distance > δ. In all three conventions the forced support spread is ≥ c(θ, convention)·√ε.

## Scope

As stated.

## Open items

None for this statement.

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.
- 2026-10-31T23:54:00+01:00, L3 developer: "atom" → "support point" and the residual convention c = 1 (finding M2) per L3-reconstruction-01 (topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md, audited head 0b7b396).
- 2026-11-01T00:47:14+01:00, L3 developer: finding L11 of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1) — original wording of the passages replaced at 2026-10-31T23:54 (round-1 response): «has an atom at distance ≥ (ε/C)^{1/2} from the nodes.»; «exact representation (or residual ≤ θε, θ < 1).».
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): propagation of finding LF-M1 of Codex audit-01 (audit-01/L3-framework.md; candidate 5ccfac2) — residual scope restated for the corrected conventions (R1)–(R3) of PD-T?…-302 with a routine proof of the residual variant; the exact statement and its status are unchanged. Original wording of the replaced passages: «Parameter range: square case M = N_n, n ≥ 1, perturbative regime, exact representation (or residual ≤ θε, θ < 1, with the residual defined with fixed scale c = 1 as in PD-T?…-302). The overdetermined case is not affected (there δ = 0, PD-T?…-303(a)).»; «| r(δ) ≤ Cδ² ⇒ δ* ≥ (ε/C)^{1/2} | PROVED | PD-T?…-303(c), PD-T?…-302(b) |»; «PD-T?…-303(c) and PD-T?…-302(b) (take E along the minimiser p of r(δ) for δ = (ε/C)^{1/2}/2).».
