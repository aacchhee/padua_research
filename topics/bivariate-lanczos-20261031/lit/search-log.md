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
