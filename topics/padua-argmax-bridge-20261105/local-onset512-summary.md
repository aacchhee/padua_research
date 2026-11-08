# Local onset-512 certificate campaign

Status: **finite computation and distinct result review accepted** under the
unchanged native-evaluator trust boundary. The [review](independent-checks-onset512-response.md#local-native-campaign-and-compact-return--accepted-at-recorded-scope)
independently checks all accounting and archive data; it makes no additional
native replay claim. The next substantive Claude audit remains separate.
The [preregistration](preregistration-onset512-local.md) fixes all 191 degrees
320..510, each primary plus separate fresh verification, with no retries.
Rules/input HEAD is `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`.
Technical work requested as Codex Sol medium; serving metadata are unexposed.

All output is outside Git at
`local-output/argmax-bridge-20261105/onset512-local-20261108/`.
All **191 pairs / 382 passes** completed, with observed engine and wrapper
exit 0, ECHILD, no timeout, failure or cleanup kill. Full trusted compact
`validate_pass` accepted every pass; primary/fresh retained proof fields agreed
for every pair. The terminal summaries record exact coverage and clean quiescence.
Final statistics were saved at 2026-11-08 10:56:05Z.

Engine-child CPU totaled 2,700.875 s; wrapper inclusive waited usage totaled
2,825.091 s (0.785 CPU-hours). The pilot used 12.632 wall-s and the remaining
190 pairs 765.823 wall-s, with at most four cases running. Per-pass child CPU
min/median/max was 5.643 / 7.022 / 9.004 s. Maximum reported wrapper/descendant
RSS was 112,688 KiB. The actual n=320 pilot used 5.889 CPU-s for the primary
and 5.651 CPU-s for fresh verification; it was not retried.

The 120 CPU-s per-pass cap is the frozen engine's aggregate bound. The outer
260 s wrapper RLIMIT_CPU bounds wrapper self CPU, not aggregate descendants.
The sandbox exposes a four-core CPU quota and 16 GiB memory limit. Four workers
run, each with 2 GiB address-space limit. One recorded campaign-process RSS
snapshot at 10:47:48Z was 607,680 KiB summed across processes (shared pages
counted in each process); total host cgroup memory then was 1,082,097,664 B.

The unchanged FREEZE and arithmetic pins are checked before/after each case.
The compact helper files were additionally observed byte-equal to the input
HEAD during the running epoch, saved with hashes in `helper-source/` and
`helper-source-pins.json`, and rechecked unchanged after quiescence. Their
`evidence.py` pin also matches the original machine preregistration. This
supplemental observation is not an additional preregistered enforcement rule.

The compact return is outside Git:
`local-output/argmax-bridge-20261105/onset512-return-20261108.zip`,
**81,602,992 B**, SHA-256
`da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e`.
It contains all 382 essential proofs, all small JSON/log/provenance records,
trusted-source/runtime hash manifests and two complete sampled native histories.
All other complete native histories remain in the local campaign tree (632 MiB
reported by `du -sh`). No bulk proof evidence has been added to Git.

After complete coverage, validation receipts and quiescence were checked,
`os.urandom(32)` supplied seed
`cb52b5324c8fa5bca69665affe22016950ca48661a429a3fa4b6e4a77bfadcdb`.
`random.Random(seed_bytes).sample(sorted_completed_degrees, 2)` drew **475, 458**
at 10:56:48Z. The seed, exact population, draw and method were persisted once in
`compact-selection.json`; there was no redraw. This is a transport/review sample,
not a statistical proof.

ZIP creation exited 0 with ECHILD and no cleanup kill (27.900 wall-s,
27.861 CPU-s, maximum RSS 402,784 KiB). The separately trusted data-only reader
reconstructed every rational proof, checked accounting/exits/admissions and
primary/fresh linkage, reproduced the draw and fully validated both sample
closures: exit 0, 4.014 wall-s. A second run from a relocated trusted source and
runtime mirror under `/tmp/padua-onset512-portable-20261108b` also exited 0
(3.717 wall-s). It used archive data for all original campaign paths. Neither
run extracted or executed archive code. The ZIP README identifies the separate
trusted release (`996fedcad4ba79a28e45a3fe3678adc12f1e5358`) and the runtime
payload restoration paths and hashes. Logs and observed-resource JSON are in
`local-output/argmax-bridge-20261105/onset512-return-build-20261108/`.

The initial packaging resource-wrapper command stopped before Python execution
because `/usr/bin/time` was absent (exit 127); its logs are preserved. Actual
export and verification were instead observed with the runner's `wait4` helper.
No scientific call was repeated. Cheap unsafe-path and missing-inventory ZIP
controls were rejected before this export.

An immutable data-only mirror of exactly 382 certificate JSON files is at
`local-output/argmax-bridge-20261105/onset512-local-20261108-essential/`.
Its sibling inventory is 75,479 B, SHA-256
`d7cea34dd64d9df329d1398c2418fbf984a9084b135cad695866a9c437551740`.
This supplies the independent-arithmetic campaign; it contains no logs or
noncertificate JSON. The onset gates have separate distinct mathematical
acceptance in J01/J02. Independent arithmetic over all inputs and the next
substantive audit remain separate obligations. Archive integrity alone is not
the theorem implication.

A small derivative certificate dataset is also available:
`local-output/argmax-bridge-20261105/onset512-certificates-20261108.zip`,
945,235 B, SHA-256
`c22d600cb67462918587b01f2ef5adcbf9030b825fb0f2cc79c1b9c27c7da8c8`.
It contains exactly the 382 immutable mirror certificates, their inventory and
a brief README, and was checked byte-for-byte against the mirror inventory both
before writing and after reading. It is not the complete provenance return;
the 81.6 MB ZIP remains the canonical review artifact. No native call was added.

Verification command, from the trusted repository:

```
python3 -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/return_bundle.py verify local-output/argmax-bridge-20261105/onset512-return-20261108.zip
```
