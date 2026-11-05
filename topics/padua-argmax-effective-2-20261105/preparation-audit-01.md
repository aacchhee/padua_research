# Claude preparation-audit-01 — PR25 registration and integration (handoff 06)

## Decision

**ACCEPTED.** The final registration, allocation, preservation, integration
rehearsal and PR25 body are correct at the stated scope.

- **Assigned:** PD-T364–369 (PROVED), PD-T370 (MEASURED), PD-N132 (PROVED
  scoped obstruction) and IDEA-454–461, all inside the unchanged reservation
  first published at `ce17564`.
- **Not registered:** T02 stays a local CONDITIONAL label. No LIT ID is
  assigned.
- **Permanent gaps:** T371–375, N133–137, IDEA462–465 and LIT594–597.
- **No change to science:** no accepted Statement, proof body, constant or
  status changed, so no mathematical re-audit is needed.
- **PD-T099 stays OPEN.** The global certified range is exactly 2–32. There
  is no explicit full-diamond N1 and no bridge 33≤n<N_*.
- **Findings:** none blocking or major. P1 is minor (a stale foreign pin in
  the PR body); P2–P3 are notes. Stage: PR, final readiness bookkeeping
  (handoff 07). Only AC merges.

## Identity and inputs

- **Auditor:** Claude, configured `claude-opus-5-5`, effort high, as
  handoff 06 requested. Role: independent preparation auditor, distinct from
  the Codex developers and the Astra-medium protocol checker. I edited no
  developer record. The serving model is not separately exposed.
- **Rules:** `AGENTS.md`, `agents/WORKFLOW.md` and
  `agents/claude/CLAUDE_ROLES.md` at head
  `b301f530a621528f77724401e572977586982651`. Rules, templates and `tools/`
  are unchanged since `22e8540`.
- **Candidate:**
  - preparation output `d3ea843`;
  - enclosing source `ab4cd00` (later commits touch only the LOG, the index
    and handoffs 05–06);
  - registered/rehearsed source `32b24b6`;
  - pre-registration baseline `5821c3f`.
- **Main:** `330fab835f43e5ba5b24e320c2d7e9647e6cbd60` (PR26 merged),
  already merged into the topic.
- **Live open PRs (2026-11-05, GitHub connector):** #21 `67b3e01`, #24
  `45646d7` and #25 `b301f53`. The ten most recent closed PRs (#14–#20,
  #22, #23, #26) are all merged; no closed-unmerged reservation was found
  among them.

## Reads

- **Topic records:** handoff 06; the LOG header and preparation entries; the
  preparation directory listing; `pr-body-template.md`; `final-id-map.json`
  through its effects in the crosswalk.
- **Shared records:** all diff lines `330fab8..HEAD` in PROOF_STATUS,
  state/IDEAS, state/CURRENT, PAPER_MAP, ID_CROSSWALK, RESULTS,
  topics/README and the batch ledger.
- **Theory files:** all eight registered files, compared with `5d47621`.
- **Novelty coverage:**
  - The full `state/IDEAS.md` read is the one recorded in audit-01 at
    `aff30e8`, including every obstruction and disposition table.
  - Read in addition: its delta `aff30e8..330fab8`, which is PR26's
    signed-MZ cleanup section IDEA-466–489 and unrelated to the argmax
    mechanisms, and the eight new IDEA-454–461 rows. No disposition history
    was altered.
- **Not re-read in full:** `protocol-check-01.md` and every rehearsal
  receipt row. Those were reproduced independently instead (below).

## Executed checks

1. **Codex registration checker:**
   `check_registration.py --baseline <fresh git archive 5821c3f> --output
   <scratch>` → **PASS, 3648 checks, 0 failures.**
2. **Diff hygiene:** `git diff --check 330fab8 HEAD` is clean.
   `tools/cold_storage.py plan` reports 0 tracked bytes to relocate.
3. **Removed lines in shared files.** My own diff of the shared files found
   that exactly three pre-existing lines change:
   - the PD-T099 row gets a dated progress insertion and keeps OPEN;
   - in `state/CURRENT.md` and `PAPER_MAP.md`, exactly the proposed
     "weighted energy and the fixed scaled phase radius remain OPEN" anchors
     are replaced by the accepted text, with T06/T07 resolved to
     PD-T368/369.

   No other line is removed in PROOF_STATUS, IDEAS, the crosswalk, RESULTS,
   the batch ledger or literature/INDEX. Literature/INDEX is untouched.
4. **New rows:**
   - PROOF_STATUS has 8 new rows: PD-T364–369 PROVED, PD-T370 MEASURED,
     PD-N132 PROVED.
   - state/IDEAS has 8 rows, IDEA-454–461, with exact provisional aliases.
   - The crosswalk maps all 16 IDs; T02 is listed as not registered.
   - The batch ledger imports the same reservation, citing `ce17564`, and
     makes no second reservation.
5. **Collision scan.** For the reserved ranges, at main `330fab8`, PR24
   `45646d7` and PR21 `67b3e01`, outside this topic, every hit is an
   acknowledgement of this reservation: PR26's merged ledger and records,
   PR24's PROT/handoff, PR21's response. None is a use.
6. **My own rehearsal at the live heads** (disposable detached worktree from
   `330fab8`, `git merge --squash` then commit; removed afterwards):
   - Orders: 25; 24→25; 25→24; 21→25; 25→21; 21→24→25; 25→24→21.
   - Result: **all clean, 0 conflicts.** The paired and triple trees are
     identical across orders (`2689261334`, `cf895d2443`, `363743e526`).
     Owned-path whitespace is clean.
   - Triple tree against main: PROOF_STATUS rows 301→309, IDEAS 357→365,
     INDEX 440→440. No new duplicate row IDs. All 11 existing RESULTS
     sections are kept, and only this topic's section is added.
   - This supersedes the developer receipt's PR24 pin `3a179f6` for current
     use. The receipt itself stays a correct record of its own run.
7. **Preservation, compared with `5d47621`:**
   - All eight registered theory files keep the accepted body as an exact
     prefix after the renamed heading. The appended text, about 1 KB each, is
     registration metadata only; I inspected PD-T369's in full.
   - T02, audit-01, response-01, response-check-01, independent-math-checks
     and response-independent-01 are byte-identical.
   - Code and evidence are unchanged since `22e8540`.
8. **Evidence index:** all 69 topic and 10 repository rows match both
   source `ab4cd00` and the current bytes. All topic JSON parses, and none
   exceeds 16 KiB. Committed non-Markdown files total 977,247 bytes, below
   the 5 MB ceiling.
9. **RESULTS:** the root section equals the topic results file modulo the
   `../topics/` → `topics/` link normalization.
   - I left both files unchanged, because they are pinned in the evidence
     index. Their "preparation audit remains pending" sentence is for
     handoff 07 to update in both copies, with a re-pin.
10. **PR25 body:** the body matches `pr-body-template.md`, with the two
    placeholders resolved to `d3ea843` and `b301f53`.
    - It carries the R1 items for AC unchanged.
    - It makes no first-constant, delivery or readiness claim.
    - It remains a draft.

## Findings

- **P1 — MINOR.** The PR25 body (§PR) states "Main/PR24 stayed unchanged.
  Final foreign pins: … PR24 3a179f68…". PR24 has since advanced to
  `45646d7`: 86 files, all under its own topic directory.
  - Check 6 shows the integration is still clean at the live head.
  - Handoff 07 must refresh the foreign pins and the reservation union in
    the PR body. This audit appends a dated auditor note rather than editing
    the developer's text.
- **P2 — NOTE (storage).** The presence of the 40 original outputs remains
  Codex-sandbox-attested. This environment cannot read
  `local-output/`. The recorded fallback wording ("not retained; regenerable
  except timing and hardware-dependent capped frontiers") is in place. No
  proof depends on these bytes.
- **P3 — NOTE (AC items, unchanged):**
  - the broader A0 criterion reading;
  - physical cold-storage delivery;
  - fulltext priority for T06 (Bos et al. 2006) and for T03's
    generating-curve analogue.

## Residual limits

- This audit checks bookkeeping and integration. The mathematics rests on
  audit-01.
- Foreign branches can advance again. Readiness requires the fresh live-head
  and reservation refresh assigned to handoff 07.
