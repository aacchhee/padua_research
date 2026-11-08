# Audit-03 E-01–E-04: focused compact-verifier development

Date: 2026-11-08. Rules/input:
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530`.
Role: delegated Codex technical developer; serving model/effort unexposed.
**Distinct technical review accepted.** The [independent review](independent-checks-onset512-response.md)
separately executed the unchanged original return and all30 focused controls,
with observed exit0. This is a verification
record, not a new mathematical claim, independent audit or readiness decision.
No novelty content is added. Sources: [audit E](audit-03/e-evidence.md),
[original return](compact-return.md), and the unchanged released validators.

Root released this work only after the certificate developer recorded all 191
new pairs quiescent and final helper hashes unchanged. No verifier/helper edit
occurred before that barrier. The sole existing file changed by this task is
[compact_pack/verify_compact.py](compact_pack/verify_compact.py). New focused
controls are [code/compact_verifier_audit03/check.py](code/compact_verifier_audit03/check.py).
No engine, scientific freeze, package copy, archive, other compact helper,
manuscript or global registry was changed by this worker.

## Candidate behavior

- **E-01:** reject any returned payload name also present in the authenticated
  trusted package manifest. Engine and asset-provenance reads go to that
  package; unknown engine/provenance names reject. The returned runtime
  manifest must equal the trusted bytes, and subsequent reads use trusted
  bytes. Archive data cannot shadow those sources.
- **E-02:** reuse existing `archive_io.verify_admissions` and `verify_history`
  through a small read-only view of the already loaded tar payloads. Check
  registered/disjoint run plans, job/admission scope and exact never-started
  lists. Check provisional per-pass summary result/first_failure, exact summary
  receipt identity, shared registration/summary/receipt freeze, started run
  binding, pass commands and fresh-primary identity. Require fresh tree,
  S/actual key sets and norm method to match the primary. Fresh numerical
  enclosures are allowed to differ. Require the exact set of server-validation
  records and match attempt and both receipt/raw hashes.
- **E-03:** optional `--expect-plan all|small|large|rehearsal` requires exact
  completed coverage for that existing registered plan. Omitting it retains
  completed-subset verification; PASS alone still does not mean full coverage.
- **E-04:** enforce the existing 24 GiB logical expanded-payload cap before
  reading another regular payload or adding a hardlink alias. Alias length is
  charged as its target's logical size, matching the existing inventory cap.
  COMPACT.json retains its separate 16 MiB bound. Existing 512 MiB per-member
  and member-count limits remain; no new scientific or conservative resource
  threshold is introduced. This is an early bound, not a claimed low peak-RAM
  implementation: payloads are still held in memory up to the existing cap.

Unsampled raw histories are absent from the compact return. Their new checks
compare the server-recorded raw SHA with the receipt/summary raw identity;
they do not pretend to hash absent raw bytes. The two sampled complete histories
continue through the existing full validator. No native re-execution occurs.

## Actual development checks

The unchanged original return is 36,045,486 B, SHA-256
`b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a`.
The trusted package is the original local `compact-release-aea62883/padua30`,
manifest SHA-256
`5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16`.
All 250 package files are present and authenticated here; no absent-file adapter
was used. The original offline ZIP and its package tree remain unchanged.

Executed from the repository root, observed exit 0:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py \
  local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz \
  --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 \
  --manifest-sha 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16 \
  --expect-plan all
```

Result: **280 pairs / 560 rational certificates**, exactly 41..319 plus 511;
sampled complete histories checked: **199, 238**. This is execution of the new
source-tree candidate against the old source/runtime package. It does not
relabel the new verifier as the verifier used in the original run.

Executed focused controls, observed exit 0:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/code/compact_verifier_audit03/check.py \
  --archive local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz \
  --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 \
  --output local-output/argmax-bridge-20261105/compact-verifier-audit03-controls-20261108/receipt.json
```

The script invokes the candidate's full data path on all original
payloads, then runs **30 focused controls**, using 12.845004368 process CPU-s in
this execution. It rehashes mutated JSON and updates the synthetic COMPACT
inventory so semantic rejection is tested beyond inventory hash failure.
Controls cover trusted namespace shadowing; ledger hash/retry; missing or
invalid preflight/current-summary/resume records; summary status, failure,
receipt and freeze identities; started binding; attempt/raw validation hashes;
duplicate/extra validation rows; never-started lists; wrong expected plan;
completed-subset acceptance with full-plan refusal; fresh tree/key/method
relations; and numerical changes allowed at the same fresh keys.

Two small synthetic tar-reader controls substitute a seven-byte aggregate cap
**inside the test only**. They assert that a second regular payload is refused
before `extractfile`, and a hardlink alias counts towards the logical cap.
The production cap is restored and asserted equal to 24 GiB. These controls do
not allocate multi-gigabyte data and do not change runtime production limits.
The fresh-shape unit controls isolate the pair relation; the original full
baseline separately executes the real rational checker on every certificate.

The fresh output path above is exclusive. For a later rerun choose a new
output path, preserving this original development receipt. No native, compiler,
producer, Syvert, external retrieval or archive-supplied executable ran. Static
compilation of the candidate and scoped `git diff --check` also passed.

## Exact candidate and source identities

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| New source-tree verify_compact.py | 13,897 | 5867ac0c6d6e1d380d72c118262177a10b617631e039da11f489e45c93ff61b6 |
| New focused check.py | 10,363 | a256cb9abc0e0610b36880aa5eed09e3c5b90c8e9ab518cd406982ce9a8017d3 |
| Development control receipt (off Git) | 5,170 | 709c76952f0ce728924fd93d407bc6ce0d68057f7b7b13b80c5272524897c2ce |

The old package verifier remains SHA-256
`7c2dad53519aff616bdadd3f925ec8943963cb4bf521b410355f827b7a1899bf`.
The package manifest authenticates **that historical version**, not the new
source-tree verifier. Its copy and the historical operational CANDIDATE.sha256
are not silently repinned. Root must record the new reviewed candidate/source
identity when publishing this operational repair; a release for a future run
needs its own reviewed manifest. Scientific FREEZE is unchanged.

The control script also compares each imported helper below byte-for-byte to
the original trusted package. These remain unchanged:

| Helper | SHA-256 |
|---|---|
| archive_io.py | 1af590ff0ed64ee51a3e264d08f944f134529c5bb52a936f1129803ab1920981 |
| common.py | 81841029b5c78b9dfa307c80ee60581d20d9405fa8b089f55b1a024c3bc2b58c |
| evidence.py | f5bf30eb06d649602ba842fa7852dc26103089f4672f3016f525a3fada4154bd |
| ownership.py | 4d53d9ad0e0f8ad9119d79031edd8c0d1f4e2046bd0e4f7008e835ef241b6825 |
| plans.py | 61e901dfd2929fbfdc24f4adc53979c14d32b4621c3a824c589d971a0e563de0 |
| process_guard.py | 05d2da2ff1a48a8298067c40d9ece7fe45ea26d59c36a9b6dbe1704e20507779 |
| storage.py | 274d009dbba97a34729b21d1319e26f684406ad8313782397c5a83ed88c69768 |

## Remaining step

Distinct focused technical review must inspect the changed verification path,
rerun the unchanged archive and controls, and decide whether E-01–E-04 can be
closed. Root owns integration, ledger statuses and the new source commit.
This worker does not mark the repair adopted or any manuscript/certificate
batch ready. Historical audit findings, chronology and source pins remain.
