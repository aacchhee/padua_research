# Readiness 01 — effective cubature and Lebesgue corollary

2026-11-14. Codex readiness orchestrator with two **gpt-6-astra high** independent registry/reservation reviewers; existing LOG runtime disclosure applies.

- Preparation candidate: `47892f13411132488a82e9dcd512d80dc543cd71`.
- Rules/open-handoff head: `b4e00bdaf2ea391489523c28a7f25f0f4fc24c49`; rules unchanged.
- Main/base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`, unchanged ancestor; no merge required.

## Verdict

**READY for AC review and merge decision**, after the separately committed MINOR wording/map corrections below. No unresolved readiness finding, reservation collision, unknown retired reservation or material scientific divergence was found. The branch may leave draft under handoff 09. Only AC merges.

This is the single registry/ID/reservation readiness check, not another substantive mathematics audit. Accepted statements, statuses, code, inputs and evidence remain unchanged. The optional missing Codex coefficient replay, arithmetic trust assumptions, retrospective-gate history and pending archival item remain disclosed.

## Reservation refresh

The GitHub all-PR collection returned **34 PRs**, fewer than the requested 100-item page: open drafts **27/34/35**, 31 closed and all merged, no closed-unmerged PR. Both reviewers independently inspected the population. Main and every open head were included; there is no omitted closed-unmerged ledger.

| Scope | Refreshed head / reviewed identity |
| --- | --- |
| main | `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3` |
| PR27 | Initial full scan `b918c1d5bedba60e8255d7d2b985dd6c70f4690a`; refreshed again to `4ed88e9b811180fa9f88fd629b4f93027c7bfe95` |
| PR34 | Published preparation/handoff `b4e00bdaf2ea391489523c28a7f25f0f4fc24c49`; MINOR fixes `10938c33791a31a2dfb33c77a556a5a24f7ed416` and `9de44d23524bf426a529d8d0fffb1d307cdc4d2a` leave every reservation and assigned ID unchanged |
| PR35 | `be28d3267bf6117878190b10f2d29840e524eac7` |

The independent scan consumed **82 complete ledger/registry copies** (66 ledgers and 16 registries), deduplicated by exact blobs to 18 ledger versions and 26 versions overall. It includes historical/retired blocks and permanent unused gaps, not just currently assigned rows. Context-checked foreign source aliases and test-fixture mentions are excluded only within their documented scope. See [reservation report](audit-work/readiness01-reservations.md) and the reproducible [control](audit-work/readiness01_reservations.py).

| Namespace | Highest foreign reserved/used | PR34 reserved | Assigned | Permanent unused |
| --- | ---: | --- | --- | --- |
| PD-T | 673 | 674–683 | 674–679 | 680–683 |
| PD-N | 245 | 246–250 | 246 | 247–250 |
| IDEA | 755 | 756–765 | 756–762 | 763–765 |
| LIT | 715 | 716–720 | 716–717 | 718–720 |

No foreign hit overlaps PR34's intervals. Existing reservation publication commit `de39dabc7301b0de1463aaf2dab99365c4d7789e` is the sole ledger-addition commit, an ancestor of the candidate and linked from the live PR body. No range was enlarged or reassigned; no priority adjudication is needed.

PR27/35 advanced after reservation time without changing any ledger or any of the four ID registries. Both peers' four registries are byte-identical to main. The later PR27 head `4ed88e9…` was fetched and checked with:

```
git diff --exit-code b918c1d5bedba60e8255d7d2b985dd6c70f4690a 4ed88e9b811180fa9f88fd629b4f93027c7bfe95 -- ':(glob)**/ALLOCATIONS.md' PROOF_STATUS.md state/IDEAS.md literature/INDEX.md ID_CROSSWALK.md
```

Exit 0: the complete full-scan blob coverage remains valid by identity. A final live population/main/peer check is required immediately before marking ready; any relevant change is compared or reviewed before that action. If main or a peer's reservation/identifier sources change before AC merges, refresh the union again. This is a standalone integration against main: neither open peer currently changes the shared ID registries, and no multi-PR squash batch is requested or performed.

## Registry and ID review

[Registry report](audit-work/readiness01-registries.md) compares the six shared-file diffs with the accepted theory/candidate/source records and audits 01–03. All 16 mapped objects have distinct final IDs, one canonical definition each and valid canonical paths. Every provisional alias expands unambiguously after the prefix-format fix. Compact PD-T678 and general-L1 PD-T679 stay distinct; PD-N246 is restricted to 2–109 with M≤8N; the C0 ranges, Chebyshev/exactness/positivity assumptions, LITERATURE dependencies, Q2 disposition and retrospective/S4 attribution are preserved.

The candidate shared-file diffs are additions only, with no other topic rewritten. The auditor's subsequent edits affect only those new rows/section and the topic map. All **63 actual relative links resolve**; table columns match PROOF_STATUS 8, INDEX 7, IDEAS 3 and CROSSWALK 4. Shared scientific registries contain no pending process after the fix; historical verification limits remain factual coverage statements. No claim/status upgrade or new result is introduced.

## MINOR fixes, committed separately from this report

- `10938c33791a31a2dfb33c77a556a5a24f7ed416`: restored the already accepted normalized product-Chebyshev measure/exactness qualifiers in the new standalone summaries, cube-LP integral normalization in IDEA-758, and “fitted” in IDEA-757's stated preregistration. Changed CURRENT's awaiting-replay task to the completed audit's coverage limitation. Removed a trailing hyphen in the abbreviated map prefix so literal expansion matches the existing crosswalk.
- `9de44d23524bf426a529d8d0fffb1d307cdc4d2a`: restored explicit positive weights in CURRENT's common hypothesis sentence.

The independent reviewer inspected both diffs and rechecked maps/links/table formatting. These are bounded wording/format restorations from linked accepted records, with no change to canonical claims, statuses, assignments, reservations, proof or code. They need no new audit round under WORKFLOW.

## Executed validation and residual limits

- `python3 -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py --verify`: **10/10 OK**.
- `git diff --check`: PASS. Canonical paths, 16 map expansions/unique identities, one registry definition per assigned ID, 63 links and table counts: PASS.
- The read-only reservation control reproduces the pinned 82-copy inventory; full commands, output identity and exact source exclusions are in its report. Fresh GitHub population checks and `git ls-remote`/fetch/diff checks are separate from that pinned control.
- No scientific rerun was performed or required: no result-bearing code or evidence changed in this application. The earlier full finite replay remains 278/278 PASS from its own audit.
- No complete Codex gamma/compact/FT replay exists because the ancillary input retrieval returned HTTP403. Original independent Opus runs, developer replays, code inspection and bounded Codex controls remain distinct. Cold-storage archival of regenerable scratch receipts/leaf lists remains pending. Arithmetic trust base and data provenance stay in the accepted theory records and preparation record.

## Post-readiness state

Agent work assigned by handoff 09 is complete. Close that handoff after committing these outputs; no further agent handoff is needed unless a new issue, relevant head/ledger change or AC request reopens work. Mark PR34 ready for review, present the audited changes/limitations to AC and request AC's merge decision. Do not merge. The reservation refresh is a checked snapshot, not continuing monitoring.

**Publication addendum, 2026-11-14.** Immediately before the ready transition, the all-PR collection still contained the same 34 PRs and no closed-unmerged PR; main and PR27 were unchanged from the table above. PR35 had advanced to `8687dfd48d854faf9a19289365bfebbf1a5220d2`. The orchestrator fetched that head and ran `git diff --exit-code be28d3267bf6117878190b10f2d29840e524eac7 8687dfd48d854faf9a19289365bfebbf1a5220d2 -- ':(glob)**/ALLOCATIONS.md' PROOF_STATUS.md state/IDEAS.md literature/INDEX.md ID_CROSSWALK.md`: exit 0. Thus its reservation-source coverage remains exact by blob identity. PR34's readiness output `2bce5d50ad5ef94297359a4ff3bdcf40b5af1669` was pushed, its PR description was updated, and GitHub's ready-for-review transition succeeded. No merge was performed. Handoff 09 is closed in the following publication commit; all assigned agent work is complete.
