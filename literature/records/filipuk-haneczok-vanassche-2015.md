# filipuk-haneczok-vanassche-2015 — G. Filipuk, M. Haneczok, W. Van Assche, "Computing recurrence coefficients of multiple orthogonal polynomials", Numer. Algorithms 70(3) (2015) 519–543

- DOI / URL: https://doi.org/10.1007/s11075-015-9959-8 ; preprint https://arxiv.org/abs/1406.0364 (v2, 23 Jan 2015, 22 pp.).
- Access and reading date: 2026-11-03, arXiv v2 PDF via pdf.js. The journal version was not opened.
- Reading coverage: exact pages, limited to what bears on MOP recurrence computation and stability: pp. 1–3 (abstract, introduction, problem statements), p. 8 (shifted step-line algorithm and Maple procedure), p. 10 (shift in the second index), p. 13 (nearest-neighbour Maple procedure), pp. 14–15 (Table 1, start of §3), p. 18 (Maple procedure for the inverse problem), pp. 19–21 (Thms 3.2–3.3 and proof), section-heading list, and whole-text keyword searches. Not read: the derivations in §2.1–2.3 (pp. 3–13).
- Reader, model and effort: Claude P4 literature reader (claude-opus-5-5, high).
- Named gaps requiring future re-reading: none for the statements below. The Aptekarev–Denisov–Yattselev half of INDEX row LIT-420 is not covered by this reading.

## Extracted published statements

### LIT?padua-literature-claude-82 — two computational problems, exact-arithmetic style, no stability analysis

- Statement in faithful paraphrase: The paper treats two problems. (1) Given the step-line (r+2)-term recurrence coefficients, obtain the nearest-neighbour recurrence coefficients, and in particular the three-term coefficients of each marginal measure. This is done for r = 2 by passing through the r shifted step-lines and then to nearest neighbours (§2). (2) The inverse: given the marginal measures' three-term coefficients, compute all nearest-neighbour coefficients and the step-line coefficients (§3). For general r this uses the compatibility (partial difference) relations of the nearest-neighbour system (3.11)–(3.13). The recursion is on the length of the multi-index and requires b_{n,i} ≠ b_{n,j} (Theorem 3.3, pp. 20–21). Theorem 3.2 (p. 19) gives the step-line coefficients from the nearest-neighbour ones. The algorithms are given as **Maple procedures** (pp. 8, 10, 13, 18). The illustrative output is printed to 20 digits (Table 1, p. 14), checked against values computed earlier from moments. The paper contains **no numerical stability or conditioning analysis**: the only occurrence of "numerical" is in a reference title, and "stable", "error", "accuracy" do not occur. The introduction names the Jacobi–Perron algorithm (vector continued fractions) and Van Iseghem's vector QD algorithm as ways to get step-line coefficients from moments (p. 3).
- Hypotheses and notation: positive measures on the real line; normal indices; monic type II MOPs; r = 2 in detail, general r in §3.3.
- Page / theorem / equation: abstract p. 1; problems p. 3; Maple pp. 8, 10, 13, 18; Table 1 p. 14; Thm 3.2 p. 19; (3.11)–(3.13) and Thm 3.3 p. 20; proof p. 21.
- Reading evidence and limitations: listed pages read; keyword searches over all 22 pages.
- Relation to campaign claims: this is the "comparison with Filipuk–Haneczok–Van Assche" that SINUM §7 lists. Its input is the marginal recurrences, not nodes and weights, so it is not an IEP solver. The nearest-neighbour compatibility relations (3.11)–(3.13) express the requirement that steps in different index directions commute, Y_{n+e_i+e_j} being reachable either way. This is structurally the condition the bivariate pair (H_x, H_y) must satisfy in the Van Barel–Chesnokov setting. The analogy is noted for memo question B only.

## Search and attribution notes

- Searches on 2026-11-03: "bivariate", "multivariate", "Chesnokov", "two variables", "several variables", "Padua": 0 hits. "stab", "error", "accura", "floating", "precision", "Digits": 0 hits. "Numerical" occurs only on p. 22 (reference list). "condition" hits are mathematical (orthogonality or boundary conditions).

## History

2026-11-03: new record (P4); provisional ID 82. Corrects the secondary description in LIT-420 (see the addendum).
