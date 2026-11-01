# PR #13 final preparation

**Ready for AC's merge decision after accepted focused audit-02. Assigned agent preparation is complete; only AC merges.**

## Inputs and authority

- Topic: `claude/handoff-id-rules-20261101`.
- Original main: `21e620ba8b5f0e0706f3a8c6613517df04d9d469`.
- Current base: `a7e123476cef761807c69e5d0af1a094c7ac3df0`, AC's squash merge of PR #6 source `b46b4dea18ce2c933489a211b0b6819dfd32ca70`.
- Claude response: `7e9504b12610682e57c57dce9ac9fd2d37dfe9a7`; published `ac4ff3fd32d73880048e38d096bbcfb58df8a724`.
- Main integration: `fcb334c7f0ef055695b8f2633692092865366ddb`, a normal two-parent merge, no conflicts. No live main write, force push or rebase.
- AC requested Codex to finalize this PR and integrate merged #6. Handoff 04 replaces handoff 03's separate Claude preparation request. Requested allocation: gpt-6-astra medium; resolved runtime metadata unexposed.

## Final scope and audit

PR #13 adds fresh-range reservation rules and immutable numbered handoffs, with the no-audit, redirection and terminal-completion cases spelled out. Permanent retired reservations, collision priority, old-owner supersession and transition timing are explicit. Claude response-01 resolves F1–F4; [audit-02](audit-02.md) independently accepts them.

The only differences from current main are `AGENTS.md`, `agents/WORKFLOW.md`, `templates/HANDOFF.md`, `templates/TOPIC_LOG.md` and this topic's administrative records. The rule content is the accepted Claude response plus main's exact Fable amendment. No scientific records, statuses, registry schemas, allocations, global state, ledger, other-topic files or .github files differ from main. The shared frontier therefore remains current without an administrative-only state rewrite.

## Current transition

Merged main keeps the lattice and programme blocks through PD-T100, PD-N043, IDEA-209, LIT-426. #11 keeps LIT-293–299. #9/#12 adopt the new procedure on next continuation within AC's ownership restrictions; no change to their branches is performed here. No closed, unmerged PR was found in the refreshed snapshot. This topic needs **no range**. Record-level details and limits are in audit-02; no retrospective headroom or renumbering is performed.

AC's recorded integration order is now #13 → #11 → #9 → #12. This preparation certifies only #13 against current main. It does not clear #11's literature findings or #12's stale-branch conflicts, and it does not reapply those branches' old registry copies.

## Verification and reproduction

Executed full changed-path comparisons against main, exact response rule/template comparisons, exact inherited Fable-block recovery, earlier report/handoff-body preservation and handoff status checks. `git diff --check` passes. The initial Fable normalization checker was corrected to retain its separator newline; no repository repair was needed.

Disposable local squash rehearsal:

```sh
git worktree add --quiet -b codex/pr13-final-rehearsal-20261101 /tmp/padua-pr13-final-rehearsal a7e123476cef761807c69e5d0af1a094c7ac3df0
git -C /tmp/padua-pr13-final-rehearsal merge --squash --no-commit claude/handoff-id-rules-20261101
git -C /tmp/padua-pr13-final-rehearsal write-tree
git rev-parse HEAD^{tree}
```

At checked source `c544dfb783446f23d5f76b0577f235da6f58a6a7`, both trees were `2e79950f1190a40d28d6575fca3553932f2f42bb`. No conflict occurred. The disposable branch does not modify main; final metadata delivery is checked for the same tree equality before publication. Actual final head/tree are recorded in the PR body to avoid self-referential hashes.

No scientific rerun is needed because every scientific file matches main. No computer-proof, literature-clearance, cold-storage-delivery or future-branch readiness claim is added.

## Completion

Commit audit/preparation outputs, then close handoff 04 in a following commit naming that real output SHA. Preserve all old instruction bodies, leave zero open handoffs because no assigned agent work remains, push the topic, update the PR body and mark PR #13 ready for review. The human merge decision remains AC's.
