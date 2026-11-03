# Gated campaign packaging

Current-storage correction, 2026-11-02: the development-boundary wording
below is historical. AC subsequently moved large regenerable outputs off
the head. Their exact historical blobs and identities are in
[cold-storage.json](../cold-storage.json). The current read-only integrity
checker verifies all archived objects without restoring them; one current
integrity manifest is retained under handoff07's explicit exception.
The separate cold-storage tool has unresolved [protocol findings](../audit-02-cold-storage.md)
and must not be used to overwrite an active record while awaiting repair.

Direction1 round1's full developer JSON is committed losslessly as outputs/gated/d1_screen_r01.json.gz (81,843bytes, SHA2568b57766f8e0251cc6bbd2b772888846ba475f0c01025e17cdf124a90d6c0fc1d). Its decompressed payload is860,021bytes, SHA25615c9d29a3d2b166ee54dc8a91fe7bff4c117cc85dc99184fa7bc7640a888e9ef. The original developer command wrote the .json path; after independent replay the uncompressed working copy was moved to /tmp/padua-gated-d1-screen-r01-developer.json. Decompress the committed gzip for retrieval; no external cold storage is needed. Gzip used mtime0 for deterministic packaging. This is compression of one artifact, not file splitting.

The independent checker writes its full replay to/tmp and commits only its compact content/comparison receipt. Timing/argv and the documented preregistration-note completion hash are excluded from numerical equality checks. The original output and code identities remain explicit. Future rounds should retain small essential evidence to keep total topic outputs below5MB and each committed generated file≤1MB.

At the final6/2/1-round output boundary, evidence-manifest.json is refreshed by code/part3/check_evidence.py (formatv2, preserving original part3 and gated input heads). It covers topic files and the topic-owned results, excluding handoffs/manifest/packaging receipt to avoid metadata cycles. The receipt at outputs/part3/packaging-validation.json records the executed file/hash/size/JSON checks. This is integrity validation; mathematical certificate acceptance comes from the separate exact checkers and their actual independent replays.

D3's13561-byte certificate and small developer checker receipt are essential finite-comparison evidence. The independent full regenerated certificate/checker output remains under/tmp, with compact outputs/gated/check_d3_r01_receipt.json pinning sources, exact comparisons, controls, commands and output hashes. No cold-storage-only dependency or archival transfer is claimed. The recorded source/command checkpoints and embedded code hashes, rather than the eventual publication commit's date, identify each run's actual inputs.

## Unified T1 reconstruction — 2026-11-02 (F1)

From repository root:

```sh
python -B topics/padua-argmax-alln-20261101/code/part3/reconstruct_t1.py --output /tmp/padua-restored-t1.json
```

This reads the frozen historical component blobs at1cecd68 and reconstructs
one complete producer-layout artifact, without restoring repo files or
creating new per-degree fragments. It verifies the archived component
hashes and every short/full profile relationship before writing. The
output is1,342,719bytes, SHA-256
`bfb0acd697bfe8530a9b8441130c400f1a3601342277ab0a0c77d2cfd6cfcb90`.
The complete input identities and analysis-invariance comparison are in
[t1-restoration.json](../response-support/t1-restoration.json).

Claude's independent raw replay is separately identified in audit-01 by
SHA-2564d7792e69f2c7a7237e03e1343e0c65feddbdeb0a034c04878202b4e37cfe7c6.
Its raw scratch bytes were not committed; reconstruction does not claim
that replay's timing identity. The historical component bytes and the
unified developer-layout output above are byte-exactly retrievable by
the committed recipe. No new measurement or lossless-archive equivalence
to an unavailable replay byte stream is inferred from a hash alone.

The revised analyzer keeps full T1 input intact, creates no split outputs,
and produces the same978summary leaves apart from the one unified-file
metadata pointer. It still requires T2/T3/T4 inputs to reproduce their
summary sections; the cold-storage audit asks Claude to correct the old
manifest commands' omitted prerequisites.
