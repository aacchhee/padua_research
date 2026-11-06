# Round ledger

A round ends with a pushed LOG entry, not with an internal reasoning pass.
Budgets are ceilings, not targets. Handoff 01 defines progress and kill rules.

| Direction | Completed rounds | Current action | Consecutive rounds without progress |
|---|---:|---|---:|
| D0/D1 | 1 | Both PASS; independent replay remains due | 0 |
| T1 | 1 | Hand theorem written; D3 and independent check next | 0 |
| T2 | 2 | Frozen families killed; finite census/quality; independent cover next | 0 |
| T3 | 1 | Exact prerequisites; survivor-dependent work blocked on D2 | 0 |
| T4 | 1 | All-n theorem and monotone lower bound; diagnostics next | 0 |
| T5 | 1 | D4 PASS; fixed-grid theorem next | 0 |
| T6 | 0 | Literature-first lower-bound survey; maximum 8 | 0 |

## Replay round 1

D0/D1 passed the actual command in [replay-notes.md](replay-notes.md).
All six historical floating values match exactly; no new mathematical claim
or mechanism is introduced. Coordinator pushed this gate boundary before
counting subsequent direction rounds.

## First mathematical boundary

The corresponding LOG entry records the exact delivered scope per direction.
T1/T3/T4 analytic claims are developer-written proofs, with independent
checks pending. T2 computations are finite and do not establish an infinite
family. T5 passed its exact pipeline gate. These results are checkpointed
together; budget counts are per-direction progress boundaries, not internal
reasoning passes. T6 has not yet delivered its first completed round.
