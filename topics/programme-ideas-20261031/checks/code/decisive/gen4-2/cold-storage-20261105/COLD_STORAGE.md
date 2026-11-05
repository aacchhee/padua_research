# Cold-storage manifest — topics/programme-ideas-20261031/checks/code/decisive/gen4-2

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
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_argmax.out` | 8918 | `9d500032d8d53583c4644fd2d554bf487c3fd5472bb21bd892ec4f70a9c6f548` | `09f17d251ee4f06e2bb9ec02817a8bd1bbc323d2` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_tail.out` | 1463 | `d863e8f2861503702831c4ab1eac0a629b4b4a39b05dc9cb9fdd204188d36492` | `778c2328901f314591ea2bbe8819eb5ebbffe53b` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_halfshift.out` | 3534 | `0f65bd19274fe11b84045061c30b0243eed5fd1b1402c5acd82612e83c99b186` | `04372783916f598de1255ce13d872bc0ec3666dc` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_identify.out` | 7379 | `7dfe7db98f26fef0ab68da6b5afb1857c3cefd0efc182bed50e9a426d8b150ed` | `5f848691829db4c5e6a412d3dcb254d0d6a17f60` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_identify2.out` | 1956 | `e8ba834388e9e0b29a5a46d2f5f853c83f42eae3fb18b8ad1517db675032f1a2` | `ba5d0a9e4b81390cab1af20bb2e040d1ed27f171` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_odd.out` | 4475 | `fc809dada19f75e3cea51ae6a3c6ec0f0d2c7b76281f6afa06d9da77e7a4c444` | `cad6e6cca28cddc57d0c78ee405493cb9233d66b` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_onepage.out` | 7028 | `4b0c81bd0dcc5f87447769b91404637ec5c4b9a815bcdd90a07be1b5ee9d5df6` | `382268c152cb51cfb549b2541b1179b590b106e5` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_certify.log` | 14474 | `4eeb37aa8848202988ebd660b0a332e8812f2adb616d0dacc56cfa1140e7f3a8` | `47ccf67917685160d463d18a954dfa241793da47` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_certify.out` | 12480 | `637303c5defbaac0fa105c80d79b9f69c8e34922af39f1607924aa2468516b06` | `073b957d1af058fad2793fff586f4b1f1fa2b31e` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_validate.out` | 7903 | `1da3aa3b434eb93cfb8041e87218401fa785c245ac40f84b096ad1a65b042e1e` | `10a6eadaa8025a2a5d815067c81ac1f709530cb1` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/programme-ideas-20261031/checks/decisive-gen4-2.md](../../../../decisive-gen4-2.md)
- [topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md](../../../../../theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md)

Short scientific summaries:
- [topics/programme-ideas-20261031/checks/decisive-gen4-2.md](../../../../decisive-gen4-2.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/programme-ideas-20261031/checks/code/decisive/gen4-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_programme-ideas-20261031_checks_code_decisive_gen4-2_cold-storage-20261105 --manifest topics/programme-ideas-20261031/checks/code/decisive/gen4-2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/programme-ideas-20261031/checks/code/decisive/gen4-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/programme-ideas-20261031/checks/code/decisive/gen4-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_argmax.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_tail.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_halfshift.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_identify.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_identify2.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_odd.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t2_onepage.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_certify.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_certify.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_validate.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/checks/decisive-gen4-2.md:38`,
blob `2a128194a6b6da260de123c0458079049b368766`:

````text
### T1 — corner argmax (`t1_argmax.py`, `t1_argmax.out`, `t1_tail.py`, `t1_tail.out`, `t1_argmax.json`)
````

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/checks/decisive-gen4-2.md:62`,
blob `2a128194a6b6da260de123c0458079049b368766`:

````text
### T2 — one-page test (`t2_onepage.py/.out`, `t2_identify.py/.out`, `t2_odd.py/.out`, `t2_halfshift.py/.out`, `t2_identify2.out`)
````

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/checks/decisive-gen4-2.md:70`,
blob `2a128194a6b6da260de123c0458079049b368766`:

````text
### T3 — certified counting (`t3_certify.py`, `t3_degenerate.py`, `t3_certify.out/.log`, `t3_maxima.json`, `t3_validate.py/.out`)
````

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md:50`,
blob `d4f35e947263b0b134c2f26f58075bfaa26ebb20`:

````text
`checks/code/decisive/gen4-2/t3_certify.py`, `t3_degenerate.py`, `t3_validate.py` with `t3_certify.out/.log`, `t3_maxima.json`, `t3_validate.out` (frozen at `614709d`). Audit replays and counterchecks: `audit-support/proposal-rerun.*`, `proposal-independent.*`, `proposal-degenerate-counterexample.*`.
````
