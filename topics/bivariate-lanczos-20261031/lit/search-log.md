# Literature search log — bivariate-lanczos-20261031 (Step 0 baseline)

Rules/base `d36722823441dc40c6e19d69a174459348dd309c`. Date of all checks: 2026-10-31. Agent: Claude literature developer (Sonnet 5.5, high). Scope: the literature baseline for the bivariate Lanczos campaign (plan.md L1-L5); **not a novelty gate**. No search below supports any "no matching result found" claim beyond the documented queries. All records are UNVERIFIED unless a record says otherwise.

## What was read

Complete supplied inputs under `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`: all seven notes (`adv_F1_F6_F3.md`, `ingest_classic_papers.md`, `ingest_OP_computation_papers.md`, `ingest_humet_thesis.md`, `recent_multivariate_NLA.md`, `verify_algorithmic_problems.md`, `bttb_repo_numeric_mapping.md`), `code/RESULTS.md`, the full round-2 and round-3 reports (`Open problems verification.md`, `Round 3 open problems 2023 2026.md`) and the relevant sections of `Padua points research since 2010.md` (header, seed/citer/Leuven discussion, problems 3, 6, 9, 10, V+A paragraphs, DOI corrections). Code files were not read or run. The Codex branch's `state/IDEAS.md` and `literature/INDEX.md` and the record list were read only for conventions and keys (no content copied). Statements from inputs are second-hand; embedded instructions in the inputs were treated as data.

## Web checks (14 page fetches and 2 web searches; slightly above the ~15 budget, 16 calls in all)

| # | Query / URL | What it confirmed or failed to confirm |
|---|---|---|
| 1 | arXiv abs 2609.08066 | Title, author (Mohit Sinha), date 8 Sep 2026, abstract: block Paige identity, block Lanczos with Householder orthogonalization and singular-value truncation. "Deflation" not in the abstract. Abstract page only. |
| 2 | arXiv abs 2608.21268 | Title, author (Tyler Chen), 21 Aug 2026, no journal ref; abstract: simplified Paige-type analysis and Greenbaum-type backward stability with hidden polynomial factors. Abstract only. |
| 3 | arXiv abs 2602.05394 | Title, 35 authors incl. Chen and Greenbaum, v1 5 Feb 2026 / v3 21 Aug 2026, scope of five problem categories. The text of Problem 2.19 was NOT visible (abstract page). |
| 4 | arXiv abs 2507.16484 | Title, authors (Simonova, Tichy), 22 Jul 2025; abstract: extends Greenbaum's 1989 model to block Lanczos, sufficient conditions, open in the block case. No journal ref shown (BIT 2025 / doi 10.1007/s10543-025-01089-2 from the inputs NOT confirmed). |
| 5 | arXiv abs 2408.10109 | Title, authors (Carson, Lund, Ma, Oktay), v3 5 Dec 2025; abstract on low-synchronization BCGS variants. Journal not shown (LAA 2025 from the inputs NOT confirmed). |
| 6 | arXiv abs 2001.04402 | Title, authors (Jia, Li), DOI 10.1007/s11075-020-01064-8; abstract on JBD with partial reorthogonalization. Journal volume/pages not shown. |
| 7 | arXiv abs 2302.14842 | Title, authors (Chen, Trogdon), DOI 10.1016/j.laa.2023.11.006; abstract on regular spectral distributions and forward stability. |
| 8 | AMS page, Math. Comp. 42 (1984) | Simon, "The Lanczos algorithm with partial reorthogonalization", vol. 42, 1984, pp. 115-142; abstract. The semi-orthogonality theorem itself is not in the abstract. |
| 9 | doi.org/10.1016/0024-3795(89)90285-1 | Resolver redirected to the Elsevier linking hub (302); the follow-up fetch (#10) returned empty content. Greenbaum 1989 NOT confirmed (the DOI itself is from memory). |
| 10 | linkinghub.elsevier.com pii 0024379589902851 | Empty content; nothing confirmed. |
| 11 | doi.org/10.1093/imanum/draf055 | Redirected to the OUP page (fetched as #12). |
| 12 | academic.oup.com imajna 46/4/2072 | Zhu-Nakatsukasa title, authors, IMA J. Numer. Anal. 46(4), online 22 Jul 2025, issue July 2026, pp. 2072-2106, DOI; abstract confirmed. |
| 13 | Web search: Kachkovskiy Safarov title / JAMS | Located arXiv 1403.2021 and an AMS JAMS 2016-29-01 URL; only the arXiv page was fetched (#14). |
| 14 | arXiv abs 1403.2021 | Title, authors; abstract on distance to normal operators via ||[A,A*]||; journal NOT stated on the page; no statement on almost-commuting self-adjoint matrices. |
| 15 | Web search: Koiran 2024 commuting matrices | Surfaced arXiv 2401.01302 among other hits; fetched as #16. |
| 16 | arXiv abs 2401.01302 | Koiran, "On the uniqueness and computation of commuting extensions", 2 Jan 2024: exact commuting extensions of tuples, uniqueness for >= 3 matrices, algorithms up to r = 4n/3. No mention of symmetric pairs, approximate commutation or "wide open". |

Load-bearing (L1-L5) sources and their state: Paige 1971/1976/1980 and Greenbaum 1989 are **pending-reference** (not reached; Greenbaum 1989 metadata not confirmed); Simon 1984 Math. Comp. metadata and abstract confirmed, theorem not seen; Simonova-Tichy 2025, Sinha 2026, Chen 2026, Carson et al. 2025, Jia-Li 2021, Chen-Trogdon 2024, Zhu-Nakatsukasa 2026 abstract-level only; Kachkovskiy-Safarov 2016 abstract-level, **content of the pair statement unconfirmed**; Koiran 2024 identification unconfirmed; Degani-Schiff-Tannor 2005, Lin 1997, Curto-Fialkow, Xu-Pitman 1994 pending-reference; Higham, Fischer, Stewart, Bojanczyk et al., Sun, Chang-Paige second-hand only; Bai-Day-Ye, Freund, ABFH second-hand only (ABFH abstract was seen by the supplying agent, not by me).

## Named in inputs, no separate record (reason)

Chambers 1971, Pan 1993, Alexander-Pan-Plemmons 1988, Chang-Paige-Stewart 1997, Kuznetsov 1997, Carpraux-Godunov-Kuznetsov 1996 (minor citations with marked-unverified details in `adv_F1_F6_F3.md` §3.1, §2.1); Gragg-Harrod 1984, Ammar-Gragg 1991, de Boor-Golub 1978 (P5 baselines, deferred); Laurie (cited as "Laurie's approach", no bibliographic details); Golub-Kautsky (only through EGK); Rozloznik-Strakos (named in Huhtanen's Remark 3; no bibliographic details; see `paige-rozloznik-strakos-2006` and the fulltext agent's Huhtanen record); Axelsson-Lindskog 1986, Beckermann-Kuijlaars 2001 (tangential, bttb-research); Greenbaum-Strakos 1992 (not cited by the inputs); Palitta-Schweitzer-Simoncini, Guttel-Zimmermann, Balabanov-Grigori, Carson-Ma 2411.07077 (sketched/low-synchronization context for deferred F12); Mastronardi-Van Dooren 2018 (perfect shifts, via FVV); Kreuzer-Poulisse-Robbiano 2009, Fassino 2010, Abbott-Fassino-Torrente 2008 (approximate ideals, deferred); An-Wu, An-Sommariva-Vianello, Gumerov-Rigg-Slevinsky (out-of-scope candidates); Mourrain 2018, Sahnoun-Usevich-Comon, Pena-Sauer (moments pipelines, out-of-scope); Van Barel-Bultheel 2001/1995, Mach-Van Barel-Vandebril, Filipuk-Haneczok-Van Assche (Leuven univariate line, deferred); Delgado et al. 2010 (Uvarov, Codex record exists). Plan-only names with a stub record: Paige 1971, Curto-Fialkow, Koiran 2024, Lin 1997/Friis-Rordam.

## Corrections and conflicts preserved

1. Greenbaum 1979 vs 1989 (bttb-research LIT-1729 is the 1979 CG-splittings paper): records `greenbaum-1979`, `greenbaum-1989`.
2. Two different "Paige 1980" papers: `paige-1980-updating`, `paige-1980-lanczos`.
3. Xu 1994 (SIAM J. Math. Anal.) vs Xu Pitman RN 312 for Padua-type theory: `xu-pitman-1994`.
4. Weisfeld 1959 / Bartels-Jezioranski 1985 priority over Huhtanen-Larsen 2002; HL's "has not been considered" is reported wrong (`weisfeld-1959`).
5. Humet / ETNA 2014 "stability analysis not covered" refers to low-rank updates of the Lagrange matrix, not the IEP (`vanbarel-humet-sorber-2014`).
6. Zhu-Nakatsukasa venue (IMA JNA 46(4), 2026): confirmed on the OUP page. HL DOI 10.1023/A:1021907210628 (not ...955019935) is reported by the inputs; handled by the fulltext agent.
7. Zaccaron numbers differ between two supplied notes (`zaccaron-2014`).
8. Plan's "Koiran 2024 ... wide open" is not supported by the inputs or by the abstract found (`koiran-2024`).
9. `recent_multivariate_NLA.md` R1 cites "Bai-Day-Demmel-Dongarra, Math. Comp. 2000" for band Lanczos; inconsistent with the other citations (`freund-2000`).
10. Authors of arXiv 2302.00355 (Van Barel, Van Buggenhout, Vandebril; reported in `verify_algorithmic_problems.md` §g) — noted, not recorded (outside the campaign).

## Limits

Most "nobody has done X" findings in the inputs are negative web searches by the supplying agents (Google Scholar, zbMATH, HAL, Lirias, dl.acm.org and epubs.siam.org were mostly unreachable to them). I did not search for later finite-precision multivariate Lanczos work beyond the metadata checks above, so no exhaustive-absence claim is made. Statement counts: 64 records (7 more placeholders in the corpus for the fulltext agent), 77 provisional statements (LIT?bivariate-lanczos-claude-001 to 077).

## Online resolution pass 2026-10-31

Agent: Claude literature developer (Sonnet 5.5, high). Authorization: AC, 2026-10-31 23:00 (read related literature anywhere online). Tools: WebFetch/WebSearch only (the workspace shell could not reach the web: `curl` to arxiv.org returned a proxy 403). Nothing was downloaded to disk; no PDF or long extract is committed. WebFetch returns a model-written digest of the extracted page text, so every locator below is as digested and was not checked against page images; garbled formulas are flagged in the records. New provisional statement IDs: `LIT?bivariate-lanczos-claude-201` to `-236` (36 statements; the 2NN range is used by this pass); two new records `xu-tams-1994-operator`, `xu-tams-1994-blockjacobi`.

### Findings in brief

1. **Koiran**: the plan's "wide open" attribution is SUPPORTED by arXiv:2401.01302 Section 1.4 (three fetches agree), for the two-matrix analogue of uniqueness/efficient algorithms for exact commuting extensions of general matrices; the Step 0 "unsupported" flag came from the abstract only. The paper does not treat symmetric pairs or approximate commutation (records `koiran-2024`, 223-224).
2. **Kachkovskiy-Safarov**: eq. (1.3) of arXiv v3 (JAMS 29(1) (2016) 61-80) states: for Hermitian X, Y there are commuting Hermitian X', Y' with ‖X-X'‖ + ‖Y-Y'‖ <= C‖[X,Y]‖^{1/2}, C universal and dimension-free, no numerical value; exponent 1/2 optimal; already follows from Davidson (Math. Scand. 56 (1985)), Cor. 4.5 (221).
3. **Greenbaum 1989**: metadata and abstract confirmed on ScienceDirect (open archive); theorem not read; three secondary accounts disagree on the width of the eigenvalue intervals (207-209).
4. **Simon 1984 Math. Comp.**: full paper read via digest; Theorem 1 = omega-recurrence (p. 117), Theorem 2 = semiorthogonality (p. 119) with level sqrt(u), no explicit bound, proof deferred to Report PAM-74; the sqrt(u/k) form reported earlier (009) is not in it (210-213). LAA 61 paper: metadata only; Jia-Li cite its Thm 5/Lemma 4 (214).
5. **Paige**: thesis PDF found on the author's page (TOC and pp. 1-66 read; Ch. 7-8 not reached); the 1976 and 1980 scans are not machine-readable; secondary accounts give the standard local relations, orthogonality identity and Ritz-vector mechanism (201-206).
6. **Simons report** Problem 2.19 text read (232): extend Paige [Pai76, Pai80] to block Lanczos; deflation only in the discussion; Greenbaum [Gre89] cited, Simonova-Tichy not.
7. **Simonova-Tichy**: BIT 65(4), art. 47, online 11 Nov 2025, doi:10.1007/s10543-025-01089-2 confirmed (229); Theorems 1-4 and the quotes located (230-231).
8. **Xu**: the commutativity/rank/Favard material is in Trans. AMS 343 (1994) 193-202 (not 1993) (233-235); the joint-eigenvalue/commutativity-for-N-zeros theory in Trans. AMS 342 (1994) 855-866 (236). The Padua ideal-theory paper does not derive Padua cubature from Pitman RN 312 (227).
9. **Degani-Schiff-Tannor**: preprint read (215-217); Theorem 2 is N >= n + (1/2) max rank [A_i,A_j]; the BTTB mapping's "colength/Gorenstein" reading is not in the preprint.
10. **Curto-Fialkow**: flat extension theorem cited as Theorem 5.13 of the Memoir by two later papers (225); Memoir not read.
11. **Lin / Friis-Rordam**: statement and bibliographic data via secondary sources (218-219); neither read.
12. **Weisfeld**: metadata only (228).
Wrong DOI caught: 10.1016/0024-3795(80)90169-X (guessed) is Saad's Arnoldi paper; Paige 1980 is 10.1016/0024-3795(80)90167-6 (Crossref).

### Log (all on 2026-10-31)

| # | Query / URL | Outcome |
|---|---|---|
| 1 | shell `curl` https://arxiv.org/pdf/1403.2021 | proxy 403; shell cannot reach the web (as announced) |
| 2 | WebFetch arxiv.org/pdf/1403.2021 | KS: eq. (1.3), Thm 1.1 (1.1)-(1.2), Remarks 1.2-1.5, Cor 1.4, Davidson/Szarek, Hastings, Lin/Friis-Rordam refs |
| 3 | WebFetch arxiv.org/pdf/2602.05394 | Simons report: Problem 2.19 in section 2.6; cites [Pai76, Pai80]; scribes Chen, Greenbaum |
| 4 | WebFetch arxiv.org/abs/2401.01302 | Koiran abstract, no journal ref, no "wide open" in abstract |
| 5 | WebFetch arxiv.org/pdf/2401.01302 | "wide open" in Section 1.4 (two matrices) and Section 2 (diagonalisable uniqueness) |
| 6 | WebFetch arxiv.org/abs/1403.2021 | KS v3, DOI 10.1090/S0894-0347-2015-00823-2, journal not named on page |
| 7 | WebFetch arxiv.org/pdf/1403.2021 (2nd) | (1.3) is Section 1.1; sum of distances; universal C; Davidson Cor 4.5 with constant 50 sqrt(2); refs [9] [11] [13] [17] |
| 8 | WebFetch arxiv.org/pdf/2401.01302v1 | confirms two occurrences of the phrase; no "open problem" wording |
| 9 | WebFetch arxiv.org/html/2401.01302 | confirms, verbatim Section 2 sentence; section headings |
| 10 | WebFetch arxiv.org/pdf/2401.01302v1 (refs) | [2] DST 2005; [6] Kaliuzhnyi-Verbovetskyi-Spitkovsky-Woerdeman arXiv 0903.0090 Thm 4.2; [7] Kimsey-Woerdeman 2008 |
| 11 | WebSearch Paige thesis 1971 | located McGill pubClassic page, ProQuest, Math Genealogy |
| 12 | WebSearch Paige 1976 JIMA | same McGill listing; other hits |
| 13 | WebFetch cs.mcgill.ca/~chris/pubClassic/listClassic.html | PDFs of Pai80a, Pai76a, Pai72, thesis |
| 14 | WebFetch .../PaigeThesis.pdf | TOC (10 chapters), pp. 1-66 content (Thm 2.1 p. 17; eqs 3.12-3.16 pp. 28-29) |
| 15 | WebFetch .../PaigeThesis.pdf offset 100000 | beyond end: extracted text is 85,717 characters |
| 16 | WebFetch .../PaigeThesis.pdf offset 60000 | text ends within Ch. 5 at p. 66; no finite-precision Lanczos chapters |
| 17 | WebFetch .../76JIMA001.pdf | binary data, no text layer |
| 18 | WebFetch .../80LAIA001.pdf | binary data, no text layer |
| 19 | WebFetch sciencedirect pii 0024379580902290 | failed (guessed PII wrong) |
| 20 | WebFetch sciencedirect pii 0024379589902851 | Greenbaum 1989: title, LAA 113, pp. 7-63, Feb 1989, DOI, abstract, open archive |
| 21 | WebSearch Greenbaum title | arXiv hits (2106.02068, 2608.21268, 2507.16484), her book page |
| 22 | WebFetch sciencedirect .../pdfft (Greenbaum) | failed |
| 23 | WebSearch Paige 1980 pii | Berkeley report EECS-2014-165, Paige 2019 PDF, others |
| 24 | WebFetch doi.org/10.1016/0024-3795(80)90169-X | 302 to linkinghub (this DOI turned out to be Saad's paper) |
| 25 | WebFetch arxiv.org/html/2507.16484v1 | truncated: Greenbaum sqrt(u) intervals, "challenging and requires further research" |
| 26 | WebFetch arxiv.org/pdf/2106.02068 | Simonova-Tichy ETNA paper: no theorem statements for Greenbaum/Paige |
| 27 | WebFetch sciencedirect pii 002437958090169X | failed |
| 28 | WebSearch Meurant-Strakos Acta Numerica | karlin.mff.cuni.cz/~strakos/download/2006_MeSt.pdf |
| 29 | WebSearch Paige 1976 OUP | no OUP page; same hits |
| 30 | WebFetch karlin.mff.cuni.cz/~strakos/download/2006_MeSt.pdf | Thms 4.1-4.3 (Paige), Thm 4.9 (Greenbaum), digest of Sections up to 4.3 |
| 31 | WebSearch core.ac.uk Paige 1980 | no open copy found |
| 32 | WebFetch linkinghub.elsevier.com pii 002437958090169X | nothing |
| 33 | WebFetch www2.eecs.berkeley.edu/.../EECS-2014-165.pdf | Carson-Demmel: Paige 1980 Lemma 3.1, Thms 3.1, 4.1-4.3, Cor 3.1 mapping; eqs (4.2)-(4.12), (5.9)-(5.22) |
| 34 | WebFetch cs.mcgill.ca/~chris/pub/Pai19.pdf | Paige 2019 (SIMAX): citations of [1976] eq. (7.1), [1980] (3.18), Thm 3.1, thesis 8.7 |
| 35 | WebFetch ams.org/journals/mcom/1984-42-165/S0025-5718-1984-0725988-X/...pdf | Simon Math. Comp.: Thm 1 (p. 117), Thm 2 (p. 119), PRO details |
| 36 | WebSearch Simon LAA 61 | AMS page, Springer, Scott thesis, others |
| 37 | WebFetch same AMS PDF (references) | refs [10]-[13] Paige, [19] Scott, [20] Simon PAM-74, [21] Takahasi-Natori; Thm 2 hypotheses; no Thm 3/4 |
| 38 | WebFetch math.berkeley.edu/publications/analysis-symmetric-lanczos-process | D. S. Scott 1978 thesis (a different work) |
| 39 | WebFetch api.crossref.org/works?query.bibliographic=Simon... | LAA 61, 101-131, DOI 10.1016/0024-3795(84)90025-9 |
| 40 | WebFetch api.crossref.org/works/10.1007/s10543-025-01089-2 | BIT 65(4) art. 47, online 11 Nov 2025, print Dec 2025 |
| 41 | WebFetch api.crossref.org/works/10.1090/S0894-0347-2015-00823-2 | rate-limited (twice, #41 and #46) |
| 42 | WebFetch api.crossref.org/works/10.1007/BF01386371 | Weisfeld metadata |
| 43 | WebFetch api.crossref.org/works?query...Degani... | failed (client error) |
| 44 | WebFetch link.springer.com/article/10.1007/BF01386371 | Weisfeld: 3 pp., restricted; refs Forsythe, Householder, Stiefel |
| 45 | WebSearch Weisfeld eudml/gdz | no free scan found |
| 46 | (see 41) | rate limit |
| 47 | WebFetch eudml.org/search | robots disallowed |
| 48 | WebFetch gdz.sub.uni-goettingen.de/search | failed |
| 49 | WebFetch api.crossref.org/works/10.1090/S0894-0347-2015-00823-2 | KS: JAMS 29(1) 61-80, online 2015-01-08, print 2016-01 |
| 50 | WebFetch api.crossref.org/works?query...Xu... | irrelevant results |
| 51 | WebSearch Xu Trans AMS multivariate OP operator theory | AMS pages of Trans. AMS 343 (1994) 193-202 and 342 (1994) 855-866; Proc. AMS 119 (1993); Math. Comp. 62 (1994) |
| 52 | WebFetch ams.org/journals/tran/1994-343-01/...pdf | Xu TAMS 343: Thms 2.1, 2.2, Cor 2.3, Lemmas 4.3-4.5, Thms 3.1, 4.1, 4.6 |
| 53 | WebFetch ams.org/journals/tran/1994-342-02/...pdf | Xu TAMS 342: Thms 3.2, 3.4, 3.5, Cor 3.3 (numbering doubtful) |
| 54 | WebSearch Curto-Fialkow Memoir | arXiv math/0507069, Iowa repository, Kokyuroku, JOT |
| 55 | WebFetch arxiv.org/pdf/math/0507069 | Curto-Fialkow hyperbolic: flat extension cited as [CuFi1, Thm 5.13], eq. (1.8) |
| 56 | WebFetch ams.org/books/memo/0568/ | failed |
| 57 | WebFetch arxiv.org/pdf/math/0507069 (refs) | reference list not in the text |
| 58 | WebFetch iro.uiowa.edu ... Solution-of-the-truncated-complex-moment | Mem. AMS 119(568), pp. 1-50, 1996, DOI 10.1090/memo/0568, section outline |
| 59 | WebFetch kurims.kyoto-u.ac.jp/.../1259-10.pdf | unique flat extension (complex case) as Thm 2.3 of the Memoir |
| 60 | WebFetch jot.theta.ro/.../1999-042-002-010.pdf | Fialkow 1999: Theorem 1.1 flat extension statement ([3] Thm 5.13); Thm 1.4; reference list |
| 61 | WebSearch Friis-Rordam | hits only citing papers |
| 62 | WebSearch Lin Fields 13 | Herrera 2011.11800, Hastings-Loring 1012.3494, others |
| 63 | WebFetch arxiv.org/pdf/2011.11800 | Lin's theorem statement; Pearcy-Shields, Szarek, Davidson, Hastings, KS |
| 64 | WebFetch arxiv.org/pdf/math/0408076 | DST preprint: Thms 1-13, open questions Section 7 |
| 65 | WebSearch Xu Pitman RN 312 | library records, NIST OPSF |
| 66 | WebSearch Xu Padua Gamma_2 | BDMX arXiv math/0604604 and Padua pages |
| 67 | WebFetch math.nist.gov/opsf/books/xu.html | RN 312 metadata and description |
| 68 | WebFetch arxiv.org/pdf/1701.02709 | Xu survey (Askey-Bateman Vol. 2, Ch. 2): Thms 2.7-2.18; Section 6 text absent |
| 69 | WebFetch arxiv.org/pdf/math/0604604 | BDMX: Pitman book covers <= n extra points, Padua has n+1; Prop 3.4 from Xu 2000; Gamma_2 uncited |
| 70 | WebFetch arxiv.org/pdf/2602.05394 (2nd) | Problems 2.15-2.19 list; deflation in discussion; [Gre89] cited; ST not cited |
| 71 | WebFetch sciencedirect pii 0024379584900259 | failed |
| 72 | WebFetch doi.org/10.1016/0024-3795(84)90025-9 | 302 to linkinghub (not followed) |
| 73 | WebFetch api.openalex.org/works/doi:10.1016/0024-3795(84)90025-9 | Simon LAA metadata; bronze OA; 24 references |
| 74 | WebFetch sciencedirect .../0024379584900259/pdf | failed |
| 75 | WebFetch tidsskrift.dk/daimipb/article/view/7070 | Larsen BPRO report (context only) |
| 76-77 | WebFetch tidsskrift.dk download links | failed (7064) / garbled text (6029) |
| 78 | WebSearch Simon semiorthogonality theorem | Jia-Li arXiv 2001.04402 among hits |
| 79 | WebFetch arxiv.org/pdf/2001.04402 | Jia-Li cite Simon LAA 61 [26, Thm 5, Lemma 4] |
| 80 | WebFetch arxiv.org/pdf/2608.21268 | Chen 2026: Greenbaum via fourth root; Paige Thms 3.1-3.9; own Thm 4.6 (N = nk, symmetric completion) |
| 81 | WebSearch Greenbaum theorem width | arXiv hits |
| 82 | WebFetch arxiv.org/pdf/2507.16484 | Simonova-Tichy: Thms 1-4, W_k, Sections 5.2, 6.1; quotes in Sections 1 and 5 |
| 83 | WebSearch Weisfeld recurrence | arXiv 2202.04843 etc. |
| 84 | WebFetch arxiv.org/pdf/2202.04843 | no mention of Weisfeld |
| 85 | WebFetch api.crossref.org/works/10.1093/imamat/18.3.341 | Paige 1976: IMA J. Appl. Math. 18(3) 341-349 |
| 86 | WebFetch api.crossref.org/works/10.1016/0024-3795(80)90169-X | Saad (wrong DOI guess) |
| 87 | WebFetch api.crossref.org/works?query...Paige+Accuracy... | Paige 1980: DOI 10.1016/0024-3795(80)90167-6 |
| 88 | WebFetch api.crossref.org/works/10.1515/crll.1996.479.121 | Friis-Rordam, pp. 121-132 |
| 89 | WebFetch api.crossref.org/works?query...Degani... | DST: Numer. Math. 101(3) 479-500, DOI 10.1007/s00211-005-0628-z |

### Limits of this pass

Digests are produced by a model reading extracted page text: statements and numbers can contain digest errors (one suspected, the Xu TAMS 342 "Theorem 3.1"). The 1976 and 1980 Paige papers, Greenbaum's theorem, Lin, Friis-Rordam, the Curto-Fialkow Memoir, Weisfeld, the Pitman book and the Simon LAA paper were not read in the original. Nothing here is a novelty gate or a proof.
