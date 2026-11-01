# Audit-04 literature administrative repair recheck

Rules/base: `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`; reviewed the working tree, identified by hashes below. Date: 2026-11-01. Independent Codex literature integration subagent; assigned `gpt-6-astra`, high (runtime model metadata not separately exposed).

AC authorized the root orchestrator to fix bookkeeping without another Claude development round. This is an independent check of that bounded administrative repair, not a new mathematical audit, novelty gate or source-reading exercise. The original pinned finding, checker and failing receipt remain unchanged. Only new literature-repair-* support files were written by this subagent; no Git mutation occurred.

## Decision

**LIT-I1 is resolved for the reviewed bytes. Accepted in the literature integration scope.** No unresolved new finding remains in that scope. All previously recorded source-reading and attribution limits remain open, including the twenty comparison flags; acceptance does not clear those flags or upgrade their statements.

Independently executed `literature-repair-check.py` against the working tree. Exit status **0**. The checker reuses the original bounded integration comparisons and adds a backslash-aware Markdown cell check, complete reading-coverage retention, unchanged-map checks, a complete CORPUS row-delta check and original-audit identity checks. The three restored rows were also inspected directly.

- LIT-342, LIT-369 and LIT-389 restore their complete original statements, sources, locators, verification labels and reading-coverage clauses. Their internal mathematical pipes are escaped correctly. LIT-369 retains the cubature-weight-formula-not-checked limitation. LIT-389 retains UNVERIFIED coverage, requested/not-read book chapters and an explicit paper/book attribution flag. Their allocated IDs and overlap links remain intact.
- All 95 programme INDEX rows preserve the baseline statement, source, locator, verification and reading coverage, allowing existing ID-alias substitution and escaped pipes. Every row parses as exactly seven Markdown columns. There are zero retention mismatches and zero missing reading-coverage clauses.
- All 16 merger aliases agree with the allocation map and crosswalk; 111 baseline IDs remain fully accounted for. The 95 programme and 32 lattice ranges remain LIT-332–426 and LIT-300–331. Both JSON comparison maps, allocation map and baseline are byte-identical to the audited candidate.
- All twenty second-pass comparison flags remain recorded. Nineteen retained INDEX rows retain their map-flag annotation; merged row 06 retains its map conflict. Row 58 remains the unchanged LIT-375 overlap with LIT-141/142 and unsupported Pitman attribution flag. The existing first-pass flags remain listed, with row 73 now additionally annotated directly in its restored row.
- CORPUS removes exactly the three bogus keys `c`, `Y`, `x±y`, adds no source keys, and changes no retained row content except 75 final-column gap clarifications: `full citation to be completed at final allocation` becomes `citation completion pending source verification; final IDs do not clear this gap`. This correctly preserves unfinished bibliography as unfinished. Each of the 34 PR #10 cleanup keys still occurs exactly once and its canonical row remains byte-identical to main `21e620b`.
- All inherited main INDEX rows remain byte-identical to main. The original literature-check.py and literature-check.json retain their recorded hashes.

## Executed command and identities

From the repository root with Python 3.12.14:

```text
python topics/programme-ideas-20261031/audit-04-support/literature-repair-check.py > topics/programme-ideas-20261031/audit-04-support/literature-repair-check.json
```

The default reads current working-tree files and pins historical comparisons to the original audit commit and main `21e620b`. An optional first argument reads a later commit instead, allowing the root to bind this result to the committed repair. Input hashes and byte sizes are in the receipt.

| Reviewed file | Bytes | SHA-256 |
|---|---:|---|
| literature/INDEX.md | 261781 | `5cad267c7f98f1832a3ed0d8c7db65fed32e4795ac396d55add801c9493e55c9` |
| literature/CORPUS.md | 102695 | `805550cc8ecaab79ac98981a71bab752e53c3ad8b2ad66615f445510071c9b62` |
| ID_CROSSWALK.md | 249483 | `543b970b311bb49cc7147db637734f37e6cdb7c48e91d67c3c9e79d55812844c` |

| New audit artifact | Bytes | SHA-256 |
|---|---:|---|
| literature-repair-check.py | 10294 | `572468fb8753fc57df2c5198e46f8ef359eb16429ff1a9142dde9cf9916e540c` |
| literature-repair-check.json | 11707 | `44ab08899f5b26654f7185402a147c2d954a9d90255ba34aa410065ea97c7d31` |

This is an independent administrative integration recheck. No PDF was fetched or read, no accepted mathematics was reopened, no new literature statement was generated, and unavailable-source limitations are unchanged.
