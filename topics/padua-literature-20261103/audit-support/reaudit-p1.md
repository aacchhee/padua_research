# Handoff08 bounded P1 re-audit — 2026-11-05

Input exact-file snapshot: `0b5fb2d4414af02af23c653cba9cd16e38c1cb8c`; scientific input `10aa5d31e3be477b90f44c122ade0c6180c9a252`. Auditor: Codex child `/root/reaudit_p1`, inherited requested gpt-6-astra high; serving model/effort metadata not independently exposed. No Git mutations or developer edits. Only this scratch report written.

## Disposition

Original F1 is resolved within the inspected documents. One new medium scope finding prevents a clean acceptance of the new MathSciNet note as written. The new source supplements can be accepted only as developer-checked reading records where noted below; this is not independent visual verification.

## New finding — MathSciNet zero does not establish universal absence (medium)

`topics/padua-literature-20261103/notes/mathscinet-citation-check-2026-11-05.md:8` infers that nothing has been published citing De Marchi's open-problems list from AC's zero MathSciNet citations. Zero indexed citations supports only that no citer was returned by that documented MathSciNet check. It does not establish the universal publication claim. The same note, line21, supplies its own counterexample to index completeness (Kuznetsova has zero despite two checked references). Replace the inference with “AC's MathSciNet query returned no indexed citing item” or equivalent bounded wording. The later limitations at line33 are appropriate but do not repair the explicit universal sentence. This finding requires no verdict change or additional mathematical development.

## Original F1 propagation — accepted

- `p1-comparison.md:37`: IMPLIES PART restricted to upper half; corner lower half explicitly search-negative; KL lower point identified as noncorner; no unchecked transfer asserted.
- `p1-comparison.md:51–52`: proposed manuscript wording attributes global coefficient4/pi² to KL, uses global-to-corner upper inequality, then separately states local corner result. Explicit no-new-coefficient warning retained.
- `report.md:31–35` and `89–91`: same upper/lower split, no credit to KL for corner lower bound.
- `results/padua-literature-20261103.md:12,42`: same narrowing. No residual false KL corner-lower attribution located in these files.
- PR body is root's responsibility and was not independently read here.

The audit does not reopen PD-T156/157 or require a transfer proof. It accepts the literature-topic choice to narrow attribution.

## Actual primary-source spot checks

1. **Padua2DM author-hosted preprint**: https://www.math.unipd.it/~marcov/pdf/fastpadua.pdf, followed from Vianello's Padua bibliography. Read extracted text on preprint printed p10/PDF index9 (web lines809–816): signed weights, negative weights few/small, sum of absolute weights tends to4, attributed to reference13. Read reference13 (lines1050–1051): SVZ2008. Read preprint p13/PDF index12 (lines961–965): unexplained multivariate CC-like behavior. These corroborate the content of MathSciNet-note line13 and unchanged RELATED bearing. The journal locators p54/p59 were not independently inspected. The preprint itself does give general weight formula(14), p8, so “no formula” should be understood as no formula identifying the negative weights, as the surrounding sentence says; no finding on this bounded reading.

2. **Kolomoitsev–Liflyand2021**: official AMS journal PDF URLs with `/proc/` and `/journals/proc/` returned403. SciSpace's indexed primary PDF header corroborates journal identity/pages/DOI, but direct open returned405; no journal p2914 visual/read claim. Author preprint https://arxiv.org/pdf/2004.12236 and HTML https://arxiv.org/html/2004.12236v1 were accessible. Read introduction/history, PDF pp1–4/HTML lines39–143, especially simplex Fourier-operator-norm setting, Kuznetsova history, and 2D formula/remainder. These corroborate RELATED DIFFERENT SETTING and failure to provide a pointwise Padua corner theorem. The preprint uses different displayed main-term normalization (16/pi and8/pi; journal record4/pi³ and2/pi³), so it is not an independent journal transcription check. The record's additional rational/irrational O(log n1)/O(log²n1) gloss (`literature/records/kolomoitsev-liflyand-2021.md:14`) was not verified against journal p2914; the accessible preprint's displayed 2D paragraph does not state that gloss and emphasizes arithmetic subtleties. Carry it as developer-verified only, or obtain its precise journal locator/hypotheses before elevating its verification. This is an unresolved access/coverage limit, not a demonstrated false published transcription.

3. **Pimenova1979**: opened Math-Net metadata https://www.mathnet.ru/eng/dan43113 and full primary PDF https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=43113&what=fullt. Read pp52–53 OCR, including grid/theorem1/equation3; mathematical OCR is garbled. Screenshot calls for PDF pages0/1 returned only textual `<<ImageDisplayed>>` markers, no image content exposed. Therefore I do not independently confirm constants/arguments from page images. `pimenova-1979.md:5–7,14–18,29`, response supplement99–102 and report128 consistently record developer's corrected n(x±y)/2 arguments and retain p54/Theorems2–3 OCR-only limitation. Accept only as developer-checked source record; no Padua implication asserted.

4. **Kuznetsova1995**: UMJ archive failed via browsing; AC-local Springer copy was not exposed by available tools. Record `kuznetsova-1995.md:5–7,13–18` and response103 honestly distinguish developer rerender from independent audit; formulas retain torus setting/no Padua symmetrisation. No independent theorem-page verification here. Original audit's primary-coverage limits remain, supplemented by developer's rerender.

5. **MathSciNet itself**: AC queries and reviews were not independently accessible; counts and triage remain reported AC/developer checks, with no independently repeated citation-index search. The note line33 adequately discloses incompleteness/nonexhaustiveness once finding line8 is repaired. Title-only and review-only triage stays qualified at lines15–19,27–28; Carnicer–Godés fulltext remains unread and is not excluded by a fulltext theorem check.

## Registry/rules/reading provenance

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, handoffs05/08, audit-01 and audit-support/p1, response-01 (especially F1 and supplement), relevant P1 memo/report/results, all three new/modified P1 source records and MathSciNet note. Existing full890-line IDEAS team read is recorded in audit-01 and inherited, not falsely claimed as a fresh personal read. Newly appended IDEAS891–974 read in separate outputs, including PR19 obstruction table, T2–T4, signed-MZ and NN-MOP scopes; relevant existing IDEA206 and286–289 rows re-read. They change no source inference or PD status in this task. INDEX introduction and relevant LIT377/379/388/379 addenda reviewed; original full-index history not independently repeated. No ideas generated, no IDs assigned.

Searches actually executed: KL–Liflyand DOI/title/PDF/rational-gloss searches; Padua2DM title/PDF search; primary-author links followed above. These were source-discovery checks, not a new exhaustive priority search. Existing audit01 bounded negative searches remain the historical evidence; no new paper was found here changing P1 verdicts. No mathematical test was appropriate to these attribution edits and none was executed.
