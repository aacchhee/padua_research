# Cold-storage manifest — topics/programme-ideas-20261031/checks/code/adv/gen3-3

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
| `topics/programme-ideas-20261031/checks/code/adv/gen3-3/bandwidth_pg_probe.out` | 4315 | `da8d787b347800074d0a6db757f3098bf7ccfccb418f98e197e59f005022c3fb` | `88df2f2cd39ac1bf49321456e2dc2e4fc1fe98f3` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/programme-ideas-20261031/checks/adversarial-gen3-3.md](../../../../adversarial-gen3-3.md)

Short scientific summaries:
- [topics/programme-ideas-20261031/checks/adversarial-gen3-3.md](../../../../adversarial-gen3-3.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/programme-ideas-20261031/checks/code/adv/gen3-3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_programme-ideas-20261031_checks_code_adv_gen3-3_cold-storage-20261105 --manifest topics/programme-ideas-20261031/checks/code/adv/gen3-3/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/programme-ideas-20261031/checks/code/adv/gen3-3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/programme-ideas-20261031/checks/code/adv/gen3-3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/programme-ideas-20261031/checks/code/adv/gen3-3/bandwidth_pg_probe.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/checks/adversarial-gen3-3.md:59`,
blob `d46ea56e8283e56156f6fb9a0a9c4ad50525fa3c`:

````text
| `checks/code/adv/gen3-3/bandwidth_pg_probe.py` (numpy, 1.7 s; output `bandwidth_pg_probe.out`) | A/B: degree bands of π∂_x, π∂_y, π²Δ, plain ∂_x in the graded orthonormal basis from exact meshes (Gauss–Duffy fan on polygons; trapezoid-in-θ × Gauss-in-r on the star-shaped quartic domain; 6 triangles on the L-shape); in-band block density; nnz(H_x). C: Dirichlet matrices with trial πΠ_n: Petrov–Galerkin (test Π_n) and symmetric Galerkin (test πΠ_n), κ with/without degree-block preconditioning, LS exponents. D: nnz(H_x)+nnz(H_y) vs N. E: trial π·(OPs of π dμ), weighted differentiation band, κ. F: degree-(b−1) matrix Pearson operator Φ∇ on polygons | n = 8 for bands/density (orthonormality 4e−15); n = 4..16 for κ (pentagon, b = 5); tolerance 1e−9 relative | A/B: bands (b−1, b−1) for pentagon (b=5, weights 1, π, π²), heptagon (7), quartic curved (4, weights 1, π), L-shape (6), square (4); π²Δ (2b−2, 2b−2) up to the n-truncation (Δ kills degrees 0,1, so lower band 6 at n = 8); plain ∂_x strictly upper, full. Block density 0.99/1.00/0.47/0.95/0.24. C: PG band (3, 8) = not banded above; Galerkin band (8,8); κ(S) exponent 4.46 (4.99 for n ≥ 8), block-preconditioned 4.21 (4.67); κ(M) 1.97, block-preconditioned 2.11 (2.49); λ_min(S) ∝ n^{−2.4..−2.8}. D: nnz ≈ 3.62–3.74·N^{3/2}. E: D̃_x band (4, −1) for n ≤ 14 ((20, −1) at n = 16 at the 1e−9 threshold, with |S̃−S_exact|/|S| = 2e−10), S̃ band (3,3), κ(S̃) exponent 1.75 (1.86), block-preconditioned 1.54 (1.72). F: Φ∇ bands (3,3) pentagon, (5,5) heptagon | MEASURED in the stated scope |
````
