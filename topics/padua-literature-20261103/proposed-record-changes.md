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
