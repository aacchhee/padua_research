# Handoff 23 — padua-3d-20261106 — PR preparation, readiness check and freeze

- Status: superseded by 24: AC directs finalizing the PR without further Claude review
- Previous handoff: [22-response-05-audit.md](22-response-05-audit.md)
- Next agent / model / effort: **Codex, gpt-6-astra high** (coordinator). Use gpt-6.1-sol medium for mechanical registry edits.
- Role: developer and orchestrator, at PR-preparation stage.
- Branch: `codex/padua-3d-20261106`. PR: [#33](https://github.com/aacchhee/padua_research/pull/33), still a draft.
- Input head SHA: `65afacf5c961ff1de224791548e87f88eaf97c33`. That is the audit-06 output: report `986cafc`, then auditor fixes `65afacf`. The following commit publishes this file.
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. Fetch first. If main has moved, merge `origin/main` into the branch. Never rewrite history.
- Stage: **PR**.
- Written by / date: Claude, claude-opus-5-5 high · 2026-11-12.

## Audit state

The Claude audits are complete:
- [audit-01](../audit-01.md) through [audit-05](../audit-05.md) accepted the mathematics, and their findings were answered;
- [audit-06](../audit-06.md) accepted response-05.

All directions are **frozen**. No research, optimization, proof or quota-spending work is authorized.

AC's 2026-11-08 decisions are settled; do not re-ask them:
- the E4 label convention;
- the storage allowance (32 KiB per file and manifest, 10 MB repository-wide, provisional, discussed in the PR);
- the accepted canonical deviations;
- the lattice timing boundary.

## Task (WORKFLOW "Work cycle" step 5, and "Audit and PR records")

1. **Audit-06 return item H-m7.** Verify, then correct, the bibliography metadata for *A Belgian View on Lattice Rules*: the co-author (Cools–Nuyens), the DOI 10.1007/978-3-540-74496-2_1, and replacing the full-book mirror link with a DOI citation. Change it only to the coverage level you can verify, and record that level. You may dispute any audit-06 auditor fix, including the K1 classification; disputes go to AC.
2. **Fresh reservation procedure** (WORKFLOW "Reserve fresh ranges; never reallocate"):
   - Refresh `main` and every open PR, drafts included.
   - Read all ledgers and used final IDs in `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`, plus the retired reservations.
   - Compute the per-namespace maxima.
   - Reserve PD-T, PD-N, IDEA and LIT ranges with headroom, in `topics/padua-3d-20261106/ALLOCATIONS.md`, and record the heads you checked.
   - Put the reservation in the PR body immediately.
3. **Final-ID assignment and registry application.** Map every retained provisional ID to a final ID, preserving every alias: PD-T, PD-N, the IDEA candidates (including all failed, deferred, abandoned and Claude `IDEA?…-claude-01..08` records) and the new LIT records.
   - Edit these shared registries directly: `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md`, `ID_CROSSWALK.md`, `state/CURRENT.md`, and `PAPER_MAP.md` (an entry for the 3-D paper note).
   - Add a `RESULTS.md` section for this topic from `results/padua-3d-20261106.md`.
   - Add the dated addenda that audit-01 requested for the old "3-D out of scope" entries IDEA-120, IDEA-013 and IDEA-029. Do not rewrite them.
   - Registries carry only claim content, status, dependencies, dispositions and links, with no process stage.
   - Statuses must match the audited theory records exactly. Use the full E4 label: "PROVED with explicit LITERATURE dependency".
4. **Frontier cleanup.** Remove or describe completed preparation tasks from the shared frontier. The detailed stage history stays in the LOG and the PR.
5. **PR body.** Fill in the WORK, AUDIT and PR sections:
   - audits 01–06 with their models;
   - the final claim and status list;
   - the reservation and the heads checked;
   - the storage-allowance use, for discussion;
   - the accepted deviations.

   The decision requested from AC is the merge decision.
6. **Readiness.** Commit and push. Then open handoff 24 for a **Claude readiness check**. It covers the reviewed `git diff` of the shared registries against `main`, plus the reservation refresh. It is not a new audit round, unless the registry application makes a material change beyond the audited scope.

## Scope limits

- Do not reopen theorems, frozen directions or audit outcomes.
- Do not edit audit reports, fix notes, the frontier records or earlier handoff bodies.
- Do not change other topics' content beyond the shared-registry application.
- Do not touch main, tags, `.github/`, settings or workflows. Do not mark the PR ready or merge it yourself unless AC asks. Only AC merges.

## Acceptance and handoff

- Reservation recorded.
- Registries applied with complete mappings.
- PR body complete.
- Exactly one open handoff (24, for the Claude readiness check), committed and pushed before replying.
