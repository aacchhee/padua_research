# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-01/L1-later

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
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/cert_square40_rerun.log` | 1823 | `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2` | `d5ee284459a4b00b87a8118d6c3f44bc0741370b` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/cert_square_rerun.log` | 1566 | `8606323c1890a4eea9d8c3528f9b40adada016130e3729e1fa4be367ed374f5a` | `3d31816531e4701107b8a3608e92de8b4a04cfcd` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/cert_triangle_rerun.log` | 1665 | `b328c93fccdccf009a3c48d07c5df0a19adc4f60eeb97a4db0085f774b65c95d` | `604f1c1144205b6d5d89283fbcc86f50bcd797f3` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/closed_loop_rerun.log` | 821 | `77b844281db536a8101a22faee5d41037ac2799a5d2a1de5604f386fc7394ebe` | `f5159b3fc11dc649d97cd60315a675bcf91c2b8d` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/environment.log` | 2051 | `bc81f3b0f70737a14a85e70a2f477eeacc056486575f89223038582901aade2f` | `22e76e7dd549ebdb88c28688bd6c2f8491feee6f` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/gain_producer_rerun.log` | 1577 | `583ca75e1338abcb7d8d193b71d865fd861f5f774a5be666d7e3af495f37169e` | `e2fa585e2770105af9d76255ec5c3946283efea4` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/independent_checks.log` | 1687 | `dd49d6a0bbd2ec832b5d3274f7ff06bc6404bf2e6f404d35ca6f33190efab0ad` | `d651d1146eca4e027f3c766adf4f843be4b9849a` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/near_product_producer_rerun.log` | 1654 | `6dd7cce88660e9a303ac2f10051c321abd95b89955e56d7460acf697451de16a` | `72d80acd8e71865b2ee7b6549ca8bedb57bbd139` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/open_loop_rerun.log` | 1662 | `38855fabb74083ad40842f65bc9b4e264382e2afd7062bbcf6302c082118eab2` | `68ac6a6cde433f12152750c702104c0a800f5df3` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/rule_reanalysis.log` | 419 | `611e9d0aa5ce7e292be59a035238601527dd576b3d1772b65a9affd5ecc71e55` | `37d47772bbbed884ade4e3609e0696dbfef51be9` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/simax_producer_rerun.log` | 306 | `7ff6cb74f7a020e21c8ecf09cf1a8ee83f923465e75f7fbb137b90171d386923` | `cb9580785addb1a22cc72ec55a03530d7d826b5e` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-01/L1-later.md](../../L1-later.md)
- [topics/bivariate-lanczos-20261031/directions/L1/candidates.md](../../../directions/L1/candidates.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md](../../../directions/L1/response-audit-01.md)
- [topics/bivariate-lanczos-20261031/pr-prep/proof_status.rows.md](../../../pr-prep/proof_status.rows.md)
- [topics/bivariate-lanczos-20261031/response-01.md](../../../response-01.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-01/L1-later.md](../../L1-later.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-01/L1-later/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-01_L1-later_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-01/L1-later/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-01/L1-later/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-01/L1-later/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/cert_square40_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/cert_square_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/cert_triangle_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/closed_loop_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/environment.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/gain_producer_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/independent_checks.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/near_product_producer_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/open_loop_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/rule_reanalysis.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/simax_producer_rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:96`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py square 40 16` | `cert_square40_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md:134`,
blob `e9df95c70551a150095508ba065b743842c46ddf`:

````text
- Codex audit-01 executed it: `rv2_certificate.py square 40 16`. Log `audit-01/L1-later/cert_square40_rerun.log`, sha256 `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2`; manifest `audit-01/L1-later/manifest.json`, executions[2].
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/pr-prep/proof_status.rows.md:38`,
blob `9e62efd643423bbb9b89f4813208a87f4980fa36`:

````text
| PD-T041 | Exact rational certificate: for the dev (BJ) rule the window-recurrence propagator grows exponentially on the triangle grid and stays polynomial on the square grid (degrees ≤ 12, computer-assisted; "exponentially" and "polynomial" describe the finite range only) | PROVED | 1. impulse identity: PROVED; 2. certificate on T_24, Q_24: PROVED (finite, dev rule). The independent rerun was done by recon-02 `rv2_certificate.py`, two ways: (A) full exact Gram–Schmidt with off-window coefficients checked exactly 0; (B) exact LDLᵀ of the moment matrix. Identical values and maximisers; criterion decided exactly; logs `reviews/logs_L1b/cert_{T24,Q24}*.log`. Before recon-02: CONDITIONAL.; 3. T_40, Q_40, rotated Q_24: PROVED (finite). T_40 and rotated Q_24: reproduced exactly by recon-02 (`cert_T40.log`, `cert_rotQ24.log`). Q_40: reproduced exactly by Codex audit-01 (`audit-01/L1-later/cert_square40_rerun.log`, sha256 `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2`); CONDITIONAL (not rerun) before 2026-11-01T08:33:59+01:00. Descriptive, not pre-registered. | none | PD-T029, PD-T032 | [exact-certificate-propagator-growth-triangle.md](tracks/bivariate-lanczos/theory/exact-certificate-propagator-growth-triangle.md) | bivariate-lanczos audits 01–03 (Codex); registry integration response to audit-04, independent review pending |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:95`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py square 24 12` | `cert_square_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:94`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py triangle 24 12 integer mp` | `cert_triangle_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:98`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_closed_loop_sets.py` | `closed_loop_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:97`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/L1/l1_r06_gain_identity.py` | `gain_producer_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:102`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/independent_checks.py` | `independent_checks.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:100`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/L1/l1_r04_near_product.py` | `near_product_producer_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:99`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_open_loop.py` | `open_loop_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:103`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/independent_checks.py rule` | `rule_reanalysis.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:101`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/L1/l1_simax_variants.py` | `simax_producer_rerun.log` |
````
