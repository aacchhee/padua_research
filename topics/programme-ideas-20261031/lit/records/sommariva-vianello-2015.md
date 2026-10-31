# sommariva-vianello-2015 — A. Sommariva and M. Vianello, "Compression of multivariate discrete measures and applications", Numerical Functional Analysis and Optimization 36(9) (2015) 1198–1223

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator)

- DOI / URL / supplied location: DOI 10.1080/01630563.2015.1062394 (from the inputs; not printed in the pages read, UNVERIFIED). Supplied location: AC local copy `/home/claude/inputs/papers/Compression of Multivariate Discrete Measures and Applications.pdf` (not copied into the repository).
- Access and reading date: 2026-10-31.
- Reading coverage: exact pages — journal p. 1201 (PDF p. 5) read from the `pdftotext -layout` text layer, plus the reference list entries [23] and [37] (text layer). The rest of the paper (compression algorithms, error bounds, applications) not read. Mapping: journal page = PDF page + 1196.
- Reader, model and effort: Claude Fable 5.1, xhigh (programme-ideas Step-0 literature subagent).
- Named gaps requiring future re-reading: the QR-orthogonalisation construction (eqs (8)–(10)), the compressed least-squares bounds (eq. (33) p. 1217, eq. (36) p. 1220 as the charter record reports), and the WAM applications; the page images were not rendered.
- Shared key: both parallel branches hold secondary-only records (`records_lanczos/sommariva-vianello-2015.md`, LIT?bivariate-lanczos-claude-074; `records_charter/sommariva-vianello-2015.md`, LIT-005). Merge at PR preparation; this record adds the first fulltext check of the HL/seed remark.

## Extracted published statements

### LIT?programme-ideas-claude-25 — fact: assessment of HL 2002 and the seed as discrete-orthogonalisation tools

- Statement in faithful paraphrase: Even an orthogonal basis of a bounding rectangle (total-degree product Chebyshev, eq. (7)) leaves the Vandermonde matrix intractably conditioned at moderate degree. A possible remedy is to orthogonalise with respect to a discrete measure supported on the data set X, computing discrete orthogonal polynomials; "clever" numerical linear algebra algorithms for discrete orthogonalisation of the bivariate monomial basis exist (ref. [23], Huhtanen–Larsen 2002, and ref. [37], Van Barel–Chesnokov 2010). The authors state that these become slow at moderate degrees when the support cardinality is high, that [23] in addition can suffer loss of orthogonality (and thus needs some kind of re-orthogonalisation), and that their use should probably be reserved to situations where no alternative is possible. The paper instead starts from the total-degree Chebyshev basis of a bounding rectangle and handles ill-conditioning by a standard QR of the Chebyshev–Vandermonde matrix.
- Hypotheses and notation: X a finite nd-determining discrete set in R^d; no numbers, timings or orthogonality measurements for [23]/[37] are given in the passage.
- Page / theorem / equation: p. 1201, paragraph before eq. (8) (PDF p. 5); references [23] and [37] in the bibliography (text layer PDF lines near pp. 1221–1223).
- Reading evidence and limitations: Text layer only; the passage is prose and unaffected by formula garbling. The claim "slow at moderate degree" is unsupported in the passage by data.
- Relation to campaign claims (no inherited proof status): Confirms the round-2 §3 A quotation and attribution. It is a competitor's assessment, not a measurement; it records that loss of orthogonality of HL-type recurrences was known to the Padova group by 2015 and that the seed was judged slow at high support cardinality.

## Search and attribution notes

No web search in this step. The round-2 report quotes the "reserved to situations" phrase at p. 1201; confirmed. Reference numbering: [23] = Huhtanen–Larsen BIT 42 (2002); [37] = Van Barel–Chesnokov, Numer. Algorithms 55 (2010) 383–402 (both checked in the text layer).

## History

- 2026-10-31: record created from a text-layer reading of p. 1201 and the reference list (claude-fable-5-1, xhigh).
