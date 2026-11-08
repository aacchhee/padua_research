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
fields for AC's DOI. The reviewed source snapshot is prepared below. Completed I25
source/runtime/evidence identities and known original/new
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
| onset512-return-20261108.zip | Canonical local provenance return, 81,602,992 B: all 191 pairs / 382 certificates for 320..510, small histories and sampled full native closures (475, 458). Locally rehashed; distinct finite-result/archive review accepted at the recorded native-evaluator scope. |
| onset512-certificates-20261108.zip | 945,235-byte derivative: exactly 382 immutable certificates, inventory and brief README. Locally rehashed; complete provenance is in the canonical 81.6 MB return. |
| onset512-essential-inventory.json | 75,479-byte mirror inventory, included off Git/deposit only; hash/bytes recorded here and in the small custody index. No bulk inventory copy added to Git. |
| padua-manuscript-20261108-131012-Oslo.pdf | Final51-page accepted journal PDF,733598 B; exact identity below. |
| padua-companion-20261108-131012-Oslo.pdf | Final147-page accepted companion PDF,1171187 B; exact identity below. |
| padua-research-source-a433c7d-20261108.zip | Complete tracked repository snapshot at a433c7d:22,105,198bytes, all6,900 file names/sizes and ZIP CRCs checked. It includes final manuscript source24a98db, checker/proof sources and reviews; the original runtime package is separately retained. |
| i25-evidence-20261108T112304Z.zip | 2,843,611-byte completed I25 evidence: all 942 proof inputs, executed full/pilot sources, runtime identities, preregistrations/amendments, logs, receipts and controls, including failed v1 and independent six-certificate replay. Locally rehashed. |
| onset512-independent-review-20261108.zip | Separate 51,749-byte supplementary review evidence package. Locally rehashed; not the canonical native return or the I25 full evidence ZIP. |
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
| I25 sources/runtime/completed evidence ZIP | 2,843,611 | d1d03156dde4248fecaa25d0144cd73c7c5414f28b66a39099342b31f2f7e0f8 |
| Separate supplementary review ZIP | 51,749 | 96f84b294b724b74bc33c112a2633bde14fed5c9220cb11196c60dae5c12ab28 |
| Final journal PDF | 733,598 | 1346fc2891e2cdd5deb6db4b1a5928a2a7bac05c1838999b1a1dee1fc0db1d2c |
| Final companion PDF | 1,171,187 | 83ca42c8052ccd760c3929ff0c30cd1667971476ae111736fe371b30e4581af2 |

The manifest lists all six exact Debian amd64 package identities: FLINT
3.1.3-2 (libflint-dev/libflint19), MPFR 4.2.2-1 (libmpfr-dev/libmpfr6), GMP
2:6.3.0+dfsg-3 (libgmp-dev/libgmp10). Original download/snapshot locators and
individual extracted arithmetic-file pins remain in asset_provenance.json.
The original manifest pins 250 operational/scientific/runtime files; it does
not imply that the host compiler, glibc or Python were identical everywhere.
The local onset preregistration records its own Python and runtime identities.
Do not overwrite those historical runtime distinctions.

## Verification commands

The small I25 bundle contains every phase witness. A [data-only recheck
recipe](RECHECK-SMALL-BUNDLE.md) uses its JSON inputs with the separately
trusted checker source, without the native-history archives. Git-based
manuscript preservation checks use a clone containing the cited commits.

The scientific verifier commands below are instructions, **not newly executed
scientific checks for this custody edit**. Preparation read/rehashed existing
files and inspected source; the nonmutating storage-tool smoke recorded below
was actually executed. Use the final reviewed
repository source and a fresh scratch layout. The original package is a trusted
input supplied separately from the return; never execute source found inside
a returned data archive. Keep the deposited original package bytes unchanged.
The reviewed source-tree verifier's invocation against the unchanged original
trusted package, from the repository root, is:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py \
  local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz \
  --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 \
  --manifest-sha 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16 \
  --expect-plan all
```

Recreate that layout by placing `original-compact-return.tar.gz` at the return
path and unpacking the trusted `original-padua30.zip` as the indicated padua30
directory. Confirm hashes before verification. Record the final checker source
commit/hash separately: the original run used its historical released checker,
and operational fixes must receive their own review. Inspect the reported
coverage list, not merely PASS: exactly integers 41..319 and control 511, all
280 pairs and 560 proofs. The reviewed `--expect-plan all` enforces that exact population. The focused
E-01–E-04 review actually reran this command and all 30 corruption/behavior
controls; see [the verifier record](../compact-verifier-audit03-response.md).

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
The label is historical program wording: the separate
[finite-result/archive review](../independent-checks-onset512-response.md) is now
accepted. Do not infer a pending current result from that unchanged label.

Independent I25 source is under `code/independent_phase_checker/`. The
[completed summary](../code/independent_phase_checker/independent-phase-summary.md),
[RESULTS.json](../code/independent_phase_checker/RESULTS.json) and
[J03](../theory/J03-independent-phase-checker.md) record **942 accepted complete
trees for all 471 degrees 41..511**, both passes per degree. All four workers
exited 0 and passed 31 arithmetic controls each; inclusive CPU was
2519.420775278 s and wall time 646.839168173 s. Distinct review independently
executed six certificates, both passes at 41,458,511, plus 31 controls, exit 0.
The reviewed pilot rejected all 27 corruptions. Failed v1 is retained with the
prospective seam-alias correction and successful v2; old `pending`, `gated` and
`prospective` strings describe their original preregistration boundaries.

The completed full run's historical exact command was:

```sh
timeout --signal=TERM --kill-after=5s 7350s env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/independent_phase_checker/launch_full.py local-output/argmax-bridge-20261105/i25-full-v1-20261108T110409Z
```

That occupied output directory is preserved history, not an instruction to
rerun or overwrite it. Any new consequential replay needs a fresh output path
and prospective reviewed resource accounting. FULL-PREREGISTRATION.json and
FULL-AMENDMENT-01.json preserve the exact input/source pins and clarify that
total 10800 CPU-s is measured campaign acceptance, not a kernel aggregate cap.
The compact I25 ZIP packages exact executed sources, all 942 proof inputs,
runtime identities and completed per-worker input/observation/control/summary
records, outer accounting, pilot failures and independent review. Its internal
MANIFEST.json records member byte sizes/SHA256; CRC and member verification
passed during export. No native histories or binaries are included. The
separate review ZIP remains independently identified above.

I25 proves complete trees using substituted independent bounds under the
explicit Python/Fraction, guarded NumPy and IEEE binary64 model and J03's
analytic premises. It is not universal validation of stored native endpoints;
`all_native_endpoints_validated` remains false. Analytic floor, folding, corner,
far and physical-cover lemmas remain premises. Independent Claude audit and
public deposit remain pending. Candidate paired TeX/Bib source freeze is
`24a98db4c3c4c4d0eede2e3929532956df87911b`; it is the accepted final manuscript baseline,
not the future reviewed repository source ZIP or its unknown hash.

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
`dcb27db7d159ca0eac66e5fb48623589035a31ef` is the current custody-index
preparation head, distinct from the final 24a manuscript freeze and all original
production/scientific pins. It is not a delivery receipt or a claim that it
generated every artifact. The original return, canonical new ZIP,
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
still awaits AC's deposit and independent retrieval. The I25 source/runtime/full-result package identities are now populated above;
the final reviewed repository source ZIP, AC DOI and external custody remain pending.

## Final manuscript acceptance — 2026-11-08

Final paired TeX/Bib freeze is `24a98db4c3c4c4d0eede2e3929532956df87911b`.
The current 51/147-page PDFs listed above were built by root, with all 116
built numbers matching and original48/162-page hashes preserved.
[Sol max review](../manuscript-onset512-solmax-review.md) accepts correctness
and exposition; report SHA-256
`fe935ea03a245dd6301370cc02b4ac826cacec55d036b8c99942a4d00d44dff9`.
Its acceptance does not supply the still-unpackaged final reviewed SOURCE ZIP,
its unknown identity, AC’s DOI/publication or completed external custody.


## Prepared source snapshot — 2026-11-08

The complete tracked repository source is now prepared at commit
`a433c7dfc61d1ed61799a7d919beb8334a2593b6`, including the final TeX/Bib
freeze24a98db, adopted correspondence checker, reviews and reproduction code.
File: `local-output/argmax-bridge-20261105/padua-research-source-a433c7d-20261108.zip`.
Bytes: **22,105,198**. SHA-256:
`66acbadb34ba51a5a2c99bd34a681deef6de433da193202830d00c0aa0f4cc03`.

Generating command, executed once with observed exit0:

```sh
git archive --format=zip --prefix=padua_research-a433c7d/ --output=local-output/argmax-bridge-20261105/padua-research-source-a433c7d-20261108.zip a433c7dfc61d1ed61799a7d919beb8334a2593b6
```

Readback passed every ZIP member CRC, the exact6,900-file Git-tree name/size
inventory and direct Git-byte comparisons of six critical checker, manuscript,
proof and scientific-freeze files. The local `.receipt.json` gives the check
scope. The snapshot contains the tracked source tree; Git history, PDFs,
I25/native data returns and runtime package are separately listed inputs.
Use the adjacent current deposit inventory for this ZIP's identity: the
inventory inside its older source tree necessarily precedes packaging itself.
All15 listed deposit payloads now exist locally. DOI/publication and durable
external retrieval remain AC's tasks.
