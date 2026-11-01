# Response 01 to protocol audit 01: handoff and ID rules

- Developer: Claude, claude-opus-5-5 (requested effort high).
- Rules read at the branch head, `3b1908b` (rule text as at candidate `10f2d85`).
- Responds to [audit-01.md](audit-01.md) at `19526f2`; the audit report is preserved unchanged.
- Main is `21e620b`, unchanged since the audit and already the base, so no merge was needed.
- AC's message invoked handoff 02 exactly, with no override.

## Dispositions

| Finding | Disposition | Where |
|---|---|---|
| **F1** retain reservations after a PR leaves the open set; namespace maxima; priority; collision repair | **Accepted, strengthened.** <ul><li>The scan (step 2) now also reads retired reservations and the ledger of any closed, unmerged PR whose reservation is not yet recorded as retired. A closed PR's block therefore cannot be lost, even before anyone records it.</li><li>Step 3 computes the maximum per namespace and includes retired reservations.</li><li>New step 7 rechecks reservations before final-ID assignment and before readiness.</li><li>New paragraphs **Priority and collisions** (the pushed commit sets priority; accepted IDs are preserved; old-to-new mapping recorded; AC decides unclear cases) and **Retired reservations** use the auditor's wording, adapted to the numbered list.</li></ul> | `agents/WORKFLOW.md`, ID procedure, steps 2–3 and 6–7, and the two new paragraphs; ledger sentence |
| **F2** superseded single-owner ledger prose; transition | **Accepted.** A dated **Transition (adopted 2026-11-01)** paragraph supersedes the single-owner and owner-confirmation prose. That prose stays as provenance and gets a supersession note at the ledger's next maintenance. The paragraph also: <ul><li>keeps all recorded ranges and AC instructions;</li><li>adopts the procedure at each topic's next continuation;</li><li>imports existing reservations unchanged, filling in provenance but adding no retrospective headroom;</li><li>says "no range" when a topic needs no final IDs;</li><li>limits early updates to reservation-only ledger and PR-body entries.</li></ul> The ledger itself is not edited here (scope limit). | `agents/WORKFLOW.md`, Transition paragraph |
| **F3** handoff ownership and lifecycle | **Accepted, with one refinement.** The auditor proposed that "the topic orchestrator alone" allocates numbers. That would bar the auditor's own orchestrator from opening the response handoff, which audit-01 itself correctly did with `02-response.md`. The rule therefore gives this authority to the orchestrator of the session holding the open handoff (developer, auditor or topic orchestrator). Its subagents never open handoffs, and two orchestrators never work one branch at the same time. The rest follows the proposed wording: <ul><li>a handoff stays open while in progress;</li><li>outputs are committed first, then a following commit sets `done in <output-commit-sha>` and adds the successor;</li><li>a redirection sets `superseded by NN: <reason>` and opens a new handoff;</li><li>`withdrawn: <reason>` cancels;</li><li>bodies are never altered.</li></ul> The template uses **Input head SHA** for the existing commit, separate from the publishing commit. | `agents/WORKFLOW.md`, Handoff files; `templates/HANDOFF.md` |
| **F4** no-audit exemption and terminal topics | **Accepted.** `Continue` reads the log "if the topic has one". The `no audit` exemption does not waive a numbered handoff while work remains; without a log, the context and chain live in the handoff files. On completion or AC withdrawal, the last handoff is closed and completion is recorded in the log (or in its status line). Such a topic has no open handoff and needs no prompt, while a topic awaiting PR preparation or a follow-up keeps one. AGENTS.md now says "while work remains", and the template states the closing step. | `AGENTS.md`; `agents/WORKFLOW.md`, Work cycle and Handoff files; `templates/HANDOFF.md` |

## Transition statement (refreshed 2026-11-01)

| PR | Branch | Head |
|---|---|---|
| main | | `21e620b` |
| #6 | `claude/programme-ideas-20261031` | `37820a5` |
| #9 | `codex/padua-proof-attempts-20261101` | `7b8884a` |
| #11 | `claude/mz-prior-art-20261101` | `97968d2` |
| #12 | `codex/padua-proof-attempts-2-20261101` | `38db12b` (advanced since the audit snapshot) |
| #13 | `claude/handoff-id-rules-20261101` | this branch |

No closed, unmerged PR exists.

I agree with the auditor's recommendation:
- **#11** keeps LIT-293–299. Its "next LIT-300" is a historical boundary.
- **#6** keeps its recorded blocks unchanged: lattice PD-T081–094, PD-N032–038, IDEA-177–189 and LIT-300–331; programme-ideas PD-T095–100, PD-N039–043, IDEA-190–209 and LIT-332–426. They are not yet on main.
- **#9 and #12** have no final reservation. Their ledger copy is byte-identical to the old one (blob `e8328eb`, as at `9bd14a6`). At their next continuation they record either fresh ranges, after a full scan, or "no range". The ownership limits AC set for them still apply.
- **#6 and #11** fill in the missing count, head and provenance details and the supersession note at their next continuation.
- **#13** needs no range.

The lowest boundaries across all recorded reservations are PD-T101, PD-N044, IDEA-210 and LIT-427, subject to a fresh scan when used. Nothing is reserved here.

## Checks actually performed

- `git diff --check` is clean.
- The changed text was re-read in full in context.
- The handoff chain has exactly one open handoff after this step: 02 is marked done and 03-audit is open.
- Only `AGENTS.md`, `agents/WORKFLOW.md`, `templates/HANDOFF.md` and this topic's files changed. `audit-01.md`, `01-audit.md` and the body of `02-response.md` are unchanged, and no registry, ledger, scientific file or other topic was touched.
- No scientific rerun was needed.
