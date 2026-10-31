# Standalone campaign allocation ledger

Allocation owner: root Codex orchestrator. Branch `codex/charter-unisolvence-20261031`. Rules/base `d36722823441dc40c6e19d69a174459348dd309c`. PR preparation refresh: `git fetch origin main` returned the same SHA, and GitHub open-PR API returned `[]`. No other active reservations or scientific IDs in base. No batch integration or squash rehearsal is applicable (one PR only). Only root allocates; no concurrent writer owns IDs.

Reserve PD-T001–PD-T012, PD-N001, LIT-001–LIT-041, and IDEA-001–IDEA-051 for retained source/local candidates. Exact provisional-to-final mapping is in [final-id-map.json](final-id-map.json) and ../../ID_CROSSWALK.md. Scientific source checkpoints: U0 `4f3d247c64d8c74a923b50f5ff575f83b5401cb8`, input code `5123a32774110e9290c42bc1cf3c6838ee6c3d35`; U1 `d5a5efbc6228ea21ef38b438ef976260f90ea83e`. Final-ID/path substitution is mechanical and will have an explicit content impact check against these checkpoints.

| Namespace | Range | Owner | Content |
|---|---|---|---|
| PD-T | 001–003 | root | U1 odd characteristic, all characteristic, kernel consequence |
| PD-T | 004–011 | root | U0 five proofs, two measured records, open extensions |
| PD-T | 012 | root | independently proved universal linear-code bounds |
| PD-N | 001 | root | characteristic-2 failure of original iff necessity |
| LIT | 001–041 | root | imported/screened source statements, coverage retained |
| IDEA | 001–051 | root | all active, refuted, equivalent and deferred source candidates |

No IDs are recycled. This draft PR will request Claude audit, not merge approval.
