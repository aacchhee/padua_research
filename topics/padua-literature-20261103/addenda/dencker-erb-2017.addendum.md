# Addendum to dencker-erb-2017 (LIT-014) — journal body read and compared with arXiv v2

P. Dencker, W. Erb, *Multivariate polynomial interpolation on Lissajous–Chebyshev nodes*, J. Approx. Theory 219 (2017) 15–45, DOI <https://doi.org/10.1016/j.jat.2017.03.003>; journal page <https://www.sciencedirect.com/science/article/pii/S0021904517300345>; arXiv 1511.04564v2 (21 Aug 2017), <https://arxiv.org/abs/1511.04564>.

- Access and reading date: 2026-11-03. Journal: publisher PDF supplied by AC (`Downloads\padua\papers\1-s2.0-S0021904517300345-main.pdf`, staged to /mnt/user-data/uploads/padua/papers/; 31 pp.), read with `pdftotext -layout`. arXiv v2: PDF (30 pp.) text layer via pdf.js in AC's built-in browser. Received 14 Nov 2015, revised 24 Sep 2016, accepted 24 Mar 2017, online 6 Apr 2017; communicated by Yuan Xu.
- Reading coverage (journal): §2.1 node sets (pp. 23–24), §2.2 discrete orthogonality (pp. 27–31: (2.12)–(2.14), Proposition 2.5, (2.19), Proposition 2.6, Theorem 2.7), §2.3 interpolation (pp. 32–34: (2.32), Theorem 2.8, Corollary 2.9, Theorem 2.10, Remarks 2.11–2.13). Theorem/proposition list of the whole paper extracted. Proofs read only where needed for the statements.
- Reader, model and effort: Claude, Opus 5.5, high. Rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.

## Statements (journal locators) and version comparison

| Item | Journal locator | arXiv v2 locator | Comparison |
|---|---|---|---|
| Index sets I^{(n)} = I₀ ∪ I₁ (parity classes r), node set LC^{(n)} (2.1) | p. 23 | p. 8 | equation present at same number; content not compared character by character |
| Cardinalities #I^{(n)} = p[n+1]/2^{d−1}, #I_M = Π_{i∈M}(n_i−1)/2^{#M−1} (2.4) | p. 23 | p. 9 | same formula |
| χ_γ(i) = Π_j cos(γ_j i_j π/n_j) (2.12); weights w_i = 2^{#M}/(2p[n]) for i ∈ I_M (2.13) | p. 27 | p. 12 | same |
| Proposition 2.5 / (2.14): the discrete integral of χ_γ is nonzero only if γ_i = h_i n_i with Σh_i even, and then equals 1 | p. 28 | p. 12 | same |
| Spectral index set Γ^{(n)} (2.19): γ_i < n_i, γ_i/n_i + γ_j/n_j < 1 for i ≠ j, plus the exceptional (0,…,0,n_d) | p. 29 | p. 13 | present at same number; content not compared character by character |
| Proposition 2.6: #Γ^{(n)} = #I^{(n)} | p. 29 | p. 13 | same numbering |
| Theorem 2.7 / (2.25): χ_γ, γ ∈ Γ^{(n)}, orthogonal basis; norms 2^{−e(γ)}, and 1 for the exceptional index | p. 30 | p. 15 | same |
| (2.32) fundamental polynomials with the exceptional-mode correction; Theorem 2.8 unique interpolation in Π^{(n)} | p. 32 | pp. 16–17 | same |
| Theorem 2.10 / (2.36): quadrature for the normalized product Chebyshev measure, exact on polynomials orthogonal to all T_γ with γ ≠ 0 satisfying (2.14) | p. 34 | p. 18 | same |
| Remark 2.11: d = 1 gives CGL; d = 2 Padua formulas first proved by Bos et al., extended to degenerate Lissajous curves by Erb et al. | p. 34 | p. 18 | same wording in substance |

- Theorem/proposition numbering is identical in both versions (Theorems 1.1, 1.4, 2.2, 2.3, 2.7, 2.8, 2.10, 3.3, 3.5, 3.9, 3.10, 3.12; Propositions 1.2, 2.1, 2.5, 2.6, 3.1, 3.7, 3.8; Corollaries 1.3, 2.9, 3.11; Remarks 2.11–2.13, 3.2, 3.4). No substantive difference was found in the inspected items. arXiv v2's abstract page carries a journal reference to J. Approx. Theory 219 (2017); p2-links row 6b said there was none — correct that note.
- Padua case: d = 2, n = (m, m+1) (or (m+1, m)) gives the Padua points up to reflection (arXiv Example 2.4(ii), p. 11; journal §2.1). The weights (2.13) for d = 2 are 1/(2m(m+1)), 1/(m(m+1)), 2/(m(m+1)) for vertex, edge, interior, i.e. the positive Chebyshev Padua weights with the correct m(m+1) denominator (consistent with the SVZ (25) correction).

## Old → new corrections

- INDEX/record status for LIT-014: Old "reported / UNVERIFIED … supplied secondary account only; original fulltext NOT inspected". New: "LITERATURE / primary reading: journal pp. 23–34 (§§2.1–2.3) read 2026-11-03 and compared with arXiv v2 (identical numbering and statements on the inspected items). The 2026-10-31 'characteristic transfer' sentence remains a proposed derivation, not a source statement."
- padua-mz-2d literature.md: Old "The 2017 journal body was not separately compared." New: "Journal body compared 2026-11-03 for Proposition 2.5, (2.12)–(2.14), (2.19), Theorems 2.7, 2.8, 2.10, Remark 2.11 (journal pp. 27–34): same as arXiv v2."

## Relation to campaign claims (no inherited proof status)

Unchanged: direct prior source for the positive checkerboard resonance (discrete Chebyshev moments) behind PD-T106 and D1; it contains no signed Lebesgue rule, no Lebesgue-measure Gram spectra and no MZ inequality. RELATED for PD-T106/T109/T115 (mechanism ingredient), RELATED, DIFFERENT SETTING for PD-T110/T116.

## History

2026-11-03: journal read and compared (P2 reader).
