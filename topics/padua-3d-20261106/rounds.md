# Round ledger

A round ends with a pushed LOG entry, not with an internal reasoning pass.
Budgets are ceilings, not targets. Handoff 01 defines progress and kill rules.

| Direction | Completed rounds | Current action | Consecutive rounds without progress |
|---|---:|---|---:|
| D0/D1 | 0 | Replay prerequisite | 0 |
| T1 | 0 | Await D0 | 0 |
| T2 | 0 | Await D0 | 0 |
| T3 | 0 | Await D0 and T2 survivors | 0 |
| T4 | 0 | Await D0 | 0 |
| T5 | 0 | Await D0; maximum 8, pipeline kill after 3 | 0 |
| T6 | 0 | Await D0; maximum 8 | 0 |
