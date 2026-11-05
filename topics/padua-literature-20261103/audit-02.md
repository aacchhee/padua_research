# Audit 02 — response 01 and handoff 08 supplements

- Auditor/orchestrator: Codex, 2026-11-05. User-requested configuration `gpt-6-astra high`; serving identity and effective effort are not independently exposed. Two bounded readers inherited this configuration. A third supplementary worker failed at model capacity and performed no review; the orchestrator checked F4–F6 directly.
- Rules read at `0b5fb2d4414af02af23c653cba9cd16e38c1cb8c`: AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, unchanged from audit01. Role: independent auditor of Claude development.
- Scientific input: `10aa5d31e3be477b90f44c122ade0c6180c9a252`; handoff head: `0b5fb2d4414af02af23c653cba9cd16e38c1cb8c`. Current main `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7` is an ancestor, merged as `77f5db2578dd228298bb619d96fa526c07112366`.
- **Disposition: original F1–F6 resolved within the scope below; one new P2 finding F7 requires response. Stage WORK; PR stays draft.** No PD status, source verdict, IDEA or final ID is changed by this audit.

## F7 — P2: a zero MathSciNet count does not establish publication absence

Location: `topics/padua-literature-20261103/notes/mathscinet-citation-check-2026-11-05.md:8`.

The note infers that nothing has been published citing De Marchi's open-problems list from AC's zero MathSciNet citation count. This index query supports only that no indexed citing item was returned by that query. It does not establish universal publication absence. The same note at line21 gives an explicit incompleteness example: Kuznetsova has zero indexed citers despite two checked citations. The later limitations do not repair the stronger sentence at line8.

Replace that inference with a bounded description, for example that AC's documented MathSciNet check returned no indexed citing item. Preserve attribution of the count to AC, the date, the search limits and the unchanged source verdicts. This needs no new mathematics or exhaustive search. The other title-only/review-only triage remains properly qualified; those sources have not thereby received full-text exclusion checks.

## Disposition of the six original findings

| Finding | Re-audit result and inspected propagation |
|---|---|
| F1 — corner attribution | **Resolved.** P1 comparison row37 and proposed wording51–52 separate the global-to-corner upper estimate from the corner lower search-negative. Report31–35/89–91 and topic results12/42 agree; the PR response summary makes the same split. The global coefficient4/π² is not claimed as new, and KL is no longer credited with the actual corner lower bound. No transfer proof was requested or supplied. |
| F2 — powered weight | **Resolved.** Mastroianni record20 restores `(u/√(wφ))^p∈A_p`, finite `1<p<∞` and positivity a.e.; proposed INDEX row1099 carries the powered condition. Fresh primary text of Theorem9 and its dual-weight proof independently corroborates the exponent. |
| F3 — rates | **Resolved.** Record10/16/28/40, P2 row34, report102–103 and proposed row1099 distinguish the missing borderline MZ-minimum decay estimate from the polynomial Sobolev/Besov approximation-error rates. The bounded RELATED verdict is retained. |
| F4 — Möller dimension | **Resolved as a transcription correction.** Dunkl–Xu addendum14 now has `dim Π²_(n−1)` with the original rank term and locator. This matches the separate primary survey evidence recorded in audit01. The claimed new book-page image check remains developer-verified. No copied incorrect display was found outside immutable historical audit text. |
| F5 — downdating scope | **Resolved.** P4 memo7 limits its absence statement to the nine inspected sources. QuestionC explicitly separates classical stored-Q/R-factor routes IDEA-094/095 and describes the proposed structured commuting-pair IEP extension. It remains an unregistered later-topic proposal requiring its own gate. Its feasibility is not established by this literature audit. |
| F6 — Laurie awareness | **Resolved.** Faghih addendum11–14 keeps both the author-limited introduction statement and the §7 proposal, without a nonexistence inference. Proposed blocks117/187/320–323 agree. Assessment32 retains the old statement as history with an explicit dated reversal. The preprint introduction corroboration from audit01 stands; the claimed published-page check is developer-verified. |

The response has answered every original finding rather than editing the auditor's report. Existing audit01/support files remain immutable historical coverage; their earlier findings and access limits are not silently rewritten into new verification.

## Bounded source acceptance and remaining uncertainty

Detailed actual accesses and source URLs are in [P1 re-audit](audit-support/reaudit-p1.md) and [P2/source re-audit](audit-support/reaudit-sources.md).

- **Fresh independent corroboration:** Mastroianni–Russo author-PDF text confirms the repaired Theorem9 hypothesis and Theorem11 construction; its CC specialization and excluded A2 endpoint are consistent. De Marchi's published PDF is now accessible in text: printedp23, §3.3(2), confirms the corners observation. This corroborates an observation, not a proof of corner attainment.
- **Pimenova/Kuznetsova:** current records consistently describe Claude's corrected phase arguments and page-image readings. Pimenova OCR is accessible but too garbled to independently certify the constants; screenshot calls delivered only textual markers to the reader. Kuznetsova's actual theorem page was inaccessible. Accept these as developer-checked source records, not independent auditor image confirmations. They supply periodic/trigonometric context, not an unproved Padua-corner transfer.
- **Xu1996/SVZ:** the mandatory journalp231 comparison remains developer-verified only in this audit. The accessible Xu author preprint independently includes∞; the journal request returned403. Thus the asserted finite-p journal version is neither independently confirmed nor refuted here. SVZ author-preprint Table1 corroborates the reported row, while journal pp417/421 and images remain developer-verified. The audit does not promote those records into independent journal verification.
- **Running-head/Greenbaum/book obligations:** response01's source/locator checks remain developer-reported where primary copies are inaccessible. Greenbaum's original Theorem1′ statement reread remains optional and unperformed here. No AC-local paper access is claimed. No access controls were bypassed.
- **New Kolomoitsev–Liflyand record:** its accessible primary preprint confirms the Fourier-simplex operator-norm setting and RELATED, DIFFERENT SETTING verdict. It supplies no pointwise Padua corner theorem. AMS journal access failed; precise published normalization, journalp2914 and the rational/irrational remainder gloss remain developer-verified, with no demonstrated false transcription found. Do not count the preprint read as that journal check.
- **Padua2DM:** the author-hosted preprint directly confirms signed weights, few/small negatives and absolute-weight sum tending to4 credited to SVZ. Journalp54/p59 pagination remains developer-verified. The no-identification/formula remark is read specifically about which weights are negative, not a denial that general cubature weight formulas exist.
- **Citation index and Crossref:** MathSciNet counts/searches remain AC/developer-reported; they were not independently repeated through NTNU. The note's incompleteness, title/review-only triage and lack of GoogleScholar/zbMATH full-text searching are appropriate once F7 is fixed. The ten direct Crossref closures in response-01-checks.json are developer reports, not new auditor API executions. No DOI mismatch was established.

This is sufficient to accept the six repaired literary statements at their bounded scopes, while retaining the above developer-only verification qualifications. It is not exhaustive priority certification, independent verification of every page image, manuscript/submission approval or readiness. F7 remains the sole new actionable finding in this re-audit.

## Mechanics actually checked

1. **Exact input snapshot.** Retrieved93 branch files through the GitHub connector at one pinned head; original blob bytes checked. The list is in `check/audit-02-inputs.json`. No third-party source PDF or extracted text was committed. The full earlier890-line IDEAS team read remains the audit01 baseline; P1 reader fully read appended891–974 and relevant old entries. No new candidate generation occurred.
2. **Literal checker rerun against actual main.** Executed:

   ```sh
   python3 -I topics/padua-literature-20261103/check/audit_old_blocks.py --repo /workspace/scratch/padua-audit-objects.git --proposal topics/padua-literature-20261103/proposed-record-changes.md --base aff30e8ad5542c94fab642ae024dc9aab4fa7ad7
   ```

   Result: **60 Old blocks, zero missing**, multi-match lines47/72/1080. This verifies substring presence, not a full sequential application or correct selection of every append target. No proposal applied. Python3.12.14; checker SHA256 `427dd07918b569f21686f833ec25a1b4c41657bf83604998e18be26d11d46359`.

   The configured shell proxy remains unusable for ordinary Git fetch. To run the unchanged checker against the actual main SHA, an isolated bare object store used existing local objects plus pinned GitHub GET responses. Main's signed commit was reconstructed from its exact payload/signature, all3496 recursive tree entries were restored, and50 missing Markdown/Python/BibTeX blobs were fetched. Every restored object was checked against its real Git SHA, including commit `aff30e8` and tree `e0a45df07481733bfc2a832b33e5825fb0013606`; no synthetic ref, replacement object, working-branch edit or remote history change was used. A normal clone at the same main SHA can rerun the command with its own repo path. No numerical code changed, so the recorded independent SVZ run was not repeated.
3. **Main merge preservation.** Complete untruncated Git trees at `ca358a9` and `77f5db2` have identical topic-subtree identity, identical24 original new-source blobs and identical topic results blob:26 comparisons. Thus the main merge changed no topic-owned literature file. Current main is an ancestor of the audited head; unrelated merged registry changes are inherited context, not this topic's proposed edits.
4. **Reservation refresh.** Read/scanned57 registry/ledger copies (20 distinct blob contents) across main and open PR21/24/25/26. All returned closed PRs are merged. Qualified LIT mentions and permanent ledgers preserve this topic's482–561 range; later blocks562–573,574–581,582–593,594–597 are disjoint and PR26 reserves no LIT. No new range or final assignment. `check/audit-02-reservations.json` pins the scan. Repeat at preparation, including main's accepted same-source mappings.

## Next step

Claude should answer F7 in response-02.md with the bounded citation wording and keep the six prior corrections and all source-verification qualifications. No broader literature campaign is requested. Then return the narrow correction for a short independent check before PR preparation. Handoff09 contains the full instruction. Handoff08's final reference to opening07 is a numbering typo:07 already exists and is superseded, so the new file is09 under the immutable-handoff rule. Only AC merges.
