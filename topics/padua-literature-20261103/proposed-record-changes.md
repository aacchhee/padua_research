# Proposed changes to shared files — padua-literature-20261103

Apply only at PR preparation, after final LIT IDs are reserved (WORKFLOW, "Reserve fresh ranges").
- `LIT?padua-literature-claude-NN` are provisional IDs.
- Pack sections P2–P4 are appended below as their readers finish.
- Each block is literal. "Old" text must match the base exactly when this is applied; otherwise re-derive it.

## P1

### 1. literature/INDEX.md — new rows (append to the statement table)

```
| LIT?padua-literature-claude-01 | LITERATURE; theorem (read) | Kuznetsova (Ukr. Math. J. 47 (1995) 259–266, Thm 1): uniformly for n/m ∈ ℕ, the Lebesgue function of the discrete rhombic (|k|/m+|l|/n ≤ 1) Fourier operator on the uniform torus mesh equals (2/π²){|sin((mx+ny)/2) sin((mx−ny)/2)| + |cos((mx+ny)/2) cos((mx−ny)/2)|}(2 log m log n − log² m) + O(log n). Periodic setting; not Padua. Source of KL 2021 (3.27)–(3.30). | kuznetsova-1995 | Thm 1, eq. (1), p. 259 | [record](records/kuznetsova-1995.md) | complete (OCR); Thm 1 checked on page image |
| LIT?padua-literature-claude-02 | LITERATURE; attribution (read) | Kuznetsova 1995 credits the m = n odd-mesh case of her eq. (1) to Pimenova (Dokl. 1979), and states Thm 1 was announced at the Saratov Winter School 1982 (publ. 1983). | kuznetsova-1995 | pp. 260, 265 | [record](records/kuznetsova-1995.md) | complete (OCR) |
| LIT?padua-literature-claude-03 | LITERATURE; theorem (OCR only) | Pimenova (Dokl. Akad. Nauk SSSR 249 (1979) 52–54, Thm 1): pointwise ln² n asymptotics of the Lebesgue function of two-variable trigonometric interpolation with rhombic frequencies on the (2n+1)² grid, remainder O(ln n). For square frequencies the leading factor differs (eq. (3)). Exact constant UNCONFIRMED. | pimenova-1979 | Thm 1 p. 52; eq. (3) p. 53 | [record](records/pimenova-1979.md) | complete OCR text; page images not inspected |
| LIT?padua-literature-claude-04 | LITERATURE; theorems (read) | Ehlich–Zeller (Math. Ann. 164 (1966) 105–112): explicit 1-D Lebesgue constants. Equispaced trigonometric interpolation: maximum at the midpoint of every node interval (Satz 1–2). Chebyshev zeros: global maximum at x = ±1 (Satz 3, (3.6)–(3.7)). Chebyshev extrema: middle interval for odd n (Satz 4). Table 2 gives local maxima for n = 10. | ehlich-zeller-1966 | pp. 105–111 | [record](records/ehlich-zeller-1966.md) | complete (OCR) |
| LIT?padua-literature-claude-05 | LITERATURE; conjecture (read) | Caliari–De Marchi–Sommariva–Vianello, 5ECM poster (Amsterdam 2008): conjecture that the Padua Lebesgue maximum is ≈ (4/π²) log² n and is attained at one of the vertices of the square. | cdmsv-poster-2008 | single page, "The Lebesgue constant" | [record](records/cdmsv-poster-2008.md) | complete |
| LIT?padua-literature-claude-06 | LITERATURE; observation and conjecture (read) | Bos–Caliari–De Marchi–Vianello (Computing 76 (2006) 311–324): for XU points the Lebesgue function appears to peak at the four vertices (p. 318); Conjecture (17): maximum ≈ ((2/π) log(n+1))², attained at the four vertices (p. 319); open (p. 324). | bcdmv-computing-2006 | pp. 318–319, 324 | [record](records/bcdmv-computing-2006.md) | located passages |
| LIT?padua-literature-claude-07 | LITERATURE; theorems (read) | Brutman (SINUM 15 (1978) 694–704). For Chebyshev zeros the local maxima of the Lebesgue function strictly decrease from the ends toward the middle (Thm 1). For Chebyshev extrema they strictly increase toward the middle (eq. (44)). Interior second-kind nodes give Λ_n = n+1 (eq. (47)). p. 695: Λ_n(T) = λ_n(T;1) was conjectured by Luttmann–Rivlin and proved by Ehlich–Zeller (see also Powell 1967). | brutman-1978 | Thm 1 p. 697; (44)–(47) pp. 702–703; p. 695 | [record](records/brutman-1978.md) | complete |
| LIT?padua-literature-claude-08 | LITERATURE; theorems (partial reading) | Günttner (SINUM 17 (1980) 512–520; SINUM 25 (1988) 461–469). Asymptotics (2/π) log n + c + r_n for the Lebesgue constants at Chebyshev, expanded Chebyshev and extrema nodes and for equispaced trigonometric interpolation, with error bounds. Deviation between local maxima below (2/π) log 2 for Chebyshev zeros. An asymptotic expansion exists for extended Chebyshev nodes. | guenttner-1980-1988 | 1980 Thms 2–3; 1988 §2 | [record](records/guenttner-1980-1988.md) | statements only |
```

### 2. literature/INDEX.md — addenda (append to the addenda list at the end)

```
- **LIT-377 / LIT-326 — 2026-11-03 primary-reading addendum (padua-literature-20261103):** journal PDF of De Marchi, Constr. Math. Anal. 5(1) (2022) 14–36, read. §3.3 "Some open problems" starts on p. 22. Item (2) on p. 23 states, as an observation with Fig. 7, that the Lebesgue function has its maxima in the corners, where there are no Padua points. The corner part of LIT-377 is now VERIFIED at this locator; its other parts are unchanged. [P1 comparison](../topics/padua-literature-20261103/p1-comparison.md).
- **LIT-379 — 2026-11-03 locator addendum (padua-literature-20261103):** for arXiv 2009.07114v1 the printed running heads coincide with the PDF pages. Confirmed: Thm 2.1 and the unnumbered Padua consequence on p. 4; Lemma 3.5 with (3.20) on pp. 10–11; Lemma 3.6 with (3.29) on p. 11, proof on p. 12. The proof imports (3.25)–(3.26) from Kuznetsova 1977 and (3.27)–(3.30) from Kuznetsova 1995 (LIT?padua-literature-claude-01). The journal pagination is unchecked. [record](records/kolomoitsev-lomako-2021.md).
- **LIT-388 — 2026-11-03 complete-reading addendum (padua-literature-20261103):** arXiv 2605.23299v1 was read in full. It makes no statement on the location of the global maximum on the square (its 2-D content is local-maxima counts only). The "Powell, 1965" credit (§2.1, p. 3) has no reference entry; see Powell, Comput. J. 9 (1967) 404–407 and Ehlich–Zeller 1966 (LIT?padua-literature-claude-04). [record](records/bialas-ciez-demarchi-suder-2026.md).
```

### 3. literature/CORPUS.md — new rows (append to the main corpus table)

```
| kuznetsova-1995 | Kuznetsova, Asymptotic behavior of Lebesgue functions of two variables, Ukr. Math. J. 47(2) (1995) 259–266 | https://doi.org/10.1007/BF01056716 | Springer via NTNU | complete (OCR); Thm 1 on page image | [record](records/kuznetsova-1995.md) | Lemmas 1–2 page images |
| pimenova-1979 | Pimenova, On Lebesgue functions for some interpolation polynomials in two variables, Dokl. Akad. Nauk SSSR 249(1) (1979) 52–54 | https://www.mathnet.ru/eng/dan43113 (no DOI) | free scan | complete OCR text only | [record](records/pimenova-1979.md) | constant in Thm 1 from page image |
| ehlich-zeller-1966 | Ehlich–Zeller, Auswertung der Normen von Interpolationsoperatoren, Math. Ann. 164 (1966) 105–112 | https://doi.org/10.1007/BF01429047 | Springer via NTNU | complete (OCR) | [record](records/ehlich-zeller-1966.md) | formulas from page images |
| cdmsv-poster-2008 | Caliari–De Marchi–Sommariva–Vianello, Near-optimal interpolation and quadrature in two variables: the Padua points, poster, 5ECM 2008 | https://www.math.unipd.it/~marcov/pdf/poster5ecm.pdf | free | complete | [record](records/cdmsv-poster-2008.md) | one lost relation symbol |
| bcdmv-computing-2006 | Bos–Caliari–De Marchi–Vianello, A numerical study of the Xu polynomial interpolation formula in two variables, Computing 76 (2006) 311–324 | https://doi.org/10.1007/s00607-005-0137-z | author PDF | pp. 318–319, 324 | [record](records/bcdmv-computing-2006.md) | §§1–2, 4 |
| kolomoitsev-lomako-2021 | (existing key; record file added) | https://doi.org/10.1016/j.amc.2021.126192 | arXiv v1 + AC-supplied journal PDF | locators confirmed in both versions | [record](records/kolomoitsev-lomako-2021.md) | — |
| brutman-1978 | Brutman, On the Lebesgue function for polynomial interpolation, SINUM 15(4) (1978) 694–704 | https://doi.org/10.1137/0715046 | AC-supplied PDF | complete | [record](records/brutman-1978.md) | page-image check of the constants |
| guenttner-1980-1988 | Günttner, SINUM 17 (1980) 512–520; SINUM 25 (1988) 461–469 | https://doi.org/10.1137/0717043 ; https://doi.org/10.1137/0725030 | AC-supplied PDFs | statements only | [record](records/guenttner-1980-1988.md) | proofs |
| bialas-ciez-demarchi-suder-2026 | Białas-Cież–De Marchi–Suder, Geometric properties of the Lebesgue function, arXiv 2605.23299 | https://arxiv.org/abs/2605.23299 | free | complete v1 | [record](records/bialas-ciez-demarchi-suder-2026.md) | newer versions |
```

### 4. literature/lattice-unisolvence/records/demarchi-2022.md — addendum (record owned by a merged topic)

Old (end of file):
```
## History

2026-10-31: bounded campaign inspection recorded.
```
New:
```
## Addendum 2026-11-03 (padua-literature-20261103, Claude claude-opus-5-5 high)

Additional primary reading of the journal PDF covered §3.3, pp. 22–23. Item (2) of "Some open problems" (p. 23) states, as an observation with reference to Fig. 7, that the Padua Lebesgue function has its maxima in the corners where there are no Padua points. Provisional statement ID: covered by the LIT-377/LIT-326 addendum in INDEX. This is a published observation, not a proof. Topic comparison: [P1](../../../topics/padua-literature-20261103/p1-comparison.md).

## History

2026-10-31: bounded campaign inspection recorded.
2026-11-03: §3.3(2) addendum (padua-literature-20261103).
```

### 5. Audit F6 locator qualification in padua-proof-attempts-2 (files owned by a merged topic)

In each of these three files, replace the qualification line:
- `topics/padua-proof-attempts-2-20261101/attempts/T-A2.md` line 25;
- `.../theory/proof-attempts-2-codex-03-corner-log-coefficient.md` line 60;
- `.../theory/proof-attempts-2-codex-04-corner-product-comparison.md` line 66.

Old:
```
Page-locator qualification (audit-01 F6): printed page numbers below are per developer reading; the auditor confirmed theorem/equation content through page-less text, without confirming PDF pagination. LIT-379 identifies KL2021 and LIT-312 identifies Bos2006.
```
New:
```
Page-locator qualification (audit-01 F6): printed page numbers below are per developer reading; the auditor confirmed theorem/equation content through page-less text, without confirming PDF pagination. LIT-379 identifies KL2021 and LIT-312 identifies Bos2006. Update 2026-11-03 (padua-literature-20261103): the KL2021 arXiv v1 locators (Thm 2.1 p. 4; Lemma 3.5 (3.20) pp. 10–11; Lemma 3.6 (3.29) pp. 11–12) were confirmed against the printed running heads. The published AMC version has the same numbering (PDF pp. 4, 8, 9); (3.29) is imported by KL from Kuznetsova 1995 (literature/records/kuznetsova-1995.md). The Bos2006 locators remain per developer reading.
```

Mathematical content and status are unchanged. These are locator and attribution notes only.

## P4 (from the P4 reader, Claude Opus 5.5 high; integrated by the orchestrator)

Addenda for existing records are under [addenda/](addenda/).


Literal old→new blocks, for merging into `topics/padua-literature-20261103/proposed-record-changes.md` (section P4) and for application at PR preparation only. The "old" lines were copied from the branch head `2a9d02f` on 2026-11-03; re-derive them if the base has moved. `LIT?padua-literature-claude-70…84` are provisional IDs (range 70–89 reserved for P4; 85–89 unused).

## 1. literature/INDEX.md — replace existing rows

### LIT-346 (INDEX.md line 173 at 2a9d02f)

Old:

```
| LIT-346 (LIT?programme-ideas-claude-21) | Coverage-qualified LITERATURE; fact | Van Barel–Van Buggenhout–Vandebril (Appl. Numer. Math. 2023, arXiv 2302.00355): univariate downdating of discrete-OP recurrences by perfect-shift QR deflation posed as an IEP. Author list conflict in the notes (with/without Faghih) unresolved. | vanbarel-vanbuggenhout-vandebril-2023 | arXiv 2302.00355; doi 10.1016/j.apnum.2023.07.009 | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Padua points research since 2010.md, "Leuven built the missing toolkit"; bibliographic table); secondary; new source statement |
```

New:

```
| LIT-346 (LIT?programme-ideas-claude-21) | Coverage-qualified LITERATURE; fact | Van Barel–Van Buggenhout–Vandebril (Appl. Numer. Math. 200 (2024) 429–452, online 2023; arXiv 2302.00355): univariate downdating of discrete-OP and ORF recurrences when nodes are removed, by perfect-shift **RQ** deflation (a QR step would break the weight condition), in explicit, implicit and eigenvector (Mastronardi–Van Dooren) variants; ORFs via rational RQZ on Hessenberg pencils. Exactly three authors (no Faghih). | vanbarel-vanbuggenhout-vandebril-2023 | arXiv v1 pp. 1, 11–14, 18–19; future-work sentences pp. 25, 34 | [record](records/vanbarel-vanbuggenhout-vandebril-2023.md) | VERIFIED (arXiv v1 exact pages, padua-literature-20261103 P4, 2026-11-03; journal version not read); supersedes the secondary baseline reading |
```

### LIT-347 (INDEX.md line 174 at 2a9d02f)

Old:

```
| LIT-347 (LIT?programme-ideas-claude-22) | Coverage-qualified LITERATURE; fact | Faghih–Rinelli–Van Barel–Vandebril–Vermeiren (SINUM 2026, arXiv 2506.19796): for discrete multiple OPs (step-line, banded Hessenberg with r superdiagonals) two IEP solvers are compared; the biorthogonal-Lanczos variant is not backward stable, the core-transformation (LU-eliminator) variant appears backward stable for N < 25 and loses it beyond; authors say a systematic comparison "would be interesting" and that they know no extension of Laurie's approach to MOPs. | faghih-et-al-2025 | arXiv 2506.19796; doi 10.1137/25m1770965 | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Padua points research since 2010.md, MOP table; branch record records_lanczos/faghih-et-al-2025.md is secondary); secondary; new source statement; overlaps LIT-119 (PR #10) |
```

New:

```
| LIT-347 (LIT?programme-ideas-claude-22) | Coverage-qualified LITERATURE; fact | Faghih–Rinelli–Van Barel–Vandebril–Vermeiren (SIAM J. Numer. Anal. 64(4) (2026) 1190–1216, arXiv 2506.19796): for discrete multiple OPs (step-line, banded Hessenberg with r superdiagonals) two IEP solvers are compared, biorthogonal Lanczos with multiple starting vectors (IEP_KRYL and reorthogonalized variants) and non-unitary core transformations (IEP_CORE). IEP_CORE and IEP_KRYLREORTH(full) are backward stable for most N < 25 and lose it for N ≥ 25; IEP_KRYL is not backward stable for any N considered; on Kravchuk/Hahn all methods are weakly stable. §7 future work: IEP conditioning; updating/downdating; extending Laurie's approach via vector or branched continued fractions (named as a possibility not discussed, not a claim that none is known); nearest-neighbour recurrences; comparison with Filipuk–Haneczok–Van Assche 2015. | faghih-et-al-2025 | Alg. 4.1 p. 1199; Alg. 5.1 p. 1205; §6.2 p. 1211; §7 p. 1213 | [record](records/faghih-et-al-2025.md) | VERIFIED-fulltext (published PDF read 2026-11-03, topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md); §2/§4.1 proofs not read line by line; overlaps LIT-119 (PR #10) |
```

### LIT-348 (INDEX.md line 175 at 2a9d02f)

Old:

```
| LIT-348 (LIT?programme-ideas-claude-23) | Coverage-qualified LITERATURE; stated future work | Faghih–Van Barel–Vandebril (arXiv 2608.25758, Aug 2026): updating (by IEP) and downdating (QR-type eigenvalue deflation) for discrete MOPs, univariate; stability analysis is listed as future work; the seed is not cited. | faghih-vanbarel-vandebril-2026 | arXiv 2608.25758 | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Open problems verification.md §3 C; reports/Round 3 … rank 6 "Leuven's stated future work"; branch record records_lanczos/faghih-vanbarel-vandebril-2026.md, LIT-118, secondary); secondary; new source statement; overlaps LIT-117, LIT-118 (PR #10); flag in integration-map-pr10 |
```

New:

```
| LIT-348 (LIT?programme-ideas-claude-23) | Coverage-qualified LITERATURE; stated future work | Faghih–Van Barel–Vandebril (arXiv 2608.25758v1, Aug 2026; no journal version found as of 2026-11-03): updating (non-unitary eliminator similarity transformations on the IEP, with a norm-balancing diagonal scaling) and downdating (two perfect-shift RL steps from the stored left/right eigenvectors) for discrete MOPs on the real line, univariate, r = 2. §6 future work: other multi-index paths (nearest-neighbour MOPs; MOPs on the complex plane), inner products with derivatives, and a thorough stability analysis. Van Barel–Chesnokov 2010 is not cited. | faghih-vanbarel-vandebril-2026 | §6 p. 24; references pp. 25–26 | [baseline](../topics/programme-ideas-20261031/lit/baseline.md); [record](records/faghih-vanbarel-vandebril-2026.md) | VERIFIED-fulltext (arXiv v1 pp. 1–26, padua-literature-20261103 P4, 2026-11-03); overlaps LIT-117, LIT-118 (PR #10); flag in integration-map-pr10 |
```

### LIT-420 (INDEX.md line 247 at 2a9d02f)

Old:

```
| LIT-420 (LIT?programme-ideas-claude-105) | Coverage-qualified LITERATURE; fact | Multiple-OP recurrence computation: Filipuk–Haneczok–Van Assche (Numer. Algorithms 70 (2015) 519–543) give two algorithms for nearest-neighbour recurrence coefficients; Aptekarev–Denisov–Yattselev (Trans. AMS 2020, arXiv 1806.10531) treat Jacobi matrices on trees and exclude finitely supported measures. | filipuk-haneczok-vanassche-2015; aptekarev-denisov-yattselev-2020 | as reported | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: adv_F2_F5_F10_F9.md lines 91–103; reports/Round 3 … F5); secondary; new source statement |
```

New:

```
| LIT-420 (LIT?programme-ideas-claude-105) | Coverage-qualified LITERATURE; fact | Multiple-OP recurrence computation: Filipuk–Haneczok–Van Assche (Numer. Algorithms 70 (2015) 519–543, arXiv 1406.0364) treat (1) step-line → shifted step-line → nearest-neighbour coefficients, incl. the marginal three-term coefficients (r = 2), and (2) marginal three-term coefficients → nearest-neighbour and step-line coefficients (general r via the compatibility relations (3.11)–(3.13), requiring b_{n,i} ≠ b_{n,j}); Maple procedures, no stability analysis. Aptekarev–Denisov–Yattselev (Trans. AMS 2020, arXiv 1806.10531) treat Jacobi matrices on trees and exclude finitely supported measures. | filipuk-haneczok-vanassche-2015; aptekarev-denisov-yattselev-2020 | FHV: arXiv v2 pp. 1–3, 8, 13, 18–21; ADY: as reported | [baseline](../topics/programme-ideas-20261031/lit/baseline.md); [record](records/filipuk-haneczok-vanassche-2015.md) | FHV half: VERIFIED (arXiv v2 exact pages, P4 2026-11-03); ADY half: UNVERIFIED (input: adv_F2_F5_F10_F9.md lines 91–103; reports/Round 3 … F5); secondary |
```

### LIT-117 (INDEX.md line 316 at 2a9d02f)

Old:

```
| LIT-117 (LIT?bivariate-lanczos-claude-052) | reported / UNVERIFIED / multiple-OP downdating with perfect shifts | Reported: downdates MOPs with RL steps using perfect shifts and the stored biorthonormal bases (rows of V_N, W_N), following Mastronardi-Van Dooren (SIMAX 2018); no multivariate mention; the conclusion says a thorough stability analysis remains important. | faghih-vanbarel-vandebril-2026 | conclusion | [record](records/faghih-vanbarel-vandebril-2026.md) | supplied secondary account only; original fulltext NOT inspected |
```

New:

```
| LIT-117 (LIT?bivariate-lanczos-claude-052) | LITERATURE / VERIFIED-fulltext / multiple-OP downdating with perfect shifts | Downdates step-line MOPs (r = 2) by two perfect-shift RL steps built from the stored left and right eigenvectors (the j-th rows of V_N and W_N, iteratively refined), following Mastronardi–Van Dooren (SIMAX 2018); eliminators then restore the weight conditions and the band; no multivariate mention; the conclusion says a thorough stability analysis remains important. | faghih-vanbarel-vandebril-2026 | §4.1–4.3 pp. 13–19; §6 p. 24 | [record](records/faghih-vanbarel-vandebril-2026.md) | complete full text (arXiv v1 pp. 1–26), read 2026-11-03 (padua-literature-20261103 P4) |
```

### LIT-118 (INDEX.md line 317 at 2a9d02f)

Old:

```
| LIT-118 (LIT?bivariate-lanczos-claude-053) | reported / UNVERIFIED / stated future work (reported) | Reported conclusion: extend to MOPs for other multi-index paths (nearest-neighbour MOPs, MOPs on the complex plane); MOP bases are typically so ill conditioned that computing large-degree MOPs becomes infeasible. | faghih-vanbarel-vandebril-2026 | conclusion | [record](records/faghih-vanbarel-vandebril-2026.md) | supplied secondary account only; original fulltext NOT inspected |
```

New:

```
| LIT-118 (LIT?bivariate-lanczos-claude-053) | LITERATURE / VERIFIED-fulltext / stated future work | §6: extend to other multi-index paths (nearest-neighbour MOPs; MOPs on the complex plane, citing a unit-circle MOP paper), to inner products with derivatives, and carry out a thorough stability analysis. Separately, the Introduction says the bases computed by the SINUM Lanczos/core methods are so ill conditioned that large-degree MOPs are infeasible in double precision, and that the new scaling and updating improve this. | faghih-vanbarel-vandebril-2026 | §6 p. 24; Introduction p. 3 | [record](records/faghih-vanbarel-vandebril-2026.md) | complete full text (arXiv v1), read 2026-11-03 (padua-literature-20261103 P4) |
```

### LIT-119 (INDEX.md line 318 at 2a9d02f)

Old:

```
| LIT-119 (LIT?bivariate-lanczos-claude-054) | reported / UNVERIFIED / IEP variants for MOPs (reported) | Reported table: IEP_KRYL (biorthogonal Lanczos, several starts) not backward stable; IEP_CORE (non-unitary eliminators) appears backward stable only for N < 25; authors not aware of an extension of Laurie's approach to MOPs. | faghih-et-al-2025 | no locator | [record](records/faghih-et-al-2025.md) | supplied secondary account only; original fulltext NOT inspected |
```

New:

```
| LIT-119 (LIT?bivariate-lanczos-claude-054) | LITERATURE / VERIFIED-fulltext / IEP variants for MOPs | IEP_KRYL (biorthogonal Lanczos, several starts) is not backward stable for any N considered; IEP_CORE (non-unitary eliminators) and IEP_KRYLREORTH(full) are backward stable for most N < 25 and lose it for N ≥ 25; on Kravchuk/Hahn all methods are weakly stable. §7 names extending Laurie's approach via vector/branched continued fractions as a possibility not discussed (not a claim that none is known). | faghih-et-al-2025 | Alg. 4.1 p. 1199; Alg. 5.1 p. 1205; §6.2 p. 1211; §7 p. 1213 | [record](records/faghih-et-al-2025.md) | published PDF read 2026-11-03 (topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md); §2/§4.1 proofs not read line by line |
```

## 2. literature/INDEX.md — new rows (append to the statement table, after the P1–P3 rows)

```
| LIT?padua-literature-claude-70 | LITERATURE; method (read) | Faghih–Van Barel–Vandebril (arXiv 2608.25758v1): updating the step-line MOP IEP (r = 2, real nodes, AT-system) by embedding, a weight-fixing transformation and 2N−3 non-unitary triangular eliminators alternating between the last row and the last column; monicity is dropped; breakdown assumed absent; no error analysis. | faghih-vanbarel-vandebril-2026 | Problem 3.1 p. 7; Lemma 3.1 pp. 8–9; p. 10; Fig. 1 p. 11 | [record](records/faghih-vanbarel-vandebril-2026.md) | complete full text (arXiv v1) |
| LIT?padua-literature-claude-71 | LITERATURE; method + numerical finding (read) | Same source: a diagonal scaling that balances the norms of corresponding columns of W and V; with it the updating keeps about five digits in the recurrence residual at N = 100 for multiple Kravchuk/Hahn MOPs, where the monic unscaled variant loses all digits for N ≈ 20–25. The authors credit both the scaling and the incremental updating. Residual-based, not a backward-error test. | faghih-vanbarel-vandebril-2026 | §3.1 pp. 10–11; Ex. 5.1–5.2 p. 20; Fig. 2 p. 21 | [record](records/faghih-vanbarel-vandebril-2026.md) | complete full text (arXiv v1) |
| LIT?padua-literature-claude-72 | LITERATURE; numerical finding (read) | Same source: bases regenerated from the recurrence lose biorthogonality as the degree grows, comparably with the computed and the exact Kravchuk/Hahn H; the authors attribute the loss to running the recurrence, not to coefficient error. | faghih-vanbarel-vandebril-2026 | pp. 21–22, Fig. 3 | [record](records/faghih-vanbarel-vandebril-2026.md) | complete full text (arXiv v1) |
| LIT?padua-literature-claude-73 | LITERATURE; method + numerical finding (read) | Same source: downdating a node by two perfect-shift RL steps (left eigenvector = j-th row of V_N, right = j-th row of W_N, iteratively refined; after Mastronardi–Van Dooren), then two lower and N−4 upper eliminators; errors stay about 1e-11 to 1e-9 over 20 downdates from N = 40 and over 20 down/up cycles. | faghih-vanbarel-vandebril-2026 | §4 pp. 11–19; §5.2 pp. 22–24 | [record](records/faghih-vanbarel-vandebril-2026.md) | complete full text (arXiv v1) |
| LIT?padua-literature-claude-74 | LITERATURE; stated future work (read) | Same source, §6: other multi-index paths (nearest-neighbour MOPs; MOPs on the complex plane), inner products with derivatives, and a thorough stability analysis. No bivariate/multivariate setting anywhere in the text. | faghih-vanbarel-vandebril-2026 | §6 p. 24 | [record](records/faghih-vanbarel-vandebril-2026.md) | complete full text (arXiv v1); keyword search |
| LIT?padua-literature-claude-75 | LITERATURE; attribution (read) | Van Barel–Van Buggenhout–Vandebril (ANM 200 (2024) 429–452) has exactly three authors; Faghih is not an author. | vanbarel-vanbuggenhout-vandebril-2023 | arXiv v1 p. 1; Crossref | [record](records/vanbarel-vanbuggenhout-vandebril-2023.md) | title page read |
| LIT?padua-literature-claude-76 | LITERATURE; method (read) | Same source: OP downdating by a perfect-shift RQ (not QR) step that keeps the weight condition; explicit, implicit and eigenvector variants; ORFs via rational RQZ on Hessenberg pencils. | vanbarel-vanbuggenhout-vandebril-2023 | pp. 1–3, 11–14, 18–19 | [record](records/vanbarel-vanbuggenhout-vandebril-2023.md) | arXiv v1 exact pages |
| LIT?padua-literature-claude-77 | LITERATURE; numerical finding + stated future work (read) | Same source: the eigenvector method is most accurate but sensitive to eigenvector accuracy (breakdown example with one refinement step); future research: the choice of refinement count (p. 25) and the most stable pencil variant (p. 34). arXiv v1 has no conclusions section. | vanbarel-vanbuggenhout-vandebril-2023 | pp. 21–25, 34, 42 | [record](records/vanbarel-vanbuggenhout-vandebril-2023.md) | arXiv v1 exact pages |
| LIT?padua-literature-claude-78 | LITERATURE; method summary, no future work (read) | Faghih–Van Barel–Van Buggenhout–Vandebril (Numer. Algorithms 100 (2025) 1837–1865): Sobolev ORF recurrences via a rational-Gauss discretization and a Hessenberg-pencil IEP, solved by unitary updating or via a Sobolev OP matrix; the conclusion states no future work. Ref. [13] gives a wrong arXiv ID (2303.11284) for the companion paper. | faghih-vanbarel-vanbuggenhout-vandebril-2025-sorf | p. 1; §5 pp. 16–17; refs | [record](records/faghih-vanbarel-vanbuggenhout-vandebril-2025-sorf.md) | abstract + conclusion |
| LIT?padua-literature-claude-79 | LITERATURE; attribution + no future work (read) | Same authors, NLAA 32 (2025) e70017: arXiv 2407.05945 is a probable preprint (same authors and content per the Crossref abstract; different title; no journal-ref) — content-consistent, not confirmed. The preprint's conclusion states no future work. | faghih-vanbarel-vanbuggenhout-vandebril-2025-nla | preprint pp. 1, 21–22; Crossref abstract | [record](records/faghih-vanbarel-vanbuggenhout-vandebril-2025-nla.md) | abstract + conclusion |
| LIT?padua-literature-claude-80 | LITERATURE; method + claims (read) | Laudadio–Mastronardi–Van Assche–Van Dooren (JCAM 451 (2024) 116109): MATLAB package GaussMOP for simultaneous Gaussian quadrature (r = 2) from the banded lower Hessenberg matrix: diagonal balancing, then Ehrlich–Aberth in O(n²); r > 2 only sketched; reliability shown against 80-digit references; no backward-error statement, no stated future work. | laudadio-mastronardi-vanassche-vandooren-2024 | arXiv v1 pp. 1–4, 16–23 | [record](records/laudadio-mastronardi-vanassche-vandooren-2024.md) | arXiv v1 exact pages |
| LIT?padua-literature-claude-81 | LITERATURE; method + stability claims (read) | Laudadio–Mastronardi–Van Dooren (Numer. Algorithms 100 (2025) 621–643): uses total nonnegativity of the MOP recurrence matrix: forward-stable scaling (Thm 1), TN-preserving reduction to symmetric tridiagonal (aimed at backward stability), Ehrlich–Aberth plus Givens eigenvectors, O(n²); conjectures extension to r > 2 and nonnegative intervals. | laudadio-mastronardi-vandooren-2025 | pp. 621–623, 627–629, 635, 639–641 | [record](records/laudadio-mastronardi-vandooren-2025.md) | exact pages; §5 proof not read |
| LIT?padua-literature-claude-82 | LITERATURE; method (read) | Filipuk–Haneczok–Van Assche (Numer. Algorithms 70 (2015) 519–543): step-line ↔ nearest-neighbour ↔ marginal recurrence coefficients; Maple procedures; general-r compatibility relations (3.11)–(3.13); requires b_{n,i} ≠ b_{n,j}; no stability analysis. | filipuk-haneczok-vanassche-2015 | arXiv v2 pp. 1–3, 8, 13, 18–21 | [record](records/filipuk-haneczok-vanassche-2015.md) | arXiv v2 exact pages + keyword search |
| LIT?padua-literature-claude-83 | LITERATURE; correspondence + stated future work (read) | Rinelli–Vandebril (arXiv 2605.16954): block Krylov subspaces ≅ matrix-polynomial spaces (no deflation); block Szegő/CMV procedures in the unitary case; future work: the deflated case and block Gaussian quadrature. | rinelli-vandebril-2026 | pp. 1–2, 26 | [record](records/rinelli-vandebril-2026.md) | abstract, introduction, conclusion |
| LIT?padua-literature-claude-84 | LITERATURE; method + stated future work (read) | Vermeiren (arXiv 2601.11317): orthonormal rational function vectors of length k ↔ IEP with a pencil of k-Hessenberg matrices; updating (rotations) beats a rational-Krylov-type method; future work: downdating. | vermeiren-2026 | pp. 1–2, 18 | [record](records/vermeiren-2026.md) | abstract, introduction, conclusion |
```

## 3. literature/CORPUS.md — replace existing rows

### vanbarel-vanbuggenhout-vandebril-2023 (CORPUS.md line 87 at 2a9d02f)

Old:

```
| vanbarel-vanbuggenhout-vandebril-2023 | as cited in programme-ideas baseline row(s) 21 | see baseline row | local PDF or campaign input note per row | UNVERIFIED (statement-level) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | citation completion pending source verification; final IDs do not clear this gap |
```

New:

```
| vanbarel-vanbuggenhout-vandebril-2023 | M. Van Barel, N. Van Buggenhout, R. Vandebril, Algorithms for modifying recurrence relations of orthogonal polynomial and rational functions when changing the discrete inner product, Appl. Numer. Math. 200 (2024) 429–452 (online 2023) | https://doi.org/10.1016/j.apnum.2023.07.009 ; https://arxiv.org/abs/2302.00355 | arXiv v1 (open) | exact pages of arXiv v1 (pp. 1–3, 11–14, 17–19, 21–26, 33–34, 38–42), P4 2026-11-03 | [record](records/vanbarel-vanbuggenhout-vandebril-2023.md) | journal version; Thm 3.3; §§6–8 theory |
```

### filipuk-haneczok-vanassche-2015 (CORPUS.md line 149 at 2a9d02f)

Old:

```
| filipuk-haneczok-vanassche-2015 | as cited in programme-ideas baseline row(s) 105 | see baseline row | local PDF or campaign input note per row | UNVERIFIED (statement-level) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | citation completion pending source verification; final IDs do not clear this gap |
```

New:

```
| filipuk-haneczok-vanassche-2015 | G. Filipuk, M. Haneczok, W. Van Assche, Computing recurrence coefficients of multiple orthogonal polynomials, Numer. Algorithms 70(3) (2015) 519–543 | https://doi.org/10.1007/s11075-015-9959-8 ; https://arxiv.org/abs/1406.0364 | arXiv v2 (open) | exact pages of arXiv v2 (pp. 1–3, 8, 10, 13–15, 18–21) + whole-text keyword search, P4 2026-11-03 | [record](records/filipuk-haneczok-vanassche-2015.md) | §2 derivations; journal version |
```

### faghih-vanbarel-vandebril-2026 (CORPUS.md line 215 at 2a9d02f)

Old:

```
| faghih-vanbarel-vandebril-2026 | Faghih, Van Barel, Vandebril, MOP updating/downdating by deflation, arXiv:2608.25758 (27 Aug 2026); title not given in inputs | arXiv 2608.25758 (not fetched by me) | supplied account; fulltext pending | supplied secondary account only (see notes/verify_algorithmic_problems.md Problem 1(g); notes/recent_multivariate_NLA.md §1 item 6, R3, R4; reports/Open problems verification.md §3 C); original fulltext NOT inspected | [record](records/faghih-vanbarel-vandebril-2026.md) | Fulltext. |
```

New:

```
| faghih-vanbarel-vandebril-2026 | A. Faghih, M. Van Barel, R. Vandebril, Updating and Downdating the Recurrences of Discrete Multiple Orthogonal Polynomials on the Real Line, arXiv:2608.25758v1 (26 Aug 2026) | https://arxiv.org/abs/2608.25758 | arXiv v1 (open); no journal version found 2026-11-03 | complete full text (arXiv v1 pp. 1–26), P4 2026-11-03 | [record](records/faghih-vanbarel-vandebril-2026.md) | figure images not inspected; re-check for a journal version |
```

### faghih-et-al-2025 (CORPUS.md line 216 at 2a9d02f)

Old:

```
| faghih-et-al-2025 | Faghih, Rinelli, Van Barel, Vandebril, Vermeiren, Krylov vs core-transformation IEPs for MOPs, arXiv:2506.19796; title not given in inputs | https://arxiv.org/pdf/2506.19796 (as cited in reports/Padua points research since 2010.md) | supplied account; fulltext pending | supplied secondary account only (see reports/Padua points research since 2010.md Leuven section; notes/recent_multivariate_NLA.md §1 item 6); original fulltext NOT inspected | [record](records/faghih-et-al-2025.md) | Fulltext. |
```

New:

```
| faghih-et-al-2025 | A. Faghih, M. Rinelli, M. Van Barel, R. Vandebril, R. Vermeiren, Krylov and Core Transformation Algorithms for an Inverse Eigenvalue Problem to Compute Recurrences of Multiple Orthogonal Polynomials, SIAM J. Numer. Anal. 64(4) (2026) 1190–1216 | https://doi.org/10.1137/25M1770965 ; https://arxiv.org/abs/2506.19796 ; code https://gitlab.kuleuven.be/numa/public/IEP-MOP (cited, not loaded) | AC-supplied published PDF | published PDF: §1, §3.2, §4.2–4.4, §5 opening + Alg. 5.1, §6.2–6.3, §7, references (assessment note 2026-11-03) | [record](records/faghih-et-al-2025.md) | §2 and §4.1 proofs; full §5 example |
```

Note: line 87 and line 149 sit in tables whose header has the same seven columns (Key | Citation | DOI / URL | Availability | Reading coverage | Record | Gaps); the new rows keep that shape.

## 4. literature/CORPUS.md — new rows (append to the P-series / padua-literature block)

```
| faghih-vanbarel-vanbuggenhout-vandebril-2025-sorf | A. Faghih, M. Van Barel, N. Van Buggenhout, R. Vandebril, Constructing Sobolev orthonormal rational functions via an updating procedure, Numer. Algorithms 100(4) (2025) 1837–1865 | https://doi.org/10.1007/s11075-025-02149-y ; https://arxiv.org/abs/2503.13711 | arXiv (open) | abstract, headings, §4.2 opening, conclusion (P4 2026-11-03) | [record](records/faghih-vanbarel-vanbuggenhout-vandebril-2025-sorf.md) | method sections; journal version |
| faghih-vanbarel-vanbuggenhout-vandebril-2025-nla | A. Faghih, M. Van Barel, N. Van Buggenhout, R. Vandebril, A Rational Arnoldi Approach for Sobolev Rational Least Squares Problems, Numer. Linear Algebra Appl. 32(2) (2025) e70017 | https://doi.org/10.1002/nla.70017 ; probable preprint https://arxiv.org/abs/2407.05945 | arXiv (open) | preprint abstract + conclusion; journal abstract via Crossref (P4 2026-11-03) | [record](records/faghih-vanbarel-vanbuggenhout-vandebril-2025-nla.md) | journal full text; preprint identity unconfirmed |
| laudadio-mastronardi-vanassche-vandooren-2024 | T. Laudadio, N. Mastronardi, W. Van Assche, P. Van Dooren, A Matlab package computing simultaneous Gaussian quadrature rules for multiple orthogonal polynomials, J. Comput. Appl. Math. 451 (2024) 116109 | https://doi.org/10.1016/j.cam.2024.116109 ; https://arxiv.org/abs/2406.11269 | arXiv (open) | arXiv v1 exact pages (P4 2026-11-03) | [record](records/laudadio-mastronardi-vanassche-vandooren-2024.md) | §§3–6; journal version |
| laudadio-mastronardi-vandooren-2025 | T. Laudadio, N. Mastronardi, P. Van Dooren, Computational aspects of simultaneous Gaussian quadrature, Numer. Algorithms 100(2) (2025) 621–643 | https://doi.org/10.1007/s11075-024-01785-0 | open access (Springer PDF) | exact pages (P4 2026-11-03) | [record](records/laudadio-mastronardi-vandooren-2025.md) | §5 Theorem 2 and backward-stability argument; §6; §8 |
| rinelli-vandebril-2026 | M. Rinelli, R. Vandebril, Block Krylov subspaces and orthogonal matrix polynomials: a structural correspondence with applications to unitary matrices, arXiv:2605.16954v1 (2026) | https://arxiv.org/abs/2605.16954 | arXiv (open) | abstract, introduction, conclusion (P4 2026-11-03) | [record](records/rinelli-vandebril-2026.md) | body |
| vermeiren-2026 | R. Vermeiren, Constructing Orthogonal Rational Function Vectors with an application in Rational Approximation, arXiv:2601.11317v2 (2026) | https://arxiv.org/abs/2601.11317 | arXiv (open) | abstract, introduction, conclusion (P4 2026-11-03) | [record](records/vermeiren-2026.md) | §3 updating algorithm |
```

## 5. New record files (copy from P4 scratch)

- `literature/records/vanbarel-vanbuggenhout-vandebril-2023.md`
- `literature/records/faghih-vanbarel-vanbuggenhout-vandebril-2025-sorf.md`
- `literature/records/faghih-vanbarel-vanbuggenhout-vandebril-2025-nla.md`
- `literature/records/laudadio-mastronardi-vanassche-vandooren-2024.md`
- `literature/records/laudadio-mastronardi-vandooren-2025.md`
- `literature/records/filipuk-haneczok-vanassche-2015.md`
- `literature/records/rinelli-vandebril-2026.md`
- `literature/records/vermeiren-2026.md`

## 6. Existing record files — edits

### literature/records/faghih-et-al-2025.md

Old (line 1):

```
# faghih-et-al-2025 — Faghih, Rinelli, Van Barel, Vandebril, Vermeiren, Krylov vs core-transformation IEPs for MOPs, arXiv:2506.19796; title not given in inputs
```

New:

```
# faghih-et-al-2025 — Faghih, Rinelli, Van Barel, Vandebril, Vermeiren, Krylov and Core Transformation Algorithms for an Inverse Eigenvalue Problem to Compute Recurrences of Multiple Orthogonal Polynomials, SIAM J. Numer. Anal. 64(4) (2026) 1190–1216 (arXiv:2506.19796)
```

Old (line 5):

```
- Reading coverage: supplied secondary account only (see reports/Padua points research since 2010.md Leuven section; notes/recent_multivariate_NLA.md §1 item 6); original fulltext NOT inspected.
```

New:

```
- Reading coverage: published PDF read 2026-11-03 (topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md): §1, §3.2, §4.2–4.4, §5 opening + Alg. 5.1, §6.2–6.3, §7, references. Earlier: supplied secondary account only.
```

In `### LIT-119 …`: replace the Verification, Statement and Page lines by the new LIT-119 row content above (backward stable for most N < 25 for IEP_CORE **and** IEP_KRYLREORTH(full); Laurie wording; locators Alg. 4.1 p. 1199, Alg. 5.1 p. 1205, §6.2 p. 1211, §7 p. 1213). Append to `## History`:

```
2026-11-03: fulltext corrections (padua-literature-20261103 P4, from the assessment note): stability statement covers IEP_CORE and IEP_KRYLREORTH(full); Laurie sentence reworded; journal citation, locators and code URL added.
```

### literature/records/faghih-vanbarel-vandebril-2026.md

Old (line 1):

```
# faghih-vanbarel-vandebril-2026 — Faghih, Van Barel, Vandebril, MOP updating/downdating by deflation, arXiv:2608.25758 (27 Aug 2026); title not given in inputs
```

New:

```
# faghih-vanbarel-vandebril-2026 — Faghih, Van Barel, Vandebril, Updating and Downdating the Recurrences of Discrete Multiple Orthogonal Polynomials on the Real Line, arXiv:2608.25758v1 (26 Aug 2026)
```

Old (line 5):

```
- Reading coverage: supplied secondary account only (see notes/verify_algorithmic_problems.md Problem 1(g); notes/recent_multivariate_NLA.md §1 item 6, R3, R4; reports/Open problems verification.md §3 C); original fulltext NOT inspected.
```

New:

```
- Reading coverage: complete full text, arXiv v1 PDF pp. 1–26, read 2026-11-03 (padua-literature-20261103 P4, claude-opus-5-5 high). Earlier: supplied secondary account only.
```

In `### LIT-117 …` and `### LIT-118 …`: set Verification to VERIFIED-fulltext and replace Statement/Page with the new INDEX rows above. Append the five `### LIT?padua-literature-claude-70…74` sections and the "Search and attribution notes" bullets from `records/faghih-vanbarel-vandebril-2026.addendum.md`. Append to `## History`:

```
2026-11-03: full text read (padua-literature-20261103 P4); LIT-117/118 verified and corrected (LIT-118 ill-conditioning clause is Introduction p. 3); statements LIT?padua-literature-claude-70–74 added.
```

## 7. Cross-topic pointers (no edit here; for PR preparation)

- IDEA?bivariate-lanczos-claude-041 (deferred, coordinate with Leuven): the source's stated future work (LIT?…-74; SINUM §7) still lists nearest-neighbour recurrences as open. No change to the IDEA status; P4 registers nothing.
- Bivariate Lanczos / V+A briefs: cite LIT-347 (corrected) and LIT?…-71/72 as 1-D comparators, as proposed in the assessment note.


## P2 (from the P2 reader, Claude Opus 5.5 high; integrated by the orchestrator)

Addenda for existing records are under [addenda/](addenda/).


Claude, Opus 5.5, high, 2026-11-03, rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`. To be applied by the orchestrator at PR preparation only. Provisional IDs `LIT?padua-literature-claude-20…24` get final IDs from the topic's reserved range. Old strings below are copied from the files at `af1ac9f`.

## 1. literature/INDEX.md — existing rows

### LIT-014 (line 20)

Old:
```
| LIT-014 | reported / UNVERIFIED | Multidimensional Lissajous–Chebyshev interpolation/discrete orthogonality is relevant predecessor; characteristic transfer is an unverified proposed derivation. | dencker-erb-2017 | exact theorem pending | [record](records/dencker-erb-2017.md) | supplied secondary account only; original fulltext NOT inspected |
```
New:
```
| LIT-014 | LITERATURE / primary reading (2026-11-03) | Dencker–Erb JAT 219 (2017): discrete Chebyshev orthogonality on Lissajous–Chebyshev nodes (Prop. 2.5, Thm 2.7), interpolation (Thm 2.8) and positive Chebyshev quadrature (Thm 2.10); Padua case n=(m,m+1). The 2026-10-31 "characteristic transfer" remains an unverified proposed derivation. | dencker-erb-2017 | journal pp. 23–34: (2.1), (2.4), (2.12)–(2.14), (2.19), (2.25), (2.32), (2.36); Prop 2.5 p. 28, Thm 2.7 p. 30, Thm 2.8 p. 32, Thm 2.10 p. 34 | [record](records/dencker-erb-2017.md) | journal §§2.1–2.3 read from AC-supplied PDF and compared with arXiv v2 (identical on inspected items); other sections not read |
```

### LIT-046 (line 57)

Old:
```
| LIT-046 | source statement / discovery | explicitly conditional CC application; exact hypotheses and limitations in record | mz-an-wu-2022 | record-specific locator | [mz-an-wu-2022.md](records/mz-an-wu-2022.md) | selected text, abstract, metadata or UNVERIFIED as individually labeled; no blanket fulltext claim |
```
New:
```
| LIT-046 | source statement / discovery | explicitly conditional CC application; exact hypotheses and limitations in record; 2026-11-03 screen: no Padua, square or 2-D Chebyshev-type MZ statement in published or arXiv v3 text | mz-an-wu-2022 | record-specific locator | [mz-an-wu-2022.md](records/mz-an-wu-2022.md) | selected text, abstract, metadata or UNVERIFIED as individually labeled; no blanket fulltext claim |
```

### LIT-058 (line 69)

Old:
```
| LIT-058 | source statement / discovery | PDE-method ancestor, unresolved norm comparison; exact hypotheses and limitations in record | mz-don-gottlieb-1994 | record-specific locator | [mz-don-gottlieb-1994.md](records/mz-don-gottlieb-1994.md) | selected text, abstract, metadata or UNVERIFIED as individually labeled; no blanket fulltext claim |
```
New:
```
| LIT-058 | source statement / discovery | PDE-method ancestor: L² stability via GLL ghost points; nodal form = pull-back of discrete GLL energy; no norm-equivalence constants | mz-don-gottlieb-1994 | journal Thm 3.1.1 p. 1524, Thm 3.1.2 pp. 1524–1525, Lemma 4.1/Thm 4.1 pp. 1528–1529 | [mz-don-gottlieb-1994.md](records/mz-don-gottlieb-1994.md) | ICASE 93-40 report and journal (AC-supplied, OCR) read; identical on items used |
```

### LIT-294 (line 92)

Old:
```
| LIT-294 | converse MZ, Jacobi nodes | König–Nielsen: same-weight Jacobi node/Christoffel/measure characterization, p in (μ,M); log growth of test norms at p=M | mz-prior-art-2026-additions | Thm 1 (arXiv math/9208201) | [record](records/mz-prior-art-2026-additions.md) | arXiv v1 via extraction; journal version not compared |
```
New:
```
| LIT-294 | converse MZ, Jacobi nodes | König–Nielsen: same-weight Jacobi node/Christoffel/measure characterization, p in (μ,M), M=4(a+1)/(2a+1) for a=max(α,β)>−1/2 and M=∞ otherwise; log growth of test norms at p=M; Remark (1): degree ≤ n/2 holds for all p | mz-prior-art-2026-additions | Thm 1 arXiv v1 pp. 3–4; (18)–(19) p. 15; Remark (1) p. 16 | [record](records/mz-prior-art-2026-additions.md) | arXiv v1 read directly 2026-11-03; journal: only p. 183 preview (matches); journal body unlicensed, not compared |
```

### LIT-427 (line 499)

Old:
```
| LIT-427 | LITERATURE / selected primary reading | Sommariva–Vianello–Zanovello, Nontensorial Clenshaw–Curtis cubature, Numer.Algorithms49 (2008),409–427 | Campaign primary record | Exact equations/pages in source record | [record](records/mz2d-sommariva-vianello-zanovello-2008.md) | Selected author-text reading; named final-version gaps remain |
```
New:
```
| LIT-427 | LITERATURE / primary reading (journal, 2026-11-03) | Sommariva–Vianello–Zanovello, Nontensorial Clenshaw–Curtis cubature, Numer.Algorithms49 (2008),409–427: signed interpolatory Padua rule (33)/(36), exactness n, Σ|λ|→4 (Thm 1; asserted for λ*), negative weights p. 421 / Table 1; eq. (25) misprints the denominator in preprint and journal | Campaign primary record | journal pp. 413 (Thm 1), 415 ((16)–(19)), 417 ((24)–(25)), 418–420 ((26)–(36)), 421 (Table 1) | [record](records/mz2d-sommariva-vianello-zanovello-2008.md) | journal pp. 409–421 read, 422–427 screened |
```

## 2. literature/INDEX.md — new rows (append to the topic's section)

```
| LIT?padua-literature-claude-20 | LITERATURE / primary reading (arXiv) | Kolomoitsev–Lomako–Prestin JAT 229 (2018): two-sided L^p MZ at Lissajous–Chebyshev/Padua nodes, positive Chebyshev weights, Chebyshev-weighted L^p, unspecified constants (Lemma 5.1, from Erb 2016); L^p interpolation error bounds (Thms 4.1–4.5) | kolomoitsev-lomako-prestin-2018 | arXiv v1 Lemma 5.1 p. 11; Thms 4.1–4.5 pp. 7–11 | [record](records/kolomoitsev-lomako-prestin-2018.md) | arXiv v1 pp. 1–12, 16, 19; journal not read |
| LIT?padua-literature-claude-21 | LITERATURE / complete reading | Wu AML 182 (2026) 110033: MZ condition ⇒ discrete Riesz map spectral equivalence and Galerkin stability with error ∝ MZ defect; no CC/Padua example | wu-aml-2026 | Prop 2.1, Lemma 2.1 p. 2; Thm 3.1 p. 3; Cor 3.1 p. 4 | [record](records/wu-aml-2026.md) | complete (AC-supplied PDF) |
| LIT?padua-literature-claude-22 | LITERATURE / screen | An–Ran–Wu survey, DRNA 18(1) (2025) 135–145: no MZ statement for Padua/square/Chebyshev rules; calls Padua-set hyperinterpolation open (positive-weight sense); multivariate MZ "relatively limited" | an-ran-wu-2025 | arXiv v1 §2.3 pp. 3–4, §3.1 p. 5 | [record](records/an-ran-wu-2025.md) | arXiv v1 keyword screen + sections; journal body not read |
| LIT?padua-literature-claude-23 | LITERATURE / selected reading | De Marchi–Kroó, Acta Math. Hungar. 154 (2018) 69–89: MZ meshes on multivariate domains with unspecified oversampling/constants; explicit 1-D CGL Lemma 1 (constants 2/3, 2) only for m ≥ 18pk+1 | demarchi-kroo-2018 | Lemma 1 pp. 72–73; Thm 1 p. 73; Thm 2 p. 77; Remark pp. 88–89 | [record](records/demarchi-kroo-2018.md) | journal pp. 69–75 + screened statements |
| LIT?padua-literature-claude-24 | LITERATURE / selected reading | Wu arXiv 2411.16584v3: MZ for scattered data on triangles/polygons (positive triangulation weights, mesh-controlled degree) | wu-polygons-2024 | Thms 3.1–3.6 pp. 4–11 | [record](records/wu-polygons-2024.md) | abstract + theorem statements |
```

## 3. literature/CORPUS.md

### dencker-erb-2017 (line 20)

Old:
```
| dencker-erb-2017 | Dencker–Erb, Multivariate polynomial interpolation on Lissajous–Chebyshev nodes, JAT (2017) | https://arxiv.org/abs/1511.04564 | supplied account; fulltext pending | supplied secondary account only; original fulltext NOT inspected | [record](records/dencker-erb-2017.md) | original fulltext/hypotheses |
```
New:
```
| dencker-erb-2017 | Dencker–Erb, Multivariate polynomial interpolation on Lissajous–Chebyshev nodes, JAT 219 (2017) 15–45 | https://doi.org/10.1016/j.jat.2017.03.003 ; https://arxiv.org/abs/1511.04564 | journal PDF supplied by AC (Downloads\padua\papers); arXiv v2 open | journal §§2.1–2.3 (pp. 23–34) read and compared with arXiv v2 | [record](records/dencker-erb-2017.md) | §§1, 3 not read |
```

### mz-don-gottlieb-1994 (line 58)

Old:
```
| mz-don-gottlieb-1994 | mz-don-gottlieb-1994 — Chebyshev–Legendre method | https://doi.org/10.1137/0731079 | see exact per-statement coverage | [mz-don-gottlieb-1994.md](records/mz-don-gottlieb-1994.md) | named gaps retained in record; historical fulltexts may be pending-reference |
```
New:
```
| mz-don-gottlieb-1994 | mz-don-gottlieb-1994 — Chebyshev–Legendre method | https://doi.org/10.1137/0731079 | see exact per-statement coverage; journal PDF supplied by AC 2026-11-03 | [mz-don-gottlieb-1994.md](records/mz-don-gottlieb-1994.md) | journal-vs-report gap closed 2026-11-03 (OCR text; formulas not image-checked) |
```

### mz-prior-art-2026-additions (line 65) — gaps column only

Old (end of row):
```
| König–Nielsen journal version; Hadronic Press 2000 Mastroianni–Russo (Xu I/II read later, LIT-296; Mastroianni–Milovanović–Notarangelo 2012 added as LIT-299, https://doi.org/10.2298/PIM1205163M) |
```
New:
```
| König–Nielsen journal body (De Gruyter "Unlicensed" 2026-11-03; only p. 183 preview read; https://doi.org/10.1515/form.1994.6.183); Hadronic Press 2000 Mastroianni–Russo (Xu I/II read later, LIT-296; Mastroianni–Milovanović–Notarangelo 2012 added as LIT-299, https://doi.org/10.2298/PIM1205163M) |
```

### New CORPUS rows

```
| kolomoitsev-lomako-prestin-2018 | Kolomoitsev–Lomako–Prestin, On L_p-error of bivariate polynomial interpolation on the square, JAT 229 (2018) 13–35 | https://doi.org/10.1016/j.jat.2018.02.005 ; https://arxiv.org/abs/1712.06075 | arXiv v1 open | arXiv pp. 1–12, 16, 19 | [record](records/kolomoitsev-lomako-prestin-2018.md) | journal body; arXiv pp. 13–15, 17–18 |
| wu-aml-2026 | H.-N. Wu, Marcinkiewicz–Zygmund stability of quadrature-based Galerkin schemes, Appl. Math. Lett. 182 (2026) 110033 | https://doi.org/10.1016/j.aml.2026.110033 | publisher PDF supplied by AC | complete | [record](records/wu-aml-2026.md) | none |
| an-ran-wu-2025 | An–Ran–Wu, The path of hyperinterpolation: a survey, Dolomites Res. Notes Approx. 18(1) (2025) 135–145 | https://doi.org/10.25430/pupj-DRNA-2025-1-11 ; https://arxiv.org/abs/2510.04904 | arXiv v1 open | keyword screen + §§2.3, 3.1–3.2 | [record](records/an-ran-wu-2025.md) | journal body; full read |
| demarchi-kroo-2018 | De Marchi–Kroó, Marcinkiewicz–Zygmund type results in multivariate domains, Acta Math. Hungar. 154 (2018) 69–89 | https://doi.org/10.1007/s10474-017-0769-4 | publisher PDF via institutional access (browser) | pp. 69–75 + screened statements | [record](records/demarchi-kroo-2018.md) | proofs pp. 76–88 |
| wu-polygons-2024 | H.-N. Wu, Marcinkiewicz–Zygmund inequalities for scattered data on polygons, arXiv 2411.16584v3 (2024); no journal DOI known | https://arxiv.org/abs/2411.16584 | arXiv open | abstract + theorem statements | [record](records/wu-polygons-2024.md) | proofs, numerics, publication status |
```

## 4. Existing records — append sections

- `literature/records/mz2d-sommariva-vianello-zanovello-2008.md`: replace the paragraph beginning "**Preprint-specific discrepancy:**" by the "New" text in `records/mz2d-sommariva-vianello-zanovello-2008.addendum.md` §"Old → new corrections"; replace "Publisher access was subscription-preview only." accordingly; append the whole addendum as a dated section "## 2026-11-03 journal-body reading (topic padua-literature-20261103)"; History line: "2026-11-03: journal body read; (25) misprint confirmed in journal; locators added."
- `literature/records/mz-prior-art-2026-additions.md`, LIT-294 section: apply the three Old→New replacements listed in `records/mz-prior-art-2026-additions.addendum.md` and append it as a dated subsection.
- `literature/records/mz-don-gottlieb-1994.md`: append `records/mz-don-gottlieb-1994.addendum.md` as "## 2026-11-03 journal-version comparison".
- `literature/records/dencker-erb-2017.md`: change header "Reading coverage: supplied secondary account only; original fulltext NOT inspected." to "Reading coverage: 2026-10-31 supplied secondary account; 2026-11-03 journal §§2.1–2.3 read (see dated section)."; append `records/dencker-erb-2017.addendum.md`.
- `literature/records/mz-an-wu-2022.md`: append `records/mz-an-wu-2022.addendum.md`.
- New record files: copy `records/kolomoitsev-lomako-prestin-2018.md`, `wu-aml-2026.md`, `an-ran-wu-2025.md`, `demarchi-kroo-2018.md`, `wu-polygons-2024.md` into `literature/records/` after final-ID substitution.

## 5. Merged topic files (historical; add dated notes, do not rewrite)

- `topics/padua-mz-2d-20261101/literature.md`, LIT-427 section: after the "Preprint-specific discrepancy" paragraph add: "2026-11-03 note (padua-literature-20261103): the journal body (p. 417) prints the same (n+2)(n+3) denominator; the misprint is in both versions. See literature/records/mz2d-sommariva-vianello-zanovello-2008.md." LIT-014 section: add "Journal body compared 2026-11-03: identical to arXiv v2 on the inspected items."
- `topics/padua-mz-2d-20261101/report.md`, "Missing independent final-version comparisons": add a dated note "SVZ, Dencker–Erb journal bodies read 2026-11-03 (padua-literature-20261103); KLP read from arXiv v1; Xu 1996, Kolomoitsev–Lomako 2021 and ASV published bodies remain unread by this P2 reader."
- `topics/mz-prior-art-20261101/comparison.md`, row "Forward citations 2010–2026": add a dated note "Wu, Appl. Math. Lett. 182 (2026) 110033 read in full 2026-11-03: abstract MZ ⇒ Galerkin stability, no CC constants; verdict unchanged."; row "König–Nielsen": add "parameter restriction confirmed from arXiv pp. 3, 15; journal body not accessible (unlicensed) 2026-11-03."; row "Don–Gottlieb": add "journal version compared 2026-11-03: identical on items used."

## 6. Link-table corrections (p2-links.md / DOWNLOADS.md)

- Row 4a: the publisher page title is "Vector-valued Lp-convergence …" (hyphen), as is the arXiv PDF title; the arXiv abs page has a journal-ref "Forum Math. 6 (1994), 183-207", which confirms the page range. Access status: De Gruyter "Unlicensed" in AC's browser on 2026-11-03 → keep on AC's list.
- Row 6b: arXiv 1511.04564v2 does carry a journal reference to J. Approx. Theory 219 (2017) (abs page, 2026-11-03); the "no journal-ref" note is wrong. Journal now read (AC-supplied).
- Row 6a, 6f, 3, 4b: status "read" (journal for 6a, 3, 4b; arXiv v1 for 6f).
- Row 8.3: published version is Dolomites Res. Notes Approx. 18(1) (2025) 135–145, DOI 10.25430/pupj-DRNA-2025-1-11 (doi.org resolves to the DRNA page with matching metadata).
- New leads: De Marchi–Kroó 2018 (DOI 10.1007/s10474-017-0769-4, read in part); Erb, Appl. Math. Comput. 289 (2016) 409–425 (source of the KLP Lemma 5.1 MZ inequalities; DOI not verified; unread).

## P3 (from the P3 reader, Claude Opus 5.5 high; integrated by the orchestrator)

Addenda for existing records are under [addenda/](addenda/).


Prepared by the P3 literature reader (Claude Opus 5.5 high), 2026-11-03, against branch head `af1ac9fde6b23cb9cd826a33d5611680566c52cb`. These are literal old→new blocks for shared files. The orchestrator applies them at PR preparation, after allocating final IDs for `LIT?padua-literature-claude-40` … `-67` by the fresh-range procedure. Nothing here changes a PD status.

Files in `p3/records/`: one new record (`xu-sima-1993.md`) and eleven addenda (`<key>.addendum.md`). Each addendum is meant to be appended to `literature/records/<key>.md` as a section "## Addendum — padua-literature-20261103 (P3, 2026-11-03)", followed by one History line. Alternatively it can be kept as a separate topic-owned file linked from the record.

## 1. literature/records — appends

| Target record | Append | History line to add |
|---|---|---|
| simonova-tichy-2025.md | `p3/records/simonova-tichy-2025.addendum.md` (statements 44–47) | 2026-11-03: P3 addendum; arXiv v1 pp. 1–5, 10–20, 23–26 read; LIT-081/082/234/235 upgraded. |
| zhu-nakatsukasa-2026.md | `zhu-nakatsukasa-2026.addendum.md` (48–50) | 2026-11-03: P3 addendum; arXiv v2 read; LIT-090 verified (Rem. 5.1(5) p. 20), the 2026-11-01 "not in v2" annotation withdrawn; LIT-284 locators corrected for v2; LIT-361 verified. |
| hokanson-2020.md | `hokanson-2020.addendum.md` (51–52) | 2026-11-03: P3 addendum; arXiv v1 pp. 1–7, 11–12 read; LIT-098/280/281/360 verified. |
| brubeck-nakatsukasa-trefethen-2021.md | `brubeck-nakatsukasa-trefethen-2021.addendum.md` (53) | 2026-11-03: P3 addendum; LIT-099/285 verified (p. 5, arXiv v1). |
| liu-narayan-2023.md | `liu-narayan-2023.addendum.md` (54–56) | 2026-11-03: P3 addendum; LIT-096 and LIT-362 corrected (d = 3 solved directly; source of non-convexity). |
| greenbaum-1989.md | `greenbaum-1989.addendum.md` (57–59) | 2026-11-03: P3 addendum; AC copy read; LIT-213 conflict resolved (Theorem 1′ has √ε and ε^{1/4} branches). |
| paige-1980-lanczos.md | `paige-1980-lanczos.addendum.md` (60–61) | 2026-11-03: P3 addendum; AC copy read; LIT-069/209 verified, LIT-210 corrected. |
| paige-2010-augmented.md | `paige-2010-augmented.addendum.md` (62) | 2026-11-03: P3 addendum; LIT-254 verified on the author PDF. |
| meurant-strakos-2006.md | `meurant-strakos-2006.addendum.md` (63) | 2026-11-03: P3 addendum; LIT-272 verified, pp. 510–512. |
| sinha-2026.md | `sinha-2026.addendum.md` (64–65) | 2026-11-03: P3 addendum; Theorems 6–8 statements read; LIT-083 verified. |
| chen-2026.md | `chen-2026.addendum.md` (66–67) | 2026-11-03: P3 addendum; arXiv **v2** (18 Oct 2026) read; LIT-289 renumbered (Thm 5.7 in v2). |
| (new) xu-sima-1993.md | `p3/records/xu-sima-1993.md` (40–43) | new record |
| austin-et-al-2021.md | Add to Search and attribution notes: "2026-11-03 (P3): Hokanson arXiv 2009.10803v1, reference [2] (p. 11), cites this work as A. P. Austin, M. Krishnamoorthy, S. Leyffer, S. Mrenna, J. Müller, H. Schulz, *Multivariate rational approximation*, 2019, arXiv:1912.02272v1, and credits the multivariate V+A to its Subsec. 3.2 (pp. 4–5). This bibliographic evidence links the arXiv number to the CPC paper; the arXiv metadata page itself was not verified." | 2026-11-03: P3 attribution note. |
| zhu-nakatsukasa-2026.md, History | Old: `2026-11-01: orchestrator annotation — the L2 developer (response-recon-01, finding F9) reports that the sentence quoted for LIT?bivariate-lanczos-claude-025 was not found in arXiv v2 of this paper;` → New: keep the line unchanged as history and add below it: `2026-11-03 (P3): the sentence IS in arXiv v2, Remark 5.1 item 5, p. 20 (pdf.js text read); finding F9's "not found" is withdrawn for v2.` | — |

No addendum is proposed for `xu-tams-1994-operator` or `xu-tams-1994-blockjacobi`: both AMS PDFs returned a bot-verification page on 2026-11-03, so they were not read, and the records stay at digest level.

## 2. literature/INDEX.md — row replacements (old → new)

Each block replaces one existing row, and the old row text is literal. Only the status-type, statement, locator and coverage cells change. Every coverage change is an append that starts with "· P3 2026-11-03:", so the history stays readable.

### INDEX.md — LIT-069

Old:

```
| LIT-069 (LIT?bivariate-lanczos-claude-004) | reported / UNVERIFIED / mechanism of loss of orthogonality (as characterised by the inputs) | As characterised by the supplying agent: in finite precision, loss of orthogonality of Lanczos vectors occurs in the direction of converged Ritz vectors; the component of q_k along a Ritz vector is bounded by roughly u*\|\|A\|\| divided by the Ritz residual, via Paige's perturbed local relations and the identity relating the strictly upper part of Q^T Q to the section T. | paige-1980-lanczos | no theorem number supplied | [record](records/paige-1980-lanczos.md) | supplied secondary account only; original fulltext NOT inspected Online pass 2026-10-31: form supported by three secondary accounts (see 205); Paige original not read. |
```

New:

```
| LIT-069 (LIT?bivariate-lanczos-claude-004) | reported → verified on the original (P3 2026-11-03) / mechanism of loss of orthogonality | As characterised by the supplying agent: in finite precision, loss of orthogonality of Lanczos vectors occurs in the direction of converged Ritz vectors; the component of q_k along a Ritz vector is bounded by roughly u*\|\|A\|\| divided by the Ritz residual, via Paige's perturbed local relations and the identity relating the strictly upper part of Q^T Q to the section T. | paige-1980-lanczos | Paige 1980 (2.17)–(2.18) p. 239; (3.11)–(3.13) p. 241 | [record](records/paige-1980-lanczos.md) | supplied secondary account only; original fulltext NOT inspected Online pass 2026-10-31: form supported by three secondary accounts (see 205); Paige original not read. · P3 2026-11-03: verified against AC's copy of the original (pp. 238–239, 241); see `p3` addendum to paige-1980-lanczos, LIT?padua-literature-claude-60. |
```

### INDEX.md — LIT-071

Old:

```
| LIT-071 (LIT?bivariate-lanczos-claude-006) | reported / UNVERIFIED / backward-stability model (indirect) | Greenbaum's 1989 model: finite-precision Lanczos results are exact Lanczos results for a slightly larger matrix whose eigenvalues lie close to those of the original (indirect description from the Simonova-Tichy abstract page). | greenbaum-1989 | no theorem number obtained | [record](records/greenbaum-1989.md) | supplied secondary account only; original fulltext NOT inspected Online pass 2026-10-31: Greenbaum LAA 113 metadata and abstract confirmed on ScienceDirect (see 207-209). |
```

New:

```
| LIT-071 (LIT?bivariate-lanczos-claude-006) | reported / UNVERIFIED / backward-stability model (indirect) | Greenbaum's 1989 model: finite-precision Lanczos results are exact Lanczos results for a slightly larger matrix whose eigenvalues lie close to those of the original (indirect description from the Simonova-Tichy abstract page). | greenbaum-1989 | Greenbaum 1989 §4 pp. 20–23; Theorem 1 p. 23 | [record](records/greenbaum-1989.md) | supplied secondary account only; original fulltext NOT inspected Online pass 2026-10-31: Greenbaum LAA 113 metadata and abstract confirmed on ScienceDirect (see 207-209). · P3 2026-11-03: verified against AC's copy of the original (Theorem 1 p. 23, Theorem 1′ p. 51); see greenbaum-1989 addendum, LIT?padua-literature-claude-58. |
```

### INDEX.md — LIT-081

Old:

```
| LIT-081 (LIT?bivariate-lanczos-claude-016) | abstract-checked / Greenbaum-type result for block Lanczos (abstract) | Extends Greenbaum's 1989 model to block Lanczos: a continuation process terminating after finitely many steps gives perturbations such that the computed block tridiagonal matrices are exact block Lanczos for a larger model matrix; sufficient conditions keep the perturbations small. In the single-vector case the conditions can always be met; whether they can always be met in the block case is stated open. | simonova-tichy-2025 | abstract | [record](records/simonova-tichy-2025.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected Online pass 2026-10-31: BIT 65(4) art. 47 confirmed; Theorems 1-4 digested (see 229-230). |
```

New:

```
| LIT-081 (LIT?bivariate-lanczos-claude-016) | abstract-checked / Greenbaum-type result for block Lanczos (abstract) | Extends Greenbaum's 1989 model to block Lanczos: a continuation process terminating after finitely many steps gives perturbations such that the computed block tridiagonal matrices are exact block Lanczos for a larger model matrix; sufficient conditions keep the perturbations small. In the single-vector case the conditions can always be met; whether they can always be met in the block case is stated open. | simonova-tichy-2025 | abstract | [record](records/simonova-tichy-2025.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected Online pass 2026-10-31: BIT 65(4) art. 47 confirmed; Theorems 1-4 digested (see 229-230). · P3 2026-11-03: arXiv v1 PDF text read (pp. 1–5, 10–20, 23–26); statement verified (abstract p. 1; §5 pp. 13–19); see simonova-tichy-2025 addendum, LIT?padua-literature-claude-44/45. |
```

### INDEX.md — LIT-082

Old:

```
| LIT-082 (LIT?bivariate-lanczos-claude-017) | reported / UNVERIFIED / author statements on difficulty and free parameter (reported) | Reported quotations: generalizing Paige's analysis to the block case 'is challenging and requires further research'; a comprehensive finite-precision block Lanczos theory 'is still lacking'; a key open question is how to select the free matrix parameter W_k. | simonova-tichy-2025 | locators not supplied | [record](records/simonova-tichy-2025.md) | supplied secondary account only; original fulltext NOT inspected Online pass 2026-10-31: both phrases located, Sections 1 and 5 (see 231). |
```

New:

```
| LIT-082 (LIT?bivariate-lanczos-claude-017) | reported → page-located (P3 2026-11-03) / author statements on difficulty and free parameter | Reported quotations: generalizing Paige's analysis to the block case 'is challenging and requires further research'; a comprehensive finite-precision block Lanczos theory 'is still lacking'; a key open question is how to select the free matrix parameter W_k. | simonova-tichy-2025 | §1 p. 3; §5 p. 13; §7 p. 24 (arXiv v1) | [record](records/simonova-tichy-2025.md) | supplied secondary account only; original fulltext NOT inspected Online pass 2026-10-31: both phrases located, Sections 1 and 5 (see 231). · P3 2026-11-03: both statements located in the arXiv v1 text (pp. 3, 13); W_k open question p. 24. |
```

### INDEX.md — LIT-083

Old:

```
| LIT-083 (LIT?bivariate-lanczos-claude-018) | abstract-checked / block Paige identity; block Lanczos with truncation (abstract) | The paper includes a block form of Paige's identity, relates its results to the frameworks of Paige and Greenbaum, and analyses block Lanczos with Householder orthogonalization and singular-value truncation. The abstract does not mention several operators. | sinha-2026 | abstract | [record](records/sinha-2026.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected |
```

New:

```
| LIT-083 (LIT?bivariate-lanczos-claude-018) | abstract-checked / block Paige identity; block Lanczos with truncation (abstract) | The paper includes a block form of Paige's identity, relates its results to the frameworks of Paige and Greenbaum, and analyses block Lanczos with Householder orthogonalization and singular-value truncation. The abstract does not mention several operators. | sinha-2026 | abstract | [record](records/sinha-2026.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected · P3 2026-11-03: verified on arXiv v1: abstract p. 1; Theorem 6 (enlarged problem I_k ⊗ A + Δ) p. 39; Theorem 7 (block Paige identities) p. 42; see sinha-2026 addendum, LIT?padua-literature-claude-64/65. |
```

### INDEX.md — LIT-085

Old:

```
| LIT-085 (LIT?bivariate-lanczos-claude-020) | abstract-checked / simplified Paige/Greenbaum-type stability (abstract) | Self-contained analysis of symmetric Lanczos without reorthogonalization: effect of rounding on the three-term recurrence, a known identity for the loss of orthogonality, bounds on where computed Ritz values lie, where stabilized Ritz values cluster, and a Greenbaum-type backward stability theorem; the proofs are said to be simpler than Paige's and Greenbaum's but to hide polynomial factors in the number of iterations. | chen-2026 | abstract | [record](records/chen-2026.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected |
```

New:

```
| LIT-085 (LIT?bivariate-lanczos-claude-020) | abstract-checked / simplified Paige/Greenbaum-type stability (abstract) | Self-contained analysis of symmetric Lanczos without reorthogonalization: effect of rounding on the three-term recurrence, a known identity for the loss of orthogonality, bounds on where computed Ritz values lie, where stabilized Ritz values cluster, and a Greenbaum-type backward stability theorem; the proofs are said to be simpler than Paige's and Greenbaum's but to hide polynomial factors in the number of iterations. | chen-2026 | abstract | [record](records/chen-2026.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected · P3 2026-11-03: abstract confirmed in arXiv v2 (18 Oct 2026), p. 1; main theorems read (Thm 4.1 p. 14, Thm 5.7 pp. 20–21, Thm 5.11 p. 22); see chen-2026 addendum. |
```

### INDEX.md — LIT-089

Old:

```
| LIT-089 (LIT?bivariate-lanczos-claude-024) | abstract-checked / multivariate Vandermonde with Arnoldi (abstract) | Extends Vandermonde with Arnoldi to several dimensions via least squares with Stieltjes orthogonalization using sample points only; about O(N^2) equispaced or O(N^2 log N) random points give a well-conditioned near-optimal approximation on many irregular domains; a weighted variant needs O(N log N) points. | zhu-nakatsukasa-2026 | abstract | [record](records/zhu-nakatsukasa-2026.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected |
```

New:

```
| LIT-089 (LIT?bivariate-lanczos-claude-024) | abstract-checked / multivariate Vandermonde with Arnoldi (abstract) | Extends Vandermonde with Arnoldi to several dimensions via least squares with Stieltjes orthogonalization using sample points only; about O(N^2) equispaced or O(N^2 log N) random points give a well-conditioned near-optimal approximation on many irregular domains; a weighted variant needs O(N log N) points. | zhu-nakatsukasa-2026 | abstract | [record](records/zhu-nakatsukasa-2026.md) | abstract page checked 2026-10-31 only; fulltext NOT inspected · P3 2026-11-03: abstract confirmed in arXiv v2, p. 1. |
```

### INDEX.md — LIT-090

Old:

```
| LIT-090 (LIT?bivariate-lanczos-claude-025) | reported / UNVERIFIED / full orthogonalization and loss of orthogonality (reported) | Reported: the implementation uses full two-pass classical Gram-Schmidt at cost O(M N^2); the authors state multivariate V+A orthogonalization 'is subject to a loss of orthogonality due to numerical cancellation'. The 2024-2026 follow-ups are reported to be applications without truncation or rounding analysis. | zhu-nakatsukasa-2026 | locators not supplied | [record](records/zhu-nakatsukasa-2026.md) | supplied secondary account only; original fulltext NOT inspected |
```

New:

```
| LIT-090 (LIT?bivariate-lanczos-claude-025) | reported → verified against arXiv v2 (P3 2026-11-03) / full orthogonalization and loss of orthogonality | Reported: the implementation uses full two-pass classical Gram-Schmidt at cost O(M N^2); the authors state multivariate V+A orthogonalization 'is subject to a loss of orthogonality due to numerical cancellation'. The 2024-2026 follow-ups are reported to be applications without truncation or rounding analysis. | zhu-nakatsukasa-2026 | Algorithm 3 p. 8; cost p. 21; Remark 5.1(5) pp. 20–21 (arXiv v2) | [record](records/zhu-nakatsukasa-2026.md) | supplied secondary account only; original fulltext NOT inspected · P3 2026-11-03: verified in arXiv v2: two-pass CGS (Alg. 3, p. 8), O(MN²) (p. 21), loss-of-orthogonality-by-cancellation sentence in Remark 5.1(5), p. 20. The 2026-11-01 annotation that the sentence is absent from v2 is withdrawn. Follow-up statement not checked. |
```

### INDEX.md — LIT-096

Old:

```
| LIT-096 (LIT?bivariate-lanczos-claude-031) | reported / UNVERIFIED / any-d truncated Stieltjes from moments; origin of the non-convex step | The multivariate Stieltjes procedure is a truncated block three-term procedure in any dimension working from moments by quadrature, with no complexity analysis, citing neither HL nor the seed. The non-convex (weighted orthogonal Procrustes) step arises from fitting each direction separately (section 5.2.6), not from the canonical form imposed afterwards by one symmetric eigendecomposition (section 3.2). | liu-narayan-2023 | sections 3.2, 5.2.1-5.2.7, eq. 22, eq. 35 | [record](records/liu-narayan-2023.md) | supplied secondary account only; original fulltext NOT inspected |
```

New:

```
| LIT-096 (LIT?bivariate-lanczos-claude-031) | reported / UNVERIFIED / any-d truncated Stieltjes from moments; origin of the non-convex step | The multivariate Stieltjes procedure is a truncated block three-term procedure working from moments (by quadrature or Monte Carlo); no complexity analysis was seen in the pages read. In d = 2 the remaining block is fixed by orthonormality and the commuting conditions need not be imposed. For d > 2 the remaining blocks are determined from the commuting condition (6c), orthonormality and mixed moments, which leaves unitary unknowns in a non-convex generalised weighted orthogonal Procrustes problem (§5.2.6, eqs. (31)–(35)); d = 3 is solved directly (§5.2.7). The canonical form is imposed by one symmetric eigendecomposition per degree (§3.2). [Corrected P3 2026-11-03; original wording: non-convex step 'arises from fitting each direction separately (section 5.2.6)'.] | liu-narayan-2023 | §3.2 p. 6; §5.2.4–5.2.7 pp. 11–13; eqs. (31)–(36) (arXiv v2) | [record](records/liu-narayan-2023.md) | supplied secondary account only; original fulltext NOT inspected · P3 2026-11-03: arXiv v2 read, pp. 1–2, 4–6, 9–13, 19, 21–22; statement corrected as shown; see liu-narayan-2023 addendum, LIT?padua-literature-claude-56. |
```

### INDEX.md — LIT-098

Old:

```
| LIT-098 (LIT?bivariate-lanczos-claude-033) | reported / UNVERIFIED / full-orthogonalization multivariate V+A | Builds each column by multiplying a previous column by one coordinate, orthogonalizes by two-pass classical Gram-Schmidt against ALL previous columns at cost O(M N^2), and notes that many orderings do not satisfy the required span property; reported to be one fixed instance of the seed's ordering scheme. | hokanson-2020 | Alg. 2.1 | [record](records/hokanson-2020.md) | supplied secondary account only; original fulltext NOT inspected |
```

New:

```
| LIT-098 (LIT?bivariate-lanczos-claude-033) | reported / UNVERIFIED / full-orthogonalization multivariate V+A | Builds each column by multiplying a previous column by one coordinate, orthogonalizes by two-pass classical Gram-Schmidt against ALL previous columns at cost O(M N^2), and notes that many orderings do not satisfy the required span property; reported to be one fixed instance of the seed's ordering scheme. | hokanson-2020 | §2 pp. 5–6, Alg. 2.1 (arXiv v1) | [record](records/hokanson-2020.md) | supplied secondary account only; original fulltext NOT inspected · P3 2026-11-03: verified in arXiv v1, pp. 5–6 (the 'instance of the seed's ordering scheme' phrase is the supplier's interpretation, not the paper's). |
```

### INDEX.md — LIT-099

Old:

```
| LIT-099 (LIT?bivariate-lanczos-claude-034) | reported / UNVERIFIED / Arnoldi = Lanczos for real nodes; risk of orthogonality loss | For real nodes the recurrence reduces to three terms (H tridiagonal, Arnoldi equivalent to Lanczos) and there is 'a risk of reduced accuracy' since the columns may lose orthogonality; univariate; cites neither HL nor the seed. | brubeck-nakatsukasa-trefethen-2021 | section 4 | [record](records/brubeck-nakatsukasa-trefethen-2021.md) | supplied secondary account only; original fulltext NOT inspected |
```

New:

```
| LIT-099 (LIT?bivariate-lanczos-claude-034) | reported / UNVERIFIED / Arnoldi = Lanczos for real nodes; risk of orthogonality loss | For real nodes the recurrence reduces to three terms (H tridiagonal, Arnoldi equivalent to Lanczos) and there is 'a risk of reduced accuracy' since the columns may lose orthogonality; univariate; cites neither HL nor the seed. | brubeck-nakatsukasa-trefethen-2021 | §4 p. 5 (arXiv v1) | [record](records/brubeck-nakatsukasa-trefethen-2021.md) | supplied secondary account only; original fulltext NOT inspected · P3 2026-11-03: verified in arXiv v1, p. 5. |
```

### INDEX.md — LIT-209

Old:

```
| LIT-209 (LIT?bivariate-lanczos-claude-205) | online pass / secondary / loss-of-orthogonality mechanism | With Ritz pair (theta_j, y_j = V_k s_j) of T_k and zeta_{kj} the last component of s_j: y_j^T v_{k+1} = -(eps_{jj}) / (eta_{k+1} \|zeta_{kj}\|), where \|eps_{jj}\| <= k eps2 ‖A‖ (a quantity of rounding size). Consequently orthogonality of v_{k+1} to the Krylov basis can be lost only in the directions of Ritz vectors whose last component is small (converged), and not before the first Ritz pair converges. The secondary text adds that loss is not proved to occur in every such direction because the numerator can vanish. | paige-1980-lanczos | Meurant-Strakos Theorem 4.3 (~p. 504), consequence ~p. 508; Paige (2019) Remark 3.2 and 3.4 cite eq. (3.18) of the 1980 paper; Carson-Demmel eqs. (5.9)-(5.11), (5.22). | [record](records/paige-1980-lanczos.md) | metadata + secondary accounts; Original NOT read (author's scan, 80LAIA001.pdf, has no text layer) |
```

New:

```
| LIT-209 (LIT?bivariate-lanczos-claude-205) | online pass / secondary / loss-of-orthogonality mechanism | With Ritz pair (theta_j, y_j = V_k s_j) of T_k and zeta_{kj} the last component of s_j: y_j^T v_{k+1} = -(eps_{jj}) / (eta_{k+1} \|zeta_{kj}\|), where \|eps_{jj}\| <= k eps2 ‖A‖ (a quantity of rounding size). Consequently orthogonality of v_{k+1} to the Krylov basis can be lost only in the directions of Ritz vectors whose last component is small (converged), and not before the first Ritz pair converges. The secondary text adds that loss is not proved to occur in every such direction because the numerator can vanish. | paige-1980-lanczos | Meurant-Strakos Theorem 4.3 (~p. 504), consequence ~p. 508; Paige (2019) Remark 3.2 and 3.4 cite eq. (3.18) of the 1980 paper; Carson-Demmel eqs. (5.9)-(5.11), (5.22). | [record](records/paige-1980-lanczos.md) | metadata + secondary accounts; Original NOT read (author's scan, 80LAIA001.pdf, has no text layer) · P3 2026-11-03: verified on the original, p. 241, (3.11)–(3.13): z_iᵀv_{k+1} = −ε_ii/(β_{k+1}η_{ki}), |ε_ij| ≤ kσε₂ (Paige's notation; σ = ‖A‖₂). |
```

### INDEX.md — LIT-210

Old:

```
| LIT-210 (LIT?bivariate-lanczos-claude-206) | online pass / secondary / accuracy and convergence | Paige 1980 Lemma 3.1: each eigenpair of T_m has an earlier 'stabilized' Ritz value nearby. Theorem 3.1: a stabilized Ritz value (delta <= sqrt(3) m^2 sigma^2 u in the report's notation) lies within (m+1)^3 sigma^2 u of an eigenvalue of A. Corollary 3.1: a stabilized Ritz pair is an exact eigenpair of a matrix within ~5 t^2 sigma^2 u of A (the report has 6 t^2). Theorem 4.1: at least one eigenvalue of T_n is within (n+1)^3 sigma^2 u of an eigenvalue of A. Theorems 4.2-4.3 concern the Krylov-space perturbation and eigenpair results (not detailed in the digest). Assumptions adopted from Paige: computed betas nonzero, m(30 + eps1) <= 1, eps0 < 1/12. Paige (2019, Section 1.1) cites section 8.7 of the 1971 thesis for the growth of Ritz-value error bounds (possibly like k^2 in bounds, proportional to k in practice for well separated eigenvalues). | paige-1980-lanczos | Paige (1980) Lemma 3.1, Theorems 3.1, 4.1-4.3, Corollary 3.1 as cited by Carson-Demmel; Paige (2019) Remark 3.3 cites Theorem 3.1. | [record](records/paige-1980-lanczos.md) | metadata + secondary accounts; Original NOT read |
```

New:

```
| LIT-210 (LIT?bivariate-lanczos-claude-206) | online pass / secondary / accuracy and convergence | Paige 1980 (original read P3 2026-11-03): with σ = ‖A‖₂ and ε₂ = √2 max(6ε₀, ε₁) ((2.10), (2.20)), Lemma 3.1 (p. 245): every eigenpair of T_k has an earlier nearby Ritz value controlled by k²σε₂/|y_jᵀR_ky_j|. Theorem 3.1 (p. 246): if β_{k+1}|η_{kj}| ≤ √3k²σε₂ (stabilized), some eigenvalue of A is within (k+1)³σε₂. Corollary 3.1 (p. 248): the final Ritz pair is an exact eigenpair of a matrix within 5t²σε₂ of A. Theorem 4.1 (p. 250): if n(3ε₀+ε₁) < 1, at least one eigenvalue of T_n is within (n+1)³σε₂ of an eigenvalue of A. Assumptions (2.16): β_{j+1} ≠ 0, k(3ε₀+ε₁) < 1, ε₀ = 2(n+4)ε < 1/12, ε₁ = 2(7+mα)ε. Theorems 4.2–4.3 not read. [Corrected P3 2026-11-03; the earlier secondary wording used 'sigma^2 u', 'm(30 + eps1) <= 1' and '6 t^2'.] | paige-1980-lanczos | Paige (1980) pp. 238–239 (2.10)–(2.21); Lemma 3.1 p. 245; Theorem 3.1 p. 246; Corollary 3.1 p. 248; Theorem 4.1 p. 250 | [record](records/paige-1980-lanczos.md) | metadata + secondary accounts; Original NOT read · P3 2026-11-03: original read (AC copy, page images) for the statements listed; Theorems 4.2–4.3 still unread. |
```

### INDEX.md — LIT-211

Old:

```
| LIT-211 (LIT?bivariate-lanczos-claude-207) | online pass / abstract-checked / backward-stability model | Lanczos and conjugate gradients generate polynomials by a three-term recurrence whose roots give approximate eigenvalues. Under small perturbations (such as rounding) the computed polynomials remain orthogonal, but with respect to a slightly different measure whose weights sit on points very near the eigenvalues of A. This explains the behaviour of Ritz values in perturbed Lanczos and the convergence of perturbed CG. The Chebyshev error bound holds approximately for perturbed CG, and a sharper bound follows from a minimax polynomial over small intervals around the eigenvalues. | greenbaum-1989 | Abstract of LAA 113 (1989) 7-63, February 1989, doi:10.1016/0024-3795(89)90285-1 (page marks the article open archive). | [record](records/greenbaum-1989.md) | metadata + abstract; ScienceDirect open-archive landing page read (metadata and abstract); full text NOT reached |
```

New:

```
| LIT-211 (LIT?bivariate-lanczos-claude-207) | online pass / abstract-checked / backward-stability model | Lanczos and conjugate gradients generate polynomials by a three-term recurrence whose roots give approximate eigenvalues. Under small perturbations (such as rounding) the computed polynomials remain orthogonal, but with respect to a slightly different measure whose weights sit on points very near the eigenvalues of A. This explains the behaviour of Ritz values in perturbed Lanczos and the convergence of perturbed CG. The Chebyshev error bound holds approximately for perturbed CG, and a sharper bound follows from a minimax polynomial over small intervals around the eigenvalues. | greenbaum-1989 | Abstract of LAA 113 (1989) 7-63, February 1989, doi:10.1016/0024-3795(89)90285-1 (page marks the article open archive). | [record](records/greenbaum-1989.md) | metadata + abstract; ScienceDirect open-archive landing page read (metadata and abstract); full text NOT reached · P3 2026-11-03: abstract confirmed on AC's copy (p. 7). |
```

### INDEX.md — LIT-212

Old:

```
| LIT-212 (LIT?bivariate-lanczos-claude-208) | online pass / secondary / theorem form | Fix a step k of finite precision Lanczos on the n x n matrix A with start vector v_1. Greenbaum's construction picks k - m_k mutually orthogonal vectors in the span of the computed vectors that are nearly orthogonal to v_{k+1}, avoiding well-separated converged Ritz directions, and continues the recurrence to length n + m_k - k. The conclusion: T_k equals the matrix generated by exact Lanczos applied to an (n+m_k) x (n+m_k) matrix B whose eigenvalues lie within O((n+m_k)^3 max{u ‖A‖, f_k, ..., f_{n+m_k}}) of eigenvalues of A, where the f_j are the smallest perturbations making some eta_{j+1} vanish by step n+m_k. Strakos (1991, Thm 4.2) is cited for the necessity that B has an eigenvalue near each eigenvalue of A with nonzero weight in v_1. | greenbaum-1989 | Meurant-Strakos, Acta Numerica 15 (2006), Theorem 4.9 (~pp. 511-512); Simonova-Tichy refer to a 'Lemma (Paige)' at Greenbaum p. 32 (see simonova-tichy-2025). | [record](records/greenbaum-1989.md) | secondary account (survey); Original theorem NOT read |
```

New:

```
| LIT-212 (LIT?bivariate-lanczos-claude-208) | online pass / secondary / theorem form | Fix a step k of finite precision Lanczos on the n x n matrix A with start vector v_1. Greenbaum's construction picks k - m_k mutually orthogonal vectors in the span of the computed vectors that are nearly orthogonal to v_{k+1}, avoiding well-separated converged Ritz directions, and continues the recurrence to length n + m_k - k. The conclusion: T_k equals the matrix generated by exact Lanczos applied to an (n+m_k) x (n+m_k) matrix B whose eigenvalues lie within O((n+m_k)^3 max{u ‖A‖, f_k, ..., f_{n+m_k}}) of eigenvalues of A, where the f_j are the smallest perturbations making some eta_{j+1} vanish by step n+m_k. Strakos (1991, Thm 4.2) is cited for the necessity that B has an eigenvalue near each eigenvalue of A with nonzero weight in v_1. | greenbaum-1989 | Meurant-Strakos, Acta Numerica 15 (2006), Theorem 4.9 (~pp. 511-512); Simonova-Tichy refer to a 'Lemma (Paige)' at Greenbaum p. 32 (see simonova-tichy-2025). | [record](records/greenbaum-1989.md) | secondary account (survey); Original theorem NOT read · P3 2026-11-03: original read: Theorem 1, p. 23, (4.7), matches this account (n + m_k = Greenbaum's N + m); the 'k − m_k vectors' description is Meurant–Strakoš's. |
```

### INDEX.md — LIT-213

Old:

```
| LIT-213 (LIT?bivariate-lanczos-claude-209) | online pass / attribution note / unresolved | (a) Simonova-Tichy (arXiv 2507.16484): Greenbaum's proof gives eigenvalue intervals of size about sqrt(u)‖A‖ and experiments suggest u‖A‖ suffices. (b) Chen (arXiv 2608.21268): the bound depends on the fourth root of the accuracy parameter and carries hidden polynomial factors, proofs 'gory'; Chen's own Theorem 4.6 (not Greenbaum's) gives symmetric N x N matrices S and T-tilde with N = nk, T-tilde tridiagonal with leading k x k block exactly the computed T_k, and ‖S - T-tilde‖ of order u‖A‖ up to polynomial factors in k, with starting weights preserved exactly. (c) Meurant-Strakos: cubic polynomial factor times a max of u‖A‖ and the f_j. These are mutually inconsistent as stated, so the exponent of u in Greenbaum's published width cannot be read off the secondary literature. | greenbaum-1989 | Simonova-Tichy Section 1 (as digested); Chen 2608.21268 Section 8, eq. (7.10), Theorem 4.6, Lemmas 4.1-4.5; Meurant-Strakos Theorem 4.9. | [record](records/greenbaum-1989.md) | secondary accounts; UNVERIFIED: three secondary accounts, none the original. |
```

New:

```
| LIT-213 (LIT?bivariate-lanczos-claude-209) | online pass / attribution note / resolved on the original (P3 2026-11-03) | (a) Simonova-Tichy (arXiv 2507.16484): Greenbaum's proof gives eigenvalue intervals of size about sqrt(u)‖A‖ and experiments suggest u‖A‖ suffices. (b) Chen (arXiv 2608.21268): the bound depends on the fourth root of the accuracy parameter and carries hidden polynomial factors, proofs 'gory'; Chen's own Theorem 4.6 (not Greenbaum's) gives symmetric N x N matrices S and T-tilde with N = nk, T-tilde tridiagonal with leading k x k block exactly the computed T_k, and ‖S - T-tilde‖ of order u‖A‖ up to polynomial factors in k, with starting weights preserved exactly. (c) Meurant-Strakos: cubic polynomial factor times a max of u‖A‖ and the f_j. These are mutually inconsistent as stated, so the exponent of u in Greenbaum's published width cannot be read off the secondary literature. RESOLUTION (P3 2026-11-03, original read): Greenbaum's Theorem 1′ (p. 51, (7.31)) has two branches: σ(N+m)³O(J²γ√ε‖A‖) when converged Ritz vectors are defined by (7.9) and the unconverged Ritz values are well separated, and σ(N+m)³O(c_max^{3/2}Jε^{1/4}‖A‖) with (7.10). Account (a) quotes the first branch, (b) the second (citing (7.10)), and (c) the unquantified Theorem 1 (p. 23). Chen's own model is Theorem 5.7 in arXiv v2. | greenbaum-1989 | Simonova-Tichy Section 1 (as digested); Chen 2608.21268 Section 8, eq. (7.10), Theorem 4.6, Lemmas 4.1-4.5; Meurant-Strakos Theorem 4.9. | [record](records/greenbaum-1989.md) | secondary accounts; UNVERIFIED: three secondary accounts, none the original. · P3 2026-11-03: resolved against AC's copy of the original, pp. 23, 43–44, 50–51. |
```

### INDEX.md — LIT-234

Old:

```
| LIT-234 (LIT?bivariate-lanczos-claude-230) | online pass / read / block Greenbaum model | Scalar case: the paper summarizes Greenbaum's 1989 result without numbering it (intervals of size about sqrt(u)‖A‖ from the proof, u‖A‖ suggested by experiments; a 'Lemma (Paige)' at Greenbaum p. 32 is invoked). Block case: Theorem 1: if the perturbations are at most eps2‖A‖ and a Ritz-vector condition holds with some eps1, every eigenvalue of T_N is within 3 max(sqrt(N) eps2, eps1)‖A‖ of an eigenvalue of A; the condition asks that every Ritz pair with a small-norm eigenvector have a nearby Ritz pair of norm at least 0.5. Theorem 2: the continuation vectors q_{k+j} are orthonormal to W_k and to each other and beta_{k+j} = q_{k+j}^T A q_{k+j-1} for j >= 3. Theorem 3: the continuation can be written as a perturbed three-term recurrence (21). Theorem 4: the perturbations are expressed through W_k with rho_k = ‖R_k^{-1}‖; if the Ritz vectors are sufficiently independent (rho_k = O(1)) two terms (35) and one term (36) dominate, and their smallness is the sufficient condition. W_k is the only free parameter, the Q-factor of a QR factorization of m selected Ritz vectors chosen by a heuristic criterion delta_{k,i} > mu‖A‖ (Section 6.1). The abstract says the conditions are always satisfiable in the single-vector case (Greenbaum, based on Paige); Section 5.2 says bounding the second term in (35) in the block case 'remains open'. | simonova-tichy-2025 | Theorems 1-4; Section 5.2; Section 6.1 (digest; abstract also gives the open question). | [record](records/simonova-tichy-2025.md) | full text (tool digest); arXiv 2507.16484 (PDF) read via tool digest; proofs and the sufficiency conditions in detail NOT checked |
```

New:

```
| LIT-234 (LIT?bivariate-lanczos-claude-230) | online pass / read / block Greenbaum model | Scalar case: the paper summarizes Greenbaum's 1989 result without numbering it (intervals of size about sqrt(u)‖A‖ from the proof, u‖A‖ suggested by experiments; a 'Lemma (Paige)' at Greenbaum p. 32 is invoked). Block case: Theorem 1: if the perturbations are at most eps2‖A‖ and a Ritz-vector condition holds with some eps1, every eigenvalue of T_N is within 3 max(sqrt(N) eps2, eps1)‖A‖ of an eigenvalue of A; the condition asks that every Ritz pair with a small-norm eigenvector have a nearby Ritz pair of norm at least 0.5. Theorem 2: the continuation vectors q_{k+j} are orthonormal to W_k and to each other and beta_{k+j} = q_{k+j}^T A q_{k+j-1} for j >= 3. Theorem 3: the continuation can be written as a perturbed three-term recurrence (21). Theorem 4: the perturbations are expressed through W_k with rho_k = ‖R_k^{-1}‖; if the Ritz vectors are sufficiently independent (rho_k = O(1)) two terms (35) and one term (36) dominate, and their smallness is the sufficient condition. W_k is the only free parameter, the Q-factor of a QR factorization of m selected Ritz vectors chosen by a heuristic criterion delta_{k,i} > mu‖A‖ (Section 6.1). The abstract says the conditions are always satisfiable in the single-vector case (Greenbaum, based on Paige); Section 5.2 says bounding the second term in (35) in the block case 'remains open'. | simonova-tichy-2025 | Theorems 1-4; Section 5.2; Section 6.1 (digest; abstract also gives the open question). | [record](records/simonova-tichy-2025.md) | full text (tool digest); arXiv 2507.16484 (PDF) read via tool digest; proofs and the sufficiency conditions in detail NOT checked · P3 2026-11-03: arXiv v1 pdf.js text, pp. 13–20: confirmed; Theorem 4 assumes local bounds (9), (11), (12) that the paper credits to unpublished Carson–Chen work; (21), (35), (36) seen. |
```

### INDEX.md — LIT-254

Old:

```
| LIT-254 (LIT?bivariate-lanczos-claude-411) | PR-prep consolidation 2026-11-01 / WebFetch digest / finite-precision Lanczos computed vectors span a Krylov space of an augmented matrix | Thm 3.1 and Cor. 3.2–3.4: the computed Lanczos vectors span a Krylov space of an augmented matrix built from A. The paper gives no distance from the computed vectors' span to the Krylov space of A itself (explicitly, as digested). Hypotheses: Hermitian A, finite-precision Lanczos without reorthogonalization. | paige-2010-augmented | Thm 3.1, Cor. 3.2–3.4 (as digested). | [record](records/paige-2010-augmented.md) | WebFetch digest of Thm 3.1, Cor. 3.2–3.4; UNVERIFIED |
```

New:

```
| LIT-254 (LIT?bivariate-lanczos-claude-411) | PR-prep consolidation 2026-11-01 / WebFetch digest / finite-precision Lanczos computed vectors span a Krylov space of an augmented matrix | Thm 3.1 and Cor. 3.2–3.4: the computed Lanczos vectors span a Krylov space of an augmented matrix built from A. The paper gives no distance from the computed vectors' span to the Krylov space of A itself (explicitly, as digested). Hypotheses: Hermitian A, finite-precision Lanczos without reorthogonalization. | paige-2010-augmented | Thm 3.1, Cor. 3.2–3.4 (as digested). | [record](records/paige-2010-augmented.md) | WebFetch digest of Thm 3.1, Cor. 3.2–3.4; UNVERIFIED · P3 2026-11-03: verified on the author PDF (Thm 3.1 pp. 2353–2354; Cors 3.2–3.4 pp. 2355–2357); the paper says the result cannot be turned into standard backward stability (p. 2348). |
```

### INDEX.md — LIT-272

Old:

```
| LIT-272 (LIT?bivariate-lanczos-claude-429) | PR-prep consolidation 2026-11-01 / WebFetch digest / Greenbaum's model as stated in the survey: extended matrix B with eigenvalues near those of A, width with unquantified f_j | §4.3, Thm 4.9, p. 511 (as digested): the eigenvalues of the extended matrix B, of order n + m_k, lie within O((n + m_k)^3 max{eps‖A‖, f_k, ..., f_{n+m_k}}) of eigenvalues of A. The f_j are the smallest perturbations that make a recurrence coefficient eta_{j+1} vanish; their size is not quantified in the returned text. Block Lanczos is excluded (p. 476). Hypotheses: Single symmetric A, single start vector. | meurant-strakos-2006 | §4.3, Thm 4.9, p. 511; p. 476 (as digested, text partly garbled). | [record](records/meurant-strakos-2006.md) | WebFetch digest, text partly garbled; UNVERIFIED |
```

New:

```
| LIT-272 (LIT?bivariate-lanczos-claude-429) | PR-prep consolidation 2026-11-01 / WebFetch digest / Greenbaum's model as stated in the survey: extended matrix B with eigenvalues near those of A, width with unquantified f_j | §4.3, Thm 4.9, p. 511 (as digested): the eigenvalues of the extended matrix B, of order n + m_k, lie within O((n + m_k)^3 max{eps‖A‖, f_k, ..., f_{n+m_k}}) of eigenvalues of A. The f_j are the smallest perturbations that make a recurrence coefficient eta_{j+1} vanish; their size is not quantified in the returned text. Block Lanczos is excluded (p. 476). Hypotheses: Single symmetric A, single start vector. | meurant-strakos-2006 | §4.3, Thm 4.9, p. 511; p. 476 (as digested, text partly garbled). | [record](records/meurant-strakos-2006.md) | WebFetch digest, text partly garbled; UNVERIFIED · P3 2026-11-03: verified on the author PDF, pp. 510–512. |
```

### INDEX.md — LIT-280

Old:

```
| LIT-280 (LIT?bivariate-lanczos-claude-437) | PR-prep consolidation 2026-11-01 / WebFetch digest / §2: the multivariate monomial-ordered basis is not a Krylov subspace; Alg. 2.1 orthogonalizes twice against all previous columns | §2 (as digested): the basis no longer corresponds to a Krylov subspace in the multivariate case. Alg. 2.1 builds each column by multiplying a previous column by one coordinate and orthogonalizes by classical Gram–Schmidt twice against all previous columns. Hypotheses: Multivariate Vandermonde-with-Arnoldi inside a rational-approximation iteration. | hokanson-2020 | §2; Alg. 2.1. | [record](records/hokanson-2020.md) | WebFetch digest; UNVERIFIED |
```

New:

```
| LIT-280 (LIT?bivariate-lanczos-claude-437) | PR-prep consolidation 2026-11-01 / WebFetch digest / §2: the multivariate monomial-ordered basis is not a Krylov subspace; Alg. 2.1 orthogonalizes twice against all previous columns | §2 (as digested): the basis no longer corresponds to a Krylov subspace in the multivariate case. Alg. 2.1 builds each column by multiplying a previous column by one coordinate and orthogonalizes by classical Gram–Schmidt twice against all previous columns. Hypotheses: Multivariate Vandermonde-with-Arnoldi inside a rational-approximation iteration. | hokanson-2020 | §2; Alg. 2.1. | [record](records/hokanson-2020.md) | WebFetch digest; UNVERIFIED · P3 2026-11-03: verified in arXiv v1, pp. 5–6. |
```

### INDEX.md — LIT-281

Old:

```
| LIT-281 (LIT?bivariate-lanczos-claude-438) | PR-prep consolidation 2026-11-01 / WebFetch digest / §2.1 selection rule 'smallest k' for the parent column; no rounding-error claims | §2.1, Alg. 2.1 (as digested): the parent of the new column is chosen by the smallest-index rule, the smallest k such that I[k] + e_j = I[l+1]; the text and the algorithm differ (l versus l+1). The text remarks that many orderings do not satisfy this constraint, which concerns the exact-arithmetic span property. The paper makes no claim about rounding error, the accuracy of the recurrence matrices, or the span in floating point. The multivariate extension is credited to Austin et al. (see austin-et-al-2021). Hypotheses: Multi-index ordering I; exact conventions not extracted. | hokanson-2020 | §2.1, Alg. 2.1. | [record](records/hokanson-2020.md) | WebFetch digest; UNVERIFIED |
```

New:

```
| LIT-281 (LIT?bivariate-lanczos-claude-438) | PR-prep consolidation 2026-11-01 / WebFetch digest / §2.1 selection rule 'smallest k' for the parent column; no rounding-error claims | §2.1, Alg. 2.1 (as digested): the parent of the new column is chosen by the smallest-index rule, the smallest k such that I[k] + e_j = I[l+1]; the text and the algorithm differ (l versus l+1). The text remarks that many orderings do not satisfy this constraint, which concerns the exact-arithmetic span property. The paper makes no claim about rounding error, the accuracy of the recurrence matrices, or the span in floating point. The multivariate extension is credited to Austin et al. (see austin-et-al-2021). Hypotheses: Multi-index ordering I; exact conventions not extracted. | hokanson-2020 | §2.1, Alg. 2.1. | [record](records/hokanson-2020.md) | WebFetch digest; UNVERIFIED · P3 2026-11-03: verified in arXiv v1, p. 6 (ℓ vs ℓ+1 inconsistency confirmed; no rounding claims in §2, pp. 5–7). |
```

### INDEX.md — LIT-283

Old:

```
| LIT-283 (LIT?bivariate-lanczos-claude-440) | PR-prep consolidation 2026-11-01 / WebFetch digest / §3: the multivariate monomial basis does not correspond to a Krylov subspace | §3 (as digested): unlike 1D Arnoldi, the multivariate monomial basis does not correspond to a Krylov subspace. Hypotheses: Multivariate V+A on irregular domains. | zhu-nakatsukasa-2026 | §3 (arXiv 2301.12241). | [record](records/zhu-nakatsukasa-2026.md) | WebFetch digest; UNVERIFIED |
```

New:

```
| LIT-283 (LIT?bivariate-lanczos-claude-440) | PR-prep consolidation 2026-11-01 / WebFetch digest / §3: the multivariate monomial basis does not correspond to a Krylov subspace | §3 (as digested): unlike 1D Arnoldi, the multivariate monomial basis does not correspond to a Krylov subspace. Hypotheses: Multivariate V+A on irregular domains. | zhu-nakatsukasa-2026 | §3 (arXiv 2301.12241). | [record](records/zhu-nakatsukasa-2026.md) | WebFetch digest; UNVERIFIED · P3 2026-11-03: verified in arXiv v2, §3 p. 7. |
```

### INDEX.md — LIT-284

Old:

```
| LIT-284 (LIT?bivariate-lanczos-claude-441) | PR-prep consolidation 2026-11-01 / WebFetch digest / rounding content of multivariate V+A: CGS2 orthogonality bound feeding the fit bound; basis accuracy evidence is 1D | No backward-stability or forward-error theorem for multivariate V+A and no analysis of the computed Hessenberg matrices was found. §2 states in exact arithmetic that the discrete orthogonal basis spans the polynomial space (univariate wording). §2.1 and Remark 3 (§5.1) give the CGS2 loss-of-orthogonality bound eps_m = O(M N^{3/2} u) on ‖Q*Q - I‖, citing Higham Thm 19.4 and '[15, Thm 2]'; eps_m enters only the near-optimality (fit) bound. Thm 6 ('stable with high probability') is about sampling, not rounding. §5.2 says the discrete orthogonal polynomials generated by V+A are unaffected by the ill-conditioning of A; the only basis-versus-exact comparisons (phi_30 against scaled Legendre, §2.3.1, Fig. 2 and Fig. 10) are 1D, and the 2D evidence is fit error on tensor and elliptical domains. No triangles or rotated domains appear and commutativity is not discussed. Remark 3 is also reported (L1 review) to say that orthogonalization is subject to a loss of orthogonality due to numerical cancellation. Hypotheses: As digested. | zhu-nakatsukasa-2026 | §2, §2.1, §2.3.1 (Figs 2, 10), Remark 3 (§5.1), Thm 6, §5.2. | [record](records/zhu-nakatsukasa-2026.md) | WebFetch digest, Appendix B not seen; UNVERIFIED |
```

New:

```
| LIT-284 (LIT?bivariate-lanczos-claude-441) | PR-prep consolidation 2026-11-01 / WebFetch digest / rounding content of multivariate V+A: CGS2 orthogonality bound feeding the fit bound; basis accuracy evidence is 1D | No backward-stability or forward-error theorem for multivariate V+A and no analysis of the computed Hessenberg matrices was found. §2 states in exact arithmetic that the discrete orthogonal basis spans the polynomial space (univariate wording). §2.1 and Remark 3 (§5.1) give the CGS2 loss-of-orthogonality bound eps_m = O(M N^{3/2} u) on ‖Q*Q - I‖, citing Higham Thm 19.4 and '[15, Thm 2]'; eps_m enters only the near-optimality (fit) bound. Thm 6 ('stable with high probability') is about sampling, not rounding. §5.2 says the discrete orthogonal polynomials generated by V+A are unaffected by the ill-conditioning of A; the only basis-versus-exact comparisons (phi_30 against scaled Legendre, §2.3.1, Fig. 2 and Fig. 10) are 1D, and the 2D evidence is fit error on tensor and elliptical domains. No triangles or rotated domains appear and commutativity is not discussed. Remark 3 is also reported (L1 review) to say that orthogonalization is subject to a loss of orthogonality due to numerical cancellation. Hypotheses: As digested. | zhu-nakatsukasa-2026 | §2, §2.1, §2.3.1 (Figs 2, 10), Remark 3 (§5.1), Thm 6, §5.2. | [record](records/zhu-nakatsukasa-2026.md) | WebFetch digest, Appendix B not seen; UNVERIFIED · P3 2026-11-03 (arXiv v2): locators for v2: Remark 5.1(5) pp. 20–21 (not 'Remark 3'); probabilistic stability = Theorem 5.1 p. 21 (phrase also p. 2); 1D basis-vs-Legendre comparison = Fig. 13 p. 23 cited in §5.2 p. 22; Giraud et al. citation is [19]. v2 has no appendix (Algorithm 4 p. 8, Algorithm 5 p. 20); the remaining gap is the IMA version of record. Substance confirmed: no statement on the computed span or H in 2D. |
```

### INDEX.md — LIT-285

Old:

```
| LIT-285 (LIT?bivariate-lanczos-claude-442) | PR-prep consolidation 2026-11-01 / WebFetch digest / §4: two-pass variant called an 'extremely stable alternative' (asserted); Lanczos caveat; univariate only | §4 (as digested): the two-pass variant is called an extremely stable alternative, asserted without proof; the Lanczos caveat of the Step 0 statement 034 is confirmed. Accuracy is measured end to end (the fit only). There is no multivariate section; §6 is complex 1D. Hypotheses: Univariate nodes. | brubeck-nakatsukasa-trefethen-2021 | §4; §6. | [record](records/brubeck-nakatsukasa-trefethen-2021.md) | WebFetch digest; UNVERIFIED |
```

New:

```
| LIT-285 (LIT?bivariate-lanczos-claude-442) | PR-prep consolidation 2026-11-01 / WebFetch digest / §4: two-pass variant called an 'extremely stable alternative' (asserted); Lanczos caveat; univariate only | §4 (as digested): the two-pass variant is called an extremely stable alternative, asserted without proof; the Lanczos caveat of the Step 0 statement 034 is confirmed. Accuracy is measured end to end (the fit only). There is no multivariate section; §6 is complex 1D. Hypotheses: Univariate nodes. | brubeck-nakatsukasa-trefethen-2021 | §4; §6. | [record](records/brubeck-nakatsukasa-trefethen-2021.md) | WebFetch digest; UNVERIFIED · P3 2026-11-03: verified in arXiv v1, p. 5; context: the 'extremely stable alternative' remark concerns computing d = Qᵀf/m after two orthogonalisation passes. |
```

### INDEX.md — LIT-289

Old:

```
| LIT-289 (LIT?bivariate-lanczos-claude-446) | PR-prep consolidation 2026-11-01 / WebFetch digest / Thm 4.6: Greenbaum-type model with N = nk and ‖S - T-tilde‖ of order eps‖A‖ up to a polynomial factor in k | Thm 4.6 (as digested): there are symmetric N x N matrices S and T-tilde with N = nk, T-tilde tridiagonal with the computed T_k as its leading block, S = U-hat^T (I_k tensor A) U-hat, and ‖S - T-tilde‖ bounded by a polynomial-in-k factor times eps‖A‖. The paper contrasts this with Greenbaum's bound, which it says depends on the fourth root of the accuracy parameter ([Gre89, eq. (7.10)]). No block or multivariate content. Hypotheses: Symmetric A, single start vector; preprint of Aug 2026. | chen-2026 | §4, Thm 4.6; remark on [Gre89, eq. (7.10)]. | [record](records/chen-2026.md) | WebFetch digest of the PDF; UNVERIFIED |
```

New:

```
| LIT-289 (LIT?bivariate-lanczos-claude-446) | PR-prep consolidation 2026-11-01 / WebFetch digest / Thm 4.6: Greenbaum-type model with N = nk and ‖S - T-tilde‖ of order eps‖A‖ up to a polynomial factor in k | Thm 4.6 (as digested): there are symmetric N x N matrices S and T-tilde with N = nk, T-tilde tridiagonal with the computed T_k as its leading block, S = U-hat^T (I_k tensor A) U-hat, and ‖S - T-tilde‖ bounded by a polynomial-in-k factor times eps‖A‖. The paper contrasts this with Greenbaum's bound, which it says depends on the fourth root of the accuracy parameter ([Gre89, eq. (7.10)]). No block or multivariate content. Hypotheses: Symmetric A, single start vector; preprint of Aug 2026. | chen-2026 | §4, Thm 4.6; remark on [Gre89, eq. (7.10)]. | [record](records/chen-2026.md) | WebFetch digest of the PDF; UNVERIFIED · P3 2026-11-03: superseded numbering: in arXiv v2 (18 Oct 2026) the model is Theorem 5.7 (pp. 20–21): Ã = I_{k+1} ⊗ A + Δ of dimension n(k+1), ‖Δ‖ ≲_k ε‖A‖, exact reproduction of T_k; fourth-root remark located in v2 §5 pp. 14–15. |
```

### INDEX.md — LIT-290

Old:

```
| LIT-290 (LIT?bivariate-lanczos-claude-447) | PR-prep consolidation 2026-11-01 / talk abstract / author's talk abstract: the old interval bound is not as small as one might hope; width of order eps‖A‖ argued | Greenbaum's own talk abstract (Prague, undated; seminar-nm.karlin.mff.cuni.cz, praguetalk1abs.pdf) confirms LAA 113 (1989) 7–63 and says the interval bound of the 1989 paper was not as small as one might hope, and sets out to argue that the widths are of order eps‖A‖. The L3 review lists the secondary accounts of the proven width as in conflict: sqrt(eps)‖A‖ (Šimonová–Tichý), the fourth root of the accuracy parameter (Chen, citing eq. (7.10)), and a max-form with unquantified f_j (Meurant–Strakoš). Hypotheses: Perturbed Lanczos/CG recurrences. | greenbaum-1989 | LAA 113 (1989) 7–63 (talk abstract); eq. (7.10) cited by Chen. | [record](records/greenbaum-1989.md) | talk abstract plus secondary reports; UNVERIFIED |
```

New:

```
| LIT-290 (LIT?bivariate-lanczos-claude-447) | PR-prep consolidation 2026-11-01 / talk abstract / author's talk abstract: the old interval bound is not as small as one might hope; width of order eps‖A‖ argued | Greenbaum's own talk abstract (Prague, undated; seminar-nm.karlin.mff.cuni.cz, praguetalk1abs.pdf) confirms LAA 113 (1989) 7–63 and says the interval bound of the 1989 paper was not as small as one might hope, and sets out to argue that the widths are of order eps‖A‖. The L3 review lists the secondary accounts of the proven width as in conflict: sqrt(eps)‖A‖ (Šimonová–Tichý), the fourth root of the accuracy parameter (Chen, citing eq. (7.10)), and a max-form with unquantified f_j (Meurant–Strakoš). Hypotheses: Perturbed Lanczos/CG recurrences. | greenbaum-1989 | LAA 113 (1989) 7–63 (talk abstract); eq. (7.10) cited by Chen. | [record](records/greenbaum-1989.md) | talk abstract plus secondary reports; UNVERIFIED · P3 2026-11-03: consistent with the paper's own conclusion (p. 61) that its theorems need excessively small ε. |
```

### INDEX.md — LIT-360

Old:

```
| LIT-360 (LIT?programme-ideas-claude-41) | Coverage-qualified LITERATURE; fact | Hokanson (arXiv 2009.10803): multivariate Vandermonde with Arnoldi builds each column by multiplying the smallest earlier index with I[k] + e_j = I[l] and orthogonalises with two-pass classical Gram–Schmidt against all previous columns (O(MN²)); notes that many orderings fail the span property. No truncation by degree blocks. | hokanson-2020 | Alg. 2.1 (as reported) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Padua points research since 2010.md, "Vandermonde with Arnoldi reinvented the recurrence densely"); secondary; new source statement; overlaps LIT-098, LIT-280, LIT-281 (PR #10); flag in integration-map-pr10 |
```

New:

```
| LIT-360 (LIT?programme-ideas-claude-41) | Coverage-qualified LITERATURE; fact — verified (P3 2026-11-03) | Hokanson (arXiv 2009.10803): multivariate Vandermonde with Arnoldi builds each column by multiplying the smallest earlier index with I[k] + e_j = I[l] and orthogonalises with two-pass classical Gram–Schmidt against all previous columns (O(MN²)); notes that many orderings fail the span property. No truncation by degree blocks. | hokanson-2020 | Alg. 2.1 p. 6; §2 pp. 5–6 (arXiv v1) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Padua points research since 2010.md, "Vandermonde with Arnoldi reinvented the recurrence densely"); secondary; new source statement; overlaps LIT-098, LIT-280, LIT-281 (PR #10); flag in integration-map-pr10 · P3 2026-11-03: verified in arXiv v1 (pp. 5–6); the paper credits the multivariate extension to Austin et al. [2, Subsec. 3.2] (arXiv 1912.02272). |
```

### INDEX.md — LIT-361

Old:

```
| LIT-361 (LIT?programme-ideas-claude-42) | Coverage-qualified LITERATURE; fact / open problem | Zhu–Nakatsukasa (IMA JNA 46(4), 2026, doi 10.1093/imanum/draf055; arXiv 2301.12241): near-optimality bound for multivariate V+A least squares on irregular domains; O(N²) equispaced or O(N² log N) random samples, O(N log N) for the weighted variant; they state the orthogonalisation is subject to loss of orthogonality by cancellation and that optimal sampling in high-dimensional irregular domains is open. | zhu-nakatsukasa-2026 | abstract and main theorem (as reported) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED beyond abstract (input: round-1 report; branch record records_lanczos/zhu-nakatsukasa-2026.md, -024/-025, abstract-level; journal data corrected in reports/Open problems verification.md §4); metadata+abstract (branch); new source statement; overlaps LIT-089, LIT-090, LIT-284 (PR #10); flag in integration-map-pr10 |
```

New:

```
| LIT-361 (LIT?programme-ideas-claude-42) | Coverage-qualified LITERATURE; fact / open problem — verified against arXiv v2 (P3 2026-11-03) | Zhu–Nakatsukasa (IMA JNA 46(4), 2026, doi 10.1093/imanum/draf055; arXiv 2301.12241): near-optimality bound for multivariate V+A least squares on irregular domains; O(N²) equispaced or O(N² log N) random samples, O(N log N) for the weighted variant; they state the orthogonalisation is subject to loss of orthogonality by cancellation and that optimal sampling in high-dimensional irregular domains is open. | zhu-nakatsukasa-2026 | abstract; Thm 4.3 p. 14; Thm 4.4 p. 15; Rem. 5.1(5) p. 20; Thm 5.1 p. 21; open problem pp. 2, 23 (arXiv v2) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED beyond abstract (input: round-1 report; branch record records_lanczos/zhu-nakatsukasa-2026.md, -024/-025, abstract-level; journal data corrected in reports/Open problems verification.md §4); metadata+abstract (branch); new source statement; overlaps LIT-089, LIT-090, LIT-284 (PR #10); flag in integration-map-pr10 · P3 2026-11-03: verified against arXiv v2; IMA version of record not read. |
```

### INDEX.md — LIT-362

Old:

```
| LIT-362 (LIT?programme-ideas-claude-43) | Coverage-qualified LITERATURE; open problem | Liu–Narayan (SISC 2023, doi 10.1137/22M1477131): multivariate Stieltjes computes Xu's block recurrence matrices from moments under an SVD canonical form (ΣB_{n,i}ᵀB_{n,i} diagonal); explicit in d = 2, a weighted orthogonal Procrustes problem in d = 3, and a non-convex optimisation for d > 3, whose investigation is said to be a natural extension; "far more stable" than moment/Gram–Schmidt methods; no complexity analysis; neither HL nor the seed cited. | liu-narayan-2023 | §5.2.1 and conclusions (as reported) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Padua points research since 2010.md Problem 4; round 2 §2 row 4 finds the non-convexity avoidable by one eigendecomposition — MEASURED in RESULTS.md); secondary; new source statement; overlaps LIT-096, LIT-279 (PR #10); flag in integration-map-pr10 |
```

New:

```
| LIT-362 (LIT?programme-ideas-claude-43) | Coverage-qualified LITERATURE; open problem | Liu–Narayan (SISC 2023, doi 10.1137/22M1477131): multivariate Stieltjes computes the block recurrence matrices from moments under a canonical form (Σ_i B_{n,i}ᵀB_{n,i} diagonal); explicit in d = 2; in d = 3 the remaining step is a weighted orthogonal Procrustes instance that the paper solves directly; for d > 3 a non-convex generalised Procrustes problem whose investigation is called a natural extension; 'far more stable' than direct Gram–Schmidt (empirical); no complexity analysis seen in the pages read; neither HL nor the seed cited. [Corrected P3 2026-11-03: d = 3 is solved directly, not left as an open WOPP.] | liu-narayan-2023 | abstract; §5.2.4–5.2.7 pp. 11–13; §7 p. 21 (arXiv v2) | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Padua points research since 2010.md Problem 4; round 2 §2 row 4 finds the non-convexity avoidable by one eigendecomposition — MEASURED in RESULTS.md); secondary; new source statement; overlaps LIT-096, LIT-279 (PR #10); flag in integration-map-pr10 · P3 2026-11-03: verified against arXiv v2 for the items stated; commuting conditions in the paper are credited to zu Castell–Filbir–Forster. |
```

### INDEX.md — LIT-364

Old:

```
| LIT-364 (LIT?programme-ideas-claude-46) | Coverage-qualified LITERATURE; fact | Finite-precision Lanczos theory for comparison: Paige 1976/1980 (single Hermitian operator), Simon 1984 (partial reorthogonalisation, semi-orthogonality), Greenbaum 1989 (nearby larger matrix), Jia–Li 2021 (joint bidiagonalisation with partial reorthogonalisation), Šimonová–Tichý BIT 2025 (block Lanczos), T. Chen 2026 (simplified Paige/Greenbaum), Sinha 2026 (block Paige identities, variable blocks), Amsel et al. 2026 (Simons list, Problem 2.19 on Paige's analysis for block Lanczos). All treat one operator (with block starts); none treats one start and two commuting operators. | paige-1976; paige-1980-lanczos; simon-1984-mathcomp; greenbaum-1989; jia-li-2021; simonova-tichy-2025; chen-2026; sinha-2026; amsel-et-al-2026 | as in the branch records | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Round 3 … F1; research_notes/Recent open problems 2023 2026/adv_F1_F6_F3.md §1; branch records listed in §4, all non-fulltext); metadata/abstract or secondary; new source statement; overlaps LIT-068, LIT-207, LIT-069, LIT-210, LIT-073, LIT-074, LIT-215, LIT-071, LIT-211, LIT-212, LIT-077, LIT-287, LIT-288, LIT-081, LIT-082, LIT-233, LIT-234, LIT-083, LIT-084, LIT-085, LIT-289, LIT-086, LIT-236 (PR #10); flag in integration-map-pr10 |
```

New:

```
| LIT-364 (LIT?programme-ideas-claude-46) | Coverage-qualified LITERATURE; fact | Finite-precision Lanczos theory for comparison: Paige 1976/1980 (single Hermitian operator), Simon 1984 (partial reorthogonalisation, semi-orthogonality), Greenbaum 1989 (nearby larger matrix), Jia–Li 2021 (joint bidiagonalisation with partial reorthogonalisation), Šimonová–Tichý BIT 2025 (block Lanczos), T. Chen 2026 (simplified Paige/Greenbaum), Sinha 2026 (block Paige identities, variable blocks), Amsel et al. 2026 (Simons list, Problem 2.19 on Paige's analysis for block Lanczos). All treat one operator (with block starts); none treats one start and two commuting operators. | paige-1976; paige-1980-lanczos; simon-1984-mathcomp; greenbaum-1989; jia-li-2021; simonova-tichy-2025; chen-2026; sinha-2026; amsel-et-al-2026 | as in the branch records | [baseline](../topics/programme-ideas-20261031/lit/baseline.md) | UNVERIFIED (input: reports/Round 3 … F1; research_notes/Recent open problems 2023 2026/adv_F1_F6_F3.md §1; branch records listed in §4, all non-fulltext); metadata/abstract or secondary; new source statement; overlaps LIT-068, LIT-207, LIT-069, LIT-210, LIT-073, LIT-074, LIT-215, LIT-071, LIT-211, LIT-212, LIT-077, LIT-287, LIT-288, LIT-081, LIT-082, LIT-233, LIT-234, LIT-083, LIT-084, LIT-085, LIT-289, LIT-086, LIT-236 (PR #10); flag in integration-map-pr10 · P3 2026-11-03: the Šimonová–Tichý, Sinha, Chen (v2), Paige 1980, Paige 2010, Greenbaum and Meurant–Strakoš readings now have page-level coverage (see p3 addenda); all treat one symmetric/Hermitian operator with a single or block start; the 'none treats one start and two commuting operators' statement is confirmed within those pages (bounded reading). |
```

## 3. literature/INDEX.md — new rows

Insert a new section after the last table (before "### Reused-source coverage addenda (2026-11-01)"), or wherever the orchestrator places the campaign's rows. Final IDs replace the provisional ones.

```
### padua-literature-20261103 — P3 primary readings

| LIT ID | Claim type / keywords | Published statement and hypotheses | Source key | Page / theorem | Record | Reading coverage |
|---|---|---|---|---|---|---|
| LIT?padua-literature-claude-40 | LITERATURE / primary reading / Favard-type (Kowalski) | Theorem K: a sequence of polynomial vectors is an orthogonal basis for some quasi-inner product iff a stacked three-term relation with rank A_k = r_{k+1} holds and a stated recursion yields nonsingular symmetric matrices. Quasi-inner products (no positivity); full sequences. | xu-sima-1993 | p. 785, Theorem K | [record](records/xu-sima-1993.md) | AC copy, pp. 783–790; displays garbled in text layer |
| LIT?padua-literature-claude-41 | LITERATURE / primary reading / coordinate three-term relation | Theorem 1: x_iP_k = A_{k,i}P_{k+1} + B_{k,i}P_k + C_{k,i}P_{k−1} with moment identities and A_{k,i}H_{k+1} = H_kC_{k+1,i}ᵀ; Kowalski-type recursion with non-unique D_{k,i}; Corollary 1: stacked A_k, C_{k+1} have rank r_{k+1}, each A_{k,i}, C_{k+1,i} rank r_k. | xu-sima-1993 | pp. 785–787, Thm 1, Cor. 1, (3.2)–(3.11) | [record](records/xu-sima-1993.md) | AC copy |
| LIT?padua-literature-claude-42 | LITERATURE / primary reading / Favard theorem (quasi-inner) | Theorem 2: a sequence {P_k} is an orthogonal basis for some quasi-inner product iff coordinate-wise three-term relations hold with rank A_k = rank C_{k+1} = r_{k+1}. No positivity, full sequences; no commuting conditions stated. | xu-sima-1993 | pp. 787–788, Thm 2 | [record](records/xu-sima-1993.md) | AC copy |
| LIT?padua-literature-claude-43 | LITERATURE / primary reading / Christoffel–Darboux, kernel | Theorem 3 (multivariate Christoffel–Darboux) and Theorem 4 (kernel depends only on the spaces V_k). | xu-sima-1993 | pp. 788–790 | [record](records/xu-sima-1993.md) | statements only |
| LIT?padua-literature-claude-44 | LITERATURE / primary reading / block Greenbaum model, conditional | Theorem 1: perturbed block Lanczos extension T_N with perturbations ≤ ε₂‖A‖ and a Ritz-vector condition (ε₁) has every eigenvalue within 3max(√Nε₂, ε₁)‖A‖ of A's. One symmetric A, block start. | simonova-tichy-2025 | arXiv v1 p. 13, Thm 1, (14)–(16) | [record](records/simonova-tichy-2025.md) | arXiv v1 PDF pp. 1–5, 10–20, 23–26 |
| LIT?padua-literature-claude-45 | LITERATURE / primary reading / continuation; open step | Continuation process (19); Theorems 2–4 (orthonormality, perturbed three-term form, perturbation formulas with ρ_k = ‖R_k^{−1}‖); sufficient conditions (35)–(36); bounding the second term of (35) open in the block case; local bounds (9), (11), (12) credited to unpublished Carson–Chen. | simonova-tichy-2025 | pp. 14–20 | [record](records/simonova-tichy-2025.md) | as above |
| LIT?padua-literature-claude-46 | LITERATURE / primary reading / experiments; open questions | Block CG matches ε‖A‖-interval model systems; continuation experiments: conditions met to ~1e-5, spreads typically O(√ε)‖A‖; key open question: choice of W_k; block analogues of Paige's results needed. | simonova-tichy-2025 | pp. 10, 23–25 | [record](records/simonova-tichy-2025.md) | as above |
| LIT?padua-literature-claude-47 | LITERATURE / location check | Author statements on difficulty located: §1 p. 3, §4 p. 10, §5 p. 13. | simonova-tichy-2025 | pp. 3, 10, 13 | [record](records/simonova-tichy-2025.md) | as above |
| LIT?padua-literature-claude-48 | LITERATURE / primary reading / multivariate V+A algorithm | Algorithm 3: smallest-k parent rule with grevlex, CGS twice against all previous columns, cost O(MN²); monomial basis not Krylov (§3). | zhu-nakatsukasa-2026 | arXiv v2 pp. 7–8, 21 | [record](records/zhu-nakatsukasa-2026.md) | arXiv v2 PDF pp. 1–8, 10–11, 13–15, 18–25 |
| LIT?padua-literature-claude-49 | LITERATURE / primary reading / rounding content | Remark 5.1(5): loss of orthogonality by cancellation; CGS2 gives ε_m ∼ O(MN^{3/2})u; ε_m enters Theorem 5.1 (reduced Gram matrix, in probability). No statement on the computed span or H. | zhu-nakatsukasa-2026 | pp. 20–22 | [record](records/zhu-nakatsukasa-2026.md) | as above |
| LIT?padua-literature-claude-50 | LITERATURE / primary reading / near-optimality; open problem | Theorem 4.4: ‖f − L(f)‖ ≤ (1 + O(N))‖f − p*‖ with M = O(N²) equispaced points (exact arithmetic); Theorem 4.3 random sampling; §5.2 'unaffected by ill-conditioning' with 1D evidence (Fig. 13); optimal sampling in high-dimensional irregular domains stated open. | zhu-nakatsukasa-2026 | pp. 2, 14–15, 22–25 | [record](records/zhu-nakatsukasa-2026.md) | as above |
| LIT?padua-literature-claude-51 | LITERATURE / primary reading / Alg. 2.1 | Multivariate V+A credited to Austin et al.; smallest-k parent rule; many orderings fail the span property; grevlex (total) and lex (max) work; CGS with two refinement steps against all previous columns; weight start vector; complex points allowed. | hokanson-2020 | arXiv v1 pp. 4–7 | [record](records/hokanson-2020.md) | arXiv v1 PDF pp. 1–7, 11–12 |
| LIT?padua-literature-claude-52 | LITERATURE / bibliographic | Reference [2] = Austin et al., Multivariate rational approximation, 2019, arXiv:1912.02272v1. | hokanson-2020 | p. 11 | [record](records/hokanson-2020.md) | as above |
| LIT?padua-literature-claude-53 | LITERATURE / primary reading / 1D stability remarks | V+A keeps H only; for real nodes Arnoldi = Lanczos with a stated risk of reduced accuracy from loss of orthogonality; two-pass orthogonalisation makes d = Qᵀf/m an 'extremely stable alternative' (asserted). Univariate. | brubeck-nakatsukasa-trefethen-2021 | arXiv v1 §4 pp. 3–5; §7 pp. 8–9 | [record](records/brubeck-nakatsukasa-trefethen-2021.md) | arXiv v1 PDF pp. 1, 3–5, 8–9 |
| LIT?padua-literature-claude-54 | LITERATURE / primary reading / commuting conditions, Favard (cited) | Theorem 2.1: commuting conditions (6a)–(6c) (credited to zu Castell–Filbir–Forster); Theorem 3.2 (credited to Dunkl–Xu Thm 3.5.1): generated sequence orthonormal for a positive-definite functional iff symmetric A, rank and commuting conditions; finite n used. | liu-narayan-2023 | arXiv v2 pp. 4, 6 | [record](records/liu-narayan-2023.md) | arXiv v2 PDF pp. 1–2, 4–6, 9–13, 19, 21–22 |
| LIT?padua-literature-claude-55 | LITERATURE / primary reading / canonical form | Definition 3.1, Theorem 3.1 (stacked consistent recurrence, Λ_{n+1} ≻ 0), §3.2 (one eigendecomposition per degree). | liu-narayan-2023 | pp. 5–6 | [record](records/liu-narayan-2023.md) | as above |
| LIT?padua-literature-claude-56 | LITERATURE / primary reading / MS algorithm; empirical stability | MS steps (25)–(28); d = 2 needs no commuting conditions; d > 2 non-convex generalised WOPP (35); d = 3 solved directly; stability claims empirical (§6.3). | liu-narayan-2023 | pp. 9–13, 19, 21 | [record](records/liu-narayan-2023.md) | as above |
| LIT?padua-literature-claude-57 | LITERATURE / primary reading / setting; Paige theorem as used | Perturbed recurrence (3) with ‖f^j‖ ≤ ε‖A‖; Paige's theorem as quoted: β_{N+m} = 0 with perturbations ≤ ξ‖A‖ gives eigenvalues within σ(N+m)³ξ‖A‖. | greenbaum-1989 | pp. 13–14, 22 | [record](records/greenbaum-1989.md) | AC copy, pp. 13–14, 20–24, 30, 43–44, 50–51, 60–62 |
| LIT?padua-literature-claude-58 | LITERATURE / primary reading / main theorems | Theorem 1 (p. 23): T_J = exact Lanczos output for a matrix with eigenvalues within σ(N+m)³max{ε‖A‖, ‖f^J‖, …}; Theorem 1′ (p. 51): widths σ(N+m)³O(J²γ√ε‖A‖) under (7.9) and separation, else σ(N+m)³O(c_max^{3/2}Jε^{1/4}‖A‖) with (7.10). | greenbaum-1989 | pp. 21–23, 43–44, 50–51 | [record](records/greenbaum-1989.md) | as above |
| LIT?padua-literature-claude-59 | LITERATURE / primary reading / caveat | The theorems need excessively small ε; observed to hold for larger ε; precise bound unknown (conclusions). | greenbaum-1989 | pp. 60–61 | [record](records/greenbaum-1989.md) | as above |
| LIT?padua-literature-claude-60 | LITERATURE / primary reading / rounding relations | (2.10)–(2.21): computed relation, local orthogonality, assumptions (2.16), ‖δR_k‖_F ≤ kσε₂; (3.13): z_iᵀv_{k+1} = −ε_ii/(β_{k+1}η_{ki}). | paige-1980-lanczos | pp. 238–239, 241 | [record](records/paige-1980-lanczos.md) | AC copy, pp. 237–239, 241, 245–246, 248, 250 |
| LIT?padua-literature-claude-61 | LITERATURE / primary reading / accuracy theorems | Lemma 3.1; Theorem 3.1 ((k+1)³σε₂ for stabilized values); Corollary 3.1 (5t²σε₂); Theorem 4.1. | paige-1980-lanczos | pp. 245–246, 248, 250 | [record](records/paige-1980-lanczos.md) | as above |
| LIT?padua-literature-claude-62 | LITERATURE / primary reading / augmented stability | Theorem 3.1, Corollaries 3.2–3.4: computed T_{k+1,k} and vectors are exact Lanczos for diag(T_k, A) + H^{(k)}, ‖H^{(k)}‖ ≤ 4(‖E_k‖ + ‖F_k‖); not standard backward stability. | paige-2010-augmented | pp. 2348, 2353–2357 | [record](records/paige-2010-augmented.md) | author PDF pp. 2347–2358 |
| LIT?padua-literature-claude-63 | LITERATURE / primary reading (survey) | Theorems 4.4–4.5 (Paige) and 4.9 (Greenbaum) as stated in the survey; rigorous a-priori blurred model incomplete. | meurant-strakos-2006 | pp. 505–506, 510–512 | [record](records/meurant-strakos-2006.md) | author PDF, those pages |
| LIT?padua-literature-claude-64 | LITERATURE / primary reading / block backward model | Theorem 6: (I_k ⊗ A + Δ)V̂ = V̂T + ŴHE_kᵀ with ‖Δ‖ ≤ 2(2√k e + 4√k(√k + k − 1)μ); one symmetric A; block sizes from deflation. | sinha-2026 | arXiv v1 pp. 37–39 | [record](records/sinha-2026.md) | statements only: PDF pp. 1, 27, 37–39, 42, 45, 49 |
| LIT?padua-literature-claude-65 | LITERATURE / primary reading / block Paige identities | Theorem 7: g_iᵀw_i = −s_iᵀMs_i, |g_iᵀw_i| ≤ μ, pairwise relation (120)–(121); Theorem 8: extra Ritz values from overlap. | sinha-2026 | pp. 42, 45 | [record](records/sinha-2026.md) | as above |
| LIT?padua-literature-claude-66 | LITERATURE / primary reading / Greenbaum-type model, O(ε) | Theorem 5.7 (v2): Ã = I_{k+1} ⊗ A + Δ, ‖Δ‖ ≲_k ε‖A‖, exact reproduction of T_k from (v̄₁, 0, …); Remark 5.8 (eigenvalues within ‖Δ‖; Wasserstein-close spectral measures); Theorem 5.11 (containment). | chen-2026 | arXiv v2 pp. 14–16, 20–22 | [record](records/chen-2026.md) | statements only: v2 PDF pp. 1, 10–11, 14–16, 20–22 |
| LIT?padua-literature-claude-67 | LITERATURE / primary reading / Paige bound | Theorem 4.1 (v2): |xᵀv_{k+1}|·β_k|e_kᵀy| ≲_k ε‖A‖ for every Ritz pair. | chen-2026 | p. 14 | [record](records/chen-2026.md) | as above |
```

## 4. literature/CORPUS.md

### 4a. New row (insert in the Lanczos block, after `chen-2026`)

```
| xu-sima-1993 | Y. Xu, On multivariate orthogonal polynomials, SIAM J. Math. Anal. 24(3) (1993) 783–794 | [doi:10.1137/0524048](https://doi.org/10.1137/0524048) (Crossref-checked 2026-11-03, p3-links item 8c); AC copy `~/Downloads/padua/papers/0524048.pdf` | have (AC local copy) | exact pages 783–790 (P3 2026-11-03) | [record](records/xu-sima-1993.md) | pp. 790–794; display transcription |
```

### 4b. Coverage-cell appends for existing rows

Append to the *Reading coverage* cell, with a leading " · ", the text shown. The old cell text stays in place. Use the coverage lines given in each addendum:

- `greenbaum-1989`: "P3 2026-11-03: AC copy `1-s2.0-0024379589902851-main.pdf` read, pp. 13–14, 20–24, 30, 43–44, 50–51, 60–62 (Theorems 1, 1′)". Also change *Availability* to append "· have (AC local copy, 2026-11-03)".
- `paige-1980-lanczos`: "P3 2026-11-03: AC copy `1-s2.0-0024379580901676-main.pdf` read, pp. 237–239, 241, 245–246, 248, 250". *Availability* append "· have (AC local copy)". *Gaps*: replace "Whole source; pending-reference. Online pass: Whole source (scan)." with "Theorems 4.2–4.3 (pp. 252–253) and pp. 242–244 unread (P3 2026-11-03)."
- `simonova-tichy-2025`: "P3 2026-11-03: arXiv v1 PDF (pdf.js) pp. 1–5, 10–20, 23–26".
- `zhu-nakatsukasa-2026`: "P3 2026-11-03: arXiv v2 PDF (pdf.js) pp. 1–8, 10–11, 13–15, 18–25; v2 has no appendix (Alg. 4 p. 8, Alg. 5 p. 20); IMA version not read".
- `hokanson-2020`: "P3 2026-11-03: arXiv v1 PDF pp. 1–7, 11–12". *Availability*: replace "supplied account; fulltext pending" with "open (arXiv)".
- `brubeck-nakatsukasa-trefethen-2021`: "P3 2026-11-03: arXiv v1 PDF pp. 1, 3–5, 8–9".
- `liu-narayan-2023`: "P3 2026-11-03: arXiv v2 PDF pp. 1–2, 4–6, 9–13, 19, 21–22".
- `paige-2010-augmented`: "P3 2026-11-03: author PDF pp. 2347–2358 (statements)".
- `meurant-strakos-2006`: "P3 2026-11-03: author PDF pp. 505–506, 510–512".
- `sinha-2026`: "P3 2026-11-03: arXiv v1 PDF pp. 1, 27, 37–39, 42, 45, 49 (statements)".
- `chen-2026`: "P3 2026-11-03: arXiv v2 (18 Oct 2026) PDF pp. 1, 10–11, 14–16, 20–22 (statements); v1 numbering superseded". In *Citation*, append "(v2 18 Oct 2026)".

(The CORPUS rows are long, so I give appends rather than full-row literals. The orchestrator should apply them with the same " · " convention the file already uses.)

## 5. Shared notes for the report

- The LIT-213 conflict about interval widths is resolved on the original: both widths are branches of Greenbaum's Theorem 1′ (p. 51).
- The LIT-090 / F9 conflict about the ZN sentence is resolved: the sentence is in v2, Remark 5.1(5), p. 20.
- Liu–Narayan credit the commuting conditions to zu Castell–Filbir–Forster and the Favard converse to Dunkl–Xu Thm 3.5.1. Any note citing "Xu's commuting conditions" should cite Xu TAMS 343 Cor. 2.3, which still needs a page-level reading because AMS was blocked.
