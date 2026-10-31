# PD-T?charter-u0-codex-06 — Finite reproduction observations for supplied Padua scripts

ID kind: PD-T. Aliases: U0 supplied-script finite checks.
Split from: supplied finite_field_padua.md computational assertions.
Split into: [code-distances.md](code-distances.md), `PD-T?charter-u0-codex-07`.

## Statement

The following finite observations were reproduced from the unchanged supplied scripts under Python 3.12.14, NumPy 2.3.5 and SymPy 1.14.0 on the recorded Linux environment:

1. `padua_ff.py`: all 76 admissible prime cases selected by its enumeration, `1<=n<=10`, pass its node-count, rank, Gram, cubature-exception, Dickson determinant, vanishing-generator, multiplication and weighted-symmetry tests. Four prescribed primitive-root canonicity checks return true. At `(n,p)=(3,13)`, y rationality is `[True,False,True,False,True]`.
2. `fast_transform.py`: all 46 enumerated dense-versus-transform comparisons and round trips for `1<=n<=12` return OK. Nine benchmark round trips for `n=8,16,24,32,48,64,80,96,128` return true. Timings are execution-specific, not complexity theorems.
3. `quadratic_padua.py`: all 13 primes `5<=q<=47` pass its character-set and unisolvence comparisons.
4. `discriminant_real.py`: all twelve printed relative discrepancies of **log absolute determinants**, `1<=n<=12`, are at most the printed maximum `4.3e-16`. This is not a relative determinant-error bound.
5. The separately implemented developer checker passes the character description, cardinality and nonzero Dickson determinant with the predicted square for `q=3,9` in `F_81`.

## Definitions and assumptions

Scope is the actual source loop selections, not all primes below 6000 or every prime power. The 76 cases use two selected primes for each available sign type; `n=1` has only two distinct sign types. All arithmetic except item 4 and timing is exact within the implementations. The separate checker uses exact integer-encoded finite-field arithmetic.

## Status by part

Overall status: **MEASURED**. Each numbered observation is MEASURED. Separate written universal proofs live under IDs `01–05`; this record neither proves nor weakens them. Candidate disposition: retained finite evidence; independent acceptance pending.

## Depends on

The exact script bytes, interpreter and libraries recorded in the U0 evidence manifest. No source statement is accepted as a dependency. `hs_ff.py` was also executed as a driver child; its mathematical claims belong to U1 and are not re-registered here.

## Checks and evidence

The unchanged `run_all.py` was run in a byte-identical cold copy and returned zero in 35.303704 seconds. It does not propagate child exit failures. The separate `replay_source.py` ran all six children and retained their individual exit statuses, all zero. No isolated-import repair was needed: the supplied modules already insert their local directory.

Canonical committed input code: `topics/charter-unisolvence-20261031/input-code/ff_padua/` (orchestrator checkpoint `5123a32`; per-file SHA-256 identities are authoritative for execution). The actual execution used the byte-identical cold copy under `/workspace/padua-cold/charter-unisolvence-20261031/U0/source-copy/`. Full commands, seeds, source and output hashes: `topics/charter-unisolvence-20261031/directions/U0/evidence.md` and `artifact-manifest.json` in that cold directory.

## Sources

`LIT?charter-unisolvence-codex-25`, the supplied note; original literature remains uninspected by this developer. The source's `<=4e-16` wording does not identify the actual printed log-determinant metric and does not match its reproduced rounded maximum `4.3e-16`; no determinant-relative-error assertion is retained.

## Scope and open items

Finite successful checks do not establish universal correctness, nonsmooth-length complexity, arbitrary-field Harris–Simanek criteria or code optimality. Independent adversary has reported separate reruns to the orchestrator; its exact report and hashes must be integrated before acceptance.

## History

2026-10-31, Codex U0, assigned `gpt-6.1-sol xhigh`; rules/base `d36722823441dc40c6e19d69a174459348dd309c`. Reproduced unchanged sources, preserved all logs outside Git and separated their scope from proofs.
