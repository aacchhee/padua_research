# PD-T532 — CC upper fits and endpoint Galerkin proxy

2026-11-06 ID history: `PD-T?mz-sharp-codex-902` → `PD-T532`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: CC upper fits and endpoint Galerkin proxy.
Split from: previously reported finite numerical observations (audit A4).
Split into: none.

## Statement and evidence

The same 42 CC rows give final-window K3 fitted limits
1.0044369722946567 (even) and 1.0044369722985076 (odd), using the fixed
scaled SVD model in S4-k3-fit-essential.json. The parity difference
3.85e-12 is floating noise, not certified agreement at that precision.
S2-model.json gives the fixed J=512 model value 1.0044369188646673;
S4-k3-comparison.json records the discrepancies about 5.343e-8 and
operational PASS. No infinite-tail or quadrature enclosure is claimed.
S2-model.json and check-S2-model-replay.json retain all finite J and
quadrature checks; this record covers exactly their sizes/parameters.

## Reproduction commands

Set the three BLAS thread variables to 1, from repository root:

```sh
python topics/padua-mz-sharp-constants-20261106/code/S4_k3_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/S4-k3-R-replay.json
```

The S2 finite-model producer and checker commands are frozen in
S2-model.json and check-S2-model-replay.json.

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
