# PD-T?programme-ideas-claude-02 — Joint Ritz residual of a projected point mass is bounded by its saturation deficit (one-sided)

ID kind: PD-T.
Aliases: joint-Ritz/saturation lemma (gen4-1 adversary, (ii)(c)); "residual ≤ 2√(1−s)"; projected point-mass residual bound.
Split from: the combined claim of `checks/adversarial-gen4-1.md` (ii)(c) at `614709d`: the bound below **and** "joint Ritz convergence of a node is equivalent, up to constants, to its saturation … residual ≍ √(1−s)". Only the bound is retained; the converse is retracted (REJECTED: refuted, see Status and History).
Split into: none.

## Statement

Let μ = Σ_{B ∈ 𝒳} w_B δ_B be a discrete measure on finitely many nodes B = (x_B, y_B) ∈ [−1, 1]² with weights w_B > 0, let k ≥ 0 be such that Π_k ⊂ L²(μ) is injective on Π_k (the nodes are Π_k-determining), let K_k be the reproducing kernel of Π_k in L²(μ), s_k(B) := w_B K_k(B, B) ∈ (0, 1] the saturation of node B, (H_x, H_y) the section pair of μ on Π_k in an orthonormal basis, and u_B the unit coefficient vector of K_k(·, B) in that basis. Then

  ‖H_x u_B − x_B u_B‖₂ ≤ 2 √(1 − s_k(B))  and  ‖H_y u_B − y_B u_B‖₂ ≤ 2 √(1 − s_k(B)).

Consequently, a node with s_k(B) close to 1 yields a simultaneous approximate eigenvector of the two sections (a joint Ritz pair) with residual O(√(1−s_k(B))). The converse — small joint residual ⇒ saturation — is **false** in general.

## Definitions

K_k(z, B) = Σ_a p_a(z) p_a(B) for any L²(μ)-orthonormal basis (p_a) of Π_k; s_k(B) ≤ 1 because Σ_{B'} w_{B'} K_k(B', B)² = K_k(B, B). Section pair: (H_x)_{ab} = ⟨x p_b, p_a⟩_μ, (H_y)_{ab} = ⟨y p_b, p_a⟩_μ.

## Assumptions

Positive weights; nodes in [−1, 1]² (used only through |x_{B'} − x_B| ≤ 2, |y_{B'} − y_B| ≤ 2); exact arithmetic for the statement.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| residual ≤ 2√(1 − s_k(B)) for H_x and H_y | PROVED | proof below (developer proof, `checks/adversarial-gen4-1.md` (ii)(c)); MEASURED ratio residual/√(1−s) ≤ 0.79 on grids and Padua sets, n ≤ 8 (and ≤ 0.37 at n = 24, 40), `checks/code/adv/gen4-1/adv_gen4_1_product_structure.py` P4 |

Candidate / claim disposition of the retracted converse ("joint Ritz convergence ⟺ saturation up to constants; residual ≍ √(1−s)"): REJECTED.
Rejection reason: refuted. Exact counterexample constructed and checked by the Codex audit (audit-01 A2; `audit-support/rejections-check.py/.json`): equal weights on the 5 × 5 grid {−1, −½, 0, ½, 1}², k = 2, B = (0, 0): s₂(B) = 27/175 while P X P e_B = P Y P e_B = 0, so both compressed residuals vanish with saturation deficit 148/175. The audit's parity explanation (for an origin-symmetric measure and even k the kernel at the origin is even, and the residual vanishes by parity and reproduction) shows the cancellation is structural, not numerical. Registered as PD-N?programme-ideas-claude-03 (response-01 addendum, at AC's instruction "register negative results"), with a developer-written proof of the general parity statement for centrally symmetric measures and even k.

## Depends on

None beyond the reproducing property of K_k.

## Checks

- Developer: `checks/code/adv/gen4-1/adv_gen4_1_product_structure.py` (P4; output `.out` beside it, frozen at `614709d`): no violation of the bound; measured ratios as above. MEASURED.
- Audit: exact SymPy counterexample to the converse, `audit-support/rejections-check.py` (verification evidence, not a developer result).

## Sources

None used.

## Proof or evidence

Write K = K_k(·, B). The function (x − x_B)K vanishes at B, so ‖(x − x_B)K‖²_μ = Σ_{B' ≠ B} w_{B'} (x_{B'} − x_B)² K(B', B)² ≤ 4 Σ_{B' ≠ B} w_{B'} K(B', B)² = 4 (K(B, B) − w_B K(B, B)²) by the reproducing identity. The coefficient vector of the orthogonal projection P_k[(x − x_B)K] onto Π_k is (H_x − x_B I) times the coefficient vector of K, and projection does not increase the norm; dividing by ‖K‖_μ = √K(B, B) gives ‖(H_x − x_B I)u_B‖ ≤ 2 √(1 − w_B K(B, B)) = 2√(1 − s_k(B)). The y-case is identical. ∎

## Scope

One-sided sufficiency only. It gives no lower bound on the residual in terms of 1 − s, so it cannot be used to say that joint Ritz pairs occur *only* at saturated nodes, or that the absence of saturation prevents joint Ritz convergence. Any asymptotic converse would need separate localisation/separation hypotheses and is OPEN (not proposed here).

## Open items

Related open target: a converse under hypotheses, `../OPEN_TARGETS.md` B4.

None for the retained statement. For the downstream topic (b) L1 (Lanczos branch): only this sufficient bound may be transferred; the earlier handover "joint Ritz pairs converge exactly at saturated nodes" is withdrawn.

## History

- 2026-11-01, gen4-1 adversarial agent (claude-fable-5-1, xhigh), `checks/adversarial-gen4-1.md` (ii)(c): bound proved; converse asserted ("equivalent, up to constants … residual ≍ √(1−s)") from one-sided measurements.
- 2026-11-01, Codex audit-01 A2: converse refuted by the exact grid counterexample.
- 2026-11-01, response-01 (claude-opus-5-5, effort not exposed): converse retracted in the source record (struck through, original wording kept) and in `report.md`, `gate-rejected.md`, `ideas/candidates.md`; this record holds the bound only.
