# L1 prior-art check 01 — mechanisms (a)–(f)

- Reviewer: Claude Opus 5.5, effort high (independent prior-art checker; not the L1 developer).
- Date: 2026-10-31. Rules/base as in `plan.md`. Scope: L1 rounds R01–R03 (`directions/L1/R01.md`–`R03.md`, `STATUS.md`) and the six candidate mechanisms named by the orchestrator.
- Authorization: AC authorized reading related literature and fulltexts anywhere on the net (coordinator message, 2026-10-31 23:00). No fulltext or long extract is stored in the repository. Working notes (short quotes and locators only) are in the session scratchpad, outside the repo.
- **How fulltexts were read.** Every "fulltext" read below went through WebFetch, where a summarising model answers a prompt against the fetched page. This is **not verbatim reading by me**. Quotes are as that model returned them (≤ 25 words each), and locators are the model's reading of running headers. Any statement that matters for a claim must be re-checked against the PDF before it is cited in a paper.
- **This review makes no novelty claims.** "No matching result found in the documented search" means only that: it covers the queries, dates and limits logged below.

## Search log (2026-10-31)

Repository first: `literature/INDEX.md` (bivariate-lanczos rows) and the records huhtanen-larsen-bit-2002, huhtanen-larsen-simax-2002, huhtanen-simax-2002, bartels-jezioranski-1985, zaccaron-2014, zhu-nakatsukasa-2026, brubeck-nakatsukasa-trefethen-2021, hokanson-2020, liu-narayan-2023, meurant-sommariva-2019, fasondini-olver-xu-2023, sommariva-vianello-2015, faghih-et-al-2025, faghih-vanbarel-vandebril-2026, freund-2000, aliaga-boley-freund-hernandez-2000, sinha-2026, carson-et-al-2025, simon-1984-mathcomp, simon-1984-laa, larsen-1998, jia-li-2021, gautschi-1982, humet-2019, kressner-2018; also `lit/search-log.md`.

Web searches (WebSearch; S = standard, E = extended):

| # | Mode | Query (abridged) | Useful hits |
|---|---|---|---|
| 1 | S | Barrio Peña Sauer three term recurrence evaluation multivariate OP left inverse stability | Liu–Narayan |
| 2 | S | Liu Narayan Stieltjes multivariate 2202.04843 | arXiv, SISC |
| 3 | E | multivariate Lanczos loss of orthogonality short recurrence bivariate OP non-tensor | none new (FOX 2023 SAPM page) |
| 4 | S | "Three term recurrence for the evaluation of multivariate orthogonal polynomials" | ScienceDirect page (blocked) |
| 5 | S | multivariate V+A Lanczos short recurrence Hokanson | Hokanson 2009.10803, Zaccaron PDF, ZN ar5iv |
| 6 | E | Barrio Peña Sauer multivariate OP evaluation Clenshaw stability JAT 162 | Waldron 2011, ScienceDirect |
| 7 | E | Barrio Peña Sauer abstract doi 10.1016/j.jat.2009.07.005 | nothing usable |
| 8 | S | zaguan.unizar.es Barrio Peña Sauer pdf | nothing usable |
| 9 | E | Tomas Sauer publications three term recurrence | nothing usable |
| 10 | S | Olver Slevinsky Townsend fast algorithms OPs multivariate Lanczos | OTV 2019 SISC (par.nsf.gov) |
| 11 | E | bivariate discretized Stieltjes stability triangle disk block Jacobi | Liu–Narayan, Gautschi 1982 (Purdue) |
| 12 | E | multivariate OP recurrence "left inverse" choice stability D_n Xu | nothing new |
| 13 | E | Sommariva Vianello Lanczos-like bivariate loss of orthogonality polygon | nothing new |
| 14 | E | multivariate Krylov commuting matrices two-directional Arnoldi / bivariate Krylov | Kressner 2018 (already recorded) |
| 15 | S | Delgado Geronimo Iliev Marcellán two variable OPs structured matrices | metadata only (not read) |
| 16 | E | block Lanczos growing/increasing block size stability multivariate OP | nothing new |
| 17 | E | omega-recurrence partial reorthogonalization block / JBD / two matrices | Simon 1984 (AMS PDF) |
| 18 | E | Lanczos normal matrices Elsner–Ikramov finite precision Ritz polyanalytic | nothing new |
| 19 | E | Forsythe OPs two variables surface fitting stability | nothing new |
| 20 | S | Meurant Sommariva low Lebesgue constant disk HL | Meurant 2014 slides |
| 21 | S | Xu lecture notes OPs several variables left inverse D_n | Xu survey arXiv 1701.02709 |
| 22 | E | Barrio Sauer Peña generalized inverse / pseudoinverse multivariate Clenshaw | nothing new |
| 23 | S | two-directional Arnoldi Li Bai Su Zeng | Li–Bai–Su–Zeng 2007 (UC Davis PDF) |
| 24 | E | "Huhtanen" "Larsen" bivariate OP instability disk triangle | Meurant 2014 slides; OSTI Austin et al. (blocked) |

Pages fetched: arXiv 2202.04843 (PDF ×3, ar5iv ×1), Zaccaron thesis PDF (×2), arXiv 2301.12241 (PDF, ar5iv), arXiv 2009.10803 (abs, PDF), arXiv 1911.09988 PDF, arXiv 2609.08066 PDF, arXiv 1701.02709 PDF, arXiv 2211.06999 PDF, par.nsf.gov 10158662 (OTV 2019), AMS Math. Comp. 42 PDF (Simon 1984), UC Davis libaisuzeng07.pdf, ncmm.karlin.mff.cuni.cz attachment 237, Springer page of Waldron 2011, Crossref (BPS 2010, Liu–Narayan, OTV), OpenAlex (BPS 2010, HL BIT).

**Coverage limits.**
- Blocked or unreachable: ScienceDirect and linkinghub (so **Barrio–Peña–Sauer 2010 was not read**), OpenAlex citation-filter queries (so no forward-citation chase of HL BIT 2002, 11 citations, or BPS 2010, 14 citations), osti.gov and core.ac.uk (robots), the Semantic Scholar API, and direct curl to arXiv (proxy 403).
- Not searched: zbMATH, MathSciNet, Google Scholar, and non-English literature.
- Not read: Dunkl–Xu 2014; Xu SIAM J. Math. Anal. 1993 and Trans. AMS 1994; Delgado–Geronimo–Iliev–Marcellán; Grimes–Lewis–Simon block shift-invert Lanczos; Ye 1996 adaptive block Lanczos; Austin et al. multivariate rational approximation. Sinha 2026 was read only through §7.1 (Theorem 7 not seen).

---

## (a) Exponential loss off product supports, before Ritz convergence; product supports behave like univariate Lanczos

**Closest prior statement.** M. Zaccaron, *Discrete orthogonal polynomials and hyperinterpolation over planar regions*, M.Sc. thesis, Univ. Padova, 25 July 2014 (advisor M. Vianello, co-advisor A. Sommariva). Fulltext read via WebFetch.
- **Table 2.1, p. 16.** HL-type window recurrence (Alg. 1.2: K once per cycle, then H repeatedly; window ≤ 2k+1, Thm 3). Quadrangle with vertices (−1,−1), (2,0), (1,1), (−2,2); WAM nodes, M = (n+1)²; uniform weights. ‖QᵀQ − I‖∞ by degree: 6.7e−16 (5), 1.2e−13 (10), 2.6e−11 (15), 9.8e−9 (20), 3.3e−6 (25), 6.1e−3 (30), 0.24 (35), 0.38 (40), 0.50 (60).
- **Table 2.2, p. 16.** At degree 60: square A = (±1,±1) gives 6.0e−14; quadrangle B gives 0.22; quadrangle C = (−1,0), (0,−1), (1,0), (0,1) gives 0.74. **C is the square rotated by π/4.**
- **p. 16.** "the loss of orthogonality of Lanczos vectors depends strongly on the geometry of the domain and the location of the nodes".
- **p. 17.** "In the present case bounds are not available".
- **p. 18, §2.6.** "We expect a situation similar to the univariate Lanczos" (ghost eigenvalues). This is an expectation, not data.

Other prior observations, all qualitative and with no data or mechanism:
- HL BIT 2002 p. 401 and HL SIMAX 2002 p. 1088 (records 111 and 119): finite-precision behaviour is "similar" to Lanczos.
- G. Meurant, slides "The computation of sets of points with small Lebesgue constant using bivariate orthogonal polynomials", Sept. 2014 (slide "Bivariate orthogonal polynomials"): HL "suffers more from rounding errors", and orthogonality is generally lost, so Sommariva's practice is to reorthogonalize twice.
- Sommariva–Vianello 2015 p. 1201 (secondary, record 074).

**Relation.**
- Zaccaron already records the domain dependence: square fine, rotated square and general quadrangles bad. The growth is geometric from low degree, roughly half a decade per degree in Table 2.1, starting at degree ~10. **The observed phenomenon is therefore known.**
- Not found in the documented search:
  - the tensor/product versus non-product dichotomy as a stated principle;
  - the claim that the growth precedes Ritz convergence;
  - the claim that product supports reproduce univariate Lanczos behaviour.
- The prior expectation in the literature is the opposite of the last two: HL and Zaccaron expect generic Lanczos-type, Ritz-driven behaviour.
- One open point affects whether Zaccaron's square A is a product support. The WAM construction on the quadrangles is not stated in the text I received; it is presumably a mapped tensor Chebyshev–Lobatto grid. **This needs checking.**

**Verdict: partially known.**
- **Kills the novelty of the bare observation.** Any write-up must cite Zaccaron Tables 2.1–2.2 as a prior measurement on the rotated square.
- The explanatory parts (product versus non-product; before Ritz convergence; univariate behaviour on product measures): no matching result found in the documented search.

## (b) Cause: triangular one-relation-per-column selection of the overdetermined bivariate Jacobi relations; propagator = inverse of the selection; property of the exact recurrence

**Closest prior statements.**
1. Y. Xu, "Orthogonal polynomials of several variables", survey, arXiv:1701.02709. Fulltext via WebFetch.
   - §2.2, eq. (2.14): P_{n+1} = Σ x_i D_{n,i}ᵀ P_n + E_n P_n + F_n P_{n−1}, with D_nᵀ A_n = I. The text says "Such a matrix is not unique".
   - Thm 2.11 gives the conditions under which this recursion yields orthonormal polynomials. The original sources (Xu 1993/1994; Dunkl–Xu 2014 §3.3) were not read.
2. Z. Liu, A. Narayan, "A Stieltjes algorithm for generating multivariate orthogonal polynomials", SIAM J. Sci. Comput. 45(3) (2023) A1125–A1147. Fulltext via WebFetch. Thm 3.1, eq. (9): p_{n+1} is obtained by stacking the d relations. The proof says "Although this stacked system is overdetermined, it is consistent", and solves it with Bᵀ_{n+1} (Λ_{n+1} diagonal).
3. S. Olver, A. Townsend, G. Vasil, "A sparse spectral method on triangles", SIAM J. Sci. Comput. 41(6) (2019) A3728–A3756. Fulltext via WebFetch. §2.3: the stacked x/y system "is not lower triangular and so we cannot immediately invert this system via forward recurrence", so they multiply by pseudo-inverses B_n⁺ (eq. 2.10).
4. **R. Barrio, J. M. Peña, T. Sauer, "Three term recurrence for the evaluation of multivariate orthogonal polynomials", J. Approx. Theory 162(2) (2010) 407–420, doi:10.1016/j.jat.2009.07.005.** Metadata only (Crossref, OpenAlex; bronze open access). **Not read.**

**Relation.**
- The algebraic frame is known: a consistent overdetermined system of d three-term relations, and a non-unique left inverse that defines a forward recursion. The window recurrence's triangular selection is a **special case** (one particular D_n) of Xu's non-unique left inverse.
- Not found: the identification of the BJ/HL window recurrence as forward substitution for a triangular selection; its error propagator equal to the inverse of that selection; the finding that the choice of left inverse decides floating-point stability.
- None of the sources read compares left inverses numerically. Liu–Narayan state they do not analyse that choice; OTV choose B⁺ for cost/structure reasons.

**Verdict: partially known** (algebraic structure known; stability mechanism: no matching result found in the documented search).
- **High-risk unread source: Barrio–Peña–Sauer 2010.** Its title says it is about using three-term recurrences to *evaluate* multivariate OPs, which is exactly where a choice-of-left-inverse stability statement would sit. It must be read before any priority statement on (b) or (c).

## (c) Remedy: two-relation block recurrence (x and y products of the previous blocks, truncation to blocks n−2, n−1) plus SVD/QR completion

**Closest prior statements.**
1. Liu–Narayan 2023 (as in (b)). Fulltext via WebFetch.
   - The multivariate Stieltjes (MS) procedure forms x_i p_n − A_{n+1,i} p_n − Bᵀ_{n,i} p_{n−1} for **every** coordinate i. This is the same three-term truncation (Eq. 24).
   - Coefficients: A from S_{n,i} (Eq. 25), B from an eigendecomposition of T_{n,i,i} (Eq. 26), a "truncated SVD" (Eq. 20) and mixed moments (Eqs. 28–30, d = 2). p_{n+1} from all relations jointly (Eq. 9).
   - Run on discrete measures (empirical, M = 10⁸, §6.2) on non-tensor domains: annulus, region between spirals, torus, square with hole, Madagascar.
   - Reported only qualitatively as better than moment methods: on the annulus MS "performs better ... for large degrees"; on the square with a hole the error is "notably increased". No orthogonality numbers in the text. No comparison with a one-relation Lanczos/HL recurrence (HL and BJ are not cited).
2. M. Fasondini, S. Olver, Y. Xu, "Orthogonal polynomials on a class of planar algebraic curves", Stud. Appl. Math. (2023), doi:10.1111/sapm.12582, arXiv:2211.06999. Fulltext via WebFetch. §§5.2, 5.4: block Lanczos in coefficient space applying both X and Y; no stability discussion.
3. Remedies by reorthogonalization:
   - Zaccaron 2014 Methods 1–2 (§2.4; QR twice, or GS twice against all vectors; O(M n⁴)).
   - Hokanson 2020 Alg. 2.1 (CGS twice against all previous columns).
   - Zhu–Nakatsukasa 2026 (CGS twice; Remark 3: "subject to a loss of orthogonality due to numerical cancellation").

**Relation.**
- The block three-term Stieltjes procedure that uses all coordinate relations with an eigen/SVD completion is **known as an algorithm** (Liu–Narayan). The campaign's recurrence is the same idea, or a close variant; equivalence of the completions is not checked.
- Not found: a measured statement that, at the same truncation, using both relations removes an instability that the one-relation window recurrence shows on the same non-product supports.

**Verdict: partially known.**
- **Liu–Narayan should be cited as the algorithmic predecessor of the remedy.** It removes novelty of the remedy as an algorithm.
- The comparative stability statement: no matching result found in the documented search.

## (d) Exact 2D ω-recurrence for the window recurrence (rounding sources plus commutator residual)

**Closest prior statements.**
1. H. D. Simon, Math. Comp. 42 (1984) 115–142. Fulltext via WebFetch (AMS PDF).
   - Thm 1, eq. (3.2), p. 117: ω_jk obeys a second-order recurrence that is exact in the local rounding vectors (terms q_jᵀf_k − q_kᵀf_j).
   - §5, eq. (5.1), p. 121: the unknown terms are simulated with random values.
   - Thm 2, p. 119: semi-orthogonality (proof deferred to his ref. [20]).
   - Nothing on several matrices.
2. Coupled single-recursion processes (abstract or secondary only): Larsen 1998 (Golub–Kahan, PROPACK); Jia–Li 2021 (joint bidiagonalization).
3. M. Sinha, arXiv:2609.08066. Read via WebFetch up to §7.1. No ω-recurrence. Its Corollary 4 relation (54) is AV = VT + W H (E_k^inj)ᵀ + F, which contains an "injection" term (see (e)).

**Relation.** Same template (Simon's exact identity), extended here to two operators, a window recurrence and a commutator-residual source. Not found: an ω-recurrence for two commuting operators, or one with a commutator-residual source.

**Verdict: partially known** (template known; 2D/window/commutator form: no matching result found in the documented search). The exactness of the identity is not itself new; Simon's eq. (3.2) is already exact.

## (e) The graded total-degree spaces are not a band/block Krylov sequence of one operator commuting with X, Y with a fixed number of starts

**Closest prior statements.**
1. Zhu–Nakatsukasa, arXiv:2301.12241 / IMA J. Numer. Anal. 46(4) (2026), §3: "Unlike the 1D Arnoldi algorithm, the multivariate monomial basis does not correspond to a Krylov subspace" (fulltext via WebFetch).
2. Hokanson, arXiv:2009.10803, §2: "the basis no longer corresponds to a Krylov subspace" (fulltext via WebFetch).
3. Y.-T. Li, Z. Bai, Y. Su, X. Zeng, "Parameterized model order reduction via a two-directional Arnoldi process", IEEE (2007), pp. 868–873. Fulltext via WebFetch. §IV and appendix: each block spans a Krylov subspace of an **enlarged bordered matrix** A[j], b[j]. That is a single operator on a larger space and is not commuting with X, Y.
4. Band Lanczos (one matrix, a block of starts with deflation): Freund 2000 and Aliaga–Boley–Freund–Hernández 2000, secondary only.
5. Sinha 2026 Cor. 4, relation (54), with an E_k^inj term (fulltext via WebFetch, partial). Whether this models vectors injected after the start was not resolved.

**Relation.**
- The informal statements (1, 2) are **weaker**: no commuting-operator qualifier, no fixed-start count, no proof.
- Li–Bai–Su–Zeng is a **different** construction.
- Not found: the precise obstruction. That obstruction is that no A commuting with X and Y and no m fixed starts reproduce S_m and S_{m+1}, so ≥ n start vectors are needed. Also not found: the "one start injected per degree" characterization.

**Verdict: partially known** (weaker informal statements known; the obstruction as stated: no matching result found in the documented search).
- **Sinha 2026 must be read in full (Thm 7, Cor. 4, the meaning of E^inj) before the "injected-start band Lanczos" framing or the growing-block Paige identity (PD-T?…-103) is called new.** It is the most likely source of overlap here.

## (f) Loss governed (or not) by Ritz values of H_x + iH_y (HL SIMAX 2002 p. 1088)

**Closest prior statement.**
- HL SIMAX 2002 p. 1088 (record 119, fulltext): loss "appears closely connected to the convergence of Ritz values" of the square part of N_k (eq. 4.2). An observation with no data.
- HL BIT 2002 p. 401 (record 111): similar to Lanczos, no Ritz values mentioned.
- Zaccaron 2014 §2.6, p. 18: expects univariate-Lanczos-like ghost behaviour.
- The literature on finite-precision Lanczos for normal matrices: nothing found (search 18).

**Relation.** The campaign's R01 result (K1 and K2 fire; neither joint nor single-section Ritz pairs govern loss off product supports) is a test of that observation. It contradicts the prior expectation and is **different** in content from it.

**Verdict:** the conjectural link is **known as an informal observation only**. No quantitative test of it, and no refutation of it, was found in the documented search.

---

## Sources that would kill or limit novelty (flags)

1. **Zaccaron 2014 Tables 2.1–2.2 (p. 16)** limits (a). The rotated square (C) and general quadrangles lose orthogonality while the square does not, and the growth is geometric from degree ~10. Cite it. This also **resolves the "two inconsistent reports" in record zaccaron-2014**: both are rows of the same Table 2.1 (0.38 at degree 40 and 0.499 at degree 60), and both remedies (QR twice, GS twice) are in §2.4.
2. **Liu–Narayan 2023** limits (c): an all-relations block Stieltjes procedure with SVD/eigen completion. It also covers the "consistent overdetermined stacked system" part of (b).
3. **Barrio–Peña–Sauer 2010 (unread)** is a potential kill for (b) and (c). Read it first.
4. **Sinha 2026 (partially read)** is a potential overlap for (e) and for the growing-block Paige identity (E^inj term). Read in full.
5. **Xu (survey 1701.02709 §2.2; Dunkl–Xu)**: the non-unique left inverse is classical, so (b)'s algebra is a special case of it.

## Recommended literature records

| Key | Citation | URL / DOI | Coverage now |
|---|---|---|---|
| zaccaron-2014 (upgrade) | M. Zaccaron, *Discrete orthogonal polynomials and hyperinterpolation over planar regions*, M.Sc. thesis, Univ. Padova, 2014 | https://www.math.unipd.it/~alvise/TESI_STUDENTI/ZACCARON/ZACCARON_prefinale.pdf | fulltext via WebFetch (Ch. 1–2, Tables 2.1–2.2, §§2.3–2.6); WAM construction not seen |
| liu-narayan-2023 (correct) | **Zexin** Liu, A. Narayan, "A Stieltjes algorithm for generating multivariate orthogonal polynomials", SIAM J. Sci. Comput. 45(3) (2023) A1125–A1147 | doi:10.1137/22M1477131; arXiv:2202.04843 | fulltext via WebFetch (§§1–3, 5.2, 6 text; figures not inspected); the record's "Y. Liu" is wrong |
| barrio-pena-sauer-2010 (new) | R. Barrio, J. M. Peña, T. Sauer, "Three term recurrence for the evaluation of multivariate orthogonal polynomials", J. Approx. Theory 162(2) (2010) 407–420 | doi:10.1016/j.jat.2009.07.005 | metadata only; **must read** |
| olver-townsend-vasil-2019 (new) | S. Olver, A. Townsend, G. Vasil, "A sparse spectral method on triangles", SIAM J. Sci. Comput. 41(6) (2019) A3728–A3756 | doi:10.1137/19M1245888; https://par.nsf.gov/servlets/purl/10158662 | fulltext via WebFetch (§§2.2–2.4) |
| xu-2017-survey (new) | Y. Xu, "Orthogonal polynomials of several variables", arXiv:1701.02709 | https://arxiv.org/abs/1701.02709 | fulltext via WebFetch (§2.2) |
| dunkl-xu-2014 (new, pending) | C. F. Dunkl, Y. Xu, *Orthogonal Polynomials of Several Variables*, 2nd ed., CUP 2014 | — | not read (locator for the left-inverse recursion) |
| li-bai-su-zeng-2007 (new) | Y.-T. Li, Z. Bai, Y. Su, X. Zeng, "Parameterized model order reduction via a two-directional Arnoldi process", IEEE (2007) 868–873 (venue name not seen) | https://www.cs.ucdavis.edu/~bai/publications/libaisuzeng07.pdf | fulltext via WebFetch |
| meurant-2014-slides (new) | G. Meurant, "The computation of sets of points with small Lebesgue constant using bivariate orthogonal polynomials", slides, Sept. 2014 | https://ncmm.karlin.mff.cuni.cz/db/attachments/single/237 | fulltext via WebFetch |
| hokanson-2020 (correct) | J. M. Hokanson, "Multivariate rational approximation using a stabilized Sanathanan–Koerner iteration", arXiv:2009.10803 (22 Sep 2020) | https://arxiv.org/abs/2009.10803 | fulltext via WebFetch (§2, Alg. 2.1); the record's title is wrong |
| fasondini-olver-xu-2023 (correct) | M. Fasondini, S. Olver, Y. Xu, "Orthogonal polynomials on a class of planar algebraic curves", Stud. Appl. Math. (2023) | doi:10.1111/sapm.12582; arXiv:2211.06999 | fulltext via WebFetch (§§5.2, 5.4) |
| zhu-nakatsukasa-2026 (upgrade) | as recorded | arXiv:2301.12241 | fulltext via WebFetch (§§2–3, Remark 3); Alg. 4 / App. B not seen |
| brubeck-nakatsukasa-trefethen-2021 (upgrade) | as recorded | arXiv:1911.09988 | fulltext via WebFetch (§4 quote confirmed; no multivariate section) |
| simon-1984-mathcomp (upgrade) | as recorded | AMS PDF | Thm 1 eq. (3.2) p. 117, eq. (5.1) p. 121, Thm 2 p. 119 via WebFetch |
| sinha-2026 (upgrade, gap) | as recorded | arXiv:2609.08066 | read via WebFetch to §7.1; Cor. 4 / eq. (54) E^inj noted; Thm 7 **not seen** |
| austin-et-al (new, pending) | Austin et al., multivariate rational approximation (cited by Hokanson as the source of multivariate V+A) | OSTI 1656649 (blocked) | not read |
| waldron-2011 (optional) | S. Waldron, "Recursive three-term recurrence relations for the Jacobi polynomials on a triangle", Constr. Approx. 33(3) (2011) 405–424 | doi:10.1007/s00365-010-9114-7 | abstract page only; no stability content |
