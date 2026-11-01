# PD-N?programme-ideas-claude-03 — A joint Ritz residual can vanish at a non-saturated node: no lower bound by the saturation deficit

ID kind: PD-N.
Aliases: refutation of "joint Ritz ⟺ saturation" / "residual ≍ √(1−s)"; parity cancellation at a symmetry centre; audit-01 A2 counterexample.
Split from: the converse half of the combined claim in `checks/adversarial-gen4-1.md` (ii)(c) at `614709d`; the retained half is `PD-T?programme-ideas-claude-02`.
Split into: none.

## Statement

Let μ = Σ_B w_B δ_B be a positive discrete measure on [−1, 1]² that is invariant under z ↦ −z and has the origin as a node, let k ≥ 2 be even with Π_k injective on supp μ, and let u_0 be the unit coefficient vector of K_k(·, 0) (notation of PD-T?programme-ideas-claude-02). Then

  H_x u_0 = 0 and H_y u_0 = 0 exactly,

so u_0 is an exact joint eigenvector of the section pair with eigenvalue (0, 0), whatever the saturation s_k(0) = w_0 K_k(0, 0) is. Consequently there is no inequality ‖H_x u_B − x_B u_B‖ + ‖H_y u_B − y_B u_B‖ ≥ c (1 − s_k(B))^β with c > 0 valid for all node sets. Explicitly, for equal weights on {−1, −½, 0, ½, 1}² and k = 2: s_2(0) = 27/175 (deficit 148/175) and both residuals are 0.

## Definitions

As in PD-T?programme-ideas-claude-02.

## Assumptions

Positive weights; central symmetry of μ; origin a node; k even; exact arithmetic.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| parity cancellation for centrally symmetric measures, even k | PROVED | proof below (the mechanism first stated in the Codex audit's R1; written out here by the developer) |
| explicit instances | PROVED (exact arithmetic) | `checks/code/response-02/ritz_converse_parity.py/.out`: 5 × 5 grid k = 2 (s = 27/175) and k = 4 (s = 541/1225), 7 × 7 grid k = 2 (s = 11/147); both residuals exactly zero in every case. First found by the audit (`audit-support/rejections-check.py`). |

Candidate / claim disposition: the side claim "joint Ritz convergence of a node is equivalent, up to constants, to its saturation; residual ≍ √(1−s)" (`checks/adversarial-gen4-1.md` (ii)(c); IDEA?programme-ideas-claude-16) is REJECTED.
Rejection reason: refuted (the cancellation holds at the centre of every centrally symmetric node set for even k, and contradicts the claimed lower bound at every such centre with s_k(0) < 1, e.g. the exact grid instances). [response-02, audit-02 B4.1: earlier wording "its negation is established for every centrally symmetric node set with a central node and even k" ignored saturated centres; at s_k(0) = 1 cancellation is consistent with the bound — exact example {0, ±(1,0), ±(0,1), ±(1,1)}, k = 2, `checks/code/response-02/ritz_saturated_centre.py/.out`.]

## Negative-result scope (PD-N only)

Attempted mechanism: reading joint Ritz convergence as a characterisation of saturation (lower bound on the residual by the deficit), proposed as a handover to (b) L1 (IDEA?programme-ideas-claude-16, gen4-draft-1 sub-problem 4).
Parameter range: all centrally symmetric positive discrete measures on [−1,1]² with a central node, all even k. **Not covered:** non-symmetric measures, nodes other than a symmetry centre, odd k, and any asymptotic converse under added localisation or separation hypotheses (not claimed either way).

## Depends on

PD-T?programme-ideas-claude-02 (definitions only).

## Checks

`python -I checks/code/response-02/ritz_converse_parity.py > checks/code/response-02/ritz_converse_parity.out` (SymPy 1.14.0, exact rationals). Independent: Codex audit-01 `audit-support/rejections-check.py/.json` (5 × 5, k = 2).

## Sources

None.

## Proof or evidence

Write K = K_k(·, 0). Since μ and Π_k are invariant under z ↦ −z, so is the reproducing kernel: K(−z, 0) = K(z, 0), i.e. K is even. The coefficient vector of the orthogonal projection P_k[xK] is H_x times the coefficient vector of K (x_0 = 0), so it suffices to show ⟨xK, p⟩_μ = 0 for every p ∈ Π_k. Split p into even and odd parts. For even p, xKp is odd and its μ-integral vanishes by symmetry. For odd p, every monomial of p has odd degree ≤ k, hence ≤ k − 1 because k is even; then xp ∈ Π_k and ⟨xK, p⟩_μ = ⟨K, xp⟩_μ = (xp)(0) = 0 by the reproducing property. Hence P_k[xK] = 0 and H_x u_0 = 0; the same argument with y gives H_y u_0 = 0. The saturation s_k(0) = w_0 K(0,0) is unrestricted by this argument; the explicit grid values are computed exactly in the script. ∎

## Scope

Exactly as in the negative-result scope: the converse fails at every unsaturated symmetry centre of a centrally symmetric measure (even k), a large structured class; the one-sided bound of PD-T?programme-ideas-claude-02 is unaffected.

## Open items

Whether a converse holds for generic (non-symmetric) measures or away from symmetry centres, with explicit hypotheses — OPEN, listed in `OPEN_TARGETS.md` (B4).

## History

- 2026-11-01, gen4-1 adversarial agent (claude-fable-5-1, xhigh): converse asserted.
- 2026-11-01, Codex audit-01 A2 / R1: exact counterexample and parity explanation.
- 2026-11-01, response-01 (claude-opus-5-5): converse retracted; no PD-N proposed.
- 2026-11-01, response-02 (claude-opus-5-5): rejection reason and summaries aligned with the formal Statement (cancellation everywhere; refutation where s < 1), audit-02 B4.1.
- 2026-11-01, response-01 addendum (claude-opus-5-5), at AC's instruction "register negative results" (08:47 CET): registered as this PD-N with a developer-written proof of the general parity statement and an independent exact script.
