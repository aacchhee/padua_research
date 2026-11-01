# Padua–Lanczos drift: independent checks

- Base/rules SHA: `cf89b140530d5838bdb208a8c28f3e7aa676ace3`.
- Status: supplementary independent checks EXECUTED; required Claude audit **PENDING**.

| Scope | Required check | Checker / pinned input | Executed commands and outputs | Disposition |
|---|---|---|---|---|
| E1 | Normal derivative and rational bounds; decisive degree12 finite comparison | Separate gpt-6-astra xhigh checker; file hashes in checks/ report | Own Fraction checker: 1,800 normal-vector identities on 15-point degree2 triangle; separate full exact T24 BJ/pivot and rotated Q24 BJ/alt/pivot reruns | Tightened ratios >100 confirmed; original KHS-only comparison inconclusive; documentation findings returned and corrected |
| E2 | Full scalar-operation graph and any all-degree claim | Separate Astra checker | Analytic bridge reconstructed; full scalar run/check status in E1 and checks/ | All-degree exponential/matching theorem remains OPEN |
| E3/E4 | Polynomial-surrogate upper certificate, filtered criterion, quantifier and ten-node obstruction | Separate Astra checker | Analytic reconstruction; independent rational evaluation of the ten-node table | No gap reported within the stated restricted scopes; no original PD-T055 resolution |
| E5 | Corner-witness asymptotic proof and square-case residual-aware family | Separate Astra checker | Independent derivative/limit reconstruction, 100-digit corroboration and own exact matrix/moment calculations | Analytic arguments reconstructed; high-precision values are corroboration only |
| E6 | Execute actual upstream source on both hard benchmark cases | Root Codex orchestrator, no E6 development; exact runtime variant/effort unexposed | Separate command below; two complete case JSON objects compared equal to developer records | CONFIRMED within measured scope; no general fit guarantee |
| Protocol / evidence | Provenance, splitting, candidates, file-size/public-repo checks | Root; exact check receipts and final snapshot manifest | Recorded separately in LOG and manifest | Final freeze checks pending until all worker outputs integrated |
| External audit | Claude audit of Codex development, as required by repository workflow | Pending handoff | Not executed here | PENDING |

For every completed check, add checker identity and requested/actual model metadata, exact SHA or file hashes, inputs, commands actually executed, environment, independently generated outputs, findings and limits. Reading another worker's output is review rather than a rerun. Supplementary independent subagent checks do not replace the external Claude audit. The developer cannot approve its own work.

## Root E6 execution

Executed separately from the E6 developer:

```sh
OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --sets rotpi4 triangle --output /workspace/padua-drift-runs/root-independent-e6.json
```

Both complete `cases` objects match the developer's twelve-set output exactly,
including input identities, reference conditioning, all six methods and fit
metrics. The committed receipt `evidence/independent-e6-root.json` contains
output/code hashes, bytes, Python version and essential numeric results. The
uncommitted full rerun is locally retained under the stated output path.
This used the same pinned upstream polyrat source, NumPy 2.3.5 and one BLAS
thread; it is an independent execution, not an implementation-independent
derivation of floating-point behavior.

## Independent mathematics scope

The supplementary checker uses requested gpt-6-astra xhigh; resolved runtime
metadata is not independently exposed. It read complete `state/IDEAS.md` and
reconstructed the claimed reductions before checking outputs. Its durable
report and exact essential evidence are under `checks/` and `evidence/`;
the report pins read files by SHA-256 and distinguishes executed reruns from
analytic review. New scalar-graph or failed-path additions after its first
snapshot require an explicit follow-up, not inferred coverage.
