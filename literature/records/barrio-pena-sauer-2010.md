# barrio-pena-sauer-2010 — R. Barrio, J. M. Peña, T. Sauer, Three term recurrence for the evaluation of multivariate orthogonal polynomials, J. Approx. Theory 162 (2010) 407–420

- DOI / URL / supplied location: doi:10.1016/j.jat.2009.07.005 (printed on p. 407); AC local copy `Downloads\padua\papers\1-s2.0-S0021904509001178-main.pdf` (supplied 2026-10-31 23:18).
- Access and reading date: 2026-10-31.
- Reading coverage: exact pages pp. 407–408 (abstract, introduction), pp. 412–413 (§4, eqs. (3)–(9), Theorem 8, Remark 9), pp. 415–416 (§5 selection strategies), pp. 418–419 (stability: triangular system (18), bounds (19)–(20)). Other pages (§3 product measures, §4 computation of B_{n,j}, C_{n,j} from moments, §5 Clenshaw/Forsythe derivation) not read.
- Reader, model and effort: Claude orchestrator (configured `claude-opus-5-5`; effort not exposed), text via pdftotext into the scratchpad only.
- Named gaps requiring future re-reading: §3 (product-measure case) and the remaining §4–5 derivations; whether any numerical experiment on non-product domains is reported.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c.

## Extracted published statements

### LIT?bivariate-lanczos-claude-301 — explicit one-variable-per-polynomial recurrence for monic multivariate OPs

- Statement in faithful paraphrase: For monic orthogonal polynomials m_α (|α| = n+1) of a d-variate measure, from the matrix three-term relations x_j p_n = A_{n,j} p_{n+1} + B_{n,j} p_n + C_{n,j} p_{n−1}, each m_α can be computed explicitly from degree-n and n−1 vectors by multiplying by any one variable x_j with α_j > 0 (eq. (5)); averaging over all admissible j gives a symmetric form (6), assembled in Theorem 8 as m_{n+1} = A_n(x) m_n − B_n m_n − C_n m_{n−1} with shift matrices L_{n,j}.
- Hypotheses and notation: quasi-definite/positive moment functional with monic OP vectors; implicit relations (3)–(4) cited from Dunkl–Xu [8].
- Page / theorem / equation: pp. 412–413, eqs. (3)–(9), Theorem 8.
- Reading evidence and limitations: read in pdftotext layout; formulas checked against the layout text, not page images.
- Relation to campaign claims (no inherited proof status): prior art for the "selection of one relation per new polynomial" view used in PD-T?bivariate-lanczos-claude-108 (row selection of the Jacobi pencil) and for an all-relations (averaged) alternative related to the two-relation remedy of IDEA?…-111; setting differs (monic OPs from moments, point evaluation, no discrete-measure Lanczos vectors, no window truncation, no loss-of-orthogonality analysis).

### LIT?bivariate-lanczos-claude-302 — the choice of variable affects rounding error (Remark 9, §5 strategies)

- Statement in faithful paraphrase: Remark 9 notes that using (5) componentwise with a suitably chosen j may give better numerical behaviour than the symmetric (7). §5 proposes two heuristic point-dependent strategies for choosing j (closest to the centre of the support's projection; or minimal norm of e_{α−j}ᵀ(x_j I − B_{n,j})), motivated by univariate Chebyshev evaluation error near endpoints. No analysis of growth with degree or of the effect of support geometry is given in the pages read.
- Page / theorem / equation: p. 413 (Remark 9); pp. 415–416 (§5, strategies 1–2).
- Relation to campaign claims: prior art that the selection is a numerical degree of freedom; does not state the exponential non-product amplification or link it to orthogonality loss (pages read).

### LIT?bivariate-lanczos-claude-303 — multivariate Clenshaw as triangular substitution; backward/forward bounds

- Statement in faithful paraphrase: The multivariate Clenshaw algorithm is equivalent to solving a block upper-triangular system M q̃ = c (eq. (18)) by substitution, so Higham's triangular-system results give a componentwise backward bound (19) (|ΔM| ≤ d_n u/(1 − d_n u)|M|) and a forward bound (20) in terms of the inverse of the comparison matrix M(M)^{-1}.
- Page / theorem / equation: pp. 418–419, eqs. (18)–(20), citing Higham ASNA Thms 8.5 and 8.10.
- Relation to campaign claims: prior art for "recurrence = triangular substitution, error governed by an inverse of the triangular matrix", the core of PD-T?…-108 / -104's propagator view, in the evaluation (Clenshaw) setting for monic OPs. PD-T?…-108 must cite this as closest predecessor; any separation must rest on the discrete-measure Lanczos-vector setting, the window truncation and the orthogonality-loss link, not on the triangular-selection view itself.

## Search and attribution notes

Flagged by the L1 prior-art check (reviews/L1-prior-art-01.md) as a potential kill for mechanisms (b)/(c); fulltext supplied by AC. Verdict after reading the pages above: mechanism (b)'s triangular-selection/propagator framing and the existence of selection freedom are **known** in the monic-evaluation setting; the link to exponential loss of orthogonality on non-product supports was not found in the pages read.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L1 prior-art review 2026-10-31 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: record created by the orchestrator from AC's local copy.

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): the L1 prior-art review (2026-10-31) recorded this source as metadata only ('not read; must read') because ScienceDirect was blocked for it; the orchestrator's reading of the AC copy (statements 301–303, pages as listed above) supersedes that and the coverage line is unchanged. The L1 review's 'high-risk unread source' flag for mechanisms (b) and (c) is thereby narrowed, not closed: the pages not read (§3, parts of §§4–5) are still named gaps. The L2 prior-art review relied on statements 301–303.
