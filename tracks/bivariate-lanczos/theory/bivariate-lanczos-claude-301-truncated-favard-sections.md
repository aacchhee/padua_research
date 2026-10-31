# PD-T?bivariate-lanczos-claude-301 — Truncated Favard theorem for degree-n sections

ID kind: PD-T.
Aliases: section–functional correspondence; consistent sections; interior commutativity conditions; "sections determine moments up to degree 2n+1"; words formula; route (iii) of L3-Q1 (Xu block-Jacobi commutativity with the last block free).
Split from: none (supporting result for PD-T?bivariate-lanczos-claude-300, the L3-Q1 target).
Split into: none.

## Statement

Fix n ≥ 1, N = N_n = dim Π_n = (n+1)(n+2)/2, and the graded order of plan.md (degree, then x-exponent ascending; index (k,s) ↔ x^s y^{k−s}). Call a pair (H_x, H_y) of real symmetric N × N matrices **structured** if both are block tridiagonal with diagonal blocks of sizes 1, 2, …, n+1 and the off-diagonal blocks A_{k,x} := (H_x)_{k,k+1}, A_{k,y} := (H_y)_{k,k+1} ((k+1) × (k+2), k = 0..n−1) satisfy
 (A_{k,x})_{s,t} = 0 for t > s+1, (A_{k,x})_{s,s+1} > 0; (A_{k,y})_{s,t} = 0 for t > s, (A_{k,y})_{s,s} > 0.

(a) [Sections of functionals.] Let L be a linear functional on Π_{2n+1} with moment matrix M_n(L) = [L(m_a m_b)]_{a,b ≤ N} positive definite, and p_a (a = (k,s)) its graded Gram–Schmidt orthonormal polynomials (leading coefficient of x^s y^{k−s} positive). Then Φ(L) := (H_x, H_y), (H_x)_{ab} = L(x p_a p_b), (H_y)_{ab} = L(y p_a p_b), is structured, and the commutator [H_x, H_y] vanishes outside the last diagonal block (n,n).

(b) [Converse, uniqueness, explicit inverse.] Conversely, if (H_x, H_y) is structured and [H_x, H_y] vanishes outside the block (n,n) ("interior commutativity conditions"), then there is exactly one functional L on Π_{2n+1} with L(1) = 1 and M_n(L) ≻ 0 such that Φ(L) = (H_x, H_y). It is given by the **words formula**
 L(x^a y^b) = e_0ᵀ w(H_x, H_y) e_0 for any word w containing a letters H_x and b letters H_y, a + b ≤ 2n+1
(the value does not depend on the word).

(c) Φ is a bijection from {L : L(1) = 1, M_n(L) ≻ 0} onto the set 𝒞_n of structured pairs satisfying the interior commutativity conditions; Φ is real-analytic and Φ^{-1} is polynomial in the matrix entries. Hence 𝒞_n is a real-analytic manifold of dimension dim Π_{2n+1} − 1 = (n+1)(2n+3) − 1, and Φ, Φ^{-1} are locally Lipschitz. Sections are invariant under L ↦ cL (c > 0).

(d) [Computed entries.] The truncated recurrence (HL/BJ order: y-product only for the first vector of each degree) forms all structured entries of H_x and only the columns (k,0) of H_y. These computed entries determine L (hence all of H_y) when consistent; they exceed dim Π_{2n+1} − 1 by e_n = 1, 6, 17, 36, 65, 106, 161, 232, 321, 430 for n = 1..10 (count, see Checks), so in exact arithmetic they satisfy e_n polynomial consistency relations.

## Definitions

Π_d: real bivariate polynomials of total degree ≤ d; m_a monomials in graded order; e_a standard basis vectors of R^N indexed like m_a. A measure μ = Σ w_i δ_{z_i} with M_n(L_μ) ≻ 0 has sections Φ(L_μ) = QᵀXQ, QᵀYQ (Q = [√w_i p_a(z_i)]), matching plan.md.

## Assumptions

Exact arithmetic [EXACT]; n ≥ 1; the fixed graded order above (any fixed monomial order compatible with multiplication works with the obvious change of the echelon pattern).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) structure and commutator support | PROVED | proof below; exact rational check `favard_check.py` Part A |
| (b) converse, uniqueness, words formula | PROVED | proof below; FP check of words formula (`favard_check.py` Part B, rel. err ≤ 5.3e-15, n ≤ 4) |
| (c) bijection, smoothness, dimension | PROVED (routine from (a), (b)) | proof below |
| (d) count e_n | PROVED (counting; routine) | `favard_check.py` Part C |

## Depends on

None beyond linear algebra. Xu SIAM J. Math. Anal. 25 (1994), eqs. (2.5)–(2.7), p. 993 (record `xu-siam-1994`, LIT?…-144) states the infinite-sequence commuting conditions as consequences of orthogonality; the present finite version is proved here and does not rely on that paper or on the Favard theorem it cites.

## Checks

- `tracks/bivariate-lanczos/code/L3/favard_check.py 4 0` (sha256 in `directions/L3/logs/code_sha256.txt`), output `directions/L3/logs/favard_check.log`: for n = 1..4, exact rational arithmetic: C := G_x G⁻¹ G_y − G_y G⁻¹ G_x (G = M_n(L), G_x = [L(x m_a m_b)], G_y) has zero rows/columns of degree < n and a nonzero (n,n) block, both for a random rational 3-more-than-D-point measure and for a random rational functional (not a measure). Since [H_x, H_y] = R^{−T} C R^{−1} with G = RᵀR (R upper triangular), this is (a). Words formula: max relative error 1.95e-16 … 5.33e-15 (FP, MEASURED sanity check of (b)). Counts as in (d). Environment: Python 3.13.18, numpy 2.5.3.
- Independent rerun: pending (Runs needed in R01).

## Sources

`xu-siam-1994` (fulltext read by the literature agent; eqs. (2.2)–(2.7) p. 993; Favard theorem only cited there). No source is used as a proof.

## Proof or evidence

(a) Write p_a = c_a m_a + (lower monomials), c_a > 0. Block tridiagonality: x p_a has degree deg a + 1, and p_b ⊥ Π_{deg b − 1}. Echelon pattern: x p_{(k,s)} ∈ span{m ≤ x^{s+1} y^{k−s}} (the order is a monomial order), and p_{(k+1,t)} ⊥ span{m < x^t y^{k+1−t}}; so (A_{k,x})_{s,t} = 0 for t > s+1 and (A_{k,x})_{s,s+1} = c_{(k,s)}/c_{(k+1,s+1)} > 0. Same for y with t > s. Commutator: for deg a ≤ n−1, x p_a ∈ Π_n, so x p_a = Σ_{c ≤ N} L(x p_a p_c) p_c, hence Σ_c (H_x)_{ac}(H_y)_{cb} = L(y p_b · x p_a) (degree ≤ 2n+1, so defined), and likewise Σ_c (H_y)_{ac}(H_x)_{cb} = L(x p_b · y p_a). Thus ([H_x,H_y])_{ab} = 0 whenever deg a ≤ n−1; by skew-symmetry also whenever deg b ≤ n−1.

(b) Let W be a word in H_x, H_y and |W| its length. Block tridiagonality gives W e_0 ∈ span{e_c : deg c ≤ |W|}. (i) For |W| ≤ 2n+1, e_0ᵀ W e_0 depends only on the letter content: an adjacent transposition W = U H_x H_y V → U H_y H_x V changes the value by (Uᵀe_0)ᵀ[H_x,H_y](V e_0) with Uᵀ e_0 of degree ≤ |U|, V e_0 of degree ≤ |V|, |U| + |V| ≤ 2n−1, so one of them has degree ≤ n−1 and the term vanishes by the support of the commutator. Define L(x^a y^b) by the words formula. (ii) Define π : Π_n → R^N on monomials by π(x^a y^b) = W e_0 (any word with that content, length a+b ≤ n), extended linearly; well defined because a transposition changes W e_0 by U[H_x,H_y]V e_0 with deg(V e_0) ≤ |V| ≤ n−2 and the columns of [H_x,H_y] of degree ≤ n−1 vanish. By the echelon pattern with positive pivots, π(m_{(k,s)}) = γ_{(k,s)} e_{(k,s)} + (span of e_c, c before (k,s)), γ > 0 [induction: m_{(k,s)} = x m_{(k−1,s−1)} for s ≥ 1, m_{(k,0)} = y m_{(k−1,0)}; column c = (j,t) of H_x meets degree j+1 only in rows (j+1,t′), t′ ≤ t+1, with positive entry at t′ = t+1; similarly for H_y]. So π is a triangular bijection. (iii) For p, q ∈ Π_n: π(p)ᵀπ(q) = L(pq) (reversed word of p followed by word of q, length ≤ 2n; H symmetric). Hence M_n(L) = Gram matrix of π(m_a) ≻ 0, and p̃_a := π^{-1}(e_a) are L-orthonormal with leading monomial m_a and positive leading coefficient, i.e. the graded Gram–Schmidt basis of L. (iv) (H_x)_{ab} = e_aᵀ H_x e_b = π(p̃_a)ᵀ H_x π(p̃_b) = L(x p̃_a p̃_b) by the words formula (length ≤ 2n+1); same for H_y. So Φ(L) = (H_x, H_y). L(1) = e_0ᵀe_0 = 1. Uniqueness: let L′ (L′(1) = 1, M_n(L′) ≻ 0) have orthonormal basis p′_a (p′_0 = 1) and sections (H′_x, H′_y), and let c(p) be the coefficient vector of p ∈ Π_n in that basis. For p ∈ Π_{n−1}, c(xp) = H′_x c(p) and c(yp) = H′_y c(p) (expand x p ∈ Π_n), so c(x^α) = W_α e_0; then L′(x^α x^β) = c(x^α)ᵀc(x^β) and L′(x^α · x · x^β) = c(x^α)ᵀ H′_x c(x^β) for |α|, |β| ≤ n, which covers every monomial of degree ≤ 2n+1. So every such L′ equals the words formula of its own sections, and Φ(L′) = Φ(L) forces L′ = L.

(c) (a)+(b) give the bijection; Φ is analytic (Cholesky of M_n(L) and rational operations), Φ^{-1} is polynomial (words formula). Dimension = number of free moments minus normalisation.

(d) Count of structured entries of H_x (B_{k,x}: (k+1)(k+2)/2; A_{k,x}: Σ_s min(s+2, k+2)) plus computed y-entries (column (k,0) of B_{k,y}: k+1; column 0 of A_{k,y}: k+1), minus (dim Π_{2n+1} − 1). That these entries determine L: the recurrence reconstructs p_{(k+1,0)} from y p_{(k,0)} and p_{(k+1,s+1)} from x p_{(k,s)} (divisions by positive pivots), orthonormality gives L on Π_{2n}, B_{n,x} gives the degree-(2n+1) moments with x-exponent ≥ 1 and (B_{n,y})_{0,0} gives y^{2n+1}.

## Scope

Exact correspondence between consistent sections and functionals on Π_{2n+1}. It does not say which functionals are moment functionals of positive measures (that is PD-T?…-302/303). "Interior commutativity conditions" in plan.md L3-Q1 are, by this theorem, exactly the vanishing of [H_x,H_y] outside the block (n,n); the (n,n) block κ := ([H_x,H_y])_{nn} (skew, (n+1) × (n+1)) is "the free last block".

## Open items

Floating-point consistency defect of the computed entries (the e_n relations) after loss of orthogonality is not addressed (L1-dependent; see R01 next question).

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab8348be80a6f16f69ee7ef9c7bb66ed42e: created in round R01.
