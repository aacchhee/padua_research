# Cold-storage manifest — lattice-unisolvence-20261031

AC's chosen destination: `C:\Users\andreyac\Downloads\padua\cold_storage\lattice-unisolvence-20261031\`.

The archive below is actually staged in the cloud workspace. Windows delivery/receipt is unconfirmed; the parent charter's separate waiver is not claimed as a receipt here. All essential small scientific code/evidence is also committed, so this storage item does not leave a computer-proof dependency unavailable.

| File | Actual staging path | Bytes | SHA-256 | Source / generating command | Checker |
|---|---|---:|---|---|---|
| lattice-evidence.zip | `/workspace/scratch/lattice-unisolvence-20261031/lattice-evidence.zip` | 832029 | `7b173b14f12eb73661e165e544f189a42faa13c08d94e957126a08eb7b7ba53a` | Source-head `61dcbe5e5a9a020810c0b8a9be974e1eba98f0ca` plus exact per-file hashes/Git blobs in the enclosed scientific audit-targets.json; `python tracks/lattice-unisolvence/code/prepare_evidence.py --archive /workspace/scratch/lattice-unisolvence-20261031/lattice-evidence.zip` | ZIP CRC and extracted identities PASS in cold-check.json |

## Committed output and identities

[audit-targets.json](audit-targets.json) records every retained source/evidence file's SHA-256, bytes and Git blob identifier. Its self-exclusion and bookkeeping exclusions avoid a recursive hash dependency; exact recorded file bytes, not an assumption that every working file already existed at source_head, govern review. [manifest-check.json](manifest-check.json) records the executed content check; [cold-manifest.json](cold-manifest.json) identifies the staged ZIP. The archive contains its own scientific snapshot manifest, allowing verification after extraction. The final repository manifest may additionally pin the later protocol-review envelope; the scientific identities agree. Protocol review remains committed separately and is excluded from the scientific ZIP to keep the dependency one-way. No third-party fulltext is included.

## Regeneration and retrieval

From the repository root, regenerate the bundle using the command above. ZIP metadata may vary on regeneration; compare extracted file identities, not an assumed byte-identical future ZIP. Retrieve the existing staged ZIP through the workspace file link or copy it to AC's selected Windows folder. Extract into a fresh directory, then run `python tracks/lattice-unisolvence/code/verify_artifacts.py topics/lattice-unisolvence-20261031/audit-targets.json --root <extracted-root>` from the extracted root. SHA-256 of the downloaded ZIP must first equal the manifest value. Verification needs ordinary Python3 only; no secret, external account or network access. No Windows execution is claimed.

The scientific computations are reproducible from committed checkers; exact Python/NumPy/SciPy/SymPy versions and commands appear in the direction evidence and AUDIT_HANDOFF.md. The present archive is a compact review/retrieval bundle, not a claim to be a complete Git checkout.

## Retention

AC is the permanent archive custodian once transferred to the chosen folder. The cloud path is temporary session staging with no promised long-term retention. No archival deletion was performed. Pending receipt remains explicit and does not imply that the required Claude audit or whole batch is merge-ready.
