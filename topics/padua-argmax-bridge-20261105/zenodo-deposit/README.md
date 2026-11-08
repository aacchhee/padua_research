# Zenodo deposit preparation — 2026-11-08

This is a **draft file list and verification plan**, implementing AC decision 4
in [handoff 29](../handoffs/29-onset512-and-manuscript-revision.md). It is not a
deposit, delivery receipt or proof of durable external custody. AC reserves the
DOI and publishes after the final certificates exist. DOI: **PENDING AC**.
No upload, DOI creation or external contact was performed for this preparation.
Rules/input: `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`; requested Codex technical
development, serving model/effort metadata unexposed. This adds no research or
novelty claim and requires no novelty search.

[MANIFEST.json.in](MANIFEST.json.in) is valid JSON with explicit null/PENDING
fields for final reviewed source/I25 artifacts and DOI. Known original/new
return identities are filled. It must be completed and saved as the final MANIFEST.json after the
missing files, source freeze and reviews exist. A placeholder filename has no
verified identity. The original and new file identities were read back and SHA-256
checked locally on 2026-11-08; this does not establish an AC Windows copy or
Zenodo retrieval.

## Files to deposit

| Deposit filename / group | Content and current state |
|---|---|
| original-compact-return.tar.gz | Existing 36,045,486-byte original return; 280 primary/fresh pairs, exactly 41..319 plus 511, hence 560 essential certificates. Locally rehashed; identity below. |
| original-padua30.zip | Existing 25,111,335-byte trusted offline package released from source `996fedcad4ba79a28e45a3fe3678adc12f1e5358`. It contains the separately trusted engine, compact checker, source/runtime inventory, headers, libraries and six official package inputs. Locally rehashed. |
| runtime_manifest.json, asset_provenance.json, SOURCE_CUSTODY.json, FREEZE.json | Exact original package/frozen-science metadata, separately listed for inspection. The runtime manifest and asset provenance are bulk deposit files, not new Git evidence. Their copies must match the original package, not newly reconstructed prose. |
| onset512-preregistration.json | Existing 49,782-byte machine preregistration, source/runtime pins and 191-degree population. Locally rehashed; included alongside the authored preregistration. |
| onset512-return-20261108.zip | Canonical local provenance return, 81,602,992 B: all 191 pairs / 382 certificates for 320..510, small histories and sampled full native closures (475, 458). Locally rehashed; independent result review remains separate. |
| onset512-certificates-20261108.zip | AC-requested 945,235-byte derivative: exactly 382 immutable certificates, inventory and brief README. Locally rehashed; it does not replace the canonical 81.6 MB provenance return. |
| onset512-essential-inventory.json | 75,479-byte mirror inventory, included off Git/deposit only; hash/bytes recorded here and in the small custody index. No bulk inventory copy added to Git. |
| PENDING-reviewed-source.zip | Final reviewed repository snapshot at an exact commit, including all checker/adapter source, mathematical reductions and cited verification records. Include the required paths below; record its eventual bytes/hash and source commit. This is distinct from the immutable original production package. |
| PENDING-I25-source-runtime.zip | Reviewed independent checker source, its soundness record, exact Python/NumPy/environment identification and its actual preregistrations. No final source identity is asserted yet. |
| PENDING-I25-evidence.zip | Actual input inventories, append-only observations, arithmetic and corruption controls, summaries and independent review, for the scopes that really completed. Fill all hashes and counts. Do not replace failed records or silently reuse a pilot output directory. |
| README.md, MANIFEST.json | Completed deposit instructions and exact final file list, with AC's DOI and retrieval date once real. |

The source snapshot must retain `code/final_hybrid_engine/` (including frozen
checker.py, engine.py, FREEZE.json, SPEC/SOURCE), `compact_pack/` (including
verify_compact.py and its imported helpers), `code/local_onset512_campaign/`,
`code/independent_phase_checker/`, `code/compact_return_replay/`,
`preregistration-onset512-local.md`, `evidence/compact-return/`,
`audit-03/replay276.md`, and completed independent-review records. Paths in this
paragraph are relative to the topic root. Also retain original package launchers,
plans, runtime_manifest.json, asset_provenance.json and SOURCE_CUSTODY.json.
Freeze and hash the final reviewed checker sources, including operational fixes;
do not treat a new verifier as the verifier used in an old run without saying so.

All essential certificates are in the compact returns. Full native histories
are included only for their recorded random samples; unsampled raw histories
remain at the original execution location under AC's retention direction.
This file makes no all-history deposit claim. The original return sampled
199 and 238. The new canonical return sampled 475 and 458 using persisted seed
`cb52b5324c8fa5bca69665affe22016950ca48661a429a3fa4b6e4a77bfadcdb`.
The [completed finite campaign summary](../local-onset512-summary.md) records
quiescence, sampling, archive generation and developer/portable verification.
This local rehash is an identity check, not a new mathematical/result audit.

## Verified original and new identities

| File | Bytes | SHA-256 |
|---|---:|---|
| Original return | 36,045,486 | b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a |
| Original offline ZIP | 25,111,335 | aac08e5f25bd27b2710de22039efd229b4ee67d8c1e3ffef9456af200e1f74d2 |
| runtime_manifest.json | 54,003 | 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16 |
| asset_provenance.json | 42,623 | 71ee5c717288f12527698e76ed17560805dd1641488e021cfe70a91ec4924a41 |
| SOURCE_CUSTODY.json | 1,655 | c9051f1910898e8af6aa895a66f8d416456b7616c5886e8936409008bfa2f31e |
| Scientific FREEZE.json | 4,153 | 0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb |
| Onset-512 machine preregistration | 49,782 | 532e5af6af478d48546b4134635c296cd0aac5207de4df2955dda8b0fb7781a3 |
| Canonical onset-512 provenance ZIP | 81,602,992 | da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e |
| Onset-512 certificate-only derivative ZIP | 945,235 | c22d600cb67462918587b01f2ef5adcbf9030b825fb0f2cc79c1b9c27c7da8c8 |
| Onset-512 mirror inventory (off Git) | 75,479 | d7cea34dd64d9df329d1398c2418fbf984a9084b135cad695866a9c437551740 |

The manifest lists all six exact Debian amd64 package identities: FLINT
3.1.3-2 (libflint-dev/libflint19), MPFR 4.2.2-1 (libmpfr-dev/libmpfr6), GMP
2:6.3.0+dfsg-3 (libgmp-dev/libgmp10). Original download/snapshot locators and
individual extracted arithmetic-file pins remain in asset_provenance.json.
The original manifest pins 250 operational/scientific/runtime files; it does
not imply that the host compiler, glibc or Python were identical everywhere.
The local onset preregistration records its own Python and runtime identities.
Do not overwrite those historical runtime distinctions.

## Verification commands

The scientific verifier commands below are instructions, **not newly executed
scientific checks for this custody edit**. Preparation read/rehashed existing
files and inspected source; the nonmutating storage-tool smoke recorded below
was actually executed. Use the final reviewed
repository source and a fresh scratch layout. The original package is a trusted
input supplied separately from the return; never execute source found inside
a returned data archive. Keep the deposited original package bytes unchanged.
The original checker's recorded invocation, from the repository root, is:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py \
  local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz \
  --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 \
  --manifest-sha 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16
```

Recreate that layout by placing `original-compact-return.tar.gz` at the return
path and unpacking the trusted `original-padua30.zip` as the indicated padua30
directory. Confirm hashes before verification. Record the final checker source
commit/hash separately: the original run used its historical released checker,
and operational fixes must receive their own review. Inspect the reported
coverage list, not merely PASS: exactly integers 41..319 and control 511, all
280 pairs and 560 proofs. The newer verifier's expected-plan option, if adopted,
needs its final reviewed command added here; no such option is assumed above.

The local onset ZIP verifier currently has this interface, inspected in source:

```sh
python3 -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/return_bundle.py \
  verify local-output/argmax-bridge-20261105/onset512-return-20261108.zip
```

This is the actual canonical archive path. Verification requires
the trusted release and runtime files at the repository-relative layout pinned
by the machine preregistration; the package metadata alone is insufficient if
the extracted arithmetic tree is absent. Its runner fixes the trusted package
at `local-output/argmax-bridge-20261105/compact-release-aea62883/padua30` and checks
the extracted arithmetic paths from asset_provenance.json. Deposit the final
reviewed setup instructions for that exact layout with the source snapshot.
The inspected verifier's success label is `accepted_pending_independent_review`,
191 pairs/382 proofs; that label does not constitute distinct audit acceptance.
Record the actual output and the separate review before completing this plan.

Independent I25 source is under `code/independent_phase_checker/`. Its inspected
pilot command is pinned prospectively in
`code/independent_phase_checker/PILOT-PREREGISTRATION.json`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/independent_phase_checker/run.py \
  --archive local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz \
  --degrees 41,199,238,511 --controls --cpu-limit 3500 \
  --output local-output/argmax-bridge-20261105/i25-pilot-v1-20261108T105100Z
```

Its soundness record is `theory/J03-independent-phase-checker.md`, currently
CONDITIONAL with distinct review/pilot pending. The output path above must be
fresh; once occupied it identifies the original run, not permission to overwrite
or silently rerun it. This is a computational run requiring reviewed soundness,
preregistration and environment; it was not executed by this preparer. The
source uses Python, NumPy binary64 arithmetic/nextafter and exact Fraction
checks, and imports its trusted sibling check/controls modules. The eventual
full-run command and additional 320..510 input adapter must be copied from the
checker developer's actual preregistration after final review. An inspected
`--additional-dir` flag alone does not prove exact 382-proof inventory. Include
inputs.json, observations.jsonl, controls.json and summary.json from each
actually completed output. A substituted-bound recertification is not a check
that every historical native outward endpoint was tight or independently
validated; preserve the recorded `all_native_endpoints_validated` limitation.

For final deposit integrity, from the directory containing completed MANIFEST.json:

```sh
python3 - <<'PY'
import hashlib, json
from pathlib import Path
m = json.loads(Path('MANIFEST.json').read_text())
assert m['status'] == 'COMPLETE_DEPOSIT_FILE_INVENTORY'
for row in m['files']:
    assert row['bytes'] is not None and row['sha256'] is not None
    path = Path(row['deposit_filename'])
    assert path.is_file()
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    assert path.stat().st_size == row['bytes'] and h.hexdigest() == row['sha256'], path
print('all listed deposit files match their recorded identities')
PY
```

This checks listed payload bytes, not mathematics or remote delivery. AC must
also download the deposited files and run the same integrity check against the
final inventory, recording the actual DOI/version URL and retrieval result.
Resolve license/author/funding metadata with AC without modifying the existing
AI declaration, ORCID or contribution text.

## E-10: small custody index applied — 2026-11-08

The [active cold-storage.json](../cold-storage.json) is now a small compatible
pending-local index. Its `entries` remains empty; it claims no physical delivery,
Zenodo upload or durable external retrieval. Source identity
`f77b6683d7601b68bae9793d7213683682bc7ecc` is the real existing commit against
which this edit was prepared, not a future publication commit or an assertion
that it generated every artifact. The original return, canonical new ZIP,
certificate-only derivative and off-Git mirror inventory were rehashed here.

The entire prior 23,904-byte manifest remains unchanged in published input
commit `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`, blob
`96aaf1885dcb2bf1c480e102af8b5ba0ec8ff1f4`, SHA-256
`3a8867bee698f32bf10324df0c0af8bf3d32d9192f6bcc6f48ac95de8ac2460e`.
The new index pins that full historical manifest, including 70 file rows and
all group generation/checking/failed-record custody notes. It does not split
the old inventory across new files. Old local artifacts are not pruned and
are not promoted to delivered evidence.

Recover the historical inventory into a fresh off-Git path with:

```sh
git show b45e29fa1fe3dbfa2517ff8043e5d9c440870530:topics/padua-argmax-bridge-20261105/cold-storage.json > /tmp/padua-bridge-historical-cold-storage.json
sha256sum /tmp/padua-bridge-historical-cold-storage.json
```

Expected identity is the historical pin above. Fetch that published commit if
absent. This recovers the inventory only, not its ephemeral payload files.
[COLD_STORAGE.md](../COLD_STORAGE.md) retains all historical narrative plus a
dated source/index pointer. A nonmutating tool compatibility smoke is:

```sh
python3 -B tools/cold_storage.py verify padua-argmax-bridge-20261105
```

Executed here with observed exit 0: `accepted: true`, `entries: 0`, `bytes: 0`,
no problems and no restored copies. With empty delivered entries this checks
manifest/source compatibility only;
it does not authenticate pending-local payloads or external delivery. Those
four payload identities were checked separately by streamed SHA-256 readback.
The full 75,479-byte mirror inventory remains off Git. E-10's per-file size
issue is repaired by this index; P-01/G-8's actual durable data-access obligation
still awaits AC's deposit and independent retrieval. The I25 final source and
full-result file identities remain explicit placeholders until actually ready.
