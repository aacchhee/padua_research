# Complete-certificate XZ representation

Verification/provenance procedure; no mathematical claim or proof status.

The complete count certificate remains one JSON document. For the new n7/n8 cases, a single XZ/LZMA2 archive contains its exact original decoded bytes. No node, leaf, pattern, edge or corner data is partitioned into another file. The separate global object remains the additional value certificate used since n4. Prior tracked n3–6 evidence is unchanged.

## Actual packaging checks

The n7 boundary-plus-partial-tree fixture was3,302,464JSON bytes:682,665gzip bytes and332,548XZ bytes, with exact decoded-byte equality (1.59s). The mechanical repacker also roundtripped the already retained n6 count/global data into temporary files:414,031gzip bytes became261,288XZ bytes. Both an initial execution and an identical repeat exited0; decoded bytes matched, the only changed global field value was certificate_sha256, all other global field values matched, and the repacker source was unchanged. This was packaging validation only; it did not rerun or change the closed n6 proof. Small receipt: outputs/a5_repack_smoke.json.

## Frozen helper and pipeline

Helper: code/a5_repack_certificate.py,6378bytes,SHA256 e1cc7fe03b69d5542fabf9d2bc8052e71bf7c33398f68d23543d2610241c7332. Python standard-library gzip/lzma/hashlib/json only. XZ uses preset9 extreme and an SHA256 container checksum. The helper preserves the exact decoded JSON bytes and changes only the global object's raw-certificate binding value; JSON layout may be reencoded. Its receipt records original/packed/raw-global/rebound-global identities, decoded-byte identity and source stability. It claims no count/global verification.

After a complete developer n7 raw artifact, from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n7_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_n7_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_n7_global.raw.json
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_repack_certificate.py topics/padua-proof-attempts-2-20261101/outputs/a5_n7_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_n7_certificate.json.xz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n7_global.raw.json --global-output topics/padua-proof-attempts-2-20261101/outputs/a5_n7_global.json --receipt topics/padua-proof-attempts-2-20261101/outputs/a5_n7_repack.json
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n7.py topics/padua-proof-attempts-2-20261101/outputs/a5_n7_certificate.json.xz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n7_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n7_full.json
```

These are next-stage commands until the case receipt records their actual execution. For n8 use its own modules/paths; each different executor uses its own original raw artifacts and a5_independent_nN output prefix. Source/global producers are unchanged. The repacker checks the original global binding before changing it. The final independent checker computes its binding from the actual XZ bytes and verifies every mathematical predicate on the entire decoded certificate. Pair the XZ archive with the rebound global, never the original gzip-bound global.

## Identity, retention and limits

- Checksum/roundtrip identity establishes packaging integrity; the separate complete checker establishes mathematical validity.
- Actual independent execution records pin producer inputs at their stage and later repacker/checker inputs at their own stage. Unused checker performance revisions do not invalidate an unchanged producer.
- Keep original raw discovery intermediates locally with their identities. The retained XZ archive is self-contained and sufficient for complete verification. Essential published evidence is the whole archive, matching global, checker code/results and execution receipts. Duplicate independently generated full archives are retained only within the aggregate budget; their actual own output/checker receipts and mathematical comparison remain explicit.
- The helper refuses a packed archive over1,000,000bytes and refuses to replace any different existing destination. It can reuse identical bytes. All committed generated evidence must also fit5,000,000bytes overall. No splitting, deletion of historical evidence or invented cold-storage destination is used.
- Gzip and raw JSON inputs remain supported by the new verifier readers. XZ decoding changes the outer byte representation only. All exact Sturm, sign, node, whole-leaf, root, boundary and value predicates are unchanged.
