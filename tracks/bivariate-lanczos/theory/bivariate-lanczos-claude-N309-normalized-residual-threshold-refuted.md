# PD-N?bivariate-lanczos-claude-309 — The pre-audit normalised-residual threshold of PD-T?…-302(b) (factor 1) is false

Final ID: **PD-N028** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: LF-M1 counterexample; normalisation counterexample; "c = 1 threshold with mass-normalised L̂"; mixing of the full-cone inradius with a mass-normalised residual.
Split from: PD-T?bivariate-lanczos-claude-302(b), pre-audit wording (the clause «the same threshold, with ε replaced by (1−θ)ε, governs representation up to a residual θε, 0 ≤ θ < 1, in the functional norm» read with the Definitions «"Up to residual θε" = ‖L_{μ′} − L̂‖ ≤ θε with L̂ := Φ^{-1}(Ĥ) normalised by L̂(1) = L_μ(1)»).
Split into: none.

## Statement

Refuted claim (pre-audit 302(b), sufficiency direction, convention (R3) with factor 1): "if r(δ) ≥ (1−θ)ε, then for every E with ‖E‖ ≤ ε (Φ(L_μ + E) defined) there is a positive measure μ′ on K_δ with ‖L_{μ′} − L̂‖ ≤ θε, where L̂ is the representative of Φ(L_μ + E) with L̂(1) = L_μ(1)".

Negation established: take n = 1, V = Π_3, the ten nodes z = (a, b) with a, b ∈ ℤ_{≥0}, a + b ≤ 3 (evaluation Vandermonde determinant 576 in absolute value, so {ev_{z_i}} is a basis of V*), the norm ‖Σ_i c_i ev_{z_i}‖ := ‖c‖_2 (so ‖p‖_* = ‖(p(z_i))_i‖_2), weights α := 1/1000 at t := (1,1) and (1 − α)/9 at the nine other nodes (m = L_μ(1) = 1), θ := 1/2, ε := 2α − α² = 1999/10⁶ and E := −ε ev_t (‖E‖ = ε). Then:
1. M_1(L_μ + E) ≻ 0 (leading minors 998001/10⁶, 110778111/10⁸, 36889110963/(4·10¹⁰) in the basis 1, x, y), so Ĥ := Φ(L_μ + E) is a consistent degree-1 section pair;
2. r(δ) ≥ r(0) = α = 1/1000 > (1−θ)ε = 1999/(2·10⁶) for every δ ≥ 0, so δ*((1−θ)ε) = 0;
3. for every δ ∈ [0, 10⁻⁸], dist(L̂, C(K_δ)) > θε, where L̂ = (L_μ + E)/(1 − ε); at δ = 0 the distance is exactly 1/999. So for every such δ — in particular every δ ∈ (0, 10⁻⁸], all of which exceed δ*((1−θ)ε) — no positive measure μ′ on K_δ, of any mass, satisfies ‖L_{μ′} − L̂‖ ≤ θε.
Meanwhile the unnormalised distance dist(L_μ + E, C(K_0)) = 999/10⁶ ≤ θε, as the corrected PD-T?…-302(b1) requires.

## Negative-result scope (PD-N only)

Attempted mechanism: the residual-threshold rule of pre-audit PD-T?bivariate-lanczos-claude-302(b) — transferring the full-ball inradius criterion r(δ) ≥ (1−θ)ε, with the exact constant 1, to residuals measured against the mass-normalised representative L̂ of the section data.
Parameter range: the explicit data above (n = 1, ten nodes, ℓ2 norm in evaluation coordinates, θ = 1/2, the single E), δ ∈ [0, 10⁻⁸]. This refutes the universally quantified claim; it does not say how large the normalisation loss is for other data. Not affected: exact representation (θ = 0), the full-ball criterion and the unnormalised residual threshold (302(b1)), the mass-slice threshold with r_0 and fixed-mass approximants (302(b2)), the factor-carrying version (302(b3)), the rate exponents of PD-T?…-303 and the sign-separation obstructions PD-N?…-301/303 (all invariant under positive scaling or stated for the unnormalised L_μ + E).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| items 1, 2 and item 3 at δ = 0 | PROVED (exact rational computation) | proof below; auditor's `exact_framework_checks.py` (rerun by the developer); developer's independent `t302b_conventions_check.py` part A |
| item 3 for δ ∈ (0, 10⁻⁸] | PROVED | Lipschitz argument below with an explicit rational gradient bound; `t302b_conventions_check.py` part B |

Candidate / claim disposition: pre-audit PD-T?…-302(b) normalised-residual variant REJECTED. Rejection reason: refuted (within the stated scope: one explicit instance suffices to refute the universal claim).

## Depends on

PD-T?…-301 (Φ is defined when M_n ≻ 0; scale invariance), PD-T?…-302(a) (closed cone, dual cone Pos(K_δ)).

## Checks

- Auditor's exact checker (Codex audit-01, LF-M1), executed by the developer on 2026-11-01 at ≈08:30 with `OPENBLAS_NUM_THREADS=1 python3 topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.py` (Python 3.13.18, SymPy 1.13.3): "NORMALIZATION COUNTEREXAMPLE: n=1 M=10, determining Pi3 Vandermonde determinant= 576 … r(0)= 1/1000 (1-theta)epsilon= 1999/2000000 … M1(Lmu+E) Sylvester minors= [998001/1000000, 110778111/100000000, 36889110963/40000000000] … normalized Lhat mass=1; exact distance to C(K0)= 1/999 > 1999/2000000 … Unnormalized distance= 999/1000000". Output printed to the terminal, not saved (the audit's own logs are `audit-01/L3-framework/exact_framework_checks.log` and `audit-01/root-framework-rerun.log`).
- Developer's independent re-implementation (Fraction arithmetic only, no import of audit or reviewer code): `python3 -I tracks/bivariate-lanczos/code/L3/t302b_conventions_check.py` (sha256 f8ad12db…0d50) → `topics/bivariate-lanczos-20261031/directions/L3/logs/t302b_conventions_check.log` (sha256 b829dd85…2039): part A reproduces items 1–3 at δ = 0 (leading minors in the basis 1, x, y: 998001/10⁶, 110778111/10⁸, 36889110963/(4·10¹⁰)); part B computes the Lagrange polynomial q of node t, the gradient bound G = 120 on [−1, 4]² and certifies δ′ = 10⁻⁸ exactly.

## Sources

Codex audit-01, `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md` §LF-M1 (the counterexample and the remark that the gap persists for small δ > 0 are the auditor's; this file records them as a scoped negative result and supplies the explicit radius).

## Proof or evidence

Items 1–2 and the evaluation basis: exact rational arithmetic (Checks). In the evaluation coordinates the cone C(K_0) is the nonnegative orthant and Pos(K_0) = {p : p(z_i) ≥ 0}; for v := (p(z_i))_i ≥ 0 with ‖v‖_2 = 1, L_μ(p) = w·v ≥ w_min ‖v‖_1 ≥ w_min, with equality at v = e_t, so r(0) = α; r is nondecreasing (302(b1)).
Item 3 at δ = 0: L_μ + E has coordinates α − ε = −α(1 − α) at t and (1 − α)/9 elsewhere, mass 1 − ε = (1 − α)². Hence L̂ = (L_μ + E)/(1 − ε) has the single negative coordinate −α/(1 − α) and its ℓ2 distance to the orthant is α/(1 − α) = 1/999 > 1999/(2·10⁶) = θε.
Item 3 for δ > 0: let q ∈ Π_3 be the Lagrange polynomial with q(z_i) = [i = t]; ‖q‖_* = 1 and ‖1‖_* = √10. For δ ≤ 1 the balls B̄(z_i, δ) lie in the box [−1, 4]², on which |∇q| ≤ G := Σ |q_{ab}|(a·4^{a−1}4^b + b·4^a4^{b−1}) = 120 (q = Σ q_{ab} x^a y^b); since q(z_i) ≥ 0 at every node, q ≥ −Gδ on K_δ, so p_δ := q + Gδ ∈ Pos(K_δ) and ‖p_δ‖_* ≤ 1 + √10 Gδ. Every L′ ∈ C(K_δ) has L′(p_δ) ≥ 0, while L̂(p_δ) = L̂(q) + Gδ L̂(1) = −α/(1 − α) + Gδ. Therefore ‖L′ − L̂‖ ≥ (L′ − L̂)(p_δ)/‖p_δ‖_* ≥ (1/999 − Gδ)/(1 + √10 Gδ), and at δ = 10⁻⁸ the right side exceeds θε (exact check after squaring, part B); the bound decreases in δ, so it holds on [0, 10⁻⁸].
Since dist(L_μ + E, C(K_0)) = ε − α = 999/10⁶ ≤ θε, the defect is exactly the normalisation factor s_E = 1/(1 − ε) of 302(b3).

## Scope

Refutes only the factor-1 normalised-residual threshold. The corrected statements in PD-T?…-302(b1)–(b4) are unaffected, and so is every exact-representation statement in PD-T?…-303–306, 310, 313 and PD-N?…-301–303.

## Open items

None for this statement. (How large the normalisation loss can be in general is answered by the two-sided bound of 302(b3).)

## History

- 2026-11-01T08:33:39+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer: created in response to finding LF-M1 of Codex audit-01 (topics/bivariate-lanczos-20261031/audit-01/L3-framework.md; candidate 5ccfac2). The counterexample is the auditor's; the explicit radius δ′ = 10⁻⁸ and the independent exact re-implementation are the developer's. Original wording of the refuted claim is quoted in "Split from" and in the History of PD-T?…-302.
