# Padua Syvert2: thirty workers, 128GB aggregate RAM

NEW artifact; original ZIP8274249f…e38b stays immutable. This pack uses the
repaired local operations v3 and unchanged frozen scientific engine. The
worklist remains7 known controls plus273 residual degrees,280 primary/fresh
pairs. No residual case or Syvert2 run has occurred in preparation.

After exact-source review, publication and root's released build, copy the
new ZIP to Syvert2. Preserve its separately supplied SHA256 and byte size.
Extract fresh to a SHORT path, for example `/scratch/padua30` (the builder
should name its top directory `padua30`). The resolved path must be at most32
characters. Never unpack over an old campaign or move a started campaign.

```
unzip padua30.zip -d /scratch
cd /scratch/padua30
chmod +x run run_small run_large finished_cases collect_data
./run
```

`./run` requests the full280 with EXACTLY30 workers. The familiar A/B/C
launcher uses `beregning` first (executable, shell function, or module
fallback), preserving its inherited allocation. At least30 inherited cores
are required. A finite visible CPU quota must cover30 CPU-equivalents;
unlimited cpu.max is accepted on Syvert2. No idle-core scan is performed.

Memory guard next uses an already bounded cgroup or
`systemd-run --user --scope --property=MemoryMax=128000000000`. This is
128GB DECIMAL (119.21GiB), a kernel aggregate cap for the supervisor and all
30 workers/descendants, not128GiB and not30 separate memory allowances.
Visible swap control is set/required at zero; unavailability is recorded.
Preflight requires an effective visible memory cap between80GiB planning
floor and128000000000B and records actual host RAM/headroom and all visible
ancestor limits. Worker2GiB address-space limits remain unchanged; they are
not an aggregate-RSS bound. The80GiB floor is conservative planning policy,
not a measured memory need or reservation guarantee.

If the user memory scope is unavailable or not delegated, the launch refuses
before any numerical attempt. Use a scheduler allocation with cgroup-v2
memory.max<=128000000000B and at least80GiB, or enable the existing user
systemd memory scope. A visible swap controller must have memory.swap.max=0.
There is no sudo, uncapped fallback, new daemon or privileged installation.
The package never claims that requesting a scope reserves physical memory.
If allocation affinity has fewer than30 cores, correct the beregning
allocation before rerunning preflight. Preflight-only failures may resume
with `./run --resume`; all previous failure epochs remain preserved.

Other commands: `./finished_cases`; after the supervisor stops,
`./collect_data --archive-directory /adequate/archive/path`. Collection
requires source-bound quiescence and streams a complete return archive;
it measures compressed peak space before writing. Initially at least32GiB
free scratch is required, with another1GiB reserve at archive creation.
The destination may be another adequate volume; raw data is never deleted.

Stop on first failure. No failed/interrupted degree may be retried, even in
a fresh root. Partial return validation reports exact completed pairs,
failed/interrupted admissions and never-started degrees. It never labels a
partial campaign a proof of the full gap. Do not delete any failure or ledger.
`run_small`/`run_large` retain the disjoint7/273 interface; choose either the
full run or the split campaign, never overlapping runs. Both use the same
30-worker allocation. `run_rehearsal` remains known41/511 only.

All pinned arithmetic packages and source inputs are offline. Target needs
Linux x86_64 LP64, CPython>=3.10, c++/readelf/ldd, compatible system loader
(pinned libraries require GLIBC>=2.38), beregning and the bounded memory
allocation above. No system-library substitution is permitted.
