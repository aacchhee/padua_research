# laudadio-mastronardi-vanassche-vandooren-2024 — T. Laudadio, N. Mastronardi, W. Van Assche, P. Van Dooren, "A Matlab package computing simultaneous Gaussian quadrature rules for multiple orthogonal polynomials", J. Comput. Appl. Math. 451 (2024) 116109

- DOI / URL: https://doi.org/10.1016/j.cam.2024.116109 ; preprint https://arxiv.org/abs/2406.11269 (v1, 17 Jun 2024, 32 pp.).
- Access and reading date: 2026-11-03, arXiv v1 PDF via pdf.js. The JCAM version was not opened.
- Reading coverage: exact pages of the arXiv v1: pp. 1–4 (abstract, introduction, outline), p. 16 (end of §6, start of §7), pp. 17–21 (§7, Remark 1, start of §8), pp. 22–23 (tables, §9 Conclusions), p. 24 (references), p. 25 (appendix header). Not read: §§3–6 in detail (classes of MOPs, ClassMOP/GaussMOP usage, balancing derivation), the code tables.
- Reader, model and effort: Claude P4 literature reader (claude-opus-5-5, high).
- Named gaps requiring future re-reading: §6 balancing derivation; the journal version.

Locators are arXiv v1 PDF pages.

## Extracted published statements

### LIT?padua-literature-claude-80 — what is computed, accuracy claims, future work

- Statement in faithful paraphrase: The package GaussMOP computes the nodes and the two weight sets of simultaneous Gaussian quadrature (r = 2, type II step-line MOPs, monic, explicitly known recurrence coefficients for nine families). The rule comes from the eigen-decomposition of the banded **lower** Hessenberg recurrence matrix (two subdiagonals, Theorem 1 p. 3, weights from the first one or two entries of the left and right eigenvectors). The eigenproblem is strongly ill conditioned, and MATLAB's balance does not help (p. 3). A diagonal balancing Ĥ = S⁻¹HS that makes the tridiagonal part symmetric reduces the eigenvalue condition numbers drastically (pp. 4, 16). Nodes are then found by an Ehrlich–Aberth iteration on Ĥ, in O(n²) time and O(n) memory, started from the eigenvalues of a similar symmetric tridiagonal matrix. Eigenvectors come from Givens-based null-space computations (pp. 17–20). For r > 2 only a four-step sketch is given (Remark 1, pp. 20–21). The conclusion (§9, p. 23) reports reliable results against 80-digit Mathematica references for n up to 100 (Tables 4–6, p. 22). It contains **no backward-error statement and no stated future work**.
- Hypotheses and notation: recurrence coefficients known in closed form; the input is H, not nodes and weights. This is the forward problem (H → nodes, weights), the reverse of the Leuven IEP.
- Page / theorem / equation: abstract p. 1; Theorem 1 p. 3; p. 4 (outline and complexity); §7 pp. 16–21; Remark 1 pp. 20–21; Tables 4–6 p. 22; §9 p. 23.
- Reading evidence and limitations: pages listed above read. The stability statement for the tridiagonal reduction refers to [13] (= the Numer. Algorithms 2025 paper, record `laudadio-mastronardi-vandooren-2025`).
- Relation to campaign claims: the companion forward problem to the MOP IEP. The idea of balancing to tame non-normality parallels the scaling in LIT?…-71. Univariate only.

## Search and attribution notes

- Searches on 2026-11-03 over all 32 pages: "bivariate", "multivariate", "Chesnokov", "two variables", "several variables", "Padua", "Van Barel", "Faghih", "Vandebril": 0 hits. The package is said to be downloadable from a CNR Bari page (p. 25, not opened).

## History

2026-11-03: new record (P4); provisional ID 80.
