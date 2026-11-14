# Prospective replacement of the missing polynomial checker executable

Status: prospective; no compilation or native arithmetic has been launched.
Rules read at `82e75e586d19a570d42648accbd3b99179991774`.
Codex developer, serving model/effort metadata inherited from the coordinator;
requested allocation Sol medium. No new mathematical claim or novelty content;
the novelty gate is inapplicable to rebuilding a frozen checker.

## Scope and retained evidence

AC asks to regenerate missing paper-dependent artifacts. The historical binary
`/tmp/padua-consolidation-small-metadata-review-_twddn_u/kernel` is absent.
All 39 compressed polynomial certificates for degrees 2 through 40 survive,
as do the accepted result records. The historical executable bytes and timings
are not needed for the mathematical implication. This step builds a current
executable from the unchanged metadata-corrected checker, retains its runtime
closure, and strictly replays the special degree-2 metadata case followed by
ordinary degree 17. It neither recreates the historical executable identity nor
claims a new full 39-degree arithmetic replay.

The existing `code/small_degree_unification/METADATA-FREEZE.json` identifies the
unchanged strict checker, baseline and metadata-corrected kernels, wrapper and
metadata patch. New `code/regeneration_polynomial_20261114/frozen-inputs.json`
pins these bytes, the common witness index, all 39 compressed inputs, checker
provenance dependencies and the new orchestration script. Static readback has
matched every compressed certificate size/hash against the common index and
all existing metadata-freeze source identities. No certificate is generated,
modified or rescued; there is no producer, search, retry or alternative kernel.

## Cost assessment before execution

The committed `padua-argmax-effective-20261103/evidence/native-checker-summary.json`
records degree-17 inclusive Python/native CPU 5.010504000000001 seconds and wall
5.01063054999986 seconds; its final receipt records 4.985913 wall seconds.
The retained degree-17..32 final-row wall times sum to 1066.193767 seconds.
The eight bridge `evidence/independent-n33.json` through `independent-n40.json`
receipts record 805.6156330850001, 813.2303646120001, 820.5946161949998,
925.8015888400002, 918.513542228, 1072.042953558, 1216.55080469 and
1367.416693362 seconds, respectively. These historical measurements are an
estimate only, not current timings or an aggregate CPU measurement. They show
that a full 39-case replay would be a substantial additional campaign.
The retained small-degree checker summary reports 19.153825 child CPU seconds
for the historical compile plus all 15 degree-2..16 checks. Rebuilding once
and checking only 2 and 17 should therefore be modest; no timing guarantee is
inferred. The coordinator schedules this single-core task around the ongoing
four-worker native/I25 work.

## Fixed prospective procedure

The coordinator commits this preregistration and code after the distinct
reviewer clears them. Only then execute from the repository root:

```sh
python3 -E -S -B topics/padua-argmax-bridge-20261105/code/regeneration_polynomial_20261114/replay.py --execute
```

The exact fresh output root is
`local-output/argmax-bridge-20261105/polynomial-regeneration-20261114`.
An existing root refuses execution; no resume or overwrite is provided.

1. Authenticate all frozen input bytes. Create the fresh output root. Record
   Python/platform identities, compiler tools and GMP header bytes.
2. Compile exactly once with `g++ -v -O3 -std=c++17`, the frozen
   `metadata_kernel.cpp`, `-lgmpxx -lgmp`, and output `kernel`. CPU limit is
   60 seconds per process, wall limit 300 seconds, address-space limit 2 GiB.
3. Run bounded `ldd` once (5 CPU seconds per process, 30 wall seconds), retain
   its output and SHA-256/size/path identities of every resolved runtime
   library and the new executable. Compilation's verbose log identifies the
   toolchain invocation. Environment/tool identities accompany the closure.
4. Run the frozen strict wrapper with `python3 -E -S -B`, the untouched n2
   input, the new executable and a fresh receipt path. Per-process CPU limit
   15 seconds; wall limit 120 seconds; address space 2 GiB.
5. Only on clean n2 acceptance run the same wrapper once at n17. Per-process
   CPU limit 60 seconds; wall limit 300 seconds; address space 2 GiB.
6. Require each actual direct child exit zero, no cleanup, complete partition,
   all supplied bounds verified, acceptance true, correct degree, expected
   leaf counts, two corner leaves and exact input/binary identities. Rehash
   the full frozen inventory before each arithmetic check and at completion.

All stages inherit affinity to one available CPU. No parallel polynomial jobs
are admitted. Each stage runs in its own process group. The supervisor uses
owned `wait4` status and usage, fails on ECHILD or missing status, and kills
the complete owned group on interruption, error or wall timeout. It records
raw stdout/stderr, actual argv, actual wait status, inclusive child CPU and
maximum RSS. Limits are per process; the Python wrapper's inherited CPU limit
also applies independently to its native child, not as a shared aggregate cap.
Any failure stops this fixed sequence and preserves observations; it grants
no retry. A completed summary explicitly says only degrees 2 and 17 were
replayed. The existing portable all-39 commands remain documented in
`paper/small-degree-unification.md`.

The new executable and closure are regenerable current artifacts, not recovered
historical bytes. Local retention is not external delivery or durable custody;
the coordinator integrates them into the requested downloadable reproduction.
