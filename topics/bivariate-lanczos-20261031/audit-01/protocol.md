# Audit-01 protocol and provenance review

Reviewer: root Codex audit orchestrator, requested `gpt-6-astra xhigh`; root runtime model identity is not separately exposed. Mathematical audit workers explicitly use `gpt-6-astra xhigh`. Rules read at `3a9063b84d14ca0a5998378371e27643fde50a29`; candidate `5ccfac223f466a9105450365d8c6c3781ff7d922`. Date: 2026-11-01 (Europe/Oslo).

This is a protocol/evidence review, not an independent historical-literature survey. Existing mathematical mechanisms and negative claims are reviewed by the six named direction reports. No new scientific candidate or priority claim is introduced.

## Read scope

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; full `state/IDEAS.md`, including its obstruction and disposition tables; topic LOG, plan, progress, report, handoff, cold-storage manifest and sources README; input-code MANIFEST; reproduction REPRO record; pertinent literature index/corpus, HL SIMAX record, and L2/L3 prior-art records. The direction audits cover the full pertinent candidate records, linked proofs, reconstruction reports and retained failed mechanisms. Source reports/digests are not promoted into direct primary-source inspection.

## Executed identity checks

Command from repository root:

```sh
python topics/bivariate-lanczos-20261031/audit-01/check_inventory.py > topics/bivariate-lanczos-20261031/audit-01/inventory.json
```

Observed: all **67** theory hashes in the frozen handoff match both the candidate and working science; no theory file is omitted. All 12 input-script SHA-256/size/Git-blob identities match their manifest. All 16 reproduction-log SHA-256 identities match. The candidate has 216 output files in the recorded log/analysis directories, totaling **1,361,364 bytes**; none exceeds 1,000,000 bytes. The counted outputs satisfy the repository size limits. This validates committed identities, not original execution or scientific conclusions.

Audit environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0, mpmath 1.3.0. These differ from the developer environment; numerical reruns must be reported at their actual precision/scope.

The original input archive and third-party fulltexts are not attached. The archive's Windows cold-storage location and historical re-verification are documented; this audit does **not** claim retrieval or independent verification of those external bytes. The committed input copies suffice for the audited runs that actually import them. Large syvert runs remain unexecuted.

## Findings and readiness obligations

### P1 — Split substantive claims with different statuses before final registration

The workflow requires separate files/IDs for substantive proved, measured, conditional and open claims. Examples: T114 retains its proved derivative and reported gain measurements together with `Split into: none`; T304 retains a measured first-order isomorphism in its PROVED file. The direction audits assess these and other examples precisely. Keep the proved results PROVED under their stated scope; move the other substantive claims to their own registered homes, preserving history and crosswalk mappings. This is a status/registration finding, not a claim that every mixed-file proof is false.

### P2 — Finish literature-record consolidation before readiness

L2 and L3 prior-art reports introduce source statements and closest-predecessor comparisons absent from the canonical `literature/INDEX.md`, `CORPUS.md` and `records/` (for example Di Dio–Schmüdgen, Blekherman 2012 and Zhang–Su–Li 2024). Preserve the actual digest/metadata coverage in source records and register their statements during PR preparation. The existing reports explicitly disclose limited coverage and make no novelty claim. This is an outstanding consolidation obligation; it does not turn an unread source into a mathematical dependency or invalidate a self-contained local proof.

### P3 — Correct stale inventory and cross-reference prose

LOG and handoff/report describe 64 theory files; the frozen manifest and actual tree contain **67**, all matching. L5's direction audit also identifies report references to nonexistent N503. Refresh counts and references when answering the audit; retain the frozen audit target hashes.

### P4 — Keep the reported backward obstruction restricted to reading (E)

`report.md:23` proposes the standalone conclusion that interpolatory Padua recurrences have no Greenbaum-type backward model. The actual negative result excludes **exact** representation (or a sufficiently smaller residual) for specified consistent perturbations given as data. `theory/bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md:14` and N303's negative scope explicitly leave the actual floating-point, loss-of-orthogonality reading (G) OPEN. Preserve that qualification in the paper brief and any headline; no general negative answer to the original Greenbaum question has been proved. The report's opening already states this distinction correctly.

## Root follow-up of the exact normalization finding

The root read and separately executed the L3-framework auditor's `exact_framework_checks.py` after inspecting T302(b), Definitions and proof. It passed the independent Padua-n2 dual-certificate reconstruction and produced the rational normalization counterexample exactly: ten integer triangle-grid nodes, Vandermonde determinant 576; all three moment-matrix Sylvester minors positive; `r(0)=1/1000 > (1-theta)*epsilon=1999/2000000` but normalized cone distance `1/999 > theta*epsilon=1999/2000000`. Command: `OPENBLAS_NUM_THREADS=1 python topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.py > topics/bivariate-lanczos-20261031/audit-01/root-framework-rerun.log`. The final script's additional rational completion checks also pass. The root reran the final version after the auditor added those checks; source/output identities are in `artifact-manifest.json`. This root execution is a rerun of the auditor's checker, not a separately implemented checker or a developer correction. See L3-framework finding for the complete hypotheses and remedy. The full-space unnormalized conic statement is sound; its translation into the declared normalized residual threshold needs repair.

## Integration boundary

Fetched main `07c5f5465d6de306aa81dbe8ca1f615295163864` contains charter PR #2 and MZ PR #3. The frozen topic still bases on `d36722823441dc40c6e19d69a174459348dd309c`. The existing LOG records AC's instruction to defer main integration to PR preparation, so the audit preserves the science and examines the candidate read-only. No final namespace is allocated; the current batch ledger's fixed owner and accepted main IDs remain authoritative. Merge main, reconcile shared records/registries and obtain a disjoint reservation before final registration, then rehearse the relevant integration and audit material changes. No permission to merge a GitHub PR is inferred.

All six direction reviews are complete. Stage returns to **WORK** with the changes-required verdict in `../audit-01.md`. This protocol review alone is not mathematical acceptance. Developer source remains unchanged; final-ID and integration obligations remain for the later preparation stage.
