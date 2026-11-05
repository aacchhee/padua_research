# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-02/L2

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
| `topics/bivariate-lanczos-20261031/audit-02/L2/independent-staircase.log` | 1551 | `3cfbdb2e7d306c4753511bf344c6d16fd7e16f775decc1780644e6c753d44f22` | `8c5a2475a671e6b8f42a18208e5b652fe142fd00` |
| `topics/bivariate-lanczos-20261031/audit-02/L2/qualification-checks.log` | 366 | `f3da5186728216624e1622a1a0b72a1f1feb9e0e5d418ee3211b3d167f9cac1c` | `3e2eca6be95d7c092f9019a01c12c697c872fb3b` |
| `topics/bivariate-lanczos-20261031/audit-02/L2/staircase-rerun.log` | 3096 | `16d21c1e4e691afb5b63205550e3af8b2039c337e97daec4f87685b499f69a32` | `41f47fcf6c946470100731ee5699cf3da374a657` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-02/L2.md](../../L2.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-02/L2.md](../../L2.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-02/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-02_L2_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-02/L2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-02/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-02/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-02/L2/independent-staircase.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-02/L2/qualification-checks.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-02/L2/staircase-rerun.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-02/L2.md:82`,
blob `a5903820c70a0f1e8e3c9aa5127054eb804cb332`:

````text
| Own `independent_staircase.py` → [log](L2/independent-staircase.log) | All selections n1–6 and all staircases n7–14, maximal preceding-column windows; no missing-order dependencies or support violations. |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-02/L2.md:31`,
blob `a5903820c70a0f1e8e3c9aa5127054eb804cb332`:

````text
Required correction: retain the universal unnormalised inequality, restrict the quotient implication to `||A||>0`, or explicitly set a zero operator's normalized defect contribution to zero. Under U(n), n≥1, the operators are nonzero and the intended part(c) applications are unaffected. [qualification_checks.py](L2/qualification_checks.py) checks this simple construction; [log](L2/qualification-checks.log). This is a domain omission, not a counterexample to the drift inequality.
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-02/L2.md:85`,
blob `a5903820c70a0f1e8e3c9aa5127054eb804cb332`:

````text
| Own `qualification_checks.py` → [log](L2/qualification-checks.log) | Zero-operator quotient issue and conditioning example above verified; neither is a counterexample to the exact projector inequality. |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-02/L2.md:81`,
blob `a5903820c70a0f1e8e3c9aa5127054eb804cb332`:

````text
| `l2_audit01_staircase.py` → [log](L2/staircase-rerun.log) | All-selection enumeration n2–6: counts2,4,8,16,32 satisfying(C), all staircases; no cycles/support failures; no disagreements with old checker where compared. All staircases n7–13 and random preceding-column subsets n2–10 pass. |
````
