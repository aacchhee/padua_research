# Handoff 04 — padua-xu-lebesgue-20261114 — readiness check for PR #36

- Status: open
- Previous handoff: [03-response-pr-preparation.md](03-response-pr-preparation.md) (done; see its status line)

- Next agent / model / effort: **Claude, Opus 5.5, high**, an auditor **distinct from the developer**: a fresh thread, or a fresh subagent spawned by the orchestrator. Which one is AC's choice (handoff 03). If it is a subagent, the orchestrator only relays and commits its outputs, and the deviation is recorded as for audit-01.
- Role: independent readiness auditor
- Branch: `claude/padua-xu-lebesgue-20261114`, draft [PR #36](https://github.com/aacchhee/padua_research/pull/36)
- Input head SHA: `0e97396c3e16df5e83451544e1cbfae044c403a4` (the commit that publishes this file comes later)
- Main / base: `99a9b1d` (recheck `origin/main` and every open PR at start)
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 (orchestrator) · 2026-11-14

## Task

Write `topics/padua-xu-lebesgue-20261114/readiness-01.md`, following agents/WORKFLOW.md (PR procedure, "Proportionate audit and records", "Reserve fresh ranges" step 7). Check:

1. **MINOR-fix diff.** Review `git diff 8fdd039 80a744e` (response-01 and the audit-01 MINOR fixes). Confirm that every change is non-material: no Statement, quantifier, constant, status, dependency direction, code or evidence changed. Confirm that response-01 answers every audit-01 finding. Pay particular attention to the new self-contained cyclotomic proof in PD-T700 (X2-23) addendum §2. Check it as mathematics: it replaced an unverified textbook locator.
2. **Registry diff.** Review `git diff 80a744e 0e97396`: PROOF_STATUS.md, state/IDEAS.md, state/CURRENT.md, ID_CROSSWALK.md, RESULTS.md, literature/INDEX.md and records, the theory headers, the results file, ALLOCATIONS.md and pr-preparation/final-id-map.json. Check:
   - shared-registry edits are additive and correctly formatted (table pipe escaping);
   - the statuses match audit-01 §6 exactly;
   - the final-ID map is complete and consistent across all files, with no ID outside the reserved ranges;
   - the LIT coverage levels are honest;
   - existing LIT entries were extended rather than duplicated (Li–Sun–Xu = LIT-307/010/650);
   - links resolve.
3. **Reservation refresh** (step 7). Repeat the full union check against current heads: main, every open PR (drafts included), and closed-unmerged PRs. Record the heads checked and confirm there is no collision with PD-T690–719, PD-N251–257, IDEA-766–795 or LIT-721–745. Append the readiness refresh to ALLOCATIONS.md, in PR34's format.
4. **PR body.** Check that it carries WORK, AUDIT (audit-01 §8.1) and PR sections, the reservation link, and the decisions for AC.

## Read first

AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md at the branch head (record the SHA); audit-01.md; response-01.md; LOG.md; ALLOCATIONS.md; handoff 03; PR34's `topics/padua-effective-cubature-20261112/readiness-01.md` for format.

## Scope limits

- No new mathematics. Do not reopen audit-01's accepted verdicts unless the diff introduced a material change. If it did, report it and set the stage to AUDIT.
- Fix nothing in developer records. MINOR readiness defects go to the orchestrator via the report.
- No commits to main, merges, force-pushes, tags, or edits under `.github/`. Do not mark the PR ready for review yourself. The orchestrator does that only after a clean readiness check, and only AC merges.

## Acceptance and outputs

- `readiness-01.md` with a verdict (ready / not ready, with blocking items), the heads checked, and the reruns or diffs inspected.
- The readiness refresh appended to ALLOCATIONS.md.
- On "ready": the orchestrator updates the PR body's readiness line, marks PR #36 ready for review, sets the LOG stage line, and closes this handoff with `done in <sha>`. No further handoff is needed unless AC asks for X2 continuation or manuscripts.
