# Audit 01 — local working-track rule

- Date: 2026-11-01.
- Auditor: Codex, independent of Claude's development. Requested audit configuration: `gpt-6-astra`, medium; independent runtime model/effort telemetry is not exposed.
- Audited candidate and rules read: `9b651b42f2ff2c9db8fd5b12a526e981045e4d19`.
- Base: `0d058fb410166bd97b178be57910f2d256d0b529`; GitHub's main-branch read confirmed that SHA during this audit.
- Scope: the local-results protocol amendment in `agents/WORKFLOW.md:85`, its topic log, consistency with the existing workflow, and PR bookkeeping.
- Verdict: **ACCEPTED within this scope. No unresolved findings. Stage PR.** Only AC decides and performs the merge.

## Coverage and provenance

Read in full at the candidate: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, `templates/TOPIC_LOG.md`, `topics/README.md`, and `topics/results-track-rule-20261101/LOG.md`. Also read the base version of `agents/WORKFLOW.md`, the full two-file PR patch, candidate commit/tree metadata, base comparison, and PR description/discussion (no comments returned).

This is a protocol audit with no scientific claims, proposed mechanisms, literature comparisons, IDs, or novelty assertions. The scientific novelty gate and full substantive read of `state/IDEAS.md` do not apply. No mathematical or computational result is accepted or upgraded by this audit.

The existing cloud clone was at `07c5f5465d6de306aa81dbe8ca1f615295163864`. Its attempted `git fetch origin main claude/results-track-rule-20261101` failed because the configured proxy was unreachable. No conclusion uses that stale checkout. The GitHub connector supplied the pinned files, which were staged outside the clone at `/tmp/padua-pr8-audit-9b651b4`, preserving repository paths under `head/` and `base/`. Complete fetched source-file list and verified Git blob identities:

| Revision | File | Git blob |
| --- | --- | --- |
| candidate | `AGENTS.md` | `8c94c718629649c3f5c89d05e5b674ae5ad3a99c` |
| candidate | `agents/WORKFLOW.md` | `ae7caab0a1a393188399615e27660e7be6cf0511` |
| candidate | `agents/codex/CODEX.md` | `16a4ecfea89acd5b1d9cd09c9213094bce144caf` |
| candidate | `templates/TOPIC_LOG.md` | `37e276cc4a1cd6af3f1d84e284fa3e930d6a0818` |
| candidate | `topics/README.md` | `c2943f50cee42df8380f499ca29d2195ab69afb7` |
| candidate | `topics/results-track-rule-20261101/LOG.md` | `7feb13c7562699c5c572032802f3728ec582791e` |
| base | `agents/WORKFLOW.md` | `1e3399cc4089c3784f017cf9ec0927bc695ef99c` |

## Checks actually performed

GitHub's compare endpoint confirmed one commit above the current main, changing only `agents/WORKFLOW.md` (+2/-0) and the new topic log (+32/-0). There is no scientific, registry, template, executable, or other rule-file change.

A separate Python standard-library inspection computed each fetched file's Git blob SHA-1 from its actual bytes and compared all seven with the pinned identities above. All matched. It also verified that removing the single added paragraph reproduces the base workflow exactly and that the log quotes the amendment exactly. All assertions passed.

`git diff --no-index --check /tmp/padua-pr8-audit-9b651b4/base/agents/WORKFLOW.md /tmp/padua-pr8-audit-9b651b4/head/agents/WORKFLOW.md` produced no whitespace diagnostics (exit 1 with differing no-index inputs). These are source/provenance inspections, not an executed concurrency test or scientific rerun.

## Protocol assessment

1. **Ownership and preservation:** topic files have a single authorized orchestrator, while a shared-file writer may change only its topic's section. Rebuilding the whole shared file from an old snapshot is expressly forbidden. This addresses the overwrite behavior reported in the log.
2. **Concurrent publication:** the required sequence is to stage current shared bytes, merge the topic section into those bytes, and submit a modification-time-guarded write. If another topic publishes first and the guard rejects the write, the writer must restage and remerge; retrying the stale full-file payload or forcing it is not permitted. This is a coherent protocol, assuming the host's guard correctly detects intervening writes.
3. **Publication timing and recovery:** shared-view updates are limited to PR preparation or after AC merges the topic's PR. The per-topic source survives a lost shared section and supplies its recovery content. This does not authorize restoring unrelated sections or undoing newer shared-file changes.
4. **Existing obligations:** the amendment leaves the repository's scientific records, evidence/provenance requirements, audit separation, Git permissions, and AC-only merge authority intact. Its explicit location is outside Git, and private/third-party local material remains outside Git.

No blocking or nonblocking correction to the amendment is required. The delivery updates only this audit record, the topic's stage/history and index entry, and PR presentation; it does not silently repair the developer's rule text.

## Limits and handoff

AC's Windows files, existing section boundaries, the claimed incident/restoration, and the reported programme-ideas migration were not accessible here and were not independently verified. No local `RESULTS.md` or per-topic results file was read or changed. The audit does not certify the host guard's atomicity, filesystem timestamp behavior, or a completed rollout. If an executor lacks the required guard, or a topic cannot identify its owned section, this rule supplies no permission to bypass the guard or overwrite ambiguous content.

The source text is accepted as a protocol requirement, not as proof that every existing writer or filesystem already implements it. No additional run is required for acceptance of this documentation-only amendment. Material rule changes require a fresh audit. No developer response is required when there are no findings. Retain AC's final merge decision.

Next prompt: `Codex (gpt-6-astra medium): After AC merges PR #8, verify the merged rule and record completion.`
