# Response-04 — direct Codex integration corrections

2026-11-01. **All five technical integration findings are corrected; independent audit-05 is CLEAN. PR #10 is ready for AC's merge decision.** AC subsequently approved the scoped output-budget exception below, resolving A4-P1. A topic-only size check is not presented as compliance with the repository aggregate cap.

AC explicitly requested: **“Can you resolve the integration here without an extra claude loop?”** AC also confirmed: **“I confirm that pr10 goes in next. All other drafts will be adjusted after pr10 is merged.”** These instructions authorize Codex to make these preparation corrections directly and supersede the ordinary extra Claude handoff and broader draft-sequence rehearsal for this repair. They do not authorize a merge or silently waive an output-size rule.

Developer/orchestrator: Codex, requested `gpt-6-astra xhigh`; root runtime model/effort metadata is not independently exposed. Registry and literature implementation was delegated to bounded continuing Astra/xhigh workers after their audit-04 reports were frozen. A **different** continuing Astra/xhigh auditor, who implemented none of these fixes, supplies audit-05. Original Claude scientific development, accepted proofs, evidence and audit-01–04 records are preserved.

Rules/source read: `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`. Frozen audit-04 baseline: `183d33760e8d6c3ecdeb588576bd65ba312f65fe`. First correction candidate: `d55504eef364542a50b455b61fb6c48ed81996be`. **Final technical candidate: `98945cbcf10c4f8eb53f77c996db358392d42391`.** Main: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`. Rules unchanged. No novelty, priority or new scientific result is claimed.

## Dispositions

| Audit-04 item | Correction and scope | Disposition |
|---|---|---|
| A4-M1, current IDEA outcomes | All 100 candidate summaries use explicitly reviewed current dispositions in `pr-prep/registry-semantics.json`, with source hashes. Historical corrections, failed/equivalent/deferred variants, mixed positive/negative parts, and post-hoc criteria remain visible. IDEA-135 is refuted as titled; the narrow measured control remains. Initial `pending` placeholders are removed. | Resolved |
| A4-M2, dependency/reference fidelity | All 77 forward-reference lists are explicit and reviewed. T053/T078 have no registry dependencies; T050 excludes T054, whose result discharges an optional assumption, while T054 cites T050 definitions only. Nondependency explanations remain in the semantic data rather than graph-readable dependency cells. Contextual shorthand is fully converted; literal norm/absolute-value bars are escaped. | Resolved |
| A4-M3, public summaries | CURRENT and the report identify formed F=Y versus injecting J=X, exclude MEASURED T035 from the proved range, require Π_(2n+1)-determining nodes and small perturbations for zero radius, and retain U(2m+1) in the fixed-start obstruction. Report/track audit metadata is reconciled; theorem bodies and statuses are unchanged. The PR description is updated from this corrected record. | Resolved |
| A4-M4, canonical source | LIT-023 and LIT-259 coexist in the accepted `mourrain-telen-vanbarel` source record, preserving their entire statement blocks and reading qualifications. The other key is a redirect. INDEX, CORPUS and both crosswalks resolve the canonical source without changing IDs. | Resolved |
| A4-L1, safe replay | The existing 404-entry map is immutable input. The allocator accepts finalized aliases, validates source identities/inventories/headers before any write, supports read-only `--check`, and preserves correct headers. Repeated default and apply invocations are byte-stable. Bad headers or altered allocation bytes fail before writing. All four generated artifacts are synchronized with the submitted tree. | Resolved |
| E1 / E2, reading provenance | BPS's generic note now credits the actual orchestrator reading rather than an L1 digest reading that never occurred. A separate Ten Lectures coverage record preserves the historical partial digest and 1D-only limit, linked from LIT-261. No new numbered statement, source rereading or proof status. | Applied |
| A4-P1, repository aggregate-output gate | AC explicitly approved a PR #10-only exception for existing evidence and these integration-review records. The 1 MB per-file limit remains, and no future experiment output is authorized. Historical evidence is preserved. [Exact authorization](response-04/AC-EXCEPTION.md). | Resolved by AC exception |

The independent reviewer caught one additional package issue in `d55504e`: regeneration changed stale negative-row artifacts. Commit `98945cb` synchronizes `negative.rows.md` and the published negative-results table, corrects shorthand/escaped bars/PD-N025's proved label, and removes truncation so IDs and scope cannot be cut mid-token. The underlying negative statements, statuses and evidence are unchanged. This narrow successor was independently rechecked, rather than approved from the first candidate's result.

## Narrow impact map and preservation

[impact-check.json](response-04/impact-check.json) records the exact **21 changed/new paths with SHA-256 and byte sizes** from the frozen audit-04 baseline to the final candidate. Categories:

- Registry rendering: PROOF_STATUS, IDEAS, generated proof/idea/negative rows, and the negative-results summary table.
- Preparation implementation: allocator, explicit current semantic data, and strengthened allocation-envelope/canonical-source checks. The map is byte-identical.
- Literature: canonical TNF record and redirect, BPS provenance, Ten Lectures coverage, INDEX/CORPUS and crosswalk source links. All existing 292 numbered statement blocks remain intact.
- Summaries/coordination: CURRENT, report, track README, and batch ledger's current AC-confirmed merge order. Accepted reservations and other topics' content remain.

The root's read-only [impact checker](response-04/check_impact.py) passes: **676 protected pre-existing topic/track files are byte-identical**, including all **77 theory files**, **139 code files**, scientific direction/reproduction evidence and frozen audit-01–04 records. Counts overlap; they are not additive. The 404-entry map bytes and crosswalk allocation pairs are unchanged. All main registry table rows remain. Status counts remain **38 PROVED, 34 MEASURED, 4 OPEN, 1 CONDITIONAL**. This is preservation of the accepted scientific envelope, not a new proof audit.

Actual root commands from repository root:

```text
python3 -B -I topics/bivariate-lanczos-20261031/response-04/check_impact.py > topics/bivariate-lanczos-20261031/response-04/impact-check.json
python3 -B -I topics/bivariate-lanczos-20261031/pr-prep/allocate.py --check
python3 -B -I topics/bivariate-lanczos-20261031/pr-prep/check_integration.py
```

Final commands exit 0. The impact checker's initial development run also asserted a terminal newline in the negative-results summary; that irrelevant formatting requirement was removed. It was an auditor-checker assumption, not a scientific or integration failure.

## Rehearsal and remaining gate

Root rehearsed **main→PR #10 only**, as AC requested, in detached `/tmp/padua-pr10-fixed`: squash `98945cb` onto main `9739a0c`, **zero conflicts**, resulting tree **`d3447f63f656f3fe3eb6f6f14b7aa6eda092582b` equals the candidate tree**. Both allocator `--check` and integration checker exit 0 on that staged tree. [Receipt](response-04/rehearsal.json), [allocator output](response-04/allocator-check.json), [integration output](response-04/integration-check.json). Main was not changed or committed. This does not approve other drafts; AC confirmed they adjust afterward.

No large-M experiment, mathematical producer or unchanged certificate suite was rerun. No primary source was reread. AC's Windows results and archive were not accessed. The final publication adds only response/audit receipts, log/readiness metadata and the PR-description source beyond the pinned technical candidate; those additions must be recorded separately from its tested tree.

Technical verification is accepted without another Claude loop. **A4-P1 was resolved afterward by AC's explicit scoped exception**, retained in [AC-EXCEPTION.md](response-04/AC-EXCEPTION.md). Audit-05's earlier conditional wording remains unchanged as history; the exception supplies its remaining readiness condition. All technical findings and the policy gate are dispositioned. AC alone decides and performs the merge. Later drafts refresh from the merged PR #10 and reconcile their own shared registries/reservations.
