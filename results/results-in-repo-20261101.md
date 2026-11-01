# results-in-repo-20261101 — repository-only results tracking (PR #16)

This topic results file is written only by the topic orchestrator. Branch `claude/results-in-repo-20261101`, draft PR #16.

**Source trail:** [log](../topics/results-in-repo-20261101/LOG.md), [Codex audit-01](../topics/results-in-repo-20261101/audit-01.md), [response-01](../topics/results-in-repo-20261101/response-01.md), and the rule itself in [agents/WORKFLOW.md](../agents/WORKFLOW.md) (Computation and evidence).

## Outcome (2026-11-01)

- **Rule (accepted by Codex audit-01).**
  - Results tracking is repository-only.
  - Each topic keeps `results/<topic-slug>.md`, written by its own orchestrator on its branch.
  - The root `RESULTS.md` is the merged view, with one section per topic, which each topic updates in its own PR at PR preparation.
  - All agent work must be possible from a cloud session. AC's machine is needed only for unfetchable papers and cold storage.
- **Migrated.** PR #14's results file is now [results/padua-mz-2d-20261101.md](padua-mz-2d-20261101.md), corrected in response-01 (audit F1–F3).
- **Not in scope.** No science, IDs or registries changed (no range). Other topics' local results files were not migrated.

## Next step

AC's readiness and merge decision on PR #16. After the merge, each topic records its results in the repository.
