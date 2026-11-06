# D01 corner finite-sum measurement

Rules/input head: `4cf68980fa0538b53e2aea7174ed6e5782a34908`.
2026-11-06, Codex technical worker, parent-assigned Sol medium;
serving metadata unexposed. No Git or shared registry operation.
The mathematical worker reviewed the ranges/tails and froze SPEC.md
before the compiler or measurement was launched. This implements the
already gated P4 candidate; no new mechanism is proposed here.

## Outcome: MEASURED

This measures **K0_C07**, the complete frozen C07 envelope in SPEC.md.
It includes the regular f majorant, analytic harmless remainder, sine
csc envelope and weighted enlarged-strip charge. It does not measure the
smallest constant for the actual Lebesgue function. Positive tail bounds
are analytically justified, but arithmetic is floating without directed
rounding: the reported endpoints are measured truncation envelopes.

| n | K0_C07 lower | K0_C07 upper |
|---:|---:|---:|
| 1000 | 9.060120982745707 | 9.062836218852432 |
| 1001 | 9.062020668397757 | 9.064737064911427 |
| 10000 | 8.956214482845258 | 8.960356017728555 |
| 10001 | 8.956405437248648 | 8.960546996951647 |
| 20000 | 8.927956689916323 | 8.932231475509308 |
| 20001 | 8.928052197816330 | 8.932326990655131 |
| 100000 | 8.863487478556898 | 8.867893759893965 |
| 100001 | 8.863506585372784 | 8.867912867111040 |

Primary K<=4 at n=1000 fails. The separately preregistered weaker
K<=7.8 at n=10000 also fails. The n=20000 kill threshold is
0.1 log(20001)^2-log(20001)/3 = 6.506826419211471, below the measured
lower endpoint. Thus the kill fires for this frozen envelope. This does
not reject all sharper derivative allocations or actual-function bounds.
No new onset or all-degree theorem follows.

## Executed work and controls

The single runner invocation was:

    time python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_corner/run.py

It first wrote the prospective degree list, D=127, cap, controls, source
and specification hashes to preregistration.json. It compiled once with
g++ -O2 -std=c++17 -fno-fast-math. It enumerated only the 128 signed
small odd diagonals and bounded all omitted positive diagonals. B20/C20
used exact integer row counts across the full board, in O(n) work.
At n=100000 this enumerated 12,741,999 terms, with 4,987,358,001 terms
covered by positive tails, avoiding the full approximately 5e9-term sum.

The independent j,r board loops at n=1000 and1001 fell inside each
diagonal truncation envelope. Full n17 sums and board count matched an
independently written exact Fraction board implementation; the six
reported relative differences after conversion to double were zero.
The n17 controls check indexing only. Every numerical command exited0;
there was no computational failure, retuning, rescue or additional degree.

The runner recorded 2.511748 CPU-s through final closure hashing.
The shell measured user2.260+sys0.264=2.524 CPU-s for its complete process
tree, including compiler/helpers and supervisor. A postrun provenance
helper used another user0.077+sys0.043=0.120 CPU-s (internal0.111408).
The total shell-observed CPU is2.644s, far below the300s cap. The
postrun helper only asked the same compiler for dependency filenames
and hashed253 source/header files; it did not run the numerical kernel.

**Preserved initial environment failure:** before the actual runner,
`/usr/bin/time -p python3 .../run.py` exited127 because `/usr/bin/time`
does not exist. Python, the compiler and the measurement had not started,
and no preregistration existed. The identical runner was then launched
using the shell's builtin `time`. This is a wrapper substitution, with
no source or mathematical input change. It was reported to the parent
before continuing. All computational first failures remain absent.

## Provenance and retention

Small essential receipt: `../../evidence/d01-corner.json` (<16KiB).
The receipt pins the frozen source/specification, preregistration,
binary and full raw manifest. The original manifest records every
command/exit/CPU, stdout/stderr identities, compiler and helper hashes,
native process loaded-file maps and hashes, and Python loaded modules,
standard-library files, interpreter and mapped-library hashes.
The separate build-closure.json pins253 compiler source/header inputs.
The Python startup modules and native mapped files are captured at the
recorded checkpoints; this is runtime identity evidence, not a security
claim about all transient compiler mappings.

Raw files are in
`local-output/argmax-bridge-20261105/post-audit-D01/corner/`.
They remain local working output, pending the topic's authorized Padua
cold-storage transfer; no archive availability is claimed. The committed
source and small receipt regenerate the measurement. Fresh reproduction
requires a fresh output directory; the runner refuses to overwrite its
preregistration. Independent consequential review belongs to the parent
and later formal audit, not to this developer record.

Frozen measurement SHA256:

* measure.cpp: ab5b8154dac29336caf50ab822bbcc8b27659a4ef32102920125d669679c8891
* run.py: 6b25fc4735f0c5f9299e6e6b13da3140ca323213baf4706d3c715296e9e3b454
* SPEC.md: 5db165cee96f1011fcac0a92286632177f44d7502e9d41a6d3d08539e48c5000

Runs needed: none within this bounded measurement. Distinct review of
the scoped gate interpretation and analytic floor checks remains with
the coordinator and mathematics worker.
