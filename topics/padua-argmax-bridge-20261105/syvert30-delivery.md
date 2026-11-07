# Syvert2 delivery —30workers,128GB total RAM

**Ready for AC's authorized run.** New offline ZIP (25,095,407B):

`local-output/argmax-bridge-20261105/syvert30-7cf34bcee4be9bdd5b4a871426083333a89b7c15/padua30.zip`

SHA256: `e51b442ba541ebcf9a94c3571a624692ee385c3178195d2a2ced071bd960d35f`.
The adjacent `padua30.zip.sha256` verifies the download. Source is published
`7cf34bcee4be9bdd5b4a871426083333a89b7c15`; runtime manifest52,884B SHA256
`78b40151280ada98ada945ac2e562b9ffa817279ed08b1dba219c78a94fddd55`.
The original498f4f4c Syvert2 ZIP remains immutable and is superseded for this run.

## Run on Syvert2

Extract fresh on a DISK-backed volume with at least32GiB free, at a resolved
path no longer than32characters. Example:

```sh
sha256sum -c padua30.zip.sha256
unzip padua30.zip -d /scratch
cd /scratch/padua30
./run
```

This is the familiar A/B/C beregning interface. Full run: EXACTLY30 workers,
one inherited core each,7 known controls plus273 residual degrees, primary
then independent fresh execution per degree (560engine passes). The guard
uses an existing bounded scheduler cgroup or a user systemd scope to enforce
**128000000000B aggregate memory.max** (decimal128GB,119.21GiB) for the whole
campaign tree. Visible swap is zero. Per-worker2GiB address-space limits and
120inclusiveCPU seconds/pass remain unchanged. Kernel memory control is the
enforcement; per-process limits and RSS extrapolation are not substitutes.
Host needs30allocated cores, compatible offline runtime (glibc>=2.38), Python,
c++/readelf/ldd and usable bounded cgroup-v2 memory allocation. No uncapped fallback.

`./finished_cases` reports progress. When stopped, collect the FULL return:

```sh
./collect_data --archive-directory /adequate/archive/path
```

Send that ZIP without pruning raw/build/runtime/captured bytes. Stop-first-failure
and append-only admissions apply; no failed degree is retried. Preflight-only
failures can resume after correcting the allocation with `./run --resume`.
Return validation accepts an exact completed subset via `--partial`; it never
promotes partial coverage to all-degree closure. Full instructions: [README](syvert30_pack/README.md).

## Measured basis and extrapolation

Actual repaired sandbox41/511 rehearsal:16.306s wall,29.675waitedCPU-s;
four engine calls27.554CPU-s; maximum individual wait4RSS159900KiB.
All four proofs/raw/build/maps and the complete returnedZIP were independently
validated. [Review](independent-checks-audit02-known-integration.md).

If the two known cases represent all280pairs, CPU arithmetic gives4154.5CPU-s
(1.15CPU-hours), about138.5s at ideal30-core utilization. Observed wall scaling
gives about152s. These suggest minutes of compute under those assumptions;
unknown degree difficulty, Syvert hardware, concurrent compiler/capture I/O,
and archive compression can materially change it. The engine cap envelope is
67200CPU-s,37m20s at ideal30CPU, excluding operations/tail; it is not a wall
completion promise or a uniform success result.

Collection is a separate likely bottleneck: sandbox collector stdout-file birth/write timestamps span approximately31.26s for its93.60MB returnedZIP. Scaling by the5.87GB compressed full-return proxy suggests roughly33minutes at similar single-collector throughput. This is a timestamp-based planning estimate, not a measured full-campaign benchmark; fixed costs and Syvert I/O/compression speed differ.

Thirty times the measured INDIVIDUAL RSS maximum is4.91GB. This is only a
size illustration: it omits simultaneous parents/compilers/page cache and
unrun-case variation, so it is not an aggregate memory forecast. The actual
128GB cgroup cap provides the requested total bound. The80GiB admission floor
is planning policy, not measured need or a reservation guarantee.

Branch-weighted storage proxy (215lower-degree-style pairs,65upper-style):
14.256GB raw plus5.870GB compressed payload,20.126GB together before ZIP
metadata/reserve, assuming the known41/511 branches remain representative.
The shared86MB capture store is counted once. It may grow; no uniform output
size is proved.32GiB initial scratch and measured archive-peak admission leave
practical headroom; insufficient space preserves raw data for another volume.

## Source, controls and actual artifact checks

[Independent final review](independent-checks-syvert30.md) accepts the new
source,23independent cgroup/guard/preflight assertions, and actual251-entry ZIP:
244manifest rows,35source paths,21operational pins,13scientificFREEZE rows,
six pinned Debian packages,nine arithmetic aliases,six0755launchers. It checks
allpayloads/safe names/modes/source/worklists/memory policy. The unchanged
scientific source and repaired operational path also have actual known-case
integration evidence. Actual Syvert2/systemd/beregning behavior remains target
preflight's responsibility; no remote or residual run occurred here.

Builder ran ONCE after source/release publication, directEXIT0, session62862,
completion9caad3, no stderr; tree+ZIP74,863,015B<2GiBreservation. Exact command
and limits are in LOG. [Receipt](evidence/syvert30/delivery.json). Artifacts remain
ephemeral local working copies; physical cold-storage transfer/durable external
retrieval are pending. This is an execution delivery, not a claim that the273
open degrees or PD-T099 have been proved. Branch WORK; unwaived chronology
findings and final Claude mathematical/record audit remain separate.
