# PD-T?bivariate-lanczos-claude-108 — The window recurrence at a point is forward substitution for a triangular row selection of the bivariate Jacobi pencil

ID kind: PD-T.
Aliases: row-selection lemma; one-relation-per-column left inverse; propagator = inverse of the selected pencil; two-relation (block) left inverse.
Split from: none.
Split into: none.

## Statement

[Statement corrected 2026-11-01T08:33:59+01:00 (Codex audit-01, findings F1, F2); the original wording of parts 1–3 is preserved in History.]

[EXACT] Assume U(n+1) and fix the graded order and the exact orthonormal basis q_0, q_1, … of PD-T?…-101 (dev/BJ order: within degree t, (t, 0), …, (t, t) ↔ x^t, …, y^t). Let H_X, H_Y be the exact sections, (H_A)_{rl} = q_rᵀ A q_l for columns l of degree ≤ n−1 and rows r of degree ≤ n. For a point z = (x, y) ∈ R² and each column l of degree ≤ n−1 consider the two **pencil relations** (the bivariate Jacobi/three-term relations)

  ℛ^X_l(z):  x π_l − Σ_r (H_X)_{rl} π_r = 0,   ℛ^Y_l(z):  y π_l − Σ_r (H_Y)_{rl} π_r = 0,

for an unknown vector π = (π_r)_{r ⪯ (n,n)} ∈ R^{N_n}. Let C(z) ∈ R^{2N_{n−1}×N_n} be the coefficient matrix of these 2N_{n−1} **homogeneous** relations, and let L*(z) be the node-propagator matrix of PD-T?…-104 built with the exact window coefficients (row 0 = e_0ᵀ). Then:

1. For every k ≥ 1, row k of L*(z) is the negative of the row of ℛ^{A_k}_{p(k)}(z) in C(z) (A_k = X for J-products, Y for F-products); its last nonzero entry is at π_k, with coefficient β_k > 0. So L*(z) consists of the normalisation row e_0ᵀ and N_n − 1 rows of −C(z), one per column k ≥ 1 (out of the 2N_{n−1} available), and the window recurrence at z solves the square lower-triangular system L*(z)π = e_0 by forward substitution; L*(z)p(z) = e_0, and its error propagator at z is L*(z)⁻¹.
2. π = p(z) := (p_r(z))_r (orthonormal-polynomial values, p_0 = 1) satisfies **all** 2N_{n−1} homogeneous relations, identically in z: C(z)p(z) = 0. Hence C(z) has rank exactly N_n − 1 for every z, and has no left inverse on R^{N_n}. The **normalised** system [e_0ᵀ; C(z)]π = [1; 0] is consistent with the unique solution p(z); it has 2N_{n−1} + 1 rows and N_n unknowns, so it is square for n = 1 and overdetermined for n ≥ 2. If S is the row selection (with the signs of part 1) for which S[e_0ᵀ; C(z)] = L*(z), then L*(z)⁻¹S is a left inverse of the normalised system: the window recurrence is one particular triangular left inverse of it.
3. Call ℛ^A_l (A ∈ {X, Y}, deg l ≤ n−1) **admissible for** k ≥ 1 if A·lm(q_l) = lm(q_k), where lm is the leading monomial in the fixed graded order. Then the row of ℛ^A_l has its last nonzero coefficient at π_k, and that coefficient, −(H_A)_{kl}, is nonzero; conversely, a relation whose row has its last nonzero coefficient at π_k is admissible for k. Any choice, for each k ≥ 1, of one relation admissible for k — e.g. the dev rule; the fixed-order mirror rule ((t, j) ← X·(t−1, j) for j < t, (t, t) ← Y·(t−1, t−1)); or a per-degree switch between such rules — together with π_0 = 1 is another square lower-triangular system with nonzero diagonal, with the same exact solution p(z) and its own propagator (its inverse), in general different from L*(z)⁻¹. Such selections keep the fixed monomial order and the exact basis. They are not the same as exchanging the coordinate order (y-first graded Gram–Schmidt): that gives another graded basis, related to this one by an orthogonal change of basis within each degree block, and in general other value vectors. The degree condition deg l = deg k − 1 alone does not make an assignment triangular, nor even nonsingular (Remark in the proof). The two-relation block recurrence (degree block n from both X Q_{n−1} and Y Q_{n−1}, truncated to blocks n−2, n−1, orthonormal completion) uses all relations ℛ^X_l, ℛ^Y_l of degree n−1 and spans the same S_n in exact arithmetic. The particular orthonormal basis it gives for the degree-n block depends on the completion (ordering or alignment choice), and need not coincide with q_{(n,0)}, …, q_{(n,n)}.

## Definitions

Exact window coefficients: (h_k)_l = (H_{A_k})_{l,p(k)} for l ∈ W_k, β_k = (H_{A_k})_{k,p(k)}; the support of column p(k) of H_{A_k} is W_k ∪ {k} (PD-T?…-101). Orthonormal-polynomial values: q_r has node values p_r(z_i)√w_i, and p(z) = (p_r(z))_r. lm(q_l): the leading monomial of p_l in the graded order (lm(q_{(t,j)}) = x^{t−j}y^j). The graded order is a monomial order: multiplication by x or y preserves it.

## Assumptions

U(n+1), w > 0, exact arithmetic. Probability normalisation Σ_i w_i = 1, so that p_0 = 1. (Without it every statement holds with e_0 replaced by p_0 e_0 and π_0 = 1 replaced by π_0 = p_0 = (Σ_i w_i)^{−1/2}.) [Normalisation made explicit 2026-11-01T08:33:59+01:00, audit-01 F2; it was implicit in "p_0 = 1".]

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. row identification; L*(z) = [e_0ᵀ; selected rows of −C(z)]; L*(z)p(z) = e_0 | PROVED | proof below |
| 2. consistency; rank C(z) = N_n − 1; normalised system (square for n = 1, overdetermined for n ≥ 2); triangular left inverse | PROVED (routine, PD-T?…-101) | proof below; exact rank checks n = 1–4 in `directions/L1/logs/a01_exact_checks.log` |
| 3. admissible selections (criterion A·lm(q_l) = lm(q_k)), same solution; two-relation variant spans S_n | PROVED (routine) | proof below; exact checks (dev, mirror, per-degree switch, random admissible) in `a01_exact_checks.log`; stability comparison MEASURED in PD-T?…-109 |
| Remark: degree-only assignments can be non-triangular or singular | illustration by exact finite computation; not a dependency of any result | `a01_exact_checks.log`; the √5/3 coefficient was also computed independently by Codex audit-01 (`audit-01/L1-foundations/independent_exact.log`) |

## Depends on

PD-T?…-101 (supports, symmetry of the square part of H_A), PD-T?…-104 (L̂(z)).

## Checks

None needed beyond the algebra; R03's exact-coefficient propagator (`code/L1/l1_exact_propagator.py`) builds L*(z) from long-double reference coefficients. Added 2026-11-01T08:33:59+01:00 (audit-01 F1/F2): exact rational check of the corrected parts 1–3 and of the Remark, `OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py > topics/bivariate-lanczos-20261031/directions/L1/logs/a01_exact_checks.log` (Python 3.13.18, mpmath 1.3.0; 16 s; all checks pass). Codex audit-01 independently computed the F1 coefficient and the F2 ranks (`audit-01/L1-foundations/independent_exact.log`).

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

*1.* Row k of L*(z)π: β_kπ_k + Σ_{l∈W_k}(h_k)_lπ_l − a_k(z)π_{p(k)}. With the exact coefficients, Σ_{l∈W_k}(h_k)_lπ_l + β_kπ_k = Σ_r (H_{A_k})_{r,p(k)}π_r because column p(k) of H_{A_k} is supported on W_k ∪ {k}. So row k is −ℛ^{A_k}_{p(k)}(z), with last nonzero entry β_k > 0 at π_k. Row 0 of L*(z) is e_0ᵀ, which is not a pencil relation; L*(z)p(z) = e_0 follows from part 2 (rows k ≥ 1) and p_0 = 1 (row 0).
*2.* x p_l(x, y) = Σ_r (H_X)_{rl} p_r(x, y) holds as a polynomial identity for deg l ≤ n−1 because x p_l ∈ Π_{deg l+1} and the p_r (deg r ≤ n) are a basis of Π_n restricted to the nodes under U(n+1) (coefficients by orthogonality); likewise for y. So C(z)p(z) = 0, and p(z) ≠ 0 because p_0 = 1; hence rank C(z) ≤ N_n − 1. The N_n − 1 rows selected in part 1, restricted to the unknowns π_1, …, π_{N_n−1}, form a lower-triangular matrix with diagonal −β_k ≠ 0, so rank C(z) ≥ N_n − 1. Adding the row e_0ᵀ gives rank N_n, so the normalised system has at most one solution, and p(z) is one. Row count: 2N_{n−1} + 1 − N_n = (n+1)(n−2)/2 + 1, which is 0 for n = 1 and ≥ 1 for n ≥ 2. Finally L*(z)⁻¹S[e_0ᵀ; C(z)] = L*(z)⁻¹L*(z) = I.
*3.* Let ψ_l = p_l/(leading coefficient) be the monic graded orthogonal polynomials (leading monomial lm(q_l) with coefficient 1, all other monomials earlier). Then A·ψ_l (A = x or y) has leading monomial m := A·lm(q_l), with coefficient 1, and all its other monomials are earlier than m, because the graded order is a monomial order. Let k(m) be the column with lm(q_{k(m)}) = m. Under U(n) the graded Gram–Schmidt basis is triangular: span{q_r : r ⪯ k(m)} = span of the monomials ⪯ m (restricted to the nodes), and the expansion of A q_l in the q_r is unique. Hence A q_l = Σ_{r ⪯ k(m)} (H_A)_{rl} q_r, with (H_A)_{k(m),l} = ‖ψ_{k(m)}‖/‖ψ_l‖ > 0 (ratio of leading coefficients; norms over the nodes with weights w). So the row of ℛ^A_l has its last nonzero coefficient at π_{k(m)}, which proves the criterion in both directions. If every k ≥ 1 is assigned a relation admissible for k, row k has zeros after π_k and a nonzero entry at π_k. With row 0 = e_0ᵀ the square matrix is lower triangular with nonzero diagonal, hence nonsingular, and p(z) solves it by part 2. The pivots are (H_A)_{kl}, which equal the dev-rule β_k only for the dev parents. The two-relation block step spans span{X Q_{n−1}, Y Q_{n−1}} + S_{n−1} = S_n, because every degree-n monomial is x or y times a degree-(n−1) monomial.
[Proof 3 corrected 2026-11-01T08:33:59+01:00, audit-01 F1. Original: "Any selection that takes, for each k ≥ 1, a row whose new unknown is k and whose other unknowns precede k gives a lower-triangular system with nonzero diagonal (the β's), hence a left inverse; the two-relation block step spans span{X Q_{n−1}, Y Q_{n−1}} + S_{n−1} = S_n." The triangularity hypothesis was already in this proof but not in Statement 3. "The β's" is correct only for the dev parents.]

*Remark (degree-only assignments; exact finite computations, `tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py`, log `topics/bivariate-lanczos-20261031/directions/L1/logs/a01_exact_checks.log`).*
- Sheared grid (Codex audit-01 F1): nodes (a, c + a/2), a, c ∈ {−1, −1/3, 1/3, 1}, uniform weights, U(3), n = 2. Assign to the target (2, 0) the relation ℛ^X_{(1,1)}, whose parent has degree one less. This relation has coefficient (H_X)_{(2,1),(1,1)} = √5/3 at the later unknown π_{(2,1)}, because x·y = lm(q_{(2,1)}), so the selection is not triangular. Completed by the dev rows for (1,0), (1,1), (2,1), (2,2), the square system with π_0 = 1 is nonsingular there, so its solution is still p(z). It is nevertheless not a forward-substitution selection.
- The same assignment on the unsheared product grid {−1, −1/3, 1/3, 1}² (U(3)) gives a singular square system: rank 5 of 6 at all five tested points. After the degree-1 rows are substituted, ℛ^X_{(1,1)} and ℛ^Y_{(1,0)} both reduce to π_{(2,1)} = xy, so the solution is not unique.

## Scope

Reformulation: the propagator is the inverse of a triangular selection (the row e_0ᵀ and one admissible relation per column) of the normalised consistent pencil system [e_0ᵀ; C(z)]π = [1; 0], which is overdetermined for n ≥ 2 [wording corrected 2026-11-01T08:33:59+01:00, audit-01 F2; it read "of a consistent overdetermined pencil"]. On product measures the selected system decouples (PD-T?…-105). On non-product measures it does not. Its conditioning depends strongly on which selection is used (PD-N?…-105: one-relation rules differ by 10³–10⁸), and the two-relation completion removes the growth only on some sets (PD-T?…-109 (b), narrowed). Corrected 2026-10-31T23:05Z (recon-01 B1, P4); original wording: "Reformulation that locates the non-product instability: the propagator is the inverse of a triangular selection of a consistent overdetermined pencil. On product measures the selected system decouples (PD-T?…-105); on non-product measures it does not, and R03 measures that the two-relation (least-squares) completion of the same truncated pencil removes the growth on rotated squares and the disk (PD-T?…-109)."

## Open items

A bound for ‖L*(z)⁻¹‖ in terms of the pencil (a conditioning statement for triangular selections); comparison with the condition of the full stacked pencil.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R03).
- 2026-10-31T23:05Z (response to reconstruction 01): CONFIRMED as mathematics by recon-01.
  - P3 (major): Sources added (Xu / Dunkl–Xu left inverse, BPS 2010, Liu–Narayan, OTV), with the separation.
  - B1/P4: the Scope sentence "locates the non-product instability" is replaced; the selection dependence is in PD-N?…-105.
- 2026-11-01T08:33:59+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-foundations F1, F2 and the 108 reconstruction note; branch head 5f52331). Status unchanged (PROVED). The intended propagator formula and its proof are unchanged. The statement is corrected as follows.
  - F1 (part 3): the degree-only condition is replaced by the admissibility criterion A·lm(q_l) = lm(q_k), which is equivalent to "nonzero coefficient at π_k and none later". The proof of part 3 already used that condition. The mirror is now named as the fixed-order mirror rule and distinguished from exchanging the coordinate order. "A different propagator" becomes "its own propagator, in general different". The two-relation sentence now notes that the degree-n orthonormal basis depends on the completion (reconstruction note on 108). Exact counterexamples to the degree-only wording are in the Remark. Original part 3: "Any other assignment of one relation per column with a parent of degree one less (e.g. HL BIT's mirror x ↔ y, or a per-degree switch) is another triangular selection with the same exact solution p(z) and a different propagator. The two-relation block recurrence (degree block n from both X Q_{n−1} and Y Q_{n−1}, truncated to blocks n−2, n−1, orthonormal completion) uses all relations ℛ^X_l, ℛ^Y_l of degree n−1 and spans the same S_n in exact arithmetic."
  - F2 (parts 1–2): the homogeneous system C(z) has p(z) in its kernel and rank N_n − 1, so it has no left inverse. The left-inverse statement is now made for the normalised system [e_0ᵀ; C(z)], with L*(z)p(z) = e_0 and "square for n = 1, overdetermined for n ≥ 2". The probability normalisation p_0 = 1 is made explicit in Assumptions. Original part 1: "For every k ≥ 1, row k of L*(z)π = 0 is exactly the relation ℛ^{A_k}_{p(k)}(z) (A_k = X for J-products, Y for F-products), whose last unknown is π_k (coefficient β_k > 0). So the window recurrence at z selects one pencil relation per column — out of the 2N_{n−1} available — and solves the resulting lower-triangular square system by forward substitution; its error propagator at z is L*(z)⁻¹." Original part 2: "π = p(z) := (p_r(z))_r (orthonormal-polynomial values, p_0 = 1) satisfies **all** 2N_{n−1} relations, identically in z. Hence the system is consistent and overdetermined, and the window recurrence is one particular triangular left inverse of it." The original preamble also called the relations "rows of the stacked pencil [xI − H_X; yI − H_Y]"; the matrix is now named C(z) with its size.
  - Evidence: the corrected parts 1–3 were checked in exact rational arithmetic (`tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py`, log `topics/bivariate-lanczos-20261031/directions/L1/logs/a01_exact_checks.log`): the sheared 16-node grid at n = 2, a 40-node random rational set at n = 1–4, selections dev, fixed-order mirror, per-degree switch and three random admissible ones. These are discriminating checks, not a finite reduction.
  - Checks wording: "long-double exact coefficients" now reads "long-double reference coefficients". They are a high-precision computation, not exact arithmetic (L1-later note on T109's P*).
