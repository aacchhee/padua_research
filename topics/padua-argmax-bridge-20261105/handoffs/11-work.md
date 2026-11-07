# Handoff 11: Padua argmax bridge. Answer interim audit-02 and decide the pack release, then implement Claude's ideas

- Status: done in d6120b602090c6ff8217ff971328698ee6113393
- Previous handoff: 10-interim-audit-syvert2.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator. Development: Sol medium for technical work and Sol xhigh for ordinary mathematics. A distinct Astra high/xhigh agent does supplementary checks. Astra ultra only with a recorded written justification.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `d5871ff9d37a52f3f18a90ecdaf987e5dd382601` (interim audit-02 outputs); this handoff is the following handoff-only commit
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`
- Stage: WORK
- Written by / date: Claude. Orchestrator `claude-sonnet-5-5`; the audit and ideas were done by six Claude Opus 5.5 subagents instructed at xhigh. See audit-02-interim.md for the disclosure. · 2026-11-07

## Authority

AC required that the interim audit leave the branch at WORK and that Codex
implements next. Pushes to this working branch stay authorized. Do not push
main, merge, force-push, change tags, `.github` or settings, or mark PR27
ready. Nothing in audit-02 waives any finding or grants readiness. Bulk
Syvert2 execution stays **unexecuted**. The approved rounds D01–D40 and
E01–E15 are complete and no new round is allocated by this handoff. A new
numerical campaign needs AC's allowance; audit-02-ideas.md proposes
bounded first tests that fit inside existing authority only where they
are paper work or small preregistered MEASURED checks, and you decide which
fit. No new AC confirmation is needed for already authorized actions.

## Read first

1. AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the current
   head; record the SHA.
2. This handoff, [audit-02-interim.md](../audit-02-interim.md) and
   [audit-02-ideas.md](../audit-02-ideas.md), then the five review records
   in [audit-02/](../audit-02/) for the exact locations and reproduction
   commands.
3. The LOG entry dated 2026-11-07 "INTERIM Claude audit-02".

## Task A: decide and fix the Syvert2 pack findings (before any release)

Write the dispositions in `response-02.md`. Each of PA1–PA4 gets a code
change, a recorded decision or a reasoned dispute. A source change to the
pack changes its identity: rebuild with a new recorded identity and a
focused re-review, and never present the result as the original ZIP
`8274249f…e38b`. Do not rebuild or substitute that artifact for a prose
correction.

- **PA1 (SIGCHLD).** Reset SIGCHLD to its default at the top of
  `server.py` and `job_worker.py`, record the inherited disposition in
  preflight, refuse to run if it was ignored, and add a control that
  fails if an ignored SIGCHLD can turn exit 7 into a recorded 0. The
  auditor's fake-worker control is in `audit-02/code/t2/x_controls.py`
  and can be adapted. Use waitpid-level status where Python's `subprocess`
  would hide ECHILD.
- **PA2 (recovery).** Handle SIGHUP and SIGQUIT like SIGTERM and set a
  parent-death signal in the worker. Define and implement a supported
  recovery for: a changed boot id after a fully quiescent completed
  campaign, and a recoverable preflight failure. Hand-written
  `COLLECTION.json` with `quiescent:true` must never be the remedy.
- **PA3 (decision).** Choose and record, with AC if you judge it
  necessary: keep stop-on-first-failure, or separate the operational stop
  from a recorded scientific terminal failure. Whichever you choose, add a
  partial-return verifier so completed cases can be data-validated, and
  say what happens to degrees 161–191, where neither the n>=192 nor the
  n>=256 premise applies.
- **PA4 (integration).** Preregister a local dress rehearsal of the actual
  worker-to-engine path on known degrees (limits, affinity,
  `LD_LIBRARY_PATH` into the compiler, evidence capture under concurrency),
  or record a decision that `run_small` on Syvert2 is that test. Do not run
  any residual degree as part of it.

Then address the pack MINORs that touch the runtime path (the receipt
size dependence on path length near the 16384 B cap, the runtime library
bytes never compared with a pin, snapshot locators for the six packages,
the out-of-protocol retry check, the size check in `verify_return`). The
ZIP and `local-output/` are not in new cloud checkouts. Archive the pinned
packages in the pending cold-storage transfer or record the limitation.

## Task B: record-only fixes for A-1…A-12

Answer each in `response-02.md` with the exact change. Wording, citations,
dated pointers and status addenda only. No statement, constant, status or
threshold changes, and pinned proof text stays intact (use dated addenda).
In particular: dated pointers where appendices still say "onset 768"; the
hash labels Hmax461214a5 and b6a9db93 (they are review-file hashes); the
named source of C-infinity(0)>0; the domain-transfer citation for
E04-assembly640 eq. (4) at n=256; the PD-T271 dependency in the PD-N
obstructions; and the size bound 9,509,626 B. If a fix seems to need a
mathematical change, it is no longer MINOR: stop and record it.

## Task C: findings that are not yours to waive

P1–P4 stay unwaived. Put them, with the auditors' severity ranking
(P1 > P3 > P4 > P2) and the inconsistency noted for the E14-wide-signed
ruling, in front of AC for an explicit disposition. Do not retire or
re-label them.

## Task D: implement the ranked ideas (bounded first tests)

Each item is a new candidate with its own provisional IDEA, attempt and
theory records under the existing novelty and kill gates. The frozen
records (E01–E15, PD-T271 and all PD-N scopes) are not edited. An onset
below 320 is a new theorem and needs a proof, an independent review and
a fresh assembly. A rescaling of the planning table is not one.

1. **I06 EM2-box, first test T1.** Bounded MEASURED script (cap 600 CPU-s):
   the four signed E14 telescope components at the eight probe phases of
   audit-02-ideas.md. Kill: any component is at least 0.1 with cancelling
   partners. On success, write the contract for the validated
   degree-free second-order remainder on phase boxes (1/32 <= rho <= 5/4)
   and preregister the Arb run before running.
2. **I07 outer seam.** Run its kill test first (it fails if the
   wide-relative inflation exceeds 1.5). Prove the E14-wide relative
   bounds on rho <= 5/4 only if it passes, and re-anchor the E13 gate
   there. Note the no-root margin identity: this route cannot reach pi/2.
3. **I08 cross-degree templates.** First analyse the committed D38
   receipts (no computation): which degrees' trees equal a band template.
   A floating producer-only dry run over the 273 degrees needs an
   explicit root release with preregistered caps; do not run it before
   Task A is settled.
4. **I09, I10.** Paper work only, after I06 shows which components
   dominate. I09 is the only lever on the n <= 82 floor barrier.

Order: Task A decisions first, then Task D1 and D2 tests. A coherent
batch returns to Claude for the final audit.

## Frozen

- All E01–E15 theory records, the global320 theorem and its reviews.
- The finite 2–42, 63–64, 159–160, 511–512, 1023 theorems and certificates.
- The D36 and hybrid engine freezes (any engine change needs a new freeze
  and review), the C03 checker, the immutable n32 candidate.
- The PD-N scopes, the post-audit round counts and the PR27 draft state.

Keep every failed receipt and audit record, and preserve the historical D36
primary missing-outer-exit limitation. No new degree with old technology, no
bulk Syvert2 run, no remote access, no major cleanup.

## Publication and next step

- Checkpoint each completed task with its records and receipts.
- Check the evidence index (336 entries, 27,665 B, under the reviewed 32 KiB
  exception), the per-file 16 KiB limit and the 10,000,000-byte temporary
  ceiling. audit-02 added about 0.35 MB of authored review text and small
  scripts, none of it generated output.
- Update LOG, report, results and the PR27 WORK, AUDIT and PR sections.
- Final IDs and the registry application stay deferred. Refresh the live
  reservation union before any later assignment.
- When development reaches a coherent batch, hand off to Claude for the
  final audit. That audit must also cover the n-independent upstream cores
  listed in audit-01 and audit-02 under "not re-derived".
- At the session boundary, commit outputs first. Then, in a separate
  commit, close this handoff as `done in <sha>` and add handoff 12. Exactly
  one handoff stays open.
