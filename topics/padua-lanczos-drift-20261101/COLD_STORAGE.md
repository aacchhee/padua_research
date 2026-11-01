# Cold-storage manifest — padua-lanczos-drift-20261101

Intended AC destination: `C:\Users\andreyac\Downloads\padua\cold_storage\padua-lanczos-drift-20261101\`.
**Windows delivery remains pending:** no bridge exists. The rows below describe
actual workspace staging, not a receipt from that destination.

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
