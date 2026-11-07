# Final Padua Syvert2 pack — source candidate, NOT RELEASED

This follows the actual pinned bttb-research A/B/C delivery interface inspected
through the GitHub connector, not its numerical algorithms. Research extension
has ended. The accepted global tail covers all integer n>=320. Prospective
small portability group: 41,42,63,64,159,160,511. Prospective large group:
43..62,65..158,161..319 (273). Their disjoint union is exactly280 cases.
No case in this source candidate has run. No new mathematical idea is proposed.

Source publication, independent source audit, release of bounded operational
tests, and a separate final Claude audit/release precede numerical pack launch.
The branch remains WORK. An interim audit is not bulk-run permission. There
are no Syvert2 credentials or configured VPN in this session; no remote launch
is possible here. Host hardware/allocation facts remain unverified.

## Delivery after release

The producer takes an explicit published full source SHA. It checks each copied
CODE/DATA byte against that commit, checks the hybrid FREEZE, and writes a fresh
ZIP under existing Padua local-output. No .git is needed on Syvert2. The producer additionally requires dpkg-deb for
reading the six trusted package archives, which are copied into the offline pack. The runtime
manifest freezes every CODE/DATA input, operation, header and library byte. Prose
hashes provide custody only and never decide scientific acceptance. The producer
uses actual phase-checker/extracted assets, not a wheel. All FLINT/GMP/MPFR header and library payloads are checked byte-for-byte against
six SHA256-pinned official Debian packages; matching version/architecture metadata
is additional attribution, never a substitute for byte verification.
The pinned packages, full target loader closure, and asset provenance are included; target preflight refuses incompatibility
and missing assets before the frozen setup.py network fallback can be reached.

After audit/release and source publication, root may run (unexecuted example):

```sh
python3 -E -S -B topics/padua-argmax-bridge-20261105/syvert2_pack/build_pack.py \
  --source-sha PUBLISHED_FULL_SHA \
  --destination local-output/argmax-bridge-20261105/final-syvert2-PUBLISHED_FULL_SHA
```

Unpack into a fresh directory. Retain the released ZIP and its SHA256 separately.

```sh
chmod +x run run_small run_large finished_cases collect_data
./run_small
./run_large
./finished_cases
./collect_data --archive-directory /adequate/archive/path
```

Alternatively `./run` attempts the full280. Full and split outputs cannot overlap.
`./run --workers 4` selects fewer inherited cores, never more than40. `beregning`
provides allocation; executable, shell function and module fallback are supported.
No host idle-core scan, affinity expansion or cross-campaign scheduling occurs.
The package targets hostname syvert2 only, CPython>=3.10, Linux x86_64 LP64,
/proc, libc subreaper support, c++, readelf, ldd and compatible offline libraries.
Preflight is operational metadata/loader inspection, never a numerical calibration.

Each case owns an exclusive directory and executes primary then a separate fresh
replay with all fixed numerical premises recomputed. Engine caps remain120CPU
per pass, with fixed1050s operational pass wall and2120s case wall guards. Worker
address space is2GiB, supervisor soft address space8GiB. These reference assumptions
are not measured RSS or a Syvert2 capacity claim. The wrapper self CPU guard260s
is separate from the engine's inclusive descendant cap; no rescue or cap increase.
The engine-envelope ceiling is280*2*120=67,200CPU seconds, conditional on each
attempt respecting its engine cap; this excludes operations and predicts no
success, termination time or actual runtime. The old28.6decimal MB/pass illustration
would be16.016decimal GB for560 passes; it is not a uniform storage bound.
At least128GiB free package scratch is prospectively required for retained raw
assets plus collection reserve, with64GiB free at archive collection; a reviewer
must assess these floors, which do not guarantee sufficient capacity.

First observed failed job stops admissions; already running jobs are stopped and
all owned descendants/orphans are cleaned across process groups. All started
attempts and raw/TU/build/native/runtime evidence remain. No retry, overwrite,
precision change or evidence pruning exists. `--resume` may execute only directories
that never existed, under an identical manifest/plan/worker identity. Every existing
attempt must already have primary and fresh EXIT0 plus complete whole accounting.
A failed, interrupted or corrupt directory prevents resume; it is never retried.

Collection requires the campaign lock, no tagged live package writer and persisted
quiescence/ECHILD. It includes complete source, inputs, runtime assets, outputs and
native/build provenance. It never takes a live snapshot. Return ZIP filenames use
actual hostname and UTC. Send the full ZIP; keep the original frozen package.

Data-only checking (after release, not run here):

```sh
python3 -I -S -B verify_return.py RETURN.zip --package TRUSTED_RELEASED_PACKAGE \
  --manifest-sha RELEASED_MANIFEST_SHA256
```

The shared per-attempt validator authenticates exact whole group coverage, primary+fresh evidence,
directly captured EXIT0, whole accounting, replay linkage, raw records and the
exact rational proof checker from the trusted local package. It executes no
archive-supplied code, native oracle, compiler or producer. Successful attempts
still await a distinct independent final scientific reviewer; status alone never
certifies a degree. Preserve complete return archives off Git; small authored
custody summaries are the only intended tracked delivery evidence.

The revised validator cross-links receipt, raw/checkpoint/native endpoints, build,
stage, preregistration, summary and final accounting. Internal artifact absolute
paths map strictly under the registered package root. External compiler, headers,
Python, loader and mapped-file bytes are captured once per SHA256 under
`preserved-sha256/`; no external identity is merely attributed and omitted. Resume
uses this same substantive validator on each existing attempt before admission;
partial campaigns are supported. Collection includes all captured objects.
README and published-commit attribution remain in separate SOURCE_CUSTODY.json,
outside numerical/runtime acceptance identity. Every Python generation disables
site processing and bytecode writes: operations use `-I -S -B`; sibling engine
launches use `-E -S -B`. Equivalent package copies share a conservative manifest
writer domain: any tagged live writer in that domain causes collection refusal.

The pinned GMP6.3 runtime has an actual ELF requirement for **glibc>=2.38**.
Root's read-only `readelf --version-info` inspection found GLIBC_2.38 in
libgmp.so.10.5.0; pinned FLINT requires up to GLIBC_2.34 and MPFR less. Therefore
this offline package requires glibc>=2.38 on Syvert2. Syvert2's actual OS/glibc
remains unverified: this is a binary prerequisite, not an observed target failure.
The existing ldd preflight must reject an unresolved/version-incompatible loader
closure before any engine launch. Pins are unchanged; no compatibility experiment
or alternate dependency selection is implied.
