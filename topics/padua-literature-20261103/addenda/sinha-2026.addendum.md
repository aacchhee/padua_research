# sinha-2026 — addendum (padua-literature-20261103, P3)

Addendum to `literature/records/sinha-2026.md`. M. Sinha, Finite-precision symmetric Krylov methods: exact rounding examples, block Paige identities, and a variable-block Lanczos model, [arXiv:2609.08066](https://arxiv.org/abs/2609.08066) (v1, 8 Sep 2026). No DOI, no journal version (`p3-links.md` item 10b).

- Access and reading date: 2026-11-03 (pdf.js in the built-in browser; 57 PDF pages).
- Reading coverage: exact PDF pages 1 (abstract, start of §1), 27 (start of §7), 37–39 (§7.4: normalisation (90)–(102), Theorem 6), 42 (Theorem 7), 45 (Theorem 8), 49 (start of §9). Main-theorem statements only, as assigned. Proofs and §§2–6, 7.1–7.3, 7.5, 7.7–8 NOT read.
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps: Lemma 4 and the local bounds of §7.2 that feed (90)–(102); Corollary 4 relation (54) (LIT-286) not re-read.

## Extracted published statements

### LIT?padua-literature-claude-64 — Theorem 6: exact block Lanczos relation for I_k ⊗ A + Δ (augmented model)

- Statement in faithful paraphrase: Let A be real symmetric, T symmetric block tridiagonal with positive block sizes r₁, …, r_k (m = Σr_i), and suppose AV = VT + WHE_kᵀ + F with normalised blocks (V_iᵀV_i = I, WᵀW = I). With U the strictly block-upper part of VᵀV − I, a = VᵀW, M = TU − UᵀT − aHE_kᵀ, e = ‖F‖, ζ the largest diagonal block of M and μ = k·max{2e, ζ}, there are V̂ (orthonormal columns), Ŵ and a symmetric Δ on R^{nk} with (I_k ⊗ A + Δ)V̂ = V̂T + ŴHE_kᵀ, first block of V̂ equal to (V₁, 0, …, 0), and ‖Δ‖ ≤ 2(2√k e + 4√k(√k + k − 1)μ). The paper introduces the construction after recalling Greenbaum's enlarged exact problem and Paige's augmented Hermitian model (p. 38; the sentence naming the source of the adapted definitions was cut off in the text read).
- Hypotheses and notation: the computed block recurrence is renormalised (eqs. (90)–(93)) under δ = max‖Ṽ_iᵀṼ_i − I‖ < 1/2; block sizes come from Householder orthogonalisation with singular-value truncation, so they can shrink under rank deflation (§7, p. 27).
- Page / theorem / equation: §7.4 pp. 37–39, eqs. (90)–(107), Theorem 6 p. 39.
- Reading evidence and limitations: statement read; proof not read.
- Relation to campaign claims (no inherited proof status): a one-operator backward model in dimension nk with Δ of local-error size; no spectral-interval or measure statement; no several-operator or injected-start content.

### LIT?padua-literature-claude-65 — Theorems 7–8: block Paige identities and extra Ritz values from overlap

- Statement in faithful paraphrase: Under (92), for eigenpairs (θ_i, s_i) of T, lifted Ritz vectors y_i = Vs_i, boundary residual coordinates w_i = HE_kᵀs_i and lost orthogonality g_i = Wᵀy_i: g_iᵀw_i = −s_iᵀMs_i, hence |g_iᵀw_i| ≤ ‖M‖ ≤ μ, and for i ≠ j a relation for (θ_j − θ_i)y_jᵀy_i with a bound on |y_jᵀy_i| (Theorem 7, (119)–(121)). Theorem 8 counts at least d + t eigenvalues of T in an interval around c from the overlap of earlier Ritz directions (Gram-matrix argument, (126)–(130)).
- Page / theorem / equation: Theorem 7 p. 42; Theorem 8 p. 45.
- Reading evidence and limitations: statements read; proofs not read.
- Relation to campaign claims (no inherited proof status): IMPLIES PART of PD-T031 (growing-block Paige identity): at an exact eigenvector (ρ = 0), with real symmetric A, symmetric T, normalised blocks and no injected vectors, PD-T031 part 1 reduces to an identity for sᵀcBs with c = Q̂ᵀQ̂₊, B the boundary coefficient, which is Sinha's g_iᵀw_i (c ↔ a = VᵀW, B ↔ HE_kᵀ). Comparison made at the level of the displayed formulas only; proofs not compared. Sinha has no diagonal complex-symmetric (bilinear) case, no injecting operator and no commutator residual.

## Corrections and upgrades (old → new)

- LIT-083: abstract-checked → verified: abstract p. 1; block Paige identity Theorem 7 p. 42; nearby enlarged problem Theorem 6 p. 39.
- LIT-084: UNVERIFIED (reported) → partly verified: block sizes change by rank deflation (p. 27, §7.4 p. 37); in the pages read nothing treats growing blocks or several operators.

## History

2026-11-03: addendum by the P3 reader (Claude Opus 5.5 high), padua-literature-20261103.
