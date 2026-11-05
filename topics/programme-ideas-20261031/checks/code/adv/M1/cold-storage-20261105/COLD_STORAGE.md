# Cold-storage manifest — topics/programme-ideas-20261031/checks/code/adv/M1

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
| `topics/programme-ideas-20261031/checks/code/adv/M1/m1_moller_extension.log` | 3338 | `73fc765b411d60a1abc4a065d81fe818057e1cd9fb82f91ac37c91379189eed5` | `9b56a7a08a820eb301d851033d25eab3be73995b` |
| `topics/programme-ideas-20261031/checks/code/adv/M1/m1_word_rule.log` | 6396 | `f86de302ce84b5d2bcaad62128fbcbf2d7e7855f239acea7514f707f02d39c3a` | `f1c10f6e532d10b09a2271d7531b313f1b42780a` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/programme-ideas-20261031/COLD_STORAGE.md](../../../../../COLD_STORAGE.md)
- [topics/programme-ideas-20261031/LOG.md](../../../../../LOG.md)
- [topics/programme-ideas-20261031/audit-01.md](../../../../../audit-01.md)
- [topics/programme-ideas-20261031/checks/adversarial-M1.md](../../../../adversarial-M1.md)
- [topics/programme-ideas-20261031/report.md](../../../../../report.md)
- [topics/programme-ideas-20261031/sources/campaign-inputs/COLD_STORAGE.md](../../../../../sources/campaign-inputs/COLD_STORAGE.md)

Short scientific summaries:
- [topics/programme-ideas-20261031/COLD_STORAGE.md](../../../../../COLD_STORAGE.md)
- [topics/programme-ideas-20261031/LOG.md](../../../../../LOG.md)
- [topics/programme-ideas-20261031/audit-01.md](../../../../../audit-01.md)
- [topics/programme-ideas-20261031/report.md](../../../../../report.md)
- [topics/programme-ideas-20261031/sources/campaign-inputs/COLD_STORAGE.md](../../../../../sources/campaign-inputs/COLD_STORAGE.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/programme-ideas-20261031/checks/code/adv/M1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_programme-ideas-20261031_checks_code_adv_M1_cold-storage-20261105 --manifest topics/programme-ideas-20261031/checks/code/adv/M1/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/programme-ideas-20261031/checks/code/adv/M1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/programme-ideas-20261031/checks/code/adv/M1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../../../../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md).
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
| `topics/programme-ideas-20261031/checks/code/adv/M1/m1_moller_extension.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/M1/m1_word_rule.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/checks/adversarial-M1.md:68`,
blob `6b735af2ef7bb225f4df32c16d095bb8d4ff71e0`:

````text
| `checks/code/adv/M1/m1_moller_extension.py` (log `m1_moller_extension.log`) | commutator rank and Möller size of the Π_{n−1} sections; Levenberg–Marquardt search for graded real symmetric commuting extensions of Möller size (DST form); nodes inside the support, min weight, local dimension of the solution set modulo O(s) | product Chebyshev, Legendre, unit disk, triangle, Jacobi (α,β) = (0.5,0)×(0,1.5); n = 2..6; 8 random starts; scipy | see table below | MEASURED (non-convergence is not a non-existence certificate) |
````

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/checks/adversarial-M1.md:67`,
blob `6b735af2ef7bb225f4df32c16d095bb8d4ff71e0`:

````text
| `checks/code/adv/M1/m1_word_rule.py` (log `m1_word_rule.log`) | T1 word exactness ≤ 2k+1; T2 order dependence at 2k+2; T3 error = ⟨(I−P_k)m_u,(I−P_k)m_v⟩ and its sign; T4 anti-Gauss flip at 2k+2 and 2k+3; T5/T5b f = 1/((x−a)²+(y−b)²) via the order-free lift vs univariate Lanczos on g(X,Y), bracketing rate; T6 three lifts of 1/(1.5−xy) | M = 30 random nodes in [−1,1]², random weights, exact pair from Householder QR to degree 9, k = 1..4; 200 (T5, T6) / 100 (T5b) random instances; numpy; 1.5 s | T1 ≤ 3e-16; T2 e.g. k = 1: 0.0815 / 0.0039 / 0.0039 vs moment 0.0631; T3 identity to 1e-16, both signs occur; T4 max|e_G + e_A| ≤ 6e-16 at 2k+2 and ≤ 2e-16 at 2k+3 (ratio −1.000); T5 brackets 200, 199, 196, 198 of 200; median rel. errors pair-Gauss 1.6e-2, 9.8e-4, 9.2e-5, 3.1e-6 vs Lanczos with m = k+1 steps 3.4e-2, 5.2e-3, 1.1e-3, 1.2e-4; T5b (equal X/Y-product count) pair 1.5e-2, 1.2e-3, 9.2e-5, 3.7e-6 vs Lanczos 1.7e-1, 5.7e-3, 2.0e-4, 3.8e-6; T6 lift spread 3.8e-5…5.0e-4 relative, brackets 177–200/200 | MEASURED |
````
