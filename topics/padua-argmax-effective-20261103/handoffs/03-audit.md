# Handoff03 — effective Padua argmax: Claude audit

- Status: open
- Previous handoff: [02-work.md](02-work.md), done in d790d58d8ecb5eb4ac455b2b7d638336d3bc0430
- Next agent/model/effort: Claude, **Opus5.5 xhigh**
- Role: auditor
- Branch: `codex/padua-argmax-effective-20261103`
- Input/output head: `d790d58d8ecb5eb4ac455b2b7d638336d3bc0430` (this handoff is published in a following commit)
- Main/base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`, refetched unchanged
- Stage: AUDIT
- Developer: Codex gpt-6-astra ultra; technical workers gpt-6.1-sol medium;
  supplementary independent reviewer gpt-6-astra high, as handoff02 directed
- Draft PR: https://github.com/aacchhee/padua_research/pull/19

## Task and scope

Audit the development outputs at their exact written scopes. The new
finite theorem covers17–32, hence the continuous certified range is2–32.
The isolated40 producer completed, but corrected acceptance reached its
600CPU-second cap;40 is not certified, and33–39 remain unrun. PD-T099 remains
OPEN: no explicit global threshold n0 and no all-degree bridge were proved.
Do not accept fitted/sampled constants as uniform bounds. Do not conflate
the new all-degree slope theorem with a fixed phase neighborhood.

Read AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the new
branch head and record that SHA. Fetch main; follow the workflow if it moved.
**Read the complete state/IDEAS.md**, not only a shortlist: this branch
contains mechanism and novelty content. Then read BRIEF, handoff02, plan,
LOG, report, all new theory/attempt/idea records, literature-g8.md,
independent-checks-01.md, independent-checks-canonical.md and
independent-math-checks-01.md. The supplementary
checks support development; they do not replace this audit.

Review the inherited dependencies actually used, especially PD-T101,
PD-T210's constructor/finite-cover proof, PD-T227 corner formulas,
PD-T228/229 scope, and PD-T231's generic edge reduction. Preserve original
statements when assessing the dated narrower variants/obstructions.

## Principal audit targets

1. **Corner spectrum and all-degree local result.** Reconstruct codex-06a's
   reflected sign data, endpoint exceptions, cosine sums and a=0 correction;
   denominator positivity, row reflection, column positivity and Lambda_c>=2.
   In06b verify both normalized slope bounds, the even-degree alternating
   correction, zero-cardinal first variation, affine sign radius and Taylor
   remainder. The proved radius is1/(2[n(n+1)]^3), of order n^-6 physical;
   the desired order n^-2/fixed phase zone and weighted-energy bound remain OPEN.
2. **Finite global theorem.** Check its final explicit degree set against
   the committed witnesses and acceptance receipts. Do not fill unrun gaps
   around an isolated probe. Audit the separate C/GMP producer and C++/GMP
   checker, schema/provenance checks, prefix coverage and strict corner-leaf
   equality argument. Shared formulas/order/dependencies are disclosed;
   arithmetic kernels are separate. Final source provenance was regenerated
   after an intermediate source-hashing race was fixed. A final native-checker
   inspection also found uncanonicalized GMP rational summands; the fix
   canonicalizes every transform-weight term before arithmetic. Inspect
   the impact record, exact Fraction weight comparison and corrected full
   replays. Old native receipts remain historical and do not substitute for
   corrected acceptance; source hashes distinguish the two versions.
3. **Exact edge spots.** Three whole-cell comparisons, n13/17/24, with strict
   rational margins1/20,1/40,1/100. Seven leaves; inherited arithmetic kernel
   shared by producer/checker, explicitly disclosed. Verify the retained
   small certificate, target lower bounds, cover and11 corruption controls.
4. **Negative scopes.** G7-F only refutes the specified fixed-sign individual
   cardinal representation on the n4 diamond; original G7 was ill-defined.
   The spectral negative at n3 and the (3,1) gradient ratio obstruction
   refute only their stated proof steps. In particular an affine sign
   failure does not establish actual-cardinal sign instability.
5. **Gates and costs.** G2/G3/G4 and G6 are MEASURED finite samples.
   G5 cannot be evaluated without uniform remainder/defect/far-margin models.
   Preserve its original decision rule. G1 labels CPU vs wall, hot path vs
   full driver, producer-only vs producer-plus-checker, and sparse-fit
   extrapolations. Python checker CPU was not benchmarked, so its producer
   capacity estimates are not full certification-pipeline budgets.
6. **Novelty/source coverage.** Check all dispositions against complete
   IDEAS. R5 coefficientwise sign duality is equivalent to IDEA-320's l1
   bound. No1-D theorem was transferred; source reading/access gaps and the
   Brutman survey journal correction are explicit. No fulltext is committed.

## Evidence and bounded replay

First verify the source/evidence inventory from the repository root:

```sh
python topics/padua-argmax-effective-20261103/code/evidence_manifest.py
```

This is a hash-integrity check, not a mathematical replay. Build and replay
selected exact witnesses with the commands in the finite theorem and native
checker README. Use independent bounded technical workers if the workflow
permits; do not run pure Python above32. The overlap9–24 reference checks,
fresh independent17–24 run and native controls are recorded in committed
compact summaries. No new exhaustive campaign is necessary merely to audit
existing witnesses. Run the controls and enough actual replays to assess
soundness independently, recording precisely which degrees were executed.

The small essential certificates remain in `evidence/`. A verified local
archive of16 bulk raw files plus its manifest is linked in COLD_STORAGE.md;
external/Windows delivery is pending. `cold-storage.json` is a custom scratch
inventory because tools/cold_storage.py handles historical committed Git
blobs, and these raw files were never committed. Do not claim that pending
external delivery or exact byte recovery after workspace loss is complete.

## IDs, files and completion

Permanent ranges: PD-T246–265, PD-N084–091, IDEA336–355, LIT466–473.
First pushed reservation commit `ed8db2fc364d0ba34c3c06815460b3b2971787b5`.
Final IDs remain unassigned. Completion recheck found concurrent PR20
(`codex/padua-lebesgue-followups-20261103`) using the disjoint next ranges;
its edge/corner followups are unmerged and are not premises of this branch. Review ALLOCATIONS.md and allocation-scan.json;
rescan all reservation sources before final assignment/preparation. Unused
IDs remain permanent gaps. Proposed dated shared-record edits are literal
old/new blocks in proposed-record-changes.md; no shared scientific registry
has been edited in development.

Write audit-01.md with findings, accepted scopes, executed checks and any
remaining blockers. Follow the repository audit workflow for response or
preparation; publish a new handoff only after committing the audit outputs.
Do not merge or mark ready merely because supplementary checks passed.
Only AC merges. Keep the draft PR's WORK/AUDIT/PR sections current.
