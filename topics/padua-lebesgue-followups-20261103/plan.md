# Development plan — T1–T4

Integrated 2026-11-03 from the handoff and individual workers' pre-run plans;
workers record their exact pre-run commands and stopping criteria in attempts/.
Rules/input: `3f5196cf3639407c25b021fa30f70cc1d3ae113a`;
base/main: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.

## Scope and allocation

The orchestrator integrates four bounded attempts. Frozen sources and scientific
registries stay unchanged. No work on the parallel effective-argmax bridge.

| Target | Worker / configured model | Ceiling | Acceptance and stop |
|---|---|---|---|
| T1 degree-eight maxima | t1_certification / gpt-6.1-sol medium | 6 h | Fresh complete interior and boundary, unchanged exact predicates, separate full replay; stop on a missing predicate, unresolved coverage, or time cap and preserve OPEN scope. |
| T2 edge-defect minimum | t2_t3_defects / gpt-6.1-sol xhigh | 4 h | Analytic proof or certified scoped counterexample; isolate any unresolved subclaim. |
| T3 general-position formula | same worker | 3 h | Rigorous integral/series and computable truncation error, checked against inherited central value; otherwise precise obstruction. |
| T4 corner constant | t4_constant / gpt-6.1-sol xhigh | 5 h | Parity-independent limit, explicit formula/enclosure and remainder; stretch terms only if proved. |

Time boxes are ceilings, not required runtimes. Workers stop at a checked result
or a precise obstruction. Each first mechanism receives its own documented
novelty gate and falsifiable test before substantial execution. Float agreement
does not certify a result. Failed/deferred routes are retained.

## Verification and evidence

T1 independent checker: t1_independent, configured gpt-6-astra high; exact
execution may be assigned to a distinct medium executor if resources permit.
Analytic results receive a distinct Astra high check after candidate files exist.
These supplement, and do not replace, the required Claude audit.

All computation stays in the sandbox. Regenerable bulk artifacts stay in
`/workspace/scratch/lebesgue-*`; small receipts record commands, code hashes,
versions, content identities and outcomes. Physical cold-storage delivery is
pending unless actually performed and verified. Preserve regeneration code.

## Publication boundaries

Checkpoint checked or honestly incomplete work at target boundaries and about
every ten minutes of changes. Open a draft PR with audit PENDING and permanent
fresh-range reservation; assign no final IDs during exploration. Keep the log,
topic results, evidence manifest, proposed shared-record edits and final report
consistent. Only the orchestrator writes these files or changes Git state.

After development, publish outputs first, then close handoff 01 in a separate
commit and open the next numbered Claude audit handoff. Only AC merges.
