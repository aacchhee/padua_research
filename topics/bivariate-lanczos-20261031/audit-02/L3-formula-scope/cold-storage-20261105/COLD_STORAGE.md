# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope

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
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/developer-t318-rerun.log` | 2605 | `06413c814eec75897aaebaa4d72da455497b1716877ee824a12e6ba28a7b9c02` | `e529f6bad21024cad7e9e51562e543d4964538c2` |
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/independent-t318-initial.log` | 319 | `33b84015940c330b10abe22b137c84d857edcf59c2c00e9bc4d47014a305778b` | `aea24c9fefdd1a39af813b88820034ff54bdd20c` |
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/independent-t318.log` | 1057 | `3e5f8bac5fee4a5ccc50dc70235c523aed216efbc422b17bab4ca9033e558de4` | `91f0ee853f511c91bd42e0eb076623e18654607a` |
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/sampling-scope.log` | 921 | `3084fecff7c500ec1df8f3000ee7b2e9111423bcc56633e073c2a9d9548333d4` | `b9e73993199b5c0293c061d6308d835a437ab371` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope.md](../../L3-formula-scope.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope.md](../../L3-formula-scope.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-02_L3-formula-scope_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/developer-t318-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/independent-t318-initial.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/independent-t318.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/sampling-scope.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope.md:101`,
blob `bc6a26264d0392bd35d020cd42fb049e90b8f8df`:

````text
Exit 0; [independent checker](L3-formula-scope/independent_t318.py), [execution log](L3-formula-scope/independent-t318.log): **ALL EXACT ASSERTIONS PASS**. The checker imports no developer or reviewer code and uses exact SymPy rational matrices and separately implemented sparse polynomial arithmetic. It uses fixed monomials and dF directly, rather than the developer's Cholesky finite differences. Rational affine triangular node sets n=1,2,3 have deliberately nonunit masses 6,21,55. It checks every moment coordinate, all remainder node values and jets, sign, top-degree cancellation, low commutator rows, radial cancellation, normalization covariance, the arbitrary-L identity after changing only highest-degree moments, and equality of the derivative and quadratic-generator row spaces. The derivative matrices have shapes 1x10, 3x21, 6x36, with ranks=dim F=dim S1 equal to 1,3,6. Exact finite Hankel basis ranks n=1,...,8 are 1,3,6,10,15,21,28,36, testing the symmetrization factors. These are finite sanity checks; the all-n theorem rests on the analytic proof above.
````
