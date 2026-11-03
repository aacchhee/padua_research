# meurant-strakos-2006 — addendum (padua-literature-20261103, P3)

Addendum to `literature/records/meurant-strakos-2006.md`. G. Meurant, Z. Strakoš, The Lanczos and conjugate gradient algorithms in finite precision arithmetic, Acta Numer. 15 (2006) 471–542, [doi:10.1017/S096249290626001X](https://doi.org/10.1017/S096249290626001X); author PDF https://www.karlin.mff.cuni.cz/~strakos/download/2006_MeSt.pdf.

- Access and reading date: 2026-11-03 (author PDF, pdf.js in the built-in browser).
- Reading coverage: exact pages 505–506 (Theorems 4.4–4.5 and the following remarks), 510–512 (§4.3 account of Greenbaum's construction, Theorem 4.9 and the following discussion). Nothing else read.
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps: the rest of the survey (not needed for P3).

## Extracted published statements

### LIT?padua-literature-claude-63 — The survey's statements of Paige's and Greenbaum's results

- Statement in faithful paraphrase: Theorem 4.4 (p. 505) summarises Paige 1980 (pp. 241–249): every Ritz value θ_j^{(k)} is within max{2.5(η_{k+1}|ζ_{kj}| + √k‖A‖ε₁), [(k + 1)³ + √3 n²]‖A‖ε₂} of an eigenvalue of A. Theorem 4.5 (pp. 505–506) gives the stabilized case (bound 5t²‖A‖ε₂). Theorem 4.9 (pp. 511–512) states Greenbaum's model: T_k equals the matrix of exact Lanczos on an (n + m_k)-order matrix B whose eigenvalues lie within O((n + m_k)³ max{ε_M‖A‖, ‖f^k‖, …, ‖f^{n+m_k}‖}) of some eigenvalues of A, the f^j being the smallest perturbations that make a coefficient vanish by step n + m_k; the construction picks k − m_k orthonormal vectors in the span of the computed vectors, avoiding converged well-separated Ritz directions (p. 511). The survey adds that B is not unique, that experiments suggest much smaller intervals than the technically complicated bounds, and that a rigorous quantification of the a-priori "blurred" model is still incomplete (p. 512).
- Page / theorem / equation: pp. 505–506 (Theorems 4.4–4.5); pp. 510–512 (§4.3, Theorem 4.9).
- Reading evidence and limitations: read in the author PDF text layer.
- Relation to campaign claims (no inherited proof status): secondary account; consistent with Greenbaum's Theorem 1 (`greenbaum-1989.addendum.md`, statement 58).

## Corrections and upgrades (old → new)

- LIT-272: WebFetch digest (partly garbled) → verified against the author PDF, Theorem 4.9 pp. 511–512. Note that Theorem 4.9 is the survey's restatement of Greenbaum's Theorem 1 (unquantified f^j); the quantified widths are Greenbaum's Theorem 1′ (p. 51 of LAA 113).

## History

2026-11-03: addendum by the P3 reader (Claude Opus 5.5 high), padua-literature-20261103.
