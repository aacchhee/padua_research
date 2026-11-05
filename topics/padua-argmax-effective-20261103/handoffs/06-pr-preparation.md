# Handoff 06 — padua-argmax-effective-20261103 — PR preparation

- Status: superseded by 07: AC requests no further Claude check unless MAJOR
- Previous handoff: [05-response-check.md](05-response-check.md), done in 99553c5f10246e3b39c432ea7b6527703dae8291

- Next agent / model / effort: Codex, gpt-6.1-sol medium. This is mechanical registry and ID work under the WORKFLOW allocation table. Use gpt-6-astra medium only if a protocol question arises.
- Role: topic orchestrator (PR preparation)
- Branch: codex/padua-argmax-effective-20261103
- Input head SHA: `99553c5f10246e3b39c432ea7b6527703dae8291` (response check accepted; the commit that publishes this file comes later)
- Main / base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 high · 2026-11-05

## Task

Prepare PR19 for AC's merge decision, at the scopes accepted by [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md). Change no mathematical statement, proof, status, checker, certificate or receipt.

1. **Setup.** Read the rules at the branch head and record the SHA. Fetch main and every open PR. At 2026-11-05 these were #20 `407fe83`, #21 `d669363` and #22 `a0abe8b`. If main moved, merge `origin/main` into the branch (never rebase published history) and record the impact first.
2. **Fresh reservation union scan** (WORKFLOW "Reserve fresh ranges"). Cover:
   - main and every open PR, including PR22;
   - the retired reservations in each ledger copy;
   - final IDs already used in PROOF_STATUS, IDEAS, literature INDEX and ID_CROSSWALK.

   Confirm that this topic's ranges (PD-T246–265, PD-N084–091, IDEA336–355, LIT466–473, first pushed `ed8db2f`) still collide with nothing. Record the scan in `allocation-scan.json` and ALLOCATIONS.md, with the heads checked.
3. **Final IDs.** Assign from the reserved ranges, keeping every provisional→final mapping in an id-map. Assign one ID to each:
   - theory record: codex-01, 02, 03, 03-spots, 06a, 06b, and claude-01;
   - negative record: N-06a, N-06b, N-04;
   - IDEA record in `ideas/`, including failed, equivalent and deferred candidates;
   - LIT record in `literature-g8.md` at its stated coverage.

   Unused IDs remain permanent gaps.
4. **Registries, once, at this stage:**
   - **PROOF_STATUS.md:**
     - add rows for each new record at its exact status and scope;
     - annotate PD-T099, PD-T227 and IDEA-330 per `proposed-record-changes.md`;
     - apply F5/F7: replace every "audit pending" phrase with final IDs and links to audit-01 and response-check-01; cite the final ID of codex-06b in the PD-T227 note; keep "weighted energy and the fixed scaled phase radius remain OPEN" verbatim.
   - **state/IDEAS.md:** a section for this campaign with the full disposition table and an obstruction table for the three PD-N records.
   - **literature/INDEX.md:** the new LIT rows, with coverage limits and the Brutman survey journal correction.
   - **ID_CROSSWALK.md:** the crosswalk and shared-ledger link.
   - **RESULTS.md:** this topic's section, copied from `results/padua-argmax-effective-20261103.md`. Do not touch other topics' sections.

   Update stale "required Claude audit pending" lines in this topic's theory/idea records so they cite audit-01.
5. **Integration rehearsal.** In a disposable local branch, rehearse sequential squash integration with PR20 (shared registry files), and with PR21/PR22 where they touch the same registries. Record the conflicts and semantic checks. Never touch main.
6. **Shared state.** Update `state/CURRENT.md`/frontier, PAPER_MAP and PROOF_STATUS summaries only as WORKFLOW step 5 requires. State the post-merge position:
   - finite 2–32;
   - all-n slopes;
   - n^-6 local radius;
   - PD-T099 OPEN, with no effective n0, degree 40 uncertified and 33–39 unrun.
7. **Verify, commit and push.** Run `evidence_manifest.py`, the link checks and `git diff --check`; commit and push. Update PR19 WORK/AUDIT/PR with base/head SHAs, the registry changes, the verification commands, the unresolved items (raw archive delivery; F8 per-receipt provenance) and the exact decision requested from AC. Keep the PR draft until the preparation check accepts.
8. **Handoff.** In a following commit, close this handoff and open handoff 07: **Claude (Opus 5.5 high): preparation check** of the final IDs, registry rows, crosswalk, RESULTS section and rehearsal. Registry-structure changes require a check by the other agent before readiness.

## Read first

- AGENTS.md, agents/WORKFLOW.md (Audit and PR records; Reserve fresh ranges; Priority and collisions), agents/codex/CODEX.md.
- This topic: LOG, audit-01, response-01, response-check-01, proposed-record-changes.md, ALLOCATIONS.md, allocation-scan.json, every theory/ideas file and literature-g8.md.
- How PR17 registered its rows: `topics/padua-argmax-alln-20261101/FINAL_CANDIDATES.md` and its prep-support.

## Scope limits

- Do not change any mathematical statement, proof, status, code, certificate or receipt. Do not edit audit-01 or response-check-01, or any earlier handoff body.
- Never renumber an accepted ID or reuse another branch's reservation. On a collision or unclear priority, stop allocation and ask AC.
- Do not merge, force-push, tag or touch .github/. Only AC merges. PD-T099 stays OPEN.

## Acceptance and outputs

- Final id-map.
- Registry rows in PROOF_STATUS, IDEAS, INDEX and ID_CROSSWALK.
- The RESULTS.md section.
- The rehearsal record.
- Updated LOG, results file and PR body.
- Handoff 07 open for the Claude preparation check. Push before replying.
