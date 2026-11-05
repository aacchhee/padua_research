# N3 common finite corner patch — batch log

Rules/input: c000899f3fb10d6ba0f1725341a045fe11ec943a. Developer: Codex,
parent-assigned gpt-6.1-sol xhigh; serving metadata not independently exposed.
Rule files checked unchanged from 714f3cad. Parent alone controls Git and
shared campaign files. Existing three-case code/data/pins remain unchanged.

Gate and fixed target before execution: `../ideas/N3-corner-batch.md`.
Every integer degree n=2..128 must satisfy the candidate exact inequality
kappa>=1/16000, under the existing reduction. Stop on the first failure;
total child CPU cap 1200 seconds. The common scaled-phase square is
|alpha|,|beta|<=1/128. A range local-corner result is not a full global
degree certificate.

## Original runs needed (first writing; now completed as specified below)

- Implement and run `../code/n3_corner_batch.py` using unchanged
  n3_corner_bounds.c arithmetic, at 256 bits, all 127 integer degrees.
- Store the full output in one local JSONL bulk file; commit only the
  short aggregate `../evidence/n3-corner-batch.json` receipt.
- Parent-arranged distinct exact range verification from integer inputs;
  no producer arithmetic kernel reuse. Range status stays CONDITIONAL
  until that independent replay actually completes.

## Completed run

Exact executed command from repository root:

```text
python topics/padua-argmax-bridge-20261105/code/n3_corner_batch.py --output-dir local-output/argmax-bridge-20261105/N3-corner-batch/r01 --mpfr-include local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include --receipt topics/padua-argmax-bridge-20261105/evidence/n3-corner-batch.json
```

All 127 integer inputs 2..128 completed and passed the unchanged predeclared
candidate kappa>=1/16000. Total child CPU 5.246695 seconds, under the 1200
second cap; summed native CPU 4.758418 seconds. Counters: 362045 nonzero
cardinal contributions, 4096 zero-cardinal omissions; zero threshold
failures/errors/unrun cases. Exact n2 controls mass 3/W331/18 are contained.

Minimum exact producer kappa occurred at 128 and is recorded as a rational
in both theory and receipt; no floating comparison entered acceptance.
This completes the producer step only. Independent range replay remains
PENDING, so the corresponding finite mathematical claim is CONDITIONAL.
No fallback constant or rejected candidate was generated.

Receipt `../evidence/n3-corner-batch.json`: 3601 bytes, SHA-256
97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88.
One local-only bulk endpoint file: 235648 bytes, SHA-256
58d3586adae81360b296740c984e122affab08514e1e3e0481803b26a5404d2f.
No full table or per-degree endpoint files are committed. Source arithmetic
hash remains a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd.

Environment: cc (Debian 14.2.0-19) 14.2.0; MPFR 4.2.2; GMP 6.3.0;
Python 3.12.14; Linux 6.18.57/glibc 2.41. The official MPFR header was
already present from the N3 runtime extraction. No network/new dependency
retrieval, randomness, Git action or shared-file write was performed.

## Remaining obligation

Parent arranges a distinct exact checker that reconstructs all 127 cases
from integer n and verifies 8E+24u*n^4<=16000*n^4*ell. The producer table
need not be a checker input; it supplies diagnostic run provenance only.
The independent run must actually execute every degree, pin source and
commands, and preserve failed/corruption controls as applicable. Only then
may the range corner claim be upgraded. Required Claude audit is separate.
