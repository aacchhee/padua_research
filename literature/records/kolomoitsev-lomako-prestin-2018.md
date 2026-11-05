# kolomoitsev-lomako-prestin-2018 — Kolomoitsev, Lomako, Prestin, On L_p-error of bivariate polynomial interpolation on the square, J. Approx. Theory 229 (2018) 13–35

Registration (2026-11-05 PR21 final registration): LIT-488. Original provisional aliases remain below; [exact map](../../topics/padua-literature-20261103/preparation/final-id-map.json). Source statements, versions, reader attribution and reading limits are unchanged. Developer-only source checks remain qualified by audit02/03; no independent auditor page-image verification is inferred.

- DOI / URL / supplied location: <https://doi.org/10.1016/j.jat.2018.02.005> (Crossref-checked in p2-links); journal page <https://www.sciencedirect.com/science/article/pii/S0021904518300194>; arXiv v1 (17 Dec 2017) <https://arxiv.org/abs/1712.06075>, PDF <https://arxiv.org/pdf/1712.06075>.
- Access and reading date: 2026-11-03, arXiv v1 PDF text layer via pdf.js in AC's built-in browser (arxiv.org origin).
- Reading coverage: arXiv v1 (20 pp.) pp. 1–12 read in full (introduction, §2 general MZ framework with Theorems 2.1–2.2, §3 Lissajous–Chebyshev preliminaries with Proposition 3.1 and Theorems 3.1–3.2, §4 main results Theorems 4.1–4.5, Corollary 4.1, Remarks 4.1–4.3, §5.1 Lemmas 5.1–5.3); p. 16 (Lemma 5.10 and proof, Lemma 5.11), p. 19 (§5.5–5.6 final remarks) and the reference list. Pages 13–15, 17–18 (smoothness lemmas) not read. The journal body was not read (ScienceDirect not used); all locators are arXiv v1 locators.
- Reader, model and effort: Claude, Opus 5.5, high. Rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.
- Named gaps: journal version (arXiv v1 has no journal-ref line; correspondence unchecked); pp. 13–15, 17–18.

## Extracted published statements

### LIT-488 (LIT?padua-literature-claude-20) — MZ inequalities on Lissajous–Chebyshev (incl. Padua) nodes in Chebyshev-weighted L^p; L^p interpolation error

- Notation (arXiv pp. 5–7): for coprime (m,n), LC_{m,n} = points γ(πk/(mn)), k = 0..mn, on the degenerate Lissajous curve γ(t) = (cos nt, cos mt); equivalently the checkerboard {(cos(iπ/m), cos(jπ/n)) : i+j even} with (m+1)(n+1)/2 points (Proposition 3.1, cited from Erb 2016). For n = m+1 these are the Padua points (p. 2). Interpolation space Π^L_{m,n} = span{T_k(x)T_l(y) : k/m + l/n < 1} ∪ {T_n(y)} (p. 6). Positive weights λ_{i,j} = 1/(2mn), 1/(mn), 2/(mn) for vertex, edge, interior nodes (3.2). Weighted space L^p_w with w(x,y) = ((1−x²)(1−y²))^{−1/(2p)}, i.e. ‖f‖^p = ∫|f|^p (1−x²)^{−1/2}(1−y²)^{−1/2} dx dy (p. 7).
- Lemma 5.1 (arXiv p. 11): for 1 ≤ p < ∞ and every P in Π^L_{m,n}, the weighted nodal ℓ^p sum (weights λ_{k,l}) is bounded by C·‖P‖_{L^p_w} from above (5.1, constant c_p) and ‖P‖_{L^p_w} ≤ C_p K_p(m,n) × (nodal sum)^{1/p} (5.2), with K_p = 1 for 1 < p < ∞ and K_1 = log(m+1)log(n+1). Constants c_p, C_p depend only on p and are not given. Attribution in the source: (5.1) for all p and (5.2) for 1 < p < ∞ are taken from Erb 2016 (Appl. Math. Comput. 289, 409–425, ref. [10]); only the p = 1 case is proved here, via an L¹_w bound C(mn)^{−1}log(m+1)log(n+1) on the fundamental polynomials (5.4).
- Lemma 5.2 (p. 12): the trigonometric form of (5.2) on the even-cosine span. Lemma 5.3 (p. 12): forward MZ for cosine polynomials of order < 6m, 6n sampled on the threefold-refined tensor grid πk/(3m), πl/(3n), from the 1-D result (5.5).
- Theorems 2.1–2.2 (pp. 3–5): abstract error bounds from a left MZ inequality on the node set plus a right MZ inequality on a superset (Theorem 2.1), or from two-sided MZ with the best one-sided approximation (Theorem 2.2).
- Theorem 4.1 (p. 7): ‖f − L_{m,n}f‖_{L^p_w} ≤ C_p K_p(m,n) × best one-sided approximation error in L^p_w. Theorems 4.2–4.5 and Corollary 4.1 (pp. 8–11): L^p_w error bounds for functions of Hardy–Krause bounded variation, with smoothness moduli, and with univariate best approximations; e.g. O(m^{−1/p} + n^{−1/p}) for HBV functions (1.6, p. 3). Mechanism (p. 3, Lemma 5.10 p. 16): LC_{m,n} is a subset of a tensor Chebyshev grid, so the error is compared with tensor-product interpolation errors.
- Final remark §5.6 (p. 19): the results hold with minor changes for the Padua points, Xu points and non-degenerate Lissajous–Chebyshev nodes.
- Hypotheses: positive Chebyshev-type weights, Chebyshev-weighted L^p norm, the anisotropic interpolation space Π^L, unspecified constants. No statement about Lebesgue measure dx dy, signed weights, total-degree subspaces Π_n with n < m, or explicit constants.
- Reading evidence and limitations: arXiv v1 text layer; formulas checked for structure, not proof-audited. The cited Erb 2016 source of (5.1)–(5.2) was not read.
- Relation to campaign claims (no inherited proof status): the only located published two-sided MZ inequality at Padua/LC nodes on the full interpolation space, but for the positive Chebyshev rule in Chebyshev measure, with unspecified constants. For p = 2 in that measure the positive Padua rule is exact on all products of degree ≤ 2m−1, so the L² case is close to an exactness statement. RELATED, DIFFERENT SETTING for PD-T116 (signed Lebesgue rule, dx dy, total-degree Π_n, explicit η(θ) sought), PD-T110 and PD-T028. Lemma 5.3 (tensor forward MZ with threefold oversampling) is RELATED to PD-T117. Nothing here bears on the uniform C→L² target PD-T114 beyond the general Lebesgue-type L¹ bound (5.4).

## Search and attribution notes

- Lead from p2-links (row 6f, 8.7). Earlier campaign: body retrieval failed (Lübeck author PDF 502, ScienceDirect not reached); now read from arXiv.
- New lead surfaced: W. Erb, *Bivariate Lagrange interpolation at the node points of Lissajous curves – the degenerate case*, Appl. Math. Comput. 289 (2016) 409–425 (KLP ref. [10]; arXiv 1503.00895 per p2-links 8.8), named by KLP as the source of the L^p MZ inequalities (5.1)–(5.2) for 1 < p < ∞. Not read; DOI not verified.

## Journal version (2026-11-05)

AC supplied the journal PDF (`Downloads\padua\papers\1-s2.0-S0021904518300194-main.pdf`, JAT 229 (2018) 13–35). Every theorem, lemma and equation label cited above (arXiv v1) has the same number in the journal. The journal page for each locator is in `topics/padua-literature-20261103/addenda/journal-versions-2026-11-05.addendum.md` (A11); for example Lemma 5.1 is on p. 25 and Lemma 5.3 on p. 26.
- Attribution refinement: (5.1) for all p, and (5.2) for 1 < p < ∞, are quoted from [10] (Erb 2016). The p = 1 case uses (5.4), itself quoted "from [10] (see also [7])".
- Wording was not diffed against arXiv v1.

## History

2026-11-03: created (P2 reader, padua-literature-20261103). Provisional ID LIT?padua-literature-claude-20.
2026-11-05: journal-version pagination added (pass 2 ingest; Sonnet subagent mapping, orchestrator spot-check).
