# PR22 preparation verification

Rules/input: f4c41acb665f4ea35b5db05ec45ae8ba34fe6b96, 2026-11-05.
Current base:21dbfc90257b952d8923f6d01739d12aa8d6e0a1, merged at4270d34.
Role: Codex orchestrator, user requested gpt-6.1-sol medium; exact runtime
backend/effort unexposed. No scientific work, code change, numerical run or
new novelty claim was performed in this preparation.

## Approved impact

- Final headers/aliases: T286–290,N100,IDEA376–379,LIT562–568, plus same-source
  reuse420/346/119/348. Complete mapping, provenance and permanent gaps in
  final-id-map.json and the topic ledger. Former provisional negative01
  remains withdrawn with no final ID, positive content mapped to T288/T289.
- E1 nonmonotone terminal diagnostic wording; E2 marginal-only versus shifted
  route and no C3 comparison; optional X1 cites auditor-executed exact
  references at sampled N4,8,12,16,24, with N32 precision convergence.
- Audit/process metadata now reflects accepted audit-01/02 and pending
  preparation protocol check. Scientific epistemic statuses are unchanged.
- Shared files are append-only topic sections, except the explicitly
  authorised IDEA117 resume/outcome row. Foreign sections, reservations and
  existing source IDs survive. This topic alone is copied into RESULTS.md.

## Mechanical commands and checks

Executed from repository root on the preparation worktree:

```sh
python topics/nn-mop-iep-20261103/preparation/check_registration.py
git diff --check
```

The registration checker verifies ten theory/negative/idea assignments, twelve
source aliases with seven new sources, unique new registry rows, complete
crosswalks, withdrawn-negative mapping, unchanged accepted proof/evidence
sections and executable/auditor bytes, preservation of shared base prefixes,
the one authorised IDEA117 row change, source anchors, literal RESULTS
copying, unchanged historical handoff instruction bodies and local links.
Initial checks while documentation was being assembled exposed missing
preparation links; these were completed before the final verification.
This is protocol checking, not a scientific test or independent audit.

## Reservation freshness

reservation-check.md/reservation-scan.json pin main and all open PR21/22/24,
35 full files/23 unique blobs, with union maxima T363/N131/IDEA453/LIT593.
All closed PRs returned are merged. The seven new LIT sources are absent
from current main and the pinned PR21 records; PR21 has no final assignments.
No provisional-number offsets or dependency on unmerged source files.

PR24 then advanced to79c3d6a. reservation-refresh.json reads all11 current
ledger/registry copies: every shared file equals current main byte-for-byte,
and its own reservation ledger is unchanged. Main21dbfc9 and PR21 890f56c
remain unchanged. No contested range or changed dedup conclusion.

## Review and integration limits

The optional gpt-6-astra medium supplementary integration check did not run
because the model returned a capacity error; integration-check.md records
that limitation. No substitute or independent approval is claimed.

Claude audit-02 already accepts the science. Handoff06 requests the separate
Claude protocol check of this preparation; PR22 remains draft until that
review and a current reservation/base check justify readiness. No readiness
for PR21/24 or AC merge order is inferred. Only AC merges.

The scoped local squash-rehearsal result is recorded below after the frozen
preparation checkpoint. Any later main change requires another impact check;
this receipt is not approval of a different base or unrelated branch.

## Completed final mechanical validation and squash rehearsal

The registration checker and `git diff --check` both passed. Its JSON reports
10 assignments,12 literature aliases,7 new sources, no final withdrawn-negative
ID, unchanged accepted proof/evidence sections and executable bytes. No science
was rerun. The temporary handoff06 draft existed for link checking; it was
excluded from the preparation checkpoint and its final input SHA is filled
only after the output commit, before publication.

[Squash receipt](squash-rehearsal.json) pins preparation checkpoint
fcb3a6af326a8a9540849fcdbe9a5c4f1b222d3c and main21dbfc9. In a detached
throwaway worktree, `git merge --squash --no-commit <PR22 checkpoint>` plus
`git write-tree` exactly matched its tree19c4370e4959f0e382973a1260650344ef1f7dcd.
After a disposable local squash commit, separately squashing current PR24
79c3d6a or PR21 890f56c completed without conflicts. Exact topic records/results
and all eight PR22 shared-registration sections were preserved in both trees.
The receipt records source/commit/tree identities. The worktree was reset and
removed; main, remote refs and other topic branches were not changed.

Rehearsal commands use `git worktree add --detach <temporary> <base>`,
`git -C <temporary> merge --squash --no-commit <head>`, `write-tree` and a
local disposable commit, then repeat each second-head squash from the same
base/PR22 checkpoint. Topic path diffs and literal shared-section comparisons
verify preservation. It is a scoped proposed sequence check, not readiness
or scientific approval of PR21/24, nor an AC merge-order decision. Later
changes to those heads require another check before relying on that sequence.
