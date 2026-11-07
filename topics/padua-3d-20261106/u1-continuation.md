# U1 continuation results and decisions

2026-11-07. Codex developer, assigned gpt-6.1-sol high; runtime metadata is
not independently exposed. Rules/input97c323bfae15cf3c76f40802c3ebabedceeb0c60.
Root owns publication/counters and the combined report. No final ID or
historical novelty claim. Current broad universal-best-design goal OPEN.

## Scope, assumptions and dependencies

The [prospective protocol](u1-continuation-protocol.md) fixes an explicitly
assumed product-Chebyshev sensor-field example, B637equal-cost independent
observations and known per-observation variance, with at least one sample
at each used site. These are research assumptions, not facts supplied by AC.
The decision tables use each explicit noiseless test function to estimate
bias: they are oracle benchmark/calibration tables. Known noise sigma
alone does not make them implementable on an unknown field. Real use would
require an independently justified prior calibration or validation data;
no data-only automatic degree selector is implemented or evaluated.
All construction/solver mechanisms are inherited known routes. Depend on
the separate U1 recipe/noise/OLS records and exact stored U2 payload; no
source-dependent log³ theorem enters the finite comparisons.

The squared-error decomposition uses mean-zero finite-variance noise and
a fixed linear map on replicate averages: continuous expected MSE equals
deterministic squared bias plus sigma² sum_j||C[:,j]||²/r_j. Only the noise
term is evaluated by the exact-model formula; bias uses finite point clouds.
No certified continuum maximum, optimal-node theorem or global model-
selection result is asserted. Jointly re-fitting a map after replication
is a different comparison and is not silently included in the first round.

## API response — zero rounds

[U1-M1 response](response-interim-u1.md) records the material validation fix,
112shape rejections and14complete-basis valid-input cases. Original complete
24-case science rerun matches every saved array exactly under new producer
provenance. The distinct focused reviewer owns its own verdict. These
repairs/verifications consume zero construction rounds.

## Pre-execution checks — zero rounds

`python -m py_compile .../code/u1c_budget.py` passed. Executed21small
integer-allocation cases against exhaustive positive compositions, all
matching the greedy minimum to1e−12. Executed a forced assessment cap by
replacing the local clock with601CPU seconds before the first512point
boundary: assessment returned no result and saved partial sums. The
preflight temporary directory was removed by `TemporaryDirectory`; no
scientific outcome, construction or counted round is attributed to it.
A distinct reviewer identified the assessment-cap/inventory requirements
before execution; the implementation now checks both construction and
assessment and inventories every raw artifact by bytes/hash.

## Continuation round1/global U1round3 — MEASURED useful decision

Protocol publishedcb014092e71d16b77c7c2651363440d7b078eab6; source frozen
atd826a0f before execution. [Compact receipt](evidence/u1c-budget.json)
retains all38designs' two-cloud squared biases for all12targets, exact-
model risk coefficients, both-cloud choices, source/input identities and
full raw inventory. Every design passes the count/reproduction gate;
maximum reproduction infinity residual2.38457e−12. All21integer-allocation
brute-force prechecks pass. No cap, invalid design or unrun case.

For the explicit primary calibration function exp(10(x−1)), the oracle
best feasible choices among
the frozen38designs are:

| Per-observation noise sd | Choice | Distinct sites | Total expected RMS estimate | MSE gain vs fixed Haar12 |
|---|---|---:|---:|---:|
|0|QR13|560|0.0000618475|63.31percent|
|0.00001|QR13|560|0.0000647325|60.08percent|
|0.0001|OLS12|637|0.000131853|1.26percent|
|0.001|OLS11|510|0.000820209|7.69percent|
|0.01|OLS9|305|0.00617031|47.01percent|
|0.1|OLS6|112|0.0429647|74.30percent|
|1|OLS3|26|0.226300|92.87percent|

Here RMS is sqrt(empirical squared Chebyshev bias plus exact-model noise
risk), from the second fresh32768-point cloud. Noise scales and all choices
were frozen prospectively. The practical gate passes: calibrated degree
selection materially changes the choice and MSE. Every one of the12x7
minimizing designs agrees across the two independent clouds, so first-cloud
choices have zero second-cloud regret within this finite candidate set.
This is an empirical stability check, not a bound on integration error or
an unknown real field. A known one-dimensional physical model would allow
a different, smaller model class; this comparison fixes three-dimensional
Pi_n and does not optimize that model assumption.

The off-centre Gaussian selects Haar11at0..0.001, OLS11at0.01 and QR1at
0.1/1. Thus higher degree is not automatically better even without noise
for this sampled design/target combination. All other targets, including
the four original functions and omitted T13mode, remain in the receipt;
no losses are omitted. No universally best family is inferred.

Construction consumed4.66995process-CPU seconds and complete run6.19196CPU
seconds,6.2003wall seconds. Other workers were authorized concurrent untimed
assessments; these are descriptive costs, not matched-cost comparisons.
Single-thread Python3.12.14/NumPy2.3.5/SciPy1.17.0. Dense coefficient maps
and integer repetitions are retained in the pinned unique/tmp raw inventory.
Raw delivery is regeneration-only, not archival. Actual command:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u1c_budget.py --raw /tmp/padua-u1c-budget-20261107a --out topics/padua-3d-20261106/evidence/u1c-budget.json --protocol-commit cb014092e71d16b77c7c2651363440d7b078eab6
```

CandidateU1c01 retained as a useful known operational extension, not a
new construction theorem. Its fixed maps need not be BLUE after unequal
replication; the next registered round tests that specific unresolved
practical improvement, rather than repeating a benchmark.

## Research-round ledger

API/checks0. Continuation round1/global U1round3 completed and published
in98cf83c8416778b6a57002cd98e85d27a954f092. New outcomes1/7, global U1=3.
The new GLS protocol is published in that same commit before execution.
Root's pushed LOG controls counters; no unused round is pre-consumed.

## Runs needed

Execute continuation round2/global U1round4, known GLS refit after fixed
replication, under its prospective five-percent total-MSE gate. Independent
review/rerun of new science remains separate from developer execution and
from the pending formal Claude audit.
