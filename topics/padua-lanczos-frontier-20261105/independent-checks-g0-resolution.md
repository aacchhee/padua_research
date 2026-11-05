# Supplementary G0 resolution review — 2026-11-05

**Verdict: RESOLVED at the arithmetic-sensitivity explanation level permitted by handoff 02.** This is an additive disposition of the T24 degree-12 replay discrepancy under the unchanged G0 criterion. Preserve the original dated FAIL and its receipts. No acceptance tolerance, universal bit-equality requirement, theorem status, or historical measurement is changed. The precise historical CPU dispatch, library binaries, and computed basis are still unknown. This review does **not** certify that one identified historical kernel produced the old numbers.

Reviewer: distinct Codex supplementary checker, requested `gpt-6-astra`, high; serving model/effort metadata is not independently exposed. Rules and input head: `f85c7b5c83822ff60b62c84bed1ec6ae31628422`. Frozen producer snapshot: `8359bf7a047d9a212bd841224fb97a458cb7435e`. Upstream polyrat: `6903d7af9995c9d88e661fb229626696e00fdfba`. No Git mutations were performed. This is supplementary Codex checking, not the later required Claude scientific/protocol audit.

## Scope and gate interpretation

Read AGENTS, WORKFLOW, CODEX, handoffs 01 and 02, the topic log/plan/report/gates, the original independent G0 report and compact receipts, frozen drift README/E6 provenance and source, prior audit-02 E6 record, and PD-T142's full statement and proof. Inspected the attribution script, the frozen L2 implementation, and upstream Arnoldi implementation. Source hashes were checked again during the independent executions.

**Novelty-gate exception:** this review only diagnoses an existing replay mismatch using existing recurrence identities and reference checks. It generates no new scientific mechanism, candidate, negative claim, literature-priority statement, or target result. The complete IDEAS read is therefore omitted under WORKFLOW's explicit no-novelty audit exception. This exception does not cover subsequent L1–L7 work or cure the already disclosed prospective novelty-gate timing deviation.

Handoff 01 says: “any unexplained mismatch stops the campaign until it is explained.” Handoff 02 explicitly permits “an arithmetic sensitivity/error-propagation analysis” to explain a class of variation without recovering the historical CPU, provided it supports the observed scales and retains uncertainty. I use that permitted explanation standard. Agreement with a newly chosen tolerance, or simply finding the differences small in absolute units, would not suffice.

## Executed independent checks

The new independent checker [code/g0_independent.py](code/g0_independent.py), SHA-256 `9742f3fe95f77f6142aad56dc7176e256241a32c7ef1106fc632ec6c6ee64c7f`, executes the unchanged six E6 producers and checks all five local Python pins, four upstream source pins, and the identical input hash `bd2a98cab06f16494f95d89697091aeacebd3a87fdbd760ffaac707bfc57a929`. It then builds the complete degree-12 monomial matrix at the **exact binary64 node values** in 384-bit Arb arithmetic. The residual

`Q - V (V^T V)^(-1) V^T Q`

uses a separate reference construction from the developer's Jacobi/Dubiner calculation. The solve returned finite enclosures; maximum residual-entry radius was below `1.44e-88`. Final singular values are evaluated in binary64, so the displayed values remain MEASURED diagnostics, not a computer-assisted proof. The computed Q singular values differ from one by about `1e-15`; replacing their residual norm by the actual span gap changes these displays below the shown precision.

Actual commands, from the repository root:

```sh
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 python -B topics/padua-lanczos-frontier-20261105/code/g0_independent.py --snapshot /tmp/padua-lanczos-frontier-g0/validation/replay --external /tmp/padua-lanczos-frontier-g0/polyrat --output-dir /tmp/padua-lanczos-frontier-g0-review/baseline
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Nehalem python -B topics/padua-lanczos-frontier-20261105/code/g0_independent.py --snapshot /tmp/padua-lanczos-frontier-g0/validation/replay --external /tmp/padua-lanczos-frontier-g0/polyrat --output-dir /tmp/padua-lanczos-frontier-g0-review/nehalem
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Haswell python -B topics/padua-lanczos-frontier-20261105/code/g0_attribution.py --external /tmp/padua-lanczos-frontier-g0/polyrat --snapshot /tmp/padua-lanczos-frontier-g0/replay --output-dir /tmp/padua-lanczos-frontier-g0-review/attribution --receipt /tmp/padua-lanczos-frontier-g0-review/attribution.json
```

All three processes exited 0. The final attribution source actually executed had SHA-256 `08b9f18d6ac1c7c90546763ac330fff754030fcb6e1561989d764990ed3dd984`. This was a separate execution of the developer's final diagnostic, including fresh Haswell/Nehalem producer subprocesses and six 50-digit frozen-surrogate evaluations; it was not merely inspection of developer output. Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and one BLAS thread were used. Exact commands, start times, versions, compact results, and raw-output identities are in [evidence/g0-independent.json](evidence/g0-independent.json).

| Method | Historical reported gap | Fresh baseline, independent monomial residual | Fresh Nehalem, independent monomial residual |
|---|---:|---:|---:|
| upstream xy | 3.3908605229e-10 | 7.5952769651e-10 | 2.2543024139e-10 |
| upstream yx / local dev | 2.4812027023e-10 | 2.7558698676e-10 | 3.2401076883e-10 |
| mirror | 1.3221174302e-14 | 1.2399895991e-14 | 2.4506508675e-14 |
| alternating | 7.3010222490e-12 | 1.3021560892e-12 | 3.0240530329e-12 |
| adaptive | 8.6560954123e-14 | 7.6247869060e-14 | 7.5841155123e-14 |

Baseline producer/legacy metrics reproduced the previous baseline numbers exactly. Upstream yx and local dev again agree entrywise. Nehalem producers reproduced the prior Nehalem legacy gaps. These are controlled arithmetic changes to fixed inputs and source, not new kernel searches.

The same-Q baseline legacy-gap corrections are `1.55e-16` for xy, `3.74e-17` for yx, and `5.59e-16` for alternating. They cannot account for the historical/current major differences. However, the **full** legacy reference-space error is `1.3353e-14`, not `1e-16`; mirror's legacy value `1.4562e-14` differs materially from its monomial-reference value `1.2400e-14`. Small-gap diagnostics therefore have a reference-noise contribution. The developer attribution receipt's Nehalem legacy measurements use Nehalem Q with the parent process's Haswell reference and metric; they need not equal the wholly Nehalem legacy receipt at the last digits. The independent monomial residuals avoid that distinction.

## Why the explanation is sufficient, and what it does not establish

1. **The changed quantity is the recurrence's computed span.** Pin and input checks exclude the inspected source/data changes; fixed-Q independent projection excludes reference noise as the explanation for the xy/yx/alternating discrepancy scales. Controlled supported kernels change the computed Q and span while preserving near-machine orthogonality. This is a causal intervention on arithmetic implementation in the current environment.
2. **Local roundoff is amplified by the inherited recurrence.** In the separate attribution rerun, maximum local residual-column norms are `0.85–1.08 u`, with residual Frobenius norms around `7–8e-16`. Applying the frozen computed-coefficient inverse from PD-T142's row identity reproduces normal errors around `2.25–7.60e-10` for xy/yx and `1.30–3.02e-12` for alternating. Six 50-digit surrogate normal-error values agree with the independent Arb monomial projections to about fifteen displayed digits; normal reconstruction discrepancies are below `2.76e-18`. The original long-double propagation calculation is less accurate (up to about `2.8e-13` discrepancy for xy/yx), and is not used to claim a sharper reconstruction. This evidence identifies a large realized amplification, not a universal bound on every rounding path. The frozen-surrogate identity alone is algebraic; the separately measured small local residuals and the kernel/precision interventions give it explanatory force here.
3. **Precision controls suppress the effect in the unchanged algorithm.** Calling the actual original producers with NumPy long double (63 explicit mantissa bits, versus 52 for binary64) reduces xy/yx gaps to about `1.94e-13` and `2.30e-13`, alternating to `2.58e-15`, mirror to `3.97e-18`, and adaptive to `4.81e-17`. These are precision controls, not replacements for the binary64 benchmark or claims about historical hardware.
4. **The historical scales are consistent with this explanation, without being reconstructed.** Historical xy/yx gaps are in the demonstrated `1e-10` arithmetic-sensitive regime. Historical alternating `7.30e-12` exceeds the two newly examined kernels' `1.30–3.02e-12` values; the previously recorded Prescott probe was `4.74e-12`. The old value is about 1.54 times that probe, not inside the observed probe range. Realized alternating normal amplification changes from about `1.9e3` to `4.1e3` under the two controlled kernels despite comparable local residual norms, and a higher-precision run suppresses the gap by hundreds. This supports the same `1e-12` sensitivity scale and explains why relative replay differences can be large. It does **not** provide an empirical envelope, a probability model, an exact IEEE witness for the old row, or a proven upper bound on every library. No acceptance threshold was fitted to include the historical value.

Taken together, these checks establish an arithmetic-kernel/operation-order sensitivity explanation of the replay variation at the relevant scales, with a separately quantified reference contribution at the smallest scales. That is the class-level explanation expressly contemplated in handoff 02. Requiring the missing historical Q or a matching historical kernel after this analysis would impose the stronger historical-reconstruction condition that handoff 02 does not require. The exact historical cause remains an explicit provenance limitation, not a recovered fact.

## Limits and disposition

The original exact E1/E5 replays remain supported by [independent-checks-g0.md](independent-checks-g0.md) and its receipts; I reviewed that evidence but did not rerun those exact programs in this supplementary step. Optional full scalar comparator-upper regeneration, G4's two high-degree PD-T146 rows, and all new scientific target runs remain outside this review. No inherited theorem is invalidated or upgraded. This is not a universal reproducibility guarantee for every future case, and unexplained future mismatches still trigger the same gate.

The original FAIL was justified by the evidence then available and remains unchanged. The additional independently executed analysis resolves G0's explanation obligation within the explicitly allowed scope, so the orchestrator may record an additive resolved verdict and resume handoff 01 subject to its remaining gates. Required later Claude audit and the disclosed novelty-gate timing issue remain pending.

Large raw NPZ artifacts stay in local `/tmp/padua-lanczos-frontier-g0-review/`; their identities and regeneration commands are recorded, but no long-term retention or Windows cold-storage delivery is claimed. Only this report, the independent checker, and the small essential receipt are owned by this reviewer.
