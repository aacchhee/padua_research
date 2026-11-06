# PD-T525 — CC lower fit and normalization diagnostics

2026-11-06 ID history: `PD-T?mz-sharp-codex-901` → `PD-T525`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: CC lower fit and normalization diagnostics.
Split from: previously reported finite numerical observations (audit A4).
Split into: none.

## Statement and evidence

K1 fits the 42 committed CC rows in evidence/S4-essential-cc.json, N=100
through 102401, both parities. Fixed windows A (j=8..14) and B (j=15..20)
use columns [1,loglogN/logN,1/logN]. Final B intercepts are
13.061135993252737 (even) and 13.061132673210166 (odd), in
S4-k1-fit-essential.json; S4-k1-fit.json is the original full-raw fit.
K2 remains KILL_MODEL operationally. These intercepts exceed the proved
limsup bound pi⁴/8=12.1761363792503 and cannot identify the true limit;
the test carries no evidential weight against equality.
Normalization checks are the finite K0 CC and carrier comparisons in
S4-k0-cc.json, S4-k0-carrier.json and check-k0-replay.json; their parameter
lists and relative-error fields define the exact scope. They are checks of
normalization, not proofs of asymptotic accuracy.

## Reproduction commands

From repository root, with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
MKL_NUM_THREADS=1:

```sh
python topics/padua-mz-sharp-constants-20261106/code/S4_k1_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/S4-k1-R-replay.json
```

Other diagnostic producer/checker commands are frozen verbatim in
S4-k0-cc.json, S4-k0-carrier.json and check-k0-replay.json.

## Definitions and assumptions

Exact mathematical conventions are those of the producer code and the
registered gates, not a new asymptotic model. Inputs are committed essential
rows and named receipts at the response input commit
0205690b9c4e959a28e949083e9a1808735abf4b. No new numerical execution is
claimed here. Final IDs are reserved for PR preparation.

## Status by part

Overall status: **MEASURED**. Each listed observation is finite-scope floating
point evidence, with no certified decimal, asymptotic inference or computer
proof. Candidate disposition: retained measurements, no PD-N.

## Checks and provenance

Producer command, versions, source/code hashes, input hashes and original
execution time are preserved in the named JSON receipts. Independent reruns
are recorded in audit-01.md, Actual executions; these are attributed audit
executions, not reruns by this response worker. evidence-manifest.json pins
the committed receipt and code identities. Optional timing-bearing raw bytes
are not archived as authoritative evidence; essential rows suffice for fit replay.

## Scope and open items

Only the finite rows, fixed truncations and registered windows below are
covered. Floating agreement is not a rigorous bound. Limit theorems retain
their separate analytic records; no gate outcome or historical receipt is
revised. Independent focused audit of this durable record remains required.

## History

2026-11-06 audit response A4; Codex, requested gpt-6.1-sol medium; actual
runtime serving-model/effort metadata unexposed. Compact durable home for
already reported measurements, not new computation or new final IDs.
