# PD-T?bivariate-lanczos-claude-401 — L4: no operator commuting with X and Y has two consecutive graded spaces in a band Krylov sequence with a fixed number of starting vectors

Final ID: **PD-T076** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: L4 obstruction; band-Krylov non-placement; codimension obstruction; "HL is not band Lanczos for one operator"; staggered-start band Lanczos (positive placement).
Split from: none (answers plan L4-Q1).
Split into: none.

## Statement

[EXACT] Let z_1, …, z_M ∈ R² be distinct, w_i > 0, q_0 = √w/‖√w‖, X = diag(x), Y = diag(y), S_n = {p(X,Y)q_0 : p ∈ Π_n}. Write **U(d)** for: no nonzero polynomial of total degree ≤ d vanishes at all nodes.

For A ∈ R^{M×M} and V = [v_1, …, v_m] ∈ R^{M×m}, the **band Krylov sequence** of (A, V) is the chain of subspaces B_{j,i} := span{A^l v_r : 0 ≤ l < j, 1 ≤ r ≤ m} + span{A^j v_1, …, A^j v_i}, j ≥ 0, 0 ≤ i ≤ m (in exact arithmetic these are the spans of the initial segments of v_1, …, v_m, Av_1, …, Av_m, A²v_1, …, i.e. the spaces produced by band Lanczos with or without deflation; the block Krylov spaces are B_{j,0} = K_j(A, V)).

**Theorem.** Let m ≥ 1 and assume U(2m+1). If A commutes with X and Y, there is no V ∈ R^{M×m} such that both S_m and S_{m+1} belong to the band Krylov sequence of (A, V).

**Corollary 1 (frozen L4-Q1).** For every A = f(X, Y) and every fixed number m of starting vectors, the graded spaces S_0, …, S_n are not all band Krylov spaces of (A, V) once n ≥ m+1 and the nodes satisfy U(2m+1) (generic nodes with M ≥ N_{2m+1}). In particular no n-independent number of starting vectors reproduces the graded spaces of a generic node set: reproducing S_0, …, S_n needs m ≥ n starting vectors (apply the theorem with m′ = n−1).

**Corollary 2 (lower bound attained by the recurrence).** If A = αI + βX + γY with (β, γ) ≠ 0 and U(n+1) holds, every band Krylov sequence of A through S_n has m ≥ n+1 starting vectors. The window recurrence realises S_n as Σ_{a=0}^{n} K_{n−a+1}(F, v_a) with one new starting vector v_a = J q̂_{a−1,0} (orthogonalised) injected per degree, i.e. n+1 staggered starts at degree n: it is a band Krylov process for the full operator F with one start vector injected per degree, and n+1 is the minimum number of chains for any band Krylov description by an affine A.

**Remark (the commutant restriction is necessary).** For the exact orthonormal graded basis Q = [q_0, …, q_{M−1}] (U(n) for the relevant n) and any symmetric tridiagonal T with nonzero off-diagonal, A := Q T Qᵀ satisfies K_j(A, q_0) = span{q_0, …, q_{j−1}}, so every S_n is a Krylov space of A with **one** start vector. This A does not commute with X, Y and requires the output Q; hence L4-Q1 has computational content only inside the commutant {A : AX = XA, AY = YA} (= diagonal matrices = {f(X, Y)} for distinct nodes).

## Definitions

N_d = (d+1)(d+2)/2 = dim Π_d. Commutant of {X, Y}: for distinct nodes, AX = XA and AY = YA give A_{ij}(x_j − x_i) = A_{ij}(y_j − y_i) = 0, so A is diagonal; conversely every diagonal A equals f(X, Y) with f a polynomial (bivariate Lagrange interpolation on distinct nodes).

## Assumptions

Distinct nodes, w > 0, U(2m+1) for the theorem; exact arithmetic.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Lemma 1 (codimension bound for band Krylov spaces) | PROVED | below |
| Lemma 2 (one band step), Lemma 3 (chain) | PROVED (routine) | below |
| Lemma 4 (multiplier is affine) | PROVED | below |
| Lemma 5 (affine codimension n+1) | PROVED | below |
| Theorem, Corollaries 1–2 | PROVED | below |
| Remark (non-commutant reproduction) | PROVED (routine) | below |
| Transfer list (which band/block finite-precision results apply) | LITERATURE-as-reported + PROVED where stated | section "Transfer" below |

## Depends on

PD-T?bivariate-lanczos-claude-101 (graded basis, for Corollary 2's identification of the chains). No external result.

## Checks

Numerical sanity check of Lemma 5's count (codim S_n ∩ X S_n in S_n = n+1) on 400 random nodes (default_rng(3)), n ≤ 8 [corrected 2026-10-31, recon-01 minor; originally "1681 random nodes, n ≤ 10"]: see R01.md §4 (computed by principal angles between the computed spans; Runs section of R01).

## Sources

HL BIT pp. 395–398 and HL SIMAX pp. 1079–1080 for the recurrence (fulltexts read); OBST?bivariate-lanczos-claude-05 (reported heuristic) and -12 (Huhtanen reduction, reported) for context only.

## Proof or evidence

*Lemma 1.* If B = B_{j,i} with j ≥ 1 then dim B − dim(B ∩ AB) ≤ m. Indeed B = span V + A B_{j−1,i}, and A B_{j−1,i} ⊂ B ∩ AB because B_{j−1,i} ⊂ B and A B_{j−1,i} ⊂ B_{j,i}. So B ⊂ span V + (B ∩ AB).

*Lemma 2.* A B_{j,i} ⊂ B_{j+1,i} (apply A to the generators) and B_{j+1,i} = B_{j,i} + span{A^j v_{i+1}, …, A^j v_m, A^{j+1}v_1, …, A^{j+1}v_i}, so dim B_{j+1,i} ≤ dim B_{j,i} + m.

*Lemma 3.* B_{j,0} ⊂ B_{j,1} ⊂ … ⊂ B_{j,m} = B_{j+1,0}: the sequence is a chain; of two members, the one of smaller dimension is contained in the other.

*Lemma 4.* Assume U(2n+1), a ∈ R^M and diag(a) S_n ⊂ S_{n+1}. Then a_i = ℓ(z_i) for an affine ℓ. Proof: diag(a)q_0 ∈ S_{n+1} gives a_i√w_i = g(z_i)√w_i for some g ∈ Π_{n+1}, so a_i = g(z_i). Let d = deg g and suppose d ≥ 2. Then diag(a)X^n q_0 ∈ S_{n+1}: there is r ∈ Π_{n+1} with g(z_i)x_i^n = r(z_i) for all i. The polynomial g·x^n − r has degree exactly d + n (its top form is (top form of g)·x^n ≠ 0, and d + n ≥ n + 2 > deg r), d + n ≤ 2n + 1, and it vanishes at all nodes — contradicting U(2n+1).

*Lemma 5.* Assume U(n+1), n ≥ 1, ℓ affine of degree exactly 1, A = diag(ℓ(z_i)). Then dim S_n − dim(S_n ∩ AS_n) = n + 1. Proof: AS_{n−1} ⊂ S_n ∩ AS_n. Conversely, if v ∈ S_n ∩ AS_n then v = (ℓp)(X,Y)q_0 = r(X,Y)q_0 with deg p ≤ n, deg r ≤ n; ℓp − r has degree ≤ n+1 and vanishes on the nodes, so ℓp = r by U(n+1), deg(ℓp) = deg p + 1 ≤ n, i.e. deg p ≤ n − 1 and v ∈ AS_{n−1}. Multiplication by ℓ is injective on Π_{n−1} restricted to the nodes (ℓp = 0 on the nodes with deg ≤ n forces ℓp = 0 by U(n), hence p = 0), so dim AS_{n−1} = N_{n−1}; dim S_n = N_n. The codimension is N_n − N_{n−1} = n + 1.

*Theorem.* Suppose S_m and S_{m+1} are in the band Krylov sequence of (A, V), A = diag(a) (commutant). Since dim S_m = N_m > m, S_m = B_{j,i} with j ≥ 1. By Lemma 2, AS_m ⊂ B_{j+1,i} with dim B_{j+1,i} ≤ N_m + m < N_m + m + 2 = N_{m+1}; by Lemma 3, B_{j+1,i} ⊂ S_{m+1}. Hence diag(a)S_m ⊂ S_{m+1} and, by Lemma 4 (U(2m+1)), a = ℓ(z) with ℓ affine. If ℓ is constant, A = αI and every band Krylov space lies in span V, of dimension ≤ m < N_m: impossible. So deg ℓ = 1 and Lemma 5 (U(m+1)) gives dim S_m − dim(S_m ∩ AS_m) = m + 1, while Lemma 1 gives ≤ m. Contradiction.

*Corollary 1.* If S_0, …, S_n (n ≥ m+1) were all in the sequence, so would be S_m and S_{m+1}. For the "m ≥ n" form, apply the theorem with m′ := n−1 ≥ m: if m ≤ n−1, then (padding V with zero columns, which does not change the chain's spaces except for repetitions) S_{n−1} and S_n would be in a band sequence with m′ starts, contradicting U(2n−1).

*Corollary 2.* For affine nonconstant A, Lemma 5 and Lemma 1 give m ≥ n+1 whenever S_n = B_{j,i}, j ≥ 1. If instead S_n = B_{0,i} lies in the initial start block, then m ≥ i ≥ dim S_n = N_n ≥ n+1 directly. [Edge case added 2026-11-01T08:41:34+01:00, Codex audit-01 L1-foundations, reconstruction of 401.] The identification S_n = Σ_a K_{n−a+1}(F, x^a q_0) follows from PD-T?…-101, 1. (S_n = span{x^a y^b q_0}), and the recurrence's column (t, j) lies on the F-chain started at (t−j, 0). The same holds with the orthogonalised starts of the Statement, v_a = q_{(a,0)} in exact arithmetic (v_0 = q_0). F^b v_a has node values y^b p_{(a,0)}·√w, a polynomial with leading monomial x^a y^b and only earlier monomials otherwise. So the N_n vectors F^b v_a (a + b ≤ n) are triangular with respect to the monomials of Π_n and span S_n; the raw starts x^a q_0 are not needed. [Added 2026-11-01T08:41:34+01:00, same source.]

*Remark.* For tridiagonal T with nonzero off-diagonal and orthonormal Q, A = QTQᵀ maps q_k into span{q_{k−1}, q_k, q_{k+1}} with nonzero q_{k+1}-component, so K_j(A, q_0) = span{q_0, …, q_{j−1}} by induction; S_n is spanned by the first N_n columns.

## Transfer (L4-Q1 second part: which band/block finite-precision statements transfer to "Lanczos for F with injected vectors from J")

Status per item; literature items are as reported in the repository records (abstract-level unless stated).

1. **Algebraic (block) Paige identity** — transfers, re-derived here for growing blocks with one injected column per degree (PD-T?…-103, PROVED as exact algebra on the computed relations). It uses only the symmetry of F and the complete F-relations; the injected column enters through the first row of the boundary block B_F, which is (n+1)×n (not square) because one column of block n is injected rather than produced by F. The block-Paige identity of sinha-2026 (abstract-level, LIT?…-018) is the fixed/shrinking-block analogue; nothing beyond the algebraic identity is imported.
2. **Paige's local-orthogonality lemma and the ε-bounds of Paige 1976/1980** (as reported, LIT?…-003/-004) — do **not** transfer verbatim: they use the three-term structure; for the window CGS (BJ) no analogue is proved here (OPEN); for ORTH (HL) local orthogonality within the window is the standard twice-is-enough property (as reported, LIT?…-110), not re-proved.
3. **Greenbaum-type and block Greenbaum-type backward results** (greenbaum-1989, simonova-tichy-2025; conditional even for one operator, LIT?…-016/-017) — do not transfer without an injection-aware model: the injected vectors J q̂_{t−1,0} are not, for all degrees at once, in a band Krylov space of F with a start block fixed in advance (Theorem; they do lie in such spaces up to a degree) [wording narrowed 2026-10-31, recon-01 minor; originally "are not in any band Krylov space of F with a start block fixed in advance"], and the implicit J-relations carry the defect G_J (PD-T?…-102, 4.). Plan L3 owns the backward question.
4. **Block Gram–Schmidt (BCGS/BCGS2) loss-of-orthogonality bounds** (carson-et-al-2025, abstract-level, LIT?…-022/-023) — cover full (non-truncated) block orthogonalisation; the window recurrence truncates (OBST?…-07). They apply only to the intra-window step, which is a single-vector Gram–Schmidt against ≤ 2t+1 vectors; no transfer to the global loss.
5. **Bai–Day–Ye first-order ω-model** (LIT?…-013, a model, not a theorem, single operator) — transfers as a template for the F-part only; for the J-part the defect recursion (PD-T?…-102, 4.) is an additional source term (L2).
6. **Simon's semi-orthogonality theorem** (as reported, LIT?…-009) — its hypotheses involve the complete relation of one operator; it can apply to the F-section, not to the J-section (never formed) nor to the pair (L2).

## Scope

Exact arithmetic, operators in the commutant. The theorem rules out every band/block Krylov description with a fixed start block by one operator f(X, Y), including Huhtanen's single-operator reduction (OBST?…-12) whose B = q(A) has unbounded degree. It does not rule out descriptions by non-commuting operators built from the output (Remark), nor Krylov processes with **injected** starting vectors, which is exactly what the recurrence is (Corollary 2).

## Open items

None for the statement. The finite-precision consequences of the placement (which F-only theory survives the J-injection) are developed in PD-T?…-103 and R02.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R01).
- 2026-10-31T23:05Z (response to reconstruction 01; verdict CONFIRMED with minor corrections):
  - The Checks counts (400 nodes, n ≤ 8) and the transfer item 3 wording are corrected in place.
  - Corollary 2: the staggered-start description Σ_a K_{n−a+1}(F, v_a) is not a member of the B_{j,i} class of the Statement. The lower bound still applies because Lemma 1 holds for any S = span V + A B′ with B′ ⊂ S.
  - The Statement covers real A. For complex commutant elements (e.g. N = X + iY) the proof transfers verbatim over C; this is not written out.
  - The Remark's sentence "L4-Q1 has computational content only inside the commutant" is an assertion, not a proved statement.
  - Recon-01 adds its own (unaudited) extensions: a commutant + rank-r argument, and continuation schemes for affine A under U(n+2). They are recorded there and not adopted here.
  - Recon-01 also showed U(2m+1) is necessary: nodes on k lines admit band descriptions with k fixed starts.
- 2026-11-01T08:41:34+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-foundations, observations in the reconstruction of 401). The proof of Corollary 2 is completed: (i) the edge case where S_n lies in the initial start block, (ii) the identification with the orthogonalised staggered starts v_a of the Statement. Neither the Statement nor the status (PROVED) changes. The audit also confirmed both points by exact rank checks at n = 1, 2 (`audit-01/L1-foundations/independent_exact.log`). Original proof text: "For affine A, Lemma 5 and Lemma 1 give m ≥ n+1 whenever S_n = B_{j,i}, j ≥ 1. The identification S_n = Σ_a K_{n−a+1}(F, x^a q_0) follows from PD-T?…-101, 1. (S_n = span{x^a y^b q_0}), and the recurrence's column (t, j) lies on the F-chain started at (t−j, 0)."
