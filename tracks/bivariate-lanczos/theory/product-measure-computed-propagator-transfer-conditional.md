# PD-T?bivariate-lanczos-claude-116 — On product measures the computed propagator of a floating-point run inherits the univariate factorisation to first order in the coefficient deviation (CONDITIONAL on near-exact computed coefficients)

ID kind: PD-T.
Aliases: FP transfer of the product factorisation; former part 2′ of PD-T?…-105; computed-propagator perturbation; hypothesis H_δ.
Split from: PD-T?bivariate-lanczos-claude-105, part 2′. Original status row: "same for the computed propagator in FP | CONDITIONAL | named hypothesis: computed coefficients = exact ones + O(δ) with ‖L(z)⁻¹‖·δ ≪ 1 …; first order in δ". The split also takes the Assumptions sentence of PD-T?…-105 on floating point (quoted in History). Split 2026-11-01T08:33:59+01:00, Codex audit-01, L1-foundations finding S1.
Split into: none.

## Statement

Setting of PD-T?…-105: a tensor grid with distinct abscissae, product probability weights w_{ab} = u_a v_b, n ≤ min(m_x, m_y) − 1, the dev (BJ) ordering, and the window used by the run. At a node z = (ξ_a, η_b) let L(z) be the node propagator built with the exact product-type coefficients (PD-T?…-105 parts 1–2). Let L̂(z) be the node-propagator matrix of PD-T?…-104 part 1, built from the computed coefficients (β̂_k > 0, ĥ_k) of one floating-point run of the window recurrence on that grid. Put ΔL := L̂(z) − L(z), δ := ‖ΔL‖_∞, κ(z) := ‖L(z)⁻¹‖_∞, and let B(z) denote the univariate bound of PD-T?…-105 part 2 per unit forcing:

  B(z) := (n+1)² (1 + Λ_x(ξ_a)/b^x_min)(1 + Λ_y(η_b)/b^y_min) · max(1, max_t |p_t(ξ_a)|) · max(1, max_j |r_j(η_b)|).

1. **(Perturbation step; minor routine, PROVED.)**
   - (i) ΔL does not depend on z. Its row 0 is zero. Its row k ≥ 1 holds β̂_k − β_k at k and ĥ_{k,l} − h_{k,l} at l ∈ W_k, where the exact h_{k,l} vanish off the product pattern of PD-T?…-105 part 1.
   - (ii) κ(z) ≤ B(z).
   - (iii) If κ(z)δ < 1, then L̂(z) is invertible, ‖L̂(z)⁻¹‖_∞ ≤ κ(z)/(1 − κ(z)δ) and ‖L̂(z)⁻¹ − L(z)⁻¹‖_∞ ≤ κ(z)²δ/(1 − κ(z)δ). So for every forcing φ the computed response γ̂ = −L̂(z)⁻¹φ differs from the factorised response γ = −L(z)⁻¹φ of PD-T?…-105 part 2 by at most κ(z)²δ‖φ‖_∞/(1 − κ(z)δ) = κ(z)²δ‖φ‖_∞ + O(δ²).
   - (iv) In particular B(z)δ < 1 implies ‖L̂(z)⁻¹‖_∞ ≤ B(z)/(1 − B(z)δ).
2. **(Main statement; CONDITIONAL on H_δ.)** Hypothesis H_δ (named, unproved): on the given run, κ(z_i)δ ≪ 1 at every node z_i. That is, the computed coefficients equal the exact product-type coefficients up to a deviation δ that is small compared with 1/κ(z_i); B(z_i)δ ≪ 1 is a sufficient form in univariate terms. Under H_δ, at every node, the computed propagator L̂(z_i)⁻¹ — the operator that carries the run's local rounding errors into the computed basis (PD-T?…-104 part 1) — equals the factorised idealised propagator of PD-T?…-105 part 2 up to a relative perturbation of order κ(z_i)δ, i.e. to first order in δ. Its size is then bounded by univariate quantities of the marginals: under H_δ alone, ‖L̂(z_i)⁻¹‖_∞ ≤ κ(z_i)/(1 − κ(z_i)δ) ≤ B(z_i)/(1 − κ(z_i)δ) (by part 1(ii)); the bound B(z_i)/(1 − B(z_i)δ) holds only under the additional hypothesis B(z_i)δ < 1, which κ(z_i) ≤ B(z_i) does not supply. No a priori bound on δ for any floating-point run is claimed.

## Definitions

As in PD-T?…-104 (node propagator with computed coefficients) and PD-T?…-105 (Λ_x, Λ_y, b_min, p_t, r_j; second-kind polynomials). Norms: ∞-norm on R^{N_n} and the induced matrix norm.

## Assumptions

Those of PD-T?…-105 (exact product measure, probability marginals), with no breakdown in the run (β̂_k > 0) and the same window positions in L(z) and L̂(z). Part 2 additionally assumes H_δ.

## Status by part

Overall status: CONDITIONAL.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. perturbation step: z-independence of ΔL, κ ≤ B, Neumann bounds | PROVED (minor routine; excluded from status aggregation) | proof below |
| 2. transfer of the factorisation to the computed propagator of a floating-point run | CONDITIONAL | H_δ is unproved. The recorded evidence is consistent with it on tensor 41² but measures only part of δ and no κ (Evidence below) |

## Depends on

PD-T?bivariate-lanczos-claude-105 parts 1–2 (exact product-type coefficients; factorisation and the bound B(z)), PD-T?…-104 part 1 (node rows with computed coefficients). The standard Neumann-series perturbation of a matrix inverse. Related, not used: PD-T?…-110 part 3 holds verbatim for computed coefficients (its Assumptions), so with the exact product coefficients as the reference it gives an alternative multiplicative bound in terms of the transfer deviations ε_r. That bound is likewise informative only when the ε_r are small.

## Checks

No new computation. Runs needed: on the tensor 41² and Padua 48 (cubature weights) runs of R02, compute δ = ‖L̂ − L‖_∞, which needs the exact product coefficients from PD-T?…-105 part 1, and κ(z_i) or B(z_i) at the nodes, to test H_δ. No script exists yet.

## Sources

None beyond the dependencies.

## Proof or evidence

*1 (i).* PD-T?…-104 part 1 defines L̂(z)_{k,p(k)} = ĥ_{k,p(k)} − a_k(z), L̂(z)_{kk} = β̂_k, L̂(z)_{kl} = ĥ_{k,l} (l ∈ W_k \ {p(k)}) and row 0 = e_0ᵀ. L(z) has the same form with the exact coefficients. The terms −a_k(z) cancel in the difference.
*1 (ii).* By PD-T?…-105 part 2, for every forcing φ the solution of L(z)γ = −φ satisfies max_k |γ_k| ≤ B(z)·max(|γ_{(0,0)}|, max_k |φ_k|). Row 0 gives γ_{(0,0)} = −φ_0. So ‖L(z)⁻¹φ‖_∞ ≤ B(z)‖φ‖_∞.
*1 (iii)–(iv).* L̂ = L(I + L⁻¹ΔL) and ‖L⁻¹ΔL‖_∞ ≤ κδ < 1. So L̂ is invertible with L̂⁻¹ = (I + L⁻¹ΔL)⁻¹L⁻¹ and ‖L̂⁻¹‖_∞ ≤ κ/(1 − κδ). Moreover L̂⁻¹ − L⁻¹ = −L̂⁻¹ΔL L⁻¹, so ‖L̂⁻¹ − L⁻¹‖_∞ ≤ κ²δ/(1 − κδ). Part (iv) follows from (ii)–(iii), since t ↦ t/(1 − tδ) is increasing on [0, 1/δ).
*2.* This follows from part 1 once H_δ holds. H_δ itself is not established.

Evidence (MEASURED, consistent with H_δ, not establishing it):
- On tensor 41² the computed within-degree coupling (off-pattern entries of the degree-t block, relative to min β) is ≤ 7e-15 (`logs/r02_block_solve_growth.log`; PD-T?…-107 (e)). This is only part of δ: on-pattern deviations and older-degree off-pattern entries are not included, and κ is not measured.
- The loss and the propagator response are flat on tensor 41² and on Padua 48 with cubature weights (PD-T?…-107 (a), (c)).

Context: PD-T?…-112 (a) shows that on product-type measures with extreme weights (the clustered checkerboard, PD-T?…-111) the computed coefficients deviate far more (1.0e-6 in double over degrees ≤ 29). So H_δ is a genuine hypothesis and is not automatic for product-type measures.

## Scope

A statement about the computed propagator (the vector channel). It does not bound the loss of orthogonality: the propagator-to-loss link is OPEN (PD-T?…-104 open item). On product-type measures with extreme weights the loss is carried by a coefficient channel that a bounded propagator does not control (PD-T?…-112 (b), -114, -117). Non-product measures are not covered.

## Open items

An a priori bound of δ for the window recurrence on product measures (through the defect recursion of PD-T?…-102 part 4), which would discharge H_δ. A measurement of δ·κ(z_i) on the tensor and Padua runs (Runs needed above).

## History

- 2026-11-01T08:33:59+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-foundations S1; branch head 5f52331): created by splitting part 2′ out of PD-T?…-105, whose exact theorem stays PROVED there.
  - Original wording in PD-T?…-105. Status row: "| 2′. same for the computed propagator in FP | CONDITIONAL | named hypothesis: computed coefficients = exact ones + O(δ) with ‖L(z)⁻¹‖·δ ≪ 1 (the second condition was added 2026-10-31, recon-01 minor); first order in δ |". Assumptions sentence: "Part 2 is a statement about the idealised propagator with exact coefficients; in floating point the computed coefficients differ from these by rounding-induced amounts (on tensor 41² the computed off-pattern coefficients are ≤ 7e-15 relative, `logs/r02_block_solve_growth.log`), so for the computed propagator part 2 holds to first order in that deviation (CONDITIONAL on it staying small)."
  - Changes in substance:
    - "first order in δ" is written out as the explicit perturbation step 1 (minor routine, PROVED), including the norm, the z-independence of ΔL and the univariate bound κ ≤ B.
    - The named hypothesis is restated as H_δ with the same content (‖L(z)⁻¹‖δ ≪ 1).
    - "computed off-pattern coefficients ≤ 7e-15 relative" is narrowed to what `r02_block_solve_growth.log` measures: the within-degree coupling relative to min β (PD-T?…-107 (e)).
  - The claim's status is unchanged: CONDITIONAL.
- 2026-11-01T09:24:53+01:00 (Claude orchestrator `claude-opus-5-5`, response to Codex audit-02 A2-L1 / L1-A2-L1): main statement's concluding bound qualified. Original wording: «Its size is then bounded by univariate quantities of the marginals, up to the factor 1/(1 − B(z_i)δ).». Status unchanged (CONDITIONAL); part 1 (i)–(iv) unchanged.
