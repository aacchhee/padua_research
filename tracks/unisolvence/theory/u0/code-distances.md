# PD-T010 — Eight exact finite Padua-code distance observations

ID kind: PD-T. Aliases: small Padua evaluation-code distances.
Split from: supplied finite_field_padua.md §4 and general code claims `PD-T008`.
Split into: none.

## Statement

Exhaustive projective-message enumeration returned the following minimum nonzero Hamming weights for `C_k=ev_(Pad_n)(P_k)` over the stated prime fields:

| q | n | N | k | K | measured distance | normalized messages checked by separate developer checker |
|---|---|---|---|---|---|---|
| 7 | 3 | 10 | 1 | 3 | 7 | 57 |
| 7 | 3 | 10 | 2 | 6 | 4 | 19608 |
| 11 | 5 | 21 | 1 | 3 | 17 | 133 |
| 11 | 5 | 21 | 2 | 6 | 13 | 177156 |
| 13 | 6 | 28 | 1 | 3 | 23 | 183 |
| 13 | 6 | 28 | 2 | 6 | 18 | 402234 |
| 17 | 8 | 45 | 1 | 3 | 39 | 307 |
| 17 | 8 | 45 | 2 | 6 | 33 | 1508598 |

## Definitions and assumptions

`n=(q-1)/2`. Source code uses Chebyshev basis and first-nonzero normalization. The separate developer checker builds nodes from characters, uses monomial basis and last-nonzero normalization. Every nonzero scalar equivalence class has a unique message with last nonzero coefficient `1`, so the intended search count is `(q^K-1)/(q-1)`. Actual counts are asserted and retained. Integer products are bounded by `K(q-1)^2<=1536`, safely inside NumPy int64 here.

## Status by part

Overall status: **MEASURED**. All eight rows are MEASURED, with finite exhaustive implementation evidence. This record is not claimed as a completed computer-assisted proof. It does not assert optimality among all linear codes.

## Depends on

Specified scripts/interpreter and field arithmetic. The mathematical interpretation of the matrices uses `PD-T004`, `PD-T007`, `PD-T008`, whose proofs are separate.

## Checks and evidence

The unchanged source `padua_codes.py` was executed twice by this developer (once by original driver, once by child-status wrapper) and reported all eight distances. `verify_exact.py`, which imports no supplied module, independently implements the developer cross-check and reports the same values plus a minimum-weight monomial coefficient witness for each row. These are separate implementations, not separate agents. Cold outputs: `source-copy/padua_codes.log`, `child-replay/padua_codes.log`, `verify_exact.jsonl` under `/workspace/padua-cold/charter-unisolvence-20261031/U0/`. Full identity manifest and commands: U0 `evidence.md`.

The integrated [independent U0 report](../../../../topics/charter-unisolvence-20261031/independent/u0/audit.md) and its frozen hashes record `q=7`, `k=1,2` enumeration returning `7,4`, with `57,19608` projective messages. The elementary universal linear-code bounds are separately integrated as [PD-T012](code-optimality-bounds.md); this record's attained distances remain MEASURED. [AUDIT_LOG](../../AUDIT_LOG.md) links Claude audit-01, which independently reproduced all eight rows and accepted this status separation.

## Sources

Supplied §4, `LIT-025`, reports the table and optimality claims. Ball (2012) was not read and is not a dependency.

## Scope and open items

No general minimum-distance formula, decoder, weight distribution or prime-power extension table is claimed. The exact source code also reports constant codes and two additional parameter cases; these remain source reproduction logs rather than new registered table claims. Claude audit-01 accepted the stated scope and MEASURED classification; administrative dispositions are in response-01.md.

## History

2026-10-31, Codex U0, assigned `gpt-6.1-sol xhigh`; rules/base `d36722823441dc40c6e19d69a174459348dd309c`. Split the finite table from proved general structure and from all-code optimality bounds.

2026-10-31, Codex response-01 A2: updated completed handoff references and Claude audit-01 acceptance metadata only; mathematical statements, proofs and epistemic statuses unchanged.
