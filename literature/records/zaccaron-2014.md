# zaccaron-2014 — M. Zaccaron, Discrete orthogonal polynomials and hyperinterpolation over planar regions, M.Sc. thesis, Università di Padova, 25 July 2014 (advisor M. Vianello, co-advisor A. Sommariva); title and date from the L1 prior-art review

- DOI / URL / supplied location: https://www.math.unipd.it/~alvise/TESI_STUDENTI/ZACCARON/ZACCARON_prefinale.pdf (URL from the inputs; not fetched by me) Fetched by the L1 prior-art reviewer via WebFetch (2026-10-31).
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see notes/adv_F1_F6_F3.md §1.1(b); notes/verify_algorithmic_problems.md Problem 3; reports/Padua points research since 2010.md; reports/Open problems verification.md §3 A; code/RESULTS.md); original fulltext NOT inspected; the supplying agents report reading it via WebFetch. PR-preparation (2026-11-01) from the L1 prior-art review of 2026-10-31: fulltext via two WebFetch digests of the thesis PDF (Ch. 1–2, Tables 2.1–2.2, §§2.3–2.6); the WAM node construction on the quadrangles was not seen. The earlier 'two inconsistent reports' are rows of one table (see below).
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L1 prior-art review 2026-10-31 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Fulltext: reconcile the two reported tables/figures below (RESOLVED at PR preparation: both are rows of Table 2.1, see statement 433). PR-preparation: Whether the node set of square A in Table 2.2 is a product (tensor) support: the WAM construction on the quadrangles is not stated in the text the reviewer received (presumably a mapped tensor Chebyshev–Lobatto grid; UNVERIFIED). Verbatim check of Tables 2.1–2.2 against the PDF.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-028 — no bounds available (author statement)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: The author states that bounds on the loss of orthogonality of the Lanczos-type bivariate recurrence are not available in the present case.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: p. 17. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §1.1(b); notes/verify_algorithmic_problems.md Problem 3; reports/Open problems verification.md §3 A; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1: author-stated gap; evidence the question is open as of 2014.

### LIT?bivariate-lanczos-claude-029 — measured loss of orthogonality (two inconsistent reports)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Report A (notes/verify_algorithmic_problems.md): Table 2.1, ||Q^T Q - I||_inf = 6.7e-16 (degree 5), 1.2e-13 (10), 9.8e-9 (20), 6.1e-3 (30), 0.38 (40); the repair is full reorthogonalization ('Method 2', O(M N^2)) giving about 1e-15 up to degree 60; basic cost O(16 M n^3/6). Report B (notes/adv_F1_F6_F3.md): Table 2.1 value 0.499 at degree 60 (M = 3721, N = 1891), remedy 'twice is enough'.
- Hypotheses and notation: Plain truncated recurrence, uniform data, unspecified node sets; not resolved from the supplied accounts.
- Page / theorem / equation: Table 2.1; section 2.4. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/verify_algorithmic_problems.md Problem 3 (A); notes/adv_F1_F6_F3.md §1.1(b) (B); reports/Open problems verification.md §2 row 3 repeats 0.38 at degree 40; reports/Padua points research since 2010.md says 'twice is enough'; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1 benchmark datum. INCONSISTENCY between supplying notes (degree/value and remedy) is flagged for the fulltext reader, not resolved. RESOLVED at PR preparation by the L1 prior-art review (2026-10-31): both reports are rows of the same Table 2.1; see statement 433.

### LIT?bivariate-lanczos-claude-433 — Table 2.1: loss of orthogonality of the HL-type window recurrence on a quadrangle, by degree

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Table 2.1 (p. 16): HL-type window recurrence (Alg. 1.2: K once per cycle, then H repeatedly; window at most 2k+1, Thm 3) on the quadrangle with vertices (-1,-1), (2,0), (1,1), (-2,2), WAM nodes with M = (n+1)^2 and uniform weights. The maximum-norm ‖Q^T Q - I‖ by degree: 6.7e-16 (5), 1.2e-13 (10), 2.6e-11 (15), 9.8e-9 (20), 3.3e-6 (25), 6.1e-3 (30), 0.24 (35), 0.38 (40), 0.50 (60). Both earlier 'inconsistent' reports (0.38 at degree 40; about 0.499 at degree 60) are rows of this single table. Both remedies, QR twice and Gram–Schmidt twice against all vectors at cost O(M n^4), are in §2.4 (Methods 1–2).
- Hypotheses and notation: Uniform weights; WAM nodes; window recurrence as above.
- Page / theorem / equation: Table 2.1, p. 16; §2.4.
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source. The identification of 0.50 with the earlier 'about 0.499' at degree 60 is the reviewer's.
- Relation to campaign claims (no inherited proof status): Corrects the 'two inconsistent reports' of LIT?bivariate-lanczos-claude-029. Prior measurement of the geometric growth (about half a decade per degree from degree 10) for the campaign's loss-regime statements PD-T?bivariate-lanczos-claude-107 and PD-T?bivariate-lanczos-claude-112; the bare observation of loss on non-product supports is therefore not new (L1 review verdict 'partially known').

### LIT?bivariate-lanczos-claude-434 — Table 2.2 and remarks: domain dependence on the square, a quadrangle and the square rotated by pi/4

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Table 2.2 (p. 16), degree 60: square A with vertices (+-1,+-1) gives 6.0e-14; quadrangle B gives 0.22; quadrangle C with vertices (-1,0), (0,-1), (1,0), (0,1) gives 0.74. C is the square rotated by pi/4 (the reviewer's observation). p. 16 (as digested): the loss of orthogonality of Lanczos vectors depends strongly on the geometry of the domain and the location of the nodes. p. 17: bounds are not available in the present case. §2.6, p. 18: the author expects a situation similar to univariate Lanczos (ghost eigenvalues); this is an expectation, not data.
- Hypotheses and notation: As for Table 2.1; the node set of square A is not stated in the digested text.
- Page / theorem / equation: Table 2.2, p. 16; p. 17; §2.6, p. 18.
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source. Whether square A is a product support is open (see Named gaps).
- Relation to campaign claims (no inherited proof status): Prior measurement on the rotated square, relevant to PD-T?bivariate-lanczos-claude-105 (product-support factorisation), PD-T?bivariate-lanczos-claude-107 and PD-N?bivariate-lanczos-claude-106 (support shape does not classify the loss regime). The prior expectation of Lanczos-type (Ritz-driven) behaviour is the opposite of the campaign's statements that product supports reproduce univariate behaviour and that the growth precedes Ritz convergence (PD-N?bivariate-lanczos-claude-101). Confirms the author statement LIT?bivariate-lanczos-claude-028 (p. 17).

## Search and attribution notes

reports/Padua points research since 2010.md notes that the thesis's refs [38]/[39] could not be confirmed to be the seed and HL. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L1 prior-art review 2026-10-31 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): title corrected from the L1 prior-art review; coverage upgraded from 'supplied secondary account only' to 'fulltext via WebFetch digests' for Ch. 1–2, Tables 2.1–2.2, §§2.3–2.6; statements 433, 434 added; the 'two inconsistent reports' of statement 029 recorded as rows of one table (Table 2.1) with both remedies in §2.4; original wording of 029 preserved.
