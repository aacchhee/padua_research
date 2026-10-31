# Local squash integration rehearsal

Only root performed Git operations. Main, remote branches and PRs were not merged or rewritten. Disposable worktree: `/workspace/scratch/lattice-unisolvence-20261031/rehearsal`; local branches are never pushed and their upstream is unset.

## Parent dependency

Started local `codex/lattice-squash-rehearsal-20261031` from main d36722823441dc40c6e19d69a174459348dd309c. Executed `git merge --squash 317a26597dedc9adc9cfc6a26fa00078df7d29e4` and committed only on that disposable branch as8f1e61512afd38de8c06981689e2040b6915add7. Its tree7967cdd46923f46c259e29d6aefc2905c379da3e exactly equals the pinned charter source tree, verifying lossless parent squash. The lattice squash and final semantic check are recorded in integration-result.json when executed after the final scientific/registry checkpoint.

## Wider batch, actual conflict observation

From that parent squash, created a second disposable branch `codex/lattice-batch-rehearsal-20261031` and executed `git merge --squash 6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994` (MZ). It exited1 with the10 shared-file conflicts in [batch-conflicts.json](batch-conflicts.json). These are current observations, not inherited from MZ's earlier9-conflict rehearsal against an older parent.

The attempted squash was discarded only in this disposable, root-owned worktree and the parent rehearsal branch restored. No scientific source bytes or live topic state were discarded. The actual wider sequence is **not complete or merge-ready**: MZ and later members must reconcile shared registries/state/ledger after AC's first merge, then repeat the chosen sequence. This draft does not request AC to merge any PR. No other member branch is repaired or mutated by this campaign.

## Preparation limits

The direct charter→lattice sequence verifies the actual scientific dependency, not the proposed charter→MZ→lattice batch order. The latter currently encounters conflicts already at MZ. AC's preferred later order and current owner allocations must be refreshed before readiness; the lattice provisional namespaces do not collide with existing final blocks. Only AC performs real squash merges. After the parent lands, merge the charter-bearing main into the published topic, never rebase it, reconcile and retarget the draft as appropriate.
