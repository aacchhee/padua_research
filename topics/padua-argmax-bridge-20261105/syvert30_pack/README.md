# Padua Syvert2: thirty workers, 128GB aggregate RAM

NEW artifact; original ZIP8274249f…e38b stays immutable. This pack uses the
repaired local operations v3 and unchanged frozen scientific engine. The
worklist remains7 known controls plus273 residual degrees,280 primary/fresh
pairs. No residual case or Syvert2 run has occurred in preparation.

After exact-source review, publication and root's released build, copy the
new ZIP to Syvert2. Preserve its separately supplied SHA256 and byte size.
Extract fresh to your chosen directory; there is no path-length restriction.
Never unpack over a started campaign or move one after an attempt starts.
The engine still enforces the actual essential-receipt size below16384bytes.

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
Preflight checks the actual RAM cap and records host RAM/headroom and
visible ancestor limits. Worker2GiB address-space limits remain unchanged;
they are not an aggregate-RSS bound. No minimum-RAM or zero-swap policy is
imposed. Requesting a scope does not reserve physical RAM.

If the user memory scope is unavailable, use an existing scheduler cgroup
with memory.max<=128000000000B or a working user systemd memory scope.
The requested128GB RAM cap remains enforced; no privileged setup is added.
If allocation affinity has fewer than30 cores, correct the beregning
allocation before rerunning preflight. Preflight-only failures may resume
with `./run --resume`; all previous failure epochs remain preserved.

Other commands: `./finished_cases`; after the supervisor stops,
`./collect_data --archive-directory /adequate/archive/path`. Collection
requires source-bound quiescence and streams a complete return archive;
it measures the actual compressed archive peak against available space
before writing. No fixed scratch-space floor or extra reserve is imposed.
The destination may be another adequate volume; raw data is never deleted.

Stop on first failure. Reruns are allowed. After every campaign writer has
stopped, preserve old outputs outside the package and start a fresh cohort:

```
mv outputs "../padua30-outputs-$(date -u +%Y%m%dT%H%M%SZ)"
./run_small
```

Choose `./run`, `./run_small` or `./run_large` for the fresh attempt. This
reruns that inexpensive cohort; no retry flags or recovery framework are
needed. Never move outputs while writers are active. Partial return
validation still reports exact completed, failed/interrupted and
never-started sets; a partial campaign is not a proof of the full gap.
`run_small`/`run_large` retain the disjoint7/273 interface; choose either the
full run or the split campaign, never overlapping runs. Both use the same
30-worker allocation. `run_rehearsal` remains known41/511 only.

All pinned arithmetic packages and source inputs are offline. Target needs
Linux x86_64 LP64, CPython>=3.10, c++/readelf/ldd, compatible system loader
(pinned libraries require GLIBC>=2.38), beregning and the bounded memory
allocation above. No system-library substitution is permitted.
