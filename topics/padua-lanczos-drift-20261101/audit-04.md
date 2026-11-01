# Audit 04 — bounded independent re-audit of response-03

- Auditor/orchestrator: Codex, user-requested `gpt-6-astra` high; resolved
  serving model/effort is not independently exposed. One fresh-context scope
  reviewer was explicitly configured `gpt-6-astra` high.
- Rules/read head: `39b3c5d8690566ce461e6e3a0a628e772a695dbc`.
- Candidate: `02bd97b892ed409ec64e9b281130c71a85e914e9`; scientific/code output
  `69caca061cda555a561f73e66226f5a59dbd412d`. The candidate adds LOG only;
  publication adds only handoffs09/10. Delta base: `3cca9b929ac006a5ed4295b3beba909dfd602271`.
- Main: `28aaa20861d08074b77efc74eaef75cdcb36234d`; sole other open draft
  PR12: `0dd4a6df2db4a2019541604bb97c05926ab3c22b`.
- Date: 2026-11-01. PR15 stays draft during preparation. No final IDs assigned.

## Verdict

**ACCEPT within the handoff10 delta scope: A03-L1/L2/L3 RESOLVED.
No new high, medium or low findings. Stage PR (preparation pending).**

The checker now requires every regeneration file when that mode is requested
and returns failure status1 for missing inputs. The minimum-comparator
refutation and reference-repair geometry are correctly scoped. Accepted
mathematical results and claim statuses from audit03 remain in force; this
bounded audit does not repeat the full research campaign.

| Finding | Disposition and evidence |
|---|---|
| A03-L1 | RESOLVED: fresh independent execution regenerates all four outputs; committed-only and complete modes pass with exit0. Nonexistent-directory and four separate one-file-omitted cases fail with exit1, false regeneration/all_pass flags and the correct missing-file lists. |
| A03-L2 | RESOLVED: full-graph squared bound conventions, one-comparator proof and both-comparator refutation are correct; alt-only reversal is explicitly scoped to the named-alt target. The strict target's equality boundary and logical countermodel check exactly. |
| A03-L3 | RESOLVED: reference information is distinguished from geometric separation; the correction is identified before normalization, and outside-span separation is conditional on the checked normal component. Recipes, guard, H17 and deferred/no-run disclosures are preserved. |

## Actual executions and provenance

The root inspected the entire checker diff and its inputs/finite-check flow.
`check_regenerated` initializes its flag from `is_dir()`, marks either kind of
missing file as failure, and records each required name. Its conjunction cannot
be reset to True by later valid files. The CLI writes its JSON and exits1 when
`all_pass` is false; optional committed-certificate-only checking is preserved.
No developer code or prior evidence was fixed by the auditor.

From `/workspace/padua_research`:

```sh
PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B topics/padua-lanczos-drift-20261101/checks/audit-04/check.py --work /workspace/padua-drift-runs/audit-04/E1 --regenerate --output topics/padua-lanczos-drift-20261101/evidence/audit-04-checker.json
python3 -B topics/padua-lanczos-drift-20261101/checks/audit-04/scope_check.py
python3 tracks/bivariate-lanczos/code/drift/integration_check.py --head 39b3c5d8690566ce461e6e3a0a628e772a695dbc --main 28aaa20861d08074b77efc74eaef75cdcb36234d --pr PR12=0dd4a6df2db4a2019541604bb97c05926ab3c22b --output topics/padua-lanczos-drift-20261101/evidence/audit-04-integration.json
python3 -B topics/padua-lanczos-drift-20261101/checks/audit-04/inventory.py
```

The root checker driver executes, separately from the developer, both
`e1_reproduce.py --set triangle|rotated` runs and both
`e1_cgs2.py --set triangle --degree 12 --rule pivot` /
`--set rotated --degree 12 --rule alt` runs. These are actual fresh producer
executions, with two concurrent workers and single-thread BLAS, followed by
seven checker cases: none, absent, complete and four omissions. Commands,
timestamps, elapsed times, source/input hashes, raw output hashes and complete
regeneration comparison fields are in
[audit-04-checker.json](evidence/audit-04-checker.json). Exact comparator uppers
equal committed U_T/U_R; both reproductions and explicit-projection checks PASS
with correct producer/certificate pins. All65 committed finite checks pass in
each invocation, including intentional missing-regeneration failures.

This environment uses CPython3.12.14 and python-flint0.9.0; the developer used
CPython3.13.18. Fresh raw bytes differ in paths/timings/metadata. The audit
compares exact arithmetic fields and pins, not timing-dependent whole-file
identity with the developer's outputs. The new receipt agrees with the
response03 receipt's expected exit/result/missing-file behavior. The historical
response02 receipt is unchanged. Existing independent mathematical
implementations from audits01–03 are reused as accepted coverage, not reported
as newly executed here. These runs do not add an IEEE-realization or all-degree
claim. Raw files stay in regenerable working storage outside Git.

The separate [scope report](checks/audit-04/Scope.md) reconstructs the corrected
inequalities and projector geometry independently. Its standard-library
Fraction checker proves the elementary countermodel/equality identities and
checks full-file preservation outside the corrected row/paragraph and History.
[audit-04-scope.json](evidence/audit-04-scope.json) pins its inputs/code/results.
For nonnegative capacities the refutation chain is

    K_BJ² <= U_BJ² <= 100 min(L_alt²,L_pivot²)
                   <= 100 min(K_alt²,K_pivot²).

For q in the stored span, P its reference-prefix projector, a=||Pq||>0 and N
the stored normal projector, `N(Pq-q)=NPq` and `N(Pq/a-q)=NPq/a`. Reference
construction alone does not force either vector nonzero; the new condition is
therefore the appropriate separation criterion. Neither argument changes the
PARTIAL scalar target, MEASURED experiment, INCONCLUSIVE test or deferred H17.

## Reading and preservation

Root read AGENTS, WORKFLOW and CODEX at the full read-head SHA, handoff10,
audit03, response03, latest LOG, all response03 changed code/theory/idea/results
text, the developer receipt, the scope report and the relevant inherited
integration/pin machinery. Its checker/protocol scope introduces no novelty;
it does not claim a second full root novelty gate. The scope reviewer read
the full783-line IDEAS registry, obstruction/disposition tables, full relevant
PD-T055/043, PD-N013/016 and L2 predecessors, as detailed in Scope.md. No new
mechanism, paper reading, priority or exhaustive literature conclusion is made.

[Inventory and output pins](evidence/audit-04-inventory.json) verify:

- Exactly nine candidate paths changed; scientific/current bytes equal the
  candidate. The later publication changes only handoff status/instructions.
- All125 frozen prior audit/check/response/evidence files are byte-identical to
  the delta base, including response02 evidence. All77 original theory files
  and protected paths are unchanged from main.
- Main and current PR12 have identical four-registry/two-ledger bytes. Existing
  reservations remain in force and unassigned; no scientific registry, root
  RESULTS or final-ID change was made in this audit.
- The conservative whole-campaign inventory, counting prose/code/results as
  well as generated evidence, stays below decimal5MB; largest file616693bytes.
  No historical artifact was deleted or split to meet the limits.

Fresh GitHub inventory in [audit-04-remote-state.json](evidence/audit-04-remote-state.json)
shows only drafts12/15 open and no closed-unmerged PR among the13 returned.
The integration rerun PASS explicitly includes a clean PR12 merge-tree and
temporary squash tree equality at the read head. Subsequent audit artifacts,
LOG, own results and handoffs do not change scientific/protected bytes.
No live main/PR merge was performed and readiness is not yet declared.

## Remaining work and limits

The accepted formal finite inequalities and analytic results retain their
stated scope. The rotated scalar factor-ten conjunct, all-degree drift,
general staircase safety, PD-T055, PD-T075(U2) and PD-T056(G) remain OPEN.
Original raw-artifact delivery to Windows cold storage remains a separate
pending archival task; committed evidence and regeneration remain sufficient.
This audit supplies no additional degree12 full normalized-trajectory replay,
new fit suite, repair experiment, optimal-rate theorem or source/archive claim.

Open handoff11 for PR preparation: fresh union/reservation checks, final IDs
from the existing ranges, literal approved proposals, record14 tombstone
removal, registry/crosswalk rows, only this topic's root RESULTS section and
recorded content-impact/readiness checks. Preserve all accepted statuses and
earlier handoffs. Only AC merges.
