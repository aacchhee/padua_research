# Protocol audit 01 — handoff and ID rules

**CHANGES REQUIRED. Stage WORK; PR #13 stays draft.**

- Auditor: Codex; AC-requested allocation `gpt-6-astra medium`. Resolved runtime model/effort metadata is not independently exposed. This is the independent Codex audit of Claude development, not developer self-approval.
- Rules and audited candidate: `10f2d8592673866ed0aa5ca73cef88d7541183ed`.
- Current main / merge base: `21e620ba8b5f0e0706f3a8c6613517df04d9d469`. The candidate is two commits ahead, zero behind.
- Scope: the six changed files, unchanged Codex role instructions, and allocation-transition evidence below. No mathematics, ideas, novelty, source-priority or proof-status assessment. The novelty gate and full IDEAS read are omitted for this explicitly administrative scope; no scientific execution or literature verification is claimed.
- AC's message exactly invokes handoff 01; there is no instruction override to record.

## Coverage and what passes

Read `AGENTS.md`, complete `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, both affected templates, this topic's log and handoff 01 at the candidate. Read the complete batch ledger on main and each open draft branch at the pinned heads below. Read the current PR bodies. Compared the complete six-file PR patch against main.

The intended policy is present: scan main and every open draft, distinguish reserving ranges from assigning final IDs, retain provisional-to-final maps, obtain additional IDs from fresh ranges, retain numbered handoff instructions and give AC a short continuation prompt. Per-branch ownership does not itself conflict with one ledger path whose reservations are unioned. The existing PR-preparation timing for substantive registry/IDEAS updates, rehearsal obligation, independent audit and AC precedence are retained. A rule-only topic needs no ID range or allocation ledger. The explicit collision exception is sensible; it must preserve already accepted IDs and record the exceptional repair.

## Findings and proposed exact wording

### F1 — P2: retain reservations when their PR leaves the open set

Location: `agents/WORKFLOW.md:111–118`. The scan visits only main and open PRs, yet unused IDs are permanent gaps. A closed, unmerged PR may contain the only record of the highest reserved block. After it closes, another topic following steps 1–3 can reuse that block. The union is not durable merely because the original Git commit remains retrievable.

Add after step 4:

> Reservations remain effective after a PR closes, is abandoned or loses its branch. Before closing or deleting the only live reference, preserve its namespace, range, owner, first published commit and PR locator as a retired reservation in the continuing batch ledger; retain those records through later integrations. Every allocation scan includes these retired reservations. If a past reservation cannot be reconstructed, stop allocation in the affected namespace and ask AC; do not infer that the range is free.

Also clarify steps 3 and 6 / the collision sentence:

> Compute the maximum separately in each namespace. Publication is the pushed reservation commit linked from the PR; date-only entries do not establish priority. Recheck current reservations before assigning IDs or declaring readiness. On a genuine collision, preserve accepted IDs and the earlier published reservation, record the old-to-new mapping for the later conflicting reservation, and select its replacement by the fresh-range procedure. If priority is unclear or either repair would renumber an accepted ID, refer the conflict to AC before further allocation.

Concurrent scans can still race; the recheck and documented collision path handle that exceptional case. This finding does not demand restoring a single allocation owner.

### F2 — P2: specify the transition from the still-binding old ledger authority

Location: `agents/WORKFLOW.md:118`; `topics/padua-batch-20261031/ALLOCATIONS.md:5` on the candidate/main. The new workflow says each branch owns its ranges, while the unchanged ledger says the root Codex MZ orchestrator is the single owner and forbids parallel allocation. Later sections also retain owner-confirmation instructions. The PR changes the workflow but does not resolve those live instructions or define when existing drafts adopt it. This is an actual rule conflict for the next allocator, not grounds for shifting any existing block.

Add a transition paragraph in WORKFLOW (an explicit supersession avoids editing any registry in this rule-only audit):

> On adoption, this range-reservation procedure supersedes older ledger prose requiring a single allocation owner or that owner's confirmation. Preserve that prose as historical provenance and add a dated supersession note when the ledger is next maintained; all existing recorded ranges and AC-specific instructions remain in force. Each existing open topic adopts this procedure at its next continuation, before any new reservation, assignment or readiness decision. Import existing reservations unchanged and fill missing provenance rather than reserving them again or adding retrospective headroom. Record no range when the topic needs no final IDs. Reservation-only ledger and PR-body updates are allowed at draft opening and do not authorize early changes to scientific registries or final-ID assignment outside PR preparation.

The concrete transition below belongs in the developer response/log and handoffs. This auditor has not changed another topic or the ledger.

### F3 — P2: define handoff ownership and the active/redirect lifecycle

Location: `agents/WORKFLOW.md:23–30`; `templates/HANDOFF.md:5,28`. The current text says `open until taken; then done`, which marks work done when it starts, while the template says mark it done when finished. It also lets whoever ends a step open a new handoff, so parallel subagents could independently choose the same number or create two open files. An AC redirect has no defined status syntax beyond a generic request to record the difference.

Replace the status/ownership instructions with:

> The topic orchestrator alone allocates handoff numbers and publishes status transitions; parallel workers return their results to that orchestrator and do not open competing topic handoffs. A handoff remains open while its assigned step is in progress. On completion, commit the step's outputs, then in a following commit change only the old handoff's status to `done in <output-commit-sha>` and create the next numbered handoff atomically. On AC redirection, record the changed instruction in the log and a new numbered handoff, and change the old status to `superseded by NN: <reason>`; cancellation uses `withdrawn: <reason>`. Never alter the earlier instruction body. At a published step boundary there is exactly one open handoff while continuation work remains.

In the template use `Input head SHA` for the already-existing commit being handed off, and distinguish it from the later commit publishing the handoff. That makes both the exact input identity and the completion SHA implementable without self-referential commit hashes. Update the listed status syntax to match. No claim that two independent orchestrators may mutate one branch is intended.

### F4 — P2: make completion and the no-audit exemption consistent

Location: `AGENTS.md:9`; `agents/WORKFLOW.md:21,23,30`; `templates/HANDOFF.md:28`. A `no audit` job may omit its log, but Continue unconditionally requires that log and every handoff must get a log link. Also, an unconditional successor and exactly one open handoff require an endless chain after a topic is finished or withdrawn. Neither case needs a long prompt or a rewritten old instruction.

Add and reflect in AGENTS/templates:

> The small-job `no audit` exemption omits only the audit and log; it does not waive a numbered handoff when further agent work remains. Read and update the log if one is required or exists; otherwise put the necessary context and handoff chain in the numbered handoff files. When all assigned work is complete or AC withdraws the topic, close its last handoff and record completion or withdrawal in its log, or in the final handoff's status line for a log-exempt job. Such a topic has zero open handoffs and needs no new continuation prompt. A topic awaiting PR preparation or a requested follow-up still has one open handoff; only AC merges.

These are policy clarifications for the developer to accept or explicitly dispute, not changes silently made by the auditor.

## Transition snapshot and recommendation

Pinned open-PR snapshot (all five were drafts):

| PR | Branch | Head |
|---|---|---|
| 6 | `claude/programme-ideas-20261031` | `37820a528c863e5cfe2dc2f1f8879b4fd40cf210` |
| 9 | `codex/padua-proof-attempts-20261101` | `7b8884a2f98518784ff3698dd2f3f9c49c9cdd62` |
| 11 | `claude/mz-prior-art-20261101` | `97968d2c2d039cb0910e0ea50747fb2d9e01a262` |
| 12 | `codex/padua-proof-attempts-2-20261101` | `44be0080c69495cc6959e3d4c2b602fa73678d76` |
| 13 | `claude/handoff-id-rules-20261101` | `10f2d8592673866ed0aa5ca73cef88d7541183ed` |

- Main now contains PR #10, including PD-T029–080, PD-N007–031, IDEA-077–176, LIT-066–292. Its original earlier accepted blocks are preserved. PR #6 remains unmerged: do not describe its blocks as already on main.
- PR #11's ledger reserves LIT-293–299. It is above main's LIT-292 endpoint. Its recorded `Next unreserved ... LIT-300` is a historical boundary, not today's global boundary.
- PR #6's ledger records lattice PD-T081–094, PD-N032–038, IDEA-177–189, LIT-300–331, then programme PD-T095–100, PD-N039–043, IDEA-190–209, LIT-332–426. It explicitly checked #11 and preserves LIT-293–299. These blocks are disjoint and ordered above the earlier reservations. Preserve them; do not reallocate them just to conform to new wording or add headroom. This checks recorded ranges, not every scientific cross-reference or allocation-script result.
- Across these recorded reservations the next lower boundaries are PD-T101, PD-N044, IDEA-210 and LIT-427, subject to a fresh full scan when used. This audit reserves none of them.
- PR #9/#12's pinned ledger copies are byte-identical old versions with no topic-owned final reservation; their PR bodies state local-only records and ownership limits. At their next continuation, reconcile the current reservations and record either required fresh ranges or an explicit no-final-ID need under AC's preserved restriction. Do not use inherited stale `Next unreserved` cells or force registry writes. Creating numbered handoffs does not require reauditing unchanged mathematics.
- PR #11/#6 should complete missing count/head/provenance and supersession metadata at their next continuation, before more allocation or readiness; no emergency rewrite of other branches is authorized by this audit. PR #13 needs no final range. This is the recommended answer to the transition question, pending developer disposition and AC's ultimate adoption of the rule.

## Executed checks and limitations

Read APIs: GitHub `get_pr_info(13)`, `search_prs(state=open)`, `compare_commits(main, topic)` and `fetch_pr_patch(13)`. All seven rule/topic input files were fetched at candidate SHA before local checkout. Batch ledgers were fetched at the five main/member SHAs above (PR #13 inherits main's ledger). Exact fetched paths: the seven paths in Coverage, plus `topics/padua-batch-20261031/ALLOCATIONS.md` at main and #6/#9/#11/#12. No unpinned file content was used as audit evidence.

Shell Git initially failed because its proxy connection was unavailable inside the default sandbox. Repeating through the supported network-enabled execution permission succeeded with the inherited proxy. Executed:

```sh
git fetch origin main claude/handoff-id-rules-20261101
git switch -c claude/handoff-id-rules-20261101 10f2d8592673866ed0aa5ca73cef88d7541183ed
git fetch origin main claude/programme-ideas-20261031 claude/mz-prior-art-20261101 codex/padua-proof-attempts-20261101 codex/padua-proof-attempts-2-20261101
git ls-remote origin refs/heads/main refs/heads/claude/handoff-id-rules-20261101
```

The remote main/topic heads matched the pinned SHAs. Reviewed numbered source lines with `nl -ba`/`sed`. These are read/inspection checks, not a scientific rerun or a batch squash rehearsal. A fresh full integration rehearsal remains a PR-preparation obligation where applicable. No complete global-ID consistency audit, closed-PR reservation census, mathematical audit or cold-storage delivery is claimed. No scientific files, rule files, templates, registries or ledger were edited in delivering this audit. The only follow-up required here is Claude's response to F1–F4 and an independent focused re-audit of material rule/template changes.
