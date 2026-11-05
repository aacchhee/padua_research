# P1 bounded literature checkpoint — simplex and discrete triangle

Reader: Codex, assigned gpt-6.1-sol xhigh; runtime-resolved model metadata
is not exposed. Access/reading date: 2026-11-05. This is a source record,
not a mathematical proof record or a priority claim. Provisional LIT IDs
below remain subject to the coordinator's final allocation.

## Xu2015 — Yuan Xu, Hahn, Jacobi, and Krawtchouk polynomials of several variables

- Journal citation: Journal of Approximation Theory 195 (2015), 19–42.
- DOI: <https://doi.org/10.1016/j.jat.2014.03.013>.
- Journal URL: <https://www.sciencedirect.com/science/article/pii/S0021904514000574>.
- Fulltext read: <https://arxiv.org/html/1309.1510v1>, title spelling
  “Krawtchouck”; submitted 5 September 2013, 22-page preprint.
- PDF counterpart acquired by browser: <https://arxiv.org/pdf/1309.1510>.
- Reading coverage: **complete preprint full text**, sections 1–5 and
  references. Overlapping bounded HTML displays covered mathematical text
  and references at lines 0–786, with explicit gap filling at 443–520.
  Extracted PDF text around Proposition 2.1 and Propositions 2.5–2.8 was
  additionally inspected. This is not a full read of the journal version.
- Named gaps: formula rendering has apparent transcription/typographical
  problems. No formula from this conversion is adopted without a fresh
  derivation or a clean PDF check. PDF screenshot calls failed with the
  tool message “content type is not application/pdf”.

### LIT?lanczos-nonproduct-codex-P1-01 — standard simplex/Hahn basis formulas

- Statement in faithful paraphrase: The preprint gives mutually orthogonal
  Jacobi bases and their squared norms on a simplex, multivariate Hahn
  bases and norms on a discrete simplex, and a relation between these
  norms. It obtains connection identities from generating functions and
  formulas for reproducing kernels and nonnegative Poisson kernels.
- Hypotheses and notation: simplex Jacobi exponents satisfy
  `kappa_i > -1`; discrete total count is `N`, with degrees at most `N`.
  Inner products are normalized. The Hahn weight in (2.3), after
  normalization, corresponds to P1's parameters `a_i=kappa_i+1`.
- Page / theorem / equation: preprint pp. 5–8, Proposition 2.1,
  equations (2.8)–(2.9), Proposition 2.6, Corollary 2.7,
  equations (2.18)–(2.19); connection identities in section 3;
  kernel results in sections 4–5.
- Reading evidence and limitations: complete text read, no independent
  verification of all source proofs. The campaign code uses its own
  rational moment/Gram construction, not imported source formulas.
- Relation to campaign claims: **LITERATURE**. The support and weight
  families and explicit orthogonal bases are established antecedents.
  The paper does not establish a comparison of this campaign's ordered,
  frozen BJ/mirror/alternating aggregate creator capacities. No N2/N3
  conclusion or inherited proof status follows.

## DunklXu2014 — Orthogonal Polynomials of Several Variables, second edition

- Authors: Charles F. Dunkl and Yuan Xu; Cambridge University Press, 2014,
  Encyclopedia of Mathematics and its Applications 155.
- Book DOI: <https://doi.org/10.1017/CBO9781107786134>.
- Chapter 5 DOI: <https://doi.org/10.1017/CBO9781107786134.007>.
- Exact chapter landing page:
  <https://www.cambridge.org/core/books/abs/orthogonal-polynomials-of-several-variables/examples-of-orthogonal-polynomials-in-several-variables/485109A71BD36A194B6BC616D95BC371>.
- Frontmatter:
  <https://assets.cambridge.org/97811070/71896/frontmatter/9781107071896_frontmatter.pdf>.
- Reading coverage: metadata/contents/landing page only. The contents locate
  section 5.3, Classical Orthogonal Polynomials on the Simplex, at p. 150;
  Chapter 5 spans pp. 137–173. The chapter page explicitly offers a preview
  and “Get access”, not the chapter's full text. The DOI resolver was not
  accessible through the browser tool. **No chapter theorem is cited.**
- Named gap: full simplex chapter acquisition and reading remain deferred.
  The 2001 first edition and 2014 second edition must not be conflated.

## GriffithsSpano2013 — Orthogonal polynomial kernels and canonical correlations for Dirichlet measures

- Authors: Robert C. Griffiths and Dario Spanò; Bernoulli 19(2) (2013),
  548–598. DOI: <https://doi.org/10.3150/11-BEJ403>.
- Preprint: <https://arxiv.org/abs/1003.5131>, version 2, 20 March 2013.
- Acquired fulltext: <https://arxiv.org/html/1003.5131v2> and the author's
  51-page journal PDF at
  <https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/spano/pub/bej403.pdf>.
- Reading coverage: abstract, contents and opening introduction only;
  HTML lines 0–96 and extracted journal PDF pp. 548–551. Acquisition is
  **not** a complete fulltext read. **No source theorem is cited.**
- Named gap: sections 2–3 and 5–6 contain candidate continuous/discrete
  kernel material but were not read in this bounded round. The full source
  remains available for targeted future reading if a concrete obligation
  requires it. No result of Xu's references is credited as our own read.

## Tratnik1989 — metadata and unsuccessful access only

- M. V. Tratnik, Multivariable Meixner, Krawtchouk, and Meixner–Pollaczek
  polynomials, Journal of Mathematical Physics 30 (1989), 2740–2749,
  DOI: <https://doi.org/10.1063/1.528507>.
- M. V. Tratnik, Multivariable biorthogonal Hahn polynomials,
  DOI: <https://doi.org/10.1063/1.528430>.
- Reading coverage: bibliographic discovery only. Both DOI resolver URLs
  returned “not accessible via this tool”. A reliable journal article URL
  or public fulltext was not acquired within the budget. A guessed AIP
  article URL also failed; its failure is not evidence about the actual
  publisher article's accessibility. **No theorem or formula is cited.**
- Named gap: acquire and inspect full texts before distinguishing these
  biorthogonal families from the positive simplex Hahn family used here.
  The different 1988 continuous Hahn article, DOI 10.1063/1.527898, was
  merely discovered and is not a source for the present finite lattice.

## Search and attribution notes

Discovery used the available `search_service_web_run` connector, including
queries for Yuan Xu Hahn/simplex/triangle fulltexts; Dunkl–Xu simplex
chapter/DOI; Tratnik multivariable Hahn/Krawtchouk/1989/DOI; the exact Xu
title and DOI; and Griffiths–Spanò's exact Dirichlet-kernel title. Search
snippets were used to locate primary sources and verify citation metadata,
not as theorem evidence. Xu's author publication list supplied additional
locators, including `pages.uoregon.edu/yuan/paper/Discrete.pdf`; that URL
was not accessible through the browser tool and was not read.

The Xu journal article URL returned browser `403 Forbidden`; its DOI URL
returned “not accessible via this tool”. Its arXiv fulltext was accessible.
Direct workspace download of `https://arxiv.org/pdf/1309.1510`, using Python
urllib under `exec_command` with additional network permission, failed once
with `URLError: Tunnel connection failed: 403 Forbidden`. No proxy or
network-policy workaround was attempted. The browser's independent public
retrieval succeeded; no downloaded source PDF or source extract is in Git.

The applicable environment runtime skill and its network reference were
read. The reported network policy was enforced and restricted; no credentials
were needed. None of the above browser failures is an automatic approval
rejection. No claim of global unreachability is made.

## Campaign disposition and history

2026-11-05, P1 round 3: prospectively bounded discovery/read checkpoint,
started 22:21:28 UTC, completed within ten minutes. One complete primary
preprint read is newly documented; other acquisition and reading limits
are explicit. The nonproduct admission P1-01 and exact finite probe P1-02
remain local results with their previous statuses. N2 remains
INCONCLUSIVE; N3 remains REDIRECT TO P4; the all-degree triangle capacity
separation remains OPEN. No new family proof or priority claim is made.

Next sufficient obligation: certify an upper bound for the full response
matrix over the entire triangle, together with a lower witness and the
normal/source factors. The proposed absolute-entry Bernstein envelope is
an untested possible certificate, not a result supplied by these sources.
