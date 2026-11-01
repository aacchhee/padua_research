# M0 literature baseline — CC/Padua MZ constants

Rules read at `d36722823441dc40c6e19d69a174459348dd309c`; 2026-10-31. Literature developer: Codex, gpt-6.1-sol, high (explicit orchestrator assignment). This file records source evidence, not an accepted mathematical result. `literature/INDEX.md` and the complete `state/IDEAS.md` were read; both have no registered statements/candidates. No shared registry or Git mutation was made by this worker.

## Baseline and scope

The supplied F7/P1 notes identify An–Sommariva–Vianello (ASV), arXiv:2601.04708, as the direct numerical predecessor. Primary HTML v1 was inspected at the introduction and §3.1; the authors distinguish degree-dependent weak constants from strong uniform constants and explicitly describe their investigation as numerical. This supports neither an exhaustive openness claim nor an inherited proof of M1–M3.

An–Wu, arXiv:2202.13691v3, primary HTML equation (2.5), theorem statement, §4 opening and Corollary 4.1 were inspected. The corollary explicitly retains the theorem's conditions with eta=3/4. A failure of that assumed bound limits its application; it does not refute a conditional theorem. Published fulltext comparison and comprehensive erratum clearance remain gaps.

The highest-priority potential prior-art threats are Sloan–Smith's 1978/1980 CC product-integration papers and Mastroianni–Milovanović's 2008 book. In particular, a norm theorem for Lobatto interpolation from weighted nodal l2 to Lebesgue L2 can translate into the endpoint minimum-eigenvalue problem. These sources have not yet been checked in full text: **FULLTEXT UNVERIFIED**. The supplied assertion that general MZ theory only covers small ratios is likewise **FULLTEXT UNVERIFIED** pending exact hypotheses.

| Target | Closest source family to screen | Cheapest literature kill test |
|---|---|---|
| M1: CC lambda_max < 2 on degree <= N-1 | CC product integration; sharp MZ constants at Chebyshev extrema | Find an explicit upper discrete/Lebesgue L2 norm ratio below 2 with the actual CC weights and the same degree range. A generic unspecified constant does not settle M1. |
| M2: endpoint lambda_min of order log^-2 N | Lobatto interpolation norm; weighted MZ endpoint theory; Toeplitz/Hankel extreme-eigenvalue theory | Find an l2(CC weights) -> L2(dx) interpolation norm of order log N, or an exactly equivalent mass-matrix theorem. Matching nodes alone is insufficient; weights, degree, endpoint constraints and both directions must match. |
| M3: each fixed theta<1, uniform MZ bounds | Lubinsky–Máté–Nevai; Mastroianni–Totik; Lubinsky survey | Check whether every fixed theta<1 is permitted, whether CC weights are comparable to the theorem's weights uniformly, and whether the upper constant is <2 if eta<1 is claimed. |

The C4 transfer note is an input report, not external published literature. The orchestrator reports a mismatch: its older account labels D1' OPEN, whereas a pinned private file `21_literature_and_open_questions.md` reports an external one-level R04 audit with D1' PROVED. No private full text is reproduced here; neither report supplies a local CC proof. The exact map and hypotheses must be established independently.

## Queries and access log

All queries below were actually issued through the web search connector on 2026-10-31; coverage is partial and no exhaustive novelty claim is made.

1. `"2601.04708"`
2. `"2202.13691" erratum`
3. `"Sloan" "Smith" "Clenshaw-Curtis" 1978 1980`
4. `"Passi" "Padua" cubature 2025 2026`
5. `"On the role of weak Marcinkiewicz" "252"`
6. `"On the quadrature exactness in hyperinterpolation" erratum correction`
7. `"Mastroianni" "Milovanović" "Interpolation Processes" "Lobatto"`

Initial direct opens of <https://arxiv.org/html/2601.04708v1> and <https://arxiv.org/html/2202.13691v3> succeeded; the first Passi PDF open timed out. A later retry through the primary author CV succeeded and the title page confirms a bachelor's thesis. ASV journal metadata was verified through that CV; journal body comparison and comprehensive erratum checking remain gaps.

Continuation queries, same date and connector (literal query strings, including unsuccessful searches):

8. `"Sloan" "Smith" "Product-integration with the Clenshaw-Curtis and related points" pdf`
9. `"Mastroianni" "Totik" 2000 "Marcinkiewicz"`
10. `"Lubinsky" "Máté" "Nevai" 1987 "Quadrature"`
11. `"Lubinsky" 1998 "Marcinkiewicz" survey pdf`
12. `"Lubinsky" "Marcinkiewicz-Zygmund inequalities: methods and results" pdf`
13. `"Widom" "Hankel matrices" 1966 pdf`
14. `"Widom" "Wilf" 1966 smallest eigenvalue pdf`
15. `"Interpolation Processes" "978-3-540-68349-0" chapter 4`
16. `"Don" "Gottlieb" 1994 "Chebyshev" Legendre quadrature`
17. `"Xiang" "Bornemann" Clenshaw Curtis 2012 arxiv`
18. `"Hale" "Townsend" Clenshaw Curtis 2014 quadrature`
19. `"On the role of Marcinkiewicz-Zygmund constants" "2027"`
20. `"Trefethen" "Is Gauss Quadrature Better" pdf`
21. `"Sloan" "Smith" "BF01398509" pdf`
22. `"Sloan" "Smith" "BF01403676" pdf`
23. `"Mastroianni" "Totik" "Weighted polynomial inequalities" pdf 2000`
24. `site:lubinsky.math.gatech.edu "Marcinkiewicz-Zygmund Inequalities: Methods and Results"`
25. `"Mastroianni" "Totik" "37-71" "pdf"`
26. `"Quadrature Sums Involving" "pdf" Lubinsky Mate Nevai`
27. `"Hale" "Townsend" "Chebyshev-Legendre" arxiv`
28. `"Clenshaw-Curtis" "Marcinkiewicz" "inequality"`
29. `"Chebyshev" "Lobatto" "Marcinkiewicz" "log"`
30. `"Lobatto" "interpolation" "L2" "log"`
31. `"Clenshaw-Curtis" "norm" "log" interpolation Sloan`
32. `"Weighted Polynomial Inequalities with Doubling" "10.1007"`
33. `"Marcinkiewicz-Zygmund" "Lubinsky" "Clenshaw"`
34. `"Sloan" "Smith" "product" "1978" "convergence" "L2"`
35. `"Widom" "Wilf" "Small eigenvalues" "rho"`
36. `"On the quadrature exactness in hyperinterpolation" "Correction"`
37. `"On the quadrature exactness in hyperinterpolation" "Erratum"`
38. `"On the role of weak" "10.1016" "733"`
39. `"Hankel matrices" "Widom" "1966" filetype:pdf`
40. `"Clenshaw-Curtis" "norm equivalence"`
41. `"Clenshaw-Curtis" "Z-matrix"`
42. `"Clenshaw-Curtis" "upper" "Marcinkiewicz"`
43. `"Chebyshev extrema" "quadrature" "2" "inequality"`

Queries are discovery evidence only. Results included secondary/aggregator and unrelated hits; mathematical statements in records use primary sources or carry FULLTEXT UNVERIFIED. Search result snippets are not substituted for theorem statements. No citation-network closure or exhaustive historical search was performed.

## Completed primary-access screen

| Source | Reading coverage actually achieved | Remaining named gap / record |
|---|---|---|
| ASV arXiv 2601.04708v1 | Introduction, §§3.1–3.2, bibliography; finite experiment ranges verified | Journal text/DOI; [record](../../literature/records/mz-an-sommariva-vianello-2026.md) |
| ASV MCS 252 (2027), 733–745 | Primary author CV metadata, not journal body | Final text changes FULLTEXT UNVERIFIED |
| An–Wu arXiv 2202.13691v3 | Assumption 2.1, eq.(2.5), main theorem statement, §4/Cor4.1 | Published body comparison; [record](../../literature/records/mz-an-wu-2022.md) |
| An–Wu errata | Exact-title searches; publisher page find for “Correction”; arXiv v3 latest listed | No matching correction found in this search; no universal absence claim |
| Sloan–Smith 1978 / 1980 | Publisher summaries and metadata | Direct content/pdf URLs redirect to subscription previews; exact norm estimates FULLTEXT UNVERIFIED; [record](../../literature/records/mz-sloan-smith-1978-1980.md) |
| Mastroianni–Milovanović 2008 | Publisher ToC and chapter 4 abstract | Chapter PDF inaccessible; all norm theorem claims FULLTEXT UNVERIFIED; [record](../../literature/records/mz-mastroianni-milovanovic-2008.md) |
| Lubinsky–Máté–Nevai 1987 | Publisher abstract/metadata | DOI/pdf redirects to access page; exact degree/weight/constant hypotheses FULLTEXT UNVERIFIED |
| Mastroianni–Totik 2000 | Publisher abstract/metadata | DOI/pdf redirects to preview; exact MZ theorem FULLTEXT UNVERIFIED |
| Lubinsky 1998 survey | Author bibliography and author-hosted PDF located | 35-page scan has no extracted text; screenshot responses yielded no inspectable page content; FULLTEXT UNVERIFIED; [classical screen](../../literature/records/mz-classical-mz-screen.md) |
| Widom 1966 / Widom–Wilf 1966 | Discovery and primary PDF attempts | AMS PDFs 403; Wilf author page 403; mathematical contents FULLTEXT UNVERIFIED; [record](../../literature/records/mz-widom-1966-screen.md) |
| Trefethen 2008 | Abstract, Theorem4.1, selected §5/Theorems5.1–5.2, eqs5.2–5.4 | Remaining body not fully screened; exact aliasing predecessor verified |
| Don–Gottlieb 1994 | Primary metadata/abstract; scan cover | Body not extracted; norm lemmas FULLTEXT UNVERIFIED; [record](../../literature/records/mz-don-gottlieb-1994.md) |
| Xiang–Bornemann 2012 | Primary arXiv abstract, introduction theorem, §3 selected formulas | No complete proof audit; some HTML references malformed |
| Hale–Townsend 2014 transform | Primary author PDF abstract/introduction, selected §3 | No complete stability audit; Gauss-node algorithm separately only abstract screened; [aliasing/transform record](../../literature/records/mz-quadrature-aliasing-screen.md) |
| Passi thesis 2025/26 | Subsequent connector retry via author CV succeeded; title/introduction/ToC/ch4 selected text | Not complete 71 pages/code; title page confirms bachelor's thesis |
| An–Sommariva–Xue | Primary author CV “in preparation” entry | Manuscript/results FULLTEXT UNVERIFIED; [Passi/CV record](../../literature/records/mz-passi-cv-2026.md) |

The failed shell PDF fetch was diagnosed with the cloud-environment-runtime skill: current environment policy is restricted/enforced, academic hosts are absent from its allowed destinations, and the proxy returned 403. No bypass or configuration change was attempted. Connector access was used for accessible primary text. No third-party PDF/fulltext extract was written into the repository.

## Candidate-specific literature dispositions

| Target / mechanism | Closest verified predecessor and proposed separation | Disposition after this screen |
|---|---|---|
| M1: strict upper CC ratio below 2 on degree <=N-1 | Trefethen2008 Thm5.2 gives the exact folded moments. The campaign proposes quadratic Gram assembly and a Z-matrix absolute-value comparison; this step was not found in inspected portions. | Continue mathematical development with explicit citation. **Novelty unresolved** because SS/book/classical MZ fulltexts remain uninspected. Searches 40–43 found no matching sharp theorem in documented results. A source proving the same upper inequality kills the novelty distinction even if its proof differs. |
| M2: endpoint two-sided log^-2 order | Weighted Lobatto interpolation is the closest functional formulation; Widom/Hankel is only a structural pointer until the exact pencil is matched. | **High prior-art risk, not cleared.** Book/mean-convergence literature needs fulltext. Any equivalent two-sided weighted l2-to-L2 interpolation norm of order log N kills order-law novelty. A one-sided result only overlaps the matching half. A claimed leading constant needs its own comparison. |
| M2 lower-bound route: CC cardinal-function weighted Schur test | Supplied private C4 template is a reported analogy with stale status mismatch. | **Conditional transfer idea only.** Public direct CC entry estimates can stand on their own after proof/audit; private C4 labels supply neither hypotheses nor acceptance. |
| M3: each fixed ratio theta<1 | Classical weighted MZ inequalities have the closest general hypotheses, but only abstracts were inspected. | **Novelty unresolved; do not claim new fixed-ratio existence.** Exact historical theorem/weight translation is mandatory. Separate mere positive A(theta), finite B(theta) from B(theta)<2 or an explicit eta(theta)<1. |
| Padua extrapolation | ASV finite square experiments are verified; continuous measure is Lebesgue and space is total degree. | No all-degree source proof extracted. One-dimensional CC bounds do not by citation establish a Padua inequality with signed interpolatory weights. |

## Factual correction scope

1. An–Wu Cor4.1 is conditional in inspected arXiv v3. A failed eta=3/4 hypothesis supports correcting an applicability assertion/description, not refuting that implication. Its 1/sqrt(1-eta) factor is a bound, not automatically the actual operator norm.
2. Passi is a bachelor's thesis, confirmed on the primary title page; replace supplied MSc attribution.
3. The 2008 book's chapter 4 is uniform-norm interpolation; its existence does not verify the supplied l2-to-L2 norm suggestion.
4. Trefethen's `exactness.pdf` is the 2022 paper; the 2008 paper has a different title/DOI and contains the exact aliasing theorem.
5. ASV arXiv m is ADE; An–Wu m counts points; campaign N indexes N+1 CC points. Specify at-least exactness through N and any parity enhancement rather than copying an inaccurate blanket maximal-ADE convention.
6. “In preparation” on a CV verifies a listing, not manuscript contents or solved overlap. The C4 D1' mismatch is a provenance issue, not a local negative result or proof dependency.

## Final M0 handoff

M0 source discovery and bounded primary-access screen are recorded for every requested source family, with 19 provisional statements/pointers and exact reading coverage. The screen found no matching M1 sharp upper theorem or M2 exact endpoint law in the inspected primary portions; it cannot exclude the explicitly uninspected fulltexts. No campaign theorem, novelty claim or accepted mathematical status is assigned by these literature files. The orchestrator owns proof/audit acceptance, final IDs, shared registries and Git.

## 2026-10-31 audit-response screen — audit-01 M2

Rules read at `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`. Codex literature developer, `gpt-6.1-sol`, high (explicit orchestrator assignment). `literature/INDEX.md` and the complete `state/IDEAS.md` were read. This follow-up adds a named prior-art family to the original 43-query screen; it does not generate a new mechanism or claim novelty. The numbered list above and original handoff remain historical records of that earlier scope.

The following 20 literal targeted queries were actually issued through `search_service_web_run` / `system2_search_query` on this date, including unsuccessful searches:

1. `Nevai "Mean convergence of Lagrange interpolation. III" 1984`
2. `Askey 1972 "Lagrange" "mean convergence"`
3. `Lubinsky "paper147" "converse"`
4. `Erdos Feldheim 1936 interpolation Lagrange`
5. `"Mean convergence of Lagrange interpolation" "III" Nevai AMS 282 669 698`
6. `site:lubinsky.math.gatech.edu "Converse" "Lobatto"`
7. `"Mastroianni" "Russo" "mean convergence"`
8. `"Xu" "Lobatto" "mean convergence"`
9. `"Nevai" "0732113" "necessary"`
10. `"Sur le mode de convergence pour l’interpolation de Lagrange" pdf`
11. `"Weighted Marcinkiewicz inequalities and boundedness of the Lagrange operator"`
12. `"Mean convergence of Lagrange interpolation. III" pdf Nevai`
13. `"On Converse Marcinkiewicz-Zygmund Inequalities" "Lobatto"`
14. `"Lubinsky" "converse" "Lobatto" quadrature`
15. `"On Converse Marcinkiewicz-Zygmund Inequalities in" Lubinsky 1999 DOI`
16. `Nevai "Mean Convergence" "III" "pdf" generalized Jacobi 1984`
17. `"Lubinsky" "Lobatto" "inequalities"`
18. `"Erdös-Turán mean convergence theorem for Lagrange interpolation at Lobatto points" Xu 1987 DOI`
19. `"Mean convergence of generalized Jacobi series and interpolating polynomials" "10.1006"`
20. `"Mean convergence of Lagrange interpolation. III" site:ams.org abstract`

Query 18's tentative author/year were search terms, not an attribution: the primary source identifies **W. E. Smith, 1986**. Third-party summaries were used only for discovery; no mathematical assertion is promoted from them to a primary theorem.

| Primary source/access | Actual outcome | Durable disposition |
|---|---|---|
| Erdős–Feldheim original Rényi scan | Selected title/text and visual inspection of p. 914 | Statement found; exact preceding-note conventions pending |
| Askey 1972 DOI/bibliography and 1969 CWI report | Corrected journal-version metadata; selected earlier-report text; journal body open failed | Journal comparison and target critical case pending |
| Nevai III AMS article/PDF, CiteSeer mirror | Article body inaccessible (403/errors); author bibliography and primary reference metadata reached | Exact theorem/parameter/added-endpoint conditions **FULLTEXT UNVERIFIED**; include 1990 addendum |
| Lubinsky paper 147 author PDF and publisher abstract | Selected results pp. 1–7; Theorem 1.2 visually inspected; no full proof audit | Converse theorem form found; CC specialization and log rate pending |
| Mastroianni–Russo and Xu author bibliographies | Named follow-up citations reached; Xu DOI body opens failed | Bibliographic pointers only; no theorem extracted |
| Smith 1986 Cambridge PDF | Abstract/introduction/Theorem 1/Corollary 1 selected text; p. 379 screenshot retry timed out | Explicit Lobatto comparison found; target norm translation pending |

Exact titles, DOIs/URLs, node/weight/norm mismatches and reading limits are in [the new mean-convergence source record](../../literature/records/mz-mean-convergence-screen.md); [literature-response-01.md](literature-response-01.md) supplies the audit disposition and manuscript integration wording. Five provisional LIT-061–065 groups await orchestrator allocation; follow-up bibliography makes no additional theorem claim.

**Named unresolved threat added to M0:** weighted mean convergence at Jacobi/Chebyshev nodes and converse quadrature-sum inequalities may subsume PD-T017 and the endpoint order behind PD-T018. Nevai III/addendum, corrected Askey, Lubinsky's full-interpolation-space hypotheses, and Mastroianni–Russo/Xu require further reading. The screen found relevant primary statements but no verified matching CC-weighted `l²→L²(dx)` quantitative borderline theorem in the inspected portions. No exclusion, exhaustive novelty search, or mathematical status change follows. Keep the description at **self-contained proof; novelty unresolved**. No third-party PDF/fulltext extract was copied into the public tree.

Allocation update: the root MZ owner reserved LIT-061–065 in the shared ledger after merging charter-bearing main. The worker's no-allocation statement above describes its development phase; final mapping and ledger-propagation receipt are part of response-01.

## 2026-11-01 fulltext closure — topic mz-prior-art-20261101

Claude, Opus 5.5 (orchestrator), rules `9739a0c`. The verdicts, translations and coverage are in [comparison.md](../mz-prior-art-20261101/comparison.md), [translation.md](../mz-prior-art-20261101/translation.md) and the dated record sections. Access route: AC's NTNU institutional access in AC's built-in browser for Springer/Cambridge; free AMS PDFs, arXiv, NTRS and MDPI through the fetch tool. No fulltext enters Git. Three Sonnet 5.5 high workers verified citations, legal access and forward citations; their literal query lists are summarized in the topic LOG.

Updated dispositions (superseding the "Completed primary-access screen" gaps where stated):

| Target / mechanism | Disposition after fulltext reading |
|---|---|
| M1 (PD-T014/PD-T022): upper ratio <2 | No matching result found in the documented search. Sloan–Smith 1978/80 read: no quadratic form. Mastroianni–Totik gives only an unspecified converse constant. |
| M2 (PD-T017/PD-T018): endpoint log order | Qualitative failure of a uniform converse MZ inequality at this borderline is classical: Mastroianni–Russo 1999 Thm 2.7 (LIT-293) at the U_{N−1} zeros, König–Nielsen (LIT-294); the U-polynomial √log mechanism (PD-T019) is classical. Lubinsky 1999 excludes the borderline exponent. Nevai III, Askey, Smith and Erdős–Feldheim are uniform-input. **No two-sided order with CC weights found.** Pending: Xu I/II, Nevai 1990, LMN 1987, Mastroianni–Russo 2000. |
| M3 (PD-T023/PD-T024): fixed ratio | **Mastroianni–Totik 2000 IMPLIES PART** (positive lower bound for n≤θ₀N, unspecified θ₀ and constant; translation.md T4). Explicit constants for every θ<1 not found. LMN 1987 pending. |
| PD-T025 | Unchanged: generic mechanism known from ASV eq. (7). |
| PD-N004 / An–Wu | Published Corollary 4.1 matches arXiv v3; no correction found (not proof of absence). |
| ASV / An–Sommariva–Xue | Published ASV: DOI 10.1016/j.matcom.2026.10.001, not open access, body unread. An–Sommariva–Xue not public. |

Later on 2026-11-01, AC supplied Xu I/II, Nevai 1990, Lubinsky–Máté–Nevai 1987, Sloan–Smith 1982, Smith–Sloan 1980 and published ASV. None changes the dispositions above.
- Lubinsky–Máté–Nevai Theorem 5 gives forward boundedness λ_+≤C at CC (unspecified C, not <2).
- Xu II has the Mastroianni–Russo borderline (sufficient conditions, Gauss nodes).
- Nevai 1990 justifies a step of Nevai III.
- Published ASV calls the CC behaviour theoretically "not known".
New LIT-296–298. Still unread: Mastroianni–Russo 2000 (Hadronic), Della Vecchia–Mastroianni–Vértesi 1995, Wu AML 2026.

Response-01 to audit-01 (2026-11-01):
- Mastroianni–Totik's CC consequence lies inside half-exactness, so it is **RELATED**, not IMPLIES PART.
- Sloan–Smith 1980 was screened in full: no theorem statements.
- The König–Nielsen critical exponent now uses max(α,β).
- The classical attribution of borderline failure was rescoped. Mastroianni–Milovanović–Notarangelo 2012 (LIT-299) gives inf_N λ_−(N,N)=0 at the CC nodes on Π_N (qualitative). Mastroianni–Russo, Xu and König–Nielsen are analogous settings only.
See topics/mz-prior-art-20261101/response-01.md.
