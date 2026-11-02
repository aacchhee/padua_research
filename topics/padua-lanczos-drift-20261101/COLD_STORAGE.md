# Cold-storage manifest — padua-lanczos-drift-20261101

Intended AC destination: `C:\Users\andreyac\Downloads\padua\cold_storage\padua-lanczos-drift-20261101\`.
**Windows delivery of the rows below remains pending.** The rows describe actual
Codex-workspace staging, not a receipt from that destination. Update 2026-11-01
(Claude, response-02): Claude sessions linked to AC's computer can reach the
destination, but these files live only in the Codex workspace, where audit-02
verified them locally. They must be delivered from there (or by AC). Delivered
so far, with readback: the audit-01 outputs in `audit-01\` (zip sha256
`29c177218d0d08dcfb1299c1cdc2cc333c40f6da3208abd6f12f1e089150f9ff`, 269978
bytes; manifest `checks/audit-01/manifest.json`). Cold storage holds large
artifacts only; results tracking is repository-only (merged PR16 rule).

| File | Actual storage path | Bytes | SHA-256 | Source commit | Frozen generating command | Script blob IDs | Checker command / result |
|---|---|---:|---|---|---|---|---|
| Own scientific snapshot ZIP | /workspace/exports/padua-lanczos-drift-b09e1db.zip | 799968 | 27476b624d424f082a71779618b9e1f9b06d6fba7db6b662755cf886637dd3a4 | b09e1dbe0baafd666cf0d779a671a40f55de2d75 | Python zipfile of the 81 own topic/code/theory files at this commit, plus SNAPSHOT.txt; no third-party sources | Git blobs at source commit; own file identities in final-validation.json | zipfile.testzip(): PASS, 82 entries |
| Nonessential raw rotated capacity output, local working artifact | /workspace/padua-drift-runs/e1/cgs2-multinode-rotated-n12-bj.json | 3626111 | ffd035eef09d39be2ab862a6c12abbe58c455cd9131615ee89b4eefba14d1d8e | b09e1dbe0baafd666cf0d779a671a40f55de2d75 (producer bytes identical to run) | PYTHONPATH=/workspace/padua-drift-runs/python-deps python tracks/bivariate-lanczos/code/drift/e1_cgs2_multinode.py --witness /workspace/padua-drift-runs/e1/cgs2-witness-rotated-n12-bj.json --output /workspace/padua-drift-runs/e1/cgs2-multinode-rotated-n12-bj.json | 241ceb94411a8b11c98ac99e97a0327f18605b33 | explicit projection PASS; separate independent capacity/sign regeneration PASS, independent-scalar-01.json |

## Essential committed evidence and regeneration

The large raw capacity file is outside Git and excluded from the handoff ZIP.
It is not a hidden mathematical input: committed e1_reproduce.py regenerates
capacities from the explicit nodes, choices and compact certificate, validates
source/code hashes, and checks the explicit projection. The independent checker
instead regenerated both prior witnesses/capacities and matched every exact
capacity/sign. Small essential evidence, proofs and checker code are committed;
the measured scalar record remains MEASURED and its factor10 test INCONCLUSIVE.

Reproduction setup/versions: tracks/bivariate-lanczos/code/drift/README.md.
Commands and source/output hashes: evidence/e1-manifest.json,
e1-scalar-manifest.json, e5-manifest.json, e6-provenance.json,
independent-math-01.json and independent-scalar-01.json.

## Delivery and retrieval

The ZIP is staged for AC to download from the workspace and unpack at the
intended topic-specific Windows destination. Verify byte count and SHA-256
above after download; record the actual Windows path and readback receipt
when that happens. The ZIP is the scientific snapshot at the stated source
commit; the later archive receipt and numbered audit handoff are published
on the topic branch. No Windows write or long-term archival receipt is claimed.
The external polyrat/BNT sources are omitted; retrieve them by the pinned URLs,
commits and hashes in external-code.md. No third-party PDFs/fulltext are included.

## Retention

No deletion or expiry policy is invented. AC is the intended permanent
custodian. Workspace files are temporary until actual delivery. Required own
code and compact evidence are also retrievable from the source commit.

## Repository cleanup 2026-11-02 — large regenerable outputs moved off the branch head

AC (2026-11-02): "I do not think that we have to store large outputs that can be regenerated. Make sure that all needed code is in the repo, some short summaries are stored and expunge the large data files (cold storage)"; "18 mb per repo is too much."

Every generated data file of 16 KiB or more in this directory left the branch head: 30 files, 2,963,704 bytes. Machine manifest: [`cold-storage.json`](cold-storage.json). Tool: `tools/cold_storage.py`.

These files have **not been delivered to AC's Padua cold storage yet** (PENDING). Until then, the only stored copy is Git history, pinned by blob id at the pushed main commit `2b52b432fe59c9a50aef9deebe5152c5d6874465`. Each file's SHA-256 is recorded alongside, so the bytes can be verified.

Code, records, and small receipts and summaries stay. Committed checkers that load or hash-pin moved files (restore first): tracks/bivariate-lanczos/code/drift/e1_reproduce.py, e1_scalar_finite_check.py, check_independent_scalar.py, e1_check.py, e1_response_checks.py, e1_replay_n4.py, e6_offsample.py, e6_offsample_compare.py, e4_response02_check.py and checks/audit-0N scripts. External polyrat 0.2.2 (commit 6903d7af) is not in Git (see external-code.md). Not recorded as scripts: assemblers of e1-scalar-cgs2.json, e1-multinode-certificates.json, independent-*.json, audit-02-e34-checks.json; producers of allocation-scan.json, final-validation.json, protocol-check.json, checks/audit-02/manifest.json; exact command of e1-n12-directional-snapshot.json. The earlier 3.6 MB rotated capacity file remains outside Git as already recorded.

Files of 16 KiB or more kept on purpose (not generated output):
- none

| File | Actual storage path | Bytes | SHA-256 | Source commit | Frozen generating command | Script blob IDs | Checker command / result |
|---|---|---|---|---|---|---|---|
| `allocation-scan.json` | Git blob `7032dac58947` at `2b52b432fe59`; AC cold storage PENDING | 24,675 | `47481c936bce23b195e7cccc9330aad0f9cb54f8b24b26f30e23c89977da2ebf` | `2b52b432fe59` | none recorded (mechanical git ls-tree/git show scan by setup assistant; method text in file) | committed at source commit | Summary: preparation/README.md 'Union and allocation'; topics/padua-batch-20261031/ALLOCATIONS.md:16. Historical reservation scan; not regenerable as-was. |
| `checks/audit-02/manifest.json` | Git blob `0d1e6f5a5eac` at `2b52b432fe59`; AC cold storage PENDING | 30,974 | `0da2a95e4199489df95da6bc6b308a3395c705361dc3ef638be8144d7dbbd1cd` | `2b52b432fe59` | none committed (audit-02 has no manifest writer) | committed at source commit | Summary: audit-02.md 'Verdict' and 'Executions and evidence'; checks/audit-02/Protocol.md. Codex audit-02 manifest: candidate cef79d66, CHANGES REQUIRED, 42 findings dispositioned; read via git blob by checks/audit-03/Protocol/check.py. |
| `evidence/audit-02-e1-checks.json` | Git blob `3e55e1ae0882` at `2b52b432fe59`; AC cold storage PENDING | 108,115 | `7bb3e3b566d7d25d369ee812c007b690b46bbdcc54b55ceb54f18fec9390d0ee` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python3 topics/padua-lanczos-drift-20261101/checks/audit-02/E1/make_evidence.py (after the reruns listed in the file's 'commands') | committed at source commit | Summary: checks/audit-02/E1.md; audit-02.md:33. Runtime input of e1_replay_n4.py and e1_scalar_finite_check.py (pinned). |
| `evidence/audit-02-e34-checks.json` | Git blob `ffe05f9224e7` at `2b52b432fe59`; AC cold storage PENDING | 19,752 | `368c4e83d0e6ce13574d36b5a8bf283d6775142ee9ccff0b7693d8541058a12e` | `2b52b432fe59` | python3 -B tracks/bivariate-lanczos/code/drift/e4_closure_check.py --output <work>/producer-rerun.json; python3 -B topics/padua-lanczos-drift-20261101/checks/audit-02/E34/independent_exact.py --output <work>/independent-exact.json; receipt assembly not scripted | committed at source commit | Summary: checks/audit-02/E34.md; audit-02.md:34.  |
| `evidence/audit-02-e5.json` | Git blob `037427e0db26` at `2b52b432fe59`; AC cold storage PENDING | 25,999 | `476f05d272a85b438e6b0afcb136537c1cd1b90e3ce7b65b1c0489b66fdda10a` | `2b52b432fe59` | python3 -B topics/padua-lanczos-drift-20261101/checks/audit-02/E5/manifest_e5.py > <out> (after response01_e5_checks.py, e5_exact_checks.py, independent_e5.py reruns) | committed at source commit | Summary: checks/audit-02/E5.md; audit-02.md:35. Receipt result PASS. |
| `evidence/audit-02-e6-checks.json` | Git blob `4c9a5f861e7c` at `2b52b432fe59`; AC cold storage PENDING | 217,139 | `34ca7a1c29cd4fcaaea9b746a9408c97ad9b8070ee1fdc4d398d7faa98bdf1d9` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python topics/padua-lanczos-drift-20261101/checks/audit-02/E6/check.py --work <work> --output <out> | committed at source commit | Summary: checks/audit-02/E6.md; audit-02.md:36. all_numerical_checks_pass = true. |
| `evidence/audit-02-protocol-artifacts.json` | Git blob `5dd38295b9a1` at `2b52b432fe59`; AC cold storage PENDING | 152,206 | `6c91b3e29b92b1dfbab199283364bb93f01b525a128a092761e4f165677c9f24` | `2b52b432fe59` | python topics/padua-lanczos-drift-20261101/checks/audit-02/Protocol/check_artifacts.py --output <out> | committed at source commit | Summary: checks/audit-02/Protocol.md; audit-02.md:37. Workspace artifact integrity receipt. |
| `evidence/audit-03-e1-checks.json` | Git blob `44bb8fc365e0` at `2b52b432fe59`; AC cold storage PENDING | 32,388 | `6be52a46390441a6bb1e278653cc47f6b0a6b0a536d946a00a064fb49a93d33b` | `2b52b432fe59` | python3 topics/padua-lanczos-drift-20261101/checks/audit-03/E1/make_evidence.py (after the executions[] listed in the file) | committed at source commit | Summary: checks/audit-03/E1.md; audit-03.md:36. finite_mathematics_pass true, degree4_replay_pass true. |
| `evidence/audit-03-e34-checks.json` | Git blob `5da82b2646d9` at `2b52b432fe59`; AC cold storage PENDING | 32,722 | `891edfd04466a3c040c6e8c1b301e511c262cbe448c0a72bae2e0b1efdba4f99` | `2b52b432fe59` | python3 -B topics/padua-lanczos-drift-20261101/checks/audit-03/E34/make_evidence.py (after e4_response02_check.py and audit-03/E34/independent_limits.py) | committed at source commit | Summary: checks/audit-03/E34.md; audit-03.md:37.  |
| `evidence/audit-03-protocol-checks.json` | Git blob `a90b3346a002` at `2b52b432fe59`; AC cold storage PENDING | 39,780 | `b78d43061e6a81058d618e727aea2685ec0887a4d66f0a587b580127de8b713c` | `2b52b432fe59` | python -B topics/padua-lanczos-drift-20261101/checks/audit-03/Protocol/check.py --output <out> | committed at source commit | Summary: checks/audit-03/Protocol.md; audit-03.md:40. all_mechanical_checks_pass = true. |
| `evidence/audit-04-checker.json` | Git blob `afdb8095fc1d` at `2b52b432fe59`; AC cold storage PENDING | 19,102 | `15d1e3b7a73b3aaa3980bf281ee57c0c83ddf6da12e4e46c4060762a402986a4` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python3 topics/padua-lanczos-drift-20261101/checks/audit-04/check.py --work <work> --regenerate --output <out> | committed at source commit | Summary: audit-04.md 'Actual executions and provenance'; evidence/audit-04-inventory.json. result PASS, 7 checker cases. |
| `evidence/e1-exact-check.json` | Git blob `1b9bfe0ac54e` at `2b52b432fe59`; AC cold storage PENDING | 20,868 | `d8488e9637210ae2e513eb4b99259ad37d617b24e2026e3743ac0e664e2caaba` | `2b52b432fe59` | python tracks/bivariate-lanczos/code/drift/e1_check.py --evidence <e1-full-sweep.json> --output <out> | committed at source commit | Summary: evidence/e1-summary.md; theory drift-codex-e1-04 (PD-T139); evidence/e1-manifest.json. 88 records checked, all PASS. |
| `evidence/e1-full-sweep.json` | Git blob `b252ae7c1837` at `2b52b432fe59`; AC cold storage PENDING | 616,693 | `0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344` | `2b52b432fe59` | PYTHONPATH=<deps> python tracks/bivariate-lanczos/code/drift/e1_batch.py --output-dir <work>/full --summary <out> --workers 4 (88 e1_exact.py runs, up to 150 s each) | committed at source commit | Summary: evidence/e1-summary.md; theory drift-codex-e1-04 (PD-T139); evidence/e1-manifest.json; code/drift/README.md. Runtime input of e1_check.py and e1_response_checks.py. |
| `evidence/e1-multinode-certificates.json` | Git blob `da3db41d9fa5` at `2b52b432fe59`; AC cold storage PENDING | 55,328 | `fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0` | `2b52b432fe59` | e1_scalar.py -> e1_cgs2_witness.py -> e1_cgs2_multinode.py chain (commands recorded in the witness records); regenerated/validated by tracks/bivariate-lanczos/code/drift/e1_reproduce.py --set triangle\|rotated; compact assembler not scripted | committed at source commit | Summary: theory drift-codex-e1-05 (PD-T140), drift-codex-e1-06 (PD-T141); evidence/e1-scalar-manifest.json. Essential runtime input of e1_reproduce.py, e1_scalar_finite_check.py, check_independent_scalar.py (hash-pinned). |
| `evidence/e1-n12-directional-snapshot.json` | Git blob `f007e66866f9` at `2b52b432fe59`; AC cold storage PENDING | 103,002 | `385b96c2b710f53332133bfcd0575b29631351ea28ad73523213492847347f1f` | `2b52b432fe59` | not recorded (early e1_exact.py degree-12 runs; code hashes listed in file) | committed at source commit | Summary: checks/audit-01/E1-records-01-05.md:171; evidence/e1-summary.md. Early snapshot superseded by e1-full-sweep.json. |
| `evidence/e1-scalar-cgs2.json` | Git blob `128bdee846fa` at `2b52b432fe59`; AC cold storage PENDING | 444,008 | `e215556a01f9e169163b228dfe1b984d28e0cebd7f78e0d858f9a61a0de878c8` | `2b52b432fe59` | composite of e1_scalar.py, e1_cgs2.py and e1_cgs2_witness.py runs recorded inside the file; assembler not scripted | committed at source commit | Summary: theory drift-codex-e1-05 (PD-T140), drift-codex-e1-06 (PD-T141, defines U_T, U_R); code/drift/README.md; evidence/e1-scalar-manifest.json. Essential runtime input of e1_reproduce.py and e1_scalar_finite_check.py (hash-pinned). |
| `evidence/e1-source-degree2-screen.json` | Git blob `448751253eff` at `2b52b432fe59`; AC cold storage PENDING | 93,265 | `9f5c354ab2b73ece1aff4540d26256ee6d03cc39963ca493e863fa8502d34191` | `2b52b432fe59` | PYTHONPATH=<deps> python tracks/bivariate-lanczos/code/drift/e1_batch.py --output-dir <work>/screen --summary <out> --degrees 2,8,12 --sources degree2 --workers 2 | committed at source commit | Summary: evidence/e1-summary.md; evidence/e1-manifest.json. 24-run restricted-source screen, superseded by the full sweep. |
| `evidence/e6-benchmarks.json` | Git blob `58e901c4a94d` at `2b52b432fe59`; AC cold storage PENDING | 239,594 | `e7a3f940c4bd79bbf84fbe4eeafca4186c9b969c92665fb972367becc23a3c58` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --output <out> (needs external polyrat 0.2.2, numpy 2.3.5) | committed at source commit | Summary: theory drift-codex-e6-50 (PD-T146); directions/E6.md 'Metrics and measured results'; evidence/e6-provenance.json. Runtime input of e6_offsample.py. |
| `evidence/e6-frozen-grids.json` | Git blob `570bc939e52f` at `2b52b432fe59`; AC cold storage PENDING | 16,852 | `8bb5ef149c5c6fa66e03b544f6588ff8e30c50e16490d9bf728f6447bf7b6f50` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --sets T24 Q24 --grid-degree 16 --output <out> | committed at source commit | Summary: theory drift-codex-e6-50; directions/E6.md. Read by checks/audit-02/E6/check.py. |
| `evidence/independent-math-01.json` | Git blob `2470873b05fa` at `2b52b432fe59`; AC cold storage PENDING | 161,274 | `1f2c3361d2e4f19aadef7e44f093643915eb445e7da21914eccb330bedd4026a` | `2b52b432fe59` | python tracks/bivariate-lanczos/code/drift/check_independent_math.py --output <out>, plus e1_verify.py and e1_check.py runs; receipt assembly not scripted | committed at source commit | Summary: checks/independent-math-01.md 'Result and scope'.  |
| `evidence/independent-scalar-01.json` | Git blob `4bc83fa25380` at `2b52b432fe59`; AC cold storage PENDING | 186,681 | `2d06b3b4e04956f9c9e2f4127c3937543dc92ee071de2926589d0a40c9bf6a10` | `2b52b432fe59` | commands[] in the file (e1_cgs2.py, e1_cgs2_witness.py, e1_cgs2_multinode.py, e1_sign_check.py, e1_cgs2_verify.py); own checker check_independent_scalar.py | committed at source commit | Summary: checks/independent-math-01.md 'Supplement 01'; theory drift-codex-e1-06. Runtime input of e1_scalar_finite_check.py (pinned). |
| `evidence/response-01-e1-checks.json` | Git blob `7f4cecda21e7` at `2b52b432fe59`; AC cold storage PENDING | 76,613 | `0852581d7072cc81422fe5fded158c768a89ed838a882d3ac4c2dde71c49bb26` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_response_checks.py --output <out> (about 4 min) | committed at source commit | Summary: checks/response-01/E1-developer-report.md; response-01.md. overall PASS. |
| `evidence/response-01-e4-closure.json` | Git blob `ee66b32f0daa` at `2b52b432fe59`; AC cold storage PENDING | 30,826 | `956dfe71e8b6958f54e19f2d7fb30f04c5788351b7942bf8be21b41977d3599c` | `2b52b432fe59` | python3 tracks/bivariate-lanczos/code/drift/e4_closure_check.py --output <out> (about 3 s) | committed at source commit | Summary: theory drift-codex-e4-15 (PD-N062) Checks; directions/E4.md. Runtime input of e4_response02_check.py. |
| `evidence/response-01-e6-offsample.json` | Git blob `95e8216f6f31` at `2b52b432fe59`; AC cold storage PENDING | 22,147 | `12a5e7c713ec53b0a26fede8f2250a9ae8d02578df672ec11271ac450339b31d` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e6_offsample.py --output <out> (needs e6-benchmarks.json) | committed at source commit | Summary: directions/E6.md 'Response-01 off-sample results'; theory drift-codex-e6-50. Frozen; compared by sha in audit-03. |
| `evidence/response-02-e1-replay-n4.json` | Git blob `b57781988e79` at `2b52b432fe59`; AC cold storage PENDING | 23,800 | `22093d9dff7e3981182d8dbe82095bde0a5db36566b4587fa4910c483b2e870b` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_replay_n4.py --output <out> (about 75 s) | committed at source commit | Summary: checks/response-02/E1-developer-report.md; response-02.md. all_pass true. |
| `evidence/response-02-e4-creator-limit.json` | Git blob `c9078b93cc53` at `2b52b432fe59`; AC cold storage PENDING | 86,816 | `a6faea9967747b9fe962ce58f5af55fe776bf4b5201f54cc364d738aa2da4526` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e4_response02_check.py --output <out> (about 2 s) | committed at source commit | Summary: theory drift-codex-e4-15 (PD-N062) Checks; results/padua-lanczos-drift-20261101.md. 25 exact instances, all assertions passed. |
| `evidence/response-02-e6-offsample-rerun.json` | Git blob `82e85306c98e` at `2b52b432fe59`; AC cold storage PENDING | 23,663 | `0d981dd1816b40833aed6d62d5f61e1d885f62104f125c6df2a7fed337f7a5fc` | `2b52b432fe59` | PYTHONPATH=<deps> OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e6_offsample.py --output <out>; python3 -I tracks/bivariate-lanczos/code/drift/e6_offsample_compare.py --embed | committed at source commit | Summary: theory drift-codex-e6-50; directions/E6.md. Rerun equal in scientific fields. |
| `final-validation.json` | Git blob `b0f887738ddf` at `2b52b432fe59`; AC cold storage PENDING | 17,265 | `4662da274bf52d6116d2c02b7ecd5090e84bbd35e56f6bad1de1ea371335b2f5` | `2b52b432fe59` | none committed (mechanical receipt at parent b09e1dbe) | committed at source commit | Summary: audit-01.md (P-F2); response-01.md. Immutable final-validation receipt; own file identities. |
| `preparation/prepare-receipt.json` | Git blob `b7aa6c91c8c0` at `2b52b432fe59`; AC cold storage PENDING | 21,902 | `eafc24ff69bdcb4304c7d633114c103a186aac48aa64a9abcbba6ea62d973db6` | `2b52b432fe59` | python topics/padua-lanczos-drift-20261101/preparation/prepare.py --apply | committed at source commit | Summary: preparation/README.md 'What was done'. PR-preparation receipt. |
| `protocol-check.json` | Git blob `37d042a2a995` at `2b52b432fe59`; AC cold storage PENDING | 20,255 | `3ceb0af80d4bf25c7589051bf9721cd4da4674f3537e14e3ce98ab6d6b33b4b5` | `2b52b432fe59` | none committed (mechanical snapshot) | committed at source commit | Summary: audit-01.md; checks/audit-01/E6-novelty-protocol.md. Immutable protocol snapshot. |

`<out>`, `<work>`, `<deps>` and `<flint>` stand for scratch paths. Never write regenerated output over committed files.

**Retrieval**

```sh
python tools/cold_storage.py verify  padua-lanczos-drift-20261101   # every entry against its Git object
python tools/cold_storage.py restore padua-lanczos-drift-20261101   # put the files back in place, then run the recorded checkers
python tools/cold_storage.py clean   padua-lanczos-drift-20261101   # remove the restored copies again
python tools/cold_storage.py export  padua-lanczos-drift-20261101 --dest C:\Users\andreyac\Downloads\padua\cold_storage
```

These commands need a full clone. In a shallow clone, first run `git fetch origin 2b52b432fe59c9a50aef9deebe5152c5d6874465`.

**Retention**

Permanent, with AC as custodian. The Git history copy lasts as long as history is not rewritten. The AC copy is created by `export`; commit its receipt hash here when that is done.
