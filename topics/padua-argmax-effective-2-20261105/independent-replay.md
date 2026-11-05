# Independent native replay — 2026-11-05

Rules and input head: `ed21cc0bf205549936fccde90244a291bc6de324`.
Role: fresh Codex independent replay subagent, assigned gpt-6.1-sol medium.
The runtime does not expose model identity/effort through a verification tool;
this records the requested allocation, not a guessed runtime attestation.
This supplements the later Claude audit and makes no new mathematical claim.

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, handoff 01,
the pre-execution plan, frozen native READMEs and drivers, canonicalization
provenance and phase-1 producer/checker summaries. The novelty gate does not
apply: this task reproduces existing certificates without proposing mechanisms,
changing mathematical statements, or making novelty/priority claims.

The phase-1 code is used read-only. No Git state changes were performed.
Cloud runtime context was read using the cloud-environment-runtime skill;
the environment reported current observations, connected execution and an
enforced restricted network policy. No network request or external compute
was needed for the replays.

## Reproduction

From repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python topics/padua-argmax-effective-2-20261105/code/replay.py \
  --work local-output/argmax-effective-2-20261105/replay \
  --summary topics/padua-argmax-effective-2-20261105/evidence/replay-summary.json
```

The runner compiles the independent C++ checker with `g++ -O3 -std=c++17`
and GMPXX/GMP. It invokes the unmodified phase-1 producer driver, which
snapshots and compiles its C/GMP source with `gcc -O3 -Wall -Wextra -Werror`.
Each degree has its own producer work directory. Every subprocess has an
initial 900-second wall limit with process-group termination on timeout;
the producer additionally uses its inherited 600-second search CPU limit.
All bulk generated files, source snapshots, input files, certificates,
binaries and raw receipts remain under the specified local-output directory.

The small [summary](evidence/replay-summary.json) records actual commands,
source and binary hashes, generated input hashes, versions, CPU identity,
per-command CPU/wall measurements and all four acceptance verdicts.
CPU measurements use RUSAGE_CHILDREN deltas around sequential fresh
subprocesses and include each Python driver's waited-for native/compiler
children. Wall times reflect concurrent sandbox load, so these measurements
do not support a new scaling or throughput claim.

## Verification scope

**Result: all four checker processes accepted.** Both regenerated certificates
are complete and exactly reproduce the committed mathematical payload,
including all frontier paths and bounds. Actual differing fields are only
the three timing fields; the native source/binary/input provenance also
matches. Mathematical SHA-256 values match the phase-1 producer summary,
and committed byte hashes match both phase-1 producer and checker summaries.

| Degree | Bound leaves | Corner leaves | Splits | Producer CPU / wall (s) | Regenerated replay CPU / wall (s) | Committed replay CPU / wall (s) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 104 | 2 | 105 | 4.160 / 4.178 | 9.545 / 9.600 | 9.173 / 9.195 |
| 24 | 152 | 2 | 153 | 27.320 / 27.373 | 60.977 / 61.019 | 59.855 / 59.871 |

Checker compilation used 2.439 CPU / 2.474 wall seconds separately.
The actual environment was GCC/G++ 14.2.0 (Debian 14.2.0-19), GMP/GMPXX
6.3.0, Python 3.12.14, Linux x86_64 with glibc 2.41, and an AMD EPYC 9V74
80-Core Processor. The fresh checker binary SHA-256 is
`f17fed2e69a98c952d1ad5e72de03c08b2ceb07970c49fc0db1b35396fe3e605`,
identical to the phase-1 summary. Full per-command measurements and hashes
are in the 14,204-byte replay summary; no cap was reached.

The runner compares every certificate field after removing exactly
`setup_seconds`, `search_seconds`, `total_seconds`, and `producer_provenance`,
matching the phase-1 mathematical-hash convention. It also compares the
entire frontier and every bound directly and checks both the committed
certificate byte hash and mathematical hash against the phase-1 summaries.
It replays each regenerated certificate and each committed certificate in
fresh checker processes, checking exact metadata, complete prefix partitions,
all supplied integer bounds and both corner leaves.

Raw gzip hashes may differ because timings and native provenance differ;
they are not the equality criterion for mathematical reproduction.
No fresh corruption controls, checker unit program or reference-Python
checker were run. These are existing-code replays at n=17,24 only, not a
fresh audit of the arithmetic derivation or PD-T210, an extension to new
degrees, or a new all-degree claim. Existing schema/formula/rounding
dependencies remain shared between the frozen producer and checker.
Bulk outputs are local and pending the orchestrator's archival decision.
