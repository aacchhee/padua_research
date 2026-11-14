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
fields for AC's DOI. The historical source snapshot is recorded below. Completed I25
source/runtime/evidence identities and known original/new
return identities are filled. It must be completed and saved as the final MANIFEST.json after the
current audit repairs, focused reviews and final source packaging are complete. A placeholder filename has no
verified identity. The original and new file identities were read back and SHA-256
checked locally on 2026-11-08; this does not establish an AC Windows copy or
Zenodo retrieval.

## Current access and historical scope — 2026-11-13

All 2026-11-08 packaging, rehash, local availability and acceptance statements
below are historical records. AC subsequently supplied the original return
and padua30 runtime package; both were authenticated, and root plus a distinct
reviewer reran the repaired compact verifier on all 280 original pairs.
The canonical onset-512 return and I25 bundle remain unavailable. No repaired
canonical onset-512 reader run, upload, delivery or durable retrieval is claimed.
See [the execution record](../reader-repair-execution-20261113.md). Audit-04 remains the source of the outstanding evidence checks.
The a433c7d ZIP is a prepared historical snapshot; it predates audit-04 repairs
and is not a final reviewed source snapshot for the repaired code. A new source
snapshot and inventory must be created after the repair review; preserve the
old snapshot's identity and provenance.

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
| padua-manuscript-20261108-131012-Oslo.pdf | Historical 51-page journal PDF,733598 B; exact identity below. |
| padua-companion-20261108-131012-Oslo.pdf | Historical 147-page companion PDF,1171187 B; exact identity below. |
| padua-research-source-a433c7d-20261108.zip | Complete tracked repository snapshot at a433c7d:22,105,198bytes, all6,900 file names/sizes and ZIP CRCs checked. It includes historical manuscript source24a98db, checker/proof sources and reviews; the original runtime package is separately retained. |
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

## Recorded original and new identities — 2026-11-08

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

The unchanged `original-padua30.zip` contains the **unrepaired historical**
`verify_compact.py`, SHA-256
`7c2dad53519aff616bdadd3f925ec8943963cb4bf521b410355f827b7a1899bf`.
Audit-04 demonstrated acceptance of altered attempt status, summary receipt
path and trusted-source shadowing (H1–H3). Preserve that original package for
provenance and invoke the separately trusted reviewed source-tree verifier.
The audit-03 repaired verifier included in the a433c7d snapshot has SHA-256
`5867ac0c6d6e1d380d72c118262177a10b617631e039da11f489e45c93ff61b6`;
it passed the audit-04 review at that historical identity. Further E4-04
repairs have a new identity and require their own focused review; the old
snapshot does not include them. Never attribute a repair to the original run.


The current audit-05-response repair sources have these SHA-256 identities:

| Source | SHA-256 |
|---|---|
| `return_bundle.py` | `3f903e62b5c155e85603be43a60724c226b800dd9908685146fd7c5b69c2c234` |
| `verify_compact.py` | `2d26886fa38089815712edcceccd4ac893fea9d8e6092afbd4c0faac7b569cef` |
| `runner.py` | `a198b65182590be13cb91110ff976d90e7e885c778180e59699fbe9b067ccdad` |
| `onset512_analytic/check.py` | `5ce8cc0701ed105fa619674993583f749046709cb02d233570e2dedc59ca1d2d` |
| `independent_phase_checker/runtime_probe.py` | `9f1c503e5c0b0739c1e4d85a5f2b920cc515f0d55f2c3039b66ce59278fd1751` |

These identities describe the current source repair, not the historical
executions or the a433c7d source ZIP. The distinct supplementary reader
review accepts the repaired code within its stated scope; the actual pinned
onset-512 canonical archive rerun remains blocked by its missing ZIP.
The reader defaults to canonical archive SHA-256 `da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e`
and independently pins runtime manifest SHA-256
`5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16`.
It reports verified counts and its own source identity. The compact verifier
reports `expect_plan` and `coverage_mode`; use `--expect-plan all` for the
complete original plan. The historical preregistration's runner identity is
preserved separately; the repaired runner is not attributed to that campaign.

## Verification commands

The small I25 bundle contains every phase witness. A [data-only recheck
recipe](RECHECK-SMALL-BUNDLE.md) uses its JSON inputs with the separately
trusted checker source, without the native-history archives. Git-based
manuscript preservation checks use a clone containing the cited commits.

The scientific verifier commands below are instructions, **not newly executed
scientific checks for this 2026-11-13 edit**. The 2026-11-08 preparation recorded
readback of existing files and a nonmutating storage-tool smoke, as described
below. Those historical actions were not repeated in this fresh workspace. Use the final reviewed
repository source and a fresh scratch layout. The original package is a trusted
input supplied separately from the return; never execute source found inside
a returned data archive. Keep the deposited original package bytes unchanged.
The source-tree verifier's prospective invocation against the unchanged original
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

The prospective repaired local onset ZIP verifier uses:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/return_bundle.py \
  verify local-output/argmax-bridge-20261105/onset512-return-20261108.zip
```

This is the actual canonical archive path. Verification requires
the trusted release and runtime files at the repository-relative layout pinned
by the machine preregistration; the package metadata alone is insufficient if
the extracted arithmetic tree is absent. Its runner fixes the trusted package
at `local-output/argmax-bridge-20261105/compact-release-aea62883/padua30` and checks
the extracted arithmetic paths from asset_provenance.json. Deposit the final
reviewed setup instructions for that exact layout with the source snapshot.
The historical verifier's success label was `accepted_pending_independent_review`,
191 pairs/382 proofs; that label does not constitute distinct audit acceptance.
The label is historical program wording: the separate
[finite-result/archive review](../independent-checks-onset512-response.md)
recorded acceptance on 2026-11-08. Audit-04 subsequently required the repaired
reader review and canonical rerun; the historical label resolves neither.

Independent I25 source is under `code/independent_phase_checker/`. The
[completed summary](../code/independent_phase_checker/independent-phase-summary.md),
[RESULTS.json](../code/independent_phase_checker/RESULTS.json) and
[J03](../theory/J03-independent-phase-checker.md) record **471 distinct complete trees for degrees 41..511**, each recorded twice
in 942 separately checked witnesses. All four workers
reported stdlib returncode 0 and passed 31 arithmetic controls each;
942 accepted rows over the exact union establish completeness. The historical
launcher did not independently authenticate waitpid exit status (E4-05); inclusive CPU was
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
public deposit remain pending. The historical paired TeX/Bib source freeze was
`24a98db4c3c4c4d0eede2e3929532956df87911b`; it was the then-accepted manuscript baseline,
distinct from the prepared a433c7d historical source ZIP and from the future
post-repair source snapshot.

For final deposit integrity, from the directory containing completed MANIFEST.json:

```sh
python3 -E - <<'PY'
import hashlib, json, sys
from pathlib import Path
def need(condition, message):
    if not condition:
        raise ValueError(message)
need(sys.flags.optimize == 0, 'optimized Python is unsupported')
m = json.loads(Path('MANIFEST.json').read_text())
need(m['status'] == 'COMPLETE_DEPOSIT_FILE_INVENTORY', 'incomplete deposit inventory')
for row in m['files']:
    need(row['bytes'] is not None and row['sha256'] is not None, 'missing file identity')
    path = Path(row['deposit_filename'])
    need(path.is_file(), f'missing file: {path}')
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    need(path.stat().st_size == row['bytes'] and h.hexdigest() == row['sha256'], f'file identity: {path}')
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
the a433c7d source ZIP was subsequently packaged as recorded below; a new
post-repair reviewed source snapshot, AC DOI and external custody remain pending.

## Final manuscript acceptance — 2026-11-08

Final paired TeX/Bib freeze is `24a98db4c3c4c4d0eede2e3929532956df87911b`.
The current 51/147-page PDFs listed above were built by root, with all 116
built numbers matching and original48/162-page hashes preserved.
[Sol max review](../manuscript-onset512-solmax-review.md) accepts correctness
and exposition; report SHA-256
`fe935ea03a245dd6301370cc02b4ac826cacec55d036b8c99942a4d00d44dff9`.
This historical review predates audit-04 findings. The a433c7d source ZIP was
subsequently packaged as recorded below; post-repair review/source packaging,
AC’s DOI/publication and completed external custody remain pending.


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
All 15 listed deposit payloads were reported locally present on 2026-11-08;
that statement does not establish availability in the 2026-11-13 workspace. DOI/publication and durable
external retrieval remain AC's tasks.


## Generated-output bound convention — 2026-11-13

Use the audit-03 convention: sum all positive generated-output deltas and give
no deletion or shrink credit. Audit-04 E4-07 gives **9,917,613 B before merging current main and this repair batch**. The former
9,897,953 B value credited the cold-storage.json shrink and is not the chosen
bound. The orchestrator must add any chargeable positive deltas from this batch;
this baseline does not claim a final post-edit bound. Merging current main
adds 1,827,288 counted bytes from the already-published Padua3D topic, so
the inherited bound becomes 11,744,901 B before this batch's positive deltas.
The current global total exceeds 10,000,000 B; unrelated evidence is preserved.
The topic LOG records this limitation; no budget/readiness acceptance is claimed.


### Final response accounting and revision record

The active paired source freeze is `ad908acb21d3589d85635618ff68f63dd01cfbca`;
current PDFs have 57/150 pages. Their BUILD records give fresh off-Git paths
and hashes. Historical inventory rows still identify the earlier prepared
51/147-page PDFs; they are not silently relabelled as current artifacts. A
post-Claude source/deposit update remains pending.

The audited conservative classification gives an actual current counted sum
of 11,729,562 bytes and a no-shrink-credit bound of 11,751,309 bytes. The latter
includes the historical 9,917,613 baseline and 1,833,696 positive bytes since the
old topic head, of which 1,827,288 came from current main's Padua3D topic.
This exceeds the inherited 10,000,000 byte cap. No other topic's evidence is
deleted or reclassified here; global budget repair and readiness remain open.

## Dated note — 2026-11-13 (Claude audit-05 MINOR fix E5-08)

The onset-512 verify command in this README fails on the canonical archive until audit-05 finding E5-01 (member allowlist omits `storage-dedup.json`
and `.preserve.lock`) is fixed and re-reviewed. The source freeze `24a98db4c3c4c4d0eede2e3929532956df87911b` named above is historical; it is
superseded by the final paired freeze `ad908acb21d3589d85635618ff68f63dd01cfbca`. See [audit-05](../audit-05.md).


## Audit-05 response: current verification interface

E5-01 is repaired in the current reader: an empty .preserve.lock and
producer-schema storage-dedup.json receipts are accepted and checked. A
real storage→completion→export→reader synthetic round-trip passes, with
explicit trust/arithmetic/closure adapters. Independent malformed receipt
and lock controls pass. This resolves the specific producer-file mismatch;
it is not a run on the unavailable canonical onset512 ZIP. Earlier dated
notes saying the command fails until E5-01 is fixed describe the older code.

Historical runner 459d0728 performed the campaign. Current runner a198b651
has performed no campaign and cannot continue the old runner identity.
The reader is deliberately scoped to the one recorded 320..510 campaign;
a future campaign requires new reviewed identities and constants.

For exact analytic reruns use the separately trusted source:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/onset512_analytic/check.py
```

The current checker refuses optimization before its verdict and explicitly
asserts log(pi)>11/10. Its normal receipt values are unchanged. Historical
commands and preregistrations remain historical, not current rerun recipes.
The revised runtime probe compares actual uint64 encodings and rejects
tested FTZ|DAZ/FTZ division behavior; it is a finite prospective probe, not
a proof of universal IEEE behavior or a historical worker's mode.

Budget attribution at the audit input: main alone 9,733,758 bytes; this
topic's own classified share 1,995,804 bytes; union 11,729,562 bytes. Adding
the topic's 2,087 byte FREEZE.md exception gives 11,731,649 bytes. The prior
conservative bound 11,751,309 already includes that exception. Neither
original branch alone exceeded 10 MB; the union does. Current growth is
recorded separately in the manifest/LOG. Nothing from another topic is
removed or relabelled; AC's budget disposition remains open.

## Dated note — 2026-11-13 (Claude audit-06 MINOR fix E6-01)

The active paired TeX/Bib freeze is `8937d3b723c09c004f49d3e565d0b02976713a37` (58/152-page PDFs; see the BUILD.md files and MANIFEST.json.in); the earlier
statements above that name `ad908acb21d3589d85635618ff68f63dd01cfbca` with 57/150-page PDFs, and call it final, describe the previous round and are historical.
See [audit-06](../audit-06.md).


## AC-directed paper-evidence regeneration — 2026-11-14

AC requires replacement of every missing paper-dependent input/output and
permits historical-only artifacts to be forgotten. The missing historical
onset512/I25 archive identities and old PDF bytes are therefore no longer
reproduction targets. New native and independent executions have separate
preregistrations and frozen inputs; see [regeneration-20261114.md](../regeneration-20261114.md)
for their current outcome and the complete delivery record. The dated
statements above describe earlier checkpoints and do not certify the new
run. No permanent storage, external retrieval or DOI is asserted here.
