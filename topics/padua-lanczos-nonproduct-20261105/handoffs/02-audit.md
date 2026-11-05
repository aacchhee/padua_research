# Handoff 02 — padua-lanczos-nonproduct-20261105 — substantive audit

- Status: open
- Previous handoff: [01-work.md](01-work.md)
- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: auditor and topic orchestrator
- Branch: codex/padua-lanczos-nonproduct-20261105
- Input head SHA: `38237fecb45f672f20a25d9989a90c31f3ff02a6`
- Main / base: `be9a8318150204711d5446d2ea26284cf1ed0819`
- Stage: AUDIT
- Written by / date: Codex, requested gpt-6-astra high · 2026-11-05

## Task

Perform the single substantive independent audit of this development batch,
with independent reruns of consequential computation at an appropriate,
explicitly recorded depth. Read the complete current `state/IDEAS.md`,
including all obstruction/disposition tables, and pertinent full entries and
linked theories: this branch has mechanism, negative and novelty content.
Choose depth independently; preserve actual commands, source/input identities,
results and remaining limits. Supplementary Astra checks do not replace this
Claude audit. Only AC merges.

1. Reconstruct the main P3 theorem and its admission/moment dependencies:
   `theory/p3-01-high-mode-weight-admission.md`,
   `p3-02-exact-moments-creators.md`, `p3-03-uniform-capacity-radius.md`.
   Check non-affine-productness against *all* affine axes, exact cutoff,
   actual weighted normal witness, all-source mirror upper, source/Gram
   scaling and quantifiers. Fixed eta is allowed but the mode changes with n.
   N4 is a sufficient analytic certificate, not maximal radius or strict
   small-n ordering. No N2 fit is a premise.
2. Reconstruct P5 admission/cubature and two-sided polynomial BJ/mirror
   bounds (`p5-01`, `p5-02`); check m>s, sharp cutoff, full-source upper,
   surviving normal lower and the fixed-rule capacity floor. No all-rule
   upper, sharp exponent or IEEE claim is made.
3. Audit common P4 definitions/model/transfer files and the scoped covariance
   obstruction. Check atomless localization versus finite atoms, explicit
   weights and source scales, moment transfer, restricted terminal-block
   corollary and the distinction between absolute capacity and ratio iff.
4. Audit P1/P2 admissions, source/recurrence records, candidate dispositions
   and N3 redirects. Exact low-degree identities are not capacity recursions
   or global/asymptotic spectral computations. Distinguish continuous disk,
   D36x9 and D65x9; no cubature equivalence or BJ=mirror follows from symmetry.
5. Audit P6's actual completed coverage and finite N2 outcomes against the
   final `report.md`, `gates.md`, `rounds.md`, receipts and raw identities.
   Include the reflection method's analytic reduction, exact guards and
   expansion to every original node/source. Ninety representative energies
   do not define a90-node measure or reduced error domain. Check per-case
   source catalogs for mixed original/reflection checker paths. Preserve
   all earlier cancellations/timeouts and failed speed experiments; never
   relabel an incomplete original receipt as successful. Generic/block
   FLINT paths were not promoted to degree16.
6. Audit protocol/novelty chronology, including the **new P3 gate-timing
   deviation** canonically disclosed in LOG. Later reading and mathematical
   acceptance do not cure/waive it; older AC acceptance on a different topic
   does not cover it. Give an explicit finding/disposition and refer any
   needed AC decision to AC after completing the audit. Do not suppress it.
7. Inspect the committed evidence inventory and storage limitations. Raw
   arrays are local working artifacts; no external cold-storage delivery is
   claimed. Code/data hashes and scientific-field digests are not prose pins.
   Check the repository-wide generated-evidence size budget as well: LOG
   records the measured aggregate and this topic's contribution; do not
   assume that per-file compliance establishes aggregate compliance.

## Read first

- Rules at this branch head: AGENTS.md, agents/WORKFLOW.md (PR29
  proportionate audit rules), agents/claude/CLAUDE_ROLES.md.
- Topic LOG, report, plan, gates, rounds and all `ideas/`, `attempts/` and
  novelty-gate records, including the bounded primary-source checkpoint.
- All topic `theory/` records and `p6-reflection-methods.md`.
- `independent-checks-math.md`, `independent-checks-scans.md` and their actual
  rerun receipts. These state accepted and omitted scope separately.
- Relevant predecessors PD-T033/038/039/053/055/069/136–146/324–339,
  PD-N062/063/116–118, IDEA246–267 and414–424; read full shortlisted
  records where needed, not only their registry titles.
- `literature/INDEX.md`, prior literature P3 comparison and the new P1
  source record. No priority claim is made; unread fulltexts are not proofs.
- `evidence-manifest.json`, `cold-storage.json`, indexed chunks and
  COLD_STORAGE.md for content identity, actual availability and regeneration.

## Useful rerun commands

Use fresh output directories/receipts, preserving original evidence:

```sh
python -I -B topics/padua-lanczos-nonproduct-20261105/code/p5_exact_checks.py --output /tmp/padua-lanczos-nonproduct-audit/p5.json
python -B topics/padua-lanczos-nonproduct-20261105/code/p4_weighted_check.py --output /tmp/padua-lanczos-nonproduct-audit/p4-weighted.json
python -B topics/padua-lanczos-nonproduct-20261105/code/p4_annulus_check.py
python -B topics/padua-lanczos-nonproduct-20261105/code/p4_terminal_check.py
python -B topics/padua-lanczos-nonproduct-20261105/code/p6_scan.py --family H24_222 --max-degree 16 --seconds 600 --work-dir /tmp/padua-lanczos-nonproduct-audit/H24 --receipt /tmp/padua-lanczos-nonproduct-audit/H24.json
```

Create the audit output parent first. The exact disk/reflection/fit commands
and frozen inputs are in their final receipts and method records; select new
paths, use each script's `--help`, and record any unexecuted high case honestly.
Do not rerun expensive generic/block inverse methods as if they were the
accepted high backend. Small guard/control runs are separately documented.

## Scope limits

No final IDs are reserved or assigned. Do not assign them during this audit.
Shared registries and ROOT RESULTS.md are untouched; registration belongs to
subsequent PR preparation, with reviewed diff and reservation refresh in one
readiness check. Do not require a separate mechanical audit round merely for
applying an already reviewed map; material changes still require focused
review under WORKFLOW. Preserve all failed/deferred candidates and limitations.

Do not change a developer proof and call it independently accepted. Return
findings; round1 has no third-round MINOR-fix exception. No rule/.github
changes, force pushes, tags or PR merges. Updating the topic from current
main follows WORKFLOW. Syvert requires AC's stated permission; external
artifact delivery remains pending and follows the repository's cold-storage
procedure if an authorized path becomes reachable. Complete the unaffected audit before
requesting any actual missing authorization or AC decision.

## Acceptance and outputs

Write `audit-01.md` with exact scope/input identity, model/effort, findings
(BLOCKING/MAJOR/MINOR/NOTE), executed reruns and residual limits. If findings
require changes, stage WORK and hand off to Codex with actionable items; if
accepted, stage PR and hand off preparation. Preserve any unchanged-claim
disagreement for AC under the PR29 response route. No claim becomes merge-ready
solely from this audit; final-ID/registry readiness and AC's merge decision
remain separate.

Commit audit outputs first. In a following commit change only this handoff's
status to `done in <audit-output-sha>` and add handoff03 for the appropriate
next agent, with exact input head and tasks. Update LOG/PR as appropriate,
push, and end with the short model-specific continuation prompt. Never
overwrite an earlier handoff's instruction body.
