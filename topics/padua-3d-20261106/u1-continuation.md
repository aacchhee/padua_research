# U1 continuation results and decisions

2026-11-07. Codex developer, assigned gpt-6.1-sol high; runtime metadata is
not independently exposed. Rules/input97c323bfae15cf3c76f40802c3ebabedceeb0c60.
Root owns publication/counters and the combined report. No final ID or
historical novelty claim. Provisional measured result:
`PD-T?padua-3d-20261106-u1c-decisions`; aliases: fixed-budget oracle
calibration, degree/noise decision, fixed-allocation GLS refit.
Main status **MEASURED**. Split from/into: none. The broad universal-best-
design goal remains separately OPEN and is outside this measured statement.

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

## Continuation round2/global U1round4 — MEASURED below the useful-gain gate

The known GLS protocol was published in98cf83c8416778b6a57002cd98e85d27a954f092
before execution; [u1c_gls.py](code/u1c_gls.py) froze all24new weighted-QR
maps before fresh assessment of all62maps. No prior query cloud was reused.
[Compact receipt](evidence/u1c-gls.json) includes every new map, both fresh
complete baseline envelopes and parent-map regressions across all12targets.
The pinned raw output retains every fresh individual baseline/new bias and
total-MSE value. Source/data identities were rechecked after execution.

All24new maps pass: reproduction infinity residual<=3.94147e−14 and
weighted covariance-identity residual<=9.22987e−17. The fixed-schedule
covariance reductions range0..3.74548percent. These use the exact-model
finite-variance interpretation; no random noise realization is substituted
for expected variance. Some rows are deliberately duplicate controls:
GLS after all-one repetitions at degree12 gives the already available OLS
map, for example. Equivalence creates no new theorem or negative record.

The useful total-error gate **fails** decisively. Against the best of the
complete38original candidates, the largest second-cloud expected-MSE gain
is1.64528percent for the primary boundary layer and0.758489percent for the
secondary Gaussian, both below the prospectively fixed5percent threshold.
Across every target/noise setting the largest envelope gain is1.81032percent
(the original absolute-ridge target). First-cloud choices have zero
second-cloud regret at recorded precision; an occasional identity difference
is a numerically tied equivalent map. Cloud agreement does not supply an
unknown-target degree selector or a continuum error certificate.

Covariance improvement also does not imply deterministic improvement. For
cos(4x−3y+2z), refitting the Haar11allocation increases zero-noise squared
bias from0.0002970779194 to0.0003356306384, a12.9773percent increase on the
second fresh cloud. The entire exponential has an11.4787percent increase
under Haar5refitting (2.6303842e−10 to2.9323192e−10); the original absolute
ridge has a10.6603percent increase under OLS2refitting. All target/noise
regressions remain in the compact raw-derived summary and full raw data.
These are fixed-map parent comparisons, not contradictions of the
nonincreasing envelope obtained by retaining the parent as an option.

Construction used0.245315process-CPU seconds; complete run2.05498CPU and
2.05613wall seconds, with the same one-thread versions and possible untimed
worker overlap. No map or whole-run cap hit, invalid case or unrun design.
Actual command:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u1c_gls.py --prior topics/padua-3d-20261106/evidence/u1c-budget.json --raw /tmp/padua-u1c-gls-20261107a --out topics/padua-3d-20261106/evidence/u1c-gls.json --protocol-commit 98cf83c8416778b6a57002cd98e85d27a954f092
```

CandidateU1c02 disposition: park this fixed-integer-allocation GLS refit
route after its failed practical5percent gate. This is an engineering stop
for a specified finite rule/scenario, not a new general negative theorem.
No extra seeds/degrees, automatic variance-model change or new global
weighted-design obstruction is inferred. The covariance algebra itself
remains sound. No separate PD-N is assigned to a practically small gain.

## Research-round ledger and endpoint

| Work | New research rounds | Actual outcome |
|---|---:|---|
|API response, regressions and original science replay|0|fixed/verified separately|
|U1c01, degree/noise oracle calibration|1|practical gate passes; useful table|
|U1c02, refit after fixed integer allocation|1|practical gate fails; park rule|

New allowance used2/7, five unused; global U1 completed outcomes4, including
the two original rounds. Root's published LOG controls formal counters.
Do not spend the five remaining rounds repeating these rules or invoke the
ceiling as a reason to declare the broad direction exhausted.

The useful current advice is conditional: if prior calibration justifies
a particular field/error model, use its bias-plus-noise table to choose
among feasible degrees and solvers. For an unknown field, this experiment
supplies no implemented data-only degree selection. U1 remains a known
low-setup-cost approximation recipe under its actual measure/site/noise
assumptions, and the original valid-input theory remains unchanged.

## Independent checks and remaining work

The distinct [focused API review](api-response-review.md) reports PASS for
the dimension fix, with independent140valid/110malformed executions. A distinct
continuation checker has the frozen two receipts, raw inventories and
source hashes for independent map/noise/fresh-bias reconstruction; its
report controls its own completed scope. This developer record supplies
no self-approval or formal Claude acceptance. No scientific producer run
remains unexecuted in the two registered U1 continuations.

Resume research only for a stated quantitative need: actual prior/validation
information that can turn oracle calibration into an implementable degree
choice, a specified changed measure/site-cost/noise model, or a different
allocation with a plausible material-gain gate. None is a pending run here.
The failed refit gate and present useful calibration endpoint justify
stopping this specified batch. Broad optimized allocation/design and
unknown-field selection remain OPEN, without an exhaustion claim.
