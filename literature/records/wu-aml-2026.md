# wu-aml-2026 — H.-N. Wu, Marcinkiewicz–Zygmund stability of quadrature-based Galerkin schemes, Appl. Math. Lett. 182 (2026) 110033

Registration (2026-11-05 PR21 final registration): LIT-489. Original provisional aliases remain below; [exact map](../../topics/padua-literature-20261103/preparation/final-id-map.json). Source statements, versions, reader attribution and reading limits are unchanged. Developer-only source checks remain qualified by audit02/03; no independent auditor page-image verification is inferred.

- DOI / URL / supplied location: <https://doi.org/10.1016/j.aml.2026.110033> (Crossref-checked in p2-links); journal page <https://www.sciencedirect.com/science/article/pii/S0893965926001643>. Publisher PDF supplied by AC (`Downloads\padua\papers\1-s2.0-S0893965926001643-main.pdf`, staged to the session at /mnt/user-data/uploads/padua/papers/), read with `pdftotext -layout`. Not stored in Git.
- Access and reading date: 2026-11-03.
- Reading coverage: complete full text, 6 pp. (journal pages are article pp. 1–6), including the reference list. Received 23 Apr 2026, revised 8 Jun 2026, accepted 8 Jun 2026, online 13 Jun 2026.
- Reader, model and effort: Claude, Opus 5.5, high. Rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.
- Named gaps: none for this source.

## Extracted published statements

### LIT-489 (LIT?padua-literature-claude-21) — abstract MZ-to-Galerkin stability transfer; no node-specific constants

- Statement in faithful paraphrase:
  - Definition 2.1 / eq. (1.3) (pp. 1–2): a positive-weight rule satisfies the MZ condition on a finite-dimensional space P_n if (1−η)‖p‖² ≤ ⟨p,p⟩_m ≤ (1+η)‖p‖² for some η in (0,1), in L²(dx).
  - Proposition 2.1 and Lemma 2.1 (p. 2): the discrete Riesz map R_n^{(m)} (defined by ⟨R p, q⟩ = ⟨p, q⟩_m) satisfies (1−η)I ≤ R ≤ (1+η)I, condition number ≤ (1+η)/(1−η), ‖R − I‖ ≤ η, hence |⟨p,q⟩_m − ⟨p,q⟩| ≤ η‖p‖‖q‖ on P_n.
  - Theorem 3.1 (p. 3): for a bilinear form a(u,v) = ⟨Au, v⟩ on P_n with A mapping P_n into itself, continuity β and coercivity α, and η < α/β, the quadrature Galerkin problem is well posed and its solution differs from the exact Galerkin solution by at most (‖F_m − F‖ + βη‖u_n‖)/(α − βη).
  - Corollary 3.1 (p. 4): for F_m(v) = ⟨f,v⟩_m with continuous f, the error is ≲ (E_n(f)_∞ + η‖f‖ + βη‖u_n‖)/(α − βη).
  - Remark 2.1 (p. 2): on S², MZ holds when n ≲ η/δ_m (mesh norm), citing Filbir–Mhaskar and Mhaskar–Narcowich–Ward; random equal-weight points need m ≳ n² log n/η² (citing Le Gia–Mhaskar).
  - §4 (pp. 4–5): numerical test on S² with n = 8, Fibonacci and perturbed Fibonacci points, m from 100 to 15000; ‖G_m − I‖₂ used as MZ-defect proxy; error roughly proportional to it.
- Hypotheses and notation: positive weights; η strictly below 1 in a two-sided symmetric form; no specific node family on an interval or square is treated. No Chebyshev, Clenshaw–Curtis, Lobatto, Padua or square example appears (whole text checked).
- Page / theorem / equation: as above.
- Reading evidence and limitations: complete read of a 6-page letter; proofs are short and were checked for logic at reading level (Theorem 3.1 uses Lemma 2.1 with p = Au and ‖Au‖ ≤ β‖u‖).
- Relation to campaign claims (no inherited proof status): an abstract consumer of MZ constants. Translation: Wu's η is max(1 − λ_−, λ_+ − 1) in our notation. At CC nodes on Π_{N−1}, PD-T017/T018 give λ_− ≍ (1+log N)^{−2}, so η → 1 at the endpoint degree: whenever α < β the hypothesis η < α/β fails for all large N, and even for α = β the factor 1/(α − βη) grows like (1+log N)²; at fixed ratio n ≤ θN, PD-T024 supplies an explicit η(θ) < 1 that can be inserted into Theorem 3.1. RELATED (generic framework, no CC/Padua constants). For the 1-D CC rows of comparison.md this closes the "Wu AML unread" gap with *no matching result found in the documented search*.

## Search and attribution notes

No forward or backward link to CC or Padua results in the reference list (14 references: hyperinterpolation survey, Sloan, MZ on manifolds/sphere, An–Wu BIT 2022 and J. Complexity 2024, Gröchenig, Ehler–Gröchenig, Lubinsky survey, An–Wu SINUM 2026). The survey reference gives the published venue of An–Ran–Wu (Dolomites Res. Notes Approx. 18(1) (2025) 135–145).

## History

2026-11-03: created from the AC-supplied publisher PDF. Provisional ID LIT?padua-literature-claude-21.
