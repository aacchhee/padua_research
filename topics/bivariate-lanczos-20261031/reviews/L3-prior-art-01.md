# L3 prior-art check 01 — mechanisms (a)–(f)

- Reviewer: Claude Opus 5.5, effort high (independent prior-art checker; not the L3 developer).
- Date: 2026-10-31. Scope: L3 rounds R01–R03 (`directions/L3/R01.md`–`R03.md`, `STATUS.md`, `lit_reading.md`) and theory file `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-303-moment-cone-rate-theorem.md` (read for exact hypotheses), against the six mechanisms named by the orchestrator.
- Authorization: AC authorized reading related literature anywhere online (coordinator message, 2026-10-31 23:00). No fulltext or long extract is stored in the repository. Short working notes are in the session scratchpad only.
- **How sources were read.** Every "fulltext" read below went through WebFetch, where a summarising model answers a prompt against the fetched page or PDF. This is **not verbatim reading by me**. Quotes are as that model returned them (at most 25 words each). Locators are the model's reading of theorem numbers and running headers. Any statement that matters for a claim must be re-checked against the PDF before it is cited in a paper.
- **This review makes no novelty claims.** "No matching result found in the documented search" means only that. It covers the queries, dates and limits logged below.

## Search log (2026-10-31)

Repository first: `literature/INDEX.md` (head and the L3-relevant rows) and the records xu-pitman-1994, xu-siam-1994, curto-fialkow-1996, degani-schiff-tannor-2005, collowald-hubert-2018, greenbaum-1989, greenbaum-1979, bos-dmv-xu-2007, harris-simanek-2021. I also read the L3 developer's `lit_reading.md` (Kachkovskiy–Safarov, Koiran, Di Dio–Schmüdgen readings) and `lit/search-log.md`. kachkovskiy-safarov-2016, koiran-2024 and lin-1997 were not re-read: L3 R03 already confirmed them, and none is the closest prior statement for (a)–(f).

| # | Tool / mode | Query or URL (abridged) | Useful result |
|---|---|---|---|
| 1 | WebSearch S | Greenbaum 1989 slightly perturbed Lanczos interval width | Chen handbook 2410.11090, Šimonová–Tichý html, Greenbaum abstract |
| 2 | WebSearch S | Cichoń Stochel Szafraniec recurrence modulo ideal | UJ publication page (metadata only) |
| 3 | WebSearch S | truncated moment problem odd degree Favard block Jacobi truncated | Schmüdgen Ten Lectures; nothing direct |
| 4 | WebSearch S | positive super-resolution dual certificate nonnegative vanishing at nodes | Eftekhari et al., Poon–Peyré, Denoyelle et al. |
| 5 | WebFetch | arXiv 2410.11090 (Chen, Lanczos handbook) | Thm 4.3: informal, no width |
| 6 | WebFetch | arXiv html 2507.16484v1 (Šimonová–Tichý) | §1: √ε‖A‖ proven, ε‖A‖ in experiments; block case open |
| 7 | WebSearch S | Meurant–Strakoš Acta Numerica 2006 | Strakoš homepage PDF |
| 8 | WebFetch | apacz.matinf.uj.edu.pl (CSS 2005 page) | JAT 134 (2005) 11–64; no abstract |
| 9–10 | WebFetch ×2 | karlin.mff.cuni.cz/~strakos/download/2006_MeSt.pdf | §4.3, Thm 4.9 p. 511 (text partly garbled) |
| 11 | WebSearch S | Greenbaum–Strakoš 1992 SIMAX 13 | epubs.siam.org doi 10.1137/0613011 |
| 12 | WebSearch S | truncated moment problem / moment cone boundary / perturbation | Di Dio–Schmüdgen 1703.01497 |
| 13–15 | WebFetch ×3 | ar5iv / arXiv 1703.01497 (Di Dio–Schmüdgen) | Prop. 27, Thm 40, Cor. 41, Lemma 37, Prop. 43 |
| 16 | WebSearch S | Eftekhari Tanner et al. sparse non-negative super-resolution | ar5iv 1804.01490 |
| 17 | WebFetch | ar5iv 1804.01490 | 1D, T-systems, O(δ^{1/7}) |
| 18 | WebSearch E | perturbation of positive cubature, nearby nodes, implicit function | nothing on the mechanism |
| 19 | WebSearch S | Putinar 1997 dilation approach to cubature | DST arXiv (Putinar dilation paper not located) |
| 20 | WebFetch | arXiv math/0408076 (Degani–Schiff–Tannor) | Thms 2, 9–13 |
| 21 | WebSearch S | Delgado–Geronimo–Iliev–Marcellán 2006 | uc3m e-archivo page |
| 22 | WebSearch E | Favard several variables, finite / truncated block Jacobi, last block | Xu Fields notes; Xu Trans. AMS 1994 |
| 23 | WebFetch | darkwing.uoregon.edu/~yuan/paper/fields.pdf (Xu lecture notes) | Thms 3.1, 3.2, 5.1–5.4, 6.1 |
| 24 | WebFetch | uc3m e-archivo (DGIM 2006) | citation and abstract only |
| 25 | WebSearch S | DGIM arXiv version | not found (only the bicircle paper math/0612400) |
| 26 | WebFetch | ams.org Trans. AMS 342 (1994) PDF (Xu) | Thms 3.2, 3.4, 4.2; §2 Favard |
| 27 | WebFetch | arXiv 2008.12698 (Schmüdgen, Ten Lectures) | only Lectures 1–5 returned; Thm 3.5 (1D) |
| 28 | WebSearch S | minimal matrix convex set, dilation, POVM | Passer–Shalit–Solel, DDSS |
| 29 | WebSearch S | Putinar Tchakaloff note; Bayer–Teichmann | AMS pages, arXiv math/0502473 |
| 30 | WebFetch | ams.org PAMS 125 (Putinar 1997) | citation and abstract |
| 31 | WebFetch | arXiv 1706.05654 (Passer–Shalit–Solel) | (1.3)–(1.4), Prop. 2.3, Thm 4.1 |
| 32 | WebSearch S | Blekherman nonnegative polynomials and SOS, faces, double zeros | arXiv 0907.1339 |
| 33 | WebSearch E | positive cubature near given points, √ rate, Hessian obstruction | Lasserre 1105.4448; nothing on the mechanism |
| 34 | WebFetch | ar5iv 0907.1339 (Blekherman) | §3.1, Lemma 3.1, Cor. 3.2, Thm 3.3 |
| 35 | WebFetch | ar5iv 1105.4448 (Lasserre) | Gaussian cubature existence criterion |
| 36 | WebSearch S | CSS 2005 abstract | nothing beyond #2 |
| 37 | WebSearch S | finite-precision Lanczos, commuting, multivariate, Greenbaum-type, two variables | nothing new (1D and block only) |
| 38 | WebFetch | arXiv abs 2608.21268 (Chen 2026) | abstract |
| 39 | WebFetch | arXiv abs 1406.3329 (Xu) | Gaussian cubature family (context) |
| 40–41 | WebFetch ×2 | arXiv PDF 2608.21268 | Thm 4.6; "fourth-root" remark on Gre89 eq. (7.10) |
| 42 | WebSearch S | Greenbaum 1989 LAA 113 title | Greenbaum talk abstract (Prague) |
| 43 | WebFetch | seminar-nm.karlin.mff.cuni.cz …/praguetalk1abs.pdf | LAA 113 (1989) 7–63 confirmed; old bound "not as small as one might hope" |
| 44 | WebSearch E | bivariate functional from truncated block Jacobi, degree 2n+1, commutator last block | nothing direct |

Not reached: Curto–Fialkow 1996 Memoir and the later C–F papers (no fulltext fetched); Schmüdgen's book *The Moment Problem* (2017), Chs. 17–19; Laurent's survey; Fialkow–Nie 2010; Möller 1976 and Mysovskikh (only through Xu and DST); Cools' surveys; Vollmer; Collowald–Hubert 2018 fulltext; Putinar's dilation paper on cubature (not located); Greenbaum 1989 fulltext (paywalled; eq. (7.10) not seen); Greenbaum–Strakoš 1992 fulltext; the DGIM 2006 and Cichoń–Stochel–Szafraniec 2005 fulltexts (metadata only). Several of these are listed under "must read" below.

## Mechanism-by-mechanism findings

### (a) Truncated Favard correspondence (PD-T?…-301)

**Claim checked.** Structured pairs (block tridiagonal with echelon off-diagonal blocks, commutator supported on block (n,n)) correspond one-to-one to normalized functionals on Π_{2n+1} with M_n ≻ 0. The inverse is the words formula. The computed entries are overdetermined by e_n = 1, 6, 17, 36, … relations.

| Closest prior statement | Locator / coverage | Relation |
|---|---|---|
| Xu's multivariate Favard: a three-term relation with the rank condition gives a square-positive functional; commuting conditions (2.5)–(2.7). Infinite sequences only. | Xu, Trans. AMS 342 (1994) 855–866, §2 item 2°, Thm 4.2 (measure version with boundedness); Xu, Fields lecture notes Thm 3.1 (Favard), Thm 3.2 (commuting conditions (3.9a–c)); xu-siam-1994 record p. 993. WebFetch summaries plus the existing fulltext record. | weaker (infinite, no truncation, no count) |
| Degani–Schiff–Tannor: N-node positive cubatures of odd degree 2q+1 correspond to symmetric commuting extensions of the coordinate-operator sections A_i on P_q that satisfy a compatibility condition; the condition makes the bottom-left (N−n)×dim P_{q−1} block zero, giving block-tridiagonal form. | Numer. Math. 101 (2005), Thms 9, 10, 11, §5.3 (arXiv math/0408076; WebFetch summary) | special case. It covers functionals that already have a positive cubature, and uses the same "sections on P_q ↔ moments to degree 2q+1" bookkeeping. It does not treat general quasi-definite functionals or the commutator-support characterisation. |
| Delgado–Geronimo–Iliev–Marcellán: relations among the bivariate recurrence coefficients give necessary and sufficient conditions for a positive functional to exist (lexicographic orderings). | SIAM J. Matrix Anal. Appl. 28(1) (2006) 118–147, doi 10.1137/05062946X; **abstract only** | possibly close; not read. **Must read** before (a) is cited. |
| Cichoń–Stochel–Szafraniec: three-term recurrence modulo an ideal (finitely supported/zero-set case) and orthogonality. | J. Approx. Theory 134 (2005) 11–64; **title and metadata only** | possibly close for the discrete-measure side; not read. **Must read.** |

**Verdict: partially known.** The infinite Favard theorem and the odd-degree cubature ↔ graded commuting extension dictionary are published. I found no truncated statement in the documented search that characterises functionals on Π_{2n+1} by the support of the commutator on block (n,n). I also found no count e_n of the overdetermination of partly computed H_y. Two must-read sources (DGIM 2006, CSS 2005) could change this verdict.

### (b) Reduction to the moment cone of K_δ and inradius criterion (PD-T?…-302)

| Closest prior statement | Locator / coverage | Relation |
|---|---|---|
| Richter–Tchakaloff: a functional in the moment cone has a finitely atomic representing measure. | Di Dio–Schmüdgen arXiv 1703.01497, Prop. 4; Bayer–Teichmann PAMS 134 (2006) (arXiv math/0502473, metadata only); Putinar PAMS 125 (1997) 2409–2414, doi 10.1090/S0002-9939-97-03862-8 (abstract only) | known component (moment-cone membership ⟺ positive cubature on K_δ) |
| Positive cubature ⟺ graded commuting extension. | DST 2005 Thms 9–11 | known component (the extension reading of 302(a)) |
| Boundary points: a moment vector is a boundary point iff a nonzero nonnegative function is annihilated. Supports lie in its zero set. | Di Dio–Schmüdgen Prop. 27(i), Cor. 41, Lemma 3 (the summary flagged a possible transcription issue in Cor. 41 (iii)–(vii)); 1D: Schmüdgen, Ten Lectures, Lecture 3, Thm 3.5 | known component (the duality behind r(δ)) |

**Verdict: partially known.** Each ingredient is classical: Tchakaloff/Richter, the DST dictionary, and conic duality. I found no source that states the backward question for the δ-fattened node set K_δ, or the criterion "all ε-perturbations representable ⟺ inradius r(δ) ≥ ε".

### (c) Rate theorem (PD-T?…-303): S_0 = 0 → δ = 0; S_1 = 0 → δ ≍ ε; S_1 ≠ 0 → δ ≳ √ε; (H) → δ ≍ √ε; PD-Hessian p* ∈ S_1 → obstruction

| Closest prior statement | Locator / coverage | Relation |
|---|---|---|
| Inner points of the moment cone (X = ℝⁿ, E ⊂ C¹): s is inner ⟺ d(s) = codim Im(s) = 0, where Im(s) is the union of the ranges of the derivative DS of the moment map. Im(s)^⊥ corresponds to functions vanishing with first partials on W(s). Full-rank DS gives an open neighbourhood map, hence an inner point. | Di Dio–Schmüdgen Thm 40, Lemma 37(ii), Prop. 43(iii)–(iv), proof step (vii)→(i) (WebFetch) | partially the same mechanism as 303(b). The space of functions vanishing to first order at the atoms plays the role of S_1, and the open-mapping argument is the linear-rate argument. This is a global statement on ℝⁿ and has no K_δ localisation, no rates and no second-order (Hessian) analysis. The summary reports "no second-order vanishing criterion" in the paper. |
| Faces of Pos_{n,2d}: a nonnegative form vanishing on S lies in I_{2,2d}(S) (double zeros). Hessians at zeros are PSD; a zero is "round" if the Hessian is PD on s^⊥. If p ≥ 0 has finite zero set and is round at each zero, and q vanishes doubly there, then p + εq ≥ 0 for small ε. The dimension of I_{2,2d}(S) follows from the Alexander–Hirschowitz count. | Blekherman, J. Amer. Math. Soc. 25 (2012) 617–635 (arXiv 0907.1339), §3.1, Lemma 3.1, Cor. 3.2, Thm 3.3 (WebFetch) | same local mechanism as 303(e). Round double zeros give local nonnegativity stable under double-vanishing perturbations. This is for global forms, about cone faces rather than backward representation, and has no rates. |
| Nonnegative-measure super-resolution: in 1D, T-systems with m ≥ 2k+1 give a unique nonnegative measure; noisy data give O(δ^{1/7}) in a generalised Wasserstein distance. | Eftekhari–Tanner–Thompson–Toader–Tyagi, ACHA (2021), arXiv 1804.01490, abstract and §1 (theorem bodies not returned) | different (1D, recovery/stability rather than exact local representability; certificate-based) |

**Verdict: partially known.** The ingredients are published: zero-gradient spaces at atoms and the open-mapping/interior link (Di Dio–Schmüdgen), and round double zeros with local nonnegativity (Blekherman). I found no source that states the quantitative trichotomy r(δ) ≍ 1, δ, δ² or 0 for the δ-fattened node set, the Hessian-cone condition (H), or its dual PD-certificate form 303(f). Not checked: Schmüdgen 2017 Chs. 17–19; Curto–Fialkow; Fialkow–Nie; the Poon–Peyré multidimensional super-resolution analysis (arXiv 1709.03157, surfaced but not read).

### (d) Square unisolvent case (PD-N?…-302, 304, PD-N?…-301)

| Closest prior statement | Locator / coverage | Relation |
|---|---|---|
| Gaussian (dim Π_{n−1}-node, degree 2n−1) cubature exists ⟺ P_n has dim Π_{n−1} common zeros ⟺ the truncated block Jacobi matrices commute. | Mysovskikh (as cited); Xu Trans. AMS 1994 Thm 3.2, Thm 3.4; Xu Fields notes Thms 5.1–5.3; xu-siam-1994 Thm 4.1; Lasserre arXiv 1105.4448 (equivalent overdetermined linear system; existence "imposes severe restrictions") | known: the exact N = N_n representation exists only if κ = 0 (the 304(b) direction "κ = 0 ⟺ N_n-node odd-degree positive cubature") |
| Möller-type bound N ≥ dim P_q + ½ max rank[A_i, A_j] for degree 2q+1 positive cubature; Möller: the rank is ⌊n/2⌋ for centrally symmetric functionals. | DST Thm 2, Thm 12 (origin Möller 1976); Xu Fields notes (5.4), Thm 5.4 | known count side: a perturbation with κ ≠ 0 needs more than N_n nodes. It says nothing about where the extra nodes can lie. |

**Verdict.** Partially known for the counting part. For the impossibility of δ = O(ε), the necessity of δ ≳ c√ε (and the bound δ ≥ c√‖κ‖), and the Padua n = 3 certificate p* ∈ Π_7: **no matching result found in the documented search.** The R03 checkerboard measurements were not assessed. They are numerical work and not prior-art material.

### (e) Dilation / POVM (minimal matrix convex set) model (PD-T?…-308)

| Closest prior statement | Locator / coverage | Relation |
|---|---|---|
| X ∈ W_n^min(K) ⟺ X is a compression of a normal tuple N with σ(N) ⊆ K ⟺ X = Σ x^{(j)} ⊗ P_j, P_j ⪰ 0, Σ P_j = I (Naimark). The matrix range of a normal tuple is W^min(σ(N)). | Passer–Shalit–Solel, arXiv 1706.05654 (J. Funct. Anal. 2018, venue from memory), (1.3)–(1.4), Prop. 2.3; Davidson–Dor-On–Shalit–Solel, arXiv 1601.07993 (IMRN 2017, from memory), Prop. 4.3, Cor. 4.4 (cited through PSS) | framework known. The degree-1 matrix moment cone in 308 is W^min_N(K_δ). |

**Verdict: partially known.** The model and the dilation/POVM equivalence are standard. I found no explicit statement that perturbed square data lie in W^min_N(K_δ) for every δ > 0. The statement looks like an elementary consequence of the framework (interiority at a commuting tuple with finite joint spectrum). I did not search for this specific statement beyond PSS/DDSS.

### (f) Greenbaum-type backward stability (1D) and multivariate extensions

| Source | Statement as read (WebFetch) | Coverage |
|---|---|---|
| Greenbaum, LAA 113 (1989) 7–63 | Metadata confirmed by Greenbaum's own talk abstract (Prague, undated). The abstract says the interval bound "was not as small as one might hope" and sets out to argue that the widths are of order ε‖A‖. | talk abstract only; fulltext not read |
| Šimonová–Tichý, arXiv 2507.16484 §1 | "the proof is given for intervals of size" √ε‖A‖; experiments indicate ε‖A‖. Block case: whether the conditions can always be satisfied "remains open". | html v1 |
| Chen, arXiv 2608.21268 §4, Thm 4.6 (preprint, Aug 2026) | Symmetric N×N matrices S and T̃ with N = nk. T̃ is tridiagonal with the computed T_k as its leading block. S = Ûᵀ(I_k ⊗ A)Û and ‖S − T̃‖ ≲_k ε‖A‖ (polynomial-in-k factor). It contrasts this with "Greenbaum's bound depends on the fourth-root of the accuracy parameter [Gre89, eq. (7.10)]". No block or multivariate content. | PDF via WebFetch |
| Meurant–Strakoš, Acta Numer. 15 (2006), §4.3, Thm 4.9 p. 511 | The eigenvalues of the extended B ((n+m_k)×(n+m_k)) lie within O((n+m_k)³ max{ε‖A‖, f_k, …, f_{n+m_k}}) of eigenvalues of A. The f_j are the smallest perturbations that make a coefficient η_{j+1} vanish; their size is not quantified in the returned text. Block Lanczos is excluded (p. 476). | PDF via WebFetch, text partly garbled |
| Greenbaum–Strakoš, SIAM J. Matrix Anal. Appl. 13(1) (1992) 121–137, doi 10.1137/0613011 | Reported through Šimonová–Tichý: with intervals comparable to ε‖A‖, finite-precision CG matches exact CG on the "blurred" matrix (experiments). | metadata plus a secondary report |

**Conflict to preserve.** The secondary sources disagree on the proven width in Greenbaum 1989: √ε‖A‖ (Šimonová–Tichý), ε^{1/4} (Chen, citing Gre89 eq. (7.10)), or a max{ε‖A‖, f_j} form with unquantified f_j (Meurant–Strakoš). Chen's preprint claims an ε‖A‖·poly(k) Greenbaum-type model. Until Gre89 is read, the L3 statement "1D Greenbaum width √ε (proven)" (R03 §3, lit_reading.md) is **not supported**. The R03 parallel "the √ε rate of 303(d) matches the 1D Greenbaum width" should be withdrawn or marked as conflicting.

**Multivariate / commuting extension.** No matching result found in the documented search (queries #1, #37, #44). The block single-matrix case is stated open by Šimonová–Tichý. One observation for reading (G), not a literature claim: Chen's construction uses the dilation I_k ⊗ A. Its bivariate analogue (I_k ⊗ X, I_k ⊗ Y) commutes exactly, but the near-by structured pair T̃_x, T̃_y need not. That is where 303(e)/N301 bite.

**Verdict for (f): partially known.** The 1D model is known, but its proven width is in conflict across sources. No multivariate or commuting version was found.

## Summary table

| Mechanism | Closest prior | Relation | Verdict |
|---|---|---|---|
| (a) truncated Favard + e_n count | Xu 1994 Trans. AMS §2/Thm 4.2; DST 2005 Thms 9–11, §5.3; DGIM 2006 (unread) | weaker / special case | partially known |
| (b) moment cone of K_δ, r(δ) ≥ ε | Tchakaloff–Richter; DST Thms 9–11; Di Dio–Schmüdgen Prop. 27 | components known | partially known |
| (c) rate trichotomy, (H), obstruction | Di Dio–Schmüdgen Thm 40/Lemma 37/Prop. 43; Blekherman 2012 Lemma 3.1 | same local ingredients, different question | partially known; the quantitative trichotomy and (H): no matching result found |
| (d) square case √ε, Padua n = 3 | Mysovskikh/Xu commuting criterion; DST Thm 12 / Möller | count side known | partially known (count); √ε necessity and Padua certificate: no matching result found |
| (e) POVM/dilation, no obstruction | Passer–Shalit–Solel (1.3)–(1.4); DDSS Prop. 4.3 | framework known | partially known |
| (f) Greenbaum width; multivariate | Šimonová–Tichý §1; Chen 2026 Thm 4.6; Meurant–Strakoš Thm 4.9 | width in conflict | partially known; multivariate: no matching result found |

## Recommended literature records (orchestrator)

New records:
- `degani-schiff-tannor-2005` (update the existing record): Thms 2, 9–13, §5.3, as read here. Numer. Math. 101 (2005) 479–500; arXiv math/0408076.
- `di-dio-schmudgen-2018`: P. J. di Dio, K. Schmüdgen, "The multidimensional truncated moment problem: atoms, determinacy, and core variety", arXiv 1703.01497 (published venue J. Funct. Anal. 2018 from memory, UNVERIFIED). Prop. 4, 27, 28; Thm 40; Cor. 41; Lemma 37; Prop. 43. Coverage: WebFetch of the PDF.
- `blekherman-2012`: G. Blekherman, "Nonnegative polynomials and sums of squares", J. Amer. Math. Soc. 25 (2012) 617–635, arXiv 0907.1339. §3.1, Lemma 3.1, Cor. 3.2, Thm 3.3. Coverage: ar5iv via WebFetch.
- `xu-tams-1994`: Y. Xu, "Block Jacobi matrices and zeros of multivariate orthogonal polynomials", Trans. AMS 342 (1994) 855–866. §2, Thms 3.2, 3.4, 4.2. Coverage: AMS PDF via WebFetch.
- `xu-lecture-notes`: Y. Xu, lecture notes on orthogonal polynomials of several variables (Fields), darkwing.uoregon.edu/~yuan/paper/fields.pdf. Thms 3.1, 3.2, 5.1–5.4, 6.1; page numbers inferred.
- `lasserre-gaussian-cubature`: J. B. Lasserre, "Existence of Gaussian cubature formulas", arXiv 1105.4448 (venue not confirmed).
- `passer-shalit-solel-2018`: arXiv 1706.05654; and `davidson-doron-shalit-solel-2017`: arXiv 1601.07993 (venues from memory).
- `putinar-1997`: PAMS 125 (1997) 2409–2414, doi 10.1090/S0002-9939-97-03862-8 (abstract). `bayer-teichmann-2006`: PAMS 134 (2006), arXiv math/0502473 (metadata).
- `greenbaum-strakos-1992`: SIAM J. Matrix Anal. Appl. 13(1) (1992) 121–137, doi 10.1137/0613011 (metadata plus a secondary report).
- `meurant-strakos-2006`: Acta Numerica 15 (2006); karlin.mff.cuni.cz/~strakos/download/2006_MeSt.pdf. §4.3, Thm 4.9 p. 511.
- `eftekhari-et-al-2021`: arXiv 1804.01490 (ACHA), context only.
- Must read, not yet read: `delgado-geronimo-iliev-marcellan-2006` (SIAM J. Matrix Anal. Appl. 28(1) 118–147, doi 10.1137/05062946X) and `cichon-stochel-szafraniec-2005` (J. Approx. Theory 134 (2005) 11–64).

Updates to existing records:
- `greenbaum-1989`: metadata LAA 113 (1989) 7–63 confirmed by Greenbaum's talk abstract. Record the width conflict (√ε / ε^{1/4} / max-form) and the pointer to eq. (7.10).
- `chen-2026`: Thm 4.6 (N = nk, ‖S − T̃‖ ≲_k ε‖A‖) and the fourth-root remark.
- `simonova-tichy-2025`: the §1 √ε‖A‖ sentence and the block-case-open statement.

## Limits

All readings are WebFetch summaries, and theorem numbers were not checked against page images. The Greenbaum 1989, Schmüdgen 2017 and Curto–Fialkow fulltexts were not reached. The odd-degree truncated moment literature (Curto–Fialkow, Fialkow–Nie, Vasilescu) and the cubature-perturbation literature were covered only by the queries listed. A negative result here is evidence of a gap in this search, not of novelty.
