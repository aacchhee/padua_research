# Cold-storage manifest — topics/bivariate-lanczos-20261031/reviews/logs_L3

2026-11-05. AC instructed: “generated outputs should go to cold storage.”
Raw transcripts/generated analysis captures are archived without changing their bytes.
Small essential receipts, scientific summaries, mathematics and all code remain tracked.

Exact retrieval source: pushed `40347d11071c81c1c633a2578cb52325bb92584a`. [Machine manifest](cold-storage.json)
records every path, SHA-256, size and Git blob. The source is a retrieval snapshot,
not a relabelling of historical execution provenance. No artifact was split; this
manifest belongs to an existing logical experiment/audit component.

## Artifact identities

| Repository path | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/dev_exact_certificates_rerun.log` | 3963 | `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b` | `c88017135d020db69ecf438794f0710dc5a09fda` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/dev_exact_certificates_rerun.time` | 42 | `b170dd95ccf2256976a02bd557dd7465989e5f782133b814879f027ac72a448c` | `e7d3013046db73cc0d0d56d1c3b7507e4bf75092` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/hankel_crosscheck.log` | 727 | `ba4d8303722fd5e12635f1d5396b3b67d74029843101992f7bddc9b82d7ae9df` | `654d2e5406cc83f02b2933c62d9009aa8404488c` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_H.log` | 3622 | `925e8040d944f8c0e8e19f510b754789b468d32aeb4db985243159f2f6abcb60` | `abf7f115c3d91082e2e19584ee2b5e300b8c8fec` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_dkappa.log` | 374 | `83f8ea7429a93a95b441ceab35cdd5e026a42ec89498cefb1b22f2b5fe48bfbd` | `be7dae0bdbd599c34bd76ecfe16832585d471684` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_exact_check.log` | 3259 | `2c2aded478ad891181e9a35272974ae0ea0099d0318941501e97fcf09d9d61d6` | `0447e32822865dba3854fdb96d2c318aaed23610` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_favard.log` | 1177 | `a3c0394aa93a7d217f1b3dab6872ed00269c947137d49d1484a38acd1171bdb4` | `9314af67ab5cae17ed1a82377bce6d672685282c` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_generator_cert.log` | 1875 | `cbedab3cce2e063d413eed29a0f989f65333607959ee3bf19dac66746223fe61` | `2cbd82a28a014ffb05504c289678460c3040cfbe` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_lp.log` | 1136 | `81beed39978c6696bc49233bd349dd18b1c96dd2eff71f85b4111e3da8d67569` | `32f0b7811558a2f0d07ca2cf4ee7538569b42649` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/padua_n4_generator_cert.log` | 726 | `0b8df79739c92fb70acc911d5553d7517045b0adfa244fd48f0d956431776494` | `a41d44a62bd0321d03c018cf358b41423bb73e61` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/unisolvence_check.log` | 318 | `a1e21ecb647ce34b747d87e456a7839acb28974cb987c57edc0734e1c9093188` | `f4de059552c1c1dac99584dfc11011ae098f8025` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/directions/L3/response-recon-01.md](../../../directions/L3/response-recon-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-prior-art-01.md](../../L3-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md](../../L3-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-02.md](../../L3-reconstruction-02.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/reviews/L3-prior-art-01.md](../../L3-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md](../../L3-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-02.md](../../L3-reconstruction-02.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/reviews/logs_L3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_reviews_logs_L3_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/reviews/logs_L3/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/reviews/logs_L3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/reviews/logs_L3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md).
Source and destination SHA/size verification is required before removing tracked
copies. The receipt describes export-time readback; re-run verify-archive when
relying on the archive later. No Git history is rewritten.

## Retention and physical delivery

Physical delivery to AC’s `Downloads/padua/cold_storage` is **PENDING**;
that destination is not mounted/accessible in this session. The local stage has
no promised retention period and is not a substitute claim of delivery.
Pinned source blobs remain reachable through the pushed branch history; they
provide cloud retrieval if staging is lost. Keep staging while available.
No purge or deletion of historical Git objects is authorized.

## Frozen command records

These are verbatim historical records, not new executions. Direct named-output
invocations are distinguished from partial argv, checker/input mentions and
script/output mappings. Preserve the original record’s working directory,
environment, source revision and placeholders; do not treat an abbreviated
line as a newly reconstructed runnable command. For missing capture details,
exact-byte retrieval from the pinned blob is the supported archival route.

| Artifact | Status | Command record IDs | Direct output IDs |
|---|---|---|---|
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/dev_exact_certificates_rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/dev_exact_certificates_rerun.time` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/hankel_crosscheck.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_H.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_dkappa.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_exact_check.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_favard.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_generator_cert.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_lp.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/padua_n4_generator_cert.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3/unisolvence_check.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/directions/L3/response-recon-01.md:25`,
blob `a9bbc41307b2dae96e8e9f2f09972f1521fa0b48`:

````text
| Informational: 306, N301 eligible for PROVED | **Applied** after the L1 fix: 306 and N301 now PROVED, citing the reviewer's independent exact rerun (`indep_exact_check.py`, log `reviews/logs_L3/indep_exact_check.log`) and the byte-identical developer rerun. | 306, N301, 300 |
````
