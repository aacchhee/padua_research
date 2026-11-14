# Handoff 05 — substantive audit of the MZ-CC and MZ-SP manuscripts

- Status: done in f9bf997447922645bba9f411d470e0d1ec4d82ce
- Previous handoff: [04-work.md](04-work.md)
- Next agent / model / effort: **Codex, gpt-6-astra, high or higher**. Supplementary subagent checks are welcome; they do not replace this audit.
- Role: independent substantive auditor. Claude developed this topic (handoffs 01–04); Codex audits. This is the single substantive audit of the topic.
- Branch: claude/padua-mz-paper-20261113 · Draft PR #35
- Input head SHA: `a03a4f7` (the output commit; this handoff is published in a later commit)
- Base main: `b5388c2`. Rules were read at `c0e57a9` and are unchanged on this branch. Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head before acting.
- Stage: AUDIT
- Written by / date: Claude, claude-opus-5-5 (configured xhigh; effort not exposed) · 2026-11-14

## Objective

Audit the two manuscripts produced from the single 2026-11-05 MZ draft, which AC split on 2026-11-13:
- **MZ-CC:** `tracks/mz-constants/paper/` (SIAM J. Numer. Anal., `siamart251216`, 32 pp.);
- **MZ-SP:** `tracks/mz-constants/paper-sp/` (J. Approx. Theory, `elsarticle`, 50 pp.).

Both are complete internal drafts with frozen statement numbering. Read first:
- [report.md](../report.md), [LOG](../LOG.md), [BRIEF](../BRIEF.md);
- [split-map.md](../split-map.md);
- [correspondence-cc.md](../correspondence-cc.md) and [correspondence-sp.md](../correspondence-sp.md), including their changes logs and frozen-numbering tables;
- the plans with their review dispositions;
- the two internal referee rounds per paper with their responses: [referee-cc-math](../referee-cc-math.md), [referee-cc-exposition](../referee-cc-exposition.md), [response-internal-cc](../response-internal-cc.md), [referee-sp-math](../referee-sp-math.md), [referee-sp-exposition](../referee-sp-exposition.md), [response-internal-sp](../response-internal-sp.md);
- [notation-cc](../notation-cc.md), [notation-sp](../notation-sp.md), [literature-mz-paper](../literature-mz-paper.md).

## What to audit

1. **Mathematics-to-text correspondence (gate W1).** For every numbered statement, check that it matches its record's scope (records under `topics/padua-mz-sharp-constants-20261106/theory/`, `topics/padua-mz-cleanup-20261105/theory/`, `tracks/mz-constants/theory/`). No PROVED result may be strengthened, and no OPEN or MEASURED item may appear as proved. Every stated result must be proved in its paper. Known departures, which must each be judged:
   - **MZ-CC:**
     - PD-T529 is stated weakened (qualitative fixed-J limits).
     - PD-T531 is omitted.
     - The proof of PD-T523 takes a different route: through Lemma A.1(c), built on PD-T544, instead of the record's pointwise (D).
     - The new Lemma 2.4 (a weighted Schur test) is used three times.
     - §3 is reordered: Thm 3.1, then Cor 3.2 (which merges the old Thm 3.1), then Thm 3.3 (the 5/3 bound).
     - The phrase "we do not claim 5/3 is optimal" is used; the 23/15 strengthening was declined.
   - **MZ-SP:**
     - PD-T539 is weakened (the log-singularity sentence is dropped).
     - The proof of PD-T534 tracks its constants more tightly, but the statement keeps the record's constants.
     - Record steps are tightened in PD-T535 and PD-T536 (m ≥ 2K; Lemma A.4 made explicit).
     - Remark 7.2 adds the bound (2+C_P)E_k(f).
     - Prop 8.1 adds "η<0.83" and merges PD-T107/298/299.
     - The fixed-(a,b) bounds of PD-T379 are now stated.
     - The CC-weight lemma is proved inside MZ-SP. MZ-SP cites MZ-CC Cor 3.2, Thm 4.3 and Prop 8.1 (AC: MZ-CC goes first, MZ-SP cites).
2. **Two new provisional claims.** Reconstruct both independently:
   - PD-T?mz-paper-claude-01 ([theory/cc-defect-condition-corollary.md](../theory/cc-defect-condition-corollary.md)): the N≥57 identity, the defect and condition-number limits, the interpolation norm, and the hyperinterpolation factor.
   - PD-T?mz-paper-claude-02 ([theory/sp-corner-norm-lower.md](../theory/sp-corner-norm-lower.md)).

   Two independent Claude subagent checks exist: [check-cc-defect-corollary](../check-cc-defect-corollary.md) and [check-new-corollaries-02](../check-new-corollaries-02.md).
3. **Proofs translated into the papers.** Both math referees (Opus 5.5 xhigh) found no CRITICAL or MAJOR issue. Sample the long appendices critically: MZ-CC Appendices A–C, MZ-SP Appendices A–B.
4. **Computer-assisted statements.** Rerun what is cheap, and compare with the committed receipts and with the decimals as printed in the papers:
   - MZ-CC Prop 5.3 (`code/P4_rayleigh.py`, `code/P4_check_grouped.py` in `topics/padua-mz-sharp-constants-20261106/`);
   - MZ-SP Props 6.8–6.9 (`code/P1_rectangle.py --N 16 --theta 256`);
   - Prop 8.1 (the certificate receipts);
   - Prop 8.2 (the witness receipts; the witness arrays are not in Git, see report §6.2).
5. **Exposition and literature (gate W3).** Check:
   - every `\cite` against the LIT record coverage;
   - that no repository or process language is visible in the PDFs;
   - abstract and introduction claims against the theorems;
   - the computer-assisted labels.
6. **Builds and records (gates W2, W4).**
   - Run clean builds of both papers. An independent rebuild at `a0206a8` gave MZ-CC 32 pp. and MZ-SP 50 pp., with zero warnings and no Type 3 fonts.
   - Check the README scope tables, the M7 manuscript-record append, the availability statements (exact checker paths; DOI and commit placeholders), and the Zenodo file list in report §6.

## Rules for the audit

Write the audit report as `topics/padua-mz-paper-20261113/audit-01.md`, with findings numbered and given severities, and say what was verified and how. Do not edit the manuscripts or the development records. Preserve disagreements for AC. Do not assign final IDs or touch shared registries; that happens at PR preparation, after the response. Do not touch PR #27 or PR #34. Commits are authored by Andrey Chesnokov <aacchhee@gmail.com>, with Agent/Model trailers. Only AC merges.

## After the audit

Write the next handoff for Claude: response and PR preparation. That covers the response to the audit, final-ID reservation for the two provisional claims by the WORKFLOW procedure, shared registries (PROOF_STATUS, PAPER_MAP, state/CURRENT.md, the LIT-045 and LIT-056 record notes), replacing provisional IDs in TeX comments, and readiness. The companions (BRIEF §5 item 3) may follow as a separate Claude task, after AC confirms the frozen texts.
