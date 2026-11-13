# Handoff 04 — padua-mz-paper-20261113 — finish MZ-CC (notation, literature, referee, freeze), then MZ-SP

- Status: open
- Previous handoff: [03-work.md](03-work.md), superseded at the session boundary. AC's answers recorded there are repeated below. [01-work.md](01-work.md)'s task list and gates remain the reference.

- Next agent / model / effort: **Claude**, a new session.
  - Orchestrator and mathematical writing: Opus 5.5 xhigh.
  - LaTeX mechanics, build and tooling: Sonnet 5.5 high. Mechanical edits: Sonnet 5.5 medium.
  - Internal referee reviews: separate Opus 5.5 instances (high or xhigh) that did not write the section they review.
- Role: orchestrator and developer (manuscripts)
- Branch: claude/padua-mz-paper-20261113 · Draft PR #35
- Input head SHA: `27347e8` (the commit that publishes this file comes later)
- Main / base: `b5388c2`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-13

## State at handoff

Read the [LOG](../LOG.md) entries of 2026-11-13 first.

- **Done:** tasks 0, 0a, 1 and 2 (with reviews and dispositions); journal classes.
- **MZ-CC is complete to draft** (`tracks/mz-constants/paper/manuscript.tex`, 30 siamart pp., clean build):
  - every result of plan-cc, with proofs (Appendices A–C);
  - title, abstract and introduction with Thms 1.1–1.3 and Cor 1.4;
  - §9 measurements and open problems; data and code availability with placeholders.
  - Statement numbering is a freeze candidate.
  - Still to do: the notation pass ([notation-cc.md](../notation-cc.md): apply the H and M renames and fix the forward uses: κ₂ undefined, u_k at l.141, 𝓛_n/E_k(f) in §1), the literature scope check ([literature-mz-paper.md](../literature-mz-paper.md)), and the internal referee round. After that MZ-CC is frozen.
- **MZ-SP** (`tracks/mz-constants/paper-sp/manuscript.tex`, 15 pp., clean): post-split text in `elsarticle`. Nothing is integrated yet.
- **Provisional claims:**
  - PD-T?mz-paper-claude-01 ([record](../theory/cc-defect-condition-corollary.md)): all four parts checked independently (PASS, corrections applied);
  - PD-T?mz-paper-claude-02 ([record](../theory/sp-corner-norm-lower.md)): checked (PASS).
  Both are flagged for the Codex audit. Checks: [check-cc-defect-corollary.md](../check-cc-defect-corollary.md), [check-new-corollaries-02.md](../check-new-corollaries-02.md).
- **Tools:** [tools/build.sh](../tools/build.sh) `<paper-dir> <scratch-out-dir>`. The sandbox needs `texlive-publishers` for `elsarticle`. Avoid `\S` in siamart text: it pulls in a bitmap TS1 font and breaks microtype font expansion.

## Task, in order

1. **Finish MZ-CC:**
   1. notation pass per notation-cc.md: H and M entries, forward uses, κ₂ definition; keep notation-cc.md as the register;
   2. literature scope check per citation (literature-mz-paper.md; task 5), resolving any remaining pre-PR #21 hedge;
   3. internal referee round (task 8): two distinct Opus reviewers (mathematics; exposition and notation), answered in `response-internal-cc.md`;
   4. **freeze MZ-CC** and record its statement numbers in correspondence-cc.md.
2. **MZ-SP integration**, per plan-sp and its dispositions:
   1. notation-sp.md first (F12);
   2. short CC recap citing MZ-CC (AC: MZ-CC first, MZ-SP cites; no reproduced λ₊<2 proof), plus the F1 weight facts proved or cited;
   3. density-lemma attribution (F11);
   4. PD-T533/537 in §5;
   5. §6 corner operator: PD-T534/535/536/539/540/541/542 with Appendices A–B, the corollary PD-T?mz-paper-claude-02 (F7) and the F8 remark;
   6. §7 with the reproduction remark (PD-N051);
   7. §8 finite results (PD-T107 if its scope fits; F9 labels; Prop 8.1 with the Zenodo placeholder);
   8. §9 open problems;
   9. title, abstract and introduction; remove process language (F6) and in-heading IDs;
   10. data and code availability (checkers for PD-T298/299/376/541/542).
3. **Tasks 5–7 for MZ-SP** (literature, notation, availability), then its internal referee round (task 8).
4. **Task 9:**
   - final builds, and an independent rebuild by a different subagent;
   - M7 manuscript-record append, README scope tables for both papers, `report.md`, results file;
   - the list of files for AC's Zenodo deposit;
   - PAPER_MAP/state/CURRENT.md diffs for PR preparation;
   - a final-ID reservation for the two provisional claims, by the WORKFLOW reservation procedure.
5. **Companions** (BRIEF §5 item 3), only after each paper's freeze. They may go to a later handoff.

Push at every task boundary. When development is complete, open the next handoff for the single substantive Codex audit (gpt-6-astra high or higher). It covers the correspondence, both provisional claims, the PD-T523 proof-route change (correspondence-cc changes log), exposition, citations and builds.

## AC's answers (2026-11-13, 21:28)

AC: "1. mz-cc first, mz-sp cites. 2. I guess they go to zenodo".

- **MZ-SP's dependence on MZ-CC** (plan-sp F2): MZ-CC goes out first (arXiv), and MZ-SP **cites** it for the CC inputs, including λ₊<2 (PD-T014/022). Do **not** reproduce the λ₊<2 proof in MZ-SP. Keep the recap short and cite stable MZ-CC labels after the MZ-CC freeze. The F1 CC-weight lemma may still be proved inside MZ-SP if that is shorter than a precise citation; otherwise cite it too. In MZ-SP's introduction, state plainly that the CC inputs are proved in MZ-CC.
- **PD-T376 witness arrays** (plan-sp F13): they go into AC's planned Zenodo deposit. Keep Prop 8.1 in MZ-SP, and point its availability statement at the deposit-DOI placeholder. List the exact files the deposit needs (arrays, exact norm files, checker inputs, with hashes from the existing cold-storage manifests) for AC in report.md. Agents create no deposit.
- For information: MZ-CC is about 37–42 SIAM pages including appendices (plan-cc M3).

## Read first

AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the branch head; BRIEF.md; the LOG; plan-cc.md and plan-sp.md with the reviews and dispositions; correspondence-cc.md and correspondence-sp.md (including the changes log); split-map.md; the theory records named above.

## Scope limits

As handoff 01: write only in this topic directory, `results/padua-mz-paper-20261113.md`, both paper directories and the M7 record (append only). Shared registries only at PR preparation. Do not write to other open branches (PR #27, PR #34). Never strengthen a statement silently: any new mathematical statement gets a provisional record and an independent check, and is flagged for the audit. No PDFs or bulk data in Git. AI declaration, ORCID, contributions, funding, cover letter, venue, submission and deposits are reserved to AC. Commits are authored by Andrey Chesnokov <aacchhee@gmail.com>, with Agent/Model trailers. Only AC merges.

## Acceptance and outputs

As handoff 01, *Acceptance and outputs*, and gates W1–W4. Reply to AC only with the `Continue` prompt for the next step.
