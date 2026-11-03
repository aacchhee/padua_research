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
