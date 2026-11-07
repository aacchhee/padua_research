# Compact operational variant: source contract

UNEXECUTED preparation,2026-11-07. Codex technical developer requested as
Sol medium; serving metadata unavailable. Scope is operational storage and
delivery, no mathematical novelty. Base is lean Syvert30 candidate529ee8be…
with conservative path/RAM-floor/swap/scratch policies already removed.
Only compact_pack/ and compact-delivery-draft.md change. Root owns Git,
publication, build and release. No imports/tests/native work in preparation.

Scientific engine/native sources and FREEZE
0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb
remain unchanged. Primary/fresh calls, exact mathematical predicates,
arithmetic pin checking, observed exits,120CPU/pass and all scientific
call/node/depth/receipt caps remain unchanged. Thirty allocated cores and
128000000000B cgroup RAM cap remain. No new retry or recovery framework.

## Physical deduplication

job_worker first directly waits and reaps the entire engine pass, calls
the full validate_pass including preserved runtime/build/native closure,
then storage.deduplicate. Only authenticated immutable source snapshots,
preprocessed TUs, freshly compiled binaries and copied dependency files in
that finished pass's workdirs are candidates. Pinned global assets are NOT
rewritten while other workers might have them mapped. Future builds still
compile in fresh exclusive directories; no cached native result is loaded.

Each candidate's bytes are authenticated against the build manifest.
Under the existing preserve-store lock, a canonical SHA object is linked
or verified, then an atomic replacement hardlink preserves the original
pathname and exact bytes. Immutable canonical files become read-only.
Mutable JSON, checkpoints, accounts, logs and empty files are not candidates.
No mathematical identity depends on inode or mtime. A storage failure is
reported as a failed attempt rather than pretending the optimization ran.
New storage-dedup.json records changed paths/counts/bytes without modifying
scientific evidence. Exact-byte copies of unique #line-path-dependent TUs
cannot be deduplicated and remain on disk.

## Compact export

Default collect_data holds the existing campaign lock and requires genuine
persisted clean quiescent/ECHILD run state. It does not forge those bits or
solve an old hard-kill recovery problem. Root explicitly selected a fresh
new campaign and cheap reruns; unclean collection simply refuses. Cleanly
stopped partial campaigns may return their exact completed subset.

Every purportedly successful pair is fully revalidated on Syvert through
unchanged validate_attempt arithmetic/native/raw/build/source/map linkage.
Invalid completed evidence fails collection. Partial/malformed attempt
status is reported as in-progress/incomplete, never accepted as a proof.
All completed certificates, accounting, preregistration, pass/wrapper exits,
attempt and run/history metadata are retained in the compact bundle.
Per-degree receipt/raw/attempt hashes document the server's validation.

After this complete local validation, os.urandom(32) supplies a seed.
random.Random(seed_bytes).sample(sorted_completed_residual,min(2,count))
chooses the sample. Seed, eligible population and draw are persisted once
under compact-selections/<coverage-hash>.json. Recollecting identical
coverage reuses the same selection, preventing accidental rerolls. The
coverage binds source manifest, exact completed degrees and original run
identities/summaries. A partial run is explicitly partial.

Both sampled case directories/workdirs are included in full. Actual reads
of validate_attempt plus the sampled run's provenance closure determine
additional required external preserved-sha256 objects. Frozen package
files are obtained from the separately trusted released package rather
than retransmitted. Every unknown required payload must be included.
Ordinary tar.gz uses included internal hardlinks for duplicate byte content;
there is no custom content decoder or reconstruction format. A plain
COMPACT.json inventory lists paths, sizes and hashes. No witness truncation
or arbitrary splitting to evade Git limits occurs. The producer prints
actual archive size;25MB is a preference, not a success assertion.

verify_compact.py uses separately trusted local code, never archive code.
It authenticates every bundled payload and frozen-source identity,
reconstructs every essential proof with the unchanged rational checker,
checks returned accounting/exits and primary/fresh identity, reproduces
the recorded random draw, and validates full raw closure for the samples.
It explicitly does NOT claim independent unsampled raw review. Distinct
native reruns of the two selected degrees are a separate root/reviewer
action. A compact return is not automatically theorem adoption.

All remaining raw histories stay on Syvert. No full cold-storage transfer
or mandatory unsampled cold retention is claimed. Source/dependency pins,
engine commands, deterministic degree scope, sample seed and validation
hashes preserve regeneration documentation. Optional collect_full retains
the old full-history archive command; default delivery is compact only.

## Review and data-only checks

Exact CANDIDATE source review precedes imports, fixture controls or builds.
Preregistered local data-only exercise uses a COPY of actual known41/511
p02 histories. Never hardlink mutable fixture data to originals. The
storage API accepts an explicit registered_root only for relocating saved
absolute identities into the copy without rewriting evidence JSON; it
must never touch original paths. Fixture sampling may explicitly substitute
known41/511 for the residual population to exercise both full-history
closures; label it a fixture, not a residual sample or new finite result.
Measure inode uniqueness/physical bytes before and after, validate all
original proof bytes, export, verify returned sample closure and report
actual tar.gz bytes. No new native call is needed for this fixture.
