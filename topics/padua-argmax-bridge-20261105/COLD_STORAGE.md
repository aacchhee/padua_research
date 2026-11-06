# Bridge working output and pending archive delivery

No archive is delivered or staged at AC's Windows destination. The authorized
destination is `Downloads\padua\cold_storage\padua-argmax-bridge-20261105\`.
Actual files are only local in `local-output/argmax-bridge-20261105/`.

[cold-storage.json](cold-storage.json) records actual local paths, byte sizes
and SHA-256 identities in `pending_local.files`. Standard `entries` is empty:
there is no archived or Git-backed bulk entry and no verified external
retrieval. Small committed receipts are the evidence records; local binary,
trace, sample and timing files are regenerable working output.

| Group | Frozen command and result record | Local output |
|---|---|---|
| B0 | [Independent replay](independent-checks-b0.md), [receipt](evidence/b0-replay.json): n24 exact mathematical payload and independent checker acceptance; n32 incomplete pilot deterministic counts reproduced | b0/ |
| B1 | [Margin anatomy](margin-anatomy.md), [receipt](evidence/b1-margins.json): finite floating diagnostics, source/raw hashes, finite raw values and count reconciliation | b1/ |

The initial inventory records 33 present files, 4,702,615 bytes, read back and
hashed in this sandbox. It includes the historical frozen prose pins used to
resolve the B0 preflight mismatch. The receipt/source commit gives all scripts;
the historical source object may require `git fetch origin
7d394fd9c45495a32ff91961a5d91942aa59e250` in a later clone. No source
credential or private-paper content is stored.

Executed `python tools/cold_storage.py plan
topics/padua-argmax-bridge-20261105`: zero tracked generated files above 16KiB
need relocation at this checkpoint. The tool's historical Git-blob export
workflow does not archive never-committed local files; the inventory is a
pending-local record, not evidence of Windows delivery.

Regenerate from the exact commands in the linked records, with Python/NumPy,
C/C++ compilers and GMP. Use fresh work directories to retain original outputs.
Scientific mathematical fields and deterministic non-CPU-capped pilot counts
are the reproduction targets; old timing bytes and binaries are not promised.
No proved bridge result depends on unique local sample or timing bytes.

The sandbox is the current custodian. Durable retention, physical delivery and
cross-session retrieval remain pending. Before accepting a delivery, rehash the
delivered files against the recorded inventory and record the actual path and
independent retrieval/verification. Do not infer retention from a past receipt.

## D01 record-preservation addendum —2026-11-06

AuditF5's three available original artifacts are copied/readback-verified
in `local-output/argmax-bridge-20261105/d01-record-preservation/`. Their
path/bytes/SHA256 rows are now in `pending_local.files` of cold-storage.json;
the group links response-01 F5. These remain ephemeral working copies,
not delivered archives or externally retrievable evidence. The original
C03postcheck-script limitation is canonical in response-01 F5. No
mathematical execution or retrospective script reconstruction is claimed.
