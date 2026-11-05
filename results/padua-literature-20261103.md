# padua-literature-20261103 — literature campaign for the new Padua results

This file is written only by the topic orchestrator. Branch `claude/padua-literature-20261103`; [draft PR #21](https://github.com/aacchhee/padua_research/pull/21); reserved LIT-482–561.

## Status (2026-11-05): audit-02 accepted F1–F6; response 02 answers F7; short Codex check next. Final report: [report.md](../topics/padua-literature-20261103/report.md)

These are literature findings only. They carry no PD status changes and no new mathematical claims.

- **Download list** with verified clickable links: [DOWNLOADS.md](../topics/padua-literature-20261103/DOWNLOADS.md), v3. AC supplied 10 of the requested PDFs; the items still needed are in Part A and A2.
- **P1 (Lebesgue function)**, [comparison](../topics/padua-literature-20261103/p1-comparison.md):
  - The corner-argmax statement was a published conjecture (CDMSV 5ECM poster 2008) and observation (De Marchi, [CMA 5 (2022)](https://doi.org/10.33205/cma.1070020) §3.3(2), p. 23), with no proof. Our PD-T209/162/166/169/174/177/181/214 (n = 2–16) and PD-T229 (n ≥ N_*) prove it in those ranges.
  - The coefficient 4/π² is published as the global constant (Kolomoitsev–Lomako 2021, built on [Kuznetsova 1995](https://doi.org/10.1007/BF01056716), with Pimenova 1979 as a special case). The corner value is bounded above by it; for the matching lower bound at the corner itself, no published statement was found (response-01 F1). The b log n term with explicit remainder (PD-T158) and the exact corner formula (PD-T101): no matching result found.
  - 1-D context and attribution: [Ehlich–Zeller 1966](https://doi.org/10.1007/BF01429047) and [Brutman 1978](https://doi.org/10.1137/0715046). "Powell 1965" should be cited as [Powell 1967](https://doi.org/10.1093/comjnl/9.4.404).
  - Audit F6 (KL locators) resolved.
- **P2 (MZ)**, [comparison](../topics/padua-literature-20261103/p2-comparison.md):
  - The SVZ 2008 eq. (25) misprint is also in the journal version, and Table 1 confirms the correct denominator.
  - PD-T106 is now IMPLIES PART: the signed rule and degree-m exactness are published, while "precisely m", the aliases and the pencil are not.
  - Gaps closed: Wu AML 2026, Don–Gottlieb journal version, Dencker–Erb journal version.
- **P4 (Leuven IEP/MOP)**: [memo for AC](../topics/padua-literature-20261103/p4-memo.md). No Leuven work treats two variables or cites Van Barel–Chesnokov 2010. Three joint questions are proposed for a later topic; none is registered.
- **P3 (Lanczos / V+A)**, [comparison](../topics/padua-literature-20261103/p3-comparison.md):
  - IMPLIES PART for PD-T031 (Sinha 2026, single operator) and PD-T057 (Xu 1993; Liu–Narayan/Dunkl–Xu). For the truncated form and the manifold structure, no matching result.
  - No matching result for the Padua obstruction (PD-T069/N303), ρ_n = O(n⁻⁵) (PD-T144) or the span drift.
  - Greenbaum width conflict (LIT-213) resolved; LIT-096, LIT-210 and LIT-362 corrected.

## Pass 2 (2026-11-05)

- **Mastroianni–Russo 2000** ([zbMATH](https://zbmath.org/1594022); AC copy) is read. It has no quantitative borderline converse-MZ result: uniform constants under A_p hypotheses, and the CC/Lebesgue/p = 2 case is exactly the excluded A_2 endpoint of its Theorem 11. This closes the MZ prior-art report's named gap; the "no matching result" verdict for the two-sided endpoint order (PD-T017/T018) stands, with wider coverage.
- **Journal versions** of [KLP 2018](https://doi.org/10.1016/j.jat.2018.02.005), [Xu 1996](https://doi.org/10.1006/jath.1996.0102), [CDMV 2007](https://doi.org/10.1016/j.cam.2006.10.058) and [BCDMVX 2006](https://doi.org/10.1016/j.jat.2006.03.008) are checked: numbering coincides with the free versions, and journal pages are recorded. One correction: Xu 1996 Thm 3.3 is for 1 < p < ∞ (LIT-314 said ≤ ∞).
- Still missing: Della Vecchia–Mastroianni–Vértesi 1995 ([zbMATH](https://zbmath.org/854180), print only); low priority Brutman 1997 survey, Feldheim 1936 ([zbMATH](https://zbmath.org/3023405)) and König–Nielsen journal version ([doi](https://doi.org/10.1515/form.1994.6.183)).

## Next step

Codex (gpt-6-astra high) short check of F7 per handoff 10, then PR preparation by Claude. Still needed from AC: print-only DMV 1995 (see DOWNLOADS v5).

## 2026-11-05 — independent audit disposition

Codex audit-01 **CHANGES REQUESTED**; stage WORK. Six source-transcription/attribution/scope findings require Claude's response. The preceding development summary is preserved as historical input and is qualified by the audit, particularly its corner-leading-term attribution and Mastroianni no-rates wording. Independent numerical consistency rerun passed;60 literal Old blocks match the recorded base. Mandatory source/image/journal/Crossref checks remain incomplete; no literature acceptance, PD status change or readiness is claimed. See [audit](../topics/padua-literature-20261103/audit-01.md) and [handoff05](../topics/padua-literature-20261103/handoffs/05-response.md).

## 2026-11-05 — response 01 (Claude)

All six audit-01 findings were accepted and answered with changes; see [response-01](../topics/padua-literature-20261103/response-01.md).
- **F1.** The PD-T156/157 attribution is split: the upper half is IMPLIES PART; for the lower bound at the corner, no published statement was found (KL's lower estimate is at a non-corner point). The coefficient 4/π² is published as the global constant and not claimed as new.
- **F2–F6.** Record corrections: Mastroianni–Russo Thm 9 hypothesis and scoped negative; Möller dim Π²_{n−1}; downdating question scoped against IDEA-094/095; Laurie awareness statement kept.
- **Primary checks.** Xu 1996 journal Thm 3.3 has 1 < p < ∞ (version difference from the preprint), De Marchi p. 23 and SVZ (25)/Table 1 confirmed; 10/10 direct Crossref matches.
- **Supplement.** Pimenova (constant 2/π²), Kuznetsova p. 259 and SVZ pp. 417/421 confirmed on page images; no verdict changes.
- **MathSciNet citation check.** One citer of KL 2021 (Kolomoitsev–Liflyand 2021, Fourier simplex constants; RELATED), no indexed citing item returned for De Marchi 2022 (an index-query result, not publication absence; response-02), nine of SVZ 2008 (Padua2DM restates "not all positive" weights). No verdict changes.

## 2026-11-05 — audit 02 of response and supplements

Original six findings are resolved in the bounded re-audit. One new P2 F7 requires narrowing the MathSciNet zero-citation inference; stage WORK and PR remains draft. Source reading closures are developer-verified where independent journal/image access failed, and are not presented as auditor verification. Actual literal checker rerun at reconciled main:60/60; merge-preservation and reservation checks pass within recorded scope. No scientific verdict/status or final ID changes. [Audit02](../topics/padua-literature-20261103/audit-02.md); [handoff09](../topics/padua-literature-20261103/handoffs/09-response.md).

## 2026-11-05 — response 02 (Claude)

Audit-02 F7 is fixed. A zero MathSciNet count for De Marchi 2022 is now reported only as "AC's check returned no indexed citing item", not as publication absence, in the note, the P1 comparison and the summary above. No verdict changes. Next: a short Codex check of F7, then PR preparation. [Response-02](../topics/padua-literature-20261103/response-02.md).


## 2026-11-05 — audit 03: F7 accepted

The narrow F7 response is accepted: the three sentences report AC's dated MathSciNet query outcome, with no universal publication-absence inference. All seven findings across audit01/02 are now resolved within their accepted scopes. Stage PR for preparation; draft remains. Existing developer-only source qualifications and nonexhaustive priority limits remain binding. No verdict/status/ID change or new run. [Audit03](../topics/padua-literature-20261103/audit-03.md); [handoff11](../topics/padua-literature-20261103/handoffs/11-prepare.md).
