# PD-T?bivariate-lanczos-claude-108 — The window recurrence at a point is forward substitution for a triangular row selection of the bivariate Jacobi pencil

ID kind: PD-T.
Aliases: row-selection lemma; one-relation-per-column left inverse; propagator = inverse of the selected pencil; two-relation (block) left inverse.
Split from: none.
Split into: none.

## Statement

[EXACT] Assume U(n+1) and let H_X, H_Y be the exact sections, (H_A)_{rl} = q_rᵀ A q_l for columns l of degree ≤ n−1 and rows r of degree ≤ n. For a point z = (x, y) ∈ R² and each column l of degree ≤ n−1 consider the two **pencil relations** (the bivariate Jacobi/three-term relations, rows of the stacked pencil [xI − H_X; yI − H_Y])

  ℛ^X_l(z):  x π_l − Σ_r (H_X)_{rl} π_r = 0,   ℛ^Y_l(z):  y π_l − Σ_r (H_Y)_{rl} π_r = 0,

for an unknown vector π = (π_r)_{r ⪯ (n,n)}. Let L*(z) be the node-propagator matrix of PD-T?…-104 built with the exact window coefficients. Then:

1. For every k ≥ 1, row k of L*(z)π = 0 is exactly the relation ℛ^{A_k}_{p(k)}(z) (A_k = X for J-products, Y for F-products), whose last unknown is π_k (coefficient β_k > 0). So the window recurrence at z selects one pencil relation per column — out of the 2N_{n−1} available — and solves the resulting lower-triangular square system by forward substitution; its error propagator at z is L*(z)⁻¹.
2. π = p(z) := (p_r(z))_r (orthonormal-polynomial values, p_0 = 1) satisfies **all** 2N_{n−1} relations, identically in z. Hence the system is consistent and overdetermined, and the window recurrence is one particular triangular left inverse of it.
3. Any other assignment of one relation per column with a parent of degree one less (e.g. HL BIT's mirror x ↔ y, or a per-degree switch) is another triangular selection with the same exact solution p(z) and a different propagator. The two-relation block recurrence (degree block n from both X Q_{n−1} and Y Q_{n−1}, truncated to blocks n−2, n−1, orthonormal completion) uses all relations ℛ^X_l, ℛ^Y_l of degree n−1 and spans the same S_n in exact arithmetic.

## Definitions

Exact window coefficients: (h_k)_l = (H_{A_k})_{l,p(k)} for l ∈ W_k, β_k = (H_{A_k})_{k,p(k)}; the support of column p(k) of H_{A_k} is W_k ∪ {k} (PD-T?…-101).

## Assumptions

U(n+1), w > 0, exact arithmetic.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. row identification | PROVED | proof below |
| 2. consistency / overdetermination | PROVED (routine, PD-T?…-101) | |
| 3. other selections; two-relation variant spans S_n | PROVED (routine) | stability comparison MEASURED in PD-T?…-109 |

## Depends on

PD-T?…-101 (supports, symmetry of the square part of H_A), PD-T?…-104 (L̂(z)).

## Checks

None needed beyond the algebra; R03's exact-coefficient propagator (`code/L1/l1_exact_propagator.py`) builds L*(z) from long-double exact coefficients.

## Sources

Added 2026-10-31T23:05Z, recon-01 major finding P3; PC-7, PC-9. The algebra is known; no novelty is claimed for it.
- In block form, the window recurrence is Xu's recurrence formula with one particular left inverse of the stacked block A_{n−1} = [A_{n−1,1}; A_{n−1,2}]. The left-inverse form is textbook: Dunkl–Xu Thm 3.2.5, as cited by Barrio–Peña–Sauer 2010 p. 412 (Dunkl–Xu not read by me); Xu's survey arXiv 1701.02709 §2.2 eq. (2.14); Liu–Narayan 2023 Thm 3.1; Olver–Townsend–Vasil 2019 §2.3 (the last three as reported by the prior-art check).
- Barrio–Peña–Sauer, J. Approx. Theory 162 (2010) 407–420, fulltext read pp. 409–410, 413, 418–419 (scratchpad only), give:
  - the one-variable-per-polynomial recurrence, eq. (5), with a free choice of variable;
  - the assembled form and the all-relations average, eq. (6) and Thm 8;
  - Remark 9: the choice affects numerical behaviour;
  - §5: point-dependent selection heuristics;
  - (18)–(20): Clenshaw evaluation as block triangular substitution, with a forward bound in a comparison-matrix inverse.
  They are the closest predecessor of parts 1 and 3.
- Separation: BPS work with monic OPs, where A_{n,j} is a 0/1 shift and the selected system has no within-degree coupling. Here the basis is the strongly orthogonal graded-lex one, whose selected block is lower triangular with coupling. The setting is discrete-measure Lanczos vectors with window truncation, and the selection is linked to loss of orthogonality (PD-T?…-104, -106, PD-N?…-105). BPS report no experiments.

## Proof or evidence

*1.* Row k of L*(z)π: β_kπ_k + Σ_{l∈W_k}(h_k)_lπ_l − a_k(z)π_{p(k)}. With the exact coefficients, Σ_{l∈W_k}(h_k)_lπ_l + β_kπ_k = Σ_r (H_{A_k})_{r,p(k)}π_r because column p(k) of H_{A_k} is supported on W_k ∪ {k}. So row k is −ℛ^{A_k}_{p(k)}(z).
*2.* x p_l(x, y) = Σ_r (H_X)_{rl} p_r(x, y) holds as a polynomial identity for deg l ≤ n−1 because x p_l ∈ Π_{deg l+1} and the p_r (deg r ≤ n) are a basis of Π_n restricted to the nodes under U(n+1) (coefficients by orthogonality); likewise for y.
*3.* Any selection that takes, for each k ≥ 1, a row whose new unknown is k and whose other unknowns precede k gives a lower-triangular system with nonzero diagonal (the β's), hence a left inverse; the two-relation block step spans span{X Q_{n−1}, Y Q_{n−1}} + S_{n−1} = S_n.

## Scope

Reformulation: the propagator is the inverse of a triangular selection of a consistent overdetermined pencil. On product measures the selected system decouples (PD-T?…-105). On non-product measures it does not. Its conditioning depends strongly on which selection is used (PD-N?…-105: one-relation rules differ by 10³–10⁸), and the two-relation completion removes the growth only on some sets (PD-T?…-109 (b), narrowed). Corrected 2026-10-31T23:05Z (recon-01 B1, P4); original wording: "Reformulation that locates the non-product instability: the propagator is the inverse of a triangular selection of a consistent overdetermined pencil. On product measures the selected system decouples (PD-T?…-105); on non-product measures it does not, and R03 measures that the two-relation (least-squares) completion of the same truncated pencil removes the growth on rotated squares and the disk (PD-T?…-109)."

## Open items

A bound for ‖L*(z)⁻¹‖ in terms of the pencil (a conditioning statement for triangular selections); comparison with the condition of the full stacked pencil.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R03).
- 2026-10-31T23:05Z (response to reconstruction 01): CONFIRMED as mathematics by recon-01.
  - P3 (major): Sources added (Xu / Dunkl–Xu left inverse, BPS 2010, Liu–Narayan, OTV), with the separation.
  - B1/P4: the Scope sentence "locates the non-product instability" is replaced; the selection dependence is in PD-N?…-105.
