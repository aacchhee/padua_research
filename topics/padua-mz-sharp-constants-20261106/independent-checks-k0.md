# Supplementary independent K0 check

Date: 2026-11-06. Role: separate Codex supplementary checker, requested
`gpt-6-astra high`; actual runtime model/effort metadata is unexposed.
Rules and source input: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
This is a completed finite computational verification, **MEASURED**, and
supplements the required Claude audit. It adds no mathematical result.

## Scope and verdict

**PASS for the finite K0 replay under the dated clarification in
[gates.md](gates.md).** No unresolved BLOCKING, MAJOR or MINOR finding in
this bounded scope. The finite carrier norm is not within 1e-10 of its
asymptotic limit. The original literal limit-equality interpretation would
fail at the tested sizes; it is not what this verdict approves.

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md and handoff01,
the replay script and its three receipts, attempts/S4.md, the imported
CC and Padua implementations, PD-T026, PD-T379, and the dated gate
clarification published by the coordinator at
`d30ccb6d84e7dd73f58f39ba1121a7f8ea3ed00a`.
No new mechanism, novelty, priority or negative mathematical claim was
considered. Consequently the novelty gate/full IDEAS read does not apply
to this replay-only check. No Git operation or shared coordinator file
was changed.

## Frozen inputs and actual execution

Before execution the developer confirmed that S4_k0_replay.py was frozen
at SHA-256 `707d8d925d34c09846ac454a7482be2efc8563b33dd0e5e9ad2a16842d605285`.
The developer's earlier Padua run used the preserved initial script,
SHA-256 `628b7f86952619b03f1e6077750d1116705b029609dc6add81838e660250322a`;
its different hash is documented, not an unrecorded input substitution.

The separate [checker](code/check_k0_replay.py) verifies the frozen code,
all imported repository code, historical Padua reference data, and all
three developer comparison receipts before execution and again on exit.
The [receipt](evidence/check-k0-replay.json) lists all those SHA-256 pins,
versions, command, seed, thread settings, output values and timings.
It intentionally does not enforce prose hashes.

Executed from the source corpus root `/workspace/sharp-work`:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/check_k0_replay.py --output topics/padua-mz-sharp-constants-20261106/evidence/check-k0-replay.json
```

The process exited successfully. Start 2026-11-06 11:34:59 UTC;
48.163 seconds total, 317660 KiB peak RSS. Python 3.12.14, NumPy 2.3.5,
SciPy 1.17.0, mpmath 1.3.0. The changed Padua seed is 20261106 versus
the developer/historical seed 20261105; tolerance 2e-11, ncv40,
maxiter20000. Carrier moment evaluation used 90 decimal digits versus
the developer's 75. All inputs remained unchanged through completion.

- Checker SHA-256: `f386e7f01ab169a78dba2b7e77caa0c710d6610b43dbf826ec9fcbf0d5f3a11c`.
- Receipt SHA-256: `145b99de6a7949b3b061de5f4be9910f8c8f10f4ceb067d2a137f5a5a9002432`.
- Receipt size: 6004 bytes. No vectors or large output arrays were saved.

## Results

CC n=N−1, both parity blocks at N=40,80,160,320,640,1280 all reproduce
PD-T026's extrema. Maximum relative discrepancy: 3.9968028886505635e-15.

| Padua m | Recomputed minimum | Relative discrepancy | Floating residual 2-norm | Matvecs |
|---:|---:|---:|---:|---:|
| 800 | 0.040025262151571574 | 2.22045e-16 | 1.34968e-14 | 162 |
| 1000 | 0.019659472013741963 | 1.84297e-14 | 2.95493e-13 | 142 |

The changed-seed Padua runs took 18.261 and 29.558 seconds respectively.
Their independently executed results pass the 1e-10 relative threshold.

The even negative carrier uses a=1/4,b=1/5, satisfying the strict
admissibility inequality. At m=512,1024,2048,4096 the Fourier/moment
formula agrees with the composite angle quadrature to at most
3.3101308776823565e-16 relative error. The 90-digit moment evaluation
agrees with the stored 60-digit developer displays within 1.23e-60.
A pre-convolution upper bound checks int64 safety: each coefficient
is bounded by (2r+1)(r+1)^2; the largest tested bound is 2152730625,
far below 2^63. The same bound is checked for the second envelope.

| m | Relative difference of finite norm squared from limit |
|---:|---:|
| 512 | −4.437864111843278e-4 |
| 1024 | −2.1440610783815423e-4 |
| 2048 | −1.0530248564295803e-4 |
| 4096 | −5.2175085856147984e-5 |

The limit used for comparison is the PD-T379 expression A J_-(1/4),
displayed as 3.750988211370259884384963454664701991610560335750029136799.
Its finite-size discrepancies decrease on this grid. No rate, limiting
value, extrapolation or uniform error bound is inferred from those four
numbers.

## Findings and limits

- NOTE: An ambiguity in the original carrier gate was raised to the
  coordinator. The dated gates.md clarification explicitly resolves it
  while preserving the original. This report approves only that clarified
  finite replay criterion.
- NOTE: Integer convolution is exact in this tested range; the subsequent
  moment sum uses multiprecision floating arithmetic. The term "exact
  finite norm formula" describes the algebraic identity, not a rational
  certificate or a rigorously enclosed computed value.
- NOTE: These are separately executed runs by another agent, with a
  changed Padua seed, but use the same imported spectral algorithms.
  Small floating residuals do not certify that an eigenvalue is globally
  extremal, and no eigenvalue enclosure or asymptotic theorem is proved.
  The carrier's two formulations also remain numerical checks.

No fit or extended grid ran. The sharp-limit targets, mathematical-model
checks and required cross-family Claude audit are outside this scope.
