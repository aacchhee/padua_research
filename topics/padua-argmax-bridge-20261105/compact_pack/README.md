# Padua compact Syvert2 pack

Fresh complete offline delivery. Default `./run` attempts all280 pairs:
7 known degrees and273 residual degrees, each primary plus fresh verification.
It uses30 allocated cores and the requested128000000000B aggregate RAM cap.
Mathematical sources, engine FREEZE and120CPU/pass caps are unchanged.
No path-length, minimum-RAM, zero-swap or fixed scratch-space policy applies.

After installing this NEW release in a fresh directory on Syvert2:

```
chmod +x run run_small run_large finished_cases collect_data
nohup setsid ./run >run.log 2>&1 < /dev/null &
```

The parent now prints completed cases into run.log. `./finished_cases` also
handles partially written status files as in-progress/incomplete. Launchers
use beregning, then the existing bounded-memory cgroup or user systemd scope.
Pinned arithmetic packages are offline. Linux x86_64, CPython>=3.10,
c++/readelf/ldd and compatible GLIBC>=2.38 are required.

After every validated, fully reaped pass, identical immutable native files
and libraries are hardlinked into the shared SHA store. Every original path
and byte stays available. Mutable logs and JSON files are never deduplicated.
This removes repeated library copies; unique preprocessed TUs still occupy
space. Full280 physical usage must be measured, not promised below a quota.

After the run stops cleanly:

```
./collect_data --archive-directory ..
```

Send the printed **compact .tar.gz** back. It contains every completed
primary/fresh essential certificate and accounting/exit metadata. It also
contains complete histories for two randomly selected completed RESIDUAL
degrees, including the exact external SHA objects needed to check them.
The random32-byte seed, full eligible list and draw are recorded after
validation, once per completed coverage. No hand-picked sample is used.
With fewer than two completed residuals, it records that smaller sample.

All completed full histories are validated on Syvert before export. All
other histories stay there; they are not silently included in the transfer
and no cold-storage upload is required. The reviewer checks all returned
rational proofs, checks the two full histories and separately reruns those
two degrees with the native engine in the sandbox. Unsampled raw histories
are explicitly server-validated, not claimed independently read in sandbox.

A completed two-case copied-history check returned40.2MB and preserved every
original proof byte. Collection prints actual bytes; full-worklist metadata
and different sampled histories can change the size. Nothing is truncated. A full raw ZIP remains optional via
`python3 -I -S -B server.py collect_full --archive-directory ..` and is NOT
the default file to send.

Runs stop at the first failure. Cheap fresh reruns are allowed; wait until
all writers stop and use a fresh output tree. The user has explicitly
authorized discarding the old partial delivery. This release does not
migrate or salvage that old campaign. A new unclean hard-killed campaign
can likewise be rerun rather than adding a recovery framework.

`run_small` and `run_large` retain the disjoint7/273 groups. Choose the full
run OR the split groups. Keep source/manifest identity with the compact
return so regeneration is possible; do not overwrite active writers.

## Production and retention record

SOURCE_CUSTODY.json identifies the exact published source commit; runtime_manifest.json
identifies every operational/scientific/header/library input by bytes andSHA256.
The engine FREEZE is unchanged, and asset_provenance.json pins the six official
Debian packages. plans.py gives the exact7+273degree set. Every degree is run
in a separate producer process, then a freshly built retained-proof verifier,
with recorded n, arguments, output paths, compiler/TU/library identities, direct
exit status and complete accounting. The exact commands and input identities
are retained per case, with the complete program in this offline release.

Before export, Syvert validates every completed full history again. The compact
return records each primary/fresh certificate hash and raw-history hash, exact
completed/missing coverage and server verification. Its persisted randomseed,
eligible residual list and selected two degrees document how the sample was
drawn; rerunning collection preserves the draw. All returned rational proofs
can be independently checked, while only the two sampled raw histories are
independently inspected and natively rerun in the sandbox.

AC explicitly accepts that unsampled certificates need not be in cold storage.
Their exact production is documented and reproducible from the released source
and pinned inputs; no claim of complete cold archival or sandbox inspection
of every unsampled raw history is made. Historical timing/paths need not be
bit-identical on regeneration.
