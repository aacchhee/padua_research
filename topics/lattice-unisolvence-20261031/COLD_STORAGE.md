# Cold-storage manifest — lattice-unisolvence-20261031

AC's chosen destination: `C:\Users\andreyac\Downloads\padua\cold_storage\lattice-unisolvence-20261031\`.

The archive below is actually staged in the cloud workspace. The original ZIP was not delivered to Windows. For F5 the developer accepts the auditor-delivered, hash-verified retrieval copy below as the archival representation of the audited head; it is a different ZIP, with an explicit audit receipt. The parent charter waiver is not used as a receipt. All essential small scientific code/evidence is also committed, so this storage item does not leave a computer-proof dependency unavailable.

| File | Actual staging path | Bytes | SHA-256 | Source / generating command | Checker |
|---|---|---:|---|---|---|
| lattice-evidence.zip | `/workspace/scratch/lattice-unisolvence-20261031/lattice-evidence.zip` | 832029 | `7b173b14f12eb73661e165e544f189a42faa13c08d94e957126a08eb7b7ba53a` | Source-head `61dcbe5e5a9a020810c0b8a9be974e1eba98f0ca` plus exact per-file hashes/Git blobs in the enclosed scientific audit-targets.json; `python tracks/lattice-unisolvence/code/prepare_evidence.py --archive /workspace/scratch/lattice-unisolvence-20261031/lattice-evidence.zip` | ZIP CRC and extracted identities PASS in cold-check.json |

## Committed output and identities

[audit-targets.json](COLD_STORAGE.md) records every retained source/evidence file's SHA-256, bytes and Git blob identifier. Its self-exclusion and bookkeeping exclusions avoid a recursive hash dependency; exact recorded file bytes, not an assumption that every working file already existed at source_head, govern review. [manifest-check.json](manifest-check.json) records the executed content check; [cold-manifest.json](cold-manifest.json) identifies the staged ZIP. The archive contains its own scientific snapshot manifest, allowing verification after extraction. The final repository manifest may additionally pin the later protocol-review and parent-integration metadata envelope; the scientific identities agree. Protocol review remains committed separately and is excluded from the scientific ZIP to keep the dependency one-way. No third-party fulltext is included.

## Regeneration and retrieval

From the repository root, regenerate the bundle using the command above. ZIP metadata may vary on regeneration; compare extracted file identities, not an assumed byte-identical future ZIP. Retrieve the existing staged ZIP through the workspace file link or copy it to AC's selected Windows folder. Extract into a fresh directory, then run `python tracks/lattice-unisolvence/code/verify_artifacts.py topics/lattice-unisolvence-20261031/audit-targets.json --root <extracted-root>` from the extracted root. SHA-256 of the downloaded ZIP must first equal the manifest value. Verification needs ordinary Python3 only; no secret, external account or network access. No Windows execution is claimed.

The scientific computations are reproducible from committed checkers; exact Python/NumPy/SciPy/SymPy versions and commands appear in the direction evidence and AUDIT_HANDOFF.md. The present archive is a compact review/retrieval bundle, not a claim to be a complete Git checkout.

## Retention

AC is the permanent archive custodian once transferred to the chosen folder. The cloud path is temporary session staging with no promised long-term retention. No archival deletion was performed. The original ZIP receipt remains unconfirmed, while the distinct auditor-delivered retrieval copy below is accepted for F5. Neither archival representation implies whole-batch merge readiness.

## Accepted retrieval-copy receipt — audit-01 F5, 2026-11-01

Claude audit-01, committed at3f369611f364c8bab41b8a48f1414f88b21937ec, reports delivery to `C:\Users\andreyac\Downloads\padua\cold_storage\lattice-unisolvence-20261031\claude-audit-01\lattice-evidence-retrieval-copy-724269a.zip`. It contains169entries:168 audited file identities plus their manifest. Size841824bytes; SHA-256 `8e75432bea5070776bb025030442adc05ba44f5efd8884ba5408fb546eca8330`. The auditor checked file hashes before zipping and after extraction, and delivered its report/scripts/checksums with the copy.

The developer accepts that copy for F5. This is an **auditor-reported delivery and integrity receipt**, not a claim that Codex accessed AC's machine or ran Python on Windows. It is not the832029byte original ZIP, whose separate identity and cloud staging are preserved above. All essential scientific files are committed; current registry/history metadata is in the Git response envelope rather than silently substituted into either historical ZIP. The immutable [audit delivery note](audit-01.md) is the receipt source.

## Repository cleanup 2026-11-02 — large regenerable outputs moved off the branch head

AC (2026-11-02): "I do not think that we have to store large outputs that can be regenerated. Make sure that all needed code is in the repo, some short summaries are stored and expunge the large data files (cold storage)"; "18 mb per repo is too much."

Every generated data file of 16 KiB or more in this directory left the branch head: 25 files, 2,917,679 bytes. Machine manifest: [`cold-storage.json`](cold-storage.json). Tool: `tools/cold_storage.py`.

These files have **not been delivered to AC's Padua cold storage yet** (PENDING). Until then, the only stored copy is Git history, pinned by blob id at the pushed main commit `2b52b432fe59c9a50aef9deebe5152c5d6874465`. Each file's SHA-256 is recorded alongside, so the bytes can be verified.

Code, records, and small receipts and summaries stay. All generators are committed under tracks/lattice-unisolvence/code (c0_catalogue, c1_mod4, c1_stability, c1_extension, c3_rank, c3_structure, c3_obstructions, c3_lebesgue, c3_records, prepare_evidence, verify_artifacts). Producer commands: directions/C0/rounds.md:14, directions/C1/rounds.md:24-32, directions/C3/evidence.md:9-29; independent reruns: independent/commands.md:25-35. Restore before running verify_artifacts.py, protocol/check_protocol.py, independent/reconstruct_*.py, claude-audit/{rect_check,cert_D,cert_D_construct,certs_AB,nine}.py or the C3 pipeline (C3 scripts read C0/catalogue.json and C3/ranks.json). Small committed summaries: C0/count-result.json, C1/symbolic.json, C1/gram.json, C3/lowdegree.json, C3/artifact-manifest.json, independent/*-reconstruction.json and comparison receipts. The earlier lattice-evidence.zip (COLD_STORAGE.md above) remains as recorded.

Files of 16 KiB or more kept on purpose (not generated output):
- `provisional-id-map.json` (19,769 bytes): registry input read by scripts in this and other topics (check-response-01.py, response-review/check_response.py, programme-ideas allocation scripts); hand-authored, not generated output.

| File | Actual storage path | Bytes | SHA-256 | Source commit | Frozen generating command | Script blob IDs | Checker command / result |
|---|---|---|---|---|---|---|---|
| `audit-targets.json` | Git blob `d0488f3157ba` at `2b52b432fe59`; AC cold storage PENDING | 52,772 | `6bb1791c0b53d9962fe5d3f3180847788cfd85466d5ab6eb9404ff88941dd46e` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/prepare_evidence.py (source_head ad40c38f; 204 identities) | committed at source commit | Summary: manifest-check.json (checked 204, no failures); COLD_STORAGE.md 'Committed output and identities'. Generated integrity manifest; read by verify_artifacts.py and protocol/check_protocol.py. |
| `claude-audit/outputs/indep_ranks.json` | Git blob `6e5a7ed8e702` at `2b52b432fe59`; AC cold storage PENDING | 142,972 | `8e1bb0f6f124df9e2ff17299776f37ad3f279c87dcbf09fbb3988635993866a0` | `2b52b432fe59` | python topics/lattice-unisolvence-20261031/claude-audit/indep_c0_c3.py | committed at source commit | Summary: claude-audit/outputs/indep_c0_c3.stdout; audit-01.md:38-40. Auditor independent rank table: 364 reps, 142 full / 222 deficient. |
| `directions/C0/catalogue.json` | Git blob `9f8490412f76` at `2b52b432fe59`; AC cold storage PENDING | 203,368 | `21cd7610051d7f51e8578051da164f73ef112d9081765cea7156b26f01441430` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c0_catalogue.py --output-dir <dir> (stdlib, deterministic) | committed at source commit | Summary: directions/C0/count-result.json; directions/C0/rounds.md:14-33; tracks/lattice-unisolvence/theory/c0-catalogue.md. 5061 canonical rows, 451 admitted (39 d2 + 412 d3); input of the C3 pipeline. |
| `directions/C0/count-trials.json` | Git blob `10fa9a834300` at `2b52b432fe59`; AC cold storage PENDING | 168,359 | `8d9d213e0725e6cc8d32b53fd71ea5220678fcb99dec0e22cd6149b8ca37b0c9` | `2b52b432fe59` | same run as directions/C0/catalogue.json | committed at source commit | Summary: directions/C0/count-result.json; rounds.md:33,42; theory c0-catalogue.md, c0-density.md. 5061 keyed trial rows. |
| `directions/C1/extension.json` | Git blob `618c27ebd6d5` at `2b52b432fe59`; AC cold storage PENDING | 18,244 | `0b7dd941ebd269eef37daa98259e784872af08ceccce6522035b472691c04948` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_extension.py --output <out> | committed at source commit | Summary: theory c1-finite-evidence.md (PD-T089) lines 14-15; directions/C1/extension.md.  |
| `directions/C1/results.json` | Git blob `4bedfa256576` at `2b52b432fe59`; AC cold storage PENDING | 44,013 | `e2576de67528fefae7c04d3f1dfe8f7d0626bb0cd0518a6295d9223bb27d00c9` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c1_mod4.py --output <out> | committed at source commit | Summary: theory c1-finite-evidence.md (PD-T089); c1-counts.md:37; directions/C1/rounds.md. counts n1..8 = 3,6,10,16,21,28,36,46. |
| `directions/C1/stability.json` | Git blob `8ce07103e5d5` at `2b52b432fe59`; AC cold storage PENDING | 29,012 | `35b3ce51f4671be608fe898733987ede2e103ab5740f10d919143be64e5969fb` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_stability.py --output <out> (2 BLAS threads required) | committed at source commit | Summary: theory c1-finite-evidence.md:14; directions/C1/rounds.md; audit-01.md F3. With 1 thread two n=22 rows differ (claude-audit/reruns/compare-1thread.txt). |
| `directions/C3/lebesgue.json` | Git blob `57515e9a3845` at `2b52b432fe59`; AC cold storage PENDING | 69,136 | `ee98828d9fe4b790c02059a60e00bacddcd9bceb835d90706c03cfb03bedb3a0` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c3_lebesgue.py <C3/ranks.json> <C0/catalogue.json> --output <out> | committed at source commit | Summary: theory c3-chebyshev-observations.md (best sampled Lambda table); directions/C3/evidence.md:17.  |
| `directions/C3/obstructions.json` | Git blob `2367f1e1e7cb` at `2b52b432fe59`; AC cold storage PENDING | 139,840 | `d61b0a60f1b99aad93b96514ef78f05f5e1542514d6db7756fbd916a54a76def` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c3_obstructions.py <C3/ranks.json> <C3/structure.json> --output <out> | committed at source commit | Summary: theory c3-deficiency-observations.md:19, c3-rectangle-observations.md:27; directions/C3/evidence.md:21-23.  |
| `directions/C3/pattern-outcomes.tsv` | Git blob `c26c2ce693c8` at `2b52b432fe59`; AC cold storage PENDING | 109,800 | `f3cccddff5e60a12fdb1cad4e51ca8cc6fd237b53dfc626ae6121d97ba645c8b` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c3_records.py | committed at source commit | Summary: theory c3-rank-observations.md:36; directions/C3/evidence.md:31. Derived index of 412 rows; no result depends on it. |
| `directions/C3/ranks.json` | Git blob `5408f15dd297` at `2b52b432fe59`; AC cold storage PENDING | 535,224 | `560471d0053fef785bcee9c64f1b7fe9a384e24c0c74ef3d4cd58b9d6c703130` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c3_rank.py <C0/catalogue.json> --output <out> (about 12 s, deterministic seeds) | committed at source commit | Summary: theory c3-rank-observations.md (PD-T092); directions/C3/evidence.md:9-11; audit-01.md:39. 412 sources -> 364 reps, 2184 modular matrices; main C3 input. |
| `directions/C3/structure.json` | Git blob `68f47e579a4a` at `2b52b432fe59`; AC cold storage PENDING | 39,828 | `d5c34e03d7c62a0f0f63470a742ff1e6b26f4dd774bb1c916e6ebee1416144be` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c3_structure.py <C3/ranks.json> --output <out> | committed at source commit | Summary: theory c3-deficiency-observations.md:19, c3-n1-mixed-axis-obstruction.md; directions/C3/evidence.md:13-15.  |
| `independent/audit-targets.json` | Git blob `0b4842fa06c5` at `2b52b432fe59`; AC cold storage PENDING | 31,492 | `8ac5c8556d98f7c00a82aa2c6a55faeaa7edf0ea95e1e532c5f6952327f5ef1f` | `2b52b432fe59` | none committed (independent reviewer's inline script) | committed at source commit | Summary: independent/report.md:11. Independent integrity manifest (84 developer + 42 independent files). |
| `independent/c0-rerun/catalogue.json` | Git blob `9f8490412f76` at `2b52b432fe59`; AC cold storage PENDING | 203,368 | `21cd7610051d7f51e8578051da164f73ef112d9081765cea7156b26f01441430` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c0_catalogue.py --output-dir <dir> | committed at source commit | Summary: independent/commands.md:44 (byte-identical to developer output). Same Git blob as directions/C0/catalogue.json. |
| `independent/c0-rerun/count-trials.json` | Git blob `10fa9a834300` at `2b52b432fe59`; AC cold storage PENDING | 168,359 | `8d9d213e0725e6cc8d32b53fd71ea5220678fcb99dec0e22cd6149b8ca37b0c9` | `2b52b432fe59` | same run as independent/c0-rerun/catalogue.json | committed at source commit | Summary: independent/commands.md:44. Same Git blob as directions/C0/count-trials.json. |
| `independent/c1-extension-rerun.json` | Git blob `42cd3375cd15` at `2b52b432fe59`; AC cold storage PENDING | 18,243 | `487878fcb02aed7232847361a457fde0bb606b71de4d0077d4c0bc22e6abc75e` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_extension.py --output <out> | committed at source commit | Summary: independent/commands.md:44; independent/c1-extension-comparison.json.  |
| `independent/c1-rerun.json` | Git blob `cb8e00fd0a13` at `2b52b432fe59`; AC cold storage PENDING | 44,015 | `0275afeb6d6f4def48200911b58fc17e2d8331f6686c37684966abd264a42247` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c1_mod4.py --output <out> | committed at source commit | Summary: independent/commands.md:44; independent/numerical-rerun-comparison.json.  |
| `independent/c1-stability-rerun.json` | Git blob `269b21b89b0e` at `2b52b432fe59`; AC cold storage PENDING | 29,003 | `b0ec03829631a2da48d8e09b4625c183281019156e19d7afe6aa8db140a90fcf` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_stability.py --output <out> | committed at source commit | Summary: independent/commands.md:44.  |
| `independent/c1-stability-rerun.log` | Git blob `baaec160459c` at `2b52b432fe59`; AC cold storage PENDING | 20,377 | `e4194bec66261a7a0f7ca1c058b8407d4ee863a58615db516b1a7fb395d4aeb4` | `2b52b432fe59` | stdout of the c1_stability.py rerun | committed at source commit | Summary: independent/c1-stability-rerun.json (cold); independent/commands.md:41. Duplicate of the rerun JSON content. |
| `independent/c3-lebesgue-rerun.json` | Git blob `f28d42612ad7` at `2b52b432fe59`; AC cold storage PENDING | 69,143 | `4ddecacce07f85d61c78b444333b6658aeff4ca2528da3f49b80ccf46fea3546` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/lattice-unisolvence/code/c3_lebesgue.py <C3/ranks.json> <C0/catalogue.json> --output <out> | committed at source commit | Summary: independent/commands.md:44; independent/report.md.  |
| `independent/c3-obstructions-rerun.json` | Git blob `4279cd910982` at `2b52b432fe59`; AC cold storage PENDING | 139,847 | `7aa20154d9f681d66d991cc88dae65632059d6d9250d58070a4432a96269c5df` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c3_obstructions.py <C3/ranks.json> <C3/structure.json> --output <out> | committed at source commit | Summary: independent/commands.md:44; independent/report.md.  |
| `independent/c3-rerun.json` | Git blob `dbdb6cd0c96b` at `2b52b432fe59`; AC cold storage PENDING | 535,225 | `b2010a96cee00ad546ebd5bd2075f894f081e8bf616d2ef0b13d1aa711b88b24` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c3_rank.py <C0/catalogue.json> --output <out> | committed at source commit | Summary: independent/commands.md:44; independent/report.md 'C3 ranks'. All 2,184 modular ranks reproduced. |
| `independent/c3-structure-rerun.json` | Git blob `5c5d13a15f83` at `2b52b432fe59`; AC cold storage PENDING | 39,835 | `10a589590b2cb409b0d54c18dab2f2f37f11edfe28ae9a82bb2e5d692555e2d5` | `2b52b432fe59` | python tracks/lattice-unisolvence/code/c3_structure.py <C3/ranks.json> --output <out> | committed at source commit | Summary: independent/commands.md:44; independent/report.md.  |
| `protocol/snapshot.json` | Git blob `35cc2caf0d05` at `2b52b432fe59`; AC cold storage PENDING | 32,598 | `062ad98a6cb689c6b78126f50e76763c0d1e0b21f9398227899d27755b171d3b` | `2b52b432fe59` | python topics/lattice-unisolvence-20261031/protocol/check_protocol.py > <out> (at head 61dcbe5e) | committed at source commit | Summary: protocol/report.md:9-27. Historical protocol snapshot; not reproducible at later heads. |
| `response-review/final-snapshot.json` | Git blob `040975bbd5fb` at `2b52b432fe59`; AC cold storage PENDING | 33,606 | `70fc6c04920857193f9cb4507e43f43a38a101fefd575a0ed9f766ef5840e07e` | `2b52b432fe59` | python topics/lattice-unisolvence-20261031/response-review/check_response.py (stdout) plus reviewer-added fields | committed at source commit | Summary: response-review/report.md:9-22; response-review/developer-check-rerun.json. Historical review snapshot. |

`<out>`, `<work>`, `<deps>` and `<flint>` stand for scratch paths. Never write regenerated output over committed files.

**Retrieval**

```sh
python tools/cold_storage.py verify  lattice-unisolvence-20261031   # every entry against its Git object
python tools/cold_storage.py restore lattice-unisolvence-20261031   # put the files back in place, then run the recorded checkers
python tools/cold_storage.py clean   lattice-unisolvence-20261031   # remove the restored copies again
python tools/cold_storage.py export  lattice-unisolvence-20261031 --dest C:\Users\andreyac\Downloads\padua\cold_storage
```

These commands need a full clone. In a shallow clone, first run `git fetch origin 2b52b432fe59c9a50aef9deebe5152c5d6874465`.

**Retention**

Permanent, with AC as custodian. The Git history copy lasts as long as history is not rewritten. The AC copy is created by `export`; commit its receipt hash here when that is done.

### Addendum 2026-11-02 — retained files also moved (AC approval)

AC approved moving the files listed above as "kept on purpose" as well. They are now in [`cold-storage.json`](cold-storage.json), and that list no longer applies. Restore them before running the scripts named in each row.

| File | Actual storage path | Bytes | SHA-256 | Source commit | Frozen generating command | Script blob IDs | Checker command / result |
|---|---|---|---|---|---|---|---|
| `provisional-id-map.json` | Git blob `587ec106e9ea` at `2b52b432fe59`; AC cold storage PENDING | 19,769 | `3b04ce988f1e90f1b84aae1c91097e309aa4dbe982c71f8317b13efd8aac60c4` | `2b52b432fe59` | not script-generated: orchestrator-authored map of 66 provisional IDs | — | Summary: ID_CROSSWALK.md:235; topics/padua-batch-20261031/ALLOCATIONS.md:128,180. Restore before running check-response-01.py, response-review/check_response.py or programme-ideas allocation scripts. AC 2026-11-02 approved moving the retained registry/source files to cold storage as well. |

### Corrections 2026-11-02: complete commands and readers (response to the Codex cold-storage audit, F3/F4)

These values replace the clipped or inaccurate ones in the tables above. The machine manifest [`cold-storage.json`](cold-storage.json) carries the same values.
- No identity field changed (path, bytes, SHA-256, Git blob).
- Commands are quoted verbatim from the cited records. Where a record gives no command, the row says so explicitly.
- A "working-tree reader" reads the checked-out file and needs `restore` first. A "historical Git reader" reads pinned Git objects and does not.
- Restoring files does not mean that point-in-time validators accept a later head.

- `provisional-id-map.json`, **notes** (F4): Registry map. Restore with `python tools/cold_storage.py restore lattice-unisolvence-20261031`. Working-tree readers: topics/lattice-unisolvence-20261031/check-response-01.py:50, topics/lattice-unisolvence-20261031/response-review/check_response.py:31 and, across topics, topics/programme-ideas-20261031/pr-prep/allocate.py:30 and topics/programme-ideas-20261031/audit-04-support/allocation-repair-check.py:49-50 (current() snapshot; the same script also reads it from Git at :45). Historical Git readers (pinned revisions; restoring the current file does not replace that history): topics/programme-ideas-20261031/audit-04-support/allocation-check.py:56 and :178-186 (SOURCE 37820a528c863e5cfe2dc2f1f8879b4fd40cf210 and ALLOC^) and topics/programme-ideas-20261031/audit-04-support/integration-repair-check.py:46-50 (git show at SOURCE and REPAIR). The programme-ideas allocator needs further topics restored too: see the notes of topics/programme-ideas-20261031/lit/integration-map.json. AC 2026-11-02 approved moving the retained registry/source files to cold storage as well.

After any export, check the archive with `python tools/cold_storage.py verify-archive <DIR>/lattice-unisolvence-20261031 --manifest topics/lattice-unisolvence-20261031/cold-storage.json`, and run it again immediately before relying on the archive (for delivery acceptance, or before a history purge). The export receipt alone is not proof that the files are still present.

## 2026-11-05 raw-output archival addendum

AC directed generated outputs to cold storage. Additional raw transcripts and
analysis captures from this topic are now pinned at source40347d1 in separate
component manifests; all older manifests/identities above are unchanged. See
[the migration index](../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md)
for exact file counts, manifest paths, verified export/restore commands and
receipt hashes. Small essential proof receipts, summaries and code remain in Git.
Physical delivery to AC remains pending; staging is not a delivery claim.
