# Handoff07 — registry diff and reservation readiness check

- Status: open
- Previous handoff: [06-preparation.md](06-preparation.md)
- Next agent / model / effort: Claude, Opus 5.5 high
- Role: readiness auditor and topic orchestrator
- Branch: codex/padua-lanczos-nonproduct-20261105
- Input head SHA: `418b8166121d3717c4d1916ae6c4619953cb4573`
- Main/base: `be9a8318150204711d5446d2ea26284cf1ed0819`
- Stage: PR (draft until this readiness check passes)
- Written by/date: Codex, requested gpt-6-astra high, 2026-11-06

## Task and boundary

Perform the single readiness check required after audited preparation:
review the applied registry diff and refresh the final-ID reservation union.
This is not another substantive audit. Audit01 accepted all stated proofs;
audit02 accepted A3 and the response dispositions. Do not reopen accepted
mathematics, the reflection method, finite outcomes, three INCONCLUSIVE N2
screens or AC's settled Q1–Q3/storage decisions.

Read AGENTS.md, WORKFLOW, Claude role, LOG, audits01/02, response01,
handoff06 and [ALLOCATIONS](../ALLOCATIONS.md). No new novelty claim is
introduced by mechanical registration; state that scope/exception if no
full catalogue reread is needed for this check. Review the full relevant
new registry entries and their source records for faithful application.

## Exact preparation and registry diffs

Reservation checkpoint, published before any assignment:
`6b313567702b0ec465330e2ca4b8186d8be210a4` (linked in PR30).
Mechanical registration output: `418b8166121d3717c4d1916ae6c4619953cb4573`.

```sh
git diff be9a8318150204711d5446d2ea26284cf1ed0819 418b8166121d3717c4d1916ae6c4619953cb4573 -- PROOF_STATUS.md state/IDEAS.md literature/INDEX.md ID_CROSSWALK.md state/CURRENT.md RESULTS.md
git diff 72cbce7816cdd6e02e799c85cb68f79001f831f7 418b8166121d3717c4d1916ae6c4619953cb4573 -- topics/padua-lanczos-nonproduct-20261105 results/padua-lanczos-nonproduct-20261105.md
```

Check:

- PD-T472–488:17 existing records,13 PROVED and4 MEASURED. Preserve exact
  scope/model, including the P1 chain **under BJ** and finite-only probes.
- PD-T489–494: six new durable homes for existing OPEN targets. Compare
  them to the retained original candidates/handoff01 and accepted audit
  scope; no exponent, parameter point, sufficient condition or theorem was
  invented. Supporting lemmas do not upgrade them to PARTIAL.
- PD-N178: scoped covariance-only absolute-capacity obstruction, PROVED;
  only IDEA-581 is REJECTED: refuted. Original ratio iff remains OPEN.
- IDEA-570–584:15 candidates with all abandoned/equivalent/deferred routes
  and unnumbered aliases retained, no administrative negative result.
- IDEA-576 permanent P3 timing qualifier/AC date unchanged. IDEA-577 fixed
  perturbation is deferred to an explicitly assigned follow-up; no candidate
  proof status or PR precondition. D65 remains deferred with a resume condition.
- LIT-630: bounded developer source-reading coverage, not a source-theorem
  proof, priority clearance or a duplicate of LIT-292 Chapter3.
- Exact namespace/case mappings in CROSSWALK, including P4-01/P4-04,
  P2-03/P2-04 and lowercase p5 theory versus uppercase P5 candidates.
- Only this topic's section was appended to RESULTS; prior shared-registry
  bytes were preserved. New shared entries contain content/dispositions and
  completed audit links, not process stage or pending tasks.
- Final IDs and full provisional aliases preserve old heading anchors.
  Mechanical reversal of existing records changes only IDs/aliases/anchors,
  three allocation-state lines, one heading link and audit02 MINOR B1.
  B1 now unambiguously says |eta|=1 lies outside the admitted positive
  full-support family. No mathematical statement/proof/status beyond
  audited content changed. Any actual unexpected material change must be
  identified, not silently accepted as registration.
- Code, frozen receipts, inventories and audit records are byte-unchanged.
  N0 is verification evidence only, with no PD-T assignment. Routine
  terminal/reflection corollaries receive no extra scientific ID.

No new scientific run is necessary merely for registration. Any execution
chosen independently must preserve actual scope and original evidence.

## Reservation refresh — mandatory at this readiness step

Fetch current main and every open PR, drafts included. Query the complete
all-state PR population, including closed-unmerged branches not already
recorded as retired. Read all ledger copies and final IDs in the four
registries at each current head; include all retired reservations and
permanent unused gaps. Follow WORKFLOW if any previously unknown retired
reservation cannot be reconstructed. Do not reuse/shift any range.

Permanent own reservation: T472–501(30), N178–180(3), IDEA570–589(20),
LIT630–632(3). Assigned: T472–494(23),N178(1),IDEA570–584(15),LIT630(1).
Unused T495–501,N179–180,IDEA585–589,LIT631–632 remain permanent gaps.
Priority stays first publication6b31356, not assignment or this audit date.

Initial complete union at main be9a831, PR27fc10953, PR284e87fc0 and own
PR3072cbce7 read62 ledger/registry copies and13 distinct full ledger versions.
The highest existing endpoints were T471/N177/IDEA569/LIT629. Before assignment
publication PR27 advanced to `8dc1521cf68f7780bd10e02495f6f71a639c03c6`;
all16 ledger/registry files were reread and byte-identical to fc10953.
Main and PR28 were unchanged. The all-state population has29 returned PRs
(no PR7),26 merged and open27/28/30, no closed-unmerged. The initial prose
count30/27 was corrected in preparation; scanned heads/files and bounds
were unaffected. These are historical pins, not a substitute for your fresh
readiness query. Foreign four-digit BTTB LIT aliases are not Padua final IDs.

If main has moved, reconcile it without rewriting published history and
record the resulting registry impact. No multi-PR merge order or peer
approval is inferred. Only AC merges.

## Acceptance and outputs

Write `readiness-01.md` with exact checked input/current heads, model/effort,
registry-diff verdict, B1 disposition, fresh union/maxima, collision check,
actual verification and residual limits. Update LOG/PR with correct WORK /
AUDIT / PR sections and the readiness decision.

If clean, the PR may be marked ready for review; never merge it. State the
exact AC decision requested, and refresh reservation safety again if main
or a peer ledger changes before AC's merge. No final claim is upgraded by
readiness. If no assigned agent work remains, close this last handoff after
committing the readiness output and record completion of agent preparation;
AC's merge decision remains separate. If findings require work, return them
to Codex with a new numbered handoff08.

Commit readiness outputs first, then change only this handoff's status to
`done in <output-sha>` in a following commit, adding handoff08 only when
further agent work exists. Push before replying. Preserve earlier handoff
bodies. No rules/.github edits, force-push, tags or agent merge.
