# Main update after PR36 — 2026-11-14

AC requested: “pr36 merged, update this one”. Codex, gpt-6-astra medium (configured assignment; runtime serving metadata not independently exposed), updated PR35's existing branch without rewriting published history.

- Previous topic head: `a045b8e9b2b4d92813a9b8e2832b2f8254e7397e`, including the later ASV source-identification note. That note changed no manuscript.
- New main: `3bedf04ba872474aba25f93f5642f5ee83676670` (PR36 squash merge), after the prior shared base `99a9b1d`.
- Merge commit: `2a3e40420abd8084e4e7f522d032b8785549e618`, with the previous topic and new main as its parents.

Five shared-file append conflicts were resolved by retaining both complete additions: ID_CROSSWALK.md, PROOF_STATUS.md, RESULTS.md, literature/INDEX.md and state/CURRENT.md. The existing MZ content and the new Xu/Morrow–Patterson content are both retained. No scientific statement, status, dependency, alias or allocation was changed to resolve a conflict.

The reproducible [integration checker](audit-support/check_pr36_integration.py) passes; compact output is [pr36-integration.json](audit-support/pr36-integration.json):

- All 135 paths introduced by main are present. The 130 nonconflicting incoming paths match main's exact Git blobs; every nonblank addition from both parents survives in the five shared files.
- PD-T684/685 and PR36's PD-T690–709 / PD-N251–253 each retain exactly one registered row. No new duplicate row label was introduced; the historical repeated PD-T140 label predates this merge and was left outside this update's scope.
- MZ manuscript, theory, code, evidence, archive templates/manifests, licence and rule paths are byte-identical to the pre-merge topic head. Thus readiness-02's accepted scope remains applicable; no numerical rerun or rebuild is justified by this shared-registry-only integration.
- The live all-PR collection has 35 records: open PR27/PR35, all closed PRs merged. Fetched PR27 is `fd82e593cd73019601fb00dea9844db09f8601c0`; its ledgers and four ID registries are unchanged from the previously checked peer head.
- Complete ledger/registry bytes were rescanned at new main, merged PR35 and current PR27. The new PR36 ledger was read in full; earlier unchanged ledger ownership remains covered by the prior full reads and PR36's accepted readiness. Union maxima are T719/N257/IDEA795/LIT745. PR35's existing T684–689 range is unchanged, and PR36's T690–719 starts above it; no new allocation or collision repair is needed.

Rules are unchanged from the prior readiness check. No further scientific or novelty audit is requested. The latest ASV note, prepared archive identities, replacement-ZIP access limits and AC's remaining publication decisions remain unchanged. PR35 retains its ready-for-review disposition; only AC merges.
