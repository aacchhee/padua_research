# PD-T538 — Padua finite minima, corner proxies and transfer diagnostic

2026-11-06 ID history: `PD-T?mz-sharp-codex-903` → `PD-T538`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: Padua finite minima, corner proxies and transfer diagnostic.
Split from: previously reported finite numerical observations (audit A4).
Split into: none.

## Statement and evidence

The 16 minimum rows in S4-padua-essential.json cover exactly
m=800,801,1000,1001,1200,1201,1400,1401,1800,1801,2200,2201,
2600,2601,3000,3001. S4-padua-fit.json records the registered parity/window
intercept-plus-log fits and slopes about −0.092 (see complete coefficient
and residual fields). K4 remains KILL_HEURISTIC_PROXY; K5 is MEASURED
finite-window parity agreement. No upper eigenvalue campaign is implied.
S3-corner-model.json gives product cuts K=16,32,64,128 at triangle Gauss
orders 128,192. K128 extrema are about −0.133580002120 and
+0.0455983195703; 120/128=0.9375 makes the analytic tail uninformative
for these displayed digits. check-S3-corner-model.json independently replays
the model. check-S3-transfer-diagnostic.json retains its exact finite
parameter list, continuous norm normalization and transfer comparisons;
it is an uncertified normalization diagnostic, not a proof of convergence.
audit-01-support/S3/big.json and mid.json supply the separate finite-mode
interpretation in audit A2, at m=400,800,801; no new branch claim is proved.

## Reproduction commands

From repository root, set all three BLAS thread variables to 1:

```sh
python topics/padua-mz-sharp-constants-20261106/code/S4_padua_fit.py --essential topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-essential.json --output /tmp/S4-padua-R-fit.json
python topics/padua-mz-sharp-constants-20261106/code/S3_corner_model.py --orders 128 192 --cuts 16 32 64 128 --output /tmp/S3-R-model.json
```

Transfer command/producer hashes are frozen in check-S3-transfer-diagnostic.json.
The model receipt preregistration hash refers to the original 59d02c7 blob;
see attempts/S3.md. Working-prose hash differences on replay are expected.

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
