# L1 (+L4) — Direction summary after R07 (2026-10-31)

> Orchestrator note: saved by the orchestrator from the L1 developer's hand-back text (the developer's file write was blocked by the tool). Content is the developer's, lightly formatted. **Correction:** the setting line originally named the recurrence "Brezinski–Jelassi 1985"; the correct attribution is **Bartels–Jezioranski 1985** (record `bartels-jezioranski-1985`). Nothing else changed.

Developer: Claude Opus 5.5, xhigh. 7 of 10 rounds used. IDs are provisional (PD-T?bivariate-lanczos-claude-1nn = PD-T?…-1nn). All statuses are the developer's own; at the time of writing nothing from R04–R07 has been independently reconstructed (reconstruction 01 of R01–R03 in progress). No novelty is claimed (prior art in §3).

## Setting

- Recurrence: the truncated bivariate window recurrence (Bartels–Jezioranski 1985 / Huhtanen–Larsen BIT 2002) for X = diag(x), Y = diag(y).
- BJ ordering: column (t,j) ↔ x^{t−j}y^j. Column (t,0) = X·(t−1,0) (the injecting operator J); column (t,j≥1) = Y·(t−1,j−1) (the full operator F). HL is the mirror image.
- Windows: block (degrees t−2..t) or exact. Orthogonalisation: CGS for BJ; MGS with conditional reorthogonalisation for HL.
- u = 2^-52. Loss = max|Q̂_nᵀQ̂_n − I|. MEASURED = floating-point experiment only.

## 1. Surviving claims, ranked

1. **Ritz residuals do not govern the loss off product-aligned supports (frozen L1-Q1).** PD-N?…-101 [MEASURED]: on non-product supports BJ and HL loss exceeds u/ρ_O by 10²–10¹⁴ for O = H_x, H_y, Z, an oblique section and N_k (R01 main sets, seed-11 rotations by 0.3 and π/4, disk, triangle; PC-1 restricts the range). On the tensor grid 41² single sections over-predict by ~10¹³. PD-T?…-107 (a,b) [MEASURED, PC-2]: Ritz-type loss on product-aligned sets; on non-product sets exponential growth from n ≈ 8–12, scaling with u, independent of Ritz convergence (onset near n = 18 for a 0.05 rotation). Frozen kill criteria K1 and K2 both fired.
2. **L4 obstruction (frozen L4-Q1).** PD-T?…-401 [PROVED]: assume distinct nodes and U(2m+1). If A commutes with X and Y, no V ∈ ℝ^{M×m} puts both S_m and S_{m+1} in the band Krylov sequence of (A, V). Corollaries: S_0..S_n needs m ≥ n starts; affine A needs m ≥ n+1, attained by injecting one start per degree. The commutant restriction is necessary (A = QTQᵀ works with one start but needs the output Q).
3. **Non-product amplification is a priori, certified on one grid.** PD-T?…-109 [MEASURED]: exact-coefficient propagator responds to u/√M forcing like the computed one to the printed digit (square, π/4 rotation, disk, triangle; M = 1681); triangle loss at n = 16 ranges 1.9e-9–6.8e-3 with orientation. PD-T?…-113 part 1 [PROVED]: impulse identity ((L*(z))⁻¹)_{k,s}² = ‖ψ_{p(s)}‖² g_k(z)² / ‖ψ_k‖². Part 2 [CONDITIONAL on independent rerun]: exact rational certificate log₁₀G(12) − log₁₀G(6) = 8.69 on T_24 vs 0.80 on Q_24; descriptive runs on T_40, Q_40, rotated Q_24.
4. **Product factorisation.** PD-T?…-105 part 2 [PROVED; IDEALIZED: exact coefficients]: on tensor grids the propagator factorises into univariate impulse responses ρ^{[s]}_j = b_s(r_{s−1}σ_j − σ_{s−1}r_j); all amplification univariate. Part 1 is known (PC-10, BPS Remark 5). PD-T?…-111 [PROVED]: moment matching on Π_{2n} ⇒ product-type coefficients and factorisation; ordered Harris–Simanek checkerboards with weights 1/|ω′_Xω′_Y| satisfy μ_e = ½ μ_X⊗μ_Y on Π_{2m} (proved independently via divided differences); Padua with cubature weights is the Chebyshev–Lobatto case.
5. **Coefficient channel.** PD-T?…-114 parts 1–4 [PROVED]: at a product-type c* (moments matched on Π_{2n}), ∂(ΞᵀΞ)/∂h_{k,l} = −(A + Aᵀ) with explicit univariate formulas (for j ≥ 1: A_{(a,b),(t+r,j+r)} = δ_{a−b,i_l}⟨r_b, r_{j_l}G^{y,[j]}_{j+r}⟩; for j = 0: A = ⟨p_{a−b}, p_{i_l}G^{x,[t]}_{i′}⟩⟨r_b, r_{j_l}r_r⟩); on-pattern entries give univariate derivatives, off-pattern entries cross-variable ones. Part 5 [MEASURED]: formula check 1e-14; clustered gains on-pattern ≤ 5e3, off-pattern up to 1e14; first-order prediction reproduces the loss. PD-T?…-115 [MEASURED]: BJ off-pattern values are feedback-dominated and sign-structured (random signs 10³×; φ and ρ cancel); open-loop estimates over-estimate (PD-N?…-104); closed-loop model (dot-product rounding only) gives C/L ∈ [0.23, 1.06] on four clustered sets, flat on controls.
6. **Paige-type identities [PROVED].** PD-T?…-102 (routine): local relations; computed F-pattern = exact support; one J-column formed per degree; exact defect recursion. PD-T?…-104: node rows ξ^{(i)} = ξ^{(i)}_0 p̂(z_i) − L̂(z_i)⁻¹φ^{(i)}; commutator residual C_res = JQ̂ − Q̂Ĥ_J satisfies an exact F-marching with clamped J-columns. PD-T?…-106: exact ω-recurrence (F-sources local; J-sources add the commutator). PD-T?…-103: growing-block bilinear Paige identity sᵀcBs = sᵀΩs − sᵀ(R − Rᵀ)ρ with Ω local, plus a Ritz corollary — a variant of a known identity (PC-8, Sinha 2026).
7. **Row selection.** PD-T?…-108 [PROVED; algebra classical (PC-7, PC-9; BPS 2010)]: row k of L*(z)π = 0 is the pencil relation ℛ^{A_k}_{p(k)}; the recurrence is forward substitution for one triangular selection of 2N_{n−1} consistent relations, the propagator is that selection's inverse; other selections have the same solution but different propagators; the two-relation recurrence uses all relations.
8. **Exact coefficient pattern.** PD-T?…-101 [PROVED]: supports of F- and J-columns; formed vs implicit entries; implicit J-columns fixed by commutativity; HL SIMAX section = Z.
9. **Near-product bound.** PD-T?…-110 [PROVED]: ‖(L*⁻¹)_{[t],[s]}‖ ≤ ‖D_s⁻¹‖ K Π(1 + Kε_r); informative only near exact products (0.4 decades on the tensor grid; 10–28 decades otherwise).
10. **Measurements.** PD-T?…-112 [MEASURED; with PC-11, PC-12]: checkerboard losses (Chebyshev–Lobatto flat, equispaced mild, cubic strong); split Q̂ = Ξ̄ − Φ̃ into vector vs coefficient channel; two-relation control fails on the clustered set; rotation sweep. PD-T?…-107 (c–f) [MEASURED, PC-3]: propagator predictor works for the vector channel only (1–5×; not on the triangle or strongly non-uniform weights); block-Paige identity controls ≤ 47%. PD-N?…-102 [MEASURED]: HL SIMAX windowed (N, N*) form grows like ~3ⁿ from n ≈ 6.

## 2. Failed routes

Ritz governance, single or joint (PD-N-101); windowed HL SIMAX form (PD-N-102); H_lin (PD-N-103a); universal propagator predictor (PD-N-103b, PC-3); two-relation recurrence as an unconditional remedy (PD-N-103c, PC-4); open-loop coefficient-noise estimates (PD-N-104: generic noise 10⁶–10⁷ over, random signs 10³, term-wise estimate killed on quartic clustering 119×); block-Paige identity as a control (≤ 47%); near-product bound away from exact products; local Gram–Schmidt as the cause of the clustered loss (CGS2 and ORTH show it too).

## 3. Prior-art separations

What was read: BPS 2010 fulltext pp. 409–410, 413, 418–419 (scratchpad only); Zaccaron 2014 via the prior-art check's WebFetch (locators to re-check); Liu–Narayan 2023 via review L1-prior-art-01 and abstract; Sinha 2026 WebFetch summary of the introduction only (Theorem 7 not seen); Xu survey and OTV via the prior-art check.

- **BPS, JAT 162 (2010) 407–420.** Closest predecessor of items 7 and 6/104 in the evaluation setting: eq. (5) one variable per monic polynomial; eq. (6)/Thm 8 averaged form; Remark 9 (choice matters numerically); §5 heuristics; (18)–(20) triangular substitution with comparison-matrix bounds; Remark 5 product case (so 105 part 1 is known). Separation (not in the pages read): discrete-measure Lanczos with window truncation; propagator → loss link (104, 106); certified dichotomy of non-product amplification (107, 109, 113) vs factorisation (105 part 2, 111); coefficient channel (114, 115).
- **Zaccaron 2014.** Prior art for the bare geometry dependence (Tables 2.1–2.2). Separation: product principle independent of Ritz convergence; factorisation on product and moment-matching measures; a-priori property (109); certificate (113).
- **Liu–Narayan SISC 45(3) 2023.** Predecessor of the two-relation control (block Stieltjes); Thm 3.1 with Xu §2.2 and OTV §2.3 gives the stacked system of 108. Separation: equal-truncation comparison (R03, 109b); its failure on clustered checkerboards (103c).
- **Sinha 2026.** Block Paige identity has the content of the 103 corollary for one operator. Separation: 103 is a variant (growing blocks, bilinear complex form, commutator error term); its E^inj is a selector, not injected starts (summary only).
- Classical: the univariate variation through associated solutions used in 114.

## 4. Development briefs

1. **PD-N-101 / 107ab.** Needs M = 10⁵–10⁶ (syvert), a quantitative notion of "product-aligned" (107e coupling ratio), and a theorem that the Ritz mechanism is the only one at product-type points (105 + univariate Paige). Fold in PC-1, PC-2.
2. **401.** Ready for reconstruction. Next: what deflated band Lanczos with n-growing starts achieves; relate to the Xu and HL Krylov characterisations.
3. **109 / 113.** First an independent (SymPy or fraction-free) rerun of the certificate; then an all-n lower bound on T_m via monic impulse responses (measured ≈ 1.4 decades² per degree, independent of m); then a quantitative propagator → loss link.
4. **105 part 2 / 111.** Ready for reconstruction (cite BPS Remark 5). Next: an [FP] version on tensor and Padua-cubature sets via 104 + univariate Paige, controlling the off-pattern channel (114), which is benign there.
5. **114 / 115.** 114 ready for reconstruction. Open: damping of the closed loop δh = ρ + Tδh (T strictly lower triangular, computable from c*, Ξ*); a proof or measurement that (I − T)⁻¹ damps the high-gain directions gives an exact-data loss estimate. Runs: m = 40–60, exponents 1.5–5, HL, BLAS-level rounding. Further: off-pattern gains at non-product points (links to item 3).
6. **102–104, 106.** Ready for reconstruction. Next: an [FP] loss bound in max_z‖L̂(z)⁻¹‖ plus the commutator residual — not Ritz-like (item 3), must include the coefficient channel (item 5). Cite 103 as a variant of Sinha's identity.
7. **108.** Keep as a framing lemma. Value-adding question (for L2): which selection minimises max_z‖L*(z)⁻¹‖? (Triangle orientation effect: 6 decades.)
8. **101** ready; **110** needs a better reference measure; measured parts (112, 107c–f, PD-N-102) need reruns.

## 5. Hand-off to L2 (not developed)

Two-relation recurrence fails on clustered checkerboards; the relation choice per column has a 6-decade effect; zeroing off-pattern entries removes the coefficient channel (R06: 3e-15 at n = 16) but only when the product structure is known; untested: compensated or extra-precision window dot products would shrink ρ, which drives the closed loop.

## 6. Runs needed

Certificate rerun; M = 10⁵–10⁶ on syvert0/1/2; m = 40–60 graded checkerboards, HL, ORTH; independent reruns of all MEASURED tables.
