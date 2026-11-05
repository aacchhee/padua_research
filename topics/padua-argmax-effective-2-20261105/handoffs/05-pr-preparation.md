# Handoff 05 — padua-argmax-effective-2-20261105 — PR preparation

- Status: open
- Previous handoff: 04-response-check.md (done in d574603d1635d5f4eca72bcf4fe7d7e8b1d4350e)

- Next agent / model / effort: Codex. Orchestrator: gpt-6-astra ultra, under AC's 2026-11-03 standing instruction for this topic. Registry classification and wording should use that model. Purely mechanical registry/ledger edits may use gpt-6.1-sol medium. Record the actual models.
- Role: orchestrator and developer (preparation)
- Branch: codex/padua-argmax-effective-2-20261105
- Input head SHA: `d574603d1635d5f4eca72bcf4fe7d7e8b1d4350e` (response-check-01 output; the commit publishing this file comes later)
- Main / base: `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7` (merged at `3707a5f`)
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 (configured; high requested) · 2026-11-05

## Task

Prepare draft PR25 for AC's merge decision, following WORKFLOW step 5 and "Audit and PR records". Before step 1, read [response-check-01.md](../response-check-01.md), whose residual notes R1–R4 bind this step, as well as audit-01, response-01 and `proposed-record-changes.md`.

1. **Reconcile the base.** Fetch `main` and every open PR (at handoff time: #21 `0b5fb2d`, #24 `02a465b`, #26 `902360d`). Merge `origin/main` if it has moved, without rewriting history. Record each SHA.
2. **Fresh reservation union check.** Follow the WORKFLOW reservation procedure:
   - Read every live and retired reservation in main and in each open PR's ledgers, `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`.
   - Confirm that T364–375, N132–137, IDEA454–465 and LIT594–597 remain uncontested. PR26 already records them and reserves above them.
   - Record the heads you checked.
3. **Final assignment, inside the reserved ranges only.** Assign exactly what response-01 proposes and response-check-01 R3 lists:
   - **PD-T:** T01, narrowly, as the finite phase-chart sufficiency reduction; T03; T04; T05; T06; T07; T08 (MEASURED).
   - **PD-N:** N01.
   - **IDEA:** IDEA01–08, with the dispositions recorded in proposed-record-changes.
   - **Not registered:** T02 stays a local label; no LIT ID is needed.
   - Unused IDs remain permanent gaps.
   - Record every provisional-to-final mapping in `ID_CROSSWALK.md` and the ledger.
   - Rename provisional headings and aliases in the theory files without changing any Statement, proof or status.
4. **Shared registries, once.**
   - Add the rows to `PROOF_STATUS.md`, with N01 as `REJECTED: refuted` for the a·b_n form only.
   - Add a section to `state/IDEAS.md` for the IDEAs, including the equivalent and deferred dispositions.
   - Apply the `state/CURRENT.md` and `PAPER_MAP.md` text from proposed-record-changes, after re-checking its anchors.
   - Add a dated progress note to the PD-T099 row: still **OPEN**, global range exactly 2–32, bridge 33≤n<N_* unresolved.
   - Import this topic's reservation into the shared batch ledger, and link it from `ID_CROSSWALK.md`.
   - In `RESULTS.md`, add or replace only this topic's section, taken from `results/padua-argmax-effective-2-20261105.md`.
   - Change no other topic's rows or sections.
5. **Integration rehearsal.** In a disposable local branch, rehearse squash-merging PR25 onto current main, and also in an order with each open PR that touches the same registries. Record the conflicts and the semantic checks (no duplicate IDs; every section and row preserved). Repair the topic branch if needed. Never touch `main`.
6. **Verification.** For this topic, run:
   - `git diff --check`;
   - the link check;
   - JSON parse and the 16 KiB limit;
   - `python tools/cold_storage.py plan topics/padua-argmax-effective-2-20261105`;
   - the whole-repository committed-output size check, which must stay below 5 MB.

   Then re-pin `evidence-manifest.json` to the preparation source commit, keeping the previous-index provenance. Historical audit and response reports keep their own pins (R4).
7. **Storage (R2).** If the 40 local outputs are still present in the Codex sandbox, re-hash them and keep "pending delivery". If they are absent, record "not retained; regenerable except timing and hardware-dependent capped frontiers". Never claim delivery.
8. **PR25 body.** Write the three sections WORK / AUDIT / PR.
   - AUDIT: audit-01 accepted the mathematics; response-check-01 accepted the response; record the auditor models.
   - PR: base and head SHAs, the final ID mapping, the verification commands, and the decision items for AC unchanged from R1:
     - the broader A0 reading (F3);
     - physical cold-storage delivery;
     - fulltext priority for T06 (Bos et al. 2006) and for T03's generating-curve analogue.
   - Keep PR25 a draft until the preparation audit below accepts. Only AC merges.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- LOG; audit-01, response-01 and response-check-01; proposed-record-changes.md; ALLOCATIONS.md; allocation-review.md.
- The current shared ledgers, and the registries named in step 4.

## Scope limits

- No new mathematics, run or claim. Do not change any Statement, proof, constant or status. A change that does so returns the topic to AUDIT for a Claude mathematical re-audit.
- PD-T099 stays OPEN. Remaining H1/H2 research (verified phase-box predicates and checker, full-diamond profile/remainder, explicit N1, bridge arithmetic) stays OPEN for a later topic. It is not part of this preparation.
- Never renumber an accepted or reserved ID.
- Do not edit other topics, `.github`, settings or tags. Never merge, force-push or push to `main`.

## Acceptance and outputs

- Registries, crosswalk, ledger and RESULTS section are updated exactly once.
- The rehearsal record and verification receipts are written. The PR25 body is complete.
- Commit the preparation outputs first. Then, in a following commit, set this handoff to `done in <sha>` and open handoff 06: a Claude preparation audit (Opus 5.5 high) of registry and allocation integrity, the rehearsal and the PR body. Push before replying.
