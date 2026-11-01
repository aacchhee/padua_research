# greenbaum-1989 — A. Greenbaum, Behavior of slightly perturbed Lanczos and conjugate-gradient recurrences, Linear Algebra Appl. 113 (1989) 7-63, doi:10.1016/0024-3795(89)90285-1 (metadata now CONFIRMED on the ScienceDirect open-archive page)

- DOI / URL / supplied location: https://www.sciencedirect.com/science/article/pii/0024379589902851 (landing page read 2026-10-31; labelled open archive, PDF behind 'View PDF' not reachable by the tool); doi:10.1016/0024-3795(89)90285-1. Earlier (Step 0): doi:10.1016/0024-3795(89)90285-1 (from memory; the DOI resolver redirected to the Elsevier linking hub and the follow-up fetch returned empty content on 2026-10-31, so even the DOI-to-paper identification is UNVERIFIED)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata + abstract confirmed on the ScienceDirect page; theorem content only via secondary accounts (Meurant-Strakos, Simonova-Tichy, Chen); the paper's text is NOT read. Earlier (Step 0): not read; metadata NOT confirmed. PR-preparation (2026-11-01) from the L3 prior-art review (2026-10-31): metadata additionally confirmed by Greenbaum's own talk abstract (Prague); the paper itself was not reached (paywalled; eq. (7.10) not seen).
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L3 prior-art review 2026-10-31 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Full text (open archive, 57 pages): the exact theorem(s) with hypotheses, dimension of the larger matrix, interval width in terms of u, the 'Lemma (Paige)' at p. 32. Load-bearing for L3. Earlier (Step 0): Whole source. PENDING-REFERENCE (load-bearing for L3; paywalled).
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-006 — backward-stability model (indirect)

- Verification: **Indirectly described by an abstract of another paper**; the source itself NOT inspected. UNVERIFIED. **Update (online pass): title, volume, pages, year and DOI are now confirmed, and the abstract confirms the nearby-measure form; the 'slightly larger matrix' wording is supported by the Meurant-Strakos statement of the theorem (statement 208). The original theorem is still unread.**
- Statement in faithful paraphrase: Greenbaum's 1989 model: finite-precision Lanczos results are exact Lanczos results for a slightly larger matrix whose eigenvalues lie close to those of the original (indirect description from the Simonova-Tichy abstract page).
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: no theorem number obtained. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance arXiv 2507.16484 abstract page (fetched 2026-10-31) says 'Greenbaum's 1989 model'; also notes/adv_F1_F6_F3.md §1.3, notes/recent_multivariate_NLA.md R1(iv); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L3-Q1: the template for a 'nearby larger node set' statement; the inputs flag that a bivariate version needs a commuting extension (notes/adv_F1_F6_F3.md §1.3).

### LIT?bivariate-lanczos-claude-207 — Abstract: computed polynomials are orthogonal for a nearby measure

- Verification: **ScienceDirect open-archive landing page read (metadata and abstract); full text NOT reached. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Lanczos and conjugate gradients generate polynomials by a three-term recurrence whose roots give approximate eigenvalues. Under small perturbations (such as rounding) the computed polynomials remain orthogonal, but with respect to a slightly different measure whose weights sit on points very near the eigenvalues of A. This explains the behaviour of Ritz values in perturbed Lanczos and the convergence of perturbed CG. The Chebyshev error bound holds approximately for perturbed CG, and a sharper bound follows from a minimax polynomial over small intervals around the eigenvalues.
- Hypotheses and notation: Perturbed Lanczos / CG recurrences (paper-wide).
- Page / theorem / equation: Abstract of LAA 113 (1989) 7-63, February 1989, doi:10.1016/0024-3795(89)90285-1 (page marks the article open archive).
- Reading evidence and limitations: Abstract only. The phrase 'orthogonal with respect to a slightly different measure' is the measure-theoretic form of the model: a nearby discrete measure with clustered nodes. Metadata (title, volume, pages, DOI, author) now confirmed.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: the exact precedent in the target form (nearby positive discrete measure with nodes near the originals); the bivariate task asks for the analogue with two commuting sections.

### LIT?bivariate-lanczos-claude-208 — Theorem form of the backward model (secondary account, Meurant-Strakos Thm 4.9)

- Verification: **Original theorem NOT read. Meurant-Strakos (2006) Section 4 is the source (tool digest of the first part of the survey). UNVERIFIED against Greenbaum.**
- Statement in faithful paraphrase: Fix a step k of finite precision Lanczos on the n x n matrix A with start vector v_1. Greenbaum's construction picks k - m_k mutually orthogonal vectors in the span of the computed vectors that are nearly orthogonal to v_{k+1}, avoiding well-separated converged Ritz directions, and continues the recurrence to length n + m_k - k. The conclusion: T_k equals the matrix generated by exact Lanczos applied to an (n+m_k) x (n+m_k) matrix B whose eigenvalues lie within O((n+m_k)^3 max{u ‖A‖, f_k, ..., f_{n+m_k}}) of eigenvalues of A, where the f_j are the smallest perturbations making some eta_{j+1} vanish by step n+m_k. Strakos (1991, Thm 4.2) is cited for the necessity that B has an eigenvalue near each eigenvalue of A with nonzero weight in v_1.
- Hypotheses and notation: Single symmetric A, single start vector.
- Page / theorem / equation: Meurant-Strakos, Acta Numerica 15 (2006), Theorem 4.9 (~pp. 511-512); Simonova-Tichy refer to a 'Lemma (Paige)' at Greenbaum p. 32 (see simonova-tichy-2025).
- Reading evidence and limitations: Hypotheses were not stated numerically in the digest; the extended dimension and the width bound are the secondary authors' rendering.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: confirms that Greenbaum's model enlarges the matrix (dimension n + m_k), and so introduces extra nodes; a bivariate version must enlarge a commuting pair, i.e. a commuting-extension problem (see degani-schiff-tannor-2005).

### LIT?bivariate-lanczos-claude-209 — Interval-width dependence on epsilon: secondary accounts disagree

- Verification: **UNVERIFIED: three secondary accounts, none the original.**
- Statement in faithful paraphrase: (a) Simonova-Tichy (arXiv 2507.16484): Greenbaum's proof gives eigenvalue intervals of size about sqrt(u)‖A‖ and experiments suggest u‖A‖ suffices. (b) Chen (arXiv 2608.21268): the bound depends on the fourth root of the accuracy parameter and carries hidden polynomial factors, proofs 'gory'; Chen's own Theorem 4.6 (not Greenbaum's) gives symmetric N x N matrices S and T-tilde with N = nk, T-tilde tridiagonal with leading k x k block exactly the computed T_k, and ‖S - T-tilde‖ of order u‖A‖ up to polynomial factors in k, with starting weights preserved exactly. (c) Meurant-Strakos: cubic polynomial factor times a max of u‖A‖ and the f_j. These are mutually inconsistent as stated, so the exponent of u in Greenbaum's published width cannot be read off the secondary literature.
- Hypotheses and notation: As above.
- Page / theorem / equation: Simonova-Tichy Section 1 (as digested); Chen 2608.21268 Section 8, eq. (7.10), Theorem 4.6, Lemmas 4.1-4.5; Meurant-Strakos Theorem 4.9.
- Reading evidence and limitations: The L3 kill test needs delta(eps); until the original (LAA 113, open archive) is read, any delta(eps) quoted from the literature must carry this uncertainty. Chen's Theorem 4.6 is a recent simplified model of the same type; its record belongs to chen-2026 (not edited here).  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: quantifies what 'Greenbaum-type delta = O(eps)' would have to match.

### LIT?bivariate-lanczos-claude-447 — author's talk abstract: the old interval bound is not as small as one might hope; width of order eps‖A‖ argued

- Verification: **Secondary report only** (the source itself NOT read). UNVERIFIED. `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Greenbaum's own talk abstract (Prague, undated; seminar-nm.karlin.mff.cuni.cz, praguetalk1abs.pdf) confirms LAA 113 (1989) 7–63 and says the interval bound of the 1989 paper was not as small as one might hope, and sets out to argue that the widths are of order eps‖A‖. The L3 review lists the secondary accounts of the proven width as in conflict: sqrt(eps)‖A‖ (Šimonová–Tichý), the fourth root of the accuracy parameter (Chen, citing eq. (7.10)), and a max-form with unquantified f_j (Meurant–Strakoš).
- Hypotheses and notation: Perturbed Lanczos/CG recurrences.
- Page / theorem / equation: LAA 113 (1989) 7–63 (talk abstract); eq. (7.10) cited by Chen.
- Reading evidence and limitations: Talk abstract only; the 1989 paper was not read. Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): The L3 reviewer concludes that the L3 development statement '1D Greenbaum width sqrt(eps) (proven)' (R03 §3 and lit_reading.md) is NOT supported until the paper is read, and that the R03 remark that the sqrt(eps) rate of PD-T?bivariate-lanczos-claude-303(d) matches the 1D Greenbaum width should be withdrawn or marked as conflicting. This sharpens statement 209.

## Search and attribution notes

Year 1989 is supported by the Simonova-Tichy abstract; journal/volume/pages are from memory. See greenbaum-1979 for the repository mix-up. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: the DOI resolved (the earlier redirect failure was a tool limit). The three secondary accounts of the width of the eigenvalue intervals disagree (statement 209), so no delta(eps) is taken from the literature here. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L3 prior-art review 2026-10-31 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): metadata and abstract confirmed; statements 207-209 added; coverage upgraded from 'not read; metadata NOT confirmed' to 'metadata + abstract'.

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): L3 prior-art review's confirmation of the citation by Greenbaum's talk abstract and the withdrawal requirement for the '1D width sqrt(eps) (proven)' statement recorded as statement 447; the paper itself is still unread (pending-reference).
