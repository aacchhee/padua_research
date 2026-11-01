# Supplementary literature, novelty-record and retention audit

- Auditor: independent Codex subagent `audit_literature`; requested model/effort `gpt-6-astra xhigh`; runtime does not expose an independent model/effort receipt.
- Candidate/rules SHA: `614709d4a60fb0c2593b05764e8d5aceda1be381`.
- Current-main base supplied by root: `07c5f5465d6de306aa81dbe8ca1f615295163864`.
- Date: 2026-11-01.
- Scope: campaign retention, literature coverage labels, inspectable predecessor statements, novelty-screen provenance. No new idea, mathematical theorem or final-ID allocation is proposed.
- Independence: no developer file was edited. This report and `literature-check.py/json` are new audit artifacts only. Root alone owns Git.

## Finding L1 — make the actual campaign criteria and input revisions retrievable

**Major reproducibility gap, if no separate pinned handoff supplies these inputs.** `brief.md:5`, `gate.md:5` and `report.md:5–9` depend on `CAMPAIGN_CONTEXT.md`; the gate also depends on `BRANCH_SNAPSHOT_NOTE.md`. Neither file exists anywhere in the candidate tree. The baseline's `lit/baseline.md:7,16` transfers VERIFIED labels from files under `/home/claude/inputs/branches/records_lanczos/` without recording a source commit/blob or a content hash; the brief likewise cites whole parallel-branch snapshots and `RESULTS.md`, which are absent. The three supplied reports are retained with valid SHA256 entries, but they do not contain the missing five exact programme criteria or the referenced source-record revisions.

This prevents independent reconstruction of the precise acceptance/exclusion boundary and of the literature-verification transfer as it existed when generation/gating ran. A present-day branch name is insufficient provenance. Retain the campaign context and branch-snapshot note, or give an exact immutable, retrievable location; list the pinned branch/source revisions and required record paths. Preserve the baseline's limited labels rather than upgrading them. This does not establish that the underlying reading or gate execution failed.

## Finding L2 — the gate double-subtracts the two merges

**Minor factual correction.** `gate.md:112` says seven candidates, five single and two merged, but the following numbered list has nine already-merged candidates: M1, M2, gen2-3, gen1-2, gen1-3, gen3-1, gen3-3, gen4-1, gen4-2. Its final count paragraph subtracts the merges again. The actual flow is eleven original draft records becoming nine distinct adversarial candidates, comprising two merged candidates and seven singles; the remaining nine original drafts are six rejects and three deferrals. The mistaken seven-programme count repeats in `report.md:9,203` and the topic log. Correct the accounting while preserving historical verdicts. The final zero-programme outcome and the twenty retained records are unaffected.

## Finding L3 — source-review summaries need coverage-qualified wording

**Minor evidence-label correction; blocks blanket full-source verification only.** `report.md:67` defines F as either an agent reading full text or a WebFetch digest. `report.md:21` consequently describes five kills as each decided by a full text, although several source tables explicitly record abstracts, selected sections or summaries, and `proposal-1.md:33` still requests a full reading of Kolomoitsev–Lomako. The underlying tables often preserve the caveats correctly; the summary loses the distinction. Keep separate labels for primary pages directly inspected, a secondary tool digest, and a complete reading, naming unverified load-bearing statements. The source spot checks below support several exact statements; they do not independently verify every claim in those sources or clear novelty exhaustively.

## Checks and accepted record-level facts

The full `state/IDEAS.md`, all its obstruction/disposition tables, and `literature/INDEX.md` were read before the novelty/source review. The rules, campaign brief, gate, retained-candidate narrative, candidate records, baseline, its three detailed records, report, proposal and relevant gen4-2 adversarial source table were inspected. Mechanism searches included commuting extension, border basis/rim chart, rational/Sobolev, constrained equilibrium/saturation, Lebesgue/Fekete, trajectory and spectral methods. Relevant accepted registry entries include IDEA-014/020/021/024/027/028/030/034/039/047/048/051 and the MZ obstruction table; the campaign preserves their exclusion/overlap reasons rather than silently replacing them.

The executed command was:

```text
python topics/programme-ideas-20261031/audit-support/literature-check.py /workspace/programme-integration > topics/programme-ideas-20261031/audit-support/literature-check.json
```

It completed successfully and checked:

- 111 unique literature row IDs, exactly provisional 01–111; the labels count 41 VERIFIED and 70 UNVERIFIED, agreeing with the log. VERIFIED is explicitly defined at statement/locator level in `lit/baseline.md:15–16`, so those 41 are not forty-one complete paper readings.
- Twenty unique IDEA headings, exactly provisional 01–20. The two appended records 03/17 are present. All twenty original draft titles, statuses and SHA256 identities were recovered by read-only `git show` from immutable historical commit `25161235fe430ec05723796afe0f20a923a69ebd`; twelve are returned and eight not returned. Removing `checks/state/` from the current tree did not erase this historical evidence.
- All three archived report files match `sources/SHA256SUMS.txt`. No manuscript/PDF was inferred to be locally available merely because a developer path named it.
- Final-ID allocation and shared-literature integration remain explicitly deferred to PR preparation; no collision is established by these provisional namespaces.

This was an actual independent record check, not a mathematical rerun. The script's source and result are durable siblings of this report.

## Independently inspected primary-source excerpts

Web access succeeded for the following narrowly scoped checks on 2026-11-01; URLs are version-pinned arXiv HTML. No PDF was opened or copied and no external message was sent.

1. [Kolomoitsev–Lomako, arXiv 2009.07114v1](https://arxiv.org/html/2009.07114v1), §2.1 Theorem 2.1 and §2.2 equations (2.3)–(2.6): the displayed Padua specialization has coefficient `4/pi²` and an `O(log n)` remainder; the rhombus Fourier projection has coefficient `16/pi⁴` for equal axis degrees. These support the recorded leading-term predecessor and the obstruction to the specified projection-constant route. They do not refute a universal interpolation lower bound by another mechanism, identify a second-order term, or prove the campaign's corner-maximum claim. Coverage: those statements and immediate surrounding definitions only.
2. [Białas-Cież–De Marchi–Suder, arXiv 2605.23299v1](https://arxiv.org/html/2605.23299v1), §3.3 Table 3, Remark 2 and §4: the source's Padua totals are `15,27,25,39,42,56` at degrees 3–8, and the remark discusses additional maxima near zero curves of a fundamental polynomial. The source presents numerical observations and an open counting question. This independently supports the attributed table and crease-neighbourhood motivation; it provides no validation of the campaign's replacement counts or counting certificate. Coverage: those sections/excerpts only, no figure inspection or complete reading.
3. [Kreuzer–Robbiano, arXiv 2503.01752v1](https://arxiv.org/html/2503.01752v1), §5 Propositions 5.4–5.6: interior coordinates can be eliminated and the planar simplicial border-basis scheme is an affine cell of dimension `(d+1)(d+2)=2N`. This supports the algebraic predecessor claimed for M2's ideal-coordinate chart. It does not independently establish the orthonormal-coordinate transcription, stability or the campaign's dimension proof. Coverage: displayed propositions and adjacent explanations only.

## Limits and disposition

No exhaustive citation search, current ownership certification, or full independent check of the other source assertions was performed. The three local detailed literature records clearly retain their limited page coverage; their original PDFs were not present in this snapshot and were not independently rendered. Claims inherited from unavailable notes or parallel-branch records remain inherited reports until pinned evidence is supplied. The narrower primary checks above can be cited without upgrading those other rows.

Candidate coverage and provisional-ID discipline pass within this scope. L1 needs a concrete source-provenance response, L2 needs count corrections, and L3 needs coverage-qualified summaries. Numerical certification, negative mathematical scopes and substantive theory registration are owned by the other audit components; this report does not approve them.
