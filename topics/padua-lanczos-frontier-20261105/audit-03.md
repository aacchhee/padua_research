# Claude audit-03 — preparation audit and AC-directed finalization of PR24

2026-11-05. **Verdict: PREPARATION ACCEPTED. PR24 is ready for AC's merge decision.**

- There is no BLOCKING or MAJOR finding.
- AC wrote: "make this PR ready to merge, no more codex". The orchestrator therefore applied the MINOR fixes itself and did not return them to Codex.
- A distinct Claude subagent independently checked those fixes; see the last section.
- Only AC merges.

## Identity, inputs and rules

- **Auditor:** Claude, independent preparation auditor and finalization orchestrator under handoff11.
  - Model: Claude Opus 5.5 (`claude-opus-5-5`), effort **high**, as AC requested ("Claude (Opus5.5 high): Continue …").
  - xhigh was not needed: the audit found no proof or mathematical statement change.
- **Family subagents:** three Claude Opus 5.5 high subagents (REG, APP, FIX). They had no Git authority, and their reports are preserved in [audit-03/](audit-03/).
- **Audited input:** preparation output `0299fcf4d3d3f23eacb69a09fb790ab653e0a724`, preparation checkpoint `e5fbd85`, main integration `a3f03be` with main `b4d292eea5eed373002506d5e16a3761bd7ae10e`. Files were read at publication head `1fb21c1a021642b76f0c60a68efde83e8024b595`, which differs from the input only in handoff10's status and the added handoff11.
- **Rules:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md, read at `1fb21c1`. They are byte-identical to the rules read for audits 01 and 02 and to current main.
- **Reading depth:** a registration-impact audit only. The response proposes no new candidate, mechanism or novelty verdict. However, every duplicate/equivalence consolidation was verified substantively against the existing IDEA rows (REG report).

## AC direction and protocol consequence

**AC's direction.** AC's explicit instruction ended Codex's role in this topic. The orchestrator recorded how this differs from WORKFLOW's normal developer/auditor separation:
- Claude both audited the preparation and applied the resulting minor fixes.
- The fixes are record-only: wording, stage text, ledger whitespace and recording AC's decision. They touch no science, status, proof, threshold or ID.

**Check of Claude's own fixes.** Because Claude both audited and applied the fixes, the fixes were checked by a separate Claude subagent rather than by Codex. AGENTS.md says that AC's explicit task instructions take precedence.

**A-P1.** AC accepted the disclosed pre-gate drafting deviation on 2026-11-05 ("I accept the deviation"). It remains permanently disclosed, not waived and not cured.

## Acceptance checks (handoff11)

| Check | Verdict | Evidence |
|---|---|---|
| 1. audit-02 R2-1–R2-7 and NOTEs | PASS WITH FIX | All R2 fixes verified at their locations (FIX report). Residual gaps in P3-FIX-1/2/3, now fixed. |
| 2. AC acceptance recorded | PASS WITH FIX | Acceptance appears in the results file, RESULTS, report, gate-timing, 14 pre-gate IDEA rows and all 18 descendant overlays. Five inherited IDEA rows and gates.md lacked it; now fixed. L7 and l1-03 are correctly classified as not pre-gate. |
| 3. Reservations | PASS WITH FIX | See below. |
| 4. Final IDs and deduplication | PASS WITH FIX | One-to-one 16/3/11 maps; all 57 aliases persist; the eight existing homes are genuine continuations or aliases; no predecessor statement was altered; the three PD-N records are scoped, not administrative. Labelling fixes P3-REG-3/4 applied. |
| 5. Literal application and preservation | PASS | See below. |
| 6. Durable source consistency | PASS | Final IDs and statuses agree in all locations. Frozen files `f27a22c4…` (L1), `44498c62…` (L2-01) and `9d857e30…` (n1 contract) are unchanged. No code or evidence change since `29a78ec`; all proof sections and fences are preserved; inherited files are append-only. |
| 7. Application refresh | PASS | See below. |
| 8. Checks and integration | PASS | See below. |

**Check 3 — reservations.**
- An independent full union was computed over main, PR27 (at both `3dda890` and `714f3ca`), PR28 (`d879256`; the API later reported `929ef78`), PR24 and `a3f03be`. There are no collisions.
- **PR28 is new and was missing from the preparation's refresh.** It reserves T432–471/N162–177/IDEA530–569/LIT614–629, which is disjoint from PR24, and it acknowledges PR24's ranges.
- PR27's 15 pertinent files are unchanged between `714f3ca` and `3dda890`.
- New union maxima are T471/N177/IDEA569/LIT629. The readiness refresh is recorded in the topic and batch ledgers and in reservation-check.md.

**Check 5 — literal application and preservation.**
- Exactly nine shared files changed: the five registries, one additive batch-ledger section, and three append-only inherited theory files.
- Every changed line is one of the 28 literal blocks or a documented transformation.
- Other topics' bytes are identical.
- The only status upgrade is PD-T140's target part, PARTIAL → PROVED. Its experiment row is byte-identical.
- Every original OPEN target keeps its status and statement.

**Check 7 — application refresh.**
- All five registry outputs reconstruct byte-identically from the base, the proposal, the map **and the live topic results file**. That fourth input is a correction (P3-APP-2): the receipt does not hash it separately.
- The receipt's hashes match, and `--update-applied` guard semantics were verified.

**Check 8 — checks and integration.**
- **Rehearsal:** the squash rehearsal was rerun in a scratch clone and reproduced the tree `aee4d7c45cade76d96481f3e79798ac1a5201196`.
- **Fast checks:**
  - manifest PASS (384 files);
  - registration checker PASS;
  - 140 JSON files, all under 16 KiB;
  - `git diff --check` clean;
  - 5006 links with 0 broken.
- **Merges:** `git merge-tree` against current main `b4d292e` is clean, and so are merges with PR27 and PR28.

## Fixes applied by the orchestrator after the audit (record-only)

**Registry text,** changed through the proposal NEW blocks plus a guarded `--update-applied` re-application:
- The stale stage text "preparation audit pending" (19×) and "awaits preparation audit" now records acceptance by Claude audit-03 (P3-APP-1).
- AC's 2026-11-05 acceptance was added to IDEA-158, 160, 162, 253 and 255 (P3-FIX-2).
- The consolidated self-references in IDEA-250, 262, 266 and 267 now name the local candidate (P3-REG-3).
- The local cross-namespace labels (IDEA/PD-T/PD-N L4-01, L6-01, L6-02, L6-03) now carry provisional tokens, so final IDs are substituted. The result reads, for example, "IDEA-420 (IDEA L4-01)" and "PD-T331" (P3-REG-4).
- "Historical audit-03 PARTIAL" now says "historical Codex audit-03 PARTIAL" (P3-APP-4).
- A dated amendment paragraph in the proposal records all of this.

**How the re-application ran:**
- The committed `apply_registration.py` hard-codes a `/tmp` archive path and resolves the repository from its own location. A scratch copy, differing only in the absolute `TOPIC` path and the archive path, ran `--update-applied --receipt preparation/application-receipt.json`. It exited 0.
- `check_registration.py --receipt …` on the real repository then exited 0 (PASS).
- The prior receipt (SHA256 `75892f5e490c9024b626fb4e516aa76a6d1a33d6bd7845d22a129d9d94d77621`) is now committed at [preparation/application-receipt-before-audit03.json](preparation/application-receipt-before-audit03.json). The new receipt's `previous_receipt.path` names the session scratch path, but the bytes are identical.

**Topic results file:** the stage now reads "ready for merge decision" (P3-APP-1). It feeds RESULTS.md.

**Ledgers:**
- Whitespace fixed in the PR24-owned batch-ledger and topic-ledger sections (P3-REG-2, ledger part).
- The readiness refresh appended (P3-REG-1).

**Other append-only additions:**
- an audit-03 acceptance line in the inherited e1-05 record;
- a gates.md AC-decision addendum (P3-FIX-3);
- one-line acceptance addenda in attempts/L2–L5 (P3-FIX-4);
- an n1 receipt pointer with link and hash in evidence-response-01.md (P3-FIX-7);
- a finalization section in preparation/record.md, which also records P3-APP-2 and P3-FIX-6.

**LOG:** header line 5 now states the final assignment (P3-FIX-1).

**Recorded and deliberately not changed (cosmetic):**
- missing spaces before digits in some applied registry prose (P3-REG-2, registry part);
- the L5-02 and L5-03 crosswalk rows each listing the other's alias, a `build()` behaviour; the two candidates remain distinct;
- a repeated sentence in the e1-05 addendum;
- the NOTE items P3-REG-5/6/7/8, P3-APP-3/5/6 and P3-FIX-5/6.

## Remaining limits, unchanged and disclosed

- **Original research targets still OPEN:**
  - PD-T055/F;
  - the broader L3 target (useful, degree-uniform, efficient selection);
  - PD-T056(G) and corrected models;
  - U2 and full G3 (n6–8; handoff01's n3–10 radius task);
  - scalar/IEEE activation;
  - external-code and literature tasks.
- **Gate verdicts:** G1 INCONCLUSIVE; G2 formal W/R PASS; G0/G4 RESOLVED, with their original failures retained.
- **L7:** MEASURED, conditional on the platform.
- **Provenance limits:** historical CPU, physical archival delivery and vanished temporary inventories remain disclosed limits.
- **Repository JSON:** 4.69 MB; about 4.81 MB if PR27 and PR28 also merge. That is within, but near, the 5 MB guidance, and the total includes non-generated JSON (P3-FIX-8).
- **Expected merge conflicts:** PR24, PR27 and PR28 all append to the batch ledger and ID_CROSSWALK, so whichever merges later will hit trivial textual conflicts, though no ID collides. A later peer must import PR24's assignments when it prepares.

## Independent check of the orchestrator's fixes

See [audit-03/CHK.md](audit-03/CHK.md), added after it ran.
