# paige-1980-lanczos — addendum (padua-literature-20261103, P3)

Addendum to `literature/records/paige-1980-lanczos.md`. C. C. Paige, Accuracy and effectiveness of the Lanczos algorithm for the symmetric eigenproblem, Linear Algebra Appl. 34 (1980) 235–258, [doi:10.1016/0024-3795(80)90167-6](https://doi.org/10.1016/0024-3795(80)90167-6); ScienceDirect page https://www.sciencedirect.com/science/article/pii/0024379580901676 (open archive).

- Supplied location: AC's copy `~/Downloads/padua/papers/1-s2.0-0024379580901676-main.pdf` (staged as `/mnt/user-data/uploads/padua/papers/...`). Scan with OCR text layer; formulas checked on page images.
- Access and reading date: 2026-11-03.
- Reading coverage: exact journal pages 237–239 (§2: algorithm (2.1)–(2.9) and rounding-error summary (2.10)–(2.21)), 241 (Definition 1, (3.8)–(3.13)), 245–246 (Lemma 3.1, Theorem 3.1), 248 (Corollary 3.1, (3.44)–(3.47)), 250 (§4 start, Theorem 4.1). Other pages (235–236, 240, 242–244, 247, 249, 251–258) NOT read; Theorems 4.2–4.3 located by heading only.
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps: Theorems 4.2–4.3 (pp. 252–253); (3.14)–(3.21) on pp. 242–243.

## Extracted published statements

### LIT?padua-literature-claude-60 — Rounding-error hypotheses and the loss-of-orthogonality relation

- Statement in faithful paraphrase: With σ := ‖A‖₂, α := ‖|A|‖/σ and m the maximum number of nonzeros per row, the computed quantities satisfy AV_k = V_kT_k + β_{k+1}v_{k+1}e_kᵀ + δV_k with |v_jᵀv_j − 1| ≤ ε₀/2, ‖δv_j‖ ≤ σε₁, local orthogonality β_{j+1}|v_jᵀv_{j+1}| ≤ 2σε₀ and a bound on the column norms (2.11)–(2.15), assuming β_{j+1} ≠ 0, k(3ε₀ + ε₁) < 1, ε₀ = 2(n + 4)ε < 1/12, ε₁ = 2(7 + mα)ε (2.16). With R_k the strictly upper triangular part of V_kᵀV_k, T_kR_k − R_kT_k = β_{k+1}V_kᵀv_{k+1}e_kᵀ + δR_k (2.17)–(2.18), and ‖δR_k‖_F ≤ kσε₂ with ε₂ := √2 max(6ε₀, ε₁) (2.20)–(2.21). For an eigenpair (μ_i, y_i) of T_k with Ritz vector z_i = V_ky_i and last component η_{ki}, z_iᵀv_{k+1} = −ε_ii/(β_{k+1}η_{ki}) with |ε_ij| ≤ kσε₂ (3.11)–(3.13): orthogonality to v_{k+1} can be lost only along Ritz vectors whose β_{k+1}|η_{ki}| is small (stabilized ones).
- Page / theorem / equation: pp. 238–239, (2.10)–(2.21); p. 241, (3.8)–(3.13), Definition 1 (stabilization).
- Reading evidence and limitations: read on page images; (2.15) and (2.19) not transcribed.
- Relation to campaign claims (no inherited proof status): the one-operator relation that PD-T031 (growing-block Paige identity) and PD-T034 (2D ω-recurrence) generalise; one symmetric A, one start vector.

### LIT?padua-literature-claude-61 — Lemma 3.1, Theorem 3.1, Corollary 3.1, Theorem 4.1 (accuracy of stabilized Ritz values)

- Statement in faithful paraphrase: Lemma 3.1 (p. 245): for every eigenpair of T_k there are r ≤ t < k with an earlier Ritz value of T_t close to it and controlled by k²σε₂/|y_jᵀR_ky_j| ((3.33)–(3.34), p. 246). Theorem 3.1 (p. 246): if an eigenvalue μ_j of T_k is stabilized so that β_{k+1}|η_{kj}| ≤ √3 k²σε₂, then some eigenvalue of A is within (k + 1)³σε₂. Corollary 3.1 (p. 248): for the final (r, t) pair, the Ritz pair is an exact eigenpair of a matrix within 5t²σε₂ of A. Theorem 4.1 (p. 250): if n(3ε₀ + ε₁) < 1, at least one eigenvalue of T_n is within (n + 1)³σε₂ of an eigenvalue of A, with an exact eigenpair of a matrix within 5t²σε₂ of A.
- Page / theorem / equation: pp. 245–246, 248, 250.
- Reading evidence and limitations: statements read on page images; proofs partly seen, not checked.
- Relation to campaign claims (no inherited proof status): the accuracy results Greenbaum's model uses (`greenbaum-1989.addendum.md`, statement 57).

## Corrections and upgrades (old → new)

- LIT-069: UNVERIFIED (reported) → verified: (2.17)–(2.18) p. 239 and (3.11)–(3.13) p. 241 (the bound is kσε₂ divided by β_{k+1}|η_{ki}|, as the reported wording says up to notation).
- LIT-209: secondary → verified on the original, p. 241, (3.13), with |ε_ij| ≤ kσε₂ (3.12). Notation note: the INDEX row's "η_{k+1}|ζ_{kj}|" is Meurant–Strakoš notation for Paige's β_{k+1}|η_{kj}|.
- LIT-210: correct the garbled quantities: "sigma^2 u" → σε₂ with σ = ‖A‖₂ and ε₂ = √2 max(6ε₀, ε₁) ((2.10), (2.20)); "delta <= sqrt(3) m^2 sigma^2 u" → β_{k+1}|η_{kj}| ≤ √3 k²σε₂ (3.35); "(m+1)^3 sigma^2 u" → (k + 1)³σε₂ (3.36); Corollary 3.1 → 5t²σε₂ (p. 248); assumptions "m(30 + eps1) <= 1" → k(3ε₀ + ε₁) < 1 (2.16). Status: secondary → verified for Lemma 3.1, Theorem 3.1, Corollary 3.1, Theorem 4.1 (pp. 245–250); Theorems 4.2–4.3 still unread.
- Record coverage line: "the original is NOT read" → "AC copy read: pp. 237–239, 241, 245–246, 248, 250 (2026-11-03)".

## History

2026-11-03: addendum by the P3 reader (Claude Opus 5.5 high), padua-literature-20261103; AC-supplied PDF.
