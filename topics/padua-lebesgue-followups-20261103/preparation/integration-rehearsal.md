# Disposable sequential squash rehearsal — 2026-11-05

Base: `5db1e01dcd2258f45de2adcaef43859e59734618`. Worktree:
`/workspace/scratch/lebesgue-prep-integration`, detached HEAD throughout.
Orchestrator Codex gpt-6.1-sol medium alone performed mutable Git operations.
Main and every remote topic branch remained unchanged by this rehearsal.

Order tested: main → PR20 → PR21 → PR22 → PR23 → PR24. Only PR20 is under
preparation here; the other four remain drafts. This hypothetical sequence tests
coexistence and preservation, not acceptance or a requested merge sequence for
unready work. Their branches are older than current main; using actual squash
merges preserves main's PR19 additions rather than replacing them from old trees.

| PR | Input head | Disposable squash commit | Result tree |
|---|---|---|---|
| 20 | `d8bc03ae06b8d0cec6442716a0d3f7a6f8c7f6f9` | `83579d14a1e5ea08d1b856aae2e52f1627d703ef` | `c3eafef0884e551097fc4eb89527a6f8a6cd0b4b` |
| 21 | `890f56ccde35431b70b43141c224b0b8817fea7f` | `d4fe649171a77ba4c60040a2eb6c4006d9a4c18e` | `9b6846363fdb91344d4f460f4c339dd5bb3621d6` |
| 22 | `30a361d19a6c23fa1df950becbe73f635aa22e71` | `d8e87200c00fe0b36d1d7b2125105e2910ad0f91` | `3f6231346242fa9a8ad60c5b2f302422cbebacb5` |
| 23 | `2b489d01d443b6780ac034f4d6c20d50fffee2a6` | `94c68c92942a281ab54f108d65727cc13bd79ff4` | `d83449ab76232ebf33cd0f53eca2a57acab39b08` |
| 24 | `5e5081e991fc48f033d3ef51ee2b6e42f892d29d` | `2aaa4a2eed7786ca5857a54a7d04b96b58cb0b07` | `ff0b3e3bdff14292bfc6fc54698062bf5471d958` |

Executed `git worktree add --detach <path> <base>`, then sequentially
`git merge --squash <input>`, `git diff --name-only --diff-filter=U`,
`git write-tree`, `git diff --check --cached`, and local `git commit` with
Agent/Model trailers. No push of rehearsal commits and no GitHub merge occurred.

All five squash merges are conflict-free. PR20's first squash tree equals its
candidate tree exactly. After each other squash, all nine protected shared
files (PROOF_STATUS, IDEAS, literature INDEX, ID_CROSSWALK, CURRENT, PAPER_MAP,
RESULTS, topics README and shared batch ALLOCATIONS) equal PR20's versions
byte for byte. Each draft currently adds topic-local records rather than
applying its shared registry proposals. Every newly introduced path from each
input was compared byte for byte against its source head after its squash.
Thus PR19/main records, PR20 registrations/results and every draft's records
and reservation survive. No semantic conflict needed repair.

`git diff --check --cached` passed for PR20–23. On PR24 it reported only two
existing draft whitespace defects: `attempts/L5.md:48` and `attempts/L6.md:54`
have a new blank line at EOF. The orchestration script stopped on that exit2;
the warning was inspected, recorded, and the already verified PR24 squash was
committed locally without altering those foreign draft files. This is not
reported as an all-drafts whitespace pass. It does not affect PR20's clean
check or the preservation result. PR24 owns its later cleanup/readiness.

Final rehearsal tree: `ff0b3e3bdff14292bfc6fc54698062bf5471d958`.
Future draft changes require their own refreshed allocation, storage and
integration checks; this record does not preapprove those changes. Disposable
commits are local diagnostic identities, not durable evidence dependencies;
the exact published input heads and commands suffice to repeat the rehearsal.

## Final live refresh rehearsal

The later live refresh returned the same 23 PRs, open20–24 and every closed
PR merged. Main/PR21/22/24 are unchanged. PR23 advanced by reconciling main
and updating its topic records. Repeated the entire sequential rehearsal in
`/workspace/scratch/lebesgue-prep-integration-final`, detached from the same
main, using current PR20 candidate and the refreshed PR23 head:

| PR | Input head | Disposable squash commit | Result tree | New paths checked |
|---|---|---|---|---:|
| 20 | `871e25bf918116f95a37f8c3dda3d1533810f4b3` | `22bac3e8d130c19018a4c97b2fd83c42955d48dc` | `3e74f77b10efa68c0aa6afc90621b1fe46618925` | 177 |
| 21 | `890f56ccde35431b70b43141c224b0b8817fea7f` | `2605a8b76449b39dae37b8eabe5cb59f3abedb63` | `167413d5e612cd0dd918e2e3942477c306162eea` | 70 |
| 22 | `30a361d19a6c23fa1df950becbe73f635aa22e71` | `79e8201e3ba4927b0775ae1615d54d4db3cb5cbd` | `510c458717bddfe8849049f98894c61fee0f7af6` | 31 |
| 23 | `8fc9c1da776f85a784eead3591c02fcf4b642250` | `c0fd9314ee1bf7e7a8cc1da320fe8064da8c210b` | `92cd410ceb6b07dd205a6a62aac577c4cc6a05cf` | 106 |
| 24 | `5e5081e991fc48f033d3ef51ee2b6e42f892d29d` | `fc821af2cc0faf2cf7d3b12233b0ab323ef417e8` | `c6589dd5d6ee143c1f1687fa57299d5f0c5fd5dc` | 58 |

All merges remain conflict-free, the first squash tree equals the PR20
candidate, all nine shared-file byte checks pass at every stage, and every
input's new paths match its published bytes. The same two PR24 EOF whitespace
warnings are recorded; PR20–23 pass the whitespace check. No remote branch
was modified. The only changes after the tested PR20 candidate are preparation
review/disposition/refresh documentation and lifecycle status; no scientific
registration or proof change is introduced by that bookkeeping.
