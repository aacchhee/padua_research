# Handoff 07 — readiness check of PR35 (response diff, final IDs, registries, reservation)

- Status: open
- Previous handoff: [06-response-and-preparation.md](06-response-and-preparation.md), done in the output commit below.
- Next agent / model / effort: **Codex, gpt-6-astra medium** (protocol and ordinary technical audit, WORKFLOW model table). Raise the effort only if the diff shows a material change; then follow the focused re-audit rule below.
- Branch: `claude/padua-mz-paper-20261113` · Draft PR #35.
- Input head SHA: `06e544dc9361de3a8c7e7495b43cb6603880b63e` (PR preparation). This handoff is published in a later commit.
- Main/base: `99a9b1d161e41a80c4fd425b63022c681fbe8779`, merged into the branch at `fa956de`.
- Stage: PR (readiness check). This is not a new audit round.
- Written by/date: Claude, claude-opus-5-5 (configured xhigh) · 2026-11-14.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head. The rules are unchanged since `c0e57a9`.
- [audit-01](../audit-01.md) and [response-01](../response-01.md).
- The LOG entries "response to audit-01" and "PR preparation".
- [ALLOCATIONS.md](../ALLOCATIONS.md) and [final-id-map.json](../pr-preparation/final-id-map.json).

## Task

1. **Response diff (F1–F5).** Review `git diff 303a564 a1a2949` on the two manuscripts, the two READMEs, the two correspondence files and the two theory records. Confirm that each finding is fixed as response-01 states, and that nothing else changed in any theorem, assumption, proof, bound, status or evidence. Confirm the frozen labels are unchanged: 104/104 CC aux labels (52 statement-type) and 56/56 SP. A clean build is optional. The developer's builds give PDF text byte-identical between `a1a2949` and `06e544d`, because the later commit changes TeX comments only.
2. **Main merge.** `fa956de` is a no-ff merge of main `99a9b1d`. Confirm it is conflict-free and adds nothing beyond main's changes.
3. **Reservation refresh (full union, WORKFLOW).**
   - Refresh main, every open PR (at writing: 27 and 35) and any closed-unmerged PR.
   - Re-read every ledger and the four ID registries.
   - Confirm that PD-T684–689 lies strictly above every other reservation and assigned ID. The union at reservation was T683, from the PR34 ledger; PD-T999 is a documented fixture.
   - Confirm that reservation commit `88824fb` was pushed and linked from the PR body before the assignments in `06e544d`.
   - Record the heads you checked.
4. **Registry application.** Review `git diff fa956de 06e544d -- PROOF_STATUS.md ID_CROSSWALK.md PAPER_MAP.md RESULTS.md state/CURRENT.md literature/`. Check:
   - the PD-T684/685 rows match the theory records' exact statements, statuses (including the computer-assisted PD-T547 dependency of PD-T684(b)'s numerical interval) and dependencies;
   - the crosswalk mapping is one-to-one, with gaps PD-T686–689;
   - the PAPER_MAP supporting-ID lists agree with the README scope tables;
   - the state/CURRENT edit removes only the stale "manuscript insert remains a proposal" clause;
   - the LIT-045 addendum claims only the published equations (7)–(8) reading recorded in the LOG (AC's message 2026-11-13), and the LIT-056 addendum is metadata only, with no invented reread.
5. **Disposition.** Write `topics/padua-mz-paper-20261113/readiness-01.md` with findings by severity.
   - **Material change found:** request a focused re-audit of that item only (WORKFLOW).
   - **MINOR findings only:** list them for the developer.
   - **Clean:** record readiness *of the agent work*.

## Unresolved item that blocks "ready" regardless of the check

The exact PD-T376 witness arrays and exact norm files (report §6.2) have **not** been retrieved or replayed. Both papers and READMEs now say so honestly. AC must either retrieve the package, so that its committed checkers can be replayed, or decide the publication scope of MZ-SP Prop 8.2. Until then, keep PR35 a **draft** and state this in the PR body. Do not regenerate witnesses, convert Prop 8.2 to a measured statement, or reopen PD-T376's accepted mathematics. If AC resolves it, a replay or scope edit is a material change and needs a focused check.

## Scope limits

- Writes allowed: `readiness-01.md`, audit-support for it, LOG, this handoff's closure and the next handoff, and PR body metadata.
- Do not edit the manuscripts, theory records, response-01 or audit-01.
- Do not touch `.github/`, settings, `main`, other branches or tags.
- Commits are authored by Andrey Chesnokov <aacchhee@gmail.com>, with Agent/Model trailers.
- Only AC merges.
- Companions remain deferred until AC confirms the frozen texts (BRIEF §5 item 3).

## Acceptance and outputs

- readiness-01.md, with the heads checked and a disposition for each of tasks 1–4.
- Updated PR body: WORK, AUDIT and PR sections, with the PD-T376 obligation explicit.
- Close this handoff in a following commit with the output SHA, and add the next numbered handoff. Leave exactly one open handoff.
