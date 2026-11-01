# PD-T?bivariate-lanczos-claude-105 — For product measures the per-node propagator of the window recurrence factorises into univariate Jacobi impulse responses

ID kind: PD-T.
Aliases: product decoupling; tensor-grid stability mechanism; chain factorisation; "no bivariate amplification on product measures".
Split from: none.
Split into: PD-T?bivariate-lanczos-claude-116 (`product-measure-computed-propagator-transfer-conditional.md`): the former part 2′, i.e. the transfer of part 2 to the computed propagator of a floating-point run (CONDITIONAL on near-exact computed coefficients). Split 2026-11-01T08:33:59+01:00, Codex audit-01 finding S1.

## Statement

Let the nodes be a tensor grid {(ξ_a, η_b) : 1 ≤ a ≤ m_x, 1 ≤ b ≤ m_y} with distinct ξ's, distinct η's and product weights w_{ab} = u_a v_b > 0, and let n ≤ min(m_x, m_y) − 1. Let p_s (resp. r_j) be the orthonormal polynomials of μ_x = Σ_a u_a δ_{ξ_a} (resp. μ_y = Σ_b v_b δ_{η_b}) with Jacobi coefficients (a^x_s, b^x_s) (resp. (a^y_j, b^y_j)), b_0 := 0, and let σ^y_j be the second-kind polynomials of μ_y (σ_0 = 0, σ_j(η) = ∫ (r_j(η) − r_j(t))/(η − t) dμ_y(t)); similarly σ^x.

1. **[EXACT] Product structure.** In the ordering of PD-T?…-101, q_{t,j} has node values p_{t−j}(ξ_a) r_j(η_b) √(u_a v_b) (up to the global normalisation of q_0). The exact window coefficients are: F-product creating (t, j), j ≥ 1: (t−1, j−1) ↦ a^y_{j−1}, (t−2, j−2) ↦ b^y_{j−1}, β = b^y_j, all other window coefficients 0; J-product creating (t, 0): (t−1, 0) ↦ a^x_{t−1}, (t−2, 0) ↦ b^x_{t−1}, β = b^x_t, all others 0. In particular the within-degree coupling matrix A′_t (entries: coefficient of q_{(t,r)} in F q_{(t−1,j−1)}, 1 ≤ r ≤ j ≤ t) is diagonal.
2. **[IDEALIZED: the node propagator L(z) of PD-T?…-104 built with the exact coefficients of 1.] Factorisation.** For every node z = (ξ_a, η_b) and every forcing φ, the solution γ of L(z)γ = −φ satisfies
   γ_{(t,0)} = −Σ_{s=1}^{t} ρ^{x,[s]}_t(ξ_a) φ_{(s,0)} / b^x_s + γ_{(0,0)} p_t(ξ_a),
   γ_{(α+j, j)} = r_j(η_b) γ_{(α,0)} − Σ_{s=1}^{j} ρ^{y,[s]}_j(η_b) φ_{(α+s,s)} / b^y_s,
   with the univariate impulse responses ρ^{[s]}_j(η) = b_s ( r_{s−1}(η) σ_j(η) − σ_{s−1}(η) r_j(η) ) (and the same with x). Consequently
   max_{k ⪯ (n,n)} |γ_k| ≤ (n+1)² (1 + Λ_x(ξ_a)/b^x_min)(1 + Λ_y(η_b)/b^y_min) · max(|γ_{(0,0)}|, max_k |φ_k|) · max(1, max_t |p_t(ξ_a)|) max(1, max_j |r_j(η_b)|),
   where Λ_y(η) := max_{1 ≤ s ≤ j ≤ n} |ρ^{y,[s]}_j(η)| ≤ 2 b^y_max max_{l ≤ n} |r_l(η)| · max_{l ≤ n} |σ^y_l(η)| (likewise Λ_x). At nodes, |r_l(η_b)| ≤ 1/√v_b and |p_s(ξ_a)| ≤ 1/√u_a. All amplification factors are univariate quantities of the marginal measures; no bivariate amplification occurs.
3. **[EXACT] Non-product measures.** If the exact within-degree coupling A′_t is not diagonal for some t (equivalently, some F-product has a nonzero exact coefficient on a column of its own degree other than its child), the chain decomposition of 2. does not hold.

## Definitions

Impulse response ρ^{[s]}: the solution of b_{l+1}ρ_{l+1} = (η − a_l)ρ_l − b_lρ_{l−1} (l ≥ s) with ρ_{s−1} = 0, ρ_s = 1. Chain α: the columns (α + j, j), j = 0, 1, …, i.e. the F-chain started at the J-column (α, 0).

## Assumptions

Tensor grid with product weights (exact product measure), with μ_x and μ_y normalised as **probability measures** (Σu_a = Σv_b = 1). This was implicit and is needed: W_0 = −1 uses σ_1 = μ_y(1)/b_1, and |r_l(η_b)| ≤ 1/√v_b uses it (added 2026-10-31, recon-01 minor). n ≤ min(m_x, m_y) − 1 (U(n) holds and all columns of degree ≤ n are nonzero). Part 2 is a statement about the idealised propagator with exact coefficients. Its transfer to the computed propagator of a floating-point run is a separate CONDITIONAL claim, PD-T?…-116 [split 2026-11-01T08:33:59+01:00, audit-01 S1; the original sentence is preserved in History].

## Status by part

Overall status: PROVED (part 2 under the stated idealisation).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. product structure and exact coefficients | PROVED | proof below. Consistency check, not a claim of this file: on tensor 41² the computed within-degree coupling is ≤ 7e-15, MEASURED in PD-T?…-107 (e) |
| 2. factorisation and bound (idealised propagator) | PROVED | proof below |
| 3. non-product: decomposition fails | PROVED (reading of 1.) | cross-reference, not a claim of this file: the computed coupling ratios 0.3–2.5 on the rotated squares and the triangle are MEASURED in PD-T?…-107 (e) |

## Depends on

PD-T?…-101 (ordering, graded basis), PD-T?…-104 (node propagator). Standard univariate facts re-proved below (second-kind polynomials, Casoratian).

## Checks

`code/L1/l1_block_solve_growth.py` (A′_t diagonal to 7e-15 on tensor 41²); `code/L1/l1_node_propagator.py` (flat propagator response on tensor 41² and Padua 48 with cubature weights; the Padua cubature measure reproduces the product Chebyshev inner products up to degree 2·48 − 1, so the exact coefficients of degree ≤ 47 are of product type).

## Proof or evidence

*1.* The vectors with node values p_s(ξ_a)r_j(η_b)√(u_av_b) are orthonormal for the product measure; for s + j = t the product p_{t−j}(x)r_j(y) equals c x^{t−j}y^j plus monomials x^{a′}y^{b′} with a′ ≤ t−j, b′ ≤ j, (a′, b′) ≠ (t−j, j), i.e. of total degree < t, so it lies in span{(t, j)} + S_{t−1} with positive leading coefficient. By PD-T?…-101 part 1 (uniqueness of the Gram–Schmidt basis with positive leading coefficients) it is q_{t,j}. Then y·p_{t−j}(x)r_{j−1}(y) = p_{t−j}(x)(b^y_j r_j + a^y_{j−1} r_{j−1} + b^y_{j−1} r_{j−2}) gives the F-coefficients, and x·p_{t−1}(x) r_0 = b^x_t p_t + a^x_{t−1} p_{t−1} + b^x_{t−1} p_{t−2} the J-coefficients.
*2.* With these coefficients, row (t, j), j ≥ 1, of L(z)γ = −φ reads b^y_jγ_{(t,j)} = (η_b − a^y_{j−1})γ_{(t−1,j−1)} − b^y_{j−1}γ_{(t−2,j−2)} − φ_{(t,j)}, which involves only chain α = t − j; row (t, 0) reads b^x_tγ_{(t,0)} = (ξ_a − a^x_{t−1})γ_{(t−1,0)} − b^x_{t−1}γ_{(t−2,0)} − φ_{(t,0)}. Each is a univariate three-term recurrence driven by forcing, so its solution is the initial-value part plus the superposition of impulse responses: initial value γ_{(α,0)} with γ_{(α−1,−1)} = 0 propagates as r_j(η_b)γ_{(α,0)} (r_0 = 1, and r satisfies the recurrence from l = 0); a forcing −φ at step s ≥ 1 sets γ_s = −φ/b_s and then propagates homogeneously, i.e. as −(φ/b_s)ρ^{[s]}. *Impulse formula:* σ satisfies the same recurrence for l ≥ 1: the numerator of [(η − a_l)σ_l − b_lσ_{l−1} − b_{l+1}σ_{l+1}] equals ∫[−(η − a_l)r_l(t) + b_l r_{l−1}(t) + b_{l+1} r_{l+1}(t)]/(η − t) dμ(t) = −∫ r_l dμ = 0 (use the recurrence at η and at t). The Casoratian W_l := b_{l+1}(r_{l+1}σ_l − r_lσ_{l+1}) is constant for l ≥ 0 (both solve the recurrence for l ≥ 1) and W_0 = b_1(0 − 1/b_1) = −1. For s ≥ 1 write ρ^{[s]} = c_1 r + c_2 σ with c_1 r_{s−1} + c_2 σ_{s−1} = 0, c_1 r_s + c_2 σ_s = 1; the determinant is r_{s−1}σ_s − σ_{s−1}r_s = 1/b_s (W_{s−1} = −1), so c_1 = −b_sσ_{s−1}, c_2 = b_s r_{s−1}. *Bound:* triangle inequality over at most n+1 forcing steps per chain and per J-chain, with |r_l(η_b)|² ≤ Σ_l r_l(η_b)² ≤ 1/v_b (rows of the orthogonal matrix [r_l(η_c)√v_c]).
*3.* If A′_t has a nonzero strictly lower entry, row (t, j) of L(z) couples γ_{(t,j)} to γ_{(t,r)}, r < j, which lies on chain t − r ≠ t − j.

## Scope

The statement explains the **idealised propagator** (no amplification beyond univariate behaviour on exact product measures and, by PD-T?…-111, on moment-matching measures such as Padua with cubature weights). It does **not** by itself explain the loss: the link from propagator to loss is OPEN (PD-T?…-104 open item). The flat loss measured on these sets (PD-T?…-107) is consistent with it. On product-type measures with very non-uniform weights the loss is not flat, because of a coefficient channel (PD-T?…-112, -114, -115). Nothing quantitative is said about near-product or non-product measures beyond the coupling reading of part 3. Non-diagonal within-degree coupling does not by itself imply growth: weights exp(xy) and exp(4xy) on the square are stable or mildly unstable (recon-01; developer rerun 2.7× and 32× u/ρ_Z at n = 24). Λ_y is finite and depends only on μ_y; it is not bounded here.

Corrected 2026-10-31T23:05Z (recon-01 major finding on scope). Original wording: "Explains why the recurrence shows no amplification beyond univariate Lanczos behaviour on exact product measures (tensor grids, and Padua points with cubature weights below degree n_P), consistent with the flat loss and propagator response measured there (PD-T?…-107). It says nothing quantitative about near-product measures (random points in a square) beyond the qualitative coupling ratio, and nothing about non-product measures except that the factorisation fails. Λ_y is finite and depends only on μ_y; how large it is (it grows when a marginal node is captured, Paige's univariate mechanism) is not bounded here."

## Open items

(i) Perturbation version: bound the propagator for measures whose within-degree coupling is O(δ) (near-product). A weak PROVED form is PD-T?…-110, informative only near exact products (PD-T?…-112 (f)). (ii) A lower bound (growth) for a non-product example. A finite exact certificate for the dev rule on the triangle grid T_24 is PD-T?…-113; there is no all-n bound. (iii) An explicit bound for max_l |σ_l(η_b)| at nodes. (iv) The hypothesis H_δ of PD-T?…-116 (near-exact computed coefficients on product measures) is unproved. [(i)–(ii) annotated and (iv) added 2026-11-01T08:33:59+01:00, audit-01 consolidated item 5, stale pointers.]

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R02).
- 2026-10-31T23:05Z (response to reconstruction 01; verdict CONFIRMED WITH CORRECTIONS):
  - Scope (major): the idealised propagator is explained, not the loss; original wording kept in Scope.
  - Minors: the probability normalisation is made explicit; 2′ needs ‖L⁻¹‖δ ≪ 1.
  - Minor, A′_t: the definition (1 ≤ r ≤ j) excludes the coupling to (t, 0) while part 3's "equivalently" includes it. Part 3 is to be read with A′_t extended to 0 ≤ r < j, the coupling to every earlier column of the same degree.
  - Minor: recon-01 notes that the factor (n+1)² in part 2 can be (n+1). This is not re-derived here; the stated bound is valid either way.
  - Minor: part 3 is close to vacuous as a statement (a reading of part 1), agreed.
  - Part 1 is known (BPS 2010 Remark 5; PC-10).
- 2026-11-01T08:33:59+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-foundations S1 and consolidated item 5). The exact theorem (parts 1–3) and its status PROVED are unchanged.
  - S1 split: part 2′ moves to the new file PD-T?…-116 (CONDITIONAL). The Assumptions sentence on floating point moves with it. Original status row: "| 2′. same for the computed propagator in FP | CONDITIONAL | named hypothesis: computed coefficients = exact ones + O(δ) with ‖L(z)⁻¹‖·δ ≪ 1 (the second condition was added 2026-10-31, recon-01 minor); first order in δ |". Original Assumptions sentence: "Part 2 is a statement about the idealised propagator with exact coefficients; in floating point the computed coefficients differ from these by rounding-induced amounts (on tensor 41² the computed off-pattern coefficients are ≤ 7e-15 relative, `logs/r02_block_solve_growth.log`), so for the computed propagator part 2 holds to first order in that deviation (CONDITIONAL on it staying small)."
  - Status-table evidence cells are relabelled as cross-references, not claims of this file. Row 3 pointed to PD-T?…-107 (f) and quoted "1–2.5". The coupling ratios are in PD-T?…-107 (e), which reads 0.3–2.5 on the rotated squares and the triangle. Original row-3 evidence: "measured coupling ratios 1–2.5 on rotated squares and the triangle (PD-T?…-107 (f))". Original row-1 evidence: "proof below; measured: tensor 41² off-pattern within-degree coupling ≤ 7e-15".
  - Open items (i)–(ii) annotated with the later results PD-T?…-110 and -113, and (iv) added (stale pointers).
