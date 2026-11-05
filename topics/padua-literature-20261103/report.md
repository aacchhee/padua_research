# Report — padua-literature-20261103 (WORK complete; audit pending)

Claude (claude-opus-5-5, high), topic orchestrator, 2026-11-03.
- Rules read at `0a173a2`; base main `440d107`.
- [Draft PR #21](https://github.com/aacchhee/padua_research/pull/21); reserved LIT-482–561.
- This topic is literature only: no new mathematical claims and no PD status changes. Every verdict rests on pages actually read, as listed in the records and in the pack comparison memos.

## How the work was done

1. **Inventory.** AC's `Downloads\padua\papers` (24 files, later 36) and `Downloads\bttb\papers` were listed through the link to AC's computer and matched to citations ([inventory.md](inventory.md)).
2. **Link verification.** Four Sonnet 5.5 high subagents, one per pack. Every DOI was checked against Crossref; arXiv and author pages were opened. The result is [DOWNLOADS.md](DOWNLOADS.md), v1→v3.
   - v1 was sent to AC early. AC supplied 10 of the requested PDFs within the session.
3. **Reading.**
   - P1 was read by the orchestrator. P2, P3 and P4 were read by Opus 5.5 high reader subagents and integrated and spot-checked by the orchestrator.
   - Methods:
     - text extraction in the built-in browser on AC's computer (arXiv; Springer via NTNU; Math-Net.ru; UMJ; DergiPark; author pages);
     - pdftotext on the AC-supplied PDFs staged into the cloud workspace;
     - page images where formulas mattered.
   - ScienceDirect, SIAM and AMS pages present bot checks, which were not bypassed; those items were listed for AC. No third-party text is committed.

## Pack results and what each fulltext changed

### P1 — Padua Lebesgue function ([p1-comparison.md](p1-comparison.md))

- **Corner argmax.**
  - It was conjectured in the Caliari–De Marchi–Sommariva–Vianello 5ECM poster (2008): the maximum is at a vertex and ≈ (4/π²) log² n.
  - It was observed in De Marchi, [CMA 5 (2022)](https://doi.org/10.33205/cma.1070020), §3.3(2), p. 23: the maxima are "in the corners, where there are no Padua points".
  - No proof was found. PD-T209/162/166/169/174/177/181/214 (n = 2–16) and PD-T229 (n ≥ N_*) prove it in those ranges.
  - Wording: "proves the conjecture of …".
  - The analogous Xu-points conjecture ([Computing 76 (2006)](https://doi.org/10.1007/s00607-005-0137-z), Conj. (17)) remains open.
- **Corner asymptotics.**
  - The coefficient 4/π² is not new, as the coefficient of the global constant: Kolomoitsev–Lomako 2021 rest on [Kuznetsova, Ukr. Math. J. 47 (1995)](https://doi.org/10.1007/BF01056716), whose Thm 1 gives pointwise rhombic Lebesgue-function asymptotics. [Pimenova, Dokl. 249 (1979)](https://www.mathnet.ru/eng/dan43113) is an earlier special case.
  - PD-T156/157: IMPLIES PART for the upper half only (Λ_c ≤ Λ_n and KL's global theorem). For the lower bound at the corner itself, no matching result was found: KL's lower estimate is at the non-corner point (cos(π/m), 1), and no transfer was checked. The coefficient 4/π² is published as the global constant and is not claimed as new. (Revised 2026-11-05, response-01 F1.)
  - No matching result was found for the b log n term with explicit remainder (PD-T158), for PD-T159, or for the exact corner formula (PD-T101).
- **Edges.** Kuznetsova's leading factor equals 1 on whole lines, so the leading term cannot separate edges from corners. No published edge-versus-corner gap was found (PD-T185–192, T211/212/230).
- **1-D context.**
  - [Ehlich–Zeller 1966](https://doi.org/10.1007/BF01429047): the maximum is at ±1 for Chebyshev zeros and at the interval midpoints for equispaced trigonometric interpolation.
  - [Brutman 1978](https://doi.org/10.1137/0715046): monotone order of the local maxima; attribution chain Luttmann–Rivlin → Ehlich–Zeller (Powell 1967).
  - Günttner 1980/1988: explicit remainders.
- **Audit F6 (padua-proof-attempts-2) is closed.** The Kolomoitsev–Lomako locators are confirmed in arXiv v1 and in the published AMC version, which has identical numbering.

### P2 — MZ constants ([p2-comparison.md](p2-comparison.md))

- **SVZ 2008, journal version** (Springer).
  - Eq. (25) misprints the weight denominator in BOTH the preprint and the journal version. Table 1 is reproduced only with the correct (n+1)(n+2); see the [check](check/README.md), rerun by the orchestrator.
  - PD-T106 moves to IMPLIES PART: the signed rule and degree-m exactness are published. "Exactness precisely m", the alias formulas and the pencil are not.
  - PD-T111 is RELATED: SVZ show negative weights but not which ones, or a formula.
- **AC-supplied journal versions.**
  - Wu, AML 182 (2026): an abstract MZ⇒Galerkin-stability result (RELATED; gap closed).
  - Don–Gottlieb journal version: identical to the ICASE report (gap closed).
  - Dencker–Erb journal version: identical to arXiv v2 (LIT-014 can move to primary reading).
- **KLP 2018**, Lemma 5.1: an L^p MZ inequality at Lissajous/Padua nodes with positive weights and unspecified constants, credited to Erb 2016 (RELATED).
- **New lead.** De Marchi–Kroó 2018: explicit 1-D constants, but only inside half-exactness.
- **Negative scope unchanged.** No published result was found for the two-sided order (1+log N)^−2, the threshold below 2, or explicit constants beyond half-exactness.

### P3 — Bivariate Lanczos / V+A ([p3-comparison.md](p3-comparison.md))

- **IMPLIES PART:**
  - PD-T031: the single-operator case is in Sinha 2026, Thm 7.
  - PD-T057: the commuting conditions and the full-sequence Favard converse are in Xu 1993 and in Liu–Narayan, who credit Dunkl–Xu Thm 3.5.1.
    - Supplement (14:50; AC supplied Xu, Trans. AMS 343 and 342 and Dunkl–Xu Ch. 3, all read): (a) is implicit in Xu 342, proof of Thm 3.4 (p. 859); the converse is in Xu 343 Thm 2.2 and Dunkl–Xu Thm 3.5.1 (p. 88).
    - The truncated form, the words formula and the manifold structure were not found.
- **RELATED, DIFFERENT SETTING:** PD-T034, T051, T053, T056(G), T058, T059, T076, T142/143. The usual mismatch: one operator, 1-D, or informal statements only.
- **No matching result found:** PD-T060, PD-T069/N303 (Padua obstruction), PD-T144 (ρ_n = O(n⁻⁵)), PD-T145, PD-T136/137/141, and the span drift (N201/PD-T146).
- **Corrections from page-level reading.**
  - The LIT-213 width conflict is resolved: Greenbaum's Thm 1′ (p. 51) has a √ε branch and an ε^{1/4} branch, and the secondary accounts quoted different branches.
  - LIT-210's bounds are corrected (Paige 1980).
  - LIT-096 and LIT-362 are corrected (Liu–Narayan solve d = 3 directly).
  - The earlier "not in v2" finding about Zhu–Nakatsukasa (F9) is withdrawn: the sentence is in v2, Remark 5.1(5), p. 20.
  - LIT-360 is verified (Hokanson Alg. 2.1).
  - arXiv 1912.02272 is confirmed as Austin et al.

### P4 — Leuven IEP/MOP line ([p4-memo.md](p4-memo.md), for AC)

- **Scope.** Nine sources were read. None treats two variables, Padua points, or cites Van Barel–Chesnokov 2010 (keyword search, zero hits).
- **Record corrections.**
  - LIT-347/119: IEP_CORE and IEP_KRYLREORTH(full) are backward stable for most N < 25.
  - LIT-346: three authors; Faghih is not an author.
  - LIT-118: the ill-conditioning sentence is in the introduction and is about the SINUM methods.
  - LIT-420: the FHV description is corrected.
- **Stated future work**, with locators in the memo: nearest-neighbour MOPs, a conditioning/stability theory, and downdating for vector functions.
- **Proposed joint questions**, for a later topic and not registered:
  - (A) what the MOP IEP conditioning actually measures;
  - (B) nearest-neighbour MOPs as a commuting-pair IEP;
  - (C) bivariate downdating by structured perfect-shift IEP steps on the pair (H_x, H_y), as distinct from the classical stored-Q and R-factor routes already settled at IDEA-094/095.

## Merged claims whose wording should be narrowed or re-attributed

1. **P1 paper and manuscripts.**
   - Do not present the corner argmax as a new *statement*; present it as a proof of the 2008 conjecture and the 2022 observation.
   - Do not claim the coefficient 4/π² as new; credit Kolomoitsev–Lomako 2021 and Kuznetsova 1995. Do not attribute the corner lower bound to them either (their lower estimate is at a non-corner point; response-01 F1).
   - "Powell 1965", as cited by Białas-Cież et al., should read Powell 1967, or Ehlich–Zeller 1966.
2. **PD-T106.** The signed rule and its degree-m exactness are SVZ 2008's; only the "precisely m" exactness, the alias formulas and the pencil are ours. Footnote the misprint in eq. (25).
3. **PD-T057.** Limit the novelty sentence to the truncated version, the words formula and the manifold structure. Cite Xu 342 Thm 3.4, Xu 343 Thm 2.2 and Dunkl–Xu Thm 3.5.1 for the classical parts, and say the proof follows Dunkl–Xu's induction (revised wording D in p3-comparison.md).
4. **P3 note.**
   - Do not compare our √ε rate (exact representation of given perturbations) with the O(ε) 1-D rates of Greenbaum and Chen (actual runs) as one quantity.
   - Always name the Greenbaum branch when quoting a width.
5. **Registry text corrections.** LIT-096, LIT-118, LIT-210, LIT-213, LIT-284, LIT-346, LIT-347/119, LIT-362, LIT-377 (corner item now VERIFIED, p. 23), LIT-379 (locators), LIT-388 (complete reading) and LIT-420. All are given as literal blocks in [proposed-record-changes.md](proposed-record-changes.md).

## Pass 2 (2026-11-05): AC-supplied A4 and A11–A14

- **Mastroianni–Russo 2000 (A4)**, read from AC's 34-page copy; record `mastroianni-russo-2000.md` (LIT?…-85). This was the MZ prior-art report's "most likely remaining place" for a quantitative borderline converse-MZ result. It contains none:
  - The paper gives uniform-constant forward (Thm 8) and converse (Thms 9–12) weighted Marcinkiewicz inequalities under doubling/A_p hypotheses. It has no quantitative borderline estimate for the lower MZ constant and no necessity statements; its approximation-error rates (Thms 14–17, order m^{−r}) concern a different quantity. The only "log" in the text is in a funding line. (Scope corrected 2026-11-05, audit-01 F3.)
  - The CC nodes for even N are an instance of its "extended" Theorem 11: zeros of T_{m+1}U_m plus ±1, on the full space Π_N.
  - For u ≡ 1 and p = 2, the hypothesis (1−x²) ∈ A_2 fails exactly at the power-weight endpoint, so the theorem is silent there. This is consistent with PD-T019 and MMN 2012.
  - Verdicts: RELATED, DIFFERENT SETTING (PD-T017–019); RELATED (PD-T014/T022, uniform boundedness only, as in LMN 1987).
  - The "no matching result found in the documented search" negative for the two-sided order now also covers this source. See the P2 comparison, row added in pass 2.
- **A11–A14 journal versions** (KLP 2018, Xu 1996, CDMV 2007, BCDMVX 2006), recorded in [addenda/journal-versions-2026-11-05.addendum.md](addenda/journal-versions-2026-11-05.addendum.md). A Sonnet subagent mapped the locators; the orchestrator spot-checked three items on the PDFs.
  - All theorem, lemma and equation labels coincide with the free versions used earlier. Wording was not diffed.
  - One correction: LIT-314 says Xu 1996 Theorem 3.3 holds for 1 < p ≤ ∞; the journal (p. 231) has 1 < p < ∞.
  - Additions: CDMV 2007's explicit bound (13), p. 80; KLP's Lemma 5.1 sources; BCDMVX Theorem 3 is an order bound only.
- Proposed shared-file edits for pass 2: [proposed-record-changes.md](proposed-record-changes.md), section "Pass 2". DOWNLOADS is now v5.

## What remains missing (clickable)

- **Print only (interlibrary loan):**
  - ~~Mastroianni–Russo 2000~~: supplied by AC and read 2026-11-05 (see "Pass 2" below);
  - Della Vecchia–Mastroianni–Vértesi 1995, IDoMAT ([zbMATH](https://zbmath.org/854180));
  - Brutman 1997 survey (Ann. Numer. Math. 4);
  - Feldheim 1936 (C. R. 203, [zbMATH](https://zbmath.org/3023405)).
- **Bot-checked; AC to download:**
  - König–Nielsen [journal version](https://doi.org/10.1515/form.1994.6.183) (De Gruyter: "Unlicensed").
- **Leads to read later (free):**
  - Erb, AMC 289 (2016), [arXiv 1503.00895](https://arxiv.org/abs/1503.00895);
  - Paige 2019 ([author PDF](https://www.cs.mcgill.ca/~chris/pub/Pai19.pdf));
  - the version-of-record checks listed in p3-comparison.md, if exact wording will be quoted.
- **Small gaps:**
  - Pimenova 1979: the Theorem 1 constant should be checked on the page image (free scan).
  - Pimenova and Kuznetsova Lemmas 1–2: OCR only.

## Outputs

- Records: 9 new P1 records (by Claude), 5 P2, 1 P3, 8 P4, all in `literature/records/`. Addenda to existing records are in [addenda/](addenda/).
- [proposed-record-changes.md](proposed-record-changes.md), to be applied at PR preparation with the final-ID mapping.
- BibTeX: [bib/](bib/), with one file per paper (Lebesgue, MZ, Lanczos) plus Leuven.
- Provisional IDs: LIT?padua-literature-claude-01…08, 20…24, 40…67 and 70…84. These map into LIT-482–561 at PR preparation.
- Cross-topic note: `codex/padua-argmax-effective-20261103` (gate G8) can reuse the P1 records after merge (list in p1-comparison.md). This topic did not write to that branch.

## Audit request

Codex (gpt-6-astra high) audits this Claude development; see handoff 02.
