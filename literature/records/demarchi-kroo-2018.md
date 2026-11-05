# demarchi-kroo-2018 — S. De Marchi, A. Kroó, Marcinkiewicz–Zygmund type results in multivariate domains, Acta Math. Hungar. 154(1) (2018) 69–89

Registration (2026-11-05 PR21 final registration): LIT-490. Original provisional aliases remain below; [exact map](../../topics/padua-literature-20261103/preparation/final-id-map.json). Source statements, versions, reader attribution and reading limits are unchanged. Developer-only source checks remain qualified by audit02/03; no independent auditor page-image verification is inferred.

- DOI / URL / supplied location: <https://doi.org/10.1007/s10474-017-0769-4> (DOI as printed on the journal PDF read; not Crossref-checked); journal page <https://link.springer.com/article/10.1007/s10474-017-0769-4>. First published online 20 Oct 2017. No free version searched.
- Access and reading date: 2026-11-03. Publisher PDF (21 pp.) via link.springer.com in AC's built-in browser (institutional access active there), text layer via pdf.js. Not stored.
- Reading coverage: journal pp. 69–75 read (abstract, §1 introduction and setting, statement of the univariate Mastroianni–Totik-type relation (3), Theorem 1 and Lemma 1 with proof, start of the proof of Theorem 1); keyword screen of the remaining pages for square, cube, Chebyshev, Padua, Xu, Lissajous, Theorem, mesh, polytope; read in context: Theorem 2 (p. 77), Propositions 1–4 and Examples (pp. 80–86), final Remark (pp. 88–89). Proof details beyond p. 75 not read.
- Reader, model and effort: Claude, Opus 5.5, high. Rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.
- Named gaps: pp. 76–88 proofs; whether a square/polytope MZ mesh is stated explicitly somewhere other than via the general principles (keyword screen found "square" only in the reference list, "polytope" only in the abstract/introduction).

## Extracted published statements

### LIT-490 (LIT?padua-literature-claude-23) — oversampled MZ meshes with unspecified oversampling and constants; explicit univariate Lemma 1

- Statement in faithful paraphrase:
  - Setting (pp. 69–70): an MZ mesh for a compact K ⊂ R^d is a point set of cardinality ≍ n^d with positive weights giving two-sided equivalence of ‖g‖^p_{L^p(w)} and the weighted nodal ℓ^p sum on P^d_n, with constants depending on p, K, w only.
  - Relation (3) (p. 71), quoted from Mastroianni–Totik for doubling weights on [−1,1]: for some integer M depending on the weight and every m ≥ M, the nodes cos(πj/(mn)), 0 ≤ j ≤ mn, with weights given by w-integrals over angular windows of width 2/n, form an MZ family on P¹_n.
  - Lemma 1 (pp. 72–73): if g satisfies the Bernstein-type relation ∫(Δ_k|g′|)^p ≤ ∫|g|^p with Δ_k(x) = 1/k² + √(1−x²)/k, then for every m ≥ 18pk+1 the CGL nodes x_j = cos(jπ/m) with weights x_j − x_{j+1} give (2/3)·Σ ≤ ∫|g|^p ≤ 2·Σ. Explicit constants 2/3 and 2.
  - Theorem 1 (p. 73): circular sectors D_a, a < 1/2, MZ mesh of (mn+1)² points for any sufficiently large m depending on the weight and p. Theorem 2 (p. 77): disc with weights w(|r|)φ(t), mesh on polar CGL-type grids, sufficiently large m. Section 3 (pp. 79–): symmetry and rotation principles (Proposition 1: union with an involution image) and examples (ball, simplex via Proposition 4, cones, torus).
  - Final Remark (pp. 88–89): the authors say explicit bounds for the oversampling parameter m and for the equivalence constants would be useful; their methods are constructive but they did not derive them.
- Hypotheses and notation: positive weights; doubling or Jacobi-type weights; oversampling factor m (unspecified in Theorems 1–2); P^d_n total degree.
- Reading evidence and limitations: selected pages as listed; Lemma 1 proof read in full.
- Relation to campaign claims (no inherited proof status):
  - 1-D (PD-T022/T023/T024): Lemma 1 gives explicit constants but only in a heavily oversampled window. For p = 2 and degree-n polynomials the hypothesis forces k ≥ n (test g = Legendre P_n: ∫(1−x²)P_n′² = n(n+1)∫P_n², so ∫(Δ_k|g′|)² ≥ (n(n+1)/k²)∫g²), hence m ≥ 36n+1, i.e. n < m/36, deep inside CC half-exactness n ≤ m/2 where exactness already gives λ_± = 1 (our translation.md T3–T4 argument applies verbatim: CC weights ≍ Δx weights within factors ½ and 5). RELATED: nothing beyond exactness follows, exactly as for Mastroianni–Totik (LIT-051).
  - 2-D (PD-T116, PD-T110, PD-T028): no Padua, Xu, Lissajous or square statement in the pages read; the 2-D results are oversampled meshes with unspecified m and constants, positive weights. RELATED, DIFFERENT SETTING. It supports the priority wording that no explicit-constant MZ statement at Padua-type nodes beyond half-exactness was found.

## Search and attribution notes

Lead found via An–Ran–Wu survey §3.1 (ref. [29]). Not previously in the repository (grep for Kroó/DOI on 2026-11-03 found only an unrelated optimal-mesh mention in programme-ideas sources).

## History

2026-11-03: created. Provisional ID LIT?padua-literature-claude-23.
